"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from flask import Flask, Response, request, jsonify
from psycopg2.errors import ForeignKeyViolation

from database import get_db_connection

app = Flask(__name__)
conn = get_db_connection()


@app.route("/", methods=["GET"])
def index() -> Response:
    """Returns a welcome message."""
    return jsonify({
        "title": "Clown API",
        "description": "Welcome to the world's first clown-rating API."
    })


@app.route("/clown", methods=["GET", "POST"])
def get_clowns() -> Response:
    """Returns a list of clowns in response to a GET request;
    Creates a new clown in response to a POST request."""

    order = request.args.get("order", "desc")
    if order and order.lower() not in ["asc", "desc"]:
        return jsonify({"error": "Invalid order parameter"}), 400

    if request.method == "GET":
        with conn.cursor() as cur:
            cur.execute(
                f"""SELECT clown_id, clown_name, speciality_name,
                        AVG(rating) AS average_rating,
                        COUNT(rating) AS num_of_ratings
                    FROM clown
                    JOIN speciality USING(speciality_id)
                    LEFT JOIN review USING(clown_id)
                    GROUP BY clown_id, clown_name, speciality_name
                    ORDER BY average_rating {order}""")
            data = cur.fetchall()
            for clown in data:
                if clown["num_of_ratings"] == 0:
                    del clown["num_of_ratings"], clown["average_rating"]
            return jsonify(data)
    else:
        data = request.json
        try:
            if "clown_name" not in data or "speciality_id" not in data:
                raise KeyError("New clowns need both a name and a speciality.")
            if not isinstance(data["speciality_id"], int):
                raise ValueError("Clown speciality must be an integer.")

            with conn.cursor() as cur:
                cur.execute("""INSERT INTO clown
                                 (clown_name, speciality_id)
                               VALUES (%s, %s)
                               RETURNING *;""",
                            (data["clown_name"], data["speciality_id"]))
                new_clown = cur.fetchone()
                conn.commit()
            return jsonify(new_clown), 201
        except (KeyError, ValueError, ForeignKeyViolation) as err:
            print(err.args[0])
            conn.rollback()
            return jsonify({"message": err.args[0]}), 400


@app.route("/clown/<int:clown_id>", methods=["GET"])
def get_clowns_with_id(clown_id: int):
    """Returns the clown's details in response to a GET request"""
    with conn.cursor() as cur:
        cur.execute(
            """SELECT clown_id, clown_name, speciality_name
                FROM clown
                JOIN speciality USING(speciality_id)
                WHERE clown_id = %s;""", (clown_id,))
        cur.close()

        data = cur.fetchall()
        if not data:
            return jsonify({"error": "No clowns found"}), 404

        return jsonify(data)


@app.route("/clown/<int:clown_id>/review", methods=["POST"])
def create_review(clown_id: int):
    """Give rating for a clown"""
    data = request.json
    if not data:
        return jsonify({"error": "Empty request"}), 404

    rating = data.get("rating")
    if not rating:
        return jsonify({"error": "Rating isn't a key parameter"}), 400

    if not isinstance(rating, int):
        return jsonify({"error": "Rating isn't an integer"}), 400

    if rating < 1 or rating > 5:
        return jsonify({"error": "Rating isn't within range"}), 400

    with conn.cursor() as cur:
        cur.execute(
            """INSERT INTO review (clown_id, rating)
            VALUES (%s, %s);""", (clown_id, rating))
        cur.close()
        conn.commit()

    return jsonify(
        {"message": f"""Clown rating of {rating} added to clown id {clown_id}"""}), 201


if __name__ == "__main__":
    app.run(port=8080, debug=True)

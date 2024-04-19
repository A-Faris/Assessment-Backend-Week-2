# Clown API

## Scenario

You work for Clowntopia, the UK's leading provider of clowns and clown-related accessories. As a new developer, you have been tasked with accessing an existing, unfamiliar codebase - the Clown API - and making a series of changes/additions to the code.

Clowntopia, despite the name, prides itself on the highest possible standards of software development and quality assurance. While making your changes, you should always be thinking about keeping your code clean, efficient, and organised.

Please ensure you do every step below carefully. Not doing so will mean we can't assess your work and **will result in a score of zero**.

1. Create a repo named exactly `Assessment-Fundamentals-Week-1`
2. Invite your coaches to it (they'll let you know they Github usernames)
3. Push all the code in this folder to your created repository
4. On your created repo, click on `Actions` in the top menu bar
   - Next, click on `I understand my workflows, go ahead and enable them`
5. Run `pip3 install -r requirements.txt` to install the required libraries
6. Run `psql postgres -f setup.sql` to create and populate the database
7. Complete the assessment
8. Commit & push your code regularly

## Development

Run the server with `python3 app.py`; you can access the API on port `8080`.

## Quality assurance

Check the code quality with `pylint *.py`.

Run tests (including the full coverage report) with `pytest --cov-report term-missing --cov .`

## API documentation

The clown API is JSON-based; **all responses should be in JSON format** only.

| Route    | Method | Response                                   |
| -------- | ------ | ------------------------------------------ |
| `/`      | `GET`  | Returns a welcome message                  |
| `/clown` | `GET`  | Returns a list of clowns and their details |
| `/clown` | `POST` | Creates a new clown in the database        |

## Tasks

Tasks can be found in [here](./tasks.md)


## Tasks

Clowntopia's corporate motto is "A job isn't done until it's done well". For a task to count as completed, the following must be all be true:

1. All the task requirements are met
2. Likely errors are handled appropriately
3. The documentation is up-to-date
4. The `pylint` score remains above 8
5. All tests pass

For efficiency reasons, as much data processing should be done in SQL as possible.

### Task 1

Update the `/clown` endpoint so that it returns the following data for each clown:

- id
- name
- name of speciality

### Task 2

Create a new endpoint - `/clown/[id]` - that returns the following data for the matching clown:

- id
- name
- name of speciality

Return appropriate messages/status codes if the clown id is invalid, or if there is no matching clown.

### Task 3

Add a new endpoint - `/clown/[id]/review` - that accepts only `POST` requests. When provided with appropriate data, this endpoint should create a new `review` in the database for a specific clown.

Only rating scores from 1 to 5 are valid.

Return appropriate messages/status codes if invalid data is provided.

### Task 4

Add an `order` query parameter to the `/clown` endpoint. Return clowns in ascending or descending order by average rating based on this parameter.

The order should default to `descending`.

Return appropriate messages/status codes if invalid `order` is provided.

### Task 5

Update both the `/clown` and `/clown/[id]` endpoints so that they also return data on

- the average rating for each clown
- the number of ratings for each clown

If a clown has no ratings, do not include these keys/values in the output.

### Task 6

Add the following tests to the `test_app.py` file

1. Test that checks that `/clown/[id]` returns the data for a clown with that `id`
2. Test that checks that `POST`ing to `/clown/[id]/review` without a rating returns an error
3. Test that checks that `/clown` endpoint includes `name` and `speciality`

You must not connect to your database in your tests. All database connections or surrounding functions must be mocked.

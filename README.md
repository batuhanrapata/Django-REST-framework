# Django-REST-framework
Rest Framework CRUD api with PostgreSQL with Login module

This is a code snippet written in Python for a simple user management system API. It includes several classes that handle user creation, deletion, and updating, as well as a health check endpoint and a login endpoint.

The UserCreate class is responsible for creating a new user. It accepts POST requests with user data, validates the data, and then creates a new user if the data is valid. It also hashes the user's password before saving it to the database for security purposes.

The UserViewSet class is used for retrieving a list of all users or a specific user by ID, and for updating user data.

The UserDelete class is used to delete a user by ID.

The UserUpdate class is used to update user data by ID.

The HealthCheck class is a simple endpoint that returns a status code of 200 OK when called, indicating that the API is functioning correctly.

The Login class handles user login requests. It accepts POST requests with a username and password, checks if the user exists, and then checks if the hashed password matches the user's stored password using a verify() function. If the passwords match, the API returns a 200 OK status code, indicating a successful login. Otherwise, it returns a 400 Bad Request status code.

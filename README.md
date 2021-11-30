# todolist-backend

A REST API for a `Todo list` written in Python using Flask

## Libraries used:

-   Marshmallow - For serializing/deserializing
-   Flask - For serving the API

## Features:

-   getTasks (`api/v1/task`) - GET - Returns a list of tasks
-   addTask (`api/v1/task`) - POST - Adds a new task to the list of tasks

## TO DO (pun intended...):

-   Add a backend DB to hold the tasks
-   Add `due date` and `created date` to facilitate ordering on the front end
-   Create `User` class and fields
-   Associate a `User` with a `Task`
-   Add Authentication using JWT

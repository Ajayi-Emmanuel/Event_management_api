# Event Planner API

This is a Django-based API for managing users and events. It includes features for user authentication, creating, listing, deleting, updating, viewing upcoming events and filtering events. The API supports filtering upcoming events and preventing duplicate entries.

## Features

- **User Authentication**: Registration, login, and JWT-based authentication.
- **Event Management**: Users can create, view, update, delete and list events.
- **Duplicate Prevention**: Events with the same title and date cannot be created.
- **Filter Events**: Users can filter upcoming events based on event details.


### Prerequisites

Make sure you have the following installed:

- Python 3.7+
- Django 3.2+
- Django REST Framework
- Django Filter
- djangorestframework-simplejwt

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Ajayi-Emmanuel/Event_management_api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Event_management_api
    ```

3. Create a virtual environment:

    ```bash
    python -m venv .venv
    ```

4. Activate the virtual environment:

    ```bash
    # On Windows
    .venv\Scripts\activate

    # On macOS/Linux
    source .venv/bin/activate
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run database migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser (admin) for the project:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

Your API should now be running at `http://127.0.0.1:8000/`.

## User App

The **User App** is responsible for managing user authentication and registration.

### Features

- User registration
- User login
- JWT authentication
- Profile management

### How It Works

1. **Registration**: Users can register by providing their `username`, `email`, and `password`. After registration, they can authenticate themselves using the JWT authentication system.
2. **Login**: After successful registration, users can obtain a JWT token by logging in using their email and password.
3. **JWT Authentication**: The API uses JWT to authenticate users and protect certain routes (such as event creation).

### User API Endpoints

- **Register User**: `/api/users/register/` (POST)
    - Request Body:

    ```json
    {
      "username": "user1",
      "email": "user1@example.com",
      "password": "password123"
    }
    ```

- **Login User**: `/api/users/login/` (POST)
    - Request Body:

    ```json
    {
      "email": "user1@example.com",
      "password": "password123"
    }
    ```

- **Profile**: `/api/users/profile/` (GET) - Requires authentication.

### Example Request Body for User Registration:

```json
{
  "username": "JohnDoe",
  "email": "john@example.com",
  "password": "password123"
}
```

## Event App

The **Event App** is responsible for managing events. Users can create, view, list, and filter events. Each event is tied to the user who created it.

### Features

- Event creation
- List all events
- Update an event
- View an event
- Delete an event
- Filter upcoming events
- Prevent duplicate events based on title and date

Here’s how **Update**, **Delete**, and **View Specific Events** functionality works in the Event app:

### How It Works

1. **Event Creation**: Authenticated users can create events. Each event has fields like `title`, `description`, and `date_time`. The user who creates the event is automatically set as the organizer.
   
2. **Duplicate Prevention**: An event with the same `title` and `date_time` cannot be created. If a duplicate is detected, an error message will be returned.

3. **Upcoming Events**: Events that have not yet occurred can be listed and filtered.

4. **Update Event**: 
    - Authenticated users can update the details of an event they created.
    - The user must provide updated fields such as `title`, `description`, and `date_time`. 
    - The API checks if the event exists and if the user making the request is the organizer of the event.
    - If the user is not the organizer, they are not authorized to update the event.
    - **Duplicate prevention** still applies when updating the event (i.e., no other event can have the same `title` and `date_time`).

5. **Delete Event**:
    - The event can only be deleted by the user who created it (the organizer).
    - If the user is the organizer, they can permanently remove the event from the database.
    - The deletion endpoint requires the event's ID, and an error will be returned if the event does not exist or if the user is not the organizer.

6. **View Specific Event**: 
    - Any user, authenticated or not, can view the details of a specific event by providing the event ID.
    - The endpoint fetches all event details, including the `title`, `description`, `date_time`, and the `organizer`.
    - This view is public, meaning anyone can view event details without authentication.

### Event API Endpoints

- **List All Events**: `/api/events/` (GET)
- **Create a New Event**: `/api/events/` (POST) - Requires authentication
- **Retrieve an Event**: `/api/events/{id}/` (GET)
- **Update an Event**: `/api/events/{id}/` (PUT)
- **Delete an Event**: `/api/events/{id}/` (DELETE)
- **List Upcoming Events**: `/api/upcoming-events/` (GET)


### Example Scenarios for Event Endpoints

1. **Create Event**
   - **Endpoint**: `/api/events/` (POST)
   - **Requires Authentication**: Yes
   - **Request Body Example**:
     ```json
     {
       "title": "Birthday Party",
       "description": "Celebrating John's birthday.",
       "date_time": "2024-10-15T18:00:00Z"
     }
     ```
   - **Successful Response**:
     ```json
     {
       "id": 1,
       "title": "Birthday Party",
       "description": "Celebrating John's birthday.",
       "date_time": "2024-10-15T18:00:00Z",
       "organizer": 1
     }
     ```
   - **Error Response** (Duplicate Event):
     ```json
     {
       "non_field_errors": [
         "The fields title, date_time must make a unique set."
       ]
     }
     ```

2. **List Upcoming Events**
   - **Endpoint**: `/api/events/upcoming/` (GET)
   - **Requires Authentication**: No
   - **Response Example** (If there are upcoming events):
     ```json
     [
       {
         "id": 1,
         "title": "Birthday Party",
         "description": "Celebrating John's birthday.",
         "date_time": "2024-10-15T18:00:00Z",
         "organizer": 1
       },
       {
         "id": 2,
         "title": "Team Meeting",
         "description": "Discussing project updates.",
         "date_time": "2024-10-20T10:00:00Z",
         "organizer": 2
       }
     ]
     ```

3. **View Specific Event**
   - **Endpoint**: `/api/events/{id}/` (GET)
   - **Requires Authentication**: No
   - **Response Example** (For event with ID 1):
     ```json
     {
       "id": 1,
       "title": "Birthday Party",
       "description": "Celebrating John's birthday.",
       "date_time": "2024-10-15T18:00:00Z",
       "organizer": 1
     }
     ```
   - **Error Response** (Event Not Found):
     ```json
     {
       "detail": "Not found."
     }
     ```

4. **Update Event**
   - **Endpoint**: `/api/events/{id}/` (PUT)
   - **Requires Authentication**: Yes
   - **Permissions**: Only the organizer can update the event.
   - **Request Body Example**:
     ```json
     {
       "title": "Updated Birthday Party",
       "description": "Celebrating John's birthday with more friends.",
       "date_time": "2024-10-15T20:00:00Z"
     }
     ```
   - **Successful Response**:
     ```json
     {
       "id": 1,
       "title": "Updated Birthday Party",
       "description": "Celebrating John's birthday with more friends.",
       "date_time": "2024-10-15T20:00:00Z",
       "organizer": 1
     }
     ```
   - **Error Response** (Unauthorized):
     ```json
     {
       "detail": "You do not have permission to perform this action."
     }
     ```

5. **Delete Event**
   - **Endpoint**: `/api/events/{id}/` (DELETE)
   - **Requires Authentication**: Yes
   - **Permissions**: Only the organizer can delete the event.
   - **Successful Response** (Event Deleted):
     ```json
     
     ```
   - **Error Response** (Unauthorized):
     ```json
     {
       "detail": "You do not have permission to perform this action."
     }
     ```
   - **Error Response** (Event Not Found):
     ```json
     {
       "detail": "Not found."
     }
     ```


### Duplicate Event Error

When a user attempts to create an event that already exists (same title and date), the API will return the following error:

```json
{
    "error": "An event with this title and date already exists."
}
```

## Filtering Events

You can filter upcoming events by title or date using query parameters.

### Example Filters

- **Filter by Title**:

    ```bash
    GET /api/upcoming-events/?title=Workshop
    ```

- **Filter by Date**:

    ```bash
    GET /api/upcoming-events/?date_time=2024-10-01T00:00:00Z
    ```

- **Filter by Title and Date**:

    ```bash
    GET /api/upcoming-events/?title=Workshop&date_time=2024-10-01T00:00:00Z
    ```

### Testing with Postman

1. Open Postman and set the request method to **GET**.
2. Use the `/api/upcoming-events/` endpoint.
3. Add query parameters such as `title` and `date_time` in the **Params** section.
4. Send the request and verify the response.


# Eurorace Backend

This is the backend for the Eurorace application, built with Django and Django REST Framework.

## Application Workflow

### Overview

The Eurorace application is designed to track user locations in real-time. The workflow consists of:

1. **User Authentication**: Users register and authenticate using email verification
2. **Location Tracking**: Authenticated users send their location updates in real-time via WebSockets
3. **Data Storage**: Location updates are stored in the database with timestamps
4. **Data Retrieval**: The application provides REST API endpoints to retrieve location data

### Data Models

The application uses the following main data model:

1. **LocationReport**:
   - Stores a user's location at a specific time
   - Contains user reference, timestamp, and geographic coordinates (latitude/longitude)
   - Provides methods to retrieve the latest location for each user

### Authentication and Email Configuration

The application uses Django's authentication system with email verification for user registration. This is why SMTP server configuration is required in the environment variables.

#### Why Email SMTP Servers are Needed

1. **User Registration**: When a new user registers at `/api/auth/registration/`, the system sends a verification email to confirm their email address.
2. **Email Verification**: Users need to verify their email by clicking on a link sent to their email address.
3. **Password Reset**: If a user forgets their password, they can request a password reset email.

All these features require a properly configured SMTP server to send emails. Without this configuration, users won't be able to complete registration or reset passwords.

### Real-time Communication with WebSockets

The application uses Django Channels with Redis to provide real-time communication via WebSockets.

#### How Channels Work

1. **Channel Layers**: The application uses Redis as a channel layer backend to manage WebSocket connections.
2. **ASGI Server**: The application runs on Daphne (an ASGI server) which supports both HTTP and WebSocket protocols.
3. **Location Updates**: Clients can send real-time location updates through WebSockets.
4. **Data Flow**: When a client sends a location update via WebSocket, the server:
   - Receives the data in the LocationConsumer
   - Creates a new LocationReport object in the database
   - Sends an acknowledgment back to the client

#### WebSocket Endpoints

- **Location Updates**: `ws://domain/ws/location/`
  - Clients can connect to this endpoint to send location updates in real-time.
  - The format for sending location updates is:
    ```json
    {
      "type": "location_update",
      "latitude": 52.2297,
      "longitude": 21.0122
    }
    ```
  - The server will respond with an acknowledgment:
    ```json
    {
      "type": "location_saved",
      "success": true
    }
    ```

#### REST API Endpoints

- **Location Reports**: `/api/location-reports/`
  - GET: Retrieve all location reports
  - POST: Create a new location report
  - `/api/location-reports/latest/`: Get the latest location for each user

## Docker Setup

### Prerequisites

- Docker
- Docker Compose

### Environment Variables

Before running the application, make sure to set the correct environment variables in the `docker-compose.yaml` file or create a `.env` file in the project root. The following variables are required:

- `DEBUG`: Set to `True` for development, `False` for production
- `EMAIL_HOST`: SMTP server host (e.g., smtp.gmail.com)
- `EMAIL_PORT`: SMTP server port (e.g., 465 for SSL)
- `EMAIL_HOST_USER`: SMTP username (your email address)
- `EMAIL_HOST_PASSWORD`: SMTP password
- `EMAIL_USE_SSL`: Set to `True` if your SMTP server uses SSL
- `REDIS_URL`: URL for Redis connection (used for WebSocket channels)

### Building and Running

To build and run the application:

```bash
# Navigate to the backend directory
cd backend

# Build and start the containers
docker-compose up -d

# To rebuild the containers after making changes
docker-compose up -d --build
```

### Accessing the Application

Once the containers are running, you can access:

- API: http://localhost:8000/api/
- Admin interface: http://localhost:8000/admin/
- API documentation: http://localhost:8000/api/schema/swagger-ui/

### Running Commands

To run Django management commands:

```bash
# Run migrations
docker-compose exec backend python manage.py migrate

# Create a superuser
docker-compose exec backend python manage.py createsuperuser

# Collect static files
docker-compose exec backend python manage.py collectstatic
```

### Stopping the Application

To stop the application:

```bash
docker-compose down
```

## Development

For development, you can mount your local directory to the container to see changes in real-time. This is already configured in the `docker-compose.yaml` file.

## Running Tests

### Running Tests in Docker

The project includes a Docker setup for running tests in an isolated environment. This ensures that all dependencies are properly installed and configured.

#### Using the Provided Scripts

On Windows:
```bash
# Navigate to the backend directory
cd backend

# Run the tests
.\run_tests.bat
```

On Linux/Mac:
```bash
# Navigate to the backend directory
cd backend

# Make the script executable
chmod +x run_tests.sh

# Run the tests
./run_tests.sh
```

#### Manual Execution

You can also run the tests manually with Docker Compose:

```bash
# Navigate to the backend directory
cd backend

# Build the test service
docker-compose build test

# Run the tests
docker-compose run --rm test

# Clean up when done
docker-compose down
```

### Running Tests Locally

If you prefer to run the tests locally without Docker, make sure you have all the required dependencies installed:

```bash
# Install dependencies
pip install -e .

# Run the tests
python manage.py test eurorace.tests
```

Note: Running tests locally requires that you have PostgreSQL with PostGIS extension and Redis installed and configured on your system.

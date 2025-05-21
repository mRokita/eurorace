# Eurorace Backend

This is the backend for the Eurorace application, built with Django and Django REST Framework.

## Docker Setup

### Prerequisites

- Docker
- Docker Compose

### Environment Variables

Before running the application, make sure to set the correct environment variables in the `docker-compose.yaml` file or create a `.env` file in the project root. The following variables are required:

- `DEBUG`: Set to `True` for development, `False` for production
- `EMAIL_HOST`: SMTP server host
- `EMAIL_PORT`: SMTP server port
- `EMAIL_HOST_USER`: SMTP username
- `EMAIL_HOST_PASSWORD`: SMTP password
- `EMAIL_USE_SSL`: Set to `True` if your SMTP server uses SSL

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

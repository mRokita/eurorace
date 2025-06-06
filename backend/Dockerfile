FROM --platform=linux/arm64 python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies including GIS libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy project first
COPY . .

# Install Python dependencies directly
RUN pip config set global.index-url https://pypi.org/simple/ && \
    pip config set global.trusted-host pypi.org && \
    for i in $(seq 1 3); do \
        pip install --no-cache-dir --timeout 300 --retries 5 django>=5.0.0 dj-rest-auth[with-social]>=5.1.0 django-environ>=0.11.2 django-leaflet>=0.31.0 django-rest-framework>=0.1.0 drf-extra-fields>=3.7.0 drf-spectacular[sidecar]>=0.28.0 six>=1.17.0 channels>=4.0.0 channels-redis>=4.1.0 psycopg2-binary>=2.9.9 daphne>=4.0.0 djangorestframework-gis>=1.0.0 && break || \
        echo "Retry $i of 3..." && \
        sleep 5; \
    done

# Install the current directory as a package
RUN pip install -e .

# Create directory for static files
RUN mkdir -p /app/static

# Expose port
EXPOSE 8000

# Command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

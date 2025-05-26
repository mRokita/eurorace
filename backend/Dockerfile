FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies including GIS libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libsqlite3-mod-spatialite \
    spatialite-bin \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy project first
COPY . .

# Install Python dependencies with retry mechanism
RUN pip config set global.index-url https://pypi.org/simple/ && \
    pip config set global.trusted-host pypi.org && \
    for i in $(seq 1 3); do \
        pip install --no-cache-dir --timeout 300 --retries 5 -e . && break || \
        echo "Retry $i of 3..." && \
        sleep 5; \
    done

# Create directory for static files
RUN mkdir -p /app/static

# Expose port
EXPOSE 8000

# Command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use Python 3.11 base image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the application files
COPY /app /app
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Start the application
CMD ["flask", "run", "--host=0.0.0.0"]
FROM python:3.11-slim-bullseye

# Set the working directory
WORKDIR /portfolio_be

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY portfolio_be/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY portfolio_be /portfolio_be

# Copy the wait-for-it script
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Expose the application port
EXPOSE 8000

# Default command
# CMD ["/wait-for-it.sh", "postgres:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["/wait-for-it.sh", "postgres:5432", "--", "gunicorn", "portfolio_be.wsgi:application", "--workers", "3", "--bind", "0.0.0.0:8000"]
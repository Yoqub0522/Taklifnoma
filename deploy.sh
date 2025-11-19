#!/bin/bash

echo "Starting deployment..."

# Environment check
if [ ! -f .env ]; then
    echo "Creating .env file from example..."
    cp .env.example .env
    echo "Please edit .env file with your actual values!"
    exit 1
fi

# Build and start containers
echo "Building and starting Docker containers..."
docker-compose down
docker-compose up -d --build

# Wait for database to be ready
echo "Waiting for database to be ready..."
sleep 10

# Run migrations
echo "Running database migrations..."
docker-compose exec web python manage.py migrate

# Create superuser if needed
echo "Do you want to create a superuser? (y/n)"
read create_su
if [ "$create_su" = "y" ]; then
    docker-compose exec web python manage.py createsuperuser
fi

echo "Deployment completed!"
echo "Your site should be available at: https://taklifnoma.yoqubaxmedov.xyz"
# Fiction Express Blog

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker
- Docker Compose

You can download Docker, which includes Docker Compose, from the [official Docker website](https://docs.docker.com/get-docker/).

## Installation

Follow these steps to get your development environment up and running:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

Replace <repository-url> with your repository URL and <repository-directory> with the name of the directory into which you've cloned the project.

### 2. Build Docker Containers

Build the project containers using Docker Compose:

```bash
docker-compose build
```

### 3. Start Docker Containers

Launch the containers:

```bash
docker-compose up -d
```

### 4. Database Migrations

Run Django migrations to set up your database schema:

```bash
docker-compose exec web python manage.py migrate
```

### 5. Create a Superuser Account

Create a superuser for Django admin (panel accessible at /admin):

```bash
docker-compose exec web python manage.py createsuperuser
```
Follow the prompts to complete the creation.

### 6. Verify Installation
Your project should now be running. Access the application through the web browser at the designated URL, usually http://localhost:8000.

### Troubleshooting

If you encounter any issues, review the Docker container logs for errors:

```bash
docker-compose logs
```
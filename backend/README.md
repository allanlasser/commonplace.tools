# Commonplace Tools Backend

## Local Development

Run the backend in local development mode from the project root:

```
docker compose up backend-local
```

To create a superuser inside the Docker container:

```
docker exec -it <container_id> python manage.py createsuperuser
```

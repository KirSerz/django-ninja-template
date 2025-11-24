# Django-Ninja Template

## Environment

Copy `.env.example` to `.env` and adjust values.

- Required: `SECRET_KEY`, `DEBUG`, `CSRF_TRUSTED_ORIGINS`, `CORS_ALLOWED_ORIGINS`, `ALLOWED_HOSTS`,
  `CORS_ORIGIN_ALLOW_ALL`, `DB_NAME`, `DB_USER`, `DB_PASS`, `DB_HOST`, `DB_PORT`,

## How to use

To run:
`docker compose --env-file .env -f docker/compose.yaml up -d`

Site available on 8000 port.

You can make any changes in code, they will appear automatically. If you want to execute something with manage.py use:

```sh
docker compose --env-file .env -f docker/compose.yaml exec app python3 manage.py migrate
docker compose --env-file .env -f docker/compose.yaml exec app python3 manage.py makemigrations
docker compose --env-file .env -f docker/compose.yaml exec app python3 manage.py createsuperuser
```

## Health and docs

- OpenAPI (if web app enabled): `/api/docs`
- Standard Django Admin site for database management: `/django/admin`
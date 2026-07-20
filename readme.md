# Django + Docker cheat sheet

Small README with the main commands for your Django, Docker Compose, and PostgreSQL project.

## Start the project

Build and start containers:

```bash
docker compose up -d --build
```

See what is running:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs web
docker compose logs db
docker compose logs -f web
docker compose logs -f db
```

## Stop and reset

Stop containers:

```bash
docker compose down
```

Stop containers and **delete** the database volume (full DB reset):

```bash
docker compose down -v --remove-orphans
```

## Django commands

### After you change models

1. Create migrations:

```bash
docker compose exec web python manage.py makemigrations
```

2. Apply migrations to the database:

```bash
docker compose exec web python manage.py migrate
```

### When you’re not sure migrations are applied

```bash
docker compose exec web python manage.py showmigrations
```

### Create admin user

```bash
docker compose exec web python manage.py createsuperuser
```

### Django shell

```bash
docker compose exec web python manage.py shell
```

## PostgreSQL commands

Connect to the DB from inside the `db` container:

```bash
docker compose exec db psql -U admin -d booking_platform
```

Change the `admin` user password inside psql:

```sql
ALTER ROLE admin WITH PASSWORD 'admin_password';
```

Exit psql:

```sql
\q
```

## Check app → database connection

Quick test from the `web` container:

```bash
docker compose exec web python -c "import psycopg2; print(psycopg2.connect(dbname='booking_platform', user='admin', password='admin_password', host='db', port=5432).get_dsn_parameters())"
```

If this works, Django can connect to the database.

## Typical daily workflow

### First run of the day

```bash
docker compose up -d
```

### After changing dependencies or the Dockerfile

```bash
docker compose up -d --build
```

### After changing Django models

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

### When the database is completely broken and you want a fresh one

```bash
docker compose down -v --remove-orphans
docker compose up -d --build
docker compose exec web python manage.py migrate
```

## Meaning of common messages

- `No changes detected`: no new model changes that require migrations.
- `No migrations to apply`: all existing migrations are already applied.
- `password authentication failed`: the app is not connecting with the correct DB credentials.
- `could not translate host name "db"`: you are trying to use the Docker hostname from outside a container.

## Important note

Since the project is now dockerized, it’s best to run `makemigrations`, `migrate`, `createsuperuser`, and other `manage.py` commands **inside the `web` container**, not directly on your local host.
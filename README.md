# FastAPI + PostgreSQL Docker Setup

### API Setup

Using a virtual environment is recommended for consistent local development.

```bash
cd backend
python -m .venv venv
```

As a one time setup, you will need to install all the necessary packages to use FastAPI with Postgres.

```bash
pip install fastapi["standard"] fastapi-sqlalchemy pydantic alembic psycopg2-binary
```

Alternatively, if `requirements.txt` already exists, you can install from that.

```bash
pip install -r requirements.txt
```

For any new packages, save them in the `requirements.txt` file.

```bash
pip freeze > requirements.txt
```

### Database Migrations

When first creating an `alembic` project, you will have to initialize it.

```bash
alembic init alembic
```

After changes to the database, create a new migration. Make sure containers are running before doing this.

```bash
docker-compose run api alembic revision --autogenerate -m "New Migration"
```

After creating the new migration, update the database.

```bash
docker-compose run api alembic upgrade head
```

### Database

To be able to run the API and database services, build the containers.

```bash
docker-compose build
```

To run local instances of the API and database, run the containers.

```bash
docker-compose up [-d]
```

To stop the services, run the following:

```bash
docker-compose down [-v]
```

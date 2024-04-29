# FastAPI-Assignment
The below code can be used as the boiler plate for any fastapi based application.

# Items in Repository:
This repository consists of or **fastapi application**(accessible via main.py), **HLD diagram** for the application, **.gitignore** file, and **readme.md** file that contains the documentation and steps to make it work locally.

# Alembic Explanation
We have used an alembic package that keeps the track of database versioning, It's easy to use and maintain and more about alembic can be read via the references provided below. 

Create table command to be used:
```
CREATE TABLE assignment (
    source_id INTEGER PRIMARY KEY NOT NULL,
    source VARCHAR(200),
    source_type VARCHAR(10),
    source_tag VARCHAR(10),
    last_updated_date TIMESTAMP,
    from_date TIMESTAMP,
    to_date TIMESTAMP,
    frequency VARCHAR(5)
);
```
got converted into python sqlalchemy code used in alembic version as:
```
def upgrade() -> None:
    op.create_table(
        'assignment',     
        sa.Column('source_id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('source', sa.String(length=200), nullable=True),
        sa.Column('source_type', sa.String(length=10), nullable=True),
        sa.Column('source_tag', sa.String(length=10), nullable=True),
        sa.Column('last_updated_date', sa.DateTime(), nullable=True),
        sa.Column('from_date', sa.DateTime(), nullable=True),
        sa.Column('to_date', sa.DateTime(), nullable=True),
        sa.Column('frequency', sa.String(length=5), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('assignment')
```

# How to run the Application
## Step-1
Create a Postgres Database in your local system using pgadmin tool or we can simply type in the commands as mentioned below:
```command prompt
psql -U <username>;
CREATE DATABASE <database_name>;
```
One can also take help from the sources mentioned below as references to create a database.

## Step-2
Create a virtual env and install the requirements.txt file using pip. Once installed, we have to add the URL for our postgres database to act as a primary database
handling all of our fastapi queries. We need to add URL in **models->db_models.py** file and also in **alembic.ini** file.


Format for database URL is mentioned here:
```
postgresql://<username>:<password>@<IP_address>:<port>/<database name>
```

Once this is done we need to upgrade the alembic locally, and for that we already have a file in this repository, hence we only use the command as:
```command prompt
alembic upgrade head
```

## Step-3
Once we are done with changing the DB URL with our local db and installing all the requirements. We can start the fastapi application by using the command.
```
python main.py
```

Once our app is running it'll be visible on our localhost port 8000. Link to open the app:
```
http://localhost:8000/
```

## Step-4
We can now test the working of the api's easily by either using curl commands(mentioned below) or we can directly go to the fast api docs and use it from there.
We can access docs via link:
```
http://localhost:8000/docs
```

## Step-5
Now all we have to do is paste these curl commands from our terminal or any shell and see if the api's are working or not, below we have all the curl sample commands along with the outputs mentioned.

**/add-data**
```
INPUT:
curl -X 'POST' \
  'http://localhost:8000/add_data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "source_id": 2,
  "source": "amazon",
  "source_type": "online",
  "source_tag": "am",
  "last_updated_date": "2023-07-07T13:25:30.420Z",
  "from_date": "2023-07-07T13:25:30.420Z",
  "to_date": "2023-07-07T13:40:30.420Z",
  "frequency": "21M"
}'


OUTPUT:
{
  "status": "success"
}
```

**/update_data**
```
INPUT:
curl -X 'POST' \
  'http://localhost:8000/update_data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "source_id": 2,
  "last_updated_date": "2023-07-07T13:27:47.461Z",
  "from_date": "2023-07-06T13:27:47.461Z",
  "to_date": "2023-07-06T13:35:47.461Z"
}
'


OUTPUT:
{
  "status": "success"
}
```

**/get_data**
```
INPUT:
curl -X 'POST' \
  'http://localhost:8000/get_data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "source_id": 2
}'


OUTPUT:
{
  "response": {
    "source_id": 2,
    "source": "amazon",
    "source_type": "online",
    "source_tag": "am",
    "last_updated_date": "2023-07-07T18:57:47.461000",
    "from_date": "2023-07-06T18:57:47.461000",
    "to_date": "2023-07-06T19:05:47.461000",
    "frequency": "21M"
  }
}
```

**/get_trigger_data**
```
INPUT:
curl -X 'POST' \
  'http://localhost:8000/get_trigger_data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "source_id": 2
}'


OUTPUT:
{
  "response": {
    "source_id": 2,
    "source": "amazon",
    "source_type": "online",
    "source_tag": "am",
    "last_updated_date": "2023-07-07T18:57:47.461000",
    "from_date": "2023-07-06T19:18:47.461000",
    "to_date": "2023-07-06T19:26:47.461000",
    "frequency": "21M"
  }
}
```

## References:
https://fastapi.tiangolo.com/tutorial/first-steps/ <br>
https://codevoweb.com/crud-restful-api-server-with-python-fastapi-and-postgresql/ <br>
https://tutlinks.com/fastapi-with-postgresql-crud-async/ <br>
https://alembic.sqlalchemy.org/en/latest/ <br>

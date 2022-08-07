# A barely working GraphQL Tornado SqlAlchemy server

Set up venv.

    python3 -m venv venv
    ./venv/bin/pip install pip wheel -U
    ./venv/bin/pip install -r requirements.txt

Create and initialize Sqlite database.

    ./venv/bin/python init_db.py

Start server:

    ./venv/bin/python main.py


Open in browser: localhost:5000/graphql

Example query:
```graphql
{
  allEmployees(sort: [NAME_ASC, ID_ASC]) {
    edges {
      node {
        id
        name
        department {
          id
          name
        }
        role {
          id
          name
        }
      }
    }
  }
}
```

## graphene-tornado

graphene_tornado is from: https://github.com/graphql-python/graphene-tornado.git

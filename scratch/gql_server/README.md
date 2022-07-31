# A barely working GraphQL Tornado SqlAlchemy server

Initialize sqlite database: `python init_db.py`

run: `python gql_server.py`

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

Abandonware?: https://github.com/graphql-python/graphene-tornado  (last update 2 yrs ago, last release 4 yrs ago)

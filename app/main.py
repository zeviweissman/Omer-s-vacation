from app.gql.Query import Query
from flask import Flask
from app.database.psql import initate_db, drop_data_base_if_exists
from app.repository.init_data_repository import init_data
from app.models import *
from graphene import Schema
from flask_graphql import GraphQLView


schema = Schema(query=Query)
app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)


if __name__ == "__main__":
    drop_data_base_if_exists()
    initate_db()
    init_data()
    app.run()
from app.settings.psql_config import engine, _session_factory, Base
from sqlalchemy_utils import database_exists, create_database, drop_database


def create_data_base_if_not_exists():
    if not database_exists(engine.url):
        create_database(engine.url)

def drop_data_base_if_exists():
    if database_exists(engine.url):
        drop_database(engine.url)

def create_tabels_if_not_exists():
    Base.metadata.create_all(engine)

def get_session():
    return _session_factory()

def initate_db():
    create_data_base_if_not_exists()
    create_tabels_if_not_exists()


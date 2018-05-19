from app.db import init_db_engine
import config

from .users import api

init_db_engine(config.SQLALCHEMY_DATABASE_URI)
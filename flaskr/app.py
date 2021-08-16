from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# instantiate
app = Flask(__name__)

# will be deprecated by default in future
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set as temp db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# set metadata and wrapped
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
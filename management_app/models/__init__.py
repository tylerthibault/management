from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .family import Family
from .parent import Parent
from .child import Child

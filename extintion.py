from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
csrf = CSRFProtect()
db = SQLAlchemy()
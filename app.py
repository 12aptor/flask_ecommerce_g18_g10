from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return "<button>Dame click</button>"

import routers.productos_router
import routers.categorias_router
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

# DeclarativeBase is a base clas for declarative class definitions
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

# Mapped is a base class for mapped class definitions
class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)

# Create the database and add a user
with app.app_context():
    db.create_all()

    db.session.add(User(username="example"))
    db.session.commit()

    # Query the database
    users = db.session.execute(db.select(User)).scalars()


# if __name__ == '__main__':
#   app.run(debug=True)

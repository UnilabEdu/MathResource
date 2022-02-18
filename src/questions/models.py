from src.extensions import db


# DB Model
class DBModel(db.Model):
    __tablename__ = "table_1"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    param1 = db.Column(db.Text)
    param2 = db.Column(db.Boolean)

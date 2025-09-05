from app import db

class branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255))
    phone = db.Column(db.String(50))
    address = db.Column(db.String(255))
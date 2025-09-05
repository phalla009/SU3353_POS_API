from app import db

class sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer)
    total = db.Column(db.Numeric(10,2), nullable=False)
    paid = db.Column(db.Numeric(10,2), nullable=False)
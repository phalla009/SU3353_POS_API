from  app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    cost = db.Column(db.Numeric(18, 2), nullable=False)
    price = db.Column(db.Numeric(18, 2), nullable=False)
    image = db.Column(db.String(500))
    stock = db.Column(db.Numeric(18, 2), nullable=False, default=0)
    description = db.Column(db.String(500))
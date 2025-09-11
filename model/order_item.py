from app import db

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    price = db.Column(db.Numeric(18, 2), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Numeric(18, 2), nullable=False)
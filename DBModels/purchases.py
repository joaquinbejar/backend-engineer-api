from sqlalchemy import func

from db import db


class Purchases(db.Model):
    __tablename__ = 'purchases'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    quantity = db.Column(db.Integer())
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def json(self):
        return {'name': self.name, 'quantity': self.quantity, 'price': self.price}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_purchases():
        allpurchases = db.session.query(Purchases.name, func.sum(Purchases.quantity).label('quantity'),
                                        func.sum(Purchases.price).label('price')).group_by(Purchases.name).all()

        purchases = [{'name': item[0], 'quantity': item[1], 'price': round(item[2], 2)} for item in allpurchases]
        print(purchases, flush=True)

        return purchases

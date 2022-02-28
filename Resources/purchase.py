from datetime import datetime

from flask_restful import Resource, reqparse

from DBModels.menu import Menu
from DBModels.purchases import Purchases


class Purchase(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('coffee',
                        type=str,
                        action='append',
                        required=True,
                        help="This field could not be blank")
    parser.add_argument('quantity',
                        type=int,
                        action='append',
                        required=True,
                        help="This field could not be blank")
    parser.add_argument('creditcardnumber',
                        type=str,
                        required=True,
                        help="This field could not be blank")
    parser.add_argument('expirydate',
                        type=str,
                        required=True,
                        help="This field could not be blank")

    def post(self):
        '''
        Make a purchase of coffee
        :return: json with purchase summary
        Example: { "errors": [ "Cappuccino is not in the Menu" ], "total": 8.65, "mocha": { "quantity": 2, "total": 6.5 }, "latte": { "quantity": 1, "total": 2.15 } }
        '''
        data = Purchase.parser.parse_args()
        print(data, flush=True)
        try:
            expirydate = datetime.strptime(data['expirydate'], '%m/%y')
            if expirydate < datetime.today():
                return {'message': 'Credit card is expired'}, 400
        except:
            return {'message': 'Wrong expiry date'}, 400

        if len(data['coffee']) == len(data['quantity']):
            purchase = {}
            purchase['errors'] = []
            purchase['total'] = 0
            for i, coffee in enumerate(data['coffee']):
                item = Menu.find_by_name(coffee)
                if item:
                    quantity = data['quantity'][i]
                    purchase[coffee] = {'quantity': quantity, 'total': quantity * item.price}
                    purchase['total'] += quantity * item.price
                    Purchases(coffee, quantity, quantity * item.price).save_to_db()
                else:
                    purchase['errors'].append(f'{coffee} is not in the Menu')

            return purchase, 200
        else:
            return {'message': 'Missing quantity or coffee'}, 400


class AllPurchases(Resource):
    def get(self):
        '''
        Get All Purchases of coffess
        :return:  json with a list of existing Purchases
        '''
        allpurchases = Purchases.get_purchases()
        return {'purchases': allpurchases}

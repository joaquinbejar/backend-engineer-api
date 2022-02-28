from flask_restful import Resource, reqparse

from DBModels.menu import Menu


class Coffee(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field could not be blank")

    def get(self, name):
        '''
        Get info about a coffee by name
        :param name: string coffee name
        :return: json with price about the coffee or error if it doesn't exist
        '''
        item = Menu.find_by_name(name)
        if item:
            return item.json()
        return {'message': f'Coffee with name {name} is not exist'}

    def post(self, name):
        '''
        Create new coffee in Menu
        :param name: string coffee name
        :return: json with message about result
        '''
        item_db = Menu.find_by_name(name)
        if item_db:
            return {'message': 'An item is already exist'}, 400
        data = Coffee.parser.parse_args()
        item = Menu(name, data['price'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500
        return item.json(), 201

    def delete(self, name):
        '''
        Delete coffe from menu
        :param name: string coffee name
        :return: json with message about result of deletion
        '''
        item_db = Menu.find_by_name(name)
        if item_db is None:
            return {"message": "Coffee '{}' not found ".format(name)}
        item_db.delete_from_db()
        return {'message': f'Coffee {name} is deleted'}

    def put(self, name):
        '''
        Update price for a coffee
        :param name: string coffee name
        :return: json with coffee price
        '''
        data = self.parser.parse_args()
        item = Menu.find_by_name(name)

        if item is None:
            item = Menu(name, data['price'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()


class MenuList(Resource):
    def get(self):
        '''
        Get Menu of coffess
        :return:  json with a list of existing coffees
        '''
        coffees_db = Menu.query.all()
        coffees = [item.json() for item in coffees_db]
        return {'Coffees': coffees}

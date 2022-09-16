class ShoppingCart():
    def __init__(self):
        self.cart = []
        items = int(input("How many items do you want to include?"))
        [self.add_item_cart() for _ in range(items)]

    def add_item_cart(self):
        id_user = input("Insert user_id:")
        id_produto = input("Insert product_id:")
        price_product = float(input("Insert product price:"))
        quantity_product = int(input("Insira a quantidade de produto:"))

        item = [id_user, id_produto, price_product, quantity_product]

        self.cart.append(item)

    def get_all_items_cart(self):
        print("Current itens in shopping cart are:\n")
        [print(f"User_id: {item[0]}\nProduct_id: {item[1]}\nProduct Price: {item[2]}\nProduct Quantity: {item[3]}\n\n") for item in self.cart]

    def get_item_cart_by_id(self, id_product):
        res = None
        for _, item in enumerate(self.cart):
            if item[1] == id_product:
                res = item
                break

        if res:
            print(f"User_id: {res[0]}\nProduct_id: {res[1]}\nProductP Price: {res[2]}\nProduct Quantity: {res[3]}\n\n")
            return res
        else:
            print('Product not found')
            return ['', '', '', '']

    def remove_item_id(self, id_product):
        res = None
        for i, item in enumerate(self.cart):
            if item[1] == id_product:
                res = self.cart.pop(i)
                break
        if res:
            print(f"You removed item:\nUser_id: {res[0]}\nProduct_id: {res[1]}\nProduct Price: {res[2]}\nProduct Quantity: {res[3]}\n\n")
            return res
        else:
            print('Product not found')
            return ['', '', '', '']
        pass

cart = ShoppingCart()

cart.get_all_items_cart()

id_product = input('Which item you would like to see?')
item = cart.get_item_cart_by_id(id_product)

id_product = input('Which item you would like remove?')
item = cart.remove_item_id(id_product)

cart.get_all_items_cart()
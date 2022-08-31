from re import I


cart = []

def add_item_cart(cart):
    id_user = input("Insert user_id:")
    id_produto = input("Insert product_id:")
    price_product = float(input("Insert product price:"))
    quantity_product = int(input("Insira a quantidade de produto:"))

    item = [id_user, id_produto, price_product, quantity_product]

    return cart.append(item)

def get_all_items_cart(cart):
    print("Current itens in shopping cart are:\n")
    [print(f"User_id: {item[0]}\nProduct_id: {item[1]}\nProductP Price: {item[2]}\nProduct Quantity: {item[3]}\n\n") for item in cart]
    return 0

def get_item_cart_by_id(cart, id_product):
    for _, item in enumerate(cart):
        if item[1] == id_product:
            res = item
            break

    if res:
        return res
    else:
        print('Product not found')
        return ['', '', '', '']

def remove_item_id(cart, id_product):
    for i, item in enumerate(cart):
        if item[1] == id_product:
            res = cart.pop(i)
            break
    if res:
        return res
    else:
        print('Product not found')
        return ['', '', '', '']
    pass

items = int(input("How many items do you want to include?"))
[add_item_cart(cart) for _ in range(items)]

get_all_items_cart(cart)

id_product = input('Which item you would like to see?')
item = get_item_cart_by_id(cart, id_product)
print(f"User_id: {item[0]}\nProduct_id: {item[1]}\nProductP Price: {item[2]}\nProduct Quantity: {item[3]}\n\n")

id_product = input('Which item you would like remove?')
item = remove_item_id(cart, id_product)
print(f"You removed item:\nUser_id: {item[0]}\nProduct_id: {item[1]}\nProduct Price: {item[2]}\nProduct Quantity: {item[3]}\n\n")

get_all_items_cart(cart)
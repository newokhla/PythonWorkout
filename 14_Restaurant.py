menu = {'sandwich': 10, 'tea': 7, 'water': 1, 'fries': 4}

def get_order(menu):
    order_total = 0
    while True:
        customer_order = input('What would you like to order? ')
        if not customer_order:
            break
        if menu.get(customer_order):
            order_total += menu.get(customer_order)
            print(f'{customer_order} is {menu.get(customer_order)}, order total is {order_total}.')
        else:
            print(f'{customer_order} is not on the menu.')
    print(f'Your order total is {order_total}.')
        
get_order(menu)
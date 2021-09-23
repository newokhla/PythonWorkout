def calculate_tax(purchase_price, province, hour):
    provinces = {'Chico': 0.5, 'Groucho': 0.7, 'Harpo': 0.5, 'Zeppo': 0.4}
    return  purchase_price * (1 + (provinces.get(province, 0) * hour/24))

print(calculate_tax(10, 'Chico', 1))
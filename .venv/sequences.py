odd_nums = range(1, 100, 2)
even_nums = range(0, 101, 2)

print(list(odd_nums))
print(list(even_nums))

fruits = ['apple', 'orange', 'banana']
quantities = [100, 200, 300, 255]

fruit_qtys_zip = zip(fruits, quantities)

fruit_qtys_dict = dict(fruit_qtys_zip)
print(fruit_qtys_dict)

products = ['phone', 'tablet', 'laptop']

products_quantities = [343, 16, 57]

products_qtys=zip(products, products_quantities)

for product in products_qtys:
    print(product)
    print(product[0])
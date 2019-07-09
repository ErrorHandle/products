products = []
while True:
	name = input('enter product name: ')
	if name == 'q':
		break
	price = input('enter price of product: ')
	products.append([name, price])
print(products)
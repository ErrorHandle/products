products = []
while True:
	name = input('enter product name: ')
	if name == 'q':
		break
	price = input('enter price of product: ')
	products.append([name, price])


for p in products:
	print('The price of', p[0], 'is', p[1], 'dollar')
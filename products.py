products = []
while True:
	name = input('enter product name: ')
	if name == 'q':
		break
	price = input('enter price of product: ')
	price = int(price)
	products.append([name, price])


for p in products:
	print('The price of', p[0], 'is', p[1], 'dollar')

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('產品, 價錢\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')


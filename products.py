
import os # operating system

products = []
if os.path.isfile('products.csv'): #check file
	print('have file')

	#read file
	with open('products.csv', 'r') as f:
		for line in f:
			if '產品, 價錢' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('no file')

#user input data
while True:
	name = input('enter product name: ')
	if name == 'q':
		break
	price = input('enter price of product: ')
	price = int(price)
	products.append([name, price])

#print products
for p in products:
	print('The price of', p[0], 'is', p[1], 'dollar')

#write file
with open('products.csv', 'w') as f:
	f.write('產品, 價錢\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')


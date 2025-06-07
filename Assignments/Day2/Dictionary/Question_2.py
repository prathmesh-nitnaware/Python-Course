"""create a dictionary with pairs
	soap:100
	deo:300
	perfume:400"""

products = {
    "soap": 100,
    "deo": 300,
    "perfume": 400
}

a = input("Enter the product name: ").lower()

if a in products:
    print(f"Price of {a}: {products[a]}")
else:
    print("product not available")

"""create a dictionary with pairs
	soap:100
	deo:300
	perfume:400"""

item = {
    "soap": 100,
    "deo": 300,
    "perfume": 400
}

a = input("Enter the Item name: ").lower()

if a in products:
    print(f"Price of {a}: {item[a]}")
else:
    print("product not available")

#create a tuple to store 5 numbers and then sort it in ascending and descending order.


tuple = (30, 49, 5, 12, 100)
print("Original Tuple: " ,tuple)

tuple2 = sorted(tuple)
print("Ascending Order: ", tuple2)

tuple3 = sorted(tuple2, reverse=True)
print("Descending Order: " ,tuple3)

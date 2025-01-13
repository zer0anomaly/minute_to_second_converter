var1 = int(input("The minute:"))

def converter(var1):
	return var1 * 60

var2 = converter(var1)
print(f"{var1} minutes is equal to {var2} seconds.")
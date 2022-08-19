def add(n1, n2):
	return n1 + n2
	
def subtract(n1, n2):
	return n1 - n2


def multiply(n1, n2):
	return n1 * n2


def divide(n1, n2):
	return round(n1 / n2, 2)


operations = {
	"+" : add,
	"-" : subtract,
	"*" : multiply,
	"/" : divide,
}

def calculation():
	to_continue = True
	num1 = float(input("Enter first number: "))

	while to_continue:
		op = input("Enter operation you would like to perform (+, -, *, /): ")
		num2 = float(input("Enter first number: "))
		op_fun = operations[op]	
		result =	op_fun(num1, num2)
		print(f"{num1} {op} {num2} = {result}")		
		choice = input("Type 'Yes' to continue with {result1} or 'No' to exit or 'New' to start new calculation: ").title()
		
		if choice  == 'Yes':
			num1 = result
		elif choice == 'New':
			to_continue = False
			calculation()
		else:
			to_continue = False
calculation()

import art

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1- n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1 / n2

addFunctionVar = add
subtractFunctionVar = subtract
multiplyFunctionVar = multiply
divideFunctionVar = divide

operations = {
    "+" : addFunctionVar,
    "-" : subtractFunctionVar,
    "*" : multiplyFunctionVar,
    "/" : divideFunctionVar
}

def calculator():
    print(art.logo)
    should_use_ans = True
    num1 = float(input("Type in the first number: "))
    while should_use_ans:

        # print("""         +
        #          -
        #          *
        #          /""")
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Type the operation to be done: ")

        num2 = float(input("Type in the next number: "))
        ans = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {ans}")

        choice = input(f"Type 'y' to continue calculating from {ans}, or type 'n' to start a new calculation :")
        if choice == 'y':
            num1 = ans
        else:
            should_use_ans = False
            print("\n * 20")   #adding this to make it clear the screen at go up.
            calculator() #after 'n' it just needs to redo the whole thing again, this time taking the first number too.

calculator() #once outside the function to initiate it.
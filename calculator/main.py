OP = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    
}

def main():
    exp = input("Please enter your expression: ")
    # 3 + 3
    # 5-2
    # 3-2
    # 1. Iterate through expression symbols
    # 3.14
    # [ 3 5 8 ]
    # [ - + ]
    numbers = []
    operators = []
    current_number = ""
    for c in exp:
        if c.isnumeric() or c == ".":
            current_number += c
            continue
        if current_number:
            numbers.append(int(current_number))
            current_number = ""
        if c == " ":
            continue
        if c in ("+", "-", "*", "/"):
            operators.append(c)
            continue
        raise ValueError()
    if current_number:
        numbers.append(int(current_number))
        current_number = ""
    print("Numbers:", numbers)
    print("Operators;", operators)

    result = numbers.pop(0)
    for op in operators:
        fn = OP[op]
        result = fn(result, numbers.pop(0))
    print ("Result is:", result)
        

if __name__== "__main__":   
    main()
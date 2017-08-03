#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv)
    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif count == 4 and sys.argv[2] == '*':
        op = sys.argv[2]
    else:
        op = sys.argv[2]

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif op == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif op == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif op == '/':
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

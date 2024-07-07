# solution.py

class InputHandler:
    @staticmethod
    def read_single_string():
        return input()

    @staticmethod
    def read_single_integer():
        return int(input())

    @staticmethod
    def read_single_float():
        return float(input())

    @staticmethod
    def read_int_array():
        return list(map(int, input().split()))

    @staticmethod
    def read_float_array():
        return list(map(float, input().split()))

    @staticmethod
    def read_string_array():
        return input().split()

    @staticmethod
    def read_mixed_array():
        return input().split()

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

def greet(name):
    return f"Hello, {name}!"

def solve():
    # Example usage of InputHandler
    input_handler = InputHandler()
    
    single_string = input_handler.read_single_string()
    single_integer = input_handler.read_single_integer()
    single_float = input_handler.read_single_float()
    int_array = input_handler.read_int_array()
    float_array = input_handler.read_float_array()
    string_array = input_handler.read_string_array()
    mixed_array = input_handler.read_mixed_array()

    # Example usage of Calculator and greet
    calc = Calculator()
    sum_result = calc.add(5, 7)
    greeting = greet("Alice")
    
    # Print results
    print(single_string)
    print(single_integer)
    print(single_float)
    print(int_array)
    print(float_array)
    print(string_array)
    print(mixed_array)
    print(sum_result)
    print(greeting)

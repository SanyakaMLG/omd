import sys
from datetime import datetime
from typing import Callable

original_write = sys.stdout.write


# task1
def my_write(s: str) -> int:
    if s == '\n':
        original_write(s)
        return 0
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    text_with_timestamp = f'[{timestamp}]: {s}'
    original_write(text_with_timestamp)
    return sys.getsizeof(text_with_timestamp)


# task2
def timed_output(function: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        def my_write(string_text: str) -> int:
            if string_text == '\n':
                original_write(string_text)
                return 0
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            text_with_timestamp = f'[{timestamp}]: {string_text}'
            original_write(text_with_timestamp)
            return sys.getsizeof(text_with_timestamp)

        sys.stdout.write = my_write
        res = function(*args, **kwargs)
        sys.stdout.write = original_write
        return res

    return wrapper


@timed_output
def print_greeting(name: str):
    print(f'Hello, {name}!')


# task3
def redirect_output(filepath: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            original = sys.stdout
            with open(filepath, 'w') as output:
                sys.stdout = output
                res = func(*args, **kwargs)
                sys.stdout = original
            return res
        return wrapper
    return decorator


@redirect_output('function_output.txt')
def calculate() -> None:
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    print(1)
    sys.stdout.write = my_write
    print(2)
    sys.stdout.write = original_write
    print(3)
    print_greeting("Nikita")
    print(4)
    calculate()
    print(5)

from functools import wraps

def safe_calculator(func):
    @wraps(func)
    def wrapper(expression, *args, **kwargs):
        try:

            result = func(expression, *args, **kwargs)
            return result
        except ZeroDivisionError:
            print(f"Помилка у виразі '{expression}': Ділення на нуль.")
            return None
        except SyntaxError:
            print(f"Помилка у виразі '{expression}': Невірний синтаксис.")
            return None
        except NameError as e:
            print(f"Помилка у виразі '{expression}': Використано заборонену змінну або функцію ({e}).")
            return None
        except Exception as e:
            print(f"Сталася непередбачена помилка для виразу '{expression}': {e}")
            return None
    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

# Приклади використання:
print(calculate("2 + 2 * 2"))
print(calculate("10 / 0"))
print(calculate("2 + 'a'"))
print(calculate("import os"))
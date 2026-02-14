from functools import wraps

def integer_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        is_int = all(isinstance(el, int) for el in args)
        if is_int:
            return func(*args, **kwargs)
        else:
            print('Ошибка: все аргументы должны быть целыми числами!')
            return None
    return wrapper
    

@integer_only
def multiply(a, b):
    return a * b

# Тесты:
print(multiply(10, 2))   # Должно вывести: 20
print(multiply(10, "2")) # Должно вывести: Ошибка... и потом None



def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    print(f'Ошибка! Пробую еще раз... осталось попыток: {times-i-1}')
            return "Функция не удалась"
        return wrapper  
    return decorator

# Тест:
import random

@retry(times=3)
def unstable_connection():
    if random.random() < 0.7: # В 70% случаев будет ошибка
        raise ConnectionError("Сбой сети!")
    return "Данные получены!"

print(unstable_connection())

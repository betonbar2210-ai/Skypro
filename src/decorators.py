from functools import wraps
from time import time


def log(filename):
    """Декоратор - логирование выполнений функций (время, имя, результат выполнения)
    с выводом в консоль или с записью в .txt файл"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_func = time()
            try:
                result = func(*args, **kwargs)
                finish_func = time()
                time_func = finish_func - start_func
                text_log_ok = (
                    f"Функция {func.__name__} оk:\n" f"Время выполнения: {time_func}\n" f"Результат:\n{result}\n\n"
                )
                if ".txt" in filename:
                    with open(filename, "a", encoding="utf-8") as x:
                        x.write(text_log_ok)
                else:
                    print(text_log_ok)
                return result
            except Exception as e:
                finish_func_error = time()
                time_func_error = finish_func_error - start_func
                text_log_er = (
                    f"Функция {func.__name__} error:\n"
                    f"{type(e).__name__}: {str(e)}\n"
                    f"Inputs:\n{args}, {kwargs}\n"
                    f"Время выполнения: {time_func_error}\n\n"
                )
                if ".txt" in filename:
                    with open(filename, "a", encoding="utf-8") as x:
                        x.write(text_log_er)
                else:
                    print(text_log_er)
                raise

        return inner

    return wrapper

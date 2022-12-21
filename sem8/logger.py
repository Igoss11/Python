# Модуль для записи результатов вычислений


def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде | задача -> ответ | """
    with open('logger.txt', 'a',  encoding='utf-8') as file:
        file.write(expr, result)


def get_history() -> str:
    """Возвращает содержимое файла с результатами вычислений"""
    with open('logger.txt', 'r',  encoding='utf-8') as file:
        return file.read()

import math

MAX_STEPS = 100_000

def f_ratio(x):
    return x / (x+1)

def f_root(x):
    return math.sqrt(x * x+1)

''' задать параметры команды
ключ = команда, и
значения(функция, описание, отрезок a,b, строгость границ) '''
FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x+1)", 0, 20, True),
    "root": (f_root, "F(x) = sqrt(x^2+1)", -5, 5, False)
}

 
def check_params(name, a, b, steps):
    ''' Проверить по команде name параметры функции:
    конечность чисел a,b
    предела в промежутке, диапазон количества шагов'''
    f, formula, low, high, closed = FUNCTIONS[name]
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Предел не является конечным числом")
    if a>=b:
        raise ValueError("Начальный предел не меньше конечного")

    for value in (a,b):
        if closed:
            outside = value < low or value > high
        else:
            outside = value <= low or value >= high
        if outside:
            raise ValueError("Предел вне промежутка")
    if not (1 <= steps <= MAX_STEPS):
        raise ValueError("Количество шагов вне диапазона")

def integrate(f, a, b, steps):
    ''' Вычисление интеграла на отрезке [a,b] c шагом steps
    для функции f (имя функции). Возвращает результат (float) '''
    dx = (b - a) / steps
    rez=0
    for i in range(steps):
        x = a + i*dx
        rez = rez + f(x)*dx
    return rez

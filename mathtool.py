import sys
from cli  import create_parser
from calc import equation
from calc import stats
from calc import series
from calc import integration


# > solve
# > solve -a 1 -b -3 -c 2
def hand_solve(args):
    ''' Обработчик для команды solve, args - АКС
        Получает коэффициенты из консоли или  АКС
        Проверяет коэффициенты на тип и количество,
        вызывает функцию решения квадратного уравнения
        Выводит результаты'''
    
    arg = [args.a, args.b, args.c]
    cnt = arg.count(None)
    print("Решение квадратного уравнения")
    if cnt == 3:
        try:
            a = int(input("введите А: "))
            b = int(input("введите B: "))
            c = int(input("введите C: "))
        except ValueError:
            raise ValueError("Коэффициент не является целым числом")
    elif cnt == 0:  # АКС
        a, b, c = args.a, args.b, args.c
    else:
        raise ValueError("Укажите три коэффициента или ни одного")

    equation.solve_check({"A": a, "B": b, "C": c})
    kind, d, roots = equation.solve(a, b, c)
    
    print(f"уравнение {kind}")
    if d is not None:
        print(f"дискриминант: {d}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("действительных корней нет")
    return 0

def get_num(source):
    ''' Преобразует числа из source файла в массив (float)'''
    ar = []
    for line in source:
        for word in line.split():
            try:
                ar.append(float(word))
            except ValueError:
                raise ValueError(f"{word} не является числом")
    return ar

# > mathtool.py stats --input numbers.txt (из файла)
# > stats (с клавиатуры через cmd ^Z)
# > type numbers.txt | python mathtool.py stats (из конвейера)
def hand_stats(args):
    ''' Обработчик для команды stats, args - АКС
        Получает значения ряда values из stdin или файла, проверяет их,
        и через REPORT выводит результат'''
    if args.input is not None: # из файла
        try:
            with open(args.input, encoding="utf-8-sig") as handle:
                values = get_num(handle)
        except OSError:
            raise OSError(f"Файл {args.input} не открывается")
    else: # из потока
        values = read_num(sys.stdin)

    stats.stats_check(values)

    for label, function, form in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")
    return 0

#> series --func sqplus --terms 6
#> series --func sqplus --eps 0.0001
#> series --func third  --terms 6
#> series --func third  --eps 0.0001
def hand_series(args):
    series.check_params(args.terms, args.eps)
    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        res = series.sum_terms(term, args.terms)
        count = args.terms
    else:
        res, count = series.sum_eps(term, args.eps)
    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {res:.4f}")
    return 0

# > integrate --func ratio --from 0 --to 20 --steps 1000
# > integrate --func root --from -5 --to 5 --steps 1000
def hand_integrate(args):
    integration.check_params(args.func, args.start, args.end, args.steps)

    f, formula, low, high, closed = integration.FUNCTIONS[args.func]

    rez = integration.integrate(f, args.start, args.end, args.steps)

    print(formula)
    print(f"Значение интеграла: {rez:.4f}")
    return 0

''' Сопоставить каждой команде соответствующий обработчик '''
HANDLERS = {
    "solve":     hand_solve,
    "stats":     hand_stats,
    "series":    hand_series,
    "integrate": hand_integrate
}

def main(argv):
    ''' Разобрать аргументы командной строки (АКС).
        По команде вызвать соответствующий обработчик функции '''   
    parser = create_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1
    
if __name__ == "__main__":
    ''' вызвать функцию main как единственную точку входа в программу,
        вернуть код ошибки,
        отладочная печать для теста'''
    print('-------------- тест   --------------')
    print(f"Команда: ", ' '.join(sys.argv[1:]))
    print('stdin: ', '<пусто>')
    print('stdout: ', '')  
    code = main(sys.argv[1:])
    print('stderr: ', '<пусто>')
    print('Код возврата: ',code)
    sys.exit(code)
    
    # sys.exit(sys.argv[1:])

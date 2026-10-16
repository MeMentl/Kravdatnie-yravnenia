import argparse
from calc import series
from calc import integration
from calc import equation

def create_parser():
    parser=argparse.ArgumentParser(
        prog="mathtool",
        description="вычисление уравнений и числовых последовательностей",
        allow_abbrev=False)

    commands = parser.add_subparsers(dest="command", title="команды")

    p = commands.add_parser("solve", allow_abbrev=False, help="Решение квадратного уравнения:")
    p.add_argument("-a", type=int, help=f"коэфициент А (целое, по модулю не более {equation.MAX_VALUE})")
    p.add_argument("-b", type=int, help=f"коэфициент B (целое, по модулю не более {equation.MAX_VALUE})")
    p.add_argument("-c", type=int, help=f"коэфициент C (целое, по модулю не более {equation.MAX_VALUE})")

    p = commands.add_parser("stats", allow_abbrev=False, help="Показатели последовательности")
    p.add_argument("--input", help="файл с данными")

    p = commands.add_parser("series", allow_abbrev=False, help="Сумма ряда")
    p.add_argument("--func", required=True, choices=sorted(series.FORMULAS), help="Имя ряда:")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="количество элементов в последовательности")
    group.add_argument("--eps", type=float, help=f"точность слагаемого (меньше {series.MAX_EPS})")

    p = commands.add_parser("integrate", allow_abbrev=False, help="Нахождение интеграла методом левых прямоугольников")
    p.add_argument("--func", required=True, choices=sorted(integration.FUNCTIONS), help="Выбрать функцию для интегрирования:")
    p.add_argument("--from", dest="start", type=float, required=True, help="нижний предел")
    p.add_argument("--to", dest="end", type=float, required=True, help="верхний предел (больше нижнего)")
    p.add_argument("--steps", type=int, required=True, help="число прямоугольников (целое)")

    return parser

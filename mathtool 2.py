# Точка входа. Вызов (диспетчеризация) команд из соответствующих модулей
import sys
import cli
from calc import equation
from calc import stats

MAX_VALUE = 50 #pred = 50

def inpInt(coef):   # Ввод числа с клавиатуры
    s = input(f'Введите число {coef}: ')  
    try:  # Проверяем,число ли это
        n = int(s)
    except ValueError:
            #print("Я же сказал, введите число")
            #print('ОШИБКА: коэффициент не является целым числом',file=sys.stderr), sys.exit(1)
            raise ValueError('коэффициент не является целым числом')            
    return n
    
# проверить_коэффициенты({"A": args.a, "B": args.b, "C": args.c})
def checkK(coefs):
    for key, val in coefs.items():
        #print(key, val)
        if abs(val) > MAX_VALUE:  # Указываем пороговое значение
            #print(f"коэффициент {key} вне допустимого диапазона", file=sys.stderr), sys.exit(1)
            raise ValueError(f"коэффициент {key} вне допустимого диапазона")
            return 1
    return 0       
             
             
def proc_solve(a,b,c): # обработчик solve
    if checkK({"A": a, "B": b, "C": c}) == 0: # проверить_коэффициенты
        kind, d, roots = equation.solve ( a, b, c )    
        print( kind, d, roots)     
        return 0
        
        
    
def main(argv): #зачем мы передали argv??

    parser = cli.createParser()  
    args = parser.parse_args()  # 3. Разобрать параметры командной строки
    if args.gav is None:        # Команда не указана вывести справку, вернуть 0
        parser.print_help()
        return 0

    # стр 28-29
    # Вызов комманд
    print('выполнить',args.gav, end= ' ')
    try:
        if args.gav == "solve": # квадратное уравнение
            if (args.a == None) + (args.b == None) + (args.c == None) !=3:
                raise ValueError("ОШИБКА: укажите все три коэффициента либо ни одного")
                return 1
            
            if args.a is None and args.b is None  and args.c is None: # > solve 
                print('ввод c клавиатуры')
                a = inpInt('a'); b = inpInt('b'); c = inpInt('c')
            else:                                       # > solve -a 1 -b -3 -c 2         
                #print( args.a, args.b, args.c )
                a = args.a; b = args.b; c = args.c 
            return proc_solve(a,b,c)
        elif args.gav == "stats": # последовательность > stats --input numbers.txt
            return proc_stats(args.input)
##        else:       
##            raise ValueError(f"Неизвестная команда: {args.gav}")
##            return 1
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr) # в поток ошибок (sys.stderr)
        return 1            
    
            
    return 0
      
if __name__ == "__main__": # модуль запущен как программа, одна точка входа
    #print(__name__)
    r = main(sys.argv[1:]) # точка входа main(),
    print(f"код {r}") #  код возврата
    sys.exit(r)  # вернуть код ошибки 0 -ок

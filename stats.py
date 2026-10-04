import sys

def do():
    print('stats', sys.argv)
    if len(sys.argv) !=4:
        print(sys.argv[1],'Недостаточное количество аргументов')
    else:
        fn = sys.argv[3]
        try:
            with open(fn) as file:
                ar = []     # пустой массив для значений из файла 17ая задача ))
                for s in file: # s - число в строке как строка
                    ar.append(int(s))   # добавить цело число в маасив ar
                file.close()
                N = len(ar)
                S = sum(ar)
                SrAr = S/N
                Skv = sum(x**2 for x in ar)
                Crkv = (Skv/N) ** 0.5
                Disp = sum((x-SrAr)**2 for x in ar)/N
                CKO = Disp ** 0.5
                StOt = (sum((x-SrAr)**2 for x in ar)/(N-1)) ** 0.5
                ArMin = min(ar)
                ArMax = max(ar)
                Pol = len([x for x in ar if x > 0])
                Otr = len([x for x in ar if x < 0])
                
                print('Количество:', N)
                print('Сумма:', S)
                print('Среднее арифметическое:', SrAr)
                print('Сумма квадратов:', Skv)
                print('Среднее квадратическое:', Crkv)
                print('Дисперсия:', Disp)
                print('СКО:', CKO)
                print('Стандартное отклонение:', StOt)
                print('Наименьшее:', ArMin)
                print('Наибольшее:', ArMax)
                print('Положительных:', Pol)
                print('Отрицательных:', Otr)
                
                
                
        except FileNotFoundError:
            print(f'Ошибка: файл "{fn}" не найден.')
        except Exception:
            print(f'Произошла непредвиденная ошибка: {e}')
           
            
        

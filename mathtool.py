import sys
pred = 50
if len(sys.argv) == 1:
    print('Данная программа создана, чтобы быстро решать квадратные уравнения \nЗдесь используются различные функции, если хочется узнать, \nто обращайтесь в интернет')
else:
    otl = sys.argv[1]
    if otl == '--help':
        print('Данная программа создана, чтобы быстро решать квадратные уравнения \nЗдесь используются различные функции, если хочется узнать, \nто обращайтесь в интернет')
    if otl == 'solve':
        if len(sys.argv) != 2:
            if sys.argv[2] == '-a' and sys.argv[4] == '-b' and sys.argv[6] == '-c':
                try:
                    A = int(sys.argv[3])
                    B = int(sys.argv[5])
                    C = int(sys.argv[7])
                except ValueError:
                    print('ОШИБКА: ваш ввод не является целым числом',file=sys.stderr), sys.exit(1)
                if abs(A) > pred or abs(B) > pred or abs(C) > pred:
                    print('ОШИБКА: значение вне допустимого диапазона',file=sys.stderr), sys.exit(1)

        else:
            a = input('Введите число ')  # Вводим число с клавиатуры
            try:  # Проверяем,число ли это
                A = int(a)
            except ValueError:
                print("Я же сказал, введите число")
                print('ОШИБКА: ваш ввод не является целым числом',file=sys.stderr), sys.exit(1)

            if abs(A) > pred:  # Указываем пороговое значение
                print(f"Введите число соответствующее ограничениям: -{pred};{pred} ")
                print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr), sys.exit(1)

            b = input('Введите число ')
            try:  # Проверяем,число ли это
                B = int(b)
            except ValueError:
                print("Я же сказал, введите число"), print('ОШИБКА: ваш ввод не является целым числом',
                                                                  file=sys.stderr), sys.exit(1)
            if abs(B) > pred:  # Указываем пороговое значение
                print(f"Введите число соответствующее ограничениям: -{pred};{pred} ")
                print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr), sys.exit(1)

            c = input('Введите число ')
            try:  # Проверяем,число ли это
                C = int(c)
            except ValueError:
                print("Я же сказал, введите число")
                print('ОШИБКА: ваш ввод не является целым числом',file=sys.stderr), sys.exit(1)
            if abs(C) > pred:  # Указываем пороговое значение
                print(f"Введите число соответствующее ограничениям: -{pred};{pred} ")
                print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr), sys.exit(1)

        if A == 0:  # Рассматриваем случай,когда уравнение линейное
            if B == 0 and C != 0:
                print("Уравнение линейное")
                print("У уравнения нет корней")
                sys.exit(1)
            if B == 0 and C == 0:
                print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr), sys.exit(1)
            if B != 0 and C == 0:
                print("Уравнение линейное")
                print('X = 0')
                sys.exit(0)
            else:
                X = -C / B
                print("Уравнение линейное")
                print(f"X = {int(X):.3f}")
                sys.exit(0)

        if B == 0:  # Рассматриваем неполное квадравтное уравнение
            print("Неполное квадратное уравнение")
            if C > 0:
                print('У уравнения нет корней')
                sys.exit(1)
            else:
                if A != 0 and C == 0:
                    print('X = 0')
                    sys.exit(0)
                if A != 0 and C != 0:
                    x1 = ((-C / A) ** 0.5)
                    x2 = -((-C / A) ** 0.5)
                    print(f"x1 = {x1:.3f}"),print(f"x2 = {x2:.3f}")
                    sys.exit(0)
        print("Квадратное уравнение")

        d = B ** 2 - 4 * A * C  # Формула дискриминанта
        print('Дискриминант =', d)
        if d >= 0:  # При значении D >= 0
            x1 = (-B - d ** 0.5) / (2 * A)
            x2 = (-B + d ** 0.5) / (2 * A)
            print(f"x1 = {x1:.3f}")
            print(f"x2 = {x2:.3f}")


        if d < 0:  # В случае d < 0
            print("ОШИБКА: Дискриминант меньше нуля. Корней нет", file=sys.stderr), sys.exit(1)
            #raise Exception


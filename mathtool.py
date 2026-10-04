import sys
import solve
import stats


pred = 50
if len(sys.argv) == 1:
    print('Данная программа создана, чтобы быстро решать квадратные уравнения \nЗдесь используются различные функции, если хочется узнать, \nто обращайтесь в интернет')
else:
    otl = sys.argv[1]
    if otl == '--help':
        print('Данная программа создана, чтобы быстро решать квадратные уравнения \nЗдесь используются различные функции, если хочется узнать, \nто обращайтесь в интернет')
    elif otl == 'solve':
        solve.do(pred)
    elif otl == 'stats': # > python mathtool.py stats --input numbers.txt
        stats.do()

 

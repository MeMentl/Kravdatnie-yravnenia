def fCnt(ar):
    return len(ar)
def fSum(ar):
    return sum(ar)
def fAvg(ar):
    return sum(ar)/len(ar)

REPORT = [
    ("Количество",     fCnt,    "d"),
    ("Сумма",          fSum,    "d"),
    ("Ср. арифм.",     fAvg,    ".3f")
]


ar = [1,4,5]
for label, f, form in REPORT:
    value = f(ar)
    print(f"{label}: {value:{form}}")

##if value is None:
##        print(f"{label}: НЕ СУЩЕСТВУЕТ")

label ="хрень"
value =10
form =".3f" # опция
print(f"{label}: {value:{form}}")

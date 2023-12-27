def temperature(x):
    if x < 15.5: print("ХОЛОДНО")
    elif x > 28: print("ЖАРКО")
    else: print("НОРМАЛЬНО")

def cat():
    n = int(input())
    flag = False
    for i in range(n):
        s = input()
        if "кот" in s or "Кот" in s:
            flag = True
    if flag: print("МЯУ")
    else: print("НЕТ")

def words_and_letters():
    word = input()
    min = word
    max = word
    while True:
        word = input()
        if word == 'стоп':
            if len(set(min) - set(max)) == 0:
                print("ДА")
                break
            else :
                print("НЕТ")
                break
        if len(word) > len(max):
            max = word
        if len(word) < len(min):
            min = word

def buy():
    n = int(input())
    buy = []
    for i in range(n):
        buy.append(input())
    for i in range(n):
        print(buy[i])

def coldly(s):
    print(''.join([char*2 for char in s]))

def great():
    Name = input()
    Surname = input()
    print("Здравствуйте,", Name, Surname)

""" Остаточные знания: из опыта только пару курсов физфака
1) Основы программирования (на С)
2) Программирование на С++ и Python https://cpp-python-nsu.inp.nsk.su/program """

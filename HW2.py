def reverse_sort():
    num = []
    n = int(input())

    for i in range(n):
        num.append(int(input()))

    num.sort()
    num.reverse()
    return num

def fil():
    s = [] 
    N = int(input())

    for i in range(N):
        s.append(input())

    for sub in s:
        if sub[:4] == '####':
            continue 
        if sub[:2] == '%%':
            print(sub[2:])
        else:
            print(sub)

def from_to():
    N = int(input())
    num = []
    s = 0

    for i in range(N):
        num.append(int(input()))

    p = int(input()) - 1
    q = int(input()) - 1

    for i, x in enumerate(num):
        if p <= i <= q : 
            s += x
    return s

def Artek(s, n):
    s = s.split(", ")
    students = []

    for sub in s:
        if '5' in sub:
            sub = sub.replace(" 5", "")
            students.append(sub)

    students.sort()
    
    for i in range(n):
        print(students[i])

def password_level():
    numb = False
    spec = False
    s = input("Введите пароль: ")
    s1 = input("Подтвердите пароль: ")
    if s != s1: return "Пароль несовпадает"
    if '0' in s or '1' in s or '2' in s or '3' in s or '4' in s or '5' in s or '6' in s or '7' in s or '8' in s or '9' in s: numb = True
    if '@' in s or '#' in s or '$' in s or '%' in s or '&' in s or '*' in s or '(' in s or ')' in s or '.' in s or ',' in s or '-' in s or '_' in s or '+' in s: spec = True
    if s.isdigit() or s.isalpha() and s.islower() or s.isalpha() and s.isupper(): return "Ненадежный пароль"
    if s.isalpha() and not s.islower() and not s.isupper() or numb and s.isupper() and not spec or not spec and numb and s.islower(): return "Слабый пароль"
    if any(ch.islower() for ch in s) and any(ch.isupper() for ch in s) and numb and spec: return "Надежный пароль"
    else: return "Недопустимый пароль"

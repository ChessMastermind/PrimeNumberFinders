def tree(n):
    tree = []
    for i in range(int(n - 1), int(n + 1)):
        for x in range(2, int(i ** 0.5 + 1)):
            if i%x == 0:
                break
        else:
            tree.append(i)
    return tree
def check_for_prime_number(i):
    global t
    if i <= 2:
        if i == 2:
            return 1
        else:
            return 0
    hhhh = tree(i)
    if i in hhhh:
        return 1
    else:
        return 0
def f(a,b,c):
    r = []
    d = []
    p = True
    for x in range(0,100):
        if check_for_prime_number(a*x**2+b*x+c) == 1 and p:
            r.append(a*x**2+b*x+c)
            d.append(a*x**2+b*x+c)
        elif check_for_prime_number(a*x**2+b*x+c) == 1:
            d.append(a*x**2+b*x+c)
        else:
            p = False
    r=list(set(r))
    d=list(set(d))
    return len(r),len(d)
w_max = 0
w1_max = 0
recordw =""
recordw1 =""
for a in range(0,100):
    for b in range(-150,150):
        for c in range(0,1000):
            result = f(a,b,c)
            w,w1 = result
            if w > w_max:
                w_max = w
                recordw = f"{a}x^2 + {b}x + {c} {w}"
            if w1 > w1_max:
                w1_max = w1
                recordw1 = f"{a}x^2 + {b}x + {c} {w1}"
            print(f"Concecutive: {recordw} ||  {recordw1}      {a}x^2 + {b}x + {c} {w}")
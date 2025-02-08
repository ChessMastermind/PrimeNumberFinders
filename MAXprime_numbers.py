from os import system

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
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

system("")
while True:
    while True:
        i = input("n = ")
        if i.isdigit() == True:
            break
        print(style.RED + "Allowed symbols: (0-9)")
        print("      Try again  " + style.WHITE)
    system("cls")
    print("n = " + style.GREEN + i + style.WHITE)
    prime = "???"
    not_prime = []
    print(style.YELLOW + "Prime number: " + style.WHITE, end="")
    a = int(i)
    b = int(i)
    if is_int(i) == True:
        i = int(i)
        if check_for_prime_number(i) == 1:
            prime = "Prime"
        else:
            prime = "Not Prime"
    else:
        prime = "Float"
    if prime == "Prime":
        print(style.GREEN + "Yes" + style.WHITE)
    elif prime == "Not Prime":
        print(style.RED + "No" + style.WHITE)
        print(style.YELLOW +"Divided into prime numbers: " + style.WHITE, end="")
        code = i
        n = 1
        while code > 1:
            if code % n == 0:
                a = a/n
                print(style.GREEN + str(n) + style.CYAN + " (" + str(int(a)) +")" + style.WHITE, end="")
                not_prime.append(n)
            
                code = code/n
            else:
                n += 1
            if n == 1:
                n = 2
            if code % n == 0:
                print(" * ", end="")
        print()
    else:
        print(style.RED + "No" + style.WHITE)
    print(style.YELLOW + "Description of number " + style.MAGENTA + str(i) + style.YELLOW + ":" + style.WHITE)
    print(style.MAGENTA + str(i) + style.YELLOW, end=" ")
    if is_int(i) == True:
        print("- natural,", end=" ")
    else:
        print("- fractional,", end=" ")
    if prime == "Prime":
        print("Prime number. Dividing by: "  + style.WHITE + "1 and " + str(i), end=" ")
    elif prime == "Not Prime":
        
        if b < 100000000:
            print("compound number. Dividing by:"  + style.WHITE, end=" ")
            for x in range(1, b+1):
                if b % x == 0:
                   print(str(x) + ",", end=" ")
        else:
            print("compound number."  + style.WHITE, end=" ")
    else:
        print("compound number. When rounded, the result will be: "  + style.WHITE + str(int(round(float(i)))), end=". ")
    print("\n")
    


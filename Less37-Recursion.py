print('============Less37-Recursion===============')
print('===========fibonacci================')
#0+1+1+2+3+5+8+13+21+34+55+89
def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(7))
def power(x, n): # x = base, n = power
    if n== 0:
        return 1
    elif n < 0:
        return 1/power(x,abs(n))
    else:
        ans = 1
        while n > 0:
            if n%2 == 1:
                ans *= x
                n -= 1
            else:
                n //= 2
                x *= x
        return ans

from time import time
x = 467346574347465458475847534857834758435734
n = 101
start = time()
power(x,n)
end = time()

print(f"{((end - start)*1000):.3f} milli-sec")
start = time()
pow(x,n)
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

print(power(5,-67))
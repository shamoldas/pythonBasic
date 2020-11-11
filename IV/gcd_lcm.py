a = int(input('input first number\n'))
b = int(input('second number\n'))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return (b*a)/gcd(a, b)
print("two input number:",a,b)
print("GCD:",gcd(a, b))
print("LCM:",lcm(a, b))

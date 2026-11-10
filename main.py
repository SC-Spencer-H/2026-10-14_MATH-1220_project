import math

# 1) Approximate arc length of sinx on [0, pi/2]
b = math.pi / 2
a = 0

## 1.1) Midpoint rule, n = 2
n = 2
result = 0
deltaX = (b - a) / n

for i in range(n):
    x = a + i*deltaX + deltaX/2
    fx = math.sqrt(1 + math.cos(x)**2)
    result += fx*deltaX

print()
print("1.1) Arc length of sin on [0, pi/2] approximation, Midpoint rule, n = 2")
print(result)
print()

## 1.2) Trapezoidal rule, n = 2
n = 2
result = 0
deltaX = (b - a) / n

for i in range(n):
    xl = a + i*deltaX
    xr = a + (i+1)*deltaX
    fxl = math.sqrt(1 + math.cos(xl)**2)
    fxr = math.sqrt(1 + math.cos(xr)**2)
    result += fxl
    result += fxr

result /= 2
result *= deltaX

print("1.2) Arc length of sin on [0, pi/2] approximation, Trapezoidal rule, n = 2")
print(result)
print()

## 1.3) Midpoint rule, 6 decimal precision
n = 1271
result = 0
deltaX = (b - a) / n

for i in range(n):
    x = a + i*deltaX + deltaX/2
    fx = math.sqrt(1 + math.cos(x)**2)
    result += fx*deltaX

print("1.3) Arc length of sin on [0, pi/2] approximation,, Midpoint rule, 6 decimal precision")
print(result)
print()

## 1.4) Trapezoidal rule, 6 decimal precision
n = 1798
result = 0
deltaX = (b - a) / n

for i in range(n):
    xl = a + i*deltaX
    xr = a + (i+1)*deltaX
    fxl = math.sqrt(1 + math.cos(xl)**2)
    fxr = math.sqrt(1 + math.cos(xr)**2)
    result += fxl
    result += fxr

result /= 2
result *= deltaX

print("1.4) Arc length of sin on [0, pi/2] approximation,, Trapezoidal rule, 6 decimal precision")
print(result)
print()

# 2) Simpson's rule numerical integration
b = 1/4
a = 0
n = 4
deltaX = (b - a) / n

Sn = 0
for i in range(n + 1):
    xi = a + deltaX * i
    fxi = 1 / (1 + xi)

    if i == 0 or i == n:
        fxi *= 1
    elif i % 2 == 0:
        fxi *= 2
    else:
        fxi *= 4

    Sn += fxi

Sn *= deltaX / 3

print("2) Simpson's rule approximation of ln(5/4), n = 4")
print(Sn)
print()

# 3) Power series derivation through integration
n = 100
x = 1/4

print("3) Power series approximation of ln(5/4)")

Sn = 0
for i in range(1, n + 1):
    gxi = x**i
    gxi /= i
    gxi *= (-1)**(i - 1)
    Sn += gxi

    if i % 10 == 0:
        print("S_%s = %s" % (i, Sn))

print()

# 4) Taylor series convergence

n = 100_000
x = 1

print("4) Power series approximation of 4*atan(1)")

Sn = 0
for i in range(0, n + 1):
    gxi = x**(2*i + 1)
    gxi /= (2*i + 1)
    gxi *= (-1)**i
    Sn += gxi

    if i % 1000 == 0:
        print("S_%s = %s" % (i, 4*Sn))

print()
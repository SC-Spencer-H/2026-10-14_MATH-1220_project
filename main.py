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
print("1.1) Midpoint rule, n = 2")
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

print("1.2) Trapezoidal rule, n = 2")
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

print("1.3) Midpoint rule, 6 decimal precision")
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

print("1.4) Trapezoidal rule, 6 decimal precision")
print(result)
print()

# 2) Simpson's rule numerical integration
# 3) Integral approximation of power series
# 4) Taylor series convergence
print("--- Exam Eligibility Check ---")
attended = 80
total_classes = 100
percentage = (attended / total_classes) * 100
if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

print("\n--- Electricity Bill ---")
units = 250
bill = 0
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
print("Electricity Bill:", bill)

print("\n--- Customize Your Ride ---")
choice = 2
if choice == 1:
    print("You chose Bike")
elif choice == 2:
    print("You chose Car")
elif choice == 3:
    print("You chose Scooter")
else:
    print("Invalid Choice")
print("--- Check Age ---")
age = 20
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
    
n = 5
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)

print("\n--- Reverse a String ---")
s = "Hello"
rev_s = ""
for i in range(len(s)-1, -1, -1):
    rev_s += s[i]
print("Reversed String:", rev_s)

print("\n--- Reverse Order ---")
numbers = [1, 2, 3, 4, 5]
rev_numbers = []
for i in range(len(numbers)-1, -1, -1):
    rev_numbers.append(numbers[i])
print("Reversed List:", rev_numbers)

print("\n--- Power Calculator ---")
base = 2
exponent = 5
result = 1
for i in range(exponent):
    result *= base
print(base, "raised to the power", exponent, "is", result)
# Activity: Natural Numbers Sum
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of first {n} natural numbers = {total}")
# infinity loop
# while True:
#     print("Hello World")

# ACP: Armstrong Number
num = int(input("Enter a number: "))
sum_of_cubes = 0
temp = num
while temp > 0:
    digit      = temp % 10
    sum_of_cubes += digit ** 3
    temp      //= 10
if sum_of_cubes == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")

# character occurance
text = "banana"
character = "a"

count = 0

for i in text:
    if i == character:
        count = count + 1

print("Character occurrence:", count)

print("\n--- Is this a Prime Number ---")
prime_check = 29
is_prime = True
if prime_check < 2:
    is_prime = False
else:
    for i in range(2, int(prime_check ** 0.5) + 1):
        if prime_check % i == 0:
            is_prime = False
            break
if is_prime:
    print(prime_check, "is Prime")
else:
    print(prime_check, "is not Prime")
    
print("\n--- Mid Product ---")
a = 10
b = 20
print("Mid product:", (a * b) // 2)

print("\n--- Binary Conversion ---")
dec = 19
binary = ''
temp = dec
while temp > 0:
    binary = str(temp % 2) + binary
    temp //= 2
print("Binary of", dec, "is", binary)


print("\n--- Right Angle Triangle ---")
n = 5
for i in range(1, n+1):
    for j in range(i):
        print('*', end=' ')
    print()
    
print("\n--- Floyd's Triangle ---")
rows = 5
num = 1
for i in range(1, rows+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

print("\n--- Diamond Pattern ---")
n = 5
for i in range(n):
    print(' '*(n-i-1) + '*'*(2*i+1))
for i in range(n-2, -1, -1):
    print(' '*(n-i-1) + '*'*(2*i+1))

print("\n--- Mirrored Triangle ---")
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()
    
    
print("\n--- Polygon (Square) ---")
n = 5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

print("\n--- Spiral Pattern (3x3) ---")
n = 3
matrix = [[0]*n for _ in range(n)]
left, right, top, bottom = 0, n-1, 0, n-1
num = 1
while left <= right and top <= bottom:
    for i in range(left, right+1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom+1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left-1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top-1, -1):
        matrix[i][left] = num
        num += 1
    left += 1
for row in matrix:
    print(' '.join(map(str,row)))

print("\n--- Square Pattern ---")
n = 5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()
        
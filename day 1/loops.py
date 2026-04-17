#while loop
i=1
print("Numbers from 1 to 10:")
while i <= 10:
    print(i)    
    i += 1

print("Even numbers from 20 to 40:")
while i <= 40:
        if i % 2 == 0:
            print(i)
        i += 1

numbers=[3,7,13,19,23,12]
total=0
product=1
print("Printing the numbers in the list:")
for num in numbers:
    print(num)
for num in numbers:
    total += num
print(f"Sum of all the numbers: {total}")

for num in numbers:
    product *= num
print(f"Product of all the numbers: {product}")
numbers = []
n = int(input("enter how many numbers: "))

for i in range(n):
    num = int(input(f"enter number {i+1}: "))
    numbers.append(num)
print(f"original list: {numbers}")

total =sum(numbers)
print(f"sum= {total}")
print(f"average= {total/len(numbers)}")
print(f"maximum= {max(numbers)}")
print(f"minimum= {min(numbers)}")
new =set(numbers)
print(f"without duplicates:{new}")

print(f"sorted asc:{sorted(new)}")
print(f"sorted desc:{sorted(new, reverse=True)}")

evens =  [x for x in new if x%2 ==0]
odds =  [x for x in new if x%2 !=0]
print (f"even numbers: {evens}")
print (f"odd numbers: {odds}")
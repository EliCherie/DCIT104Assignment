userInput = int(input("Please enter your integer: "))
sum = 0
lists = []
check = []
for number in range(2, userInput):
    lists.append(number)
for x in range(2, len(lists)+1):
    for item in lists:
        if(item != x):
            if (int(item % x) == 0):
                check.append(item)
final = list(set(lists)-set(check))
for prime in final:
    sum = sum + prime
print(f"The sum of numbers less than {userInput} is {sum}")

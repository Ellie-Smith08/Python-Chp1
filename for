# total = 0
# for i in range(1,101):
#     print(i)
#     total += i
# print(total)
# 
# number = int(input("What number do u want the times table for:"))
# 
# for i in range(1,11):
#     answer = number * i
#     print(number,"x",i,"=",answer)
    
# for num in range(1,51):
#     if num % 15 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
# 



number = int(input("What number do u want the times table for:"))

for i in range(1,11):
    answer = number * i
    if answer == 49:
        continue 
    print(number,"x",i,"=",answer)
    

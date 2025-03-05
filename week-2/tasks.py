# Write a function that sums numbers in a list.
def sumOfList():
  n=int(nput("How many elements? "))
  numbers=[]
  sumOfNums=0
  for i in range(n):
    num=int(input("Enter the element: "))
    numbers.append(num)
    sumOfNums+=num
  return sumOfNums
print(sum_of_list())
    
# Print even numbers between 1 and 20 using a loop.
def print_Evens():
  for i in range(1,20):
    if i % 2 == 0:
      print(i)
print_Evens()

# Write a program to find the largest number in a list.
def find_max():
   n=int(input("How many elements? "))
  numbers = [int(input("Enter the element: ")) for _ in range(n)]
  max_num=numbers[0]
  for num in numbers:
        if num > max_num:
            max_num = num
 return max_num
print(find_max())
  
  

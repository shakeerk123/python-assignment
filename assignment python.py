#!/usr/bin/env python
# coding: utf-8

# # Write a function to find the maximum element in a array

# In[1]:


def names(arr):
    max_elem=arr[0]
     
    for elem in arr:
        if elem>max_elem:
            max_elem=elem
    return max_elem
arrays=[1,2,3,6]
max_elem=names(arrays)
print(max_elem)


# # Write a function to reverse a string 

# In[ ]:


def string_reverse(strings):
    return strings[::-1]
    
stringss=str(input("enter a string"))
reverseElem=string_reverse(stringss)
print(reverseElem)


# # Write a function to sort a array in ascending order

# In[ ]:


def ascending(listt):
    return sorted(listt)
arr=[1,3,22,4,2,45,3]
sorted_array=ascending(arr)
print(sorted_array)


# # Write a function to calculate the sum of all even numbers between 1 and n.

# In[ ]:


def calculate_sum_of_even(num):
    sum=0
    for elem in range(0,num+1,2):
        sum=sum+elem
    print(sum)
num=10 
calculate_sum_of_even(num)


# # Write a function to check if a given number is prime.

# In[ ]:


def prime_num(num):
    count=0
    for elem in range(1,num+1):
        if num % elem == 0  :
            count+=1
    if count==2:
        print("prime number")
    else:
        print("not prime num")
    
num=int(input("enter a number"))

prime_num(num)


# # Write a function to find the second largest number in a array.

# In[ ]:


def second_large(arr):
    arr.sort()
    print("Second largest element is",arr[-2])

arr=[1,3,4,5,4,7]
second_larg=second_large(arr)


# # Write a function to remove duplicates from a array

# In[ ]:


def remove_duplicates(arr):
    
    return list(set(arr))

arr = [1, 2, 3, 3, 4, 5, 5]
unique_arr = remove_duplicates(arr)
print(unique_arr) # Output: [1, 2, 3, 4, 5]


# # Write a function to calculate the sum of all numbers in a array

# In[ ]:


def calculate_sum(arr):
    return sum(arr)
arr = [4, 21, 3, 4,55]
total = calculate_sum(arr)
print(total) # Output: 15


# # Write a function to generate all prime numbers up to a given limit
# 

# In[ ]:


def generate_primes(limit):
   
    primes = [True] * (limit + 1)  
    primes[0] = primes[1] = False 
    
    for i in range(2, int(limit /2) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    
    return [i for i in range(2, limit + 1) if primes[i]]


limit = int(input("enter a number to find the prime number limit :"))
primes = generate_primes(limit)
print(primes)


# # Write a program to find the maximum and minimum elements in an array of integers.

# In[ ]:


def find_max_min(arr):

    max_num = arr[0]
    min_num = arr[0]
   
    for num in arr[1:]:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return (max_num, min_num)

arr = [5, 1, 9, 3, 7]
max_num, min_num = find_max_min(arr)
print("Maximum number:", max_num) 
print("Minimum number:", min_num) 


# # Write a function to calculate the factorial of a given number n

# In[ ]:


def calculate_factorial(n):
   
    if n == 0:  
        return 1
    else: 
        for i in range(1,n):
            n=n*i
        return  n

n = int(input("enter a num to find its factorial:"))
factorial = calculate_factorial(n)
print("the factorial is :",factorial) 


# # Write a function to check given string is palindrome or not.

# In[ ]:


def is_palindrome(s):
    s=s.lower()
    return s == s[::-1]

s = input("enter a num to check its palidrome :")
if is_palindrome(s):
    print("The string is  palindrome.")
else:
    print("The string is not  palindrome.")


# # Write a function to check if a given number is an Armstrong number.

# In[ ]:



def is_armstrong_number(n):
    
    
    num_digits = len(str(n))

    
    sum_of_cubes = 0
    for digit in str(n):
        sum_of_cubes =sum_of_cubes + int(digit) ** num_digits
    return sum_of_cubes == n
    
n = int(input("enter a num to check it is armstrong or not "))
if is_armstrong_number(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")


# # A program to print the Fibonacci series.

# In[ ]:


def fibonacci(n):

    fib_series = [0, 1]


    while fib_series[-1] + fib_series[-2] <= n:
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series

n = int(input("enter the num to find its fibonacci :"))
fib_series = fibonacci(n)
print(fib_series)


# # Write a program to find the sum of all prime numbers up to a given limit.

# In[ ]:


def is_prime(n):
    
    for i in range(2, int(n /2) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_primes(limit):
   
    sum_of_primes = 0

    for i in range(2, limit + 1):
        if is_prime(i):
            sum_of_primes += i

    return sum_of_primes

limit = int(input("enter the limit:"))
sum = sum_of_primes(limit)
print(f"The sum of all prime numbers up to {limit} is {sum}.")


# # Write a program to find the sum of all the multiples of 3 or 5 below a given number.
# 

# In[ ]:



def sum_of_multiples(n):
   
    sum_of_multiples = 0

    
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i

    return sum_of_multiples


n = int(input("enter the limit :"))
sum = sum_of_multiples(n)
print(f"The sum of all multiples of 3 or 5 below {n} is {sum}.")


# # Write a program to find the sum of all the even or odd numbers below a given number.

# In[ ]:


def sum_of_numbers(n, even=True):

    sum_of_numbers = 0


    for i in range(n):
        if even and i % 2 == 0:
            sum_of_numbers += i
        elif not even and i % 2 != 0:
            sum_of_numbers += i

    return sum_of_numbers



n = int(input("enter the limit:"))
even_sum = sum_of_numbers(n)
odd_sum = sum_of_numbers(n, False)
print(f"The sum of all even numbers below {n} is {even_sum}.")
print(f"The sum of all odd numbers below {n} is {odd_sum}.")


# # Write a program to find the union of two arrays of integers.

# In[ ]:


def array_union(arr1, arr2):
   
    union_set = set(arr1 + arr2)

   
    union_list = sorted(list(union_set))

    return union_list


array1 = [1, 3, 5, 7]
array2 = [2, 3, 4, 6]
union = array_union(array1, array2)
print(f"The union of {array1} and {array2} is {union}.")


# # Write a program to find the sum of the digits of a given number.

# In[ ]:


def digit_sum(number):   
    digits = list(str(number))
    digit_sum = 0   
    for digit in digits:
        digit_sum += int(digit)
    return digit_sum

number = 12345
sum_of_digits = digit_sum(number)
print(f"The sum of the digits of {number} is {sum_of_digits}.")


# # Write a program to count the number of vowels in a given string.
# 

# In[ ]:


def count_vowels(string):
   
    
    vowels = set("aeiouAEIOU")

   
    vowel_count = 0

  
    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count


string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"There are {vowel_count} vowels in the string '{string}'.")


# In[ ]:





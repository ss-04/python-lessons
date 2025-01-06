import re
import csv
import string
from collections import Counter

#import paramiko

def dgt_int():
	str = '083g3wj3j32'

	digits = re.findall(r'\d', str)
	digits_as_string = ''.join(digits)

	strr = re.findall(r'[a-zA-z]+', str)
	strr_as_string = ''.join(strr)

	print(digits)
	print(digits_as_string)
	print(strr)
	print(strr_as_string)
	
print(dgt_int())
	
def reverse_str(s):
	return s[::-1]
	
print(reverse_str("hello"))

#Write a Python function to count the number of occurrences of a specific word in a string.
def count_occurences(text, word):
	text = text.translate(str.maketrans('', '', string.punctuation))

	return text.lower().split().count(word.lower())

print(count_occurences("This is a sample text with the word sample occurring twice: sample.","twice"))

#Write a Python script to process a CSV file and extract specific information
# def process_csv(file_path):
#     with open(file_path, mode='r') as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             # Assuming the CSV has columns: Name, Age, Country
#             name, age, country = row
#             if int(age) > 30:  # Example condition
#                 print(f"Name: {name}, Age: {age}, Country: {country}")

# # Example usage
# process_csv("sample_data.csv")

#Write a Python script that connects to a given server via SSH and runs a command.
# def ssh_connect(host, username, password, command):
#     # Create an SSH client
#     client = paramiko.SSHClient()
    
#     # Automatically add host key if missing
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
#     try:
#         # Connect to the server
#         client.connect(host, username=username, password=password)
        
#         # Execute the command
#         stdin, stdout, stderr = client.exec_command(command)
        
#         # Output the result
#         print(stdout.read().decode())
        
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         # Close the SSH connection
#         client.close()

# # Example usage
# ssh_connect("192.168.1.100", "user", "password", "ls -l")

#Write a function that counts the occurrences of each character in a string.
def ch_count(str):
    count = {}
    for char in str:
        count[char] = count.get(char, 0) + 1
    return count

print(ch_count("hellooooreeee"))

#Write a function that takes a string as input and returns a string with all vowels removed.
def strWithoutVowels(str):
	vowels = "aeiouAEIOU"

	return ''.join([char for char in str if char not in vowels])

print(strWithoutVowels("hello, world!"))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function
print(is_prime(30))  # O

#Given an array of integers, find the largest number.
def largest_num(arr: list) -> int:
    return max(arr);

#arr = [3, 5, 7, 2, 8, 6]
print(largest_num([3, 5, 7, 2, 8, 6]))

#fizzbuzz
def fizbuzz(n):
	for i in range(1, n+1):
		if i % 3 == 0 and i % 5 == 0:
			print("fizzBuzzzzz")     
		elif i % 3 == 0:
			print("fizz")
		elif i % 5 == 0:
			print("buzz")
		else:
			print(i)
fizbuzz(35)

#string is palindrome
def isPalindrome(s: str) -> bool:
	return s == s[::-1]

print(isPalindrome("madam"))

#Given a list of integers from 1 to n with one number missing, find the missing number.
def find_missing_number(nums: list, n: int) -> int:
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

arr = [1, 2, 3, 4, 6]
n = 6
print(find_missing_number(arr, n))

#Merge two sorted lists into one sorted list.
def merge_sorted_lists(list1: list, list2: list) -> list:
    merged_list = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append remaining elements of list1 or list2
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2)) 

#Given a string, find the first non-repeating character
def find_non_repeating_ch(s: str) -> str:
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

print(find_non_repeating_ch("swwaatthhi"))

#binary search
def binary_search(arr: list, target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 5
print(binary_search(arr, target))

#Write a function to find all the permutations of a string.
from itertools import permutations

def string_permutations(s: str):
    return [''.join(p) for p in permutations(s)]

# Example usage:
input_string = "abcc"
print(string_permutations(input_string))  

#approach 2 without permuations
def generate_permutations(s: str) -> list:
    # Base case: If the string is empty or has only one character, return it as the only permutation.
    if len(s) <= 1:
        return [s]
    
    # List to store all permutations
    permutations = []
    
    # Loop through every character in the string
    for i in range(len(s)):
        # Remove the current character (to get the remaining string)
        remaining = s[:i] + s[i+1:]
        
        # Recursively find all permutations of the remaining characters
        for perm in generate_permutations(remaining):
            # Add the current character back to each of the permutations
            permutations.append(s[i] + perm)
    
    return permutations

# Example usage:
input_string = "abc"
result = generate_permutations(input_string)
print(result)  
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

#Find the k-th largest element in an unsorted array.
import heapq

def kth_largest(arr: list, k: int) -> int:
    return heapq.nlargest(k, arr)[-1]

# Example usage:
arr = [3, 2, 1, 5, 6, 4]
k = 3
print(kth_largest(arr, k))

#Check if an array is sorted in non-decreasing order.
def is_sorted(arr: list) -> bool:
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Example usage:
arr = [7,1, 2, 3, 4, 5]
print(is_sorted(arr))

 #Sample dictionary
my_dict = {'banana': 3, 'apple': 4, 'orange': 2, 'grape': 5}

# Sort the dictionary by keys
sorted_dict = dict(sorted(my_dict.items()))

print(sorted_dict)
# Output: {'apple': 4, 'banana': 3, 'grape': 5, 'orange': 2}
# Sort the dictionary by values
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_by_value)

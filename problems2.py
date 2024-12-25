#You are given a list of strings. Write a function that sorts the strings by their length in ascending order. If two strings have the same length, they should be sorted alphabetically. 
def sort_names(s):
    return sorted(s, key=lambda x: (len(x), x))

lst = ["banana", "apples", "amrudh", "dragonfruit", "chickoo", "kiwi"]
print(sort_names(lst))

#You are given a list of numbers, and you need to: Sort the list in ascending order. Remove any duplicate numbers.
def sort_and_remove_dups(numbers):
    return sorted(set(numbers))

print(sort_and_remove_dups([7,1, 2, 3, 4, 5,1,2,3]))

#Imagine that you want to remove duplicates from a list of numbers, but you want to square each number first before removing duplicates and sorting.
def square_and_sort(numbers):
    squared_num = map(lambda x : x**2, numbers)

    return sorted(set(squared_num))
print(square_and_sort([7,1, 2, 3, 4, 5,1,2,3]))

#You are given a list of numbers. Sort the list in ascending order and find the median value. If the list has an even number of elements, return the average of the two middle elements.
def sort_and_find_median(numbers):
    
    sorted_num = sorted(set(numbers))
    
    n = len(sorted_num)

    # If the number of elements is odd, return the middle element
    if n % 2 != 0:
        median = sorted_num[n // 2]
    # If the number of elements is even, return the average of the two middle elements
    else:
        median = (sorted_num[n // 2 - 1] + sorted_num[n // 2]) / 2
    
    return median
print(sort_and_find_median([7,1, 2, 3, 4,8,9]))
print(sort_and_find_median([4,1, 2, 3]))

#You are given a list of tuples where each tuple contains a name and an age. Write a function that sorts the list first by age in ascending order and then by name in alphabetical order in case of ties in age.
def sort_by_age_and_name(people):
    # Sort by age first, and then by name alphabetically in case of ties
    return sorted(people, key=lambda x: (x[1], x[0]))

people = [("Alice", 30), ("Bob", 25), ("Charlie", 30), ("David", 20)]
sorted_people = sort_by_age_and_name(people)
print(sorted_people)

#approach2
from operator import itemgetter

def sort_by_age_and_name_app2(people):
    return sorted(people, key=itemgetter(1, 0))

people = [("Alice", 30), ("Bob", 25), ("Charlie", 30), ("David", 20)]
sorted_people = sort_by_age_and_name_app2(people)
print(sorted_people)

#sort and group by length
def sort_and_group_by():
    from itertools import groupby

    words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
    words_sorted = sorted(words, key=lambda x: len(x))  # Sort by length first
    print(words_sorted)
    grouped = groupby(words_sorted, key=lambda x: len(x))  # Group by length

    for key, group in grouped:
        print(key, list(group))

sort_and_group_by()

#You are given a list of integers. Sort the list in ascending order and return a dictionary where the keys are the numbers and the values are the counts of how many times each number appears in the list.
from collections import Counter

def sort_and_count(numbers):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Use Counter to count occurrences of each number
    counts = Counter(sorted_numbers)
    print(counts)

    # Convert to dictionary and return
    return dict(counts)

# Example usage
numbers = [4, 2, 2, 8, 3, 3, 3, 1, 2, 4]
result = sort_and_count(numbers)
print(result)

#approach 2 without counter
def sort_and_count(numbers):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Create an empty dictionary to store the counts
    counts = {}
    
    # Count the occurrences
    for num in sorted_numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    return counts

# Example usage
numbers = [4, 2, 2, 8, 3, 3, 3, 1, 2, 4,8]
result = sort_and_count(numbers)
print(result)

#You are given a list of dictionaries, each containing name and age keys. Sort the list by the age key in descending order. If two people have the same age, sort them by name in ascending order.
def sort_by_age(people):
    return sorted(people, key=lambda person: (-person['age'], person['name']))

people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 30}, {'name': 'David', 'age': 20}]
print(sort_by_age(people))

#You are given a list of numbers. Write a function to sort the list in descending order and return the result.
def reverse_sort_numbers(numbers):
    return sorted(numbers, key=lambda x: -x)

numbers = [1, 8, 5, 2, 9, 3]
print(reverse_sort_numbers(numbers))

#sort in reverse app2
def reverse_sort_numbers_app2(numbers):
    return sorted(numbers, reverse=True)

numbers = [1, 8, 5, 2, 9, 3]
print(reverse_sort_numbers_app2(numbers))

#same for names but doesnt work as expected
def reverse_sort_names(names):
    return sorted(names, key=lambda x: x[::-1], reverse=True)

names = ["amy","jack","bob","anna","pat"]
print(reverse_sort_names(names))

#You are given a list of tuples where each tuple contains (name, age, salary). Sort the list first by age in ascending order, and if two people have the same age, sort them by salary in descending order.
def sort_by_age_and_salary(people):
    return sorted(people, key=lambda x: (x[1], -x[2]))

people = [("Alice", 30, 50000), ("Bob", 25, 70000), ("Charlie", 30, 60000), ("David", 25, 50000)]
print(sort_by_age_and_salary(people))

#Write a function that finds the kth largest number in a list of integers. You can sort the list and return the kth element.
def find_kth_elem(numbers, k):
    sorted_numbers = sorted(numbers, reverse=True) # sort in dsc
    #sorted_numbers = sorted(numbers, reverse=False)  # sort in asc
    print(sorted_numbers)
    return sorted_numbers[k-1]

numbers = [10, 4, 3, 7, 1, 9, 2]
k = 3
print(find_kth_elem(numbers, k))

#You are given a list of strings. Sort the list by the last character of each string in ascending order.
def reverse_sort_strings(words):
    return sorted(words, key=lambda x: x[-1])

words = ["apple", "banana", "grape", "kiwi"]
print(reverse_sort_strings(words))

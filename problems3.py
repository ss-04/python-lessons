#Given a list of words, sort the list first by the length of each word in ascending order. If two words have the same length, sort them alphabetically.
def sort_words_by_length_and_asc(words):
    return sorted(words, key= lambda x: (len(x), x))

#words = ["apple", "banana", "kiwi", "cherry", "mango"]
words = ["dog", "cat", "elephant", "bat", "zebra", "ant"]
print(sort_words_by_length_and_asc(words))

#You are given a list of numbers. Sort the list in ascending order and remove any negative numbers.
def sort_and_remove_negative(numbers):

    return list(filter(lambda x: x >= 0, sorted(numbers)))

    #OR
    # positive_numbers = [num for num in sorted(numbers) if num >= 0]
    # return positive_numbers

numbers = [1, -3, 4, 0, -2, 5, 7]
print(sort_and_remove_negative(numbers))

#You are given a list of integers. First, square each element, then sort the resulting list in ascending order.
def square_and_sort(numbers):

    return sorted(map(lambda x : x**2, numbers))

numbers = [1, 3, 4, 0, 2, 5, 7]
print(square_and_sort(numbers))

#You are given a list of tuples where each tuple contains (name, score, age). Sort the list first by score in descending order, and if two scores are the same, sort by age in ascending order.
def sort_by_score_and_age(students):
    return sorted(students, key= lambda person:(-person[1], person[2]))


students = [("Alice", 90, 30), ("Bob", 85, 25), ("Charlie", 90, 25), ("David", 80, 35)]
print(sort_by_score_and_age(students))

#Given a list of words, group the words by their first character and return the result as a dictionary where the keys are the characters and the values are lists of words starting with that character.
def group_by_first_char(words):
    from itertools import groupby

    words_sorted = sorted(words, key=lambda x: x[0])  # Sort by length first
    print(words_sorted)
    grouped = groupby(words_sorted, key=lambda x: x[0])  # Group by length

    grouped_dict = {key: list(group) for key, group in grouped}
    
    return grouped_dict

words = ["apple", "banana", "cherry", "avocado", "blueberry"]
print(group_by_first_char(words))

#approach 2
from collections import defaultdict

def group_words_by_first_char(words):
    grouped_words = defaultdict(list)  # Initialize a defaultdict where each value is a list
    
    for word in words:
        grouped_words[word[0]].append(word)
    
    return dict(grouped_words)  # Convert defaultdict to regular dict before returning

words = ["apple", "banana", "cherry", "avocado", "blueberry", "carrot", "date"]
result = group_words_by_first_char(words)
print(result)

#You are given a list of tuples where each tuple contains a name and an age. Sort the list alphabetically by name in ascending order.
def sort_by_name(people):
    return sorted(people, key= lambda person:(person[0]))

people = [("Jack", 24),("Dave", 34),("Alice", 30), ("Bob", 25), ("Charlie", 35), ("David", 20)]
print(sort_by_name(people))

#You are given a list of integers. Find the most frequent element in the list. If multiple elements have the same frequency, return the one that appears first in the list.
def most_frequent(numbers):
    from collections import Counter

    freq = Counter(numbers)
    return max(numbers, key=lambda x: (freq[x], -numbers.index(x)))

numbers = [4, 2, 2, 8, 3, 3, 3, 1, 2, 4]
print(most_frequent(numbers))

#You are given a list of integers. Sort the list in ascending order and return the unique elements along with their counts.
def count_unique(numbers):
    from collections import Counter
    
    counts = Counter(numbers)
    unique_elements = {num: count for num, count in counts.items() if count == 1}

   # sorted_unique_elements = sorted(counts.items())  returns all elemnts with occurences
    sorted_unique_elements = sorted(unique_elements.items())

    return sorted_unique_elements

numbers = [4, 2, 2, 8, 3, 3, 3, 1, 2, 4]
print(count_unique(numbers))

#appr2
from collections import Counter

def sort_and_count_unique(numbers):
    # Count the occurrences of each element
    counts = Counter(numbers)
    
    # Use a lambda function to filter out elements that appear exactly once
    unique_elements = list(filter(lambda x: counts[x] == 1, counts))
    
    # Sort the unique elements in ascending order
    sorted_unique_elements = sorted(unique_elements)
    
    # Return a list of tuples with element and count (which is 1)
    return [(elem, 1) for elem in sorted_unique_elements]

# Example usage:
numbers = [4, 2, 2, 8, 3, 3, 3, 1, 2, 4]
result = sort_and_count_unique(numbers)
print(result)

#appr3
from collections import Counter

def sort_and_find_non_repeating(numbers):
    # Count the occurrences of each element
    counts = Counter(numbers)
    
    # Filter out the elements that appear only once
    non_repeating = [num for num, count in counts.items() if count == 1]
    
    # Sort the non-repeating elements in ascending order
    return sorted(non_repeating)

# Example usage:
numbers = [4, 2, 2, 8, 3, 3, 3, 1, 2, 4]
result = sort_and_find_non_repeating(numbers)
print(result)

#you are given a list of integers. Sort the list in ascending order and remove all even numbers.
def sort_and_remove_even(numbers):
    return list(filter(lambda x: x %2 == 0, sorted(numbers)))

numbers = [1, 4, 7, 2, 9, 10]
print(sort_and_remove_even(numbers))

#you are given a list of integers. Sort the list in ascending order and remove all odd numbers.
def sort_and_remove_odd(numbers):
    return list(filter(lambda x: x %2 != 0, sorted(numbers)))

numbers = [1, 4, 7, 2, 9, 10]
print(sort_and_remove_odd(numbers))

#You are given a list of dictionaries where each dictionary has keys name, age, and salary. Sort the list first by age in ascending order, and then by salary in descending order in case of ties in age.
def sort_by_age_n_salary(people):
    return sorted(people, key= lambda person:(person['age'], -person['salary']))

people = [{'name': 'Alice', 'age': 30, 'salary': 50000}, {'name': 'Bob', 'age': 25, 'salary': 60000}, {'name': 'Charlie', 'age': 30, 'salary': 70000}]
print(sort_by_age_n_salary(people))

#You are given a list of numbers. Sort the list based on the absolute values of the numbers. display results with - sign
def sort_absolute_values(num1):
    return sorted(num1, key=lambda x: x if x >= 0 else -x)

    #return sorted(num1, key=lambda x: abs(x))

num1 = [-3, 5, -1, 8, -2]
print(sort_absolute_values(num1))

#appr2 display only absolute (removing - sign)
#You are given a list of numbers. Sort the list based on the absolute values of the numbers.
def sort_absolute_values_app2(numbers):

    sorted_numbers = sorted(numbers, key=lambda x: abs(x))
    return [abs(x) for x in sorted_numbers]

numbers = [-3, 5, -1, 8, -2]
print(sort_absolute_values_app2(numbers))

#You are given a list of integers. Find the kth smallest element in the list.
def find_kth_smallest_elem(digits, k):
   return sorted(digits)[k-1]

digits = [7, 3, 1, 9, 4, 2]
k = 2
print(find_kth_smallest_elem(digits, k))

#You are given a list of integers where every element appears twice except for one element. Find the element that appears only once.
def find_single_element(num01):
    counts = Counter(num01)
    return list(filter(lambda x: counts[x] == 1, counts))
    #return [num for num, count in counts.items() if count == 1]

num01 = [4, 1, 2, 1, 2, 5]
print(find_single_element(num01))

#Given a list of tuples where each tuple contains two integers, sort the list first by the first element in ascending order and then by the second element in descending order if the first elements are the same.
def sort_by_first_and_second(pairs):
    return sorted(pairs, key=lambda x:(x[0], -x[1]))

pairs = [(1, 3), (2, 4), (2, 2), (1, 1)]
print(sort_by_first_and_second(pairs))

#You are given a list of numbers. Remove any duplicates and sort the list in reverse order.
def remove_duplicates_and_sort_reverse(num02):
    return sorted(set(num02), reverse=True)

num02 = [3, 1, 4, 1, 2, 5, 9,10,2,3]
print(remove_duplicates_and_sort_reverse(num02))
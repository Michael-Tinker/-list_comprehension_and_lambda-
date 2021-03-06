''' 1)
Write a Python program to filter a list of integers using Lambda. 
Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(original_list)
even_list = list(filter(lambda num:(num%2)==0,original_list))
odd_list = list(filter(lambda num:(num%2)!=0,original_list))
print(even_list)
print(odd_list)
''' 2)
find which days of the week have exactly 6 characters.
'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
six_chars = list(filter(lambda day:(len(day)==6), weekdays))
print(six_chars)
''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
removed_list = ['orange', 'black']
modified_list = list(filter(lambda word:word not in removed_list, original_list))
print(original_list)
print(removed_list)
print(modified_list)
''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
removed_list = [2, 4, 6, 8]
modified_list = list(filter(lambda num:num not in removed_list, original_list))
print(original_list)
print(removed_list)
print(modified_list)
''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']

Substring to search:
ack
Elements of the said list that contain specific substring:
['black']

Substring to search:
abc
Elements of the said list that contain specific substring:
[]
'''
original_list = ['red', 'black', 'white', 'green', 'orange']
substring = "ack"
substring2 = "abc"

search1 = list(filter(lambda x: substring in x,original_list))
search2 = list(filter(lambda x: substring2 in x,original_list))

print(search1)
print(search2)
''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and 
a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
give_string = "Aa1thisis8chars+"
#Check if lower
chars = list(give_string)

#Check if upper
#Check if number
#Combine with and?
#use lambda to check if upper or lower or digit
print(check)


''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

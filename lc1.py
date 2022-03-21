# numbers 1 thru 9



x = [i for i in range(10)]
print(x)

#adding an expression - square of each number
squares = [i**2 for i in range(10)]
print(squares)

#multiply each element by 3
list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(list1)
print(multiplied)

# word manipulation
listOfWords = ["this","is","a","list","of","words"]
# The output should be a list of the first letter of each word
#['t', 'i', 'a', 'l', 'o', 'w']
firstletter = [word[0] for word in listOfWords]
print(firstletter)


list1 = ["A", "B", "C"]
list2 = [x.lower() for x in list1]
print(list2)
list3 = [x.upper() for x in list2]
print(list3)


# adding in an IF condition

evennum = [x*x for x in range(5) if x%2 ==0]
print(evennum)
oddnum = [x*x for x in range(5) if x%2 != 0]
print(oddnum)

string = "Hello 12345 World"
numstring = [x for x in string if x.isdigit()]
wordstring = [x for x in string if x.isalpha()]
print(numstring)
print(wordstring)


#Old way
numbers = []
for x in string:
    if x.isdigit():
        numbers.append(x)


#using a file
myfile = open("test.txt","r")
result = [i.rstrip("\n") for i in myfile if "line3" in i]
print(result)


#using functions
def double(x):
    return x*2

print(double(10))


mynumbers = [double(x) for x in range(10)]

print(mynumbers)

mynumbers_even = [double(x) for x in range(10) if x%2 ==0]

print(mynumbers_even)


# You can add more arguments

result = [x+y for x in [10,30,50] for y in [20,40,60]]

print(result)
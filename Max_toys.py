# Question : 1 How to find the maximum occurring character in given String?

def max_chars(str):
    dict = {}
    max = 0
    max_char = ""

    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1

    for i in dict:
        if dict[i] > max:
            max += dict[i]
            max_char += i
    print(max)
    print(max_char)

max_chars("ankitakatoch")

# 2. How to remove all duplicates from a given string?

def remove_dup(str):
    dict = {}
    str1 = ""

    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1

    print(dict)

    for i in dict:
        str1 += i
    print(str1)
remove_dup("ankitakatoch")

# 3. How to print the duplicate characters from the given String?

def dup_chars(str):
    dict = {}
    str1 = ""
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1

    for i in dict:
        if dict[i] > 1:
            str1 += i
    print(str1)

dup_chars("harikapatha")

# 4. How to remove characters from the first String which are present in the second String?

def removerchars_twostrings(str1,str2):
    dict1 = {}
    dict2 = {}
    str3 = ""

    for i in range(len(str1)):
        if str1[i] in dict1:
            dict1[str1[i]] += 1
        else:
            dict1[str1[i]] = 1
    for i in range(len(str2)):
        if str2[i] in dict2:
            dict2[str2[i]] += 1
        else:
            dict2[str2[i]] = 1
    print(dict1)
    print(dict2)

    for i in dict1:
        if i not in dict2:
            str3 += i
    print(str3)

removerchars_twostrings("ankitakatoch","anujrapujput")

# 5.How to check if two strings are rotations of each other?


# 6) How to reverse a given String?

str = "Python is best"
str1 = str[::-1]
print(str1)

# 9) How to find the first non-repeating character in a given String?

def nonrepeating_char(str):
    dict = {}

    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1
    print(dict)

    for c in dict:
        if dict[c] == 1:
            return c
    return None

print(nonrepeating_char("ankitakatoch"))

# 8) How to print all permutation of a String?

# def permutations(a):
#     if len(a) == 1:
#         return 1
#     elif len(a) == 2:
#         return 2
#     else:
#         return a * permutations(len(a) - 1)
# print(permutations("123"))

# Find factorial of a number :

# def factorialnum(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return n*factorial(num(n-1)
#
# print(factorial(num(7))

# 10) How to reverse the words in a given String sentence?

# 11) How to find the smallest substring in a given string containing all characters of another string?

def smallest_substring(str1,str2):
    dict1 = {}
    dict2 = {}
    for i in range(len(str1)):
        if str1[i] in dict1:
            dict1[str1[i]] += 1
        else:
            dict1[str1[i]] = 1
    for i in range(len(str2)):
        if str2[i] in dict2:
            dict2[str2[i]] += 1
        else:
            dict2[str2[i]] = 1
    print(dict2)
    print(dict1)

    # for i in dict1:
    #     if dict1 in dict2:
    #         print(dict1[i])

print(smallest_substring("this is string","tist"))

# 12) How to check if two given String is the anagram of each other?

def ifAnagram(str1,str2):
    dict1 = {}
    dict2 = {}
    for i in range(len(str1)):
        if str1[i] in dict1:
            dict1[str1[i]] += 1
        else:
            dict1[str1[i]] = 1
    for i in range(len(str2)):
        if str2[i] in dict2:
            dict2[str2[i]] += 1
        else:
            dict2[str2[i]] = 1
    print(dict2)
    print(dict1)

    if dict1 == dict2:
        return True
    else:
        return False


print(ifAnagram("aaankita","kitaaaan"))

# 13) How do you check if a given String is Palindrome or not?

def palindrome(str):

    if str == str[::-1]:
        return True


print(palindrome("ankitatikna"))

# 17.remove given character from string

def remove_char(str,char):
    str1 = ""
    dict = {}
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]]+=1
        else:
            dict[str[i]] = 1

    print(dict)

    for i in dict:
        if i not in char:
            str1 += i
    print(str1)

print(remove_char("ankitakatoch","k"))

# 18) How do you count a number of words in String?

def number_words(str):
    str1 = str.split(" ")
    print(str1)
    print(len(str1))
number_words("my name is ankita katoch")

def duplicate(str):
    dict = {}
    str1 = ""
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1
    print(dict)

    for j in dict:
        if dict[j] > 1:
            str1 += j
    print(str1)

duplicate("ankita katoch")

# split the array and add first part to the end

def splitarray(arr, k):
    for i in range(0, k):
        x = arr[0]
        print(x)
        for j in range(0, len(arr)-1):
            arr[j] = arr[j + 1]
        arr[len(arr) - 1] = x
    for i in range(0, len(arr)):
        print(arr[i], end=' ')
splitarray([10,12,1,23,4], 2)

# sort an array

# def sort(arr):
#     for i in range(len(arr)):
#         for j in range(1, len(arr)-i):
#             if arr[j-1] < arr[j]:
#                 (arr[j], arr[j-1]) = (arr[j-1], arr[j])
# def quicksort(array):
#     #assign a index as pivot. compare values of array with the pivot and sort
#
#     less = []
#     greater = []
#     equal = []
#
#     if len(array) > 1:
#         pivot = array[0]
#         for i in array:
#             if i > pivot:
#                 less.append(i)
#             elif i == pivot:
#                 equal.append(i)
#             else:
#                 greater.append(i)
#         return (quicksort(less) + equal + quicksort(greater))
#         # sort(less)
#         # sort(greater)
#         # print(less + equal + greater)
# quicksort([10,12,1,5,4,24,34])


# palindrome

def find_palindrome(str):
    if str == str[::-1]:

        print("string is palindrome")
    else:
        print("not palindrome")

find_palindrome("a(n(a")

# #balance paranthesis
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0:
                popped = stack.pop()
                if popped == open_list[pos]:
                    print("inside loop")
                else:
                    return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
# Driver code
string = "{[]{(})}"
print(string, "-", check(string))


def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]
        # print(lst[:i])

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# # Driver program to test above function
# data = list('123')
# for p in permutation(data):
#     print(p)
#
#
#
# def sortarray():
#     if len(list) == 1:
#         return list
#     for i in range(len(list)):
#         for j in range(1, len(list)):
#             if list[j] > list[j-1]:
#                 (list[j], list[j-1]) = (list[j-1], list[j])
#     return list
# print(sortarray())


# list = []
# dict = {}
# textfile = open('/Users/ankitakatoch/Documents/data.txt',
# print(textfile.read())
#
# textfile1 = textfile.split(",")
#
# for i in textfile:
#     list.append(i)
# print(list)
#
#
# for i in range(0,len(list), 2):
#     dict[list[i]] = list[i+1]
# print(dict)
#
# dict = {"ankita" : "03-09-1991", "anuj" : "09-28-2987" }
# Data = input("please enter the month")
# date = "03-09-1991"
# date1 = "09-28-2987"
# new_date = date.split("-")[0]
# new_date1 = date1.split("-")[0]
# dict["ankita"] = new_date
# dict["anuj"] = new_date1
# if Data == dict.keys:
#     print(dict.values)
#
#
# list = [2,3,7,5,1,90,"ankita",5]
# res = dict(list[idx : idx + 2] for idx in range(0, len(list), 2))
# print(res)
# dict = {}
#
#
# daily_balances = [107.92, 108.67, 109.86, 110.15]
# print(daily_balances[2:]+daily_balances[:2])
#
#
# iterator = [i for i in range(1, 4)]
# matrix = [[x * y for y in iterator] for x in iterator]
# print(matrix)






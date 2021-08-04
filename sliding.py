def duplicate(str):
    dict = {}
    str1 = ""

    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1
    print(dict)

    for i in dict:
        if dict[i] > 1:
            str1 += i
    print(str1)

duplicate("ankita katochAAA")



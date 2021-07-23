#Here I am writing a Python program to get the smallest number from a list. Moreover, if there is a string in list than how to frame the program to ignore the string and focus only on int data type.  

def minimum(lst):
    min=lst[0]
    for a in lst:
        if type(a)==str:
            pass
        elif a<min:
            min=a
    return min
print(minimum([1,3,44,"abhi",555667,72,100]))

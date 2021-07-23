def minimum(lst):
    min=lst[0]
    for a in lst:
        if type(a)==str:
            pass
        elif a<min:
            min=a
    return min
print(minimum([1,3,44,"abhi",555667,72,100]))
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

#Write a Python program to remove duplicates from a list
lst=['abc', 'xyz', 'aba', '1221',22,44,55,22,'abc']

for value in lst:
	if lst.count(value)>1:
		lst.remove(value)
print(lst)

#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
lst=['abc', 'xyz', 'aba', '1221']

def same(lst):
	new_lst=[]
	for n in lst:
		if len(n)>2 and n[0]==n[-1]:
			new_lst.append(n)	
	print(new_lst)
same(lst)


#Write a python program to count character occurrences: 
l=[1,2,3,1,2,2,5,6]

def count(lst):
    repeat={}
    for value in lst:
        a=l.count(value)
        b=value
        repeat.update({b:a})
    return repeat
print(count(l))




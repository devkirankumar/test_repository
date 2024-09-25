'write  a function which will take two arguments one is list and another one is x value and return a news list of elements which are smaller than x value.'

'''
def smaller_ele(l,x):
    new_l=[]
    for v in l:
        if v<x:
            new_l.append(v)
    return new_l

l=[10,12,17,9,3]
x=10
print(smaller_ele(l,x))

'''
'write the same using list comprehension. wrote extra comment. push to the github'

'''
def smaller_ele(l,k):
    return [x for x in l if x < k]

l=[10,12,20,30,40]
k=20
print(smaller_ele(l,k))'''


'write a function which using range take value as 10 and returns all even numbers between 10 in a list '

def even_odd():
    even=[]
    odd=[]
    for x in range(11):
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)

print(even_odd)







find one proffesional data scientist and tell him/ her briefly about your goal. what you want to do by learning data science . convince them to teach you data science
if tey are not convinced to teach you then ask them atleast roadmap to learn data science
convince them that you can do anything to learn data science


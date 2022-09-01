############# Lecture 2 #############
########### Qiaozheng Lu ############

'''

Vectors (arrays) contains homogenous elements, list can contain heterogenous elements

Matrix - Homogenous, Data Frame - Heterogenous

'''

## Tuple = immutable list

t1 = 2, 4
t2 = (2, 4)

print(str(type(t2)) + ' ' + str(type(t1)))

## Dictionary

'''
Each element is a pair of two: Index & Content

Call the content by referencing the index
'''

dic = {1: 2, 'a': 'Hello'}

## Enumerating a list

l = [1, 2, 4, 5]

for i, x in enumerate(l):
    print(str(i) + ': ' + str(x))

## list comprehension

fillings = ['apple', 'cherry']
pies = [x + ' pie' for x in fillings]  # Capable of incorporating iterations inside the definition of a new list

## swaping the cases of the letters

swapped = [x.swapcase() for x in fillings]
swapped_dic = {x: x.swapcase() for x in fillings}

print(swapped)
print(swapped_dic)


## Recursive functions

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))

from PythonBasics import kompalDSA, fibo
import math
from fibo import fib
def calculate_square() :
    number_of_times,end = input("Range of squares ?").split()
    squares = list(map(lambda x:x**2,range(int(number_of_times),int(end)+1)))
    print(squares)
    # another way
    square_eff = [x**2 for x in range(int(number_of_times),int(end)+1)]
    print(square_eff)
    return square_eff

def combine_elements(list1,list2):
    return [(x, x * 2) for x in list1 if x >= 3 for y in list2 if y > 5]
    #return list(set(list1 + list2))

def tuple_set_example(input1,input2,operation):
    print(input1,input2)
    list1 = set(input1)
    list2 = set(input2)
    tuple1 = tuple(list1)+tuple(list2)

    print(list1,list2,tuple1)

    if operation == "union":
        return list1 & list2
    elif operation == "intersection":
        return list1 | list2
    elif operation == "difference":
        return list1 - list2
    elif operation == "symmetric_difference":
        return list1 ^ list2

    test = zip(list1)
    print(test)
    return {x:y for x,y in zip(sorted(list1),sorted(list2))}


#name,age = input("What is your name? ").split()
#result = kompalDSA.get_message(name,age)
#print(result)
#calculate_square()

#print(combine_elements([1,2,3],[4,5,6]))

inp1,inp2,op = input('Give me 2 words').split()
print(tuple_set_example(inp1,inp2,op))
print(fibo.fib(10))
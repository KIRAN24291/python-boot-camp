'''
Data types in Python define the type of values stored in a variable.
They are:
1)Numeric Data Type (int,float,complex)
2)Boolean Data Type (True,False)
3)Sequence Data Type(string,list,tuple)
4)set
5)Dictionary
'''

'''
IMP:There is an function for finding these data types known as type().
'''
name = "kiran"
print(type(name))           #str

'''
1)Numeric Data Type
int --> whole numbers (0,50,-89)
float --> decimal numbers (58.2,871,-246.0)
complex --> real and imaginary (a+3b,b+aj)
'''

num = 10
height = 154.5
math = 4+3j

'''
2)Boolean data type represents one of two valaues:True or False (Logical Operations).
'''

is_sunny = True
is_rainy = False

'''
3)Sequence data types in Python are ordered collections of items that allow you to store multiple values in an organized manner, accessible via indexing (starting from 0) and slicing.
String: Immutable sequences of characters defined by quotes, used for text data storage.  
List: Mutable, ordered collections defined by square brackets [], capable of holding heterogeneous data types. 
Tuple: Immutable, ordered collections defined by parentheses (), used when data integrity and read-only access are required. 
'''
name = 'kiran' #string
fruits = ['apple','banana']
my_tuple = ('data1','data2')

print(type(name),type(fruits),type(my_tuple))           #<class 'str'> <class 'list'> <class 'tuple'>

'''
4)Set Data Type
Sets are unordered and mutable collections used to store unique elements.
Since sets are unordered, elements cannot be accessed using indexing. Elements are usually accessed by iterating through the set using a loop.
Sets are defined with curly braces.
'''

s1 = {"a", "a", "b", "c", "b"}
print(s1)           #{'a', 'c', 'b'}

'''
5)Dictionary Data Type
Dictionaries are used to store data in key:value pairs.
Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method.
key:value,key1:value1
'''

person ={
    'name' : "kiran",
    'age' : 100,
    'number' : 0000000000

}
print(person)
print(person.get('name'))
print(type(person))         #dict
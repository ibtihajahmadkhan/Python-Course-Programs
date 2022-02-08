## DataTypes

x = "Hello World" 			    # str 	
x = 20 					    # int 	
x = 20.5 				    # float 	
x = 1j 					    # complex 	
x = ["apple", "banana", "cherry"] 	    # list 	
x = ("apple", "banana", "cherry") 	    # tuple 	
x = range(6) 				    # range 	
x = {"name" : "John", "age" : 36} 	    # dict 	
x = {"apple", "banana", "cherry"} 	    # set 	
x = frozenset({"apple", "banana", "cherry"})# frozenset 	
x = True 				    # bool
					

# Data Type Conversion
x = str("Hello World")                      # str 	
x = int(20)                                 # int 	
x = float(20.5)                             # float 	
x = complex(1j)                             # complex 	
x = list(("apple", "banana", "cherry"))     # list 	
x = tuple(("apple", "banana", "cherry"))    # tuple 	
x = range(6)                                # range 	
x = dict(name="John", age=36)               # dict 	
x = set(("apple", "banana", "cherry")) 	    # set 	
x = frozenset(("apple", "banana", "cherry"))# frozenset 	
x = bool(5)                                 # bool

# Strings in Python
str = 'Hello World!'
print (str)             # Prints complete string
print (str[0] )         # Prints first character of the string
print (str[2:5] )       # Prints characters starting from 3rd to 5th
print (str[2:] )        # Prints string starting from 3rd character
print (str * 2 )        # Prints string two times
print (str + 'TEST' )   # Prints concatenated string


# List in Python
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print ( list )         	     # Prints complete list
print ( list[0] )     	     # Prints first element of the list
print ( list[1:3] )    	     # Prints elements starting from 2nd till 3rd 
print ( list[2:] )     	     # Prints elements starting from 3rd element
print ( tinylist * 2 )  	     # Prints list two times
print ( list + tinylist )  	     # Prints concatenated lists


# Bool in Python
print(10 > 9)
print(10 == 9)
print(10 < 9) 
## Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))


# Dict in Python
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964 }
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(thisdict.keys())
print( thisdict.values())
thisdict["year"] = 2020
print(thisdict)
if "model" in thisdict:
	print("Yes, 'model' is one of the keys in the this dict dictionary") 
## __Duplicates__
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict) 




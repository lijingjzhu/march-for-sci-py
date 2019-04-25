### Data Structures
Python (and most programming languages) has a variety of different data structures, or ways to hold information. Holding information is important because we are telling the computer that we want to save these values for later use. I've described the most useful ones below; if you continue in Python, you may also run into sets, tuples, and arrays. 

#### Integers  
An integer is a whole number, without any decimals.   
Examples include `2`, `4`, `8`.   
In Python, you can add, subtract, and divide integers with normal math symbols `+`, `-`, `/`, `*` (multiply).  

#### Strings 
A string is a sequence of any kind of characters and is often a word.
In Python, you can make a string by enclosing characters in single quotes `''` or double quotes `""`.  
Examples include `'Drew'`, `"Julie"`, `'Sam 123'`.  

#### Booleans    
A Boolean holds a true or false value. There are only two options. In Python, it's written `True` and `False` (make sure the first letter is capitalized and the rest are not). 

#### Floats  
A float is a number with decimals. Examples include `4.0`, `3.14159`, `0.01`. You can perform math operations on floats, but you can run into problems when mixing them with integers, so just be aware. 

#### Lists  
A list is an ordered collection of any data structure. In Python, lists can contain a mix of data types. 

You create a list with brackets and commas, like this:  

```
mylist = ['This', 'is', 'my', 'list', 23] 
```

You can call things back out of the list by using their position (the number they are in the list minus 1).   
I'm using > to represent writing code in the interpreter: 
```
> mylist = ['This', 'is', 'my', 'list', '23']
> mylist[2]
  'my'
```

#### Dictionaries  
A dictionary is an unordered collection of key-value pairs (I know this sounds scary, it's actually pretty simple).  

It's easiest to explain with an example. 

In Python, you make a dictionary with curly braces, colons, and commmas, like this:  
```
mydictionary = {'Sam':8, 'Drew':7.5, 'Julie':9}
```

The thing before the colon is the key, and the thing after the colon is the value. Dictionaries can contain any mix of data types.  

Dictionaries become useful when you get the value back out of them, using indexing:
```
> mydictionary['Sam']  
  8
```

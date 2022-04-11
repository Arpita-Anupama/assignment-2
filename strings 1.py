#string
txt = "hello, and welcome to my world."

#capitalize
x = txt.capitalize()
print (x)

#casefold
x = txt.casefold()
print(x)

#center
txt = "banana"
x = txt.center(20, "O")
print(x)

#count
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

#encode
txt = "My name is Asmita"
x = txt.encode()
print(x)

#endswith
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

#expandtabs
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

#find
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#format
txt = "For only {price:.2f} rupees!"
print(txt.format(price = 49))

#index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#isalnum
txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha
txt = "CompanyX"
x = txt.isalpha()
print(x)

#isascii
txt = "Company123"
x = txt.isascii()
print(x)

#isdecimal
txt = "\u0033" 
x = txt.isdecimal()
print(x)

#isdigit
txt = "50800"
x = txt.isdigit()
print(x)

#isidentifier
txt = "Demo"
x = txt.isidentifier()
print(x)

#islower
txt = "hello world!"
x = txt.islower()
print(x)

#isnumeric
txt = "565543"
x = txt.isnumeric()
print(x)

#isprintable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

#isspace
txt = "   "
x = txt.isspace()
print(x)

#istitle
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

#isupper
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

#join
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#1just
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

#lower
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#1strip
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#maketrans
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

#partition
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

#replace
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#rfind
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

#rindex
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

#rjust
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

#rpartition
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

#rsplit
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

#strip
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#split
txt = "welcome to the jungle"
x = txt.split()
print(x)

#splitlines
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

#startswitch
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

#swapcase
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#title
txt = "Welcome to my world"
x = txt.title()
print(x)

#translate
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#upper
txt = "Hello my friends"
x = txt.upper()
print(x)

#zfill
txt = "50"
x = txt.zfill(10)
print(x)


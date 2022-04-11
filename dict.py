#dictionary
t-shirt = {"brand": "polo","model": "v neck","colour": "green"}

#removing elements 
x=t-shirt.clear()
print(x)

#copy
x = t-shirt.copy()
print(x)

#fromkeys
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#get
x = t-shirt.get("model")
print(x)

#items
x = t-shirt.items()
t-shirt["colour"] ="red"
print(x)

#keys
x = t-shirt.keys()
t-shirt["waranty"] = 2
print(x)

#pop
x = t-shirt.pop("model")
print(x)

#setdefault
x = t-shirt.setdefault("color", "white")
print(x)

#update
x=t-shirt.update({"waranty": 2})
print(x)

#values
x = t-shirt.values()
print(x)

# craeting a list 

Fruit = ["Apple", "Banana", "Watermellon"]
print (Fruit)

print (Fruit[1])

# adding new a item in list

Fruit.append ("Mango")
print(Fruit)

# removing item from list by string

Fruit.remove("Apple")
print(Fruit)

# removing item by int

del Fruit [1]
print(Fruit)
# adding multiple items in list (Opertor 1)
Fruit.extend(["Apple", "Watermelon"])
print(Fruit)

#(Operator 2)

Vege = ["Tomato", "Lemon", "Capsicumm"]
print(Vege)

Fruit = Fruit + Vege # andding 2 lists in one
print(Fruit)

#Task 1

movies = ["M1", "F2", "R3"]
movies.append("Y4")
# adding more
movies.extend(["U6","H7","I8"])
print(movies)

movies.remove("M1")
movies.remove("F2")
movies.remove("R3")

print(movies)

pic = ["M1", "F2", "R3"]

print(movies)
print(pic)

# list functions

#1
number = [12,34,32,45,75,23,32,45]
number.sort()
print(number)

name =["Zain", "Ahmad", "UG"] 
name.sort()
print (name)
#2
name.reverse()
print(name)

number.reverse()
print(number)
#3 
print(len(name))
print (len(number))

#4
print(number.count(32))

#5
print(number.index(32))
#6
number.insert(1, 89)
print(number)


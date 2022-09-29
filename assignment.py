# # END OF WEEK 7 QUIZ

# 1. Your task is to create slightly different animals, which should have the same properties and methods, but should implement the talk() method in different ways. 
# For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". They should all share the following (private) properties: name (string), 
# age (number), food (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. Finally, all the animals must have the talk function, but that function must, as I said, be implemented in each animal, as the animals have different sounds.

# When you have made the classes, create instances of the classes and put in a list - loop through the list - and let all the animals talk! :)

class Animal:
    def __init__(self,name,age,food):
        self.__name = str(name)
        self.__age = int(age)
        self.__age = food 
    
    def Talk(self):
        print("am talking")


    def get_name(self,name):
        return self.get_name

    def set_name(self,name):
        self.set_name= name
        
    def get_age(self,age):
        return self.get_age
    def set_age(self,age):
        self.set_age= age

    def get_food(self,food):
        return self.append(food)
    def add_food(self,food):
        self.set_name= food
    def remove_food(self,__food):
        return self.remove_food(__food)
    


class Cat(Animal):
    def __init__(self):
        super().__init__(self)
        print("am a cat")
    def talk(self):
        print("moew")

class Dog(Animal):
    def __init__(self):
        super().__init__(self)
        print("am A dog")
    def talk(self):
        print("woff")

class Fish(Animal):
    def __init__(self):
        super().__init__(self)
        print("am A Fish")
    def talk(self):
        print("blub")

class Cow(Animal):
    def __init__(self):
        super().__init__(self)
        print("am cow")
    def talk(self):
        print("muuu")

catt = Cat('swee', 20, "pork")
do = Dog('Germay', 20, "pork")
fi = Fish('tarapia', 20, "pork")
co = Cow('exotic', 20, "pork")
catt.talk()
catt.get_name()
catt.get_age()
catt.add_food()

do.get_name()
do.get_age()
do.add_food()

fi.get_name()
fi.get_age()
fi.add_food()

co.get_name()
co.get_age()
co.add_food()









# 2. The snail climbs up 7 feet each day and slips back 2 feet each night. 
# How many days will it take the snail to get out of a well with the given depth?. Using python, write a function to solve this problem.
# Sample Input: 31
# Sample Output: 6

day = 0
total = 0
depth = 0

while(total<depth){
    day += 1;
    total += 7;  
    if(total >= depth){
        break;  
    }
    total -= 2; 
}    



# 3. Write a function that takes a list of numbers and returns the largest number in the list.

def myMax(list1):
 
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max
 
list1 = [104, 60, 4, 45, 19]
print("the largest number in the list:", myMax(list1))

# 4. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# `Hello world!`
# Then, the output should be:
# `UPPER CASE 1`
# `LOWER CASE 9`

def SentenceAccept(sentence):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in sentence:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print (sentence)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

SentenceAccept('Hello world!')

# 5. Using Object Oriented Programming, write a program that implements
# a dice game. The game should have two players, and each player
# should have a name and a score. The game should have a method
# called `play` that takes two players as arguments and simulates
# the game. The game should be played as follows:
#     - Each player rolls a die.
#     - The player with the highest roll wins the round.
#     - The winner gets one point added to their score.
#     - The game ends when one player has 5 points.
#     - The player with the most points at the end of the game wins.
#     - The program should print out the winner's name and score.
#     - If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a third time, they get an extra roll, but their turn ends.

# 6. Write a Python program that lists out all the default as well as custom properties of the class.

# 7. Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal methods.

class Stack:
    
    def __init__(self):
        
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        self.__stack.pop()

    def traverse(self):
        for item in self.__stack[::-1]:
            print("|", item, "|")

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.pop()
stack.pop()

stack.traverse()

# 8. Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.

# 9. Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).
def queue():
    def enqueue(self, data):
        self.queue.insert(0, data)
        return True

    
    def dequeue(self):
        return self.queue.pop()

   
    def size(self):
        return len(self.queue)

    def display(self):
            return self.queue

q = queue()

q.enqueue('city')
q.enqueue('does')
q.enqueue('Assignment')

print(q.display())

print(q.dequeue())

print(q.display())

print(q.size())

# 10. Using a while loop, implement merge sort algorithm.

def merge_sort(list):
    
    list_length = len(list)

    if list_length == 1:
        return list

    mid_point = list_length // 2

    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    return merge(left_partition, right_partition)


def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def run_merge_sort():
    unsorted_list = [4, 1, 5, 6, 1, 1, 6, 4, 10, 79]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)


run_merge_sort()


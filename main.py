class Toe:
    def __init__(self):
        pass

class Cat:
    def __init__(self):
        self.toes = []
        # create an instance from a class
        toe1 = Toe()
        toe2 = Toe()
        toe3 = Toe()
        toe4 = Toe()
        toe5 = Toe()
        self.toes.append(toe1)
        self.toes.append(toe2)
        self.toes.append(toe3)
        self.toes.append(toe4)
        self.toes.append(toe5)
    
    def say_hi(self):
        print("meow")

class App:
    def __init__(self):
        pass

    def run(self):
        cat1 = Cat()
        cat1.say_hi()
        # print(cat1.toes)

        # properties vs methods
        # this


# app = App()
# app.run()



# lst = [1, 2, 3]

# for num in lst:
#     print(num ** 2)

# name = "John"
# print(name)

# 1. Object oriented
# 2. Procedural
# 3. Functional


def process_string(my_function, string):
    print(my_function(string))

def uppercase(s):
    return s.upper()

def lowercase(s):
    return s.lower()


process_string(uppercase, "some string")
process_string(lowercase, "SOME STRING")

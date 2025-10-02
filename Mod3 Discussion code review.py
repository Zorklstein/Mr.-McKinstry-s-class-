#Ezekiel Mesman

class User():
    #creates a user and displays a message and user summary
    def __init__(self, firstName, lastName, age, userID):
        self.firstName = firstName.title()
        self.lastName = lastName.title()
        self.age = age
        self.userID = userID

    def describeUser(self):
        print(f"Name: {self.firstName} {self.lastName}\nAge: {self.age}\nID Number: {self.userID}")

    def greeting(self):
        print(f"Welcome to the program {self.firstName} {self.lastName}.\n")

#User 1
p1 = User('matt', 'miller', 42, 1110)
p1.describeUser()
p1.greeting()

#User 2
p2 = User('jacob', 'smith', 57, 1111)
p2.describeUser()
p2.greeting()

#User 3
p3 = User('chris', 'williams', 82, 1112)
p3.describeUser()
p3.greeting()

#User 4
p4 = User('jackson', 'davenport', 24, 1113)
p4.describeUser()
p4.greeting()

#User 5
p5 = User('corbin', 'archer', 33, 1114)
p5.describeUser()
p5.greeting()

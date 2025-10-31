import sys

class Student:
    def __init__(self, name, grade, ID):
        self.name = name  
        self.grade = grade  
        self.ID = ID      

    def getName(self):
        return self.name
    def getgrade(self):
        return self.grade
    def getID(self):
        return self.ID
    def setName(self, name):
        self.name = name
    def setgrade(self, grade):
        self.grade = grade
    def setID(self, ID):
        self.ID = ID
   
    def showEverything(self):
        print(f"Name: {self.name}\nGrade: {self.grade}\nID: {self.ID}\n")

class managingStudents:
    def __init__(self):
        self.students =[]

    def addStudent(self):
        print("Adding Student\n")
        newName = input("What is your name:")
        while True:
            try:
                grade = float(input("What is the student's grade:"))
                break
            except ValueError:
                print("Please type in a valid number:")
           
        while True:
            try:
                IDs = int(input("What is the student's ID:"))
                break
            except ValueError:
                print("Please type in a whole number:")

        newStudent = Student(newName, grade, IDs)
        self.students.append(newStudent)

    def displayStudents(self):
        if not self.students:
            print("No students in the system")
        else:
            print(self.students)
            for i in self.students:
                i.showEverything()

    def findStudents(self):
        try:
            studentID = int(input("Please enter student ID:"))
        except ValueError:
            print("Please type in a whole number:")
            return

        for i in self.students:
            if i.getID() == studentID:
                print("User Found\n")
                i.showEverything()
                return
        print(" Student Not Found")

    def removeStudent(self):
        try:
            studentID = int(input("Please enter student ID:"))
        except ValueError:
            print("Please type in a whole number:")
            return

        for i in self.students:
            if i.getID() == studentID:
                print("User Removed\n")
                self.students.remove(i)
                return
        print(" Student Not Found")

    def updateGrade(self):  
        try:
            studentID = int(input("Please enter student ID:"))
        except ValueError:
            print("Please type in a whole number:")
            return
       
        for i in self.students:
            if i.getID() == studentID:
                print("User Found\n")

                while True:
                    try:
                        newGrade = float(input("What is the new student grade:"))
                        break
                    except ValueError:
                        print("Please type in a valid number:")

                i.setgrade(newGrade)
                print("Grade Updated")

                return
        print(" Student Not Found")
           
if __name__ == "__main__":
    manager = managingStudents()
    while True:
        print("Student Management System\n")
        print("1. Add Student\n")
        print("2. Display All Students\n")
        print("3. Find Student by ID\n")
        print("4. Remove Student by ID\n")
        print("5. Update Student Grade\n")
        print("6. Exit\n")
       
        option = input("Enter your operation:")

        if option == '1':
            manager.addStudent()
        elif option == '2':
            manager.displayStudents()
        elif option == '3':
            manager.findStudents()
        elif option == '4':
            manager.removeStudent()
        elif option == '5':
            manager.updateGrade()
        elif option == '6':
            print("Leaving program")
            sys.exit(0)
#student_mangrader = managingStudents()
#student_mangrader.displayStudents()

#1. Add Student
#2. Display All Students
#3. Find Student by ID
#4. Remove Student by ID
#5. Update Student Grade
#6. Exit

#Enter your operation:1

#Adding Student

#What is your name:Ayush Kumar
#What is the student's grade:110
#What is the student's ID:201229032

#Student Management System

#1. Add Student
#2. Display All Students
#3. Find Student by ID
#4. Remove Student by ID
#5. Update Student Grade
#6. Exit

#Enter your operation:2
#Name: Ayush Kumar
#Grade: 110.0
#ID: 201229032

#Student Management System

#1. Add Student
#2. Display All Students
#3. Find Student by ID
#4. Remove Student by ID
#5. Update Student Grade
#6. Exit

#Enter your operation:3
#Please enter student ID:201229032
#User Found

#Name: Ayush Kumar
#Grade: 110.0
#ID: 201229032

#Student Management System

#1. Add Student
#2. Display All Students
#3. Find Student by ID
#4. Remove Student by ID
#5. Update Student Grade
#6. Exit

#Enter your operation:4
#Please enter student ID:201229032
#User Removed

#Student Management System

#1. Add Student
#2. Display All Students
#3. Find Student by ID
#4. Remove Student by ID
#5. Update Student Grade
#6. Exit

#Enter your operation:3
#Please enter student ID:201229032
# Student Not Found
#Student Management System

#1. Add Student
#2. Display All Students
#3. Find Student by ID
#4. Remove Student by ID
#5. Update Student Grade
#6. Exit

#Enter your operation:1
#Adding Student

#What is your name:Ayush Kumar
#What is the student's grade:35
#What is the student's ID:201229032
#Student Management System

#1. Add Student
#2. Display All Students
#3. Find Student by ID
#4. Remove Student by ID
#5. Update Student Grade
#6. Exit

#Enter your operation:5
#Please enter student ID:201229032
#User Found

#What is the new student grade:100
#Grade Updated
#Student Management System

#1. Add Student
#2. Display All Students
#3. Find Student by ID
#4. Remove Student by ID
#5. Update Student Grade
#6. Exit

#Enter your operation:6
#Leaving program
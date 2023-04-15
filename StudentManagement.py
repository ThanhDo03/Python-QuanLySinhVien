import csv
from Student import Student

class StudentManagement:
    # listStudent = open("Student.csv", mode="r" , encoding="utf-8-sig")
    listStudent = []

    # The Function create ID for Student
    def generateID(self):
        maxID = 1
        if(self.NumberOfStudent() > 0):
            maxID = self.listStudent[0]._id
            for student in self.listStudent:
                if (maxID < student._id):
                    maxID = student._id
            maxID = maxID + 1
        return maxID

    # The Function Return The Number Of Students
    def NumberOfStudent(self):
        return len(self.listStudent)

    # The Function Enter Student
    def EnterStudent(self):
        # New Student
        StudentID = self.generateID()
        Name = input("Student's Name: ")
        Sex = input("Student's Gender: ")
        Age = int(input("Student's Age: "))
        Role = input("Student's Role: ")
        GPA = int(input("Student's GPA: "))
        NewStudent = Student(StudentID, Name, Sex, Age, Role, GPA)
        self.Ranked(NewStudent)
        self.listStudent.append(NewStudent)

    # The Function Update Information Student
    def UpdateStudent(self, ID):
        # Search Student In List
        student:Student = self.findByID(ID)
        # If the student exists, update the student information
        if (student != None):
            # Enter Information Student
            name = input("Enter student name: ")
            sex = input("Enter student gender: ")
            age = int(input("Enter student age: "))
            role = input("Enter student role: ")
            GPA = int(input("Enter the student's GPA: "))
            # Update Information Student
            student._name = name
            student._sex = sex
            student._age = age
            student._role = role
            student._GPA = GPA
            self.Ranked(student)
        else:
            print("Student with ID = {} does not exist.".format(ID))

    # The Function Delete Student
    def Destroy(self, ID):
        isDelete = False
        student = self.findByID(ID)
        if (student != None):
            self.listStudent.remove(student)
            isDelete = True
        return isDelete

    # The Function Search Student
    def findByName(self, keyword):
        listS = []
        if(self.NumberOfStudent() > 0):
            for student in self.listStudent:
                if(keyword.upper() in student._name.upper()):
                    listS.append(student)
        return listS

    # The Function Ranked
    def Ranked(self, student:Student):
        if (student._GPA >= 3.6 ):
            student._Ranked = "Excellent"
        elif (student._GPA >= 3.2 ):
            student._Ranked = "Good"
        elif (student._GPA >= 2.5 ):
            student._Ranked = "Moderately Good"
        elif (student._GPA >= 2 ):
            student._Ranked = "Medium"
        else:
            student._Ranked = "Weak"

    # The Function to sort the list of students by ID ascending
    def sortByID(self):
        self.listStudent.sort(key=lambda x: x._id, reverse=False)

    # The Function GPA ----->
    def sortByGPA(self):
        self.listStudent.sort(key=lambda x: x._GPA, reverse=False)

    # Function to sort the list of students by name ascending
    def sortByName(self):
        self.listStudent.sort(key=lambda x: x._name, reverse=False)

    # Display Student
    def showStudent(self, listStudent):
        # Show column headers
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Role", "GPA", "Ranked"))
        # Display List Student
        if (listStudent.__len__() > 0):
            for sv in listStudent:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._role, sv._GPA, sv._Ranked))
        print("\n")


    # The Function Display List Student
    def getListStudent(self):
        return self.listStudent

    # The Function FIND BY ID
    def findByID(self, ID):
        searchResult = None
        if (self.NumberOfStudent() > 0):
            for student in self.listStudent:
                if (student._id == ID):
                    searchResult = student
        return searchResult

    # The Function Save student information to Excel
    def SaveCSV(self):
        with open("Student.csv", "w", newline="") as file_new:
            writer = csv.writer(file_new)
            writer.writerow(["ID", "Name", "Gender", "Age", "Role", "GPA", "Ranked"])
            for student in self.listStudent:
                writer.writerow([student._id, student._name, student._sex, student._age, student._role, student._GPA, student._Ranked])









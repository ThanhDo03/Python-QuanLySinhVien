from StudentManagement import StudentManagement

# Initialize a StudentManagement object to manage students
SDMG = StudentManagement()

while(1==1):
    print("\nSTUDENT MANAGEMENT PROGRAM - PYTHON")
    print("*************************MENU**************************")
    print("**  1. Upload A Student.                             **")
    print("**  2. Update student information by ID.             **")
    print("**  3. Delete student information by ID.             **")
    print("**  4. Search Student' Name.                         **")
    print("**  5. Sort students by Grade Point Average (GPA).   **")
    print("**  6. Sort students by name.                        **")
    print("**  7. Sort students by ID.                          **")
    print("**  8. Display List Of Students.                     **")
    print("**  9. Save student information to Excel.            **")
    print("**  0. Exit                                          **")
    print("*******************************************************")

    key = int(input("Enter options: "))
    if (key == 1):
        print("\n1. Upload A Student.")
        SDMG.EnterStudent()
        print("\nUpload Student Successful!")
    elif (key == 2):
        if (SDMG.NumberOfStudent() > 0):
            print("\n2. Update Information Student. ")
            print("\nEnter ID: ")
            ID = int(input())
            SDMG.UpdateStudent(ID)
        else:
            print("\nStudent list is empty!")
    elif (key == 3):
        if (SDMG.NumberOfStudent() > 0):
            print("\n3. Delete Information Student.")
            print("\nEnter ID: ")
            ID = int(input())
            if (SDMG.Destroy(ID)):
                print("\nStudent with ID = ", ID, " been deleted.")
            else:
                print("\nStudent with ID = ", ID, " doesn't exist.")
        else:
            print("\nStudent list is empty!")
    elif (key == 4):
        if (SDMG.NumberOfStudent() > 0):
            print("\n4. Search Student' Name.")
            print("\nEnter a name to search: ")
            name = input()
            searchResult = SDMG.findByName(name)
            SDMG.showStudent(searchResult)
        else:
            print("\nStudent list is empty!")
    elif (key == 5):
        if (SDMG.NumberOfStudent() > 0):
            print("\n5. Sort students by Grade Point Average (GPA).")
            SDMG.sortByGPA()
            SDMG.showStudent(SDMG.getListStudent())
        else:
            print("\nStudent list is empty!")
    elif (key == 6):
        if (SDMG.NumberOfStudent() > 0):
            print("\n6. Sort students by name.")
            SDMG.sortByName()
            SDMG.showStudent(SDMG.getListStudent())
        else:
            print("\nStudent list is empty!")
    elif (key == 7):
        if (SDMG.NumberOfStudent() > 0):
            print("\n7. Sort students by ID.")
            SDMG.sortByID()
            SDMG.showStudent(SDMG.getListStudent())
        else:
            print("\nStudent list is empty!")
    elif (key == 8):
        if (SDMG.NumberOfStudent() > 0):
            print("\n8. Display List Of Students.")
            SDMG.showStudent(SDMG.getListStudent())
        else:
            print("\nStudent list is empty!")
    elif (key == 9):
        if(SDMG.NumberOfStudent() > 0):
            print("\n9. Save student information to Excel.")
            SDMG.SaveCSV()
            print("\nSave student information to Excel Successfully.")
        else:
            print("\nStudent list is empty!")
    elif (key == 0):
        print("\nYou have chosen to exit the program!")
        break
    else:
        print("\nThis function is not available!")
        print("\nPlease select another function in the menu.")

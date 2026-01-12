students = []

while True:
    print('Student Management System')
    print('1.Add Student')
    print('2.Remove the Student')
    print('3.View Students')
    print('4.Search Students')
    print('5.EXit')

    choice = int(input('Enter the Operation(1-5):'))

    if choice == 1:
        student = input("Enter the Student name:")
        students.append(student)
        print('Added Successfully')

    elif choice == 2:
        student = input('Enter the student name to remove:')
        if student in students:
            students.remove(student)
        else:
            print('name not found')

    elif choice == 3:
        if students == 0:
            print('No Student found')
        else:
            for s in students:
                print(s)


    elif choice == 4:
        if student == 0:
            print('No Students found')
        else:
            student = input('Enter the name you want to search:')
            print('Student index:',students.index(student))

    elif choice == 5:
        break
    else:
        print('Invalid please try again!')



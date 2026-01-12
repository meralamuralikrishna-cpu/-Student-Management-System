
# 📚 Student Management System

A simple **Python-based Student Management System** that allows users to add, remove, view, and search student records interactively using a command-line interface.

---

## 🚀 Features
- ➕ **Add Student** – Add a new student to the list.  
- ➖ **Remove Student** – Remove an existing student by name.  
- 👀 **View Students** – Display all students currently in the system.  
- 🔍 **Search Student** – Find a student by name and display their index.  
- ❌ **Exit** – Quit the program safely.  

---

## 🛠️ How It Works
The program runs in a continuous loop until the user chooses to exit.  
It provides a menu-driven interface where the user selects an operation by entering a number (1–5).

---

## 📑 Code Example
```python
students = []

while True:
    print('Student Management System')
    print('1.Add Student')
    print('2.Remove the Student')
    print('3.View Students')
    print('4.Search Students')
    print('5.Exit')

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
            print('Name not found')

    elif choice == 3:
        if len(students) == 0:
            print('No Student found')
        else:
            for s in students:
                print(s)

    elif choice == 4:
        if len(students) == 0:
            print('No Students found')
        else:
            student = input('Enter the name you want to search:')
            if student in students:
                print('Student index:', students.index(student))
            else:
                print('Student not found')

    elif choice == 5:
        break
    else:
        print('Invalid choice, please try again!')
```

---

## 🐛 Fixes Made
- ✅ Changed `if students == 0:` → `if len(students) == 0:` (to check if list is empty).  
- ✅ Fixed search logic to handle cases where student is not found.  
- ✅ Improved exit option text.  

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   ```
2. Navigate to the project folder:
   ```bash
   cd student-management-system
   ```
3. Run the script:
   ```bash
   python student_management.py
   ```

---

## 📌 Future Improvements
- Add student details (age, roll number, course).  
- Save student records to a file or database.  
- Create a GUI version using Tkinter or PyQt.  

---

## 🏷️ License
This project is open source – feel free to use and modify it.

---



students = []

while True:
   print("n===WELCOME TO STUDENT SYSTEM ===")
   print("1. Add Student")
   print("2. View Students")
   print("3. Exit")
   
   choice = input("Choose option: ")
   
   if choice == "1":
      name = input("Enter student name: ")
      matric = input("Enter matric number: ")
      
      students.append({"name": name, "matric": matric})
      print("Student added!")
      
   elif choice == "2":
      print("\n--- Student List ---")
      if len(students) == 0:
         print("No students yet.")
      else:
         for i, s in enumerate(students, 1):
            print("{}. {} ({})".format(i, s['name'], s['matric']))
            
    elif choice == "3" :
       print("Bye!")
       break
       
    else:
       print("Invalid choice")
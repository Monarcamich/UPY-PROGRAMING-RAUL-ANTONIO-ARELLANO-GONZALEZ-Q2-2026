# Required Structures
users = {
    'jperez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo':	{
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':	{
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}
 
subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)
 
notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

print("-------------------------------------")
print("WELCOME TO SCHOOL MANAGEMENT PROGRAM")
print("-------------------------------------")

#INPUT
#Login section
loggedin=False
while not loggedin:
    username=input("Enter your username:")
    password=input("Enter your password:")

    if username in users and users[username]['password'] == password:
        loggedin=True
        print(f"Hi {users[username]['name']}! You are logged in as a {users[username]['rol']}.")
        role = users[username]['rol']
        break
    else:
        print("Invalid username or password. Please try again.")

#PROCCESS
#Student Section
if role == 'student':
    print(f"Report Card: {users[username]['name']}")
    
    for subject in subjects:
        grade = notes[username][subject]
        print(f"{subject}: {grade}")
    
    approved = set()
    for subject in subjects:
        if notes[username][subject] >= 8.0:
            approved.add(subject)
    
    pending = set(subjects) - approved
    
    print(f"\nApproved subjects: {approved}")
    print(f"Pending subjects: {pending}")

#Professor Section
elif role == 'professor':
 while True:
        print("Students")
        for user in users:
            if users[user]['rol'] == 'student':
                print(f"User: {user} | Student: {users[user]['name']}")

        student = input("\nStudent to grade (username): ")

        # Exit condition: if user presses Enter without typing a username
        if student == "":
            break

        if student in notes:
            print("Subjects")
        
            for subject in subjects:
                print(subject)

            subject = input("\nSubject to grade: ")

            if subject in subjects:
                # Get current grade
                current_grade = notes[student][subject]
                new_grade = float(input("New grade: "))
                confirmation = input("Do you confirm (yes/no)? ")

                # Show grade change
                print(f"{subject}: {current_grade} ==> {new_grade}")

                if confirmation.lower() == 'yes':
                    notes[student][subject] = new_grade
                    print("Grade updated!")
                    # Print all grades for this student
                    print(notes[student])
                else:
                    print("Write other thing to exit")
            else:
                print("Invalid subject.")
        else:
            print("Invalid student username.\nExit: presses Enter without typing a username")


#Coordinator Seccion
elif role == 'coordinator':
    print(" COORDINATOR REPORT ")
    
    print("Professors")
    for user_key in users:
        if users[user_key]['rol'] == 'professor':
            print(f"  - {users[user_key]['name']} ({user_key})")
    
    print("Subjects")
    for subject in subjects:
        print(f"  - {subject}")
    
    print("Students & Grades")

    for student_username in notes:
        student_name = users[student_username]['name']

        print(f"\n{student_name} ({student_username}):")
        for subject in subjects:
            grade = notes[student_username][subject]
            print(f"    {subject}: {grade}")

else:
    print("Unknown role.")

#OUTPUT
print("\nThank you for using the School Management Program. Goodbye!")




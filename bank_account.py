gpa_database = []
name_database = []
classes_database = []
school_database = []
password_database = []
f_note = []
s_note = []
t_note = []
fo_note = []
fi_note = []
si_note = []
se_note = []
ei_note = []
ni_note = []
f_date = []
s_date = []
t_date = []
fo_date = []
fi_date = []
si_date = []
se_date = []
ei_date = []
ni_date = []
class Account:
    def binarysearch(array,key,left,right):
        if left == 0 and right == 0:
            left = min(range(len(array)))
            right = len(array) 
        if left > right:
            return False
        mid = int((left+right)/2)
        if key == array[mid]: 
            return True
            mid_database.append(mid)
        if key > array[mid]:
            return Account.binarysearch(array,key,mid+1,right)
        if key < array[mid]:
            return Account.binarysearch(array,key,left,mid-1)
    def set_info(gpa,name,school,password):
        student_name = name
        name_database.append(student_name) 
        student_school = school
        school_database.append(student_school)
        student_password = password
        password_database.append(student_password)
        if gpa == 0:
            pass
        if gpa > 0:
            student_gpa = gpa
            gpa_database.append(student_gpa)
    def sign_up(gpa,name,school,password,id):
        id = []
        Account.set_info(gpa,name,school,password)
    def sign_in(password):
        if Account.binarysearch(password_database,password,0,0) == True:
            return True
        else:
            return False
    def gpa(gpa_database):
        gpa_total = 0
        for i in gpa_database:
            gpa_total += i
        return gpa_total/len(gpa_database)
def executable_code():
    print("1. Sign up")
    print("2. Sign in")
    sign_in_up = int(input())
    if sign_in_up == 1:
        gpa = float(input("GPA/ if you don't know input 0"))
        print("")
        name = input("Full name")
        print("")
        school = input("School name")
        print("")
        password = input("Choose a password")
        print("")
        id_gpa = input("Input the first number of your id (written in english)")
        print("")
        Account.sign_up(gpa,name,school,password,id_gpa)
        add_classes = input("Would you like to add your classes?")
        if add_classes == "Y":
            print("")
            first = input("First period") 
            print("")
            second = input("Second")
            print("")
            third = input("Third")
            print("")
            fourth = input("Fourth")
            print("")
            fifth = input("Fifth")
            print("")
            sixth = input("Sixth")
            print("")
            seventh = input("Seventh")
            print("")
            eighth = input("Eighth")
            print("")
            nineth = input("Nineth")
            executable_code()
            student_classes = [first,second,third,fourth,fifth,sixth,seventh,eighth,nineth]
            classes_database.append(student_classes)
        else:
            print("")
            executable_code()
    if sign_in_up == 2:
        password = input("Input your password")
        print("")
        if Account.sign_in(password) == True:
            if len(classes_database) == 0:
                print("1. 1st period")
                print("")
                print("2. 2nd period")
                print("")
                print("3. 3rd period")
                print("")
                print("4. 4th period")
                print("")
                print("5. 5th period")
                print("")
                print("6. 6th period")
                print("")
                print("7. 7th period")
                print("")
                print("8. 8th period")
                print("")
                print("9. 9th period")
                print("")
                print("10. Info")
                print("")
                print("11. Exit")
            if len(classes_database) > 0:
                print("1. ",classes_database[0][0])
                print("")
                print("2. ",classes_database[0][1])
                print("")
                print("3. ",classes_database[0][2])
                print("")
                print("4. ",classes_database[0][3])
                print("")
                print("5. ",classes_database[0][4])
                print("")
                print("6. ",classes_database[0][5])
                print("")
                print("7. ",classes_database[0][6])
                print("")
                print("8. ",classes_database[0][7])
                print("")
                print("9. ",classes_database[0][8])
                print("")
                print("10. Info")
                print("")
                print("11. Exit")
            home_screen_input = int(input())
            if home_screen_input == 1:
                if len(gpa_database) > 0:
                    print(gpa_database[0])
                else:
                    add_gpa_ask = input("Would you like to add your grade for this class?")
                    print("")
                    if add_gpa_ask == 'Y':
                        add_gpa = float(input("Grade (0-100)"))
                        print("")
                        gpa_database.append(add_gpa)
                        executable_code()
                for i in range(len(f_note)):
                    print("Dates:",f_date[i])
                    print("Notes:",f_note[i])
                print("Add new notes?")
                add_notes = input()
                if add_notes == "Y":
                    new_date = input("Date")
                    print("")
                    new_note = input("Note") 
                    f_note.append(new_note)
                    f_date.append(new_date)
                    print("")
                    print("Would you like to exit?")
                    exit_two = input()
                    if exit_two == "Y":
                        executable_code()
                    else:
                        pass
                if add_notes == "N":
                    exit = input("Exit?")
                    if exit == "Y":
                        executable_code()
                    else:
                        pass
            if home_screen_input == 2:
                for a in range(len(notes_database)):
                    print("Dates:",s_date[a])
                    print("Notes:",s_note[a])
                add_notes_two = input("Add new notes?")
                if add_notes_two == "Y": 
                    new_date_two = input("Date")
                    print("")
                    new_note_two = input("Note")
                    s_note.append(new_note_two)
                    s_date.append(new_date_two) 
                if add_notes_two == "N": 
                    exit = input("Exit?")
                    if exit == "Y":
                        executable_code()
                    else:
                        pass
            if home_screen_input == 3:
                for b in range(len(notes_database)):
                    print("Dates:",t_date[b])
                    print("Notes:",t_note[b]) 
                add_notes_three = input("Add new notes?")
                if add_notes_three == "Y":
                    new_date_three = input("Date")
                    new_note_three = input("Note")
                    t_note.append(new_note_three)
                    t_date.append(new_date_three)
                if add_notes_three == "N": 
                    exit = input("Exit?")
                    if exit == "Y": 
                        executable_code()
                    else:
                        pass
            if home_screen_input == 4:
                for c in range(len(notes_database)):
                    print("Dates:",fo_date[c]) 
                    print("Notes:",fo_note[c]) 
                add_notes_four = input("Add new notes?") 
                if add_notes_four == "Y":
                    new_date_four = input("Date")
                    new_note_four = input("Note") 
                    fo_note.append(new_note_four)
                    fo_date.append(new_date_four) 
                if add_notes_four == "N": 
                    exit = input("Exit?")
                    if exit == "Y": 
                        executable_code()
                    else:
                        pass
            if home_screen_input == 5:
                for d in range(len(notes_database)): 
                    print("Dates:",fi_date[d])
                    print("Notes:",fi_note[d])
                add_notes_five = input("Add new notes?")
                if add_notes_five == "Y":
                    new_date_five = input("Date") 
                    new_note_five = input("Note") 
                    fi_note.append(new_note_five) 
                    fi_date.append(new_date_five) 
                if add_notes_five == "N": 
                    exit = input("Exit?")
                    if exit == "Y": 
                        executable_code()
                    else:
                        pass
            if home_screen_input == 6:
                for e in range(len(notes_database)): 
                    print("Dates:",si_date[e]) 
                    print("Notes:",si_note[e]) 
                add_notes_six = input("Add new notes?")
                if add_notes_six == "Y":
                    new_date_six = input("Date")
                    new_note_six = input("Note")
                    si_note.append(new_note_six)
                    si_date.append(new_date_six)
                if add_notes_six == "N": 
                    exit = input("Exit?")
                    if exit == "Y": 
                        executable_code()
                    else:
                        pass
            if home_screen_input == 7:
                for f in range(len(notes_database)):
                    print("Dates:",se_date[f])
                    print("Notes:",se_note[f])
                add_notes_seven = input("Add new notes?")
                if add_notes_seven == "Y":
                    new_date_seven = input("Date")
                    new_note_seven = input("Note")
                    se_note.append(new_note_seven)
                    se_date.append(new_date_seven)
                if add_notes_seven == "Y":
                    exit = input("Exit?")
                    if exit == "Y": 
                        executable_code()
                    else:
                        pass
            if home_screen_input == 8:
                for g in range(len(notes_database)):
                    print("Dates:",ei_date[g])
                    print("Notes:",ei_note[g])
                add_notes_eight = input("Add new notes?")
                if add_notes_eight == "Y":
                    new_date_eight = input("Date")
                    new_note_eight = input("Note")
                    ei_note.append(new_note_eight)
                    ei_date.append(new_date_eight)
                if add_notes_seven == "Y":
                    exit = input("Exit?")
                    if exit == "Y": 
                        executable_code()
                    else:
                        pass
            if home_screen_input == 9:
                for h in range(len(notes_database)):
                    print("Dates:",ni_date[h])
                    print("Notes:",ni_note[h])
                add_notes_nine = input("Add new notes?")
                if add_notes_nine == "Y":
                    new_date_nine = input("Date")
                    new_note_nine = input("Note")
                    ni_note.append(new_note_nine)
                    ni_date.append(new_date_nine)
                if add_notes_nine == "N":
                    exit = input("Exit?")
                    if exit == "Y": 
                        executable_code()
                    else:
                        pass
            if home_screen_input == 10:
                for l in range(len(password_database)):
                    if password_database[l] == password:
                        print(gpa_database[l])
                        print("")
                        print(name_database[l])
                        print("")
                        print(school_database[l])
                        print("")
                        print(password_database[l])
                        print("")
                        for d in classes_database[l]:
                            print("class ",l)
                            print("")
                            print(d)
            if home_screen_input == 11:
                executable_code()
        else:
            return False
executable_code()
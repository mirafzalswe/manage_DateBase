import psycopg2
import animation
from config import host, db_name, password, user
from procces import delete_stuendts, search_students, add_students


choose = input('''Hi, you can find students you are interested in and add new students and delete.
 Which one do yuo want (add or find or delete): ''')
if choose == 'find' or choose == 'Find':
    country_lk = input("Which country are you looking for students from (if it doesn't matter just click enter): ")
    date_br_lk = input("Write dates of birth of students (yyyy-mm-dd): ")
    date_br_lk2 = input("Until what year should it be (yyyy-mm-dd): ")
    univer_lk = input("From which university should be (if it doesn't matter just click enter): ")
    job_lk = input("Which specialists are you interested in: ")

    students = search_students(country_lk, date_br_lk, date_br_lk2, univer_lk, job_lk)
    print("Students on your request: ")
    animation.loading_animation(3)
    for student in students:
        print(f"| {student[1]} | {student[2]} | {student[3]} | {student[4]} | {student[5]} | {student[6]} |")
elif choose=="add":
    add_students()
elif choose == 'delete' or choose == 'Delete':
    delete_stuendts()

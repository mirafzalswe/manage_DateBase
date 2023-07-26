import psycopg2
import animation
from config import host, db_name, password, user



def delete_stuendts():
    try:
        connection = psycopg2.connect(database=db_name, user=user, host=host, password=password)
        cur = connection.cursor()
        delete_st = input("Enter the ID of the student you want to delete: ")
        query = f'''
        DELETE FROM students
        WHERE id = {delete_st};
        '''
        cur.execute(query)
        connection.commit()
        animation.loading_animation(2)
        print("Student deleted successfuly! ")
    except psycopg2.Error:
        print(f"ERROR: {psycopg2.Error}")
    finally:
        cur.close()
        connection.close()

def add_students():
    try:
        connection = psycopg2.connect(database=db_name, user=user, host=host, password=password)
        cur = connection.cursor()
        full_name = input("Enter your full name: ")
        country = input("Which country do you live in: ")
        passport = input("Enter your passport ID: ")
        date = input("Enter your date of birth (yyyy-mm-dd): ")
        major = input("Which yo're specialists: ")

        query = f"""
        INSERT INTO students (full_name, country, passport, date_of_birth, major)
        VALUES ('{full_name}', '{country}', '{passport}', '{date}', '{major}');
        """
        cur.execute(query)
        connection.commit()
        animation.loading_animation(2)
        print("Student added successfully!")
    except psycopg2.Error :
        print(f"Error: {psycopg2.Error}")
        print("Please try again")
    finally:
        cur.close()
        connection.close()






def search_students(country, date_of_birth_start, date_of_birth_end, university, major):
    try:
        connection = psycopg2.connect(database=db_name, user=user, host=host, password=password)
        cur = connection.cursor()

        query = f'''
        SELECT * FROM students
        WHERE 1 = 1
        '''

        if country:
            query += f"AND country = '{country}' "

        if date_of_birth_start:
            query += f"AND date_of_birth >= '{date_of_birth_start}' "

        if date_of_birth_end:
            query += f"AND date_of_birth <= '{date_of_birth_end}' "

        if university:
            query += f"AND university = '{university}' "

        if major:
            query += f"AND major = '{major}' "

        cur.execute(query)

        return cur.fetchall()
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        connection.close()


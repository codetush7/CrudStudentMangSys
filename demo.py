import psycopg2
def create_table():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="8984",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key,name text,address text,age int,ph_num text);")
    print("Student table created")
    conn.commit()
    conn.close()

def insert_Values():
    #code to accept data from user
    name = input("Enter name ")
    address = input("Enter address ")
    age = input("Enter age")
    phone_number = input("Enter Phone Number")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="8984",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("insert into students(name,address,age,ph_num) values (%s,%s,%s,%s)",(name,address,age,phone_number))
    print("Data inserted in Students Table")
    conn.commit()
    conn.close()


def update_Values():
    #code to accept data from user
    id = input("Enter id of the students you want to update")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="8984",host="localhost",port="5432")
    cur = conn.cursor()
    field={
        '1':("name","Enter name "),
        '2':("address","Enter address "),
        '3':("age","Enter age"),
        '4':("ph_num","Enter Phone Number")
    }
    print("Which field you want to update ?")
    for key in field:
        print(f'{key}:{field[key][0]}')
    field_choice = input("Which field do you want to update? ")

    if field_choice in field:
        field_name,prompt = field[field_choice]
        new_Val = input(prompt)
        sql = f"update students set {field_name} = %s where student_id= %s"
        cur.execute(sql,(new_Val,id))
        print(f"{field_name} updated Successfully")
    else:
        print("Invalid choice")    
    conn.commit()
    conn.close()
def read_Data():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="8984",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("select * from students;")
    students = cur.fetchall()       
    for student in students:
        print(f"ID : {student[0]}, Name : {student[1]},Address :{student[2]},Age: {student[3]},Phone_number: {student[4]} ")

def delete_data():
    student_id = input("Enter id of the students you want to delete")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="8984",host="localhost",port="5432")
    cur = conn.cursor()

    cur.execute("select * from students where student_id = %s",(student_id,))
    student = cur.fetchone()

    if student:
        print(f"Student to be deleted : ID {student[0]} ,Name : {student[1]} ,Address :{student[2]} ,Age: {student[3]} ,Phone_number: {student[4]} ")
        choice = input("Enter Yes or no")
        if choice.lower() == "yes":
            cur.execute("delete from students where student_id=%s",(student_id,))
            print("Record Deleted ")
        else:
            print("Delete cancelled ")
    else:
        print("Invalid Student id ")
    
    conn.commit()
    conn.close()

while True:
    print("\n Welcome to the student database management System")

    print("1. Create Table: ")
    print("2. Insert Data ")
    print("3. Read Data ")
    print("4. Update Data ")
    print("5. Delete Data ")
    print("6. Exit ")

    choice = input("Enter your choice")

    if choice == '1':
        create_table()
    elif choice == '2':
        insert_Values()
    elif choice == '3':
        read_Data()
    elif choice == '4':
        update_Values()
    elif choice =='5':
        delete_data()
    elif choice == '6':
        break
    else:
        print("Invalid Choice Please Enter a number between 1-6 ")




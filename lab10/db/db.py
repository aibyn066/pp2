import psycopg2
import csv

import os

conn = psycopg2.connect(
    database = "phonebook",
    user = "postgres",
    password = "071106",
    host = "localhost",
    port = "5432"
)

cur = conn.cursor()

# из цсв в бд
def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("📥 CSV деректері қосылды.")





# вручуню заполнить бд
def insert_from_input():
    name = input("Атыңызды енгізіңіз: ")
    phone = input("Телефон нөмірі: ")
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("✅ Жаңа контакт қосылды.")




# обновить контакт
def update_contact():
    contact_id = input("Қай ID жаңартасың? ")
    new_name = input("Жаңа аты: ")
    new_phone = input("Жаңа телефон: ")
    cur.execute("UPDATE contacts SET name = %s, phone = %s WHERE id = %s", (new_name, new_phone, contact_id))
    conn.commit()
    print("♻️ Контакт жаңартылды.")




#искать контк
def query_with_filter():
    keyword = input("Аты не номер бойынша ізде: ")
    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s OR phone ILIKE %s", (f'%{keyword}%', f'%{keyword}%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)



#удалть

def delete_contact():
    contact_id = input("Қай ID өшіргің келеді? ")
    cur.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
    conn.commit()
    print("❌ Контакт өшірілді.")

#показать все
def show_all_contacts():
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    if rows:
        print("\n📋 Барлық контакттар:")
        for row in rows:
            print(f"ID: {row[0]}, Аты: {row[1]}, Тел: {row[2]}")
    else:
        print("🔍 Контакттар табылмады.")



def menu():
    run = True
    while run:
        print("\n📱 PHONEBOOK MENU:")
        print("1 - insert csv")
        print("2 - from input")
        print("3 - update contact")
        print("4 - query with filter")
        print("5 - delete contact")
        print("6 - break")
        print("7 - show all contacts")
        
        
        choice = input("Таңдаңыз (1–7): ")

        if choice == '1':
            insert_from_csv('/Users/ajbynkumargali/Desktop/projects_pp2/lab10/db/ph.csv')
            
        elif choice == '2':
            insert_from_input()

        elif choice == '3':
            update_contact()

        elif choice == '4':
            query_with_filter()

        elif choice == '5':
            delete_contact()

        elif choice == '6':
            run = False
        elif choice == '7':
            show_all_contacts()
        else:
            print("❗ Қате таңдау.")
    

menu()
cur.close()
conn.close()
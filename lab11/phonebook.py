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

def search_by_pattern():
    pattern = input("Іздеу үлгісін енгізіңіз (аты/нөмірі): ")
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    if rows:
        print("🔎 Табылған контакттар:")
        for row in rows:
            print(f"ID: {row[0]}, Аты: {row[1]}, Тел: {row[2]}")
    else:
        print("❌ Ештеңе табылмады.")

def add_or_update_contact():
    name = input("Аты: ")
    phone = input("Телефон нөмірі: ")
    cur.execute("SELECT add_or_update_contact(%s, %s)", (name, phone))
    conn.commit()
    print("✅ Қосылды немесе жаңартылды.")

def add_multiple_contacts():
    count = int(input("Қанша контакт қосқыңыз келеді? "))
    names = []
    phones = []
    for _ in range(count):
        name = input("Аты: ")
        phone = input("Телефон нөмірі: ")
        names.append(name)
        phones.append(phone)
    cur.execute("SELECT add_multiple_contacts(%s, %s)", (names, phones))
    conn.commit()
    print("📥 Барлық контакттар өңделді (қате нөмірлер - NOTICE-те).")
#11
def getDataFromPagination():
    print("\n📖 Просмотр контактов постранично")
    
    try:
        # Получаем параметры пагинации
        limit = int(input("Сколько контактов показать на странице: ") or 3)
        page = int(input("Номер страницы (начиная с 1): ") or 1)
        offset = (page - 1) * limit
        
        # Прямой SQL-запрос с LIMIT и OFFSET
        cur.execute("""
            SELECT id, name, phone 
            FROM contacts 
            ORDER BY id 
            LIMIT %s OFFSET %s
        """, (limit, offset))
        
        contacts = cur.fetchall()
        
        if not contacts:
            print("\n🔍 Контакты не найдены")
            return
            
        # Вывод результатов
        print(f"\n📄 Страница {page}:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. ID: {contact[0]}, Аты: {contact[1]}, Тел: {contact[2]}")
        
        # Дополнительная информация
        cur.execute("SELECT COUNT(*) FROM contacts")
        total = cur.fetchone()[0]
        print(f"\nВсего контактов: {total}")
        print(f"Всего страниц: {max(1, (total + limit - 1) // limit)}")
        
    except ValueError:
        print("❌ Ошибка: Введите целые числа")
    except Exception as e:
        print(f"❌ Ошибка базы данных: {e}")
def check_contact(name):
    cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    print(f"Найдены контакты: {cur.fetchall()}")

def delete_contact_by_name_or_phone():
    print("\nУдаление контакта")
    print("1 - По точному имени.")
    print("2 - По точному номеру")
    
    choice = input("Выберите (1/2): ")
    
    if choice == '1':
        name = input("Введите ТОЧНОЕ имя: ").strip()
        check_contact(name)  # Проверка перед удалением
        
        try:
            # Прямой SQL-запрос вместо процедуры для теста
            cur.execute("DELETE FROM contacts WHERE name = %s RETURNING id", (name,))
            deleted = cur.fetchone()
            
            if deleted:
                conn.commit()
                print(f"Удален контакт ID: {deleted[0]}")
            else:
                conn.rollback()
                print("Контакт не найден!")
                
        except Exception as e:
            conn.rollback()
            print(f"Ошибка удаления: {e}")
    
    elif choice == '2':
        phone = input("Введите ТОЧНЫЙ номер: ").strip()
        try:
            cur.execute("DELETE FROM contacts WHERE phone = %s RETURNING *", (phone,))
            result = cur.fetchone()
            
            if result:
                conn.commit()
                print(f"Удален: ID {result[0]}, Имя: {result[1]}")
            else:
                print("Номер не найден!")
                conn.rollback()
                
        except Exception as e:
            conn.rollback()
            print(f"Ошибка: {e}")

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
        print("8 - search by pattern (SQL function)")
        print("9 - add/update (SQL procedure)")
        print("10 - add many (SQL procedure)")
        print("11 - pagination")
        print("12 - delete by name or phone (SQL proc)")

        
        
        choice = input("Таңдаңыз (1–12): ")

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
        elif choice == '8':
            search_by_pattern()
        elif choice == '9':
            add_or_update_contact()
        elif choice == '10':
            add_multiple_contacts()
        elif choice == '11':
            getDataFromPagination()
        elif choice == '12':
            delete_contact_by_name_or_phone()

        else:
            print("❗ Қате таңдау.")
    

menu()
cur.close()
conn.close()
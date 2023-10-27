import sqlite3

def create_table():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone_number TEXT,
                email TEXT)''')
    conn.commit()
    conn.close()

def add_contact(name, phone_number, email):
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute('''INSERT INTO contacts (name, phone_number, email)
                VALUES (?, ?, ?)''', (name, phone_number, email))
    conn.commit()
    conn.close()

def search_contact_by_name(name):
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE name=?", (name,))
    result = c.fetchall()
    conn.close()
    return result

def view_all_contacts():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    result = c.fetchall()
    conn.close()
    return result

def delete_contact_by_name(name):
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()
    conn.close()

# Создаем таблицу
create_table()

# Добавляем контакт
add_contact('John Doe', '1234567890', 'johndoe@email.com')

# Ищем контакт по имени
search_result = search_contact_by_name('John Doe')
print(search_result)

# Получаем все контакты
all_contacts = view_all_contacts()
print(all_contacts)

# Удаляем контакт
delete_contact_by_name('John Doe')

# Проверяем, что контакт удален
all_contacts = view_all_contacts()
print(all_contacts)
import psycopg2
from psycopg2 import sql

# Параметры подключения к PostgreSQL (измените под свои)
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'лаба 1',
    'user': 'postgres',
    'password': 1234
}

conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS doctors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    experience INTEGER NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS diagnoses (
    id SERIAL PRIMARY KEY,
    diagnosis_name VARCHAR(200) NOT NULL,
    prescription_date DATE NOT NULL
)
''')
conn.commit()

while True:
    print("\n=== МЕНЮ ===")
    print("1 - Пациенты")
    print("2 - Врачи")
    print("3 - Диагнозы")
    print("0 - Выход")
    choice = input("Выберите таблицу: ")

    if choice == "0":
        break

    if choice not in ("1", "2", "3"):
        print("Неверный ввод")
        continue

    # Определяем имя таблицы и поля
    if choice == "1":
        table = "patients"
        fields = ("name", "age")
    elif choice == "2":
        table = "doctors"
        fields = ("name", "experience")
    else:
        table = "diagnoses"
        fields = ("diagnosis_name", "prescription_date")

    while True:
        print(f"\n--- {table.upper()} ---")
        print("1 - Просмотреть все")
        print("2 - Добавить")
        print("3 - Изменить")
        print("4 - Удалить")
        print("0 - Назад")
        action = input("Действие: ")

        if action == "0":
            break

        if action == "1":
            cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(table)))
            rows = cursor.fetchall()
            if not rows:
                print("Нет записей.")
            else:
                for row in rows:
                    print(row)

        elif action == "2":
            if table == "patients":
                name = input("Имя: ")
                age = int(input("Возраст: "))
                cursor.execute(f"INSERT INTO {table} (name, age) VALUES (%s, %s)", (name, age))
            elif table == "doctors":
                name = input("Имя: ")
                exp = int(input("Стаж: "))
                cursor.execute(f"INSERT INTO {table} (name, experience) VALUES (%s, %s)", (name, exp))
            else:  # diagnoses
                diag = input("Название диагноза: ")
                date = input("Дата (ГГГГ-ММ-ДД): ")
                cursor.execute(f"INSERT INTO {table} (diagnosis_name, prescription_date) VALUES (%s, %s)", (diag, date))
            conn.commit()
            print("Добавлено.")

        elif action == "3":
            id_val = int(input("ID записи для изменения: "))
            if table == "patients":
                name = input("Новое имя: ")
                age = int(input("Новый возраст: "))
                cursor.execute(f"UPDATE {table} SET name=%s, age=%s WHERE id=%s", (name, age, id_val))
            elif table == "doctors":
                name = input("Новое имя: ")
                exp = int(input("Новый стаж: "))
                cursor.execute(f"UPDATE {table} SET name=%s, experience=%s WHERE id=%s", (name, exp, id_val))
            else:
                diag = input("Новое название диагноза: ")
                date = input("Новая дата (ГГГГ-ММ-ДД): ")
                cursor.execute(f"UPDATE {table} SET diagnosis_name=%s, prescription_date=%s WHERE id=%s", (diag, date, id_val))
            conn.commit()
            print("Изменено.")

        elif action == "4":
            id_val = int(input("ID записи для удаления: "))
            cursor.execute(f"DELETE FROM {table} WHERE id=%s", (id_val,))
            conn.commit()
            print("Удалено.")

        else:
            print("Неверный ввод.")

cursor.close()
conn.close()
print("До свидания!")
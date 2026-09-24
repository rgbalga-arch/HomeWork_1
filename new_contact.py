from pathlib import Path
contacts_path = Path("contacts.json")
import json

if not contacts_path.exists():
    with open("contacts.json", "w", encoding="UTF-8") as contacts_file:
        data_cont = contacts_file.read()

else:
    name = input("напишите имя ")
    while True:
        try:
            phone = int(input("Введите номер телефона: "))
            break
        except ValueError:
            print("Ошибка! Введите только цифры.")
    comment = input("Напишите комментарий ")


    with open("contacts.json", "a", encoding="UTF-8") as contacts_file:
        phone_list = {"name": name, "phone": phone, "comment": comment}
        json.dump(phone_list, contacts_file, ensure_ascii=False)
        contacts_file.write("\n")

with open("contacts.json", "r", encoding="UTF-8") as contacts_file:
    data = contacts_file.read()
print(data)

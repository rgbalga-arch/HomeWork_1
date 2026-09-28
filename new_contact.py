from pathlib import Path
import json
#data_cont = []



def new_reg():
    contacts_path = Path("contacts.json")
    data_cont = []
    if contacts_path.exists():
        with open(contacts_path, "r", encoding="UTF-8") as contacts_file:
            for line in contacts_file:
                data_cont.append(json.loads(line))
    name = input("напишите имя ")
    while True:
        try:
            phone = int(input("Введите номер телефона: "))
            break
        except ValueError:
            print("Ошибка! Введите только цифры.")

    for contact in data_cont:
        if phone == contact["phone"]:
            print("Ошибка! Такой номер уже существует.")
            return


    comment = input("Напишите комментарий ")
    phone_list = {"name": name, "phone": phone, "comment": comment}

    with open("contacts.json", "a", encoding="UTF-8") as contacts_file:
        json.dump(phone_list, contacts_file, ensure_ascii=False)
        contacts_file.write("\n")

#print("hello world")

#git add test.py
#git status
#git commit -m "Add test.py"
#git log
#git add . добавить все файлы



#git commit -am "updated test.py"
#git push -u origin main


#git pull

#git log --oneline

#git clone https://github.com/rgbalga-arch/HomeWork_1.git     ССФЛКА НА ЧУЖОЙ РЕПОЗИТОРИЙ

# while True:
#     try:
#         phone = int(input("Введите номер телефона: "))
#         break
#     except ValueError:
#         print("Ошибка! Введите только цифры.")

def int_check() -> int:
    phone = input("Введите номер телефона: ")

    while not phone.isdigit():
        print("Ошибка! Введите только цифры.")
        phone = input("Введите номер телефона: ")
    return int(phone)

phone = int_check()
print(phone)
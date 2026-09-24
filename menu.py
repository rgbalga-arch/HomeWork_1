def menu():
    while True:
        print("1 - чтобы добавить контакт")
        print("2 - чтобы посмотреть все контакты")
        print("3 - чтобы найти контакт")
        print("4 - чтобы изменить контакт")
        print("5 - чтобы удалить контакт")

        action_menu = input("Выберите действие: ")

        if action_menu == "1":
            import new_contact
        elif action_menu == "2":
            import see_all
        elif action_menu == "3":
            import find_contact
        elif action_menu == "4":
            import edit_contact
        elif action_menu == "5":
            import delete_contct
        else:
            print("неверная команда")
menu()

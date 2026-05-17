from manager import FinanceManager


def main():
    qarzhy_esebi = FinanceManager()


    qarzhy_esebi.load_from_json('data.json')

    while True:
        print("\n=== Personal Finance Tracker (FINAL) ===")
        print("1. Tranzakciya qosu (Добавить)")
        print("2. Tranzakciyalardy koru (Посмотреть все)")
        print("3. Balancety esepteu (Баланс)")
        print("4. Sanat boyinsha izdeu (Фильтр по категории)")
        print("5. Shygu (Выход)")

        tandau = input("Tandauynyzdy engiziniz (1-5): ")

        if tandau == '1':
            try:
                somasi = float(input("Somani engiziniz: "))
                sanaty = input("Sanatyn engiziniz: ")
                sipattamasy = input("Sipattamasyn engiziniz: ")
                turi = input("Turin engiziniz (Income/Expense): ")

                if turi not in ['Income', 'Expense']:
                    print("Qate! Turin durys engiziniz.")
                    continue

                qarzhy_esebi.add_transaction(somasi, sanaty, sipattamasy, turi)
            except ValueError:
                print("Qate! Soma san boluy kerek.")

        elif tandau == '2':
            transactions = qarzhy_esebi.get_all_transactions()
            if not transactions:
                print("\nТранзакций пока нет.")
            else:
                print("\n--- Barlyq tranzakciyalar ---")
                for t in transactions:
                    print(t)

        elif tandau == '3':
            print(f"\nQazirgi balance: {qarzhy_esebi.calculate_balance()} tg.")

        elif tandau == '4':
            izdew = input("Qanday sanatty izdeysiz? (Введите категорию для поиска): ")
            natije = qarzhy_esebi.filter_by_category(izdew)

            if not natije:
                print(f"\n'{izdew}' sanatynda tranzakciyalar tabylmady.")
            else:
                print(f"\n--- '{izdew}' sanatynyn tranzakciyalary ---")
                for t in natije:
                    print(t)

        elif tandau == '5':
            print("Saubolynyz! Проект успешно завершен!")
            break

        else:
            print("Qate tandau. 1 men 5 aralygynda san engiziniz.")


if __name__ == '__main__':
    main()
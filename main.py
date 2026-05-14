from manager import FinanceManager


def main():
    qarzhy_esebi = FinanceManager()

    # --- НОВОЕ: Загружаем данные из файла при старте ---
    qarzhy_esebi.load_from_json('data.json')

    while True:
        print("\n=== Personal Finance Tracker (Week 4: JSON) ===")
        print("1. Tranzakciya qosu (Добавить)")
        print("2. Tranzakciyalardy koru (Посмотреть все)")
        print("3. Balancety esepteu (Баланс)")
        print("4. Shygu (Выход)")

        tandau = input("Tandauynyzdy engiziniz (1-4): ")

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
            print("Saubolynyz!")
            break


if __name__ == '__main__':
    main()
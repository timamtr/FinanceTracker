from manager import FinanceManager

#
def main():
    qarzhy_esebi = FinanceManager()

    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Tranzakciya qosu (Добавить)")
        print("2. Tranzakciyalardy koru (Посмотреть все)")
        print("3. Balancety esepteu (Баланс)")
        print("4. Shygu (Выход)")

        tandau = input("Tandauynyzdy engiziniz (1-4): ")

        if tandau == '1':
            somasi = input("Somani engiziniz (например, 5000): ")
            sanaty = input("Sanatyn engiziniz (например, Tamaq, Zhol): ")
            sipattamasy = input("Sipattamasyn engiziniz (Описание): ")
            turi = input("Turin engiziniz (Income или Expense): ")

            qarzhy_esebi.add_transaction(somasi, sanaty, sipattamasy, turi)

        elif tandau == '2':
            print("\n--- Barlyq tranzakciyalar ---")
            for barlyq_tr in qarzhy_esebi.get_all_transactions():
                print(barlyq_tr)

        elif tandau == '3':
            print(f"\nQazirgi balance: {qarzhy_esebi.calculate_balance()} tg.")

        elif tandau == '4':
            print("Kelesi kezdeskenshe!")
            break

        else:
            print("Qate tandau. 1 men 4 aralygynda san engiziniz.")


if __name__ == '__main__':
    main()
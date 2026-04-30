from models import Transaction
from utils import log_areket


class FinanceManager:
    def __init__(self):
        self.transactions = []

    @log_areket
    def add_transaction(self, amount, category, description, type_trans):
        new_transaction = Transaction(amount, category, description, type_trans)
        self.transactions.append(new_transaction)
        print(f"Успешно добавлено: {new_transaction}")

    def get_all_transactions(self):
        return self.transactions

    def calculate_balance(self):
        balance = 0.0
        for t in self.transactions:
            if t.type == 'Income':
                balance += t.amount
            elif t.type == 'Expense':
                balance -= t.amount
        return balance
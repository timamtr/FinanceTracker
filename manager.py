import json
from models import Transaction
from utils import log_areket


class FinanceManager:
    def __init__(self):
        self.transactions = []

    @log_areket
    def add_transaction(self, amount, category, description, type_trans):
        new_transaction = Transaction(amount, category, description, type_trans)
        self.transactions.append(new_transaction)
        self.save_to_json('data.json')
        print(f"Успешно добавлено и сохранено: {new_transaction}")

    def get_all_transactions(self):
        return self.transactions

    def calculate_balance(self):
        balance = 0.0
        for t in self.transactions:
            if t.type == 'Income':
                balance += t.amount
            else:
                balance -= t.amount
        return balance

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            data = [t.__dict__ for t in self.transactions]
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_json(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.transactions = []
                for item in data:
                    t = Transaction(item['amount'], item['category'], item['description'], item['type'])
                    t.date = item['date']
                    self.transactions.append(t)
        except (FileNotFoundError, json.JSONDecodeError):
            self.transactions = []

    def filter_by_category(self, category_name):
        filtered_list = [t for t in self.transactions if t.category.lower() == category_name.lower()]
        return filtered_list
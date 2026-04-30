from datetime import datetime

class Transaction:
    def __init__(self, amount, category, description, type_trans):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.type = type_trans
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"[{self.date}] {self.type} | {self.category}: {self.amount} ({self.description})"
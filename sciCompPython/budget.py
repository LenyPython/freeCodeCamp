class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * (-1),
                                'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * (-1),
                                'description': f'Transfer to {other.name}'}
                               )

            other.ledger.append({'amount': amount,
                                'description': f'Transfer from {self.name}'}
                                )
            return True
        else:
            return False

    def check_funds(self, amount):
        return True if amount <= self.get_balance() else False

    def __str__(self):
        entries = []
        line = self.name
        while len(line) < 30:
            line = line + '*' if len(line) % 2 == 1 else '*' + line
        entries.append(line)
        for entry in self.ledger:
            title = entry['description']
            value = f'{entry["amount"]:.2f}'
            if len(title) + len(value) >= 30:
                line = title[:29 - len(value)] + ' ' + value
            else:
                line = title + ' ' * (30 - len(title) - len(value)) + value
            entries.append(line)

        entries.append(f'Total: {self.get_balance()}')
        return '\n'.join(entries)


def create_spend_chart(categories):
    answer = 'Percentage spent by category\n'
    names = dict()
    for category in categories:
        names[category.name] = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                names[category.name] -= transaction['amount']
    for key, value in names.items():
        names[key] = int(names[key] / sum(names.values()) * 100)

    char_bot = '    -' + '---' * len(names)
    for num in range(11):
        char = ''
        if num == 10:
            char += str(num) + '0| '
        elif num == 0:
            char += '  0| '
        else:
            char += ' ' + str(num) + '0| '

        for value in names.values():
            if value >= num * 10:
                char += 'o  '
            else:
                char += '   '
        char_bot = char + '\n' + char_bot
    answer += char_bot + '\n'

    for i in range(len(max(names.keys(), key=len))):
        line = '     '
        for cat in names.keys():
            if i < len(cat):
                line += cat[i] + '  '
            else:
                line += '   '
        answer += line
    return answer[:-1]

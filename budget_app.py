import sys


class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=None):
        if description is not None:
            self.ledger.append({'amount': amount, 'description': description})
        else:
            self.ledger.append({'amount': amount, 'description': ''})

    def withdraw(self, amount, description=None):
        if self.check_funds(amount) == True:
            if description is not None:
                self.ledger.append(
                    {'amount': - (amount), 'description': description})
            else:
                self.ledger.append({'amount': -(amount), 'description': ''})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def transfer(self, amount, budget_category):
        if self.check_funds(amount) == True:
            self.ledger.append(
                {'amount': -(amount), 'description': f'Transfer to {budget_category.category}'})
            budget_category.deposit(
                amount, description=f'Transfer from {self.category}')
            return True
        else:
            return False

    def __str__(self):
        first_row = ''
        final_balance = ''
        total_budget = 0

        first_row = self.category.center(30, '*')

        for item in self.ledger:
            description_part = item['description'][0:23]

            amount_part = str("{:.2f}".format(item['amount']))

            total_budget += item['amount']

            final_balance += description_part + ' ' * \
                (30-len(description_part)-len(amount_part)) + amount_part + '\n'

        balance = first_row + '\n' + final_balance + \
            'Total: ' + str(total_budget)
        return balance


# Example
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)


def create_spend_chart(categories):
    spent = {}
    for cat in categories:
        abs_cat = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                abs_cat += abs(item['amount'])
        spent[cat.category] = round(abs_cat, 2)
    total = sum(spent.values())
    perc_spent = {}
    for i in spent.keys():
        perc_spent[i] = int(round(spent[i]/total, 2)*100)
    output = 'Percentage spent by category\n'
    for i in range(100, -10, -10):
        output += f'{i}'.rjust(3) + '| '
        for percent in perc_spent.values():
            if percent >= i:
                output += 'o  '
            else:
                output += '   '
        output += '\n'
    output += ' '*4+'-'*(len(perc_spent.values())*3+1)
    output += '\n     '
    result_list = list(perc_spent.keys())
    max_len_category = max([len(i) for i in result_list])

    for i in range(max_len_category):

        for name in result_list:
            if len(name) > i:
                output += name[i] + '  '
            else:
                output += '   '
        if i < max_len_category-1:
            output += '\n     '

    return output


print(create_spend_chart([food, clothing]))

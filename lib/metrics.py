def total_profits(moves):
    profits = 0
    for move in moves:
        if move["type"] == "profit":
            profits += move["value"]

    return profits

def total_expenses(moves):
    expenses = 0
    for move in moves:
        if move["type"] == "expense":
            expenses += move["value"]

    return expenses

def total_balance(moves):
    profits = 0
    expenses = 0

    for move in moves:
        if move["type"] == "profit":
            profits += move["value"]
        else:
            expenses += move["value"]

    balance = profits - expenses

    return balance

def expenses_resume(moves):
    has = False
    categories = {}
    
    for move in moves:
        if move["type"] != "expense":
            continue

        category = move["category"]

        if category not in categories:
            categories[category] = move["value"]
        else:
            categories[category] += move["value"]
        has = True

    for category, value in categories.items():
        print(f"{category}: R$ {value:.1f}")

    print("\n")

    return has
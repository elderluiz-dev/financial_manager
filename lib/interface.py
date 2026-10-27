def clear_terminal():
    print('\033[H\033[2J', end='')

def main_menu():
    print("1. Registros")
    print("2. Movimentações")
    print("3. Métricas")
    print("0. Sair")
    choose = input("\n> ")

    return choose

def register_menu():
    print("1. Registrar receita")
    print("2. Registrar despesa")
    print("0. Voltar")
    choose = input("\n> ")

    return choose

def move_menu():
    print("1. Listar movimentações")
    print("2. Pesquisar por descrição")
    print("3. Pesquisar por categoria")
    print("4. Remover movimentação")
    print("0. Voltar")
    choose = input("\n> ")
    
    return choose

def metric_menu():
    print("1. Saldo atual")
    print("2. Total de receitas")
    print("3. Total de despesas")
    print("4. Resumo de gastos")
    print("0. Voltar")
    choose = input("\n> ")
    
    return choose
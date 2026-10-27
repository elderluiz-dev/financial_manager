from lib.interface import *
from lib.storage import *
from lib.moves import *
from lib.metrics import *
import json

def main():
    try:
        with open("moves.json", "r", encoding="utf-8") as file:
            moves = json.load(file)
    except FileNotFoundError:
        moves = []
    
    item_id = 0

    while True:
        clear_terminal()
        choose = main_menu()

        match choose:
            case "1":
                clear_terminal()
                while True:
                    reg_choose = register_menu()
                    match reg_choose:
                        case "1":
                            clear_terminal()
                            type = "profit"
                            desc = input("Descrição: ")
                            value = float(input("Valor: "))
                            category = input("Categoria: ")

                            profit = register(desc, value, category, type, item_id)
                            moves.append(profit)

                            clear_terminal()
                            print("Receita adicionada com sucesso!\n")
                            item_id += 1

                        case "2":
                            clear_terminal()
                            type = "expense"
                            desc = input("Descrição: ")
                            value = float(input("Valor: "))
                            category = input("Categoria: ")
                    
                            expense = register(desc, value, category, type, item_id)
                            moves.append(expense)
                    
                            clear_terminal()
                            print("Despesa adicionada com sucesso!\n")
                            item_id += 1

                        case "0":
                            clear_terminal()
                            break

                        case _:
                            clear_terminal()
                            print("Opção inválida")

            case "2":
                clear_terminal()
                while True:
                    move_choose = move_menu()
                    match move_choose:
                        case "1":
                            clear_terminal()
                            if moves == []:
                                print("Sem movimentações\n")
                            else:
                                show_moves(moves)

                        case "2":
                            clear_terminal()
                            if moves == []:
                                print("Sem movimentações\n")
                                continue

                            desc = input("Digite a descrição a ser buscada: ")
                            if search_by_desc(moves, desc) == False:
                                clear_terminal()
                                print("Nenhum item com essa descrição encontrado.")

                        case "3":
                            clear_terminal()
                            if moves == []:
                                print("Sem movimentações\n")
                                continue

                            cat = input("Digite a categoria a ser buscada: ")
                            if search_by_category(moves, cat) == False:
                                clear_terminal()
                                print("Nenhum item com essa categoria encontrado.")

                        case "4":
                            clear_terminal()
                            if moves == []:
                                print("Sem movimentações\n")
                                continue

                            rem_id = int(input("Digite o ID do item a ser removido: "))

                            clear_terminal()
                            if remove_move(moves, rem_id) == True:
                                print("Item removido com sucesso.\n")
                            else:
                                print("Nenhum item com esse ID encontrado.\n")

                        case "0":
                            clear_terminal()
                            break

                        case _:
                            clear_terminal()
                            print("Opção inválida")


            case "3":
                clear_terminal()
                while True:
                    metric_choose = metric_menu()
                    match metric_choose:
                        case "1":
                            clear_terminal()
                            balance = total_balance(moves)
                            print(f"Saldo atual: R$ {balance:.1f}")

                        case "2":
                            clear_terminal()
                            profits = total_profits(moves)
                            print(f"Receita total: {profits:.1f}")

                        case "3":
                            clear_terminal()
                            expenses = total_expenses(moves)
                            print(f"Despesas totais: {expenses:.1f}")

                        case "4":
                            clear_terminal()
                            if moves == []:
                                print("Sem movimentações\n")
                            else:
                                if expenses_resume(moves) == False:
                                    clear_terminal()
                                    print("Nenhuma despesa cadastrada.")

                        case "0":
                            clear_terminal()
                            break

                        case _:
                            clear_terminal()
                            print("Default")

            case "0":
                clear_terminal()

                with open("moves.json", "w", encoding="utf-8") as file:
                    json.dump(moves, file, indent=4, ensure_ascii=False)

                print("Programa encerrado pelo usuário. Os dados foram salvos em moves.json.")
                break
            case _:
                clear_terminal()
                print("Opção inválida")

if __name__ == "__main__":
    main()
from lib.interface import *

def main():
    while True:
        choose = main_menu()

        match choose:
            case "1":
                clear_terminal()
                while True:
                    reg_choose = register_menu()
                    match reg_choose:
                        case "0":
                            clear_terminal()
                            break

                        case _:
                            clear_terminal()
                            print("Default")

            case "2":
                clear_terminal()
                while True:
                    move_choose = move_menu()
                    match move_choose:
                        case "0":
                            clear_terminal()
                            break

                        case _:
                            clear_terminal()
                            print("Default")


            case "3":
                clear_terminal()
                while True:
                    metric_choose = metric_menu()
                    match metric_choose:
                        case "0":
                            clear_terminal()
                            break

                        case _:
                            clear_terminal()
                            print("Default")

            case "0":
                clear_terminal()
                break
            case _:
                clear_terminal()
                print("Opção inválida")

if __name__ == "__main__":
    main()
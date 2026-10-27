def show_moves(moves):
    for move in moves:
        if move['type'] == "profit":
            print("Tipo: Receita")
        else:
            print("Tipo: Despesa")
        print(f"ID: {move['id']}")
        print(f"{move['description']}")
        print(f"Valor: R$ {move['value']:.1f}")
        print(f"Categoria: {move['category']}")
        print("\n")

def remove_move(moves, id):
    for index, move in enumerate(moves):
        if move['id'] == id:
            moves.pop(index)
            return True

    return False

def search_by_desc(moves, desc):
    has = False
    for move in moves:
        if desc in move["description"]:
            if move['type'] == "profit":
                print("Tipo: Receita")
            else:
                print("Tipo: Despesa")
            print(f"ID: {move['id']}")
            print(f"{move['description']}")
            print(f"Valor: R$ {move['value']:.1f}")
            print(f"Categoria: {move['category']}")
            print("\n")

            has = True

    return has

def search_by_category(moves, cat):
    has = False
    for move in moves:
        if cat == move["category"]:
            if move['type'] == "profit":
                print("Tipo: Receita")
            else:
                print("Tipo: Despesa")
            print(f"ID: {move['id']}")
            print(f"{move['description']}")
            print(f"Valor: R$ {move['value']:.1f}")
            print(f"Categoria: {move['category']}")
            print("\n")

            has = True

    return has
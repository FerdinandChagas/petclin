

from utils.print import clean
"""Usado para renderizar uma lista de itens onde ao mesmo tempo consulta"""

def render_search(title: str, items: list):
    size = len(items)
    print(f"\n------------- {title} -------------\n".upper())
    for index in range(0, size):
        print("-------------------------------")
        print(f"Item {index}: \n{items[index]}")
    print("\nInforme sua entrada: ".upper())
    indice_menu = int(input())
    print("\n")
    if indice_menu < 0 or indice_menu >= size:
        clean()
        print("\nNão encontrado. Por favor, tente outro!\n".upper())
        return render_search(title, items)
    return items[indice_menu]

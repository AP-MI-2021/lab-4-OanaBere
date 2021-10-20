def print_menu():
    print('1. Citire liste')
    print('2. Verificare daca listele au acelasi numar de elemente pare. ')
    print('3. Intersectia listelor de multimi')
    print('4. ')
    print('x. Exit')

def citire_lista(lst):
    result_list = []
    dimensiune = int(input("Dimensiune lista: "))

    while dimensiune:
        element = int(input("Introduceti un element: "))
        result_list.append(element)
        dimensiune -= 1

    return result_list

def contor_de_elem_pare(lst):
    '''
    functie care determina daca cele doua liste au acelasi numar de elemente pare
    :param lst: lista de intregi
    :return: numarul de elemente pare
    '''
    contor = 0
    for i in lst:
        if i % 2 == 0:
            contor += 1
    return contor
def test_contor_elem_pare():
    assert contor_de_elem_pare([1, 2, 16, 95, 1, 7]) == 2
    assert contor_de_elem_pare([3, 5, 7, 8, 13]) == 1
    assert contor_de_elem_pare([1, 11, 71, 105]) == 0


def intersectia_multimilor(a, b):
    '''
    functie care returneaza intersectia listelor de multimi
    :param a: lista de intregi
    :param b: lista de intregi
    :return: lista de elemente comune
    '''
    return list(set(a) & set(b))





def main():
    lista1 = []
    lista2 = []
    test_contor_elem_pare()
    while True:
        print_menu()
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            lista1 = citire_lista(lista1)
            lista2 = citire_lista(lista2)
        elif optiune == '2':
            if contor_de_elem_pare(lista1) == contor_de_elem_pare(lista2):
                print('Listele au acelasi numar de elemente pare.')
            else:
                print('Listele nu au acelasi numar de elemente pare. ')
        elif optiune == '3':
            print(intersectia_multimilor(lista1, lista2))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')

main()








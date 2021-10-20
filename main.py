def print_menu():
    print('1. Citire liste')
    print('2. Verificare daca listele au acelasi numar de elemente pare. ')
    print('3. Intersectia listelor de multimi')
    print('4. Palindroamele obtinute prin concatenarea elementelor de pe aceleasi pozitii')
    print('5. listele obținute prin înlocuirea în cele două liste citite a tuturor elementelor cu oglinditul lor dacă îndeplinesc regula specificata')
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

def numar_palindrom(nr):
    '''
    functie care determina daca un numar este palindrom sau nu
    :param nr: int
    :return: True daca numarul este palindrom, False in caz contrar
    '''
    inv = 0
    copie = nr
    while copie:
        inv = inv * 10 + (copie % 10)
        copie = copie // 10
    if nr == inv:
        return True
    else:
        return False


def test_numar_palindrom():
    assert numar_palindrom(121) == True
    assert numar_palindrom(13) == False
    assert numar_palindrom(313) == True
    assert numar_palindrom(1229) == False

def concatenare_elemente(nr1, nr2):
    '''
    functie care concateneaza doua elemente
    :param nr1: string
    :param nr2: string
    :return: elementul ce rezulta un urma concatenarii
    '''

    nr3 = str(nr1) + str(nr2)
    return int(nr3)


def test_concatenare_elemente():

    assert concatenare_elemente('12', '78') == 1278
    assert concatenare_elemente('10', '3') == 103






def main():
    lista1 = []
    lista2 = []
    test_contor_elem_pare()
    test_numar_palindrom()
    test_concatenare_elemente()
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
        elif optiune == '4':
            rezult_list = []
            for i in range(len(lista1)):
                for j in range(len(lista2)):
                    nr = concatenare_elemente(lista1[i], lista2[j])
                    if numar_palindrom(nr) is True:
                        rezult_list.append(nr)
            print(rezult_list)


        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')

main()








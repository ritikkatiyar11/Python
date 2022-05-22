def append():
    n = int(input("enter the no of elements\n "))

    for i in range(n):
        element = input("enter the element\n ")
        list.append(element)
    print(list)
    return choice()


def remove():
    element = input("enter the element to remove\n ")
    list.remove(element)
    print(list)
    return choice()


def insert():
    element = input("enter the element\n ")
    index = int(input("index please\n "))
    list.insert(index, element)
    print(list)
    return choice()


def choice():
    choice = int(input(
        "enter opertation to perform \n1-append\n2-insert\n3-Remove\n enter no :\n "))
    if choice == 1:
        append()

    if choice == 2:
        insert()
    if choice == 3:
        remove()


list = []
choice()

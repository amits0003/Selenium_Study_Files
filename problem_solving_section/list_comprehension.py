if __name__ == '__main__':
    x = int(input("Enter value of x \t "))
    y = int(input("Enter value of y \t "))
    z = int(input("Enter value of z \t "))
    n = int(input("Enter value of n \t "))
    lista = []
    [lista.append([idx1, idx2, idx3]) for idx1 in range(x + 1) for idx2 in range(y + 1) for idx3 in
                   range(z + 1) if (idx1 + idx2 + idx3) != n]
    print(lista)

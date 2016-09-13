def calc(a, b):
    soma = 0
    for i in range(0,len(a)):
        soma += a[i] * b[i]

    return soma

if __name__ == '__main__':
    assert calc([1], [1]) == 1
    assert calc([1], [2]) == 2
    assert calc([2], [2]) == 4

    assert calc([1, 1], [1, 1]) == 2
    assert calc([2, 2], [2, 2]) == 8
    assert calc([3, 3], [3, 3]) == 18

    assert calc([1, 1, 1], [1, 1, 1]) == 3
    assert calc([2, 2, 2], [2, 2, 2]) == 12
    assert calc([3, 3, 3], [3, 3, 3]) == 27
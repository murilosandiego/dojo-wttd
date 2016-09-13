"""
Você está resolvendo este problema. 
Este problema foi utilizado em 111 Dojo(s).
Definimos dois vetores A e B de dimensão n em termos de componentes como:
A = (a1, a2, a3, ..., an) e B = (b1, b2, b3, ..., bn)
O produto escalar entre esses vetores é descrito como:
A . B = a1 * b1 + a2 * b2 + a3 * b3 + ... + an * bn
Desenvolva um programa que, dado dois vetores de dimensão n, retorne o produto escalar entre eles.
"""



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
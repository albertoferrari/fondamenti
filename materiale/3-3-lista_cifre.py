'''
- Definire una funzione digits
    - Parametro: numero intero positivo
    - Risultato: lista di int
    - Cifre che compongono il numero, dalle unità in su
- Divedere il numero ripetutamente per 10
    - A ogni passaggio, la cifra è il resto della divisione
    - Non usare la rappresentazione come str!
    - Es. 6543 → [3, 4, 5, 6]
- Chiamare la funzione da main
    - Chiedere dei numeri all'utente, fino a riga vuota
    - Di volta in volta, mostrare la lista risultante
'''
def digits(n: int) ->list:
    ''' return lista delle cifre decimali di n
        dalla meno significativa
    '''
    l = []
    while n != 0:
        c = n % 10
        l.append(c)
        n = n // 10
    return l

def main():
    n = input('n: ')
    while n != '':
        print(digits(int(n)))
        n = input('n: ')    

if __name__ == '__main__':
    main()
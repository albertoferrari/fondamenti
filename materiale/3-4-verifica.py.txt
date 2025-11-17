'''
- Ottenere la lista di cifre di un numero dalla funzione digits (es. 3.3)
- Verificare la correttezza del risultato
    - Ciclo sulla lista con enumerate
    - Moltiplicare ogni cifra per la corrispondente potenza di 10
'''
from digits import digits

def verify(l: list) -> int:
    ''' calcola il valore del numero espresso dalla lista di cifre l
        visualizza anche la procedura di calcolo
    '''
    val = 0
    s = ''
    for e , v in enumerate(l):
        val += v * 10 ** e
        s += f'{v}*{10}**{e} + '
    print(s[:-3])    # non visualizza gli ultimi 3 caratteri ' + '
    return val

def main():
    n = 6543
    cifre = digits(n)
    print(f'{n} -> {cifre}')
    print(f'{cifre} -> {verify(cifre)}')

if __name__ == '__main__':
    main()

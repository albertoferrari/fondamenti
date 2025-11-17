'''
- Definire funzione per f(x) = x^3 - x - 1
- Definire funzione approx_zero
    - Parametro: un intervallo come tupla (a, b)
    - Risultato: un nuovo intervallo
- Si calcola punto mediano c = (a + b)/2
    - Risultato (a, c), se f(a) e f(c) hanno segno diverso
    - Risultato (c, b), se f(c) e f(b) hanno segno diverso
    - Altrimenti, generare ValueError con messaggio
- In funzione main, partire da intervallo (1, 2)
    - Poi, per 5 volte, chiamare approx_zero con l'intervallo ottenuto nel passaggio precedente 
    - esempio: (1, 1.5) → (1.25, 1.5) → (1.25, 1.37) → (1.31, 1.37) → (1.31, 1.34)
'''
def f(x:float) ->float:
    return x**3-x-1 

def aprox_zero(interv: tuple) -> tuple:
    a,b = interv
    c = (a+b)/2
    if f(a) * f(c) < 0:     #segno diverso
        return (a,c)
    elif f(b) * f(c) < 0:
        return (c,b)
    else:
        raise ValueError(f'non esiste 0 fra {a} e {b}')

def main():
    intervallo = aprox_zero((1,2))
    for _ in range(5):
        print(intervallo,end=' → ')
        intervallo = aprox_zero(intervallo)
    print(' ... ')
    
if __name__ == '__main__':
    main()
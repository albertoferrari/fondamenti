'''
- Creare una classe delle curve esponenziali
    - y = a*e**(b x) + c
    - Coefficienti a, b, c come campi, da inizializzare nel costruttore
- Metodo estimate
    - Parametro: x
    - Risultato: valore della funzione in x
- Nella funzione main
    - Istanziare un singolo modello esponenziale con coefficienti forniti dall'utente
    - Valutare il modello, chiamando estimate, in diversi punti x forniti iterativamente dall'utente
    - Terminare il ciclo quando l'utente fornisce una stringa vuota
'''
from math import e, exp

class Exponential():
    ''' curva esponenziale '''
    
    def __init__(self,x,y,z):
        self._a = x
        self._b = y
        self._c = z
        
    def estimate(self,x: float) ->float:
        ''' return valore della funzione in x '''
        y = self._a * exp(self._b * x) + self._c
        return y
        
def main():
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    e = Exponential(a,b,c)
    x = input('x: ')
    while x != '':
        x = float(x)
        print(e.estimate(x))
        x = input('x: ')
        
if __name__ == '__main__':
    main()
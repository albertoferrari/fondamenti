'''
- Definire una classe Circle
- Campi per centro e raggio
- Metodo area per calcolare l'area
- Metodo inside per controllare se un certo punto è nel cerchio
    - Parametro per il punto da controllare
    - Risultato booleano
- Nella funzione main
    - Istanziare un unico cerchio con dati forniti dall'utente
    - Eseguire il metodo per ottenere l'area e visualizzarla all'utente
    - Poi, per vari punti inseriti dall'utente, verificare se sono nel cerchio
    - Terminare all'inserimento di una riga vuota
'''
from math import pi

class Circle:
    ''' Cerchio con attributi centro e raggio '''
    
    def __init__(self,c: tuple,r: float):
        self._c = c
        self._r = r
        
    def area(self) -> float:
        return pi * self._r ** 2
    
    def inside(self, p: tuple) -> bool:
        cx , cy = self._c    #umpacking
        px , py = p
        distance = (cx-px)**2 + (cy-py)**2
        return distance <= self._r**2
    
def main():
    cx = float(input('ascissa  del centro: '))
    cy = float(input('ordinata del centro: '))
    r = float(input('raggio: '))
    c = Circle((cx,cy),r)
    a = c.area()
    print('area: ',a)
    px = float(input('ascissa  del punto: '))
    while px !='':
        px = float(px)
        py = float(input('ordinata del punto: '))
        if c.inside((px,py)):
            print(f'punto {(px,py)} interno al cerchio')
        else:
            print(f'punto {(px,py)} esterno al cerchio')
        px = input('ascissa  del punto: ')
        
if __name__ == '__main__':
    main()
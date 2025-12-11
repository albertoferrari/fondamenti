'''
Definire la classe Ball che rappresenta una pallina che si muove in un canvas di
dimensione 600x400.
La posizione iniziale, il movimento (dx,dy) e il colore sono passati come parametri
nel costruttore.
Raggiunti i limiti del canvas l'oggetto 'rimbalza'.
Nel main istanziare una lista di palline con posizione iniziale casuale,
movimento casuale di un pixel nelle 8 direzioni possibili e colore casuale.

Creare una animazione che visualizza il movimento delle palline visualizzando
per ognuna un cerchio di diametro 5 pixel del colore della pallina
'''
import g2d
import random
ARENA_W,ARENA_H = 600, 400  # dimensioni arena
RAGGIO= 5                   # raggio cerchio
N = 20                      # numero palline

class Ball:
    def __init__(self,x0:int,y0:int,dx:int,dy:int,col:tuple):
        self._x = x0                  # coordinate iniziali
        self._y = y0
        self._dx, self._dy = dx, dy   # spostamento
        self._col = col               # colore

    def move(self):
        # gestione limiti arena
        if not 0 <= self._x + self._dx <= ARENA_W - RAGGIO:
            self._dx = -self._dx    # comportamento per limiti orizzontali
        if not 0 <= self._y + self._dy <= ARENA_H - RAGGIO:
            self._dy = -self._dy    # comportamento per limiti verticali
        # spostamento
        self._x += self._dx
        self._y += self._dy

    def pos(self) -> (int, int):
        ''' posizione oggetto '''
        return self._x, self._y
    
    def getcolore(self) ->(int,int,int):
        return self._col

def tick():
    g2d.clear_canvas() # background
    for b in balls:
        g2d.set_color(b.getcolore())
        g2d.draw_circle(b.pos(),5)  # foreground
        b.move()

def random_color():
    ''' return tupla colore casuale '''
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return (r,g,b)

def random_direction():
    dir = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    return random.choice(dir)

def main():
    global balls
    balls = []                           # lista palline
    for _ in range(N):
        colore = random_color()          # colore casuale
        x = random.randrange(ARENA_W)    # posizione casuale
        y = random.randrange(ARENA_H)
        dx,dy = random_direction()       # direzione casuale
        b = Ball(x,y,dx,dy,colore)       # istanziazione oggetto
        balls.append(b)                  # inserimento in lista

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()

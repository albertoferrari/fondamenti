'''
Definire la classe Ball che rappresenta una pallina che si muove in un canvas di dimensione 600x400.
La posizione iniziale è passata come parametro nel costruttore
mentre il movimento è generato casualmente ed è solo in orizzontale o in verticale
e il colore è generato casualmente e piò essere solo rosso, verde o blu.
Raggiunti i limiti del canvas l'oggetto si blocca.
Nel main istanziare una lista di palline con posizione iniziale casuale.
Creare una animazione che visualizza il movimento delle palline visualizzando
per ognuna un cerchio di diametro 5 pixel del colore della pallina.
'''
import g2d
import random
ARENA_W,ARENA_H = 600, 400  # dimensioni arena
RAGGIO= 5                   # raggio cerchio
N = 20                      # numero palline

class Ball:
    def __init__(self,x0:int,y0):
        self._x = x0                  # coordinate iniziali
        self._y = y0
        self._random_direction()      # spostamento
        self._random_color()          # colore
        self._movement = True         # abilitato movimento

    def move(self):
        # gestione limiti arena
        if not self._movement:
            return
        if not 0 <= self._x + self._dx <= ARENA_W - RAGGIO:
            self._movement = False
        if not 0 <= self._y + self._dy <= ARENA_H - RAGGIO:
            self._movement = False
        if self._movement:
            self._x += self._dx
            self._y += self._dy

    def pos(self) -> (int, int):
        ''' posizione oggetto '''
        return self._x, self._y
    
    def getcolore(self) ->(int,int,int):
        return self._col
    
    def _random_color(self):
        ''' return tupla colore casuale '''
        color = [(255,0,0),(0,255,0),(0,0,255)]
        self._col = random.choice(color)
        
    def _random_direction(self):
        dir = [(0,-1),(0,1),(-1,0),(1,0)]
        self._dx, self._dy = random.choice(dir)

def tick():
    g2d.clear_canvas() # background
    for b in balls:
        g2d.set_color(b.getcolore())
        g2d.draw_circle(b.pos(),5)  # foreground
        b.move()

def main():
    global balls
    balls = []                           # lista palline
    for _ in range(N):
        x = random.randrange(ARENA_W)    # posizione casuale
        y = random.randrange(ARENA_H)
        b = Ball(x,y)                    # istanziazione oggetto
        balls.append(b)                  # inserimento in lista

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()

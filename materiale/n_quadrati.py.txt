'''
Esempio linearità
- input n
- disegnare n quadrati
- il primo grande come il canvas (500x500)
- l'ultimo di lato 10
- tutti centrati con il canvas
- tutti con colori casuali
'''
import g2d
from random import randrange

g2d.init_canvas((500,500))

'''
# primo quadrato
g2d.set_color((randrange(255),randrange(255),randrange(255)))
g2d.draw_rect((0,0),(500,500))

# ultimo quadrato
g2d.set_color((randrange(255),randrange(255),randrange(255)))
g2d.draw_rect((245,245),(10,10))
'''
# n quadrati
n = int(g2d.prompt('n: '))

for i in range(n):
    g2d.set_color((randrange(255),randrange(255),randrange(255)))
    
    pos = 245 / max(n-1,1) * i
    dim = -490 / max(n-1,1) * i + 500
    
    g2d.draw_rect((pos, pos), (dim,dim))

g2d.main_loop()

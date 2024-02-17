from PIL import Image
import random


image = Image.open(r'C:\Users\rouzaud\Pictures\blanc.png')

taille_x=500
taille_y=500

tab = [["r" for y in range(taille_y)] for x in range(taille_x)]
tab[1][1]=128

for x in range (2,taille_x-1):
  for y in range (1,taille_y-1):
    list=[]
    tot=0
    if tab [x-1][y]!="r":
      list.append(tab [x-1][y])
    if tab [x+1][y]!="r":
      list.append(tab [x+1][y])
    if tab [x][y-1]!="r":
      list.append(tab [x][y-1])
    if tab [x][y+1]!="r":
      list.append(tab [x-1][y+1])
    for n in range(0,len(list)):
      tot+=list[n]
    tab[x][y]=(tot/len(list))+random.randrange(-5,6)

    image.putpixel( (x, y), (int(tab[x][y]),int(tab[x][y]),int(tab[x][y]), 255) )
  print(x)
image.show()


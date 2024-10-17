"""
import random
nombre = random.randint(1, 20)

devine = int(input('a quel nombre je pense entre 1 et 20 ? '))

while nombre != devine:
  if devine > nombre:
    print('trop grand')
  else:
    print('trop petit')
  devine = int(input('autre chance ? '))
  

nombre = int(input('Entrz un nombre: '))

for x in range(1,10):
  print(str(nombre) + ' x ' + str(x) + ' = ' + str(nombre*x))
  """
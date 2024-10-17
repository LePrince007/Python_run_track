""""
# ************** Exercice 1 ***************

valeur1 = input("Entrez une valuer: ")
valeur2 = input("Entrez une valeur: ")

if valeur1 == valeur2:
    print("valeur1 est égal à valeur2")
else:
    print("Les deux valeurs ne sont pas egales")  

# ************** Exercice 2 ***************

age = int(input('how old are you ? '))

if age >= 18:
    print('you can vote')
else:
    print('too young')

# ************** Exercice 3 ***************

i = 0
for i in range(0,101):
    if i in [26, 37, 88]:
        continue
    print(i)


# ************** Exercice 4 ***************

i = 0
for i in range(0,101):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)
 
# ************** Exercice 6 ***************

Reponse = int(input('Entrez un nombre: '))
if Reponse % 2 == 0:
        print(f'Le nombre {Reponse} est pair')
else:
    print('Le nombre est impair')
"""
# ************** Exercice 7 ***************
nombre = 2  # On commence à 2 car 1 n'est pas un nombre premier
while nombre <= 1000:
    est_premier = True  # On suppose que le nombre est premier
    for i in range(2, int(nombre ** 0.5) + 1):  # On vérifie les diviseurs jusqu'à la racine carrée
        if nombre % i == 0:  # Si divisible par un autre nombre, il n'est pas premier
            est_premier = False
            break
    if est_premier:
        print(nombre)
    nombre += 1




  



  

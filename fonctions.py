"""
# *************EXERCICE 1************

def My_print_hello():
  print('Hello world')

My_print_hello()


# *************EXERCICE 2************

def My_print_name(name):
  print(name)

My_print_name("Alan")
My_print_name("Barry")
My_print_name("lamine")

# *************EXERCICE 3************

def Add(a,b):
  print(a + b)

Add(2,2)
Add(5,5)
Add(7,7)

# *************EXERCICE 4************

def GetHello():
  return print("Hello La Plateforme")

GetHello()

# *************EXERCICE 5************

def calcule(num1,operator,num2):
  return print(f"{num1} {operator} {num2}")

calcule(2, "*", 3)


# *************EXERCICE 6************

def number(nombre):
  if nombre > 0:
    print('Positif')
  elif nombre < 0:
    print('négatif')

number(5)
number(-5)
number(-17)
number(17)

# *************EXERCICE 7************

def Language(langage):
  if langage == "Javascript":
    print('tu es un dev web')
  elif langage == "Python":
    print('tu es un dev IA')
  elif langage == "Java":
    print('tu es un dev logiciel')
  elif langage == "reactjs":
    print('tu es un dev mobile')
  else:
    print('un jour inshallah!')

Language("Javascript")
Language("Python")
Language("Java")
Language("reactjs")
Language("Php")

# *************EXERCICE 8************

def Seasons(type,saison):
  if type == "fruits" and saison == "hiver":
    print('orange, mandarine et kiwi')
  elif type == "fruits" and saison == "été":
    print('Poire, fraise, cassis')
  elif  type == "légume" and saison == "hiver":
    print('carotte, topinambour, endive')
  elif type == "légume" and saison == "été":
    print('artichaut, aubergine,navet')
  else:
    print('On ne peut rien faire pour toi!')

Seasons("fruits","hiver")
Seasons("fruits","été")
Seasons("légume","hiver")
Seasons("légume","été")
Seasons("mangue","hiver")

# *************EXERCICE 9************

def moyenne(n1,n2,n3):

  moyenne_etudiant = (n1 + n2 +n3) / 3

  if moyenne_etudiant >= 15:
    print('Très bon élève')
  elif moyenne_etudiant >= 11:
    print('bon élève')
  elif moyenne_etudiant >= 8:
    print('Élève moyen')
  else:
    print('Élève devant faire des efforts')

moyenne(20,15,17)
moyenne(14,13,12)
moyenne(10,8,9)
moyenne(0,5,7)

# *************EXERCICE 10***********

def check(a):
  if a % 2 == 0:
    print('pair')
  else:
    print('impair')
  
check(7)
check(12)
check(5)
check(19)
"""

# *************EXERCICE 11***********





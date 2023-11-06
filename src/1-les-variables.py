import math

# 1 - Créer un nouveau projet sur PyCharm, et saisir le script suivant et l’enregistrer sous le nom tp1.py
def question1():
    a = 5
    print("a = ", a) 

    b = 5.50
    print("b = ", b) 

    c = 5,50,14
    print("c = ",c)

    texte = "Mon texte"
    print(texte)

    print("type de a: ",type(a))
    print("type de b: ",type(b))
    print("type de c: ",type(c))
    print("type de texte: ",type(texte))

# 2 a - Écrire un programme, qui définit 3 variables : une variable de type texte, une variable de type nombre entier, une variable de type nombre décimal et qui affiche leur type.
def question2a():
	text = "Hello"
	numInt = 13
	numDec = 0.369
	
	print("type de text: ",type(text))
	print("type de numInt: ",type(numInt))
	print("type de numDec: ",type(numDec))

# 2 b - Affecter dans une même ligne les 3 variables précédemment définies.
def question2b():
	text, numInt, numDec = "World", 369, 1036.7803

# Écrire un programme qui, à partir de la saisie d’un rayon et d’une hauteur, calcule le volume d’un cône droit
def question3():
	r = int(input("Enter un rayon: "))
	h = int(input("Enter une hauteur: "))

	v = 1/3 * math.pi * math.pow(r, 2) * h
	print(f"Le volume d'un cône qui a une hauteur de {h} et un rayon de {r} est {v}")
	
def main():
	print("1 - Créer un nouveau projet sur PyCharm, et saisir le script suivant et l’enregistrer sous le nom tp1.py")
	question1()
	print("------------------------------------------------------\n\n")
	
	print("2 a - Écrire un programme, qui définit 3 variables : une variable de type texte, une variable de type nombre entier, une variable de type nombre décimal et qui affiche leur type.")
	question2a()
	print("------------------------------------------------------\n\n")
	
	print("2 b - Affecter dans une même ligne les 3 variables précédemment définies.")
	question2b()
	print("------------------------------------------------------\n\n")
	
	print("Écrire un programme qui, à partir de la saisie d’un rayon et d’une hauteur, calcule le volume d’un cône droit")
	question3()
	print("------------------------------------------------------\n\n")
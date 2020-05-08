# -*- coding: utf-8 -*-
import turtle


###############################JEU######################################


def puissance4(liste_p4) :
	'''
	le jeu du morpion

	:param liste_p4: une liste de 6 listes de 7 éléments pour simuler un rectangle de 42 cases (comme au puissance 4)
	:type liste_p4: list
	'''
	#affichage
	print("Bienvenue au jeu du PUISSANCE 4 !!!!!!")
	print()
	r = 1
	print("========== " + "round n° " + str(r) + " ==========")
	print()
	grille()

	j1 = joueur1(liste_p4)
	j2 = joueur2(liste_p4)
	vide = est_vide(liste_p4)

	while True :
		r += 1
		print()
		print("========= " + "round n° " + str(r) + " ============")
		print()
		j1 = joueur1(liste_p4)
		if j1 :
			print()
			print("================================================")
			print("| Joueur 1 (rouge) a gagné en " + str(r) + " rounds !!!!!!  |")
			print("================================================")
			break
		vide = est_vide(liste_p4)
		if vide :
			print()
			print("==============================================")
			print("| Match nul, il y a eu " + str(r) + " rounds !!!!!!  |")
			print("==============================================")
			break
		j2 = joueur2(liste_p4)
		if j2 :
			print()
			print("================================================")
			print("| Joueur 2 (jaune) a gagné en " + str(r) + " rounds !!!!!!  |")
			print("================================================")
			break
		vide = est_vide(liste_p4)
		if vide :
			print()
			print("==============================================")
			print("| Match nul, il y a eu " + str(r) + " rounds !!!!!!  |")
			print("==============================================")
			break



###############################JEU_ET_DESSIN############################


def joueur1(liste_p4):
	'''
	round pour le joueur 1
	il prend une colone pour placer son jeton
	renvoie True s'il gagne, False sinon

	:param liste_p4: une liste de 6 listes de 7 éléments pour simuler un rectangle de 42 cases (comme au puissance 4)
	:type liste_p4: list
	:return: True ou False
	:rtype: bool
	'''
	j1_col = input("Joueur 1 (rouge) prend une colone (entre 1 et 7) : ")
	#assert made in tommy
	if not(j1_col in [str(i) for i in range(1,8)]) :
		while not(j1_col in [str(i) for i in range(1,8)]) :
			print("PRENDRE 1, 2, 3, 4, 5, 6 OU 7 !!!!!!")
			j1_col = input("Joueur 1 (rouge) prend une colone (entre 1 et 7) : ")
	j1_col = int(j1_col)

	print()

	#si emplacement occupé, le joueur resaisie un emplacement valide
	if liste_p4[0][j1_col -1] == 'R' or liste_p4[0][j1_col -1] == 'J':
		while liste_p4[0][j1_col -1] == 'R' or liste_p4[0][j1_col -1] == 'J':
			print("Emplacement occupé!!!!!!")
			#resaisie comme plus haut
			j1_col = input("Joueur 1 (rouge) prend une colone (entre 1 et 7) : ")
			#assert made in tommy
			if not(j1_col in [str(i) for i in range(1,8)]) :
				while not(j1_col in [str(i) for i in range(1,8)]) :
					print("PRENDRE 1, 2, 3, 4, 5, 6 OU 7 !!!!!!")
					j1_col = input("Joueur 1 (rouge) prend une colone (entre 1 et 7) : ")
			j1_col = int(j1_col)

	#placement des 'R' (s' il y a ' ' a la case du bas, elle prend la valeur 'R')
	if liste_p4[-1][j1_col -1] == ' ' :
		liste_p4[-1][j1_col -1] = 'R'
		#dessin
		turtle.penup()
		turtle.goto(-235,245)
		turtle.left(90)
		turtle.fd(480/7* j1_col - 480/7/2)
		turtle.right(90)
		turtle.fd(480 - 1*480/6/2)
		turtle.left(90)
		turtle.fd(1)
		turtle.pendown()
		turtle.pencolor('red')
		turtle.dot(60)
		turtle.right(90)

	#(s' il y a ' ' suivit d'une lettre, cet élément prend la valeur 'R')
	else :
		for ligne in range( len(liste_p4) -1 ) :
			if liste_p4[ligne][j1_col -1] == ' ' and ( liste_p4[ligne+1][j1_col -1] == 'J' or liste_p4[ligne+1][j1_col -1] == 'R' ) :
				liste_p4[ligne][j1_col -1] = 'R'
				#dessin
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* j1_col - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('red')
				turtle.dot(60)
				turtle.right(90)

	#vérifications :
	#une ligne de 'R'
	colone = 0
	ligne = 0
	for ligne in range(6): #6 lignes
		for colone in range(7-4+1) : #7 lignes / -4 car 4 jetons alignés /
			#+1 car inclusion (le dernier jeton est à la colone 7 donc liste_p4[ligne][6])
			if (liste_p4[ligne][colone] == liste_p4[ligne][colone+1] == liste_p4[ligne][colone+2] == liste_p4[ligne][colone+3] == 'R') :
				#trait vert qui indique les 4 jetons alignés
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* (colone+1) - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('green')
				turtle.width(7)
				turtle.fd(210)
				return True

	#une colone de 'R'
	colone = 0
	ligne = 0
	for colone in range(7): #7 colones
		for ligne in range(6-4+1): #6 lignes /  -4 car 4 jetons alignés /
			#+1 car inclusion (le dernier jeton est à la ligne 6 donc liste_p4[5][colone])
			if (liste_p4[ligne][colone] == liste_p4[ligne+1][colone] == liste_p4[ligne+2][colone] == liste_p4[ligne+3][colone] == 'R') :
				#trait vert qui indique les 4 jetons alignés
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* (colone+1) - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('green')
				turtle.right(90)
				turtle.width(7)
				turtle.fd(240)
				return True

	#une diagonale de 'R'
	#1er sens
	for ligne in range(3,6):
		for colone in range(4):
			if liste_p4[ligne][colone] == liste_p4[ligne-1][colone+1] == liste_p4[ligne-2][colone+2] == liste_p4[ligne-3][colone+3] == 'R' :
				#trait vert qui indique les 4 jetons alignés
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* (colone+1) - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('green')
				turtle.left(49)
				turtle.width(7)
				turtle.fd(315)
				return True
	#2nd sens
	for ligne in range(0,3):
		for colone in range(4):
			if liste_p4[ligne][colone] == liste_p4[ligne+1][colone+1] == liste_p4[ligne+2][colone+2] == liste_p4[ligne+3][colone+3] == 'R' :
				#trait vert qui indique les 4 jetons alignés
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* (colone+1) - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('green')
				turtle.right(49)
				turtle.width(7)
				turtle.fd(315)
				return True

	return False



###############################JEU_ET_DESSIN############################


def joueur2(liste_p4):
	'''
	round pour le joueur 2
	il prend une colone pour placer son jeton
	renvoie True s'il gagne, False sinon

	:param liste_p4: une liste de 6 listes de 7 éléments pour simuler un rectangle de 42 cases (comme au puissance 4)
	:type liste_p4: list
	:return: True ou False
	:rtype: bool
	'''
	j2_col = input("Joueur 2 (jaune) prend une colone (entre 1 et 7) : ")
	#assert made in tommy
	if not(j2_col in [str(i) for i in range(1,8)]) :
		while not(j2_col in [str(i) for i in range(1,8)]) :
			print("PRENDRE 1, 2, 3, 4, 5, 6 OU 7 !!!!!!")
			j2_col = input("Joueur 2 (jaune) prend une colone (entre 1 et 7) : ")
	j2_col = int(j2_col)

	print()

	#si emplacement occupé, le joueur resaisie un emplacement valide
	if liste_p4[0][j2_col -1] == 'R' or liste_p4[0][j2_col -1] == 'J':
		while liste_p4[0][j2_col -1] == 'R' or liste_p4[0][j2_col -1] == 'J':
			print("Emplacement occupé!!!!!!")
			#resaisie comme plus haut
			j2_col = input("Joueur 2 (jaune) prend une colone (entre 1 et 7) : ")
			#assert made in tommy
			if not(j2_col in [str(i) for i in range(1,8)]) :
				while not(j2_col in [str(i) for i in range(1,8)]) :
					print("PRENDRE 1, 2, 3, 4, 5, 6 OU 7 !!!!!!")
					j2_col = input("Joueur 2 (jaune) prend une colone (entre 1 et 7) : ")
			j2_col = int(j2_col)

	#placement des 'J' (s' il y a ' ' a la case du bas, elle prend la valeur 'J')
	if liste_p4[-1][j2_col -1] == ' ' :
		liste_p4[-1][j2_col -1] = 'J'
		#dessin
		turtle.penup()
		turtle.goto(-235,245)
		turtle.left(90)
		turtle.fd(480/7* j2_col - 480/7/2)
		turtle.right(90)
		turtle.fd(480 - 480/6/2)
		turtle.left(90)
		turtle.fd(1)
		turtle.pendown()
		turtle.pencolor('yellow')
		turtle.dot(60)
		turtle.right(90)

	#(s' il y a ' ' suivit d'une lettre, cet élément prend la valeur 'J')
	else :
		for ligne in range( len(liste_p4) -1 ) :
			if liste_p4[ligne][j2_col -1] == ' ' and ( liste_p4[ligne+1][j2_col -1] == 'J' or liste_p4[ligne+1][j2_col -1] == 'R' ) :
				liste_p4[ligne][j2_col -1] = 'J'
				#dessin
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* j2_col - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('yellow')
				turtle.dot(60)
				turtle.right(90)

	#vérifications :
	#une ligne de 'J'
	colone = 0
	ligne = 0
	for ligne in range(6): #6 lignes
		for colone in range(7-4+1) : #7 colones / -4 car 4 jetons alignés /
			#+1 car inclusion (le dernier jeton est à la colone 7 donc liste_p4[ligne][6])
			if (liste_p4[ligne][colone] == liste_p4[ligne][colone+1] == liste_p4[ligne][colone+2] == liste_p4[ligne][colone+3] == 'J') :
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* (colone+1) - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('green')
				turtle.width(7)
				turtle.fd(210)
				return True

	#une colone de 'J'
	colone = 0
	ligne = 0
	for colone in range(7): #7 colones
		for ligne in range(6-4+1): #6 lignes /  -4 car 4 jetons alignés /
			#+1 car inclusion (le dernier jeton est à la ligne 6 donc liste_p4[5][colone])
			if (liste_p4[ligne][colone] == liste_p4[ligne+1][colone] == liste_p4[ligne+2][colone] == liste_p4[ligne+3][colone] == 'J') :
				#trait vert qui indique les 4 jetons alignés
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* (colone+1) - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('green')
				turtle.right(90)
				turtle.width(7)
				turtle.fd(240)
				return True

	#une diagonale de 'J'
	#1er sens
	for ligne in range(3,6):
		for colone in range(4):
			if liste_p4[ligne][colone] == liste_p4[ligne-1][colone+1] == liste_p4[ligne-2][colone+2] == liste_p4[ligne-3][colone+3] == 'J' :
				#trait vert qui indique les 4 jetons alignés
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* (colone+1) - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('green')
				turtle.left(49)
				turtle.width(7)
				turtle.fd(315)
				return True
	#2nd sens
	for ligne in range(0,3):
		for colone in range(4):
			if liste_p4[ligne][colone] == liste_p4[ligne+1][colone+1] == liste_p4[ligne+2][colone+2] == liste_p4[ligne+3][colone+3] == 'J' :
				#trait vert qui indique les 4 jetons alignés
				turtle.penup()
				turtle.goto(-235,245)
				turtle.left(90)
				turtle.fd(480/7* (colone+1) - 480/7/2)
				turtle.right(90)
				turtle.fd( (ligne+1)*480/6 - 480/6/2)
				turtle.left(90)
				turtle.fd(1)
				turtle.pendown()
				turtle.pencolor('green')
				turtle.right(49)
				turtle.width(7)
				turtle.fd(315)
				return True

	return False



###############################JEU######################################


def est_vide(liste_p4) :
	'''
	renvoie False si il y a un enmplacement qui peut être joué
	(pas vide)
	renvoie True si toutes les cases ont été joué
	(vide)

	:param liste_p4: une liste de 6 listes de 7 éléments pour simuler un rectangle de 42 cases (comme au puissance 4)
	:type liste_p4: list
	:return: True ou False
	:rtype: bool
	'''
	l_bis = []
	for i in range( len(liste_p4) ):
		l_bis.append( ' ' in liste_p4[i] )
	return not(True in l_bis)



##############################DESSIN####################################


def grille():
	turtle.hideturtle()
	turtle.speed(0)

	#ligne
	turtle.penup()
	turtle.goto(-235,-235)
	turtle.pendown()
	for i in range(6):
		turtle.fd(480)
		turtle.fd(-480)
		turtle.left(90)
		turtle.fd(80)
		turtle.right(90)
	turtle.fd(480)

	#colones
	turtle.right(90)
	for i in range(7):
		turtle.fd(480) #80*6
		turtle.penup()
		turtle.fd(30)
		turtle.right(90)
		turtle.fd( (480/7) / 2 + 20)
		turtle.pendown()
		turtle.write('colone n° ' + str(7-i))
		turtle.penup()
		turtle.fd( (480/7) / 2 - 20)
		turtle.right(90)
		turtle.fd(480+30)
		turtle.left(180)
		turtle.pendown()
	turtle.fd(480)



########################################################################


puissance4([ [' ', ' ', ' ', ' ', ' ', ' ', ' '] for i in range(6)])
turtle.exitonclick()

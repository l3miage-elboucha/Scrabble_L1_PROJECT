
import random
cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
cases_bonus = {'MT':cases_MT, 'MD':cases_MD,'LT':cases_LT,'LD':cases_LD}
bonus = ['MT','MD','LT','LD']
bonus_array = []

def init_bonus():
  for i in range(15):
      row = ["  "]*15
      bonus_array.append(row)    
  for i in cases_bonus.keys():
      value = cases_bonus.get(i)
      l = len(value)
      for index in value:
          bonus_array[index[0]][index[1]] = i
  for i in range(15):
      print(bonus_array[i])


def init_jetons():
  for i in range(15):
      row = ["  "]*15
      bonus_array.append(row)    
  for i in range(15):
      print(bonus_array[i])




def affiche_jetons(j,x):
  for i in range(15):
      row = ["  "]*15
      bonus_array.append(row)
  if j in cases_MT:
            bonus_array[j[0]][j[1]] = x + '*'
  elif j in cases_MD:
            bonus_array[j[0]][j[1]] = x + '°'
  elif j in cases_LT:
            bonus_array[j[0]][j[1]] = x + '+'
  elif j in cases_LD:
            bonus_array[j[0]][j[1]] = x + '¤'
  else:
            bonus_array[j[0]][j[1]] = x + ' '
            


def plateau():
  print("Pendant le jeu, les bonus sont affichés par des symboles à côté des lettres posées; 'MT' = *, 'MD' = °, 'LT' = +, 'LD' = ¤ ")
  init_jetons()
  


def init_dico():
  dico = {"A":{"occ":9,"val":1},"B":{"occ":2,"val":3},"C":{"occ":2,"val":3},"D":{"occ":3,"val":2},"E":{"occ":15,"val":1},"F":{"occ":2,"val":4},"G":{"occ":2,"val":2},"H":{"occ":2,"val":4},"I":{"occ":15,"val":1},"J":{"occ":1,"val":8},"K":{"occ":1,"val":10},"L":{"occ":5,"val":1},"M":{"occ":3,"val":2},"N":{"occ":6,"val":1},"O":{"occ":6,"val":1},"P":{"occ":2,"val":3},"Q":{"occ":1,"val":8},"R":{"occ":6,"val":1},"S":{"occ":6,"val":1},"T":{"occ":6,"val":1},"U":{"occ":6,"val":1},"V":{"occ":2,"val":4},"W":{"occ":1,"val":10},"X":{"occ":1,"val":10},"Y":{"occ":1,"val":10},"Z":{"occ":1,"val":10},"#":{"occ":2,"val":0}}
  return dico

dic = init_dico()
def init_pioche(dico):
  dicov2 = []
  for key in dico.keys():
    value = dico[key]
    for i in range(value["occ"]):
      dicov2.append(key)
  return dicov2

sac = init_pioche(dic)
def piocher(x, sac):
   sac2 = []
   if len(sac) > x:
       for i in range(x):
           a = (random.choice(sac))
           b = sac.index(a)
           del sac[b]
           sac2.append(a)
   else:
      print("Number of jetons unavailable")
   return sac2


def complete_hand(hand,sac):
  l = len(hand)
  if l < 7:
    hand = hand + (piocher(7-l, sac))
  else:
    print("Hand Full")
  return hand

def exchange(jetons, hand, sac):
  for i in jetons:
        a = hand.index(i)
        del hand[a]
  hand = complete_hand(hand, sac)
  sac = sac + jetons
  return hand


def genere_dico(nf):
    with open(nf) as f:
         mots = [ligne.rstrip() for ligne in f]
    return mots


def mot_jouable(mot, ll):
  jouable = True
  c = 0
  d = 0
  for i in mot:
    a = mot.count(i)
    b = ll.count(i)
    c += a
    d += b
  if d + 1 == c and '#' in ll:
    jouable = True
  elif c == d:
      jouable = True
  elif c != d:
      jouable = False
  return jouable



def mots_jouables(motsfr, ll):
  new_list = []
  for k in motsfr:
    a = mot_jouable(k, ll)
    if a == True:
      new_list.append(k)
  return new_list


def lire_coords():
  i = int(input("Entre coordonnée horizontale : "))
  j = int(input("Entre coordonnée verticale : "))
  coords = True
  if bonus_array[i][j] == "  ":
    coords = True
  else:
    coords = False
  if coords == True:
    return i, j
##Fonction pour transformer mot en une liste ( on va l'utiliser dans la fonction tester_placement)
  
def codage4(mot):
    liste = [] 
    liste [:0] = mot
    return liste

def tester_placement(plateau,i,j,direction,mot):
  test = True
  vide = []
  if direction == 'horizontale':
    if bonus_array[i][j] == "  " and (len(codage4(mot)) < (15 - j) or len(codage4(mot)) == (15 - j)):
      test = True
    elif bonus_array[i][j] == codage4(mot)[0] + ' ' or bonus_array[i][j] == codage4(mot)[0] + '¤' or bonus_array[i][j] == codage4(mot)[0] + '+' or bonus_array[i][j] == codage4(mot)[0] + '°' or bonus_array[i][j] == codage4(mot)[0] + '*' and (len(codage4(mot)) < (15 - j) or len(codage4(mot)) == (15 - j)):
      for k in mot:
        indice = mot.index(k)
        if bonus_array[i][j] == bonus_array[i][j] == "  " or codage4(mot)[indice] + ' ' or bonus_array[i][j] == codage4(mot)[indice] + '¤' or bonus_array[i][j] == codage4(mot)[indice] + '+' or bonus_array[i][j] == codage4(mot)[indice] + '°' or bonus_array[i][j] == codage4(mot)[indice] + '*':
           test = True
        j += 1
    else:
      test = False
      
  if direction == 'verticale':
    if bonus_array[i][j] == "  " and (len(codage4(mot)) < (15 - i) or len(codage4(mot)) == (15 - j)):
      test = True
    elif bonus_array[i][j] == codage4(mot)[0] + ' ' or bonus_array[i][j] == codage4(mot)[0] + '¤' or bonus_array[i][j] == codage4(mot)[0] + '+' or bonus_array[i][j] == codage4(mot)[0] + '°' or bonus_array[i][j] == codage4(mot)[0] + '*' and (len(codage4(mot)) < (15 - j) or len(codage4(mot)) == (15 - j)):
      for k in mot:
        if bonus_array[i][j] == bonus_array[i][j] == "  " or codage4(mot)[indice] + ' ' or bonus_array[i][j] == codage4(mot)[indice] + '¤' or bonus_array[i][j] == codage4(mot)[indice] + '+' or bonus_array[i][j] == codage4(mot)[indice] + '°' or bonus_array[i][j] == codage4(mot)[indice] + '*':
           test = True
        i += 1
    else:
      test = False
  if test == True:
    return codage4(mot)
  if test == False:
    return vide

def placer_mot(plateau,lm,mot,i,j,direction):
  cd = codage4(mot)
  test1 = True
  if tester_placement(plateau, i, j, direction, mot) == cd:
    for k in cd:
        if k in lm:
          test1 = True
        elif k not in lm and tester_placement(plateau, i, j, direction, mot) == cd:
          test1 = True
        else:
          test1 = False
    if test1 == True:
      if direction == 'horizontale':
         for k in mot:
             affiche_jetons([i,j],k)
             if k in lm:
                s = lm.index(k)
                del lm[s]
             j += 1
         return lm
      elif direction == 'verticale':
        for k in mot:
            affiche_jetons([i,j], k)
            if k in lm:
               s = lm.index(k)
               del lm[s]
            i += 1
        return lm
    else:
       print("Erreur! Le mot ne peut pas être placé")
       return lm
  else:
    print("Erreur! Le mot ne peut pas être placé")
    return lm



# 4.1

def valeur_mot(mot, dico, i, j, direction):
	"""
	calcule et renvoie la valeur de ce mot en points
	"""

	valeur = 0
	bonus_lettres = 0
	nb_cases_mdb = 0
	nb_cases_mtp = 0

	for c in mot:
		val_lettre = dico[c]["val"]
		valeur += val_lettre
		if ([i,j] in cases_LD):
			bonus_lettres += val_lettre
			cases_LD.remove([i,j])
		elif ([i,j] in cases_LT):
			bonus_lettres += val_lettre*2
			cases_LT.remove([i,j])
		
		if ([i,j] in cases_MD):
			nb_cases_mdb += 1
			cases_MD.remove([i,j])
		elif ([i,j] in cases_MT):
			nb_cases_mtp += 1
			cases_MT.remove([i,j])
		
		if (direction == 'horizontal'):
			j += 1
		elif (direction == 'vertical'):
			i += 1
	
	
	valeur = max(valeur,valeur*nb_cases_mdb*2 + valeur*nb_cases_mtp*3) + bonus_lettres
	
	if (len(mot) == 7):
		valeur += 50
	
	return valeur

# 4.2

def meilleur_mot(motsfr, ll, i, j, dico, direction):
	"""
	calcule et renvoie le meilleur mot (de plus haute valeur telle que calcul´ee avec valeur mot),
	 parmi les mots autoris´es de la liste motsfr, jouable avec les lettres de la liste ll
	"""

	mmot = ''
	mmot_score = -1

	for m in motsfr:
		if (mot_valide(m, ll)):
			m_score = valeur_mot(m, dico, i, j ,direction)
			if (m_score > mmot_score):
				mmot = m
				mmot_score = m_score

	return mmot


def mot_valide(mot, ll):
	"""
	verifier si un mot est valide
	"""

	ll_temp = ll.copy()
	for c in mot:
		if (c in ll_temp):
			ll_temp.remove(c)
		else:
			return False
	
	return True



# 4.3

def meilleur_mots(motsfr, ll, dico):
	mots = list()
	motsfr_temp = motsfr.copy()
	mmot_score = -1

	while (motsfr_temp):
		mmot = meilleur_mot(motsfr_temp, ll, dico)
		score = valeur_mot(mmot, dico)
		if (score < mmot_score):
			break
		mmot_score = score
		mots.append(mmot)
		motsfr_temp.remove(mmot)
	
	return mots

# 6.

def tour_joueur(joueur_courant):
  """
  foction gère le tour d’un joueur : affichage du plateau, demande du coup (passer,
  échanger, placer)
  """
  print('\n')
  print('#'*60)
  print('# TOUR DE: #{}   SCORE: {}'.format(joueur_courant["nom"], joueur_courant["score"]))
  print('# MAIN: {}'.format(joueur_courant["main"]))
  print('#'*60)
  print('')
  plateau()
  tour = str(input("Que voulez vous faire? 'passer', 'échanger' ou 'placer' : "))
  if tour == 'échanger':
           nombre_de_jetons = int(input("Combien de jetons voulez vous échanger ? :  "))
           jetons = []
           i = 1
           while nombre_de_jetons != 0:
             print("Entrez jeton",i," :")
             a = input()
             jetons.append(a)
             i +=1
             nombre_de_jetons -= 1
           joueur_courant["main"] = exchange(jetons, joueur_courant["main"], sac)
  elif tour == 'passer':
          None
  elif tour == 'placer':
          mot_a_placer = str(input("Entrez le mot à placer :  "))
          if mot_a_placer in genere_dico('./Mot autorisés SCRABBLE.txt'):
             if mot_valide(mot_a_placer, joueur_courant["main"]) == True:
                  direction = str(input("Entrez la direction (horizontale - verticale) :  "))
                  i = int(input("Entrez coordonnée ligne (0->14):  "))
                  j = int(input("Entrez coordonnée colonne (0->14):  "))
                  if tester_placement(plateau(),i,j,direction,mot_a_placer) == codage4(mot_a_placer):
                     placer_mot(plateau(),joueur_courant["main"],mot_a_placer,i,j,direction)
                     joueur_courant["score"] += valeur_mot(mot_a_placer, dic, i, j, direction)
                     completer_main = piocher(len(mot_a_placer), sac)
                     joueur_courant["main"] += completer_main
                  else:
                    print('Mot ne peut pas être placé!')
                    tour_joueur(joueur_courant)
             else:
                 print('Mot invalide!')
                 tour_joueur(joueur_courant)
          else:
             print('Mot invalide!')
             tour_joueur(joueur_courant)
  return plateau()
            
            
            
             


def joueur_suiv(joueurs, joueur_courant):
	"""
	fonction calcule et renvoie le joueur suivant
	"""
	joueur_suiv_i = (joueurs.index(joueur_courant)+1)%len(joueurs)
	return joueurs[joueur_suiv_i]

def est_finie(sac, joueurs):
	if (len(sac) > 0):
		return False
	for joueur in joueurs:
		if (len(joueur["main"]) == 0):
			return True
	return False

############################### test #############################

# dict = {"A": {"occ" : 9, "val" : 1}, "B" : {"occ" : 2, "val" : 3}}

# test 4.1
# print(valeur_mot('BABABAB', dict))

# ll = ['A', 'B', 'A', 'B', 'B', 'A']
# motsfr = ['BABA', 'BIBA', 'BBB', 'BBAAA']

# test 4.2
# print(meilleur_mot(motsfr, ll, dict))

# test 4.3
# print(meilleur_mots(motsfr, ll, dict))

# -*- coding:utf-8 -*-

# o Comment gérer le fait que l'utilisateur raccroche le combiné n'importe quand?
# roadmap
# étape1:
#    composition de numéro seule, 
#    l'opératrice "parle" dans la console, 
#    l'utilisateur "parle" dans la console, 
#    le numéro est composé dans la console
#
# étape 2: l'opératrice parle vraiment (à partir de fichier enregistrés)
# étape 3: connexion au service google pour la reconnaissance vocale: l'utilisateur parle aussi
# étape 4: mise en place d'un répertoire fixe
# étape 5: mise en place du répertoire dynamique


#--------------------------------------------------------------------------------------------------
# "dit" le texte d'identifiant speechId
#
# TODO évolutif:
# A-=> se contente d'écrire l'id du texte
# B- utilise l'id pour retrouver le texte dans un fichier utilisable pour les traductions (ou variations)
# C- prononce le texte dont les mp3 sont pré-enregistrés
# D- Eventuellement utilise la synthèse vocale. 
#--------------------------------------------------------------------------------------------------
def say(speechId):
    print(speechId)
    
#--------------------------------------------------------------------------------------------------
# "dit" le texte speech. La différence avec say() est que repeate ne dit pas des phrases connues à
# l'avance. Il dit des éléments qui ont été transmis par l'utilisateur comme un numéro de téléphone 
# (quoi qu'on puisse enrigistrer les chiffres àl'avance) ou les noms des entrée du répertoire.
#
# TODO évolutif:
# A-=> se contente d'écrire le texte
# B- Utilise la syntèse vocale
# C- On pourra éventuellement se passer de la synthèse vocale pour les numéros de téléphone parce 
#    que le vocabulaire est limité.
# D- On pourr éventuellement se passer de la syntheése vocale pour le répertoire s'il est fixe. 
#--------------------------------------------------------------------------------------------------
def repeate(speech):
    print(speech)

#--------------------------------------------------------------------------------------------------
# "écoute" l'utilisateur 
#
# TODO évolutif:
# A-=> se contente de lire le texte en ligne de commande
# B- utilise le service en ligne de reconnaissance vocale de google
# C- Eventuellement gestion du multilingue...
# D- Eventuellement utilise la reconnaissance vocale locale (sans connexion internet). 
#--------------------------------------------------------------------------------------------------
def listen():
    return input()

#--------------------------------------------------------------------------------------------------
# "écoute" l'utilisateur jusqu'àce qu'on ai compris s'il a dit oui ou non. 
#--------------------------------------------------------------------------------------------------
def getBoolAnser():
    while True:
        ans = listen()
        if ans=="yes": return True
        if ans=="no": return False
        say("I didn't understand, please say yes or no")
    

#--------------------------------------------------------------------------------------------------
# demande un qui on veut contacter
# écoute la demande
# détermine si c'est un numéro quelconque ou une entrée du répertoire.
#
# TODO évolutif:
# A-=> le cas du répertoire n'est pas traité
# B- cas du répertoire
#--------------------------------------------------------------------------------------------------
def askRequest():
    say("who do you want to call?")
    request = listen()
    # TODO traitement pour déterminer si c'est un numéro ou une entrée du répertoire.
    return "number"

#--------------------------------------------------------------------------------------------------
# Valide que la chaine de caractére est un numéro de téléphone valide
# TODO évolutif:
# A-=> vérifie que ce sont des chiffres
# B- vérifie que c'est un numéro effectivement valide
#--------------------------------------------------------------------------------------------------
def isValidNumber(s):
    s.replace(" ","")
    return s.isdigit()

#--------------------------------------------------------------------------------------------------
# écoute et fait répéter le numéro à composer jusqu'à ce qu'il soit validé
# Remarque: On peut partir en boucle infinie si on a un utilisateur incompréhensible et coriace  
#--------------------------------------------------------------------------------------------------
def getNumber():
    while True :
        number = listen()
        say("I understood:")
        repeate(number)
        if not isValidNumber(number):
            say("this is not a valid number")
            say("please repeat the call number")
            continue
            
        say("is this number correct?")
        if (getBoolAnser()):
            return number
        
        say("sorry")
        say("please repeat the call number")

#--------------------------------------------------------------------------------------------------
# demande et renvoie le numéro àcomposer
#--------------------------------------------------------------------------------------------------
def askNumber():
    say("which_number?")
    return getNumber()

#--------------------------------------------------------------------------------------------------
# compose le numéro demandé
# TODO:
# pour le moment se contente de l'afficher à l'écran
# Que fait en cas d'échec de l'appel? Le programme aura-t-il encore la main?
#--------------------------------------------------------------------------------------------------
def composeNumber(number):
    say("ok, let's go!")
    print("COMPOSOTION:" + number)


#--------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    say("presentation")
    request = askRequest()
    if request=="number":
        number = askNumber()
        composeNumber(number)
        
        
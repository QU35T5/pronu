#Skapa ett lämpligt användarsnitt för spelen Sten, Sax, Påse. Spelaren
# spelar mot datorn vars val genereras slumpmässigt.
import random
def spel():
    # Ber användaren om input
    anvandare = input("Vad vill du börja med? skriv 'sten', 'sax' eller 'påse':\n" )
    # Gör allt till gemener
    anvandare =anvandare.lower()
    # variabel datorn sätts till en random val av sten,sax eller påse.
    dator = random.choice(['sten','sax','påse'])
    # Kollar först om ex sax=sax
    if anvandare == dator:
        return f'Det är jämt. båda valde {dator}'
    
    if vinnare(anvandare,dator):
        return f'Du har valt {anvandare} och datorn valde {dator}. Du vann!.'
    # antar att de fall som är kvar är dem där anvandaren förlorade., dvs inte jämt, inte vin
    return f'Du har valt {anvandare} och datorn valde {dator}. Du förlorade.'

# Funktion som kollar vem som är vinnare, vi har alla fallen nerskrivna
# Om sant returnera true och if satsen ovan körs. 
def vinnare(spelare,motstandare):
    # Returnerar sant om Spelaren vinner mot motsandaren.
    if (spelare=='sten' and motstandare=='sax') or (spelare=='sax'and motstandare=='påse') or (spelare=='påse' and motstandare=='sten'):
        return True
    # annars false, spelaren har inte vunnit mot motståndaren,
    return False

print(spel())
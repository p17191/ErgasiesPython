import random #Για να γεμίσω τήν λίστα με τυχαιους αριθμους


def Triplets(lista, n):
 #Βρισκουμε τα τριδυμα
    found = True
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (lista[i] + lista[j] + lista[k] == 0):
                    print(lista[i], lista[j], lista[k])
                    found = True
     
             
    
    #Αν δεν υπαρχει συνδυασμος τοτε εμφανιζουμε αναλογο μυνημα
    if (found == False):
        print("Δεν υπάρχει τέτοιος συνδυασμός.")
 
#Γινεται γεμισμα της λιστας απο τυχαιους αριθμους ευρους -30 μεχρι 30 , max 30 κελια
lista = random.sample(xrange(-30,30), 30)
print ("Ιδού η λίστα: ")
print ("\n")
print lista
#Παιρνουμε το πληθος των κελιων της λιστας
n = len(lista)
print ("\n")
print ("\n")
print ("Ιδού οι συνδυασμοί: ")
print ("\n")
Triplets(lista, n)
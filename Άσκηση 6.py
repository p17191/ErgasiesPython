from __future__ import print_function # Για τις όμορφες ιδιότητες της python 3!
from datetime import datetime
import datetime as dt # Για να μην μπλέξουν οι βιβλιοθήκες!

#Τίτλοι ημερών
week = ['Su ', 'Mo ', 'Tu ', 'We ', 'Th ', 'Fr ', 'Sa ']

# Οι μήνες και το εύρος ημερών τους
# + 1 για αποφυγή μπερδέματος με το max των ημερών
calender = [('January', range(1, 31 + 1)),
            ('Feburary', range(1, 28 + 1)),
            ('March', range(1, 31 + 1)),
            ('April', range(1, 30 + 1)),
            ('May', range(1, 31 + 1)),
            ('June', range(1, 30 + 1)),
            ('July', range(1, 31 + 1)),
            ('August', range(1, 31 + 1)),
            ('September', range(1, 30 + 1)),
            ('October', range(1, 31 + 1)),
            ('November', range(1, 30 + 1)),
            ('December', range(1, 31 + 1))]
			
#Ελεγχος εγκυροτητας μηνα
while True:
	try:
		month = int(raw_input("Δώσε τον μήνα που επιθυμείς σε αριθμητική μορφή (1-12): "))
		if month <= 0 or month > 12:
			print ("\n")
			print ("Μη έγκυρος μήνας!")
			print ("\n")
			continue
		else:
			break
	except Exception:
		print ("\n")
		print ("Μη έγκυρος μήνας!")
		print ("\n")
		
print ("\n")

while True:
	try:
		yeard = int(raw_input("Δώσε τον χρόνο που επιθυμείς σε αριθμητική μορφή: "))
		if yeard <=0 or yeard >= 10000:
			print ("\n")
			print ("Ο χρόνος πρέπει να είναι έγκυρος και σε αριθμητική μορφή.")
			print ("\n")
			continue
		else:
			break
	except Exception:
		print ("\n")
		print ("Ο χρόνος πρέπει να είναι έγκυρος και σε αριθμητική μορφή.")
		print ("\n")

print ("\n")
# Για να εμφανιστεί έπειτα ως τίτλος
if month ==1:
	month2 = "January"
if month ==2:
	month2 = "Feburary"
if month ==3:
	month2 = "March"
if month ==4:
	month2 = "April"
if month ==5:
	month2 = "May"
if month ==6:
	month2 = "June"
if month ==7:
	month2 = "July"
if month ==8:
	month2 = "August"
if month ==9:
	month2 = "September"
if month ==10:
	month2 = "October"
if month ==11:
	month2 = "November"
if month ==12:
	month2 = "December"
	
#Πότε αρχίζει ο μήνας 
start = datetime(yeard, month,1).isoweekday() 
if start == 7:
	startw = week[0]
if start == 1:
	startw = week[1]
if start == 2:
	startw = week[2]
if start == 3:
	startw = week[3]
if start == 4:
	startw = week[4]
if start == 5:
	startw = week[5]
if start == 6:
	startw = week[6]

#Πότε τελειώνει ο μήνας 
def last_day_of_month(date):
    next_month = date.replace(day=28) + dt.timedelta(days=4)  
    return next_month - dt.timedelta(days=next_month.day)
	
endd = last_day_of_month(dt.date(yeard, month, 1))
# Παίρνω την ημέρα μόνο
endd = endd.day

#Εμφάνιση ημερολογίου
def calendar(year, start_day,month2):
    # Ανάλογα με την μέρα έναρξης του μήνα ,αρχικοποιώ το starting position στο calendar
		start_pos = week.index(start_day)
	
    # αν είναι True, αλλάζω τον Φεβρουάριο σε 29 days
		if leap(year):
			calender[1] = ('Feburary', range(1, 29 + 1))

        # Print τον τίτλο του μήνα
		print('{0} {1}'.format(month2, year).center(20, ' '))
        # Print τούς τίτλους των ημερών
		print(''.join(['{0:<3}'.format(w) for w in week]))
        # Βάζω κενά αν η ημέρα δεν αρχίζει από Sunday
		print('{0:<3}'.format('')*start_pos,end='')
		
		for day in range(1,endd+1):
            # Print την ανάλογη ημέρα
				print('{0:>2} '.format(day),end='')
				start_pos += 1
				if start_pos == 7:
                # Αν start_pos == 7 (Saturday) αλλάζω γραμμή
					print()
					start_pos = 0 # Reset μετρητή
		print('\n')

def leap(year):
    #Check αν year ειναι  leap year (δίσεκτος)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Καλώ την συνάρτηση και εμφανίζω το ημερολόγιο.
calendar(yeard,startw,month2)
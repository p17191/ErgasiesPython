import urllib2 # Για την πιο εύκολη σύνδεση με URL
import json # Για την αποθήκευση-ανταλλαγή δεδομένων
import datetime

#αρχικοποιω μεταβλητες
cur_date=datetime.datetime.now()
maxsucc = -1
maxdate = " "
countermax = 0	
#ελεγχος εγκυροτητας
while True:
	try:
		n1 = int(raw_input("Δώσε τον πρώτο αριθμό: "))
		if n1 < 1 or n1 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:	
		n2 = int(raw_input("Δώσε τον δεύτερο αριθμό: "))
		if n2 < 1 or n2 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:	
		n3 = int(raw_input("Δώσε τον τρίτο αριθμό: "))
		if n3 < 1 or n3 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:	
		n4 = int(raw_input("Δώσε τον τέταρτο αριθμό: "))
		if n4 < 1 or n4 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:
		n5 = int(raw_input("Δώσε τον πέμπτο αριθμό: "))
		if n5 < 1 or n5 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:
		n6 = int(raw_input("Δώσε τον έκτο αριθμό: "))
		if n6 < 1 or n6 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:
		n7 = int(raw_input("Δώσε τον έβδομο αριθμό: "))
		if n7 < 1 or n7 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:
		n8 = int(raw_input("Δώσε τον όγδοο αριθμό: "))
		if n8 < 1 or n8 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:
		n9 = int(raw_input("Δώσε τον ένατο αριθμό: "))
		if n9 < 1 or n9 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
while True:
	try:
		n10 = int(raw_input("Δώσε τον δέκατο αριθμό: "))
		if n10 < 1 or n10 > 80:
			print ("\n")
			print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
			continue
		break
	except Exception:
		print ("\n")
		print("Παρακαλώ δώσε έναν αριθμό από το 1 έως 80.")
		
print ("\n")
mynums=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
#Για καθε μερα του μηνα τραβαω ημερομηνια και αποτελεσματα κληρωσεων
for i in range(31):
	cur_date= cur_date - datetime.timedelta(days=1)
	date_str= cur_date.strftime("%d-%m-%Y")
	url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data=json.loads(data)
	klhrwseis= data['draws']['draw']
	#βρισκω την ημερομηνία με τις περισσότερες επιτυχίες
	countermax = 0
	for k in klhrwseis:
		tmp=k["results"]
		match = set(mynums) & set(tmp)
		if len(match) > 4:
			countermax+=1
		if countermax > maxsucc:
			maxsucc = countermax
			maxdate = date_str
if maxsucc == 0:
	print "Δεν θα είχες καμία επιτυχία με αυτούς τους αριθμούς. :( "
else:
	print "Η ημερομηνία που θα είχες τις περισσότερες επιτυχίες είναι η: %s" %maxdate

# Στην εκφωνηση της ασκησης λεει να εμφανιστει η ημερα του μηνα , αλλα επειδη λειτουργω με 31 μερες και οχι ανα μηνα, υπαρχει 
# η περιπτωση να μπλεξει για παραδειγμα η ημερομηνια 1/2/2018 με την 1/3/2018 καθως με 31 μερες απο την 1/2/2018 φτανει στην
# 3/3/2018 και υπαρχουν δυο μερες με τον αριθμο 1. Γι'αυτο τον λογο εμφανιζω ολοκληρη την ημερομηνία και οχι μονο την μερα,
# διαφορετικα θα πρεπει να βαλουμε καταληλο format στην maxdate αφου την κανουμε parse σε μορφη date ή datetime
# και επειτα να παρουμε την μερα μονο με maxdate.day.
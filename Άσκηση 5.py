import tweepy # Για τα κλειδια
import json # Για την αποθήκευση-ανταλλαγή δεδομένων
import re # Για να ομορφίνουμε τα δεδομένα και να αφαιρέσουμε ο,τι δεν θέλουμε (regular expression)
import collections # Χρήσιμα για databases - αποθήκευση δεδομένων
from tweepy import OAuthHandler # Για register με τα κλειδια
 
# Παιρνω κλειδια για ταυτοποιηση απο twitter
consumer_key = 'tM5kw6PxV6QFQBC9HZ2npSNks'
consumer_secret = '3fSt1Vc5HWvjJ0HBXMaDR4HSeInmdmbPRuNbJNhppL2gmmlsXk'
access_token = '2758633369-ZJLmPrEEWQp1GisvheyVefJekVeF0weSXpgaeJQ'
access_secret = 'gCDhGmyk93k3hc7yTzJIPhKB5UsyDQlRGSeWJSNCkpLdd'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
#ελεγχος εγκυροτητας screen name
while True:
	try:
		screename = (raw_input("Γράψε το screen name του προφιλ του χρήστη που επιθυμείς: "))
		#Παιρνω 10 τελευταια tweets
		keimeno = " "
		for status in tweepy.Cursor(api.user_timeline, screen_name=screename).items(10):
			keimeno = keimeno+" "+ status._json['text']
		break
	except Exception:
		print ("\n")
		print("Το screen name που έγραψες δεν είναι έγκυρο.")
#Αφαιρω αριθμους
keimeno = ''.join([i for i in keimeno if not i.isdigit()])
#Αφαιρω συμβολα και κραταω μονο λεξεις
keimeno = ' '.join(re.sub("(#[A-Za-z0-9]+)|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",keimeno).split())
#ξεχωριζω τις λεξεις με αυτακια 
lista = keimeno.split (' ')
#αφαιρω το u απο unicode για αισθητικους λογους
lista = [ x.encode('ascii', errors='replace') for x in lista ]
#απαριθμω ποσες φορες εμφανιστηκε η καθε λεξη
counter = collections.Counter(lista)
#βρισκω ποια λεξη εμφανιστηκε τις περισσοτερες φορες
popular = str((counter.most_common(1)))
#κραταω μονο γραμματα (λεξη)
popular = re.sub('[^a-zA-Z]+', '', popular)

print ("Η δημοφιλέστερη λέξη είναι η: "+popular+".")
import json
import random

nonpcwords = ['gay', 'dyke', 'homo', 'fag', 'faggot', 'perv',  'paedo' , 'crone', 'wrinkly', 'hag', 'pussy', 'slag', 'whore', 'slut', 'fulgy', 'cow', 'dog', 'ghetto', 'heffer', 'fatso', 'whale', 'lame', 'dumb', 'autistic', 'cripple', 'derp', 'gimp', 'midget', 'retard', 'retarded', 'spastic', 'spaz']

with open('data.json', 'r') as f:
	altinsult = json.loads(f.read())

print """
Hey! We're the PCPCs... or the Politically Correct Police Constables. 
We're here to make sure that when you want to offend someone, you don't end up offending eevveryone!
"""
insult = raw_input("So, here goes, give us an insult! >>").lower()

print """
Right so, '%s'..?
I don't want to know who you're going to say that to!
One moment whilst we check whether we can give you the go-ahead...
""" % insult

words = insult.split()

if any(x in words for x in nonpcwords):
	print """
	Uh-oh! You're not being very pc there...
	How about you try something else?

	Oh, here's a good one!
	"""
	new = random.choice(altinsult)
	quote = new['quote']
	author = new['author']

	print """
	"{}"
	-{}

	How's about that?! Nice and PC :)
	""".format(quote, author)
else: 
	print """
	Perfect! Go ahead and say it - 
	But, don't blame us if you get hurt..!
	"""



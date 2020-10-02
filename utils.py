import string
from math import sqrt

def lines_from_file(path):
	"""Vraća listu stringova/riječi, po svaki string/riječ iz jednog retka iz
	fajla nakon poziva ove funkcije."""
	
	with open(path, 'r') as f:
		return [line.strip() for line in f.readlines()]

punctuation_remover = str.maketrans('', '', string.punctuation)

def remove_punctuation(s):
	"""Vraća string bez punktacija (tačke, zarezi id..).
	
	>>> remove_punctuation("It's a lovely day, don't you think?")
	'Its a lovely day dont you think'
	"""
	
	return s.strip().translate(punctuation_remover)

def lower(s):
	"""Vraća string sa svim slovima u umanjenom obliku"""
	
	return s.lower()

def split(s):
	"""
	Svaku riječ stringa dijeli i kao zaseban element stavlja u listu.
	
	>>> split("It's a lovely day, don't you think?")
	["It's", 'a', 'lovely', 'day,', "don't", 'you', 'think?']
	"""
	
	return s.split()

"""Funkcije za manipuliranje brojevima i operacijama. (Koristi se za funkciju
WPM iz fajla cats.py."""
def rational(x, y):
	return [x, y]
	
def div_rational(x, y):
	n = rational(num(x) * den(y), den(x) * num(y))
	return num(n) / den(n)

num = lambda r: r[0]
den = lambda r: r[1]


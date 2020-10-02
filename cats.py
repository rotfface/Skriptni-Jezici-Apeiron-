"""Implementacija pisanja i brzine - Glavni fajl"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime

#1. Dio
def choose(paragraphs, select, k):
	"""Ova funkcija selektuje koji paragraf će korisnik zapravo unositi.
	Uzima lisu paragrafa(stringova), select funkciju koja vraća True za
	paragrafe koji se mogu selektovati, i pozitivni indeks k. Choose
	funkcija vraća k-ti paragraf za koji selekt funkcija vrati True. Ako
	takav paragraf ne postoji jer je k prevelik, onda choose vraća prazan
	string.
	"""
	
	s = [p for p in paragraphs if select(p)]
	return s[k] if len(s) > k else ''


def about(topic):
	"""Ova funkcija uzima riječ prema kojoj će se odabrati paragrafi
	za pisanje. Ona vraća funkciju koja se može proslijediti funkciji choose
	kao select argument. Vraćena funkcija uzima paragraf i vraća boolean
	vrijednost koja pokazuje da li dati paragraf sadrži ijednu riječ iz
	topic-a.

	>>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
	>>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
	'Cute Dog!'
	>>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
	'Nice pup.'
	"""
	
	assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
	def helper(paragraph):
		contain = False
		for s in topic:
			if s in lower(paragraph):
				contain = True
		return contain
	return helper
	
def accuracy(typed, reference):
	"""
	Ova funkcija uzima typed paragraf i reference paragraf. Ona vraća
	postotak riječi iz typed koji odgovaraju riječima iz reference.
	Punktacija te velika i mala slova također moraju da odgovaraju.
	Riječ/String u ovom slučaju je bilo koja sekvenca karaktera koja je
	odvojena spaceom.
	Ako unesena riječ nema odgovarajuće riječi iz reference zato što je
	typed rečenica veća od reference rečenice, onda sve dodatne riječi iz
	typed su netočne. Ako je typed prazan onda je podudaranost 0%.


	>>> accuracy('Cute Dog!', 'Cute Dog.')
	50.0
	>>> accuracy('A Cute Dog!', 'Cute Dog.')
	0.0
	>>> accuracy('cute Dog.', 'Cute Dog.')
	50.0
	>>> accuracy('Cute Dog. I say!', 'Cute Dog.')
	50.0
	>>> accuracy('Cute', 'Cute Dog.')
	100.0
	>>> accuracy('', 'Cute Dog.')
	0.0
	"""
	
	typed_words, reference_words = split(typed), split(reference)
	same_words, gornja_granica = 0, 0
	if len(typed_words) > len(reference_words):
		gornja_granica = len(typed_words) - (len(typed_words) - len(reference_words))
	else:
		gornja_granica = len(typed_words)
	for i in range(0, gornja_granica):
		if typed_words[i] == reference_words[i]:
			same_words += 1
	return (same_words / len(typed_words)) * 100 if typed else 0.0

def wpm(typed, elapsed):
	"""Ova funkcija računa words per minute, to je zapravo mjera za
	brzinu pisanja koja uz dati string typed i vrijeme koje je bilo potrebno
	za kucanje tog stringa elapsed računa WPM. WPM se zapravo ne bazira na
	broju ukucanih riječi u minuti nego na broj ukucanih karaktera/slova,
	tako da typing test ne određuje dužina pojedinačnih riječi. Formula za
	WPM je odnos broja svih karaktera / 5 i proteklog vremena elapsed.
	"""
	
	assert elapsed > 0, 'Elapsed time must be positive'
	wpm_typed, time = rational(len(typed), 5), rational(elapsed, 60)
	return div_rational(wpm_typed, time)

def autocorrect(user_word, valid_words, diff_function, limit):
	"""Ova funkcija uzima user_Word i listu svih validnih riječi te diff
	funkciju. Ako se user_word nalazi u listi valid_words, autocorrect će
	vratiti tu riječ. U drugom slučaju autocorrect će vratiti riječ iz
	valid_words koja ima najmanju razliku u odnosu na user_word bazirano na
	funkciji diff_function. Ako je najmanja razlika između user_word i bilo
	kojih od valid_words veća od limit-a, onda se vraća user_word a ne valid_word. 
	Diff funkcija uzima tri argumenta, gdje dva od ta tri su
	stringovi za usporedbu(user_word i riječ iz valid_words) kao i limit.
	Vraćena vrijednost ove funkcije je broj koji označava broj različitih
	karaktera da dva stringa. Sve riječi moraju biti implementirane i
	pretvorene u mala slova radi lakše usporedbe i korištenja. Ako više
	stringova ima istu najmanju razliku prema diff_funkciji, autocorrect
	vraća string koji se prvi pojavi u valid_words.
	"""
	
	if user_word in valid_words:
		return user_word
	else:
		for w in valid_words:
			if not diff_function(user_word, w, limit):
				return w
		small_list = [valid_words[i] for i in range(0, len(valid_words)) if (diff_function(user_word, valid_words[i], limit) < limit)]
		return min(small_list) if small_list else user_word

def sphinx_swap(start, goal, limit):
	"""Ova funkcija je zapravo ta prava diff_funkcija koja uzima dva
	stringa. Ona vraća minimalni broj karaktera koji se moraju promijeniti
	da bi string start odgovarao stringu goal. Ako stringovi nisu jednake
	dužine razlika dužine se dodaje u total. Ako je broj karaktera koji se
	moraju promijeniti u stringu start veći od limit-a onda ova funkcija
	sphinx_swap treba vratiti bilo koji broj veći od limit-a i treba
	smanjiti nivo komputacije koji je potreban za pretvaranje u goal na
	minimum.
	"""
	
	if not start:
		return len(goal)
	elif not goal:
		return 0
	elif start[0] != goal[0]:
		return sphinx_swap(start[1:], goal[1:], limit) + 1
	else:
		return sphinx_swap(start[1:], goal[1:], limit)

def feline_fixes(start, goal, limit):
	"""Ova funkcija je druga diff_funkcija koja vraća broj minimalnih
	potrebnih promjena da bi se start transformirao u goal. Dakle ovdje
	postoje tri vrste opreacija u rekurzivnim pozivima a to su: Dodaj riječ
	na start, ukloni riječ sa starta i zamijeni riječ iz starta sa drugom
	riječi. Da bi start odgovarao goal-u. Svaki edit dodaje 1. Pravilo za
	slučaj da je broj edita veći od limita važi isto kao i za prethodnu
	funkciju. Sphinx_swap.
	"""
	
	if limit < 0 or len(start) == 0 or len(goal) == 0:
		return abs(len(start) - len(goal))
	elif start[0] == goal[0]:
		return feline_fixes(start[1:], goal[1:], limit)
	else:
		add_diff = 1 + feline_fixes(start, goal[1:], limit - 1)
		remove_diff = 1 + feline_fixes(start[1:] , goal, limit - 1)
		substitute_diff = 1 + feline_fixes(start[1:], goal[1:], limit - 1)
		return min(add_diff, remove_diff, substitute_diff)
		
def wrong_words(original, typed):
	"""Uzima original dati paragraf/string i poredi sa unesenim te
	vraća netačne riječi u tačnom obliku.
	"""
	
	if not original:
		return [[]]
	elif not typed:
		return [list(original)]
	elif original[0] != typed[0]:
		return wrong_words(original[1:], typed[1:]) + [[original[0], typed[0]]]
	else:
		return wrong_words(original[1:], typed[1:])

def run_typing_test(topics):
	"""Test funkcija koja sve ovo gore povezuje i u CMD-u radi sličnu
	stvari kao i u GUI-u stim da ovdje fali opcija za vidljivi autocorrect
	krivo upisanih riječi koji te krive riječi automatski pretvara u točne.
	Ovdje se mjeri vrijeme kucanja, postotak točnosti te daje lista krivo
	upisanih riječi i njihove odgovarajuće točne riječi ukoliko ih je moguće
	pronaći.
	"""
	
	paragraphs = lines_from_file('data/sample_paragraphs.txt')
	select = lambda p: True
	if topics:
		select = about(topics)
	i = 0
	while True:
		reference = choose(paragraphs, select, i)
		if not reference:
			print('No more paragraphs about', topics, 'are available.')
			return
		print('Type the following paragraph and then press enter/return.')
		print('If you only type part of it, you will be scored only on that part.\n')
		print(reference)
		print()

		start = datetime.now()
		typed = input()
		if not typed:
			print('Goodbye.')
			return
		print()

		elapsed = (datetime.now() - start).total_seconds()
		print("Nice work!")
		print('Words per minute:', wpm(typed, elapsed))
		print('Accuracy: ', accuracy(typed, reference))
		print('Wrong words: ')
		for x, y in wrong_words(split(reference), split(typed))[1:]:
			print(str(y) + ' -> ' + str(x))
			print('Missing words: ', wrong_words(split(reference), split(typed))[0])
			print('\nPress enter/return for the next paragraph or type q to quit.')
			if input().strip() == 'q':
				return
			i += 1

@main #dekorator
def run(*args):
	"""Ova funkcija služi za čitanje CLI argumenata i na osnovu njih
	određuje koju odgovarajuću funkciju da pozove.
	"""
	
	import argparse
	parser = argparse.ArgumentParser(description="Typing Test")
	parser.add_argument('topic', help="Topic word", nargs='*')
	parser.add_argument('-t', help="Run typing test", action='store_true')

	args = parser.parse_args()
	if args.t:
		run_typing_test(args.topic)




from cs50 import get_string

s = get_string("Unesite tekst: ").strip()
broj_riječi, broj_slova, broj_rečenica = 0, 0, 0

for i in range(len(s)):
    if (i == 0 and s[i] != ' ') or (i != len(s) - 1 and s[i] == ' ' and s[i + 1] != ' '):
        broj_riječi += 1
    if s[i].isalpha():
        broj_slova += 1
    if s[i] == '.' or s[i] == '?' or s[i] == '!':
        broj_rečenica += 1

L = broj_slova / broj_riječi * 100
S = broj_rečenica / broj_riječi * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

print(broj_slova, broj_riječi, broj_rečenica, index)

if index < 1:
    print('Prije ocjene 1')
elif index >= 16:
    print('Ocjena 16+')
else:
    print(f"Ocjena {index}")
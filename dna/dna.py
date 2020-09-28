from sys import argv, exit
import csv

# Uvom mini projektu zadatak je pronaći broj ponavljanja nekog substringa u datom stringu. Upute u -> README.md

def get_max_num_of_times_substring(s, sub):
    # vraća maksimalni broj ponavljanja substringa sub iz stringa s.

    # Primjer
    # s   = [ATATATTATAT]
    # ans = [30201002010] # počevši od određenog i-tog indexa koliko puta se substring sub ponavlja u stringu s.

    # sub = AT

    # O(len(n)) brzina algoritma jer je linearan prolazak kroz niz
    ans = [0] * len(s) # novi niz jednake dužine kao i string sa brojem ponavljanja substringa sub.
    for i in range(len(s) - len(sub), -1, -1): # slično sljedećem kodu for(int i = strlen(s) - strlen(sub); i > -1; i --)
        if s[i: i + len(sub)] == sub:
            if i + len(sub) > len(s) - 1: # base case
                ans[i] = 1
            else:
                ans[i] = 1 + ans[i + len(sub)]
    return max(ans)

def print_match(reader, array):
    for line in reader:
        person = line[0]
        values = [int(val) for val in line[1:]] # vrijednost (brojeve) ponavljanja dodaje u novi niz bez 0-tog elementa.
        if values == array: # uspoređuje dvije liste ako su jednake printa se ime osobe i završava funkcija.
            print(person)
            return
    print("Ne poklapa se.") # ako nijedna lista iz reader-a nije jednaka array listi.

def main():
    if len(argv) != 3: # provjera da li je broj unesenih argumenata jednak 3.
        print("Način korištenja: $ dna.py databases/ime_csv_fajla.csv sequences/broj.txt")
        exit(1)

    csv_path = argv[1]
    with open(csv_path) as csv_file: # otvara određeni fajl kao .csv i zatvara u slučaju greške.
        reader = csv.reader(csv_file) # csv_file se učitava pomoću csv.reader modula i iz toga dobivamo objekt

        # for row in reader:
        #    print(row) # na ovaj način printamo sve redove fajla kojeg učitamo.
        # test: python dna.py databases/large.csv sequences/5.txt.

        all_sequences = next(reader)[1:] # Učitava prvi red počevši od 1. elementa niza.

        txt_path = argv[2] # pokazivač na sequences/broj.txt.
        with open(txt_path) as txt_file: # otvara txt_path kao txt_file i zatvara u slučaju greške.
            s = txt_file.read() # učitava čitav string u jednu varijablu

            # print(s)

            array = [get_max_num_of_times_substring(s, seq) for seq in all_sequences] # LC -> provjerava koliko puta se substring (seq) iz all_sequences ponavlja u stringu s i ubacuje u novi niz.
        print_match(reader, array) # funkcija uspoređuje reader koji sadrži brojeve ponavljanja sa array-om.

if __name__ == "__main__":
    main()
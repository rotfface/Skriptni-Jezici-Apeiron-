from cs50 import SQL
from sys import argv

if len(argv) != 2:
    print("Netočan broj argumenata!")
    exit(1)

db = SQL("sqlite:///students.db")

house = argv[1]
rows = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", house)

for row in rows:
    first, middle, last, birth = row["first"], row["middle"], row["last"], row["birth"]
    print(f"{first} {middle + '' if middle else ''} {last}, rođen {birth} godine.")
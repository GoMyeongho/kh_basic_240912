word = input()
word.upper()
num_alphabet = []

for i in (ord("A"),ord("Z")+1):
    num_alphabet.append(word.count(chr(i)))
if num_alphabet.count(max(num_alphabet)) > 1:
    max_alphabet = "?"

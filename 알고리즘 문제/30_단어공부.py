word = input()
word = word.upper()
num_alphabet = []

for i in range(ord("A"),ord("Z")+1):
    num_alphabet.append(word.count(chr(i)))
if num_alphabet.count(max(num_alphabet)) > 1:
    max_alphabet = "?"
else:
    max_alphabet = chr(ord("A") + num_alphabet.index(max(num_alphabet)))
print(max_alphabet)
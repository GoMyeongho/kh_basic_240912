def encrypt(code, key):
    password = ""
    keys = []
    for e in key:
        keys.append(ord(e))
    count = 0
    for e in code:
        if e == " ":
            password += " "
        else:
            print(keys)
            temp_ord = (ord('e') - keys[count]) % 26 + ord("a")
            password += chr(temp_ord)
        count  = (count + 1) % len(keys)
    return password

words_input = input()
key_input = input()

print(encrypt(words_input,key_input))


#abcdefghijklmnopqrstuv
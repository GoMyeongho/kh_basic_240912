

def prime_config(num):
    prime_n = [2]
    for i in range(3, (num+1)//2 ):
        prime = True
        for e in prime_n:
            if i % e == 0: prime = False
        if prime: prime_n.append(i)
    for e in prime_n:
        if num % e == 0: return False
    return True

def str2ord(word):
    prime_sum = 0
    for e in word:
        if ord(e) >= ord("A"): prime_sum += ord(e) - ord("A") + 27
        else: prime_sum += ord(e) - ord("a") + 1
    return prime_sum

nums = str2ord(input())

print("It is a prime word") if prime_config(nums) else print("It is not a prime word")



#abcdefghijklmnopqrstuvwxyz
#12345678901234567890123456
# 21 + 6 + 18 + 14 +26 * 4
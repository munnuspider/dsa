print(ord('a'))
print(ord('e'))
print(ord('i'))
print(ord('o'))
print(ord('u'))

s = '__hel lo 123$world '
consonant = 0
vowel = 0

for i in s:
    if not (97 <= ord(i) <= 123):
        continue
    elif ord(i) == 97 or ord(i) == 101 or ord(i) == 105 or ord(i) == 111 or ord(i) == 117:
        vowel += 1
    else:
        consonant += 1

print(f"consonant nō: {consonant} and vowel nō: {vowel}")

vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():
        if ch in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print(f"consonant nō: {consonants} and vowel nō: {vowels}")

rand_string = "dana scully"
count = {}
for ch in rand_string:
    count[ch] = count.get(ch, 0) + 1

print(count)

from collections import Counter
print(Counter(rand_string))
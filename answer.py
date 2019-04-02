from pprint import pprint
sentence = "This is a common interview question"

# Find the most repeated charachter in this text

sentence = list(sentence)
# print(len(sentence))

charachter_number = []

for characthers in sentence:
    count = sentence.count(characthers)
    charachter_number.append(int(count))

# print(charachter_number)

combination = list(zip(sentence, charachter_number))
# print(combination)

letters = dict(set(combination))
print(letters)


# now reference the number part of the letters list
count = 0
for key, value in letters.items():
    if value > count:
        count = value
        char = key
    charachter = [char, count]

print(charachter)

count = 0
for key, value in letters.items():
    if value > count and key != ' ':
        count = value
        char = key
    charachter = [char, count]

print(charachter)

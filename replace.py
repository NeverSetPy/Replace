sentence = ('The!quick!brown!fox!jumps!over!the!lazy!dog!.')
sentence_rep = sentence.replace('!', ' ')
print(sentence_rep)

sentence_repCAPS = sentence_rep.upper()
print(sentence_repCAPS)

print(sentence_repCAPS[::-1])
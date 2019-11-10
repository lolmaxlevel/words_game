# coding: utf8
a = input("слово?\n")
slovo,otvet = [],[]
for i in a:
    slovo.append(i)
slovo_copy = slovo[:]
with open(r"word_rus.txt","rb") as diction:
    for i in diction:
        words = diction.readlines()
for i in words:
    word = ((i.decode("utf-8"))[:-2])
    for o in range(len(word)):
        if o == len(word) - 1 and word[len(word) - 1] in slovo_copy:
            otvet.append(word)
            slovo_copy = slovo[:]
        elif word[o] in slovo_copy:
            slovo_copy.remove(word[o])
        else:
            slovo_copy = slovo[:]
            break
if a in otvet:
    otvet.remove(a)
print(otvet)

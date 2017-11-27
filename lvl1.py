str = 'map'

str1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

alphabet = "abcdefghijklmnopqrstuvwxyzabc"
char = " ()'."
seq = []
s = ""
for letter in str:
    if letter in alphabet:
        new = alphabet[(alphabet.find(letter))+2]
        seq.append(new)
    elif letter in char:
        seq.append(letter)

print(s.join(seq))

print(s.maketrans())
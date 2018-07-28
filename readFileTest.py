path = "Z:/Python/deckLists/[SUM-CLS]Zygarde.txt"

f = open(path,'r')
while True:
    text = f.readline()
    if '* ' in text:
        print(text.split(' '))
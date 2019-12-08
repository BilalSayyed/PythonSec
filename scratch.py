alphabet = 'abcdefghijklmnopqrstuvwxzy'

key = 4

newmsg =''

message = input('enter a message')

for character in message:

    postion = alphabet.find(character)

    newpostion = (postion+key)%26

    newchar = alphabet[newpostion]

    print('encrypted new character is', newchar)

    newmsg+=newchar

    print('the encripted final message',newmsg)
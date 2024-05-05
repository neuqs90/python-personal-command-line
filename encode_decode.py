from string import ascii_letters,punctuation,digits
from random import sample,randint

def encode(text):

    encode_text = ""

    c = ascii_letters + digits + punctuation
    front_length = randint(1,5)
    random_fronts = sample(c,front_length)

    shift = randint(1,4)
    random_fronts = chr(front_length) + ''.join(random_fronts)
    encode_text += random_fronts
    
    for i in text:

        encode_text += chr(ord(i) + shift)

    return encode_text + chr(shift)

def decode(text):

    front_length = ord(text[0])
    removed_front = text[front_length+1:]

    shift = ord(text[len(text)-1])
   
    decoded_text = ""

    for i in removed_front:

        decoded_text += chr(ord(i) - shift)


    return decoded_text

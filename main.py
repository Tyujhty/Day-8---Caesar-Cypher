alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encode_text = list(text)
    new_encode_text = ''
    for letter in encode_text:
        if letter in alphabet:
            new_encode_text += alphabet[alphabet.index(letter) + shift]
    print(f"The encode message is: {new_encode_text}")

def decrypt(text, shift):
    decode_text = list(text)
    new_decode_text = ''
    for letter in decode_text:
        if letter in alphabet:
            new_decode_text += alphabet[alphabet.index(letter) - shift]
    print(f"The decode message is: {new_decode_text}")

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("Please, choose a correct direction")

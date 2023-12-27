alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encode_text = list(text)
    new_encode_text = ''
    for letter in encode_text:
        if letter in alphabet:
            new_letter = alphabet[alphabet.index(letter) + shift]
            new_encode_text += new_letter
    print(f"The encode message is: {new_encode_text}")
            
encrypt(text, shift)


    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

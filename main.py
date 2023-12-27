from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)
play_again = True

while play_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #modulus to set the range
    shift = shift % 26

    def caesar(direction, text, shift):
        cypher_text = ''
        if direction == 'decode':
            shift *= -1
        for letter in text:
            letter_position = alphabet.index(letter)
            cypher_text += alphabet[letter_position + shift]
        print(f"The {direction} message is: {cypher_text}\n")

    caesar(direction, text, shift)
    play_again = input("Type 'Yes' if you want to go again. Otherwise type 'no'").lower()
    if play_again == 'yes':
        play_again = True


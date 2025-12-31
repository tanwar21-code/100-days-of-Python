alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def cipher(original_text,shift_amount):
    if direction == 'encode':
        encrypted_text = ''
        for letter in original_text:
            position = alphabet.index(letter)
            new_position = position +shift_amount
            if new_position >25:
                new_position -= 26
            encrypted_text += alphabet[new_position]
        print(f'Your encrypted text is {encrypted_text}')
    else:
        decrypted_text = ''
        for letter in original_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            decrypted_text += alphabet[new_position]
        print(f'Your decrypted text is {decrypted_text}')

if direction == 'encode' or direction == 'decode':
    cipher(text,shift)
else:
    print('invalid input')
            
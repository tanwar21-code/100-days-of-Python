#caesar cipher part 1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text1,shift1):

    
        


#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

    encrypted_text = ''
    for letter in text1:
        position = alphabet.index(letter)
        new_position = position + shift1
        if new_position > 25:
            new_position = new_position - 26
        encrypted_text += alphabet[new_position]
    print(f'The encoded text is {encrypted_text}')


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == 'encode':
    encrypt(text, shift)

def decrypt(text1,shift1):
    decrypted_text = ''
    for letter in text1:
        position = alphabet.index(letter)
        new_position = position - shift1
        
        decrypted_text += alphabet[new_position]
    print(f'The decoded text is {decrypted_text}')

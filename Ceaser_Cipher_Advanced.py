alphabet = "abcdefghijklmnopqrstuvwxyz"
plain_text = input("Enter the text you want to encrypt: ")
shift = int(input("Enter the number of shift you want: "))
encrypted_text = ""
for char in plain_text:
    if char in alphabet:
        char_index = alphabet.find(char)
        char_index = (char_index + shift) % 26
        char = alphabet[char_index]
    encrypted_text += char
print(encrypted_text)
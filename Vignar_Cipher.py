def encrypt_letter(letter, shift):
    abc = "abcdefghijklmnopqrstuvwxyz"
    if letter.isalpha():
        ind = abc.index(letter)
        ind = (ind + shift) % 26
        secret_letter = abc[ind]
    else:
        secret_letter = letter
    return secret_letter    
print(encrypt_letter("v", 25))


def calculate_shift(letter):
    abc = "abcdefghijklmnopqrstuvwxyz"
    ind = abc.index(letter)
    return ind
print(calculate_shift("z"))

def encrypt_text(text, keyword):
    text = text.lower()
    keyword = keyword.lower()

    encrypted_text = ""

    for i in range(len(text)):
        key_letter = keyword[i % len(keyword)]
        shift = calculate_shift(key_letter)
        encrypted_text += encrypt_letter(text[i], shift)
    return encrypted_text

text = input("Enter the text you want to encrypt: ")
keyword = input("Enter the keyword you will employ for encryption: ")
print(encrypt_text(text, keyword))
    


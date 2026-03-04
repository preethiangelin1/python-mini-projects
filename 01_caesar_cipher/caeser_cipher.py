def encrypt(text, shift):
    encoded = ""
    if shift < 0:
        return text
    for ch in text.lower():
        encoded += chr(ord(ch) + shift)
    return encoded
    
def decrypt(text, shift):
    decoded = ""
    if shift < 0:
        return text
    for ch in text.lower():
        decoded += chr(ord(ch) - shift)
    return decoded

def main():
    print("Caeser Cipher!!")

    continue_game = True
    while continue_game:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("How many shifts?:\n"))

        if direction == 'encode':
            encrypted_text = encrypt(text,shift)
            print(f"Here,s the encoded result: {encrypted_text}")

        elif direction == "decode":
            decrypted_text = decrypt(text,shift)
            print(f"Here,s the decoded result: {decrypted_text}")

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n ").lower()
        
        if restart == 'no':
            continue_game = False
            print("Goodbye")

if __name__ == "__main__":
    main()

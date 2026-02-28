def main():
    print("Caeser Cipher!!")

    def encrypt(text, shift):
        encoded = ""
        for ch in text.lower():
            encoded += chr(ord(ch) + shift)
        return f"Here,s the encoded result: {encoded}"

    def decrypt(text, shift):
        decoded = ""
        for ch in text.lower():
            decoded += chr(ord(ch) - shift)
        return f"Here,s the decoded result: {decoded}"

    continue_game = True
    while continue_game:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("How many shifts?:\n"))

        if direction == 'encode':
            print(encrypt(text,shift))

        elif direction == "decode":
            print(decrypt(text,shift))

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n ").lower()
        
        if restart == 'no':
            continue_game = False
            print("Goodbye")

if __name__ == "__main__":
    main()

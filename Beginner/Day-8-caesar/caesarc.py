alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

from ccart import logo

print(logo)


def encrypt(text, shift):
    text_list = []
    for char in text:
        text_list.append(char)
    for i in range(len(text_list)):
        if text_list[i] in alphabet:
            index = alphabet.index(text_list[i])
            if index + shift > 25:
                text_list[i] = alphabet[index + shift - 26]
            else:
                text_list[i] = alphabet[index + shift]

    return "".join(text_list)


def decode(text, shift):
    text_list = []
    for char in text:
        text_list.append(char)
    for i in range(len(text_list)):
        if text_list[i] in alphabet:
            index = alphabet.index(text_list[i])
            if index - shift < 0:
                text_list[i] = alphabet[index - shift + 26]
            else:
                text_list[i] = alphabet[index - shift]

    return "".join(text_list)


end = False
while not end:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encode = encrypt(text, shift)
        print(f"The encoded text is : {encode}\n")
    elif direction == 'decode':
        decode = decode(text, shift)
        print(f"The decoded text is : {decode}\n")
    else:
        print("Invalid input")
        continue
    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == 'no':
        end = True
        print("Goodbye")
    elif restart == 'yes':
        end = False

print("Шифр тексту")
alphabet = "abcdefghijklmnopqrstuvwxyzaабвгдеєжзиійклмнопрстуфхцчшщьюяа12345678901"
while True:
    text1 = input("Введіть текст: ")
    x = input("Шифр(+), Розшифрування(-): ")
    key = int(input("Введіть ключ: "))
    text1 = text1.lower()
    text2 = ""

    if x == "+":
        for letter in text1:
            position = alphabet.find(letter)
            newposition = position + key
            if letter in alphabet:
                text2 = text2 + alphabet[newposition]
            else:
                text2 = text2 + letter
          
    elif x == "-":
        for letter in text1:
            position = alphabet.find(letter)
            newposition = position - key
            if letter in alphabet:
                text2 = text2 + alphabet[newposition]
            else:
                text2 = text2 + letter
           
    print(text2)
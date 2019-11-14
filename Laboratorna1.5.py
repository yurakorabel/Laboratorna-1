print("Шифр тексту")

alphabetEng = "abcdefghijklmnopqrstuvwxyz"
alphabetUa = "абвгдеєжзиійклмнопрстуфхцчшщьюя"
while True:
    language = input("Виберіть мову (eng or ua): ")
    text1 = input("Введіть текст: ")
    x = input("Шифр(+), Розшифрування(-)")
    key = int(input("Введіть ключ: "))
    text1 = text1.lower()
    text2 = ""
    if language == "eng":
        if x == "+":
            for letter in text1:
                position = alphabetEng.find(letter)
                newposition = position + key
                if letter in alphabetEng:
                    text2 = text2 + alphabetEng[newposition]
                else:
                    print("Помилка!")
        elif x == "-":
            for letter in text1:
                position = alphabetEng.find(letter)
                newposition = position - key
                if letter in alphabetEng:
                    text2 = text2 + alphabetEng[newposition]
                else:
                    print("Помилка!")
    elif language == "ua":
        if x == "+":
            for letter in text1:
                position = alphabetUa.find(letter)
                newposition = position + key
                if letter in alphabetUa:
                    text2 = text2 + alphabetUa[newposition]
                else:
                    print("Помилка!")
        elif x == "-":
            for letter in text1:
                position = alphabetUa.find(letter)
                newposition = position - key
                if letter in alphabetUa:
                    text2 = text2 + alphabetUa[newposition]
                else:
                    print("Помилка!")
    print(text2)
print("Калькулятор")
while True:
    what = ""
    choise = ["+", "-", "*", "/", "exit"]

    while what not in choise:
     what = input("Ведіть що ви хочете виконати(+, -, *, /, exit): ")

    if what == ("exit"):
        print("Дякую що використовуєте саме наш калькулятор)")
        break
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    if what == ("+"):
        c = a+b
        print("Відповідь: " + str(c))
    elif what == ("-"):
        c = a-b
        print("Відповідь: " + str(c))
    elif what == ("/"):
        try:
            c = a/b
        except:
            b = float(input("Введіть ще раз друге число: "))
            c = a/b
        finally:
            print("Відповідь: " + str(c))
    elif what == ("*"):
        c = a*b
        print("Відповідь: " + str(c))
    else:
        print("Помилка!")
   

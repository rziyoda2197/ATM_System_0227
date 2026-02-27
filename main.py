plastik_parol = 1414
plastik_balance = 100_000
foiz = 0.01

sorov = int(input("Karta parolini kiriting: "))

if sorov == plastik_parol:
    while True:
        print("\nSo‘rovni tanlang:")
        print("1 - Balance ko‘rish")
        print("2 - Naqd pul olish")
        print("0 - Chiqish")

        tanlov = int(input("Tanlovingiz: "))

        if tanlov == 1:
            print(f"Balansingiz: {plastik_balance}")

        elif tanlov == 2:
            print("\nSummani tanlang:")
            print("1 - 50_000")
            print("2 - 100_000")
            print("3 - 200_000")
            print("4 - 500_000")
            print("5 - Boshqa summa")

            tanlov_summa = int(input("Tanlovingiz: "))

            if tanlov_summa == 1:
                summa = 50_000
            elif tanlov_summa == 2:
                summa = 100_000
            elif tanlov_summa == 3:
                summa = 200_000
            elif tanlov_summa == 4:
                summa = 500_000
            elif tanlov_summa == 5:
                summa = int(input("Summani kiriting: "))
            else:
                print("Noto‘g‘ri tanlov ")
                continue

            kamm = int(summa * foiz)
            plastik_balance -= kamm
            print(f"Bizning kammissiyamiz: {kamm}")

            if summa <= plastik_balance:
                plastik_balance -= summa
                print("Pul muvaffaqiyatli yechildi ")
                print("Qolgan balans:", plastik_balance)

            else:
                print("Balans yetarli emas")

        elif tanlov == 0:
            print("Bankomatdan chiqildi")
            break

        else:
            print("Noto‘g‘ri tanlov")

else:
    print("Parol xato")

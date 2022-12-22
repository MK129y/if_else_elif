sport = input ( "Какое время года?: ")
pl_score = float(input("Какая температура воздуха днем: "))
p2_score = float(input("Какая температура воздуха ночью: "))
# 1
if sport.lower() == "зима":
# 2
    if pl_score == p2_score:
        print("Погода одинаковая и днем и ночью")
    elif pl_score > p2_score:
        print("Днем Теплее чем ночью")
    else:
        print("Ночью теплее чем днем.")
#elif sport.lower() == "golf":
elif sport.lower() == "лето":
# 3
    if pl_score == p2_score:
        print("Погода одинаковая и днем и ночью")
    elif pl_score > p2_score:
        print("Днем Теплее чем ночью")
    else:
        print("Ночью теплее чем днем.")
elif sport.lower() == "весна":
# 3
    if pl_score == p2_score:
        print("Погода одинаковая и днем и ночью")
    elif pl_score > p2_score:
        print("Днем Теплее чем ночью")
    else:
        print("Ночью теплее чем днем.")
elif sport.lower() == "осень":
# 3
    if pl_score == p2_score:
        print("Погода одинаковая и днем и ночью")
    elif pl_score > p2_score:
        print("Днем Теплее чем ночью")
    else:
        print("Ночью теплее чем днем.")
else:
    print(" Ты ввел неправильно, попробуй еще разочек")

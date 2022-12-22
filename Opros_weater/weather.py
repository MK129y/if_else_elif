sport = input ( "Какое время года?: ")
pl_score = int(input("Какая температура воздуха днем: "))
p2_score = int(input("Какая температура воздуха ночью: "))
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
elif sport.lstrip() == "лето":
# 3
    if pl_score == p2_score:
        print("Погода одинаковая и днем и ночью")
    elif pl_score > p2_score:
        print("Днем Теплее чем ночью")
    else:
        print("Ночью теплее чем днем.")
elif sport.lstrip() == "весна":
# 3
    if pl_score == p2_score:
        print("Погода одинаковая и днем и ночью")
    elif pl_score > p2_score:
        print("Днем Теплее чем ночью")
    else:
        print("Ночью теплее чем днем.")
elif sport.lstrip() == "осень":
# 3
    if pl_score == p2_score:
        print("Погода одинаковая и днем и ночью")
    elif pl_score > p2_score:
        print("Днем Теплее чем ночью")
    else:
        print("Ночью теплее чем днем.")
else:
    print(" Ты ввел неправильно, попробуй еще разочек ")

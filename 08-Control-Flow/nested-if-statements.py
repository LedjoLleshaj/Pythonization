ingredienti = "Pasta"
ingredinti2 = "Sugo"
if ingredienti == "Pasta":
    if ingredinti2 == "Sugo":
        print("Fai la pasta al sugo")
    else:
        print("Fai la pasta al pomodoro")
else:
    print("Fai la pizza")

if ingredienti == "Pasta" and ingredinti2 == "Sugo":
    print("Fai la pasta al sugo")
elif ingredienti == "Pasta" and ingredinti2 == "Pomodoro":
    print("Fai la pasta al pomodoro")
else:
    print("Fai la pizza u bitch")
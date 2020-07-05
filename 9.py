secret = "isabela"
guess = ""
hints = {
    1: "i",
    2: "is",
    3: "isa",
    4: "isab",
    5: "isabe",
    6: "isabel",
    7: "isabel_",
}
count = 0

while guess != secret:
    count += 1
    guess = input("Guess the secret work: ")
    if count < 8:
        print(f" Here is a hint: '{hints[count]}'")
    elif count >= 8:
        print("If you can't guess it by now you are an idiot")


print("Congradulations you have guessed the secret word!")
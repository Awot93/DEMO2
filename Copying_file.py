with open("numbers.txt", "r") as file:
    for line in file:
        with open("number2.txt", "a") as file2:
            line2 = str(line)
            file2.write(line2)
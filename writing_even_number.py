with open("numbers.txt","r+") as file:
    for line in file:
        line = int(line)
        if line % 2 == 0:
            with open("even_numbers.txt","a") as file2:
                line2 = line
                line2 = str(line2)
                file2.write(line2 + "\n")
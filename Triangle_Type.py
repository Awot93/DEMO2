first_angle = int(input("Please enter the first angle"))
second_angle = int(input("Please enter the second angle"))
third_angle = int(input("Please enter the third angle"))

sum_of_angle = first_angle + second_angle + third_angle

if (first_angle > 0) and (second_angle > 0) and (third_angle > 0) and (sum_of_angle == 180):
    if (first_angle == 90) or (second_angle == 90) or (third_angle == 90):
        print("The triangle is a right triangle.")
    elif (first_angle > 90) or (second_angle > 90) or (third_angle > 90):
        print("The triangle is an obtuse triangle")
    elif (first_angle < 90) or (second_angle < 90) or (third_angle < 90):
        print("The triangle is an acute triangle")
else:
    print("The entered values are not valid")
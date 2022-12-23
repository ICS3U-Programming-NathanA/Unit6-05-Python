#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Dec.15, 2022
# This program calculates the average of marks

# function that calculates the average
def calc_average(marks):
    # set sum to 0
    sum = 0
    # for each loop to calculate the sum of all the marks
    for counter in marks:
        sum = sum + counter
    # sum divided by the length to find the average
    average = sum / len(marks)
    # round the average
    average = round(average, 2)
    # return average
    return average


def main():
    # Create an empty list to store the marks
    marks_lists = []

    # Loop until the user enters -1
    while True:
        # Get the user's input
        mark_str = input("Enter a mark between 0 and 100 (-1 to stop): ")

        # Try catch to catch any invalid inputs
        try:
            mark = float(mark_str)
        except:
            # If they entered a invalid input then display this
            print("You must enter a valid number")
            # break out of the loop
            break
        else:
            # if marks is less than -1
            if mark > -1 and mark < 100:
                # If the user entered -1, stop the loop
                if mark == -1:
                    # Add the mark to the list
                    marks_lists.append(mark)
                    # Calculate and print the average of the marks
                    average = calc_average(marks_lists)
                    print("Average:", average)
            else:
                # if don't enter a number between -1 and 100
                print("You must enter a number between -1 and 100")
                # break out of the loop
                break


if __name__ == "__main__":
    main()

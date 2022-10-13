 #Task to take the first  two and last two letters of the input

manipulation_string = input("Write here please :) \n")

if len(manipulation_string) > 1:
    print(manipulation_string[0] + manipulation_string[1] + manipulation_string[-2] + manipulation_string[-1])
else:
    print("No input :(")

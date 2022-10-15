#Make a program that has some sentence (a string) on input and returns a dict containing
#all unique words as keys and the number of occurrences as values.

input_string = "Horse Cat Dog Fish Horse Giraffe Fish Dog Fish Cat Cat Horse Giraffe Horse Cat Giraffe"

def word_counter(str):
    counts = dict()
    words = str.split(" ")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_counter(input_string))

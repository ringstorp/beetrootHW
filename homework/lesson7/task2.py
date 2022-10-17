"""
Creating a dictionary.

Create a function called make_country, which takes in
a country’s name and capital as parameters. Then create a
dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
Make the function print out the values of the dictionary to make
sure that it works as intended.
"""

def make_country(name, capital):
    #list_name = [element1, element2]
    country_dict = {"name": name, "capital": capital}

    #different ways to print it
    print(name, capital)
    print(country_dict["name"], country_dict["capital"])
    print(country_dict)


make_country("Sweden", "Stockholm")
make_country("Denmark", "Copenhagen")

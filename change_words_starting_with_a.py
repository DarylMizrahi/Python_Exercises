def change_words_starting_with_a(words):
    appended_string = "hello"
    return [appended_string + " " +i for i in words if i.startswith("a")] #list comprehension


fruits = ["apples", "oranges", "apricots", "peaches"]
print(change_words_starting_with_a(fruits))
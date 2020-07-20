# define inputs to keep
letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
numbers = "0123456789"
keep = letters + numbers

# get input
string = input("Provide an input: ")

# remove punctuation

my_str = string.casefold()

no_punct = ""
for char in my_str:
    if char in keep:
        no_punct = no_punct + char

# check if the string contains numbers, for the hint in the output

str_state = ""

if no_punct.isalpha():
    str_state = "let_only"
elif no_punct.isnumeric():
    str_state = "num_only"
else:
    str_state = "al_num"

# check if string is a palindrome

if (no_punct == no_punct[::-1]):
    if (str_state == "num_only"):
        print("That is a palindromic number.")
    else:
        print("That is a palindrome.");
else:
    print("That is not a palindrome.")
    if (str_state == "al_num"):
        print("Your string contains numbers. Perhaps you need to type the numbers differently.")

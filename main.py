# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_template:
    letter_content = letter_template.read()

with open("./Input/Names/invited_names.txt") as letter_names:
    names_list = letter_names.readlines()

for name in names_list:
    custom_letter_content = letter_content
    # remove the spaces and new lines around the string name by using the string strip function
    stripped_name = name.strip()
    # replace the placeholder string with the individual names
    custom_letter_content = custom_letter_content.replace(PLACEHOLDER, stripped_name)

    letter_name = f"letter_for_{stripped_name}.txt"

    with open(f"./Output/ReadyToSend/{letter_name}", mode="w") as new_letter:
        new_letter.writelines(custom_letter_content)

# Helpful methods:
# https://www.w3schools.com/python/ref_file_readlines.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.w3schools.com/python/ref_string_strip.asp

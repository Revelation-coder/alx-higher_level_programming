#!/usr/bin/python3
'''
This module  function that prints a text
with 2 new lines after each of these characters:
., ? and :
'''


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    ., ? and :

    :param text: str, the text to be printed
    :return: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # remove any leading/trailing whitespaces
    text = text.strip()

    # loop over each character in the text
    for char in text:
        # print the character without a new line
        print(char, end="")

        # if the char is one of these chars: ., ? or :, print 2 new lines
        if char in [".", "?", ":"]:
            print("\n\n", end="")
        # if the character is not one of the above characters, print a new line
        else:
            print("\n", end="")

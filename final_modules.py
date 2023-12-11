#Modules for Final Project
#Author: Ryan Brown W0491090
#Date: Dec. 5, 2023

#this program is a module for final_project_ryan_brown.py
#functions used in that program have been transferred here

#import textwrap to format printed blocks of text
import textwrap

def wrappingtext(text_string):
    #this function takes a string of text [text], and wraps the 
    # text as output with width of 100
    wrap_text = textwrap.wrap(text = text_string, width = 100)
    wrapped_sentence = ""
    for row in wrap_text:
        wrapped_sentence += f"{row}\n"
    return wrapped_sentence       

def check_if_repeat(input_value, previous_input_list):
    #this function takes an input from the user [input_value], 
    #and checks if it is already present in a list of previously 
    #inputted values [previous_input_list]
    if input_value in previous_input_list:
        return True
    else:
        return False

def check_if_correct(input_value, valid_input_list):
    #this function takes an input from user [input_value],
    #and checks if it is a valid input for the selection 
    #[valid_input_list]
    if input_value in valid_input_list:
        return True
    else:
        return False
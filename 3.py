# import modules
import random
from threading import Timer

# define the function for timeouting timer
def timeout() -> None:
     '''this function used for timeout of timer for showing the message'''

     # showing the message for user
     print("\nTime of your exam is finish")


# define the clculate_magic_numbers 
def calculate_magic_numbers(start, end) -> binary_nubmer:
     ''' this function use for choice a random number of 1 to 15 and transform
     that to binary '''

     # choice a random number from 1 to 15
     random_number = random.randint(start, end)
     # print(random_number)
    
     # return the binary of the our random number
     return bin(random_number)


# define exam_num
def exam_num(magic_number) -> None :
     ''' this function used for guss an int number for our binary number in 20 seconds '''
     
     # create Timer object with 20 seconds and connected to the timeout function
     t = Timer(20, timeout)

     # Start of our timer object
     t.start()

     # save of user's answer in answer variable
     answer = int(input(f"what is int of {magic_number.lstrip('-0b') } : "))

     # check of answer with magic_number
     if answer == int(magic_number, 2):
          print("your answer is correct")
     else:
          print('this answer is not correct!')


# call the calculate_magic_numbers and save it into magic_number varaible
magic_number = calculate_magic_numbers(0, 15)

# call exam_num for checking the user's answer
exam_num(magic_number)


# -----------------------------------
import string

# define check_punctuation 
def check_punctuation(word):
     ''' this function used for checking the exist punctuation in our string '''

     # return True and flase if exist punctuation or not
     return any(char in string.punctuation for char in word)

# define the check_pass function
def check_pass(user_list) -> list:
     ''' this function used for check valid username and returned to the program '''

     # define helping variable 
     valid_password_len = False 
     valid_password_lower_letter = False
     valid_password_upper_letter= False
     valid_password_punction = False

     # check item by item 
     for item in user_list:

          # showing the password
          # print(item[1])

          # check len of password
          if len(item[1]) >= 8:
               valid_password_len = True

          # check letter by letter
          for letter in item[1]:

               # checking exist lower case in our string
               if letter in list('abcdefghigklmnopqrstuvwkyz'):
                    valid_password_lower_letter = True

               # checking exist Captal case in our string
               if letter in list( 'abcdefghigklmnopqrstuvwkyz'.upper() ):
                    valid_password_upper_letter = True

          # check exist a punctuation in our string
          valid_password_punction = check_punctuation( item[1] )
          
          # debugging
          # print('len', valid_password_len)
          # print('lower:', valid_password_lower_letter)
          # print('upper:', valid_password_upper_letter)
          # print('punction:', valid_password_punction)

          valid = valid_password_len and valid_password_lower_letter and valid_password_upper_letter and valid_password_punction

          # check valid password
          if valid:
             print(item[0])


my_tuple = [('asgharrr', 'Azizi123456'), ('bardia', 'Bardia.Tabesh')]


check_pass( my_tuple)

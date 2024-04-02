import random
from threading import Timer

def timeout() -> None:
     print("\nTime of your exam is finish")


def calculate_magic_numbers(start, end) -> binary_nubmer:
     random_number = random.randint(start, end)
     return bin(random_number)

def exam_num(magic_number) -> None :
     t = Timer(20, timeout)
     t.start()
     answer = int(input(f"what is int of {magic_number.lstrip('-0b') } : "))
     if answer == int(magic_number, 2):
          print("your answer is correct")
     else:
          print('this answer is not correct!')
magic_number = calculate_magic_numbers(0, 15)
exam_num(magic_number)



import string


def check_punctuation(word):
     return any(char in string.punctuation for char in word)
def check_pass(user_list) -> list:
     valid_password_len = False 
     valid_password_lower_letter = False
     valid_password_upper_letter= False
     valid_password_punction = False
     for item in user_list:
          if len(item[1]) >= 8:
               valid_password_len = True
          for letter in item[1]:
               if letter in list('abcdefghigklmnopqrstuvwkyz'):
                    valid_password_lower_letter = True
               if letter in list( 'abcdefghigklmnopqrstuvwkyz'.upper() ):
                    valid_password_upper_letter = True
          valid_password_punction = check_punctuation( item[1] )
          valid = valid_password_len and valid_password_lower_letter and valid_password_upper_letter and valid_password_punction
          if valid:
             print(item[0])


my_tuple = [('asgharrr', 'Azizi123456'), ('bardia', 'Bardia.Tabesh')]


check_pass( my_tuple)

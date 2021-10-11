


# word_phrase = []
# caps_list = []
# new_string = ''
# letter_counter = ''
# i = ''
comp_str = []

def user_input ():
    word_phrase = input ('Please type the word or phrase you would like to use: ')
    selected_value = word_phrase
    return word_phrase

# def word_reverse_tool ():
#     new_word_phrase = ''
#     for index in range(len(word_phrase) -1,-1,-1):
#         new_word_phrase += word_phrase[index]
#     print (new_word_phrase)

# word_phrase = user_input()
# word_reverse_tool()


# def capitalize():
#     new_string = ''
#     caps_list = []
#     word_phrase_string = ''
#     word_phrase = user_input()
#     if len (word_phrase == 0):
#         print ('No input detected')
#     word_phrase_list = list(word_phrase.split(' '))
#     for word in word_phrase_list:
#         new_word = word.capitalize()
#         caps_list.append(new_word)
#     for item in caps_list:
#         new_string += item + ' '
#     print(new_string)
#     return (new_string)

# def compression():
#     letter_counter = int(0)
#     list_of_letters = []
#     i = (0)
#     user_string = user_input()
#     while letter_counter < len(user_string) -1:
#         if (list_of_letters[i]) == (list_of_letters[i+1]):
#             letter_counter += 1
#             #list_of_letters = list_of_letters + str(user_string) + str(letter_counter)
#         elif (list_of_letters[i]) != (list_of_letters[i+1]):
#             list_of_letters = list_of_letters + str(user_string) + str(letter_counter)

#         print(list_of_letters)


def compression():
    letter_counter = int(0)
    list_of_letters = []
    i = (0)
    user_string = user_input()
    while letter_counter < len(user_string) -1:
        if (user_string[i]) == (user_string[i+1]):
            letter_counter += 1
            #list_of_letters = list_of_letters + str(user_string) + str(letter_counter)
        elif (user_string[i]) != (user_string[i+1]):
            list_of_letters =str(user_string) + str(letter_counter)

        print(list_of_letters)

compression()


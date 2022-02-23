# -*- coding:utf-8 -*-

# import nltk
# nltk.download('words')
from nltk.corpus import words

# print(type(words.words()))

# print(len(A)) 236736
# print(words_list)
# dough -> ['-----', ()] -> ('d', 'o', 'u', 'g', 'h') del 1 word del 5 letters 'd', 'o', 'u', 'g', 'h'
# if first input as '-----' del 1 word and 5 letters, no need to ask second input in round 1
# and renew list...
# alias -> ['--i--', ('l', 's')] del 1 letter 'a'
# renew list
# smile -> ['s-il-', ()] del 2 letters 'm', 'e'
# renew list
# still -> ['s-ill', ()] del 1 letter 't'
# renew list
# spill -> ['s-ill', ()] del 1 letter 'p'
# renew list
# swill -> ['swill', ()] del 0 letter
def renew_dict(input, reference, letter, idx=None, bool=None):
    if not input:
        return reference
    else:
        if idx:
            return [K for K in reference if letter == K[idx]]
        if bool:
            return [K for K in reference if letter not in K]
        return [K for K in reference if letter in K]

    
# global A
# global A5
# global words_list
A = words.words()
A5 = [K.lower() for K in A if len(K) == 5]
# dynamic list
words_list = [list(K) for K in A5]
round = 0

def prompt(round=None):
    if not round:
        print("Wellcome to WORDLE !!!")
        prompt(True)
    else:
        # dynamic list
        global words_list
        while round < 7:
            print("You left {} times guessing !".format(6 - round))
            round += 1
            spotA = input("Skip(Enter) if not a word in the correct spot: ")
            if not spotA:
                spotB = input("Oops, all the letters are not in any spot.\nPlease input correct letters for renewing the Dict: ")
                if spotB:
                    print("We will renew the Dict", spotB)
                    for idx, letter in enumerate(list(spotB)):
                        words_list = renew_dict(spotB, words_list, letter)
                        print(words_list, len(words_list), "word(s) have been kept!!!")
                else:
                    print(words_list, len(words_list), "word(s) have been kept!!!")
                    print('Enter(skip) then break')
                # The letters are not in the word in any spot.
                spotC = input("Please input incorrect letters for renewing the Dict: ")
                if spotC:
                    for idx, letter in enumerate(list(spotC)):
                        words_list = renew_dict(spotC, words_list, letter, None, True)
                        print(words_list, len(words_list), "word(s) have been kept!!!")
                    print("Go next round!!!")
                    print("round: ", round)
                else:
                    input('Enter(skip) then break...')
                    break
            else:
                number = 0
                for idx, letter in enumerate(list(spotA)):
                    if letter != "-":
                        number += 1
                        words_list = renew_dict(spotA, words_list, letter, idx)
                        print('The letter {} is in the word and in the {}th spot.'.format(letter, idx))
                if(number == 5):
                    round = 6
                    print("Good job !!! see you tomorrow.")
                    break
                print(words_list, len(words_list), "word(s) have been kept!!!")
                spotB = input("Please input correct letters for renewing the Dict: ")
                if spotB:
                    print("We will renew the Dict...")
                    for idx, letter in enumerate(list(spotB)):
                        words_list = renew_dict(spotB, words_list, letter)
                    print(words_list, len(words_list), "word(s) have been kept!!!")
                else:
                    print(words_list, len(words_list), "word(s) have been kept!!!")
                    print('Enter(skip) then break...')
                # The letters are not in the word in any spot.
                spotC = input("Please input incorrect letters for renewing the Dict: ")
                if spotC:
                    for idx, letter in enumerate(list(spotC)):
                        words_list = renew_dict(spotC, words_list, letter, None, True)
                    print(words_list, len(words_list), "word(s) have been kept!!!")
                    print("Go next round!!!")
                    print("round: ", round)
                else:
                    print('Enter(skip) then break...')
                    break
                if round > 7:
                    print("Keeping fighting, see you tomorrow")
                    break     


prompt()
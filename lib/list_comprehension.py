#!/usr/bin/env python3

def return_evens(num_list):
    return_evens= []
    for num in num_list:
        if(num%2 == 0):
            return_evens.append(num)
    return return_evens
return_evens([1,10,2])

def make_exclamation(sentence_list):
    exclamation_list = []
    for sentence in sentence_list:
        exclamation_list.append(f"{sentence}!")
    print(exclamation_list)
    return exclamation_list
make_exclamation(["I like computers", "I require coffee", "Live long and prosper"])
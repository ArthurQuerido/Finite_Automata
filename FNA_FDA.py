# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:41:04 2021

@author: Arthur Querido Lopes

"""

#function to change state and check if final state is part of the accepted 
#states' set

def FA(transitions, state, accepting, s):
    
    if (s == "-") or (s == ''):
        if state not in accepting:
            return False
        else:
            return True
    if (transitions.get(str(state), {}).get(s[0]) == None):
        return False
        
    states = transitions[str(state)][s[0]]
    for next_state in states:
        if(FA(transitions, next_state, accepting, s[1:])):
            return True
        
    return False
        

#Dictionary populator if you have multiple values for a single key
def add_values_in_dict1(sample_dict, key, value):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].append(value)
    return sample_dict

#Dictionary populator for populating dictionary keys with another dictionary
def add_values_in_dict2(sample_dict, key, sup_dict):
    if key not in sample_dict:
        sample_dict[key] = {}
    sample_dict[key] = sup_dict
    return sample_dict

sup_dictionary = {}
transitions_dictionary = {}

#receiving number of states from user
n = int(input("Input total number of states: "))
for i in range(n):
    transitions_dictionary[str(i)] = {}

#Receiving acceptance states from user
acceptance_states = input("Enter acceptance states separated by space: ")
acceptance_states = set(map(int, acceptance_states.split()))

#Receiving number of transitions from user
t = int(input("Input total number of transitions: "))

#Receiving transitions from user
transitions = []
for i in range(t):
    transitions.append(input("Enter transition: "))

#Populating transitions dictionary
for trans in transitions:
    state, key, value = trans.split()
    sup_dictionary = transitions_dictionary[state] 
    add_values_in_dict1(sup_dictionary, key, int(value))
    add_values_in_dict2(transitions_dictionary, state, sup_dictionary)


#Receiving number of strings to be tested
c = int(input("Input number of strings to be tested: "))

#Receiving strings one by one
print("Enter string by string, pressing enter after each: ")
strings = []
for i in range(c):
    strings.append(str(input()))

#Testing all strings
for string in strings:
    if (FA(transitions_dictionary, 0, acceptance_states, string)):
        print("accept")
    else:
        print("reject")
        
input()
#!/usr/bin/env python
#Xavier Marseille

import sys
import json
from collections import namedtuple



def main():     #open the json file we need
    with open('blood-die.json', 'r') as bloodie_jason:
        blooddiefile = json.load(bloodie_jason)
        bloodie_jason.close()
        
    empty_list = [] #make an empty list which i will use to put in my retrieved data
    compare_list = namedtuple("language", "name, classification") #use the namedtuple function


    for x in blooddiefile:      #look through the blood-die.json file
        blood = x[2].split()    #Split the words in the third line of the file
        die = x[3].split()      #split the words in the fourth line of the file
        [empty_list.append(compare_list(x[0], x[1])) for bloodie_word in blood if bloodie_word in die] #put the splitted words in the empty list if they are the same
    [print(x) for x in empty_list] #prints the outcome

    
    

if __name__ == '__main__':
    main()

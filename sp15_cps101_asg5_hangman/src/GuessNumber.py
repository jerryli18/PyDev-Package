'''
Illustrates interactive "game"
Created on Feb 14, 2011
Revised Oct 8, 2012

@author: ola
'''

import random

def get_status(secret,guess):
    '''
    Based on parameters secret and guess returns one of 'high', 'low', 'correct'
    e.g., if secret < guess returns 'high'
    '''
    
    if secret == guess:
        return "correct"
    if secret < guess:
        return "high"
    return "low"

def play_game_computerguess():
    '''
    plays a game in which the computer guesses the human player's number
    '''
    
    _MAX = 100
    low = 1
    high = _MAX
    guess_count = 0
    
    print "I will guess your number, you answer [h]igh, [l]ow, [c]orrect"
    print "start by thinking of a number between 1 and ",_MAX
    
    answer = 'none'
    while answer[0] != 'c':
        guess = (low+high)/2
        guess_count += 1
        print "I guess ",guess
        print "[h]igh,[l]ow,[c]orrect> ",
        answer = raw_input()
        if answer[0] == 'h':
            high = guess-1
        elif answer[0] == 'l':
            low = guess+1
        
        if low > high:
            print "either you made a mistake or I did, I give up!"
            break
    
    print "it took me ",guess_count," tries to guess ",guess
    
def play_game_humanguess():
    '''
    plays a game in which the human guesses the computer's number
    '''
    
    _MAX = 100
    secret = random.randint(1,_MAX)
    guess_count = 0
 
    print "I'm thinking of a number between 1 and ",_MAX
    
    guess = -1 
    while secret != guess:
        print "guess> ",
        guess = raw_input()
        guess = int(guess)
        guess_count += 1
        status = get_status(secret,guess)
        if status == "low":
            print "you're guess is too low, try again"
        elif status == "high":
            print "you're guess is too high, try again"
    
    print "Great! it took you ",guess_count," tries to guess ",secret
    
if __name__ == "__main__":
    play_game_computerguess()           
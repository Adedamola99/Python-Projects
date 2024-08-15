import random
def play():
    user = input('What your choice? rock(r), scisscors(s) and paper(p): ')
    computer = random.choice(['r', 's', 'p'])
    
    if user == computer:
        return 'It\'s is a tie'
    
    if is_win(user, computer):
        return 'You won'
    
    else:
        return 'You lost'
    
def is_win(player, opponent) :
    if (player == 'r' and opponent == 's') and (player == 's' and opponent == 'p') and (player == 'p' and opponent == 'r'): 
        return True
     
print(play())
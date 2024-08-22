choice_1 = int(input('Player 1, choose an integer from 1 to 100: '))
choice_2 = int(input('Player 2, choose an integer from 1 to 100: '))
choice_3 = int(input('Player 3, choose an integer from 1 to 100: '))
if choice_2 < choice_1 < choice_3 or choice_3 < choice_1 < choice_2:
    print('Player 1 wins!')
elif choice_1 < choice_2 < choice_3 or choice_3 < choice_2 < choice_1:
    print('Player 2 wins!')
elif choice_1 < choice_3 < choice_2 or choice_2 < choice_3 < choice_1:
    print('Player 3 wins!')
else:
    print('Two or more players chose the same number - no one wins.')
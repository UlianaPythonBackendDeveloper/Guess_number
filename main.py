print("-----------------------------------")
print("Welcome to game guess number!")

def guess_number(number):
    if number == 42:
        return 'You win!'
    elif number > 42:
        return 'Try again! So big number'
    else: 
        return 'Try again! So low number'
        
while True:
    try:
        play_screen = int(input("Enter You number: "))
        result = guess_number(play_screen)
        print(result)
        
        if play_screen == 42:
            break
    except ValueError:
        print('Erorr! Enter valid number!')

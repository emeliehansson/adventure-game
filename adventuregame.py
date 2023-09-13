# Define a room
description = 'big room with chandelier hanging from the roof and paintings all along the walls.'
doors = ['North', 'South', 'West', 'East']

# Welcome screen
print('Hello and welcome to Emelies adventurous journey!')
print('''
▄▀█ █▀█ █▀▀   █▄█ █▀█ █░█   █▀█ █▀▀ ▄▀█ █▀▄ █▄█ ▀█ █
█▀█ █▀▄ ██▄   ░█░ █▄█ █▄█   █▀▄ ██▄ █▀█ █▄▀ ░█░ ░▄ ▄''')
print()

# Main loop/gameloop
run = True
while run:
    # Print rooms
    print('You are standing in a ' + description)
    print()
    print('There are doors to your:')

    # Format and print out all the directions that are available in the room
    directions = ''
    for direction in doors:
        directions = directions + ', ' + direction
    directions = directions[2:]
    print(directions)
    print()

    # Print menu
    print('What do you want to do?')
    print('1. Go North')
    print('2. Go South')
    print('3. Go West')
    print('4. Go East')
    print('5. Look')
    print('0. Quit game')

    # Ask user for input
    choice = input('Please enter your choice by choosing a number between 0-5: ')

    # Sanitize user input
    if not choice.isnumeric():
        print('Sorry! I did not understand what you meant?')
        continue

    # Do something based on what the user asks for.
    # If the user enters something you don't understand, let them know.
    choice = int(choice)
    if choice == 0:
        run = False
        print('Quitting game')
    elif choice == 1:
        print('You are going north')
    elif choice == 2:
        print('You are going south')
    elif choice == 3:
        print('You are going east')
    elif choice == 4:
        print('You are going west')
    elif choice == 5:
        print("You are looking really hard but can't find anything new")
    else:
        print('Sorry, you asked for something I cannot do')

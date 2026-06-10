import string

while True:
    # Get password
    password = input('Enter a password (type "quit" to exit): ')

    if password.lower() == 'quit':
        print('Goodbye')
        break

    score = 0
    tips = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append('Password must have at least 8 characters')

    # Uppercase Letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        tips.append('Password must contain at least one uppercase letter')

    #lowercase letter
    if any(char.islower() for char in password):
        score += 1
    else:
        tips.append('Password must contain at least one lowercase letter')

    # Numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        tips.append('Password must contain at least one number')

    # Special character
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        tips.append('Password must contain a special character')


    # Determine strength
    if score <= 2:
        strength ='weak'
    elif score <= 4:
        strength = 'Medium'
    else:
        strength = 'Strong'

    # Result
    print('\nPassword Analysis')
    print('-------------------')
    print(f'score: {score}/6')
    print(f'strength: {strength}')

    if tips:
        print('\nSuggestions:')
        for tip in tips:
            print(f'- {tip}')
    else:
        print('\nYour password meets all recommended requirements!')

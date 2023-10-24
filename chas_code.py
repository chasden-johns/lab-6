def encode(password):
    total = ''
    for item in str(password):
        if int(item) < 7:
            total += (str(int(item) + 3))
        if item == '7':
            total += '0'
        elif item == '8':
            total += '1'
        elif item == '9':
            total += '2'
    return total

def decode(password):
    total = ''
    for item in str(password):
        if int(item) > 2:
            total += (str(int(item) - 3))
        if item == '0':
            total += '7'
        elif item == '1':
            total += '8'
        elif item == '2':
            total += '9'
    return total

if __name__ == '__main__':
	while True:
    		print('\nMenu')
    		print('-------------')
    		print('1. Encode\n2. Decode\n3. Quit')
    		print()
    		menu_option = int(input('Please enter an option: '))
    		if menu_option == 1:
        		global password
        		password = int(input('Please enter your password to encode: '))
        		print('Your password has been encoded and stored!')
        		password = encode(password)
        		continue
    		if menu_option == 2:
        		print(f'The encoded password is {password}, and the original password is {decode(password)}.')
    		if menu_option == 3:
        		break

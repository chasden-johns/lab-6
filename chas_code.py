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

def decode(code):  ## Darvan Cherichel
    pass_decode=""
    
    for digit in code:
        
        if digit == "1":
            pass_decode+="8"
        
        elif digit =="2":
            pass_decode="9"
        
        elif digit=="3":
            pass_decode+="0"
            
        elif digit=="4":
            pass_decode+="1"
            
        elif digit=="5":
            pass_decode+="2"
        
        elif digit=="6":
            pass_decode+="3"
        
        elif digit=="7":
            pass_decode+="4"

        
        elif digit=="8":
            pass_decode+="5"
        
        elif digit=="9":
            pass_decode+="6"
        
        elif digit=="0":
            pass_decode+="7"
        
    return pass_decode

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

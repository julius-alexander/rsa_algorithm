"""
This program was written to show the implementation of the RSA algorithm in (Python) code
This likely has not been fully optimized, but that is a task for another day...
(Note: program is case-sensitive)

Example test case:
    n = 77
    e = 37
    d = 13

Remember, n and e together form the public key and the integer d is the private key
"""

# stop is placeholder for 0 index, which we do not want used
legal_chars = ['stop', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               ',', '\'', '?', '!', '.', ' ']


def decrypt(message_to_decrypt, modulo, private_key):
    words_in_message = message_to_decrypt.split(' ')
    for letters in words_in_message:
        letter_values = int(letters)
        decrypted_letter = letter_values ** private_key % modulo
        letter = legal_chars[decrypted_letter]
        print(letter, end='')


def encrypt(message_to_encrypt, modulo, public_key):
    my_list = [char for char in message_to_encrypt]
    for i in my_list:
        letter = legal_chars.index(i)
        crypted_letter = letter ** public_key % modulo
        print(crypted_letter, end=' ')


def menu():
    print('\nWelcome to the RSA encryption program.\nPlease choose from the following:'
          '\n1. Encrypt a message\n2. Decrypt a message\n')


# Driver function for program
def main():

    run_again = 'yes'
    while run_again == 'yes':
        menu()

        decision = int(input('Enter your choice (1 or 2): '))
        while decision < 1 or decision > 2:
            decision = int(input('Invalid entry. Please enter a valid choice: '))

        mod = int(input('What\'s the value of n? '))
        while mod <= 0:
            mod = int(input('Invalid entry. Please enter a valid choice: '))

        if decision == 1:
            public = int(input('What\'s the value of e? '))
            message = input('Enter a message you would like to encrypt: ')
            # noinspection PyBroadException
            try:
                encrypt(message, mod, public)
            except:
                print('Something went wrong...')

        elif decision == 2:
            private = int(input('What\'s the value of d? '))
            message = input('Enter a message you would like to decrypt: ')
            # noinspection PyBroadException
            try:
                decrypt(message, mod, private)
            except:
                print('Something went wrong... Do you have the correct private key? ', end='')

        run_again = input('\n\nWould you like to run this program again? Enter yes or no: ')


main()

print('\nThanks for using this program!')

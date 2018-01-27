def palindrome_check(word):
    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    return False


if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
        print('Usage: {} <input string>'.format(argv[0]))
        exit(-1)

    if palindrome_check(argv[1]):
        print('{} is a palindrome.'.format(argv[1]))
    else:
        print('{} is NOT a palindrome.'.format(argv[1]))

'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0

    if word.startswith('th'):
        count = 1

    if len(word) > 2:
        return count_th(word[1:len(word)]) + count
    else:
        return count

if __name__ == '__main__':
    word = "abcthxyz"
    count = count_th(word)
    print(f"word: '{word}, expected: 1, actual: {count}")

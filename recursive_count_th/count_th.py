'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0

    if len(word) <= 1:
        return count
    # If word first two chars 'th' increase count by 1, and
    elif word[0:2] == 'th':
        count += 1
        return count + count_th(word[2:])
    else:
        wtf = count_th(word[1:])
        # recurse with rest of the chars (split the word) if no chars found
        return count_th(word[1:])
    

word = "th"
# THtHThth 0
# HtHThth 0
# tHThth 0
# HThth 0
# Thth 0
# hth 0
# th 1
print(count_th(word))

# Build-in method
# def count_th(word):
#     return word.count('th')
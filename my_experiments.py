# def double_char(s):
#     result = ''
#     i = 0
#     while i < len(s):
#         result = result + s[i] * 2
#         i += 1
#     print(result)

# double_char('World is empty!')

# chars = []
# for i in range(65, 91):
#     chars.append(chr(i))
 
# print(chars)
# создается список из букв латиницы в алфавитном порядке

# alph = list('abcdef')
# print(alph)

"""
When provided with a letter, return its position in the alphabet.

Input :: "a"
Ouput :: "Position of alphabet: 1"
"""

# def position(char):
#     alphabet = list('abcdefghijklmnopqrstuvwxyz')
#     i = 0
#     while i < len(alphabet):
#         if char != alphabet[i]:
#             i += 1
#         else:
#             break
#     return 'Position of alphabet: ' + str(i + 1)
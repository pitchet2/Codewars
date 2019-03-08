#There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.  A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".  As a simplification, you may assume that no letter occurs more than once in the secret string.  You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.


from itertools import chain
def recoverSecret(triplets):
    total_letters = list(set(chain.from_iterable(triplets)))
    a = 0
    while a < 3:
        for i in triplets:
            index =[]
            for j in i:
                index.append(total_letters.index(j))
            index.sort()
            print(total_letters)
            total_letters[index[0]] = i[0]
            total_letters[index[1]] = i[1]
            total_letters[index[2]] = i[2]
        a += 1
    return ''.join(total_letters)

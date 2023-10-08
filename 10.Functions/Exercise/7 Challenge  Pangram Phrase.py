# 7 Challenge  Pangram Phrase
# pangram - very letter in the english must appear atleast once in the sentence
# eg : The quick brown fox jumps over the lazy dog

def pangram(phrase):
    alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

    list_phrase = [x.lower() for x in phrase]
    set_phrase = set(list_phrase)

    if set_phrase >= alphabets:
        return True
    else:
        return False


p1 = pangram('The quick brown fox jumps over the lazy dog')
print(p1)

p2 = pangram('Hi my name is Arun')
print(p2)

p3 = pangram('abcdefghijkllllmmnnooppqqrrssttuuvvwxyz')
print(p3)

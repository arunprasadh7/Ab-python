# 8 Challenge  Case Counting Letters - count the no of uppercase and lowercase letters in given string

def counting(sentence):
    # list1 = [x for x in sentence]
    upper_count = 0
    lower_count = 0

    for i in sentence:
        if i.isupper() is True:
            upper_count += 1
        elif i.islower() is True:
            lower_count += 1

    print(f'Total no of Upper case letters : {upper_count}.')
    print(f'Total no of Lower case letters : {lower_count}.')


sentence = input('Enter the sentence: ')
counting(sentence)

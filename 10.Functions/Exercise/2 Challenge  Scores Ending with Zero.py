# 22. Challenge  Scores Ending with Zero

scores = [200, 456, 300, 100, 234, 678]


def non_zero_scores():
    count = 0
    nonzero = []
    for i in scores:
        if i % 10 == 0:
            count += 1
            nonzero.append(i)
    # return count,nonzero
    print(f'Total no of nonzero scores in the list = {count}.')
    print('\nNon-zero scores from the list are :')
    for score in nonzero:
        print(score)


non_zero_scores()

# if the list is not provided


def nozero(L=[]):
    n = []
    score_count = 0
    for score in L:
        if score % 10 == 0:
            score_count += 1
            n.append(score)
    print(f'Non-zero scores in the list is : {score_count}')
    print('Non-zero scores from the list are:')
    for i in n:
        print(i)


b = [100, 123, 200, 234, 300]
nozero(b)

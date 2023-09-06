#Finding words starting with given letter in a list
food = ['pizza','nuggets','hotdog','noodles','pasta','burger']
letter = input('Enter the letter : ')

'''
#method 1
matching_word = [food for food in food if food.startswith(letter)]
print(matching_word)
'''
#method 2
for i in food:
    if i.startswith(letter):
        print(i)
    else:
        pass
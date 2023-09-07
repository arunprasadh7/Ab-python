#Finding the longest and shortest meaning in a dict

dictionary = {
    "apple": "A round fruit with red or green skin and crisp flesh, typically eaten fresh.",
    "car": "A four-wheeled motor vehicle used for transportation.",
    "computer": "An electronic device that can store, retrieve, and process data.",
    "book": "A written or printed work consisting of pages glued or sewn together along one side.",
    "dog": "A domesticated mammal of the species Canis lupus familiaris, typically kept as a pet."
}


words = list(dictionary.keys())
meanings = list(dictionary.values())
lens = [ len(x) for x in dictionary.values()]
#print(lens)
max_length = max(lens)
min_length = min(lens)

#toFindTheIndex
max_index = lens.index(max_length)
min_index = lens.index(min_length)

print(f'Max value : {max_length} \n{words[max_index]} - {meanings[max_index]}')
print(f'Min value : {min_length} \n{words[min_index]} - {meanings[min_index]}')

def changeling(x):
    word_array = x.split()
    for i in range(len(word_array)/2):
        if word_array[i] == word_array[len(word_array) - i]:
            print('yes')

changeling('araros')
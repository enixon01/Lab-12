#Emily Nixon
def get_hashtags(input_sentence):
    output_list = []
    for word in input_sentence.split():
        if word.startswith("#"):
            output_list.append(word)
        return output_list

my_sentence = "I love #Python and #MachineLearning!"
my_list = get_hashtags(my_sentence)
print(my_list)

#This code is different from the last because it loops through the sentence and sorts the words based on the characters present

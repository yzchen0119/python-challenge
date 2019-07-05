import os
import re

fileList = ["paragraph_1.txt", "paragraph_2.txt"]
for file in fileList:
    txtpath = os.path.join("raw_data", file)

    with open(txtpath, 'r') as text:
        paragraph = text.read()
        sentences = re.split('[.?!]\s+|[.?!]\"', paragraph)
        words = re.split(" ", paragraph)
        letter_count = 0
        word_count = 0
        for word in words:
            word_count = word_count + 1
            letter_count = letter_count + len(word)        
        
        average_sentence_length = round(word_count/len(sentences), 1)
        average_letter_count = round(letter_count/word_count, 1)
    
    outputpath = os.path.join("..", "PyParagraph", file.split(".")[0] + "_result.txt")
    
    with open(outputpath, 'w') as textfile:
        textfile.writelines('Paragraph Analysis\n-----------------\n')
        textfile.writelines(f'Approximate Word Count: {word_count}\n')
        textfile.writelines(f'Approximate Sentence Count: {len(sentences)}\n')
        textfile.writelines(f'Average Letter Count: {average_letter_count}\n')
        textfile.writelines(f'Average Sentence Length: {average_sentence_length}\n')
        textfile.writelines('-----------------\n')
        
    with open(outputpath, "r") as readfile:
        print(readfile.read())    
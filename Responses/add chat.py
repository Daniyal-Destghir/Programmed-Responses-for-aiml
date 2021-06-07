
Question =input("Question: ")
Answer =input("Answer: ")

lines = ["<category>", "<pattern>", (Question), "</pattern>", (Answer), "</template>", "</category>"]
with open('Responses.txt', 'a') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
    

#<category>
#<pattern>
#QUESTION
#</pattern>
#<template>
#ANSWER
#</template>
#</category>

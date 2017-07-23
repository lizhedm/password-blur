# function to calculate levenshtein distance
def levenshtein(s, t):
        ''' From Wikipedia article; Iterative with two matrix rows. '''
        if s == t: return 0
        elif len(s) == 0: return len(t)
        elif len(t) == 0: return len(s)
        v0 = [None] * (len(t) + 1)
        v1 = [None] * (len(t) + 1)
        for i in range(len(v0)):
            v0[i] = i
        for i in range(len(s)):
            v1[0] = i + 1
            for j in range(len(t)):
                cost = 0 if s[i] == t[j] else 1
                v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
            for j in range(len(v0)):
                v0[j] = v1[j]
                
        return v1[len(t)]
print (levenshtein('startup','sTarfi$h'))
    
import csv

# set right answer list
typB_right_list = []
typC_right_list = []
file = open('right_answers.txt','r')
the_list = file.read().split('\n')
for row in the_list:
    right_answer_list = row.split(',')
    typB_right_list.append(right_answer_list[0])
    typC_right_list.append(right_answer_list[1])

# get users' answers from csv file
typB_list = []
typC_list = []
file = open('results-survey.csv', 'r', encoding = "ISO-8859-1")
readCSV = file.read()
row_list = readCSV.split('\n')
typB_distance_list = [[] for x in range(8)]
typC_distance_list = [[] for x in range(8)]
for i in range(8):
    for item in row_list:
        row_str_list = item.split(',')
        # claculate levenshtein distance
        # should we clean the empty str?
        #if row_str_list[6*i + 9] != '':
        typB_distance = levenshtein(row_str_list[6*i + 9],typB_right_list[i + 1])
        typB_distance_list[i].append(typB_distance)
        #if row_str_list[6*i + 10] != '':
        typC_distance = levenshtein(row_str_list[6*i + 10],typC_right_list[i + 1])
        typC_distance_list[i].append(typC_distance)
    print('distance of ' + typB_right_list[i + 1] + ':')
    print(typB_distance_list[i][1:])
    print('distance of ' + typC_right_list[i + 1] + ':')
    print(typC_distance_list[i][1:])



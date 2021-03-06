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

import csv
import pandas as pd

# get right answer list
df = pd.read_csv('right_answers.csv', encoding = "ISO-8859-1")
typB_right_list = df['TypB'].tolist()
typC_right_list = df['TypC'].tolist()
# split() works not well
# file = open('right_answers.csv','r')
# the_list = file.read().split('\n')
# for row in the_list:
#     right_answer_list = row.split(',')
#     typB_right_list.append(right_answer_list[0])
#     typC_right_list.append(right_answer_list[1])
# typB_right_list = typB_right_list[1:]
# typC_right_list = typC_right_list[1:]

# create a list of lists
typB_distance_list = [[] for x in range(8)]
typC_distance_list = [[] for x in range(8)]

# get users' answers from csv file
df = pd.read_csv('results-survey.csv', encoding = "ISO-8859-1")
df2 = df.copy()
for i in range(8):
    for index, row in df.iterrows():
        if pd.isnull(row[6*i + 9]):
            row[6*i + 9] = ''
#         if row[6*i + 9] != '':
        typB_distance = levenshtein(row[6*i + 9],typB_right_list[i])
        if typB_distance > len(typB_right_list[i]):
            typB_distance = len(typB_right_list[i])
#         this does not works, do not know why
#         if row[6*i + 9] != '':
#             df2.set_value(index,6*i + 9,typB_distance)
#             print(row[6*i + 9],df2.iloc[index][6*i + 9])
        if row[6*i + 9] == '':
            typB_distance = None
        typB_distance_list[i].append(typB_distance)
        
        if pd.isnull(row[6*i + 10]):
            row[6*i + 10] = ''
#         if row[6*i + 10] != '':
        typC_distance = levenshtein(row[6*i + 10],typC_right_list[i])
        if typC_distance > len(typC_right_list[i]):
            typC_distance = len(typC_right_list[i])
        if row[6*i + 10] == '':
            typC_distance = None
        typC_distance_list[i].append(typC_distance)
        
df2.colorhalftone6TypB = typB_distance_list[0]
df2.colorhalftone6TypC = typC_distance_list[0]
df2.colorhalftone5TypB = typB_distance_list[1]
df2.colorhalftone5TypC = typC_distance_list[1]
df2.crystallize8TypB = typB_distance_list[2]
df2.crystallize8TypC = typC_distance_list[2]
df2.crystallize7TypB = typB_distance_list[3]
df2.crystallize7TypC = typC_distance_list[3]
df2.gauss8TypB = typB_distance_list[4]
df2.gauss8TypC = typC_distance_list[4]
df2.gauss75TypB = typB_distance_list[5]
df2.gauss75TypC = typC_distance_list[5]
df2.mosaik11TypB = typB_distance_list[6]
df2.mosaik11TypC = typC_distance_list[6]
df2.mosaik10TypB = typB_distance_list[7]
df2.mosaik10TypC = typC_distance_list[7]
#     print('\ndistance of ' + typB_right_list[i] + ':\n', typB_distance_list[i][:], 
#           '\ndistance of ' + typC_right_list[i] + ':\n', typC_distance_list[i][:])

df2.to_csv('results-survey-after-calculated.csv',sep=',', encoding='ISO-8859-1')
    
# split() works not well
# for i in range(8):
#     for item in row_list:
#         row_str_list = item.split(',')
# #         print(len(row_str_list))
#         # claculate levenshtein distance
#         # clean the empty string
#         if row_str_list[6*i + 9] != '':
#             typB_distance = levenshtein(row_str_list[6*i + 9],typB_right_list[i])
#             typB_str = '(' + row_str_list[6*i + 9] + ',' + typB_right_list[i] + ')' + str(typB_distance)
#             typB_distance_list[i].append(typB_str)
#         if row_str_list[6*i + 10] != '':
#             typC_distance = levenshtein(row_str_list[6*i + 10],typC_right_list[i])
#             typC_distance_list[i].append(typC_distance)
#     print('distance of ' + typB_right_list[i] + ':')
#     print(typB_distance_list[i][1:])
#     print('distance of ' + typC_right_list[i] + ':')
#     print(typC_distance_list[i][1:])

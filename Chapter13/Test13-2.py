import pandas
score = pandas.read_csv('score2.csv', encoding='utf-8')
print(score[score['Japanese'] >= 95])
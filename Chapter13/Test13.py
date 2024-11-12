import numpy
score = numpy.loadtxt('score.csv', delimiter=',')
print(score[score[:, 2] >= 95])
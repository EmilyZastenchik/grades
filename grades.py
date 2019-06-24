quiz = {1:10, 2:9, 3:10}
test = {1:95, 2:87, 3:90}

def avg(sum, count):
    return sum /count
quizSum = 0
testSum = 0
for i in quiz:
    quizSum += quiz[i]*10
    #quiz out of 10pts
for j in test:
    testSum += test[j]
testSum += avg(quizSum,i)
print(round(avg(quizSum,i)))
print(round(avg(testSum,j+1),2))



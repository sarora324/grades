numberItems = 3
score1 = [.15, 3, 75]
score2 = [.4, 2, 90]
score3 = [.45, 3, 95]

def scoreCalc(percentage, numberItems, score):
  x = (percentage/numberItems) * score
  return x

score_list = [score1,score2,score3]

for score in score_list:
    test = scoreCalc(score[0],score[1],score[2])
    print(test)

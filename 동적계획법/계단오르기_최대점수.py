
stairs = int(input("계단 총 개수 : "))
scores = [0]
for i in range(stairs):
    scores.append(int(input("{0}번째 계단의 점수 : ".format(i+1))))
score = 0
check = 0
dp = [0 for i in range(stairs+3)]
dpi = 0
i =1


dp[1] = scores[1]
dp[2] = scores[1] + scores[2]
if scores[2]+scores[3] > scores[1] + scores[3]:
    dp[3] = scores[2] + scores[3]
else:
    dp[3] = scores[1] + scores[3]

for i in range(4, stairs+1):
    dp[i]=max(scores[i]+scores[i-1]+dp[i-3], scores[i]+dp[i-2])

print(dp)
#print("최댓값 : {0}".format(count(0, scores, score, check)))
#6= 1+1+1+1+1+1
#=1+1+2+2
#=1+1+1+1+2
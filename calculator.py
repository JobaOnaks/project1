#grading in a school system based on score
score = int(input('Enter your score: '))
if 45<= score < 50:
    print('D')
elif 50<= score <60:
    print('C')
elif 60<= score <70:
    print('B')
elif score >= 70:
    print('A')
else:
    print('F')
def quiz(q,a):
    s=0
    for j in range(len(q)):
      print(f'question {j} : {q[j]}')
      i=input('enter the answer(0 to stop): ')
      if i=='0':
          break
      elif i.lower()==a[j]:
          s=s+1
          print('right answer\nyour score is: ',s)
      else:
          print('wrong answer. your total score is',s)

def qa():
    inp=input('enter question : ')
    with open('questions.txt','a') as f:
        f.write(','+inp) 
    inp=input('enter answer : ')
    with open('answers.txt','a') as f1:
        f1.write(','+inp)
def loaddata():
    with open('questions.txt','r') as f:
        q=f.read().split(',')
    
    with open('answers.txt','r') as f1:
        a=f1.read().split(',')
    return q,a
q,a=loaddata()
while True:
    inp1=int(input('1.quiz  or 2.write questions and answers(0 to stop): '))
    if inp1==0:
        break
    elif inp1==1:
        quiz(q,a)
    elif inp1==2:
        passwd=input('enter password : ')
        if passwd=='momin0000':
            qa()
            print('(ques. and ans. saved successfully)')
        else:
            print('wrong password, ask\nhttps://www.facebook.com/profile.php?id=100044047537257\nfor password') 
    else:
        print('please choose 1 or 2 or 0')
print('.\n.\nthanks for playing my quiz:)\n.\ncreated by >> momin')

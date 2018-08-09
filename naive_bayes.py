fr=open('file.txt','r')
total_entries=14
buy_comp,age,income,student,credit=[],[],[],[],[]
for lines in fr:
    second =((lines.split()))
    buy_comp.append(second[0])
    age.append(second[1])
    income.append(second[2])
    student.append(second[3])
    credit.append(second[4])
buy_comp.pop(0)
age.pop(0)
income.pop(0)
student.pop(0)
credit.pop(0)
yes=buy_comp.count('yes')
no=buy_comp.count('no')
def prob (buy):
    yes_prob=yes/total_entries
    no_prob=no/total_entries
    return yes_prob,no_prob
probility= list(prob(buy_comp))
comp_age= list(zip(buy_comp,age))
def age30(tuple1):
    a=tuple1.count(('yes','<=30'))
    b=tuple1.count(('no','<=30'))
    return a/yes,b/no
def age31_(tuple1):
    a=tuple1.count(('yes','31-40'))
    b=tuple1.count(('no','31-40'))
    return a/yes,b/no
def age40(tuple1):
    a=tuple1.count(('yes','>40'))
    b=tuple1.count(('no','>40'))
    return a/yes,b/no
comp_income=list(zip(buy_comp,income))
def medium(tuple2):
    a=tuple2.count(('yes','medium'))
    b=tuple2.count(('no','medium'))
    return a/yes,b/no
def low(tuple2):
    a=tuple2.count(('yes','low'))
    b=tuple2.count(('no','low'))
    return a/yes,b/no
def high(tuple2):
    a=tuple2.count(('yes','high'))
    b=tuple2.count(('no','high'))
    return a/yes,b/no
comp_stud=list(zip(buy_comp,student))
def y_stud(tuple3):
    a=tuple3.count(('yes','yes'))
    b=tuple3.count(('no','yes'))
    return a/yes,b/no 
def n_stud(tuple3):
    a=tuple3.count(('yes','no'))
    b=tuple3.count(('no','no'))
    return a/yes,b/no
comp_credit=list(zip(buy_comp,credit))
def exc_cred(tuple4):
    a=tuple4.count(('yes','excellent'))
    b=tuple4.count(('no','excellent'))
    return a/yes,b/no
def fair_cred(tuple4):
    a=tuple4.count(('yes','fair'))
    b=tuple4.count(('no','fair'))
    return a/yes,b/no
age=int(input("Enter Your Age = "))
income=input("Enter your income = ")
student=input("Are You a Student = ")
credit=input("Enter your Credit Rating = ")
def cal_age(age):
    if(age<=30):
        y,n=(age30(comp_age))
        return y,n
    elif(age>30 and age <=40):
        y,n=(age31_(comp_age))
        return y,n
    elif(age>40):
        y,n=(age40(comp_age))
        return y,n
def cal_income(income):
    if(income=='high'):
        y,n=(high(comp_income))
        return y,n
    elif(income=='medium'):
        y,n=(medium(comp_income))
        return y,n
    elif(income=='low'):
        y,n=(low(comp_income))
        return y,n
def cal_status(student):
    if(student=='yes'):
        y,n=(y_stud(comp_stud))
        return y,n
    elif(student=='no'):
        y,n=(n_stud(comp_stud))
        return y,n
def cal_credit(credit):
    if(credit=='excellent'):
        y,n=(exc_cred(comp_credit))
        return y,n
    elif(credit=='fair'):
        y,n=(fair_cred(comp_credit))
        return y,n
prob1=list(cal_age(age))
prob2=list(cal_income(income))
prob3=list(cal_status(student))
prob4=list(cal_credit(credit))
p_yes=prob1[0]*prob2[0]*prob3[0]*prob4[0]
p_no=prob1[1]*prob2[1]*prob3[1]*prob4[1]
final1=p_yes*probility[0]
final2=p_no*probility[1]
if final1>final2:
    print("YES CUSTOMER WILL BUY A COMPUTER")
else:
    print("NO CUSTOMER WILL NOT BUY A COMPUTER")












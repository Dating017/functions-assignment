def oddeven(*numb):
    evenlist=[n for n in numb if n%2==0]
    oddlist=[n for n in numb if n%2==1]
    return f'evennumbers:{evenlist} oddnumbers: {oddlist}'

value=oddeven(1,2,3,4,5,6,7,8,9,10,11,12,13)
print(value)    
n = eval(input("input a four-digit number"))
digit_1 = int(n%10000/1000)
digit_2 = int(n%1000/100)
digit_3 = int(n%100/10)
digit_4 = int(n%10/1)

digit_1 = (digit_1 + 5)%10
digit_2 = (digit_2 + 5)%10
digit_3 = (digit_3 + 5)%10
digit_4 = (digit_4 + 5)%10

c=1000*digit_4+100*digit_3+10*digit_2+ digit_1

print(c)

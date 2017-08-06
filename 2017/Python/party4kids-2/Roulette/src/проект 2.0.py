from random import*
cash=1000
while cash>0:
    print()
    print('у вас есть: ',cash,'$')
    change=int(input('выберите цифру от 1 до 20: '))
    hod=int(input('сколько денег ставите, но не менше 10: '))
    if cash>=hod:
         win_number=randint(1,21)
         print('выиграло число: ', win_number)
         if win_number==change:
             print("ТЫ ВЫИГРАЛ!")
             cash=hod*15+cash
         else:
            print("УПС...")
            cash=cash-hod
    else:
        print("у вас недостаточно денег")
     
print('денег нет - ИДИ РАБОТАЙ!!!!')
    
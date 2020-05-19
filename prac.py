def theintrestfuntion():   
    print('intrest calculator')
    amount = float(input('Intail amount \n'))
    roi = float(input('Rate of intreste \n'))
    yrs  = int(input('Number of years  \n ' ))
    total  = (amount*pow(1+(roi/100),yrs))
    intrerst = total - amount
    print ('\n \t The total of the investmet = R %0.2f'%total)
    print('\n  \t Intrerest = R %0.2f ' %intrerst)
    


theintrestfuntion()

def month(a,language="русский"):
    monr = {1:'Январь',2:'Февраль' ,3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь', 7:'Июль',8: 'Август',9: 'Сентябрь',11: 'Ноябрь', 10:'Октябрь',12: 'Декабрь'}
    mone = {1:'January',2:'February' ,3:'March', 4:'April', 5:'May', 6:'June', 7:'July',8: 'August',9: 'September',11: 'November', 10:'October',12: 'December'}
    
    if language == 'русский':
        return monr[a]
    else:
        return mone[a]
        
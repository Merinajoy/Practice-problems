import datetime

def compare_date(date1):
    date2 = datetime.datetime.now()
    date1 = datetime.datetime.strptime(date1, '%d-%m-%Y')
    a = date2 - date1
    print(a.days, 'days')

s ='01-01-2021'
compare_date(s)

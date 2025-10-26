from datetime import date
ageIoana = date.today()-date(2001,1,7)
ageAndrei = date.today()-date(2000,11,5)
print(ageIoana.days)
print(ageAndrei.days)
print(abs(ageIoana-ageAndrei))
print(date.today())
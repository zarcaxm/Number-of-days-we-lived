__author__ = 'zarcaxm'
import datetime


userinfo=input("When did u born?(dd/mm/yyyy)")
#convert userinfo
bday = datetime.datetime.strptime(userinfo,"%d/%m/%Y").date()
today = datetime.date.today()
days = today - bday
print(days)

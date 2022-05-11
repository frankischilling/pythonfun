import datetime as obj_dt

bday = obj_dt.datetime(2004, 7, 29)
datenow = obj_dt.datetime.now()
birthday = datenow - bday 

print(birthday*86400)
# birday.days * 86400

# birhtday.days = 365
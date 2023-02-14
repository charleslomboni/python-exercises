import datetime

x = datetime.datetime.now()

print(f'The Date: {x.strftime("%d")}')
print(f'Day: {x.strftime("%A")}')
print(f'Year: {x.year}')

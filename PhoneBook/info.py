import csv
users=[
    ('personName', 'phoneNumber'),
    ['Bishimbayev', 'GadalkaNumber'],
    ['Nukenova', 'JusticePeace']
]
with open(r'C:\Users\ADMIN\OneDrive\Рабочий стол\azamat\lab10\fil.csv', 'w', newline='') as f:
    writer=csv.writer(f)
    writer.writerows(users)

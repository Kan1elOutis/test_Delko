import calendar
def calendars():
    mounths = {1: "Января",
               2: "Ферваля",
               3: "Марта",
               4: "Апреля",
               5: "Мая",
               6: "Июня",
               7: "Июля",
               8: "Августа",
               9: "Сентября",
               10: "Октября",
               11: "Ноября",
               12: "Декабря"
               }
    cl = calendar.Calendar()
    for number_of_mounth in range(1, len(mounths) + 1):
        rez = cl.itermonthdays(2023, number_of_mounth)
        for day in rez:
            if day != 0:
                yield f'{day} {mounths[number_of_mounth]}'


test = calendars()
for i in range(366):
    print(next(test))


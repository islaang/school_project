import calendar

def event_calendar():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    
    print(f"\nКалендарь на {calendar.month_name[month]} {year} года:")
    print(calendar.month(year, month))
    
    events = {}
    
    while True:
        date = input("Введите дату для добавления события (дд.мм) или 'выход' для завершения: ")
        if date.lower() == 'выход':
            break
        event = input("Введите описание события: ")
        events[date] = event
    
    print("\nСобытия на выбранный месяц:")
    for date, event in events.items():
        print(f"{date}: {event}")

event_calendar()

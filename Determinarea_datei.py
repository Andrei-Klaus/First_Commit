from datetime import datetime, timedelta

def get_calendar_date(year, day):
    start_date = datetime(year, 1, 1)
    target_date = start_date + timedelta(days=day-1)
    print(target_date.year)
    return target_date.year, target_date.month, target_date.day


print(get_calendar_date(2025, 300))
print(get_calendar_date(2026, 300))
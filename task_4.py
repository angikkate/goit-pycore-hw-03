from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    in_seven_days = today + timedelta(days=7)

    result = []

    for user in users:
        # Convert string birthday to date object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Replace year with current year
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday already passed this year, use next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Check if birthday is in the next 7 days
        if today <= birthday_this_year <= in_seven_days:
            congratulation_date = birthday_this_year

            # If weekend, move to next Monday
            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            # Add result in desired format
            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result

users = [
    {"name": "John Doe", "birthday": "1985.06.13"},
    {"name": "Jane Smith", "birthday": "1990.06.20"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

from datetime import datetime

def get_days_from_today(date):

    try:
        datetime_object = datetime.strptime(date, "%Y-%m-%d") # Create datetime object
        current_date = datetime.today()  # To get current date
        delta_day = current_date - datetime_object  # Difference between two dates

        return delta_day.days
    except ValueError: 
        return "Invalid date format. Enter date in 'YYYY-MM-DD' format."

get_days_from_today('2024-12-05')
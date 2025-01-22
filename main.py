from datetime import datetime, timedelta
import random
import re

def get_days_from_today(date: str)-> int:
    """
    Calculate the difference between the given date and today date.

    Parameters:
    date (str): Date in the format 'YYYY-MM-DD'.

    Returns:
    int: Difference in days.
    """
    try:
        new_date: datetime = datetime.strptime(date, "%Y-%m-%d")
        now_date: datetime = datetime.today()
        result: timedelta = now_date - new_date
        return result.days
    except ValueError:
        print(f"Error: Invalid date format. Please use 'YYYY-MM-DD'. Input was: {date}")
        return None

print(get_days_from_today('10-09-2000'))





def get_numbers_ticket(min: int, max: int, quantity: int)-> list:
    """
    Return a list of random numbers in given range.

    Parameters:
    min (int): Lower bound of the range.
    max (int): Upper bound of the range.
    quantity (int): Quantity of random numbers to generate.

    Returns:
    list: List of random numbers.
    """
    if min > 0 and max < 1001 and min < max and 0 < quantity <= (max - min + 1):
        return [random.randint(min, max) for _ in range(quantity)]
    else:
        return []


lottery_numbers: list = get_numbers_ticket(-1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)



def normalize_phone(phone_number: str)-> str:
    """
    Return a normalized phone number.

    Parameters:
    phone_number (str): Phone number to normalize.

    Returns:
    str: Normalized phone number.
    """
    only_digits: str = re.sub(r"\D", "", phone_number)

    if only_digits.startswith("380"):
        only_digits = "+" + only_digits
    elif only_digits.startswith("0"):
        only_digits = "+38" + only_digits

    return only_digits






raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers: list = [normalize_phone(num) for num in raw_numbers]


print(sanitized_numbers)

def days_since_birth(birthday):
    """
    Calculates how many days have passed since the day you were born,
    excluding the birth year and the current year, while considering leap years.

    :param birthday: A string in the format "DD-MM-YYYY"
    :return: Number of days passed (whole years only)
    """
    # Extract the birth year
    birth_year = int(birthday[-4:])  # Last 4 characters represent the year

    # Ask the user for the current year
    current_year = int(input("Enter the current year: "))

    # Count only full years in between
    full_years = current_year - birth_year - 1

    # Count leap years
    leap_years = 0
    for year in range(birth_year + 1, current_year):  # Exclude birth and current year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1

    # Calculate total days (normal years + leap years)
    total_days = (full_years * 365) + (leap_years * 1)

    return total_days


# Example usage:
print(days_since_birth("03-07-2005"))
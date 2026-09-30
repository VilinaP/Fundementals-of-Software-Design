# Date class
# Prof. O & CPTR-215
# 2025-09-25


"""Date class
Represents a particular day in the Gregorian calendar.


We want to be able to:
0. Initialize a date with a given year, month, and day
1. Display a date ("October 31, 2019")
2. Determine the day of the week a date falls on (2025-09-25 is a Thursday)
3. Determine whether a date is within a leap year (2025-09-25 is NOT, but 2024-09-25 WAS)


We could store the date internally as:
1. A single string ("October 31, 2019")
2. 3 integers (year, month, day)
3. A list (or dictionary, or tuple) of 3 integers {'year': 2024 ...}
4. A single integer - the distance from some defined starting point in some unit (days since January 1, 1970)
"""


class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
    def display(self):
        """Print this date out in Mmm d, yyyy format
        >>> Date(2025, 9, 25).display()
        Sep 25, 2025
        >>> Date(1844, 10, 22).display()
        Oct 22, 1844
        """
        month_names = "NONE Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
        print(f"{month_names[self.month]} {self.day}, {self.year}")
    def day_of_week(self):
        """Determine the day of the week this date falls on (1 = Sun, 7 = Sat).
        >>> Date(2025, 9, 25).day_of_week()
        5
        >>> tomorrow = Date(2025, 9, 26)
        >>> tomorrow.day_of_week()
        6
        """
        month, year = self.month, self.year
        if month < 3:
            month += 12
            year -= 1
        dow = (self.day + (13 * (month + 1) // 5) + year + year // 4 - year // 100 + year // 400) % 7
        return 7 if dow == 0 else dow
    def is_leap_year(self) -> bool:
        '''Takes the year and checks if it's a leap year
        >>> Date(2024, 4, 1).is_leap_year()
        True
        >>> Date(2000, 4, 2).is_leap_year()
        True
        >>> Date(1900, 4, 3).is_leap_year()
        False
        >>> Date(2025 , 4, 3).is_leap_year()
        False
        '''
        return self.year % 4 == 0 and self.year%100 != 0 or self.year%400 == 0
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    today = Date(2025, 9, 25)
    today.display()
    Date.display(today) # don't do it this way, just an example
    print(today.is_leap_year())

class Solution:
    def dayOfYear(self, date: str) -> int:
        # define dictionary for the number of days in each month
        days_in_month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10: 31, 11:30, 12:31}
        
        # represent year, month and day as int
        year = 1000*int(date[0])+100*int(date[1])+10*int(date[2])+int(date[3])
        month = 10*int(date[5])+int(date[6])
        day = 10*int(date[8])+int(date[9])
        
        # sum days from previous months
        day_of_year = 0
        for i in range(1,month):
            day_of_year += days_in_month_dict[i]
        
        # include days from current month
        day_of_year += day
        
        # handle leap years
        if year%4 == 0 and month >= 3 and year != 1900:
            day_of_year += 1
        
        # return the day number of the year
        return day_of_year
        
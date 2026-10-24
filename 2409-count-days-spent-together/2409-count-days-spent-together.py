class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def dateToDayOfYear(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            return sum(days_in_months[:month - 1]) + day

        # Find the start and end of the overlapping period
        start_date = max(arriveAlice, arriveBob)
        end_date = min(leaveAlice, leaveBob)

        # Convert to day of year
        start_day = dateToDayOfYear(start_date)
        end_day = dateToDayOfYear(end_date)

        # Return the overlap length
        return max(0, end_day - start_day + 1)
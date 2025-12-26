class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        # of N's BEFORE + # of Y's AFTER
        """
        n = len(customers)
        total_y = customers.count("Y")
        minimum_penalty = total_y
        earliest_hour = 0
        n_before = 0
        for i, c in enumerate(customers):
            n_before += c == "N"
            y_after = total_y - (i+1 - n_before)

            if n_before + y_after < minimum_penalty:
                earliest_hour = i+1
                minimum_penalty = n_before + y_after
    
        return earliest_hour

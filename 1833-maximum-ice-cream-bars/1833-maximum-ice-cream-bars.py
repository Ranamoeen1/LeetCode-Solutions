class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Find the maximum cost to define the size of our frequency array
        max_cost = max(costs)
        
        # Create a frequency array to store the count of each ice cream price
        # Index represents the cost, value represents the frequency
        frequency = [0] * (max_cost + 1)
        for cost in costs:
            frequency[cost] += 1
            
        ice_cream_count = 0
        
        # Iterate through all possible costs from 1 to max_cost
        for price in range(1, max_cost + 1):
            if frequency[price] == 0:
                continue
                
            # If we can't even afford one ice cream at this price, we are done
            if coins < price:
                break
                
            # Calculate how many ice creams of this price we want vs how many we can afford
            count_to_buy = min(frequency[price], coins // price)
            
            # Deduct the cost and update our total count
            coins -= count_to_buy * price
            ice_cream_count += count_to_buy
            
        return ice_cream_count
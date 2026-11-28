class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        # Count occurrences of each factor (1 <= factor_i <= n)
        freq = [0] * (n + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        # Calculate how many items have a factor divisible by f
        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            for mult in range(f, n + 1, f):
                multiples[f] += freq[mult]
                
        # Group available 2-item bundles by price: (price, max_available_copies)
        bundles = []
        min_single_price = float('inf')
        
        for factor, price in items:
            if price < min_single_price:
                min_single_price = price
            
            valid_targets = multiples[factor] - 1
            if valid_targets > 0:
                bundles.append((price, valid_targets))
                
        # Sort 2-item bundles by price ascending
        bundles.sort()
        
        # Baseline: spend entire budget on the single cheapest item (1 item per purchase)
        max_items = budget // min_single_price
        
        spent = 0
        items_from_bundles = 0
        
        # Greedily take 2-item bundles and fill remaining budget with 1-item purchases
        for price, count in bundles:
            if spent + price > budget:
                break
                
            # Maximum copies of this bundle we can afford
            can_buy = min(count, (budget - spent) // price)
            
            # Test taking `can_buy` copies
            spent_full = spent + can_buy * price
            items_full = items_from_bundles + can_buy * 2
            max_items = max(max_items, items_full + (budget - spent_full) // min_single_price)
            
            # Also test taking `can_buy - 1` copies in case leaving `price` budget 
            # allows buying more 1-item copies (when price >= 2 * min_single_price)
            if can_buy > 1:
                spent_prev = spent + (can_buy - 1) * price
                items_prev = items_from_bundles + (can_buy - 1) * 2
                max_items = max(max_items, items_prev + (budget - spent_prev) // min_single_price)
                
            spent = spent_full
            items_from_bundles = items_full
            
            # If we couldn't buy all available copies of this bundle, we can't afford any more
            if can_buy < count:
                break
                
        return max_items
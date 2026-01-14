class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        x_coords = set()
        events = []
        
        # 1. Collect all boundary coordinates
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
            # Event: (y-coordinate, type, left_x, right_x)
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        # Sort X for coordinate compression
        sorted_x = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        num_intervals = len(sorted_x) - 1
        tree_cnt = [0] * (4 * num_intervals)
        tree_len = [0.0] * (4 * num_intervals)
        node_range_len = [0.0] * (4 * num_intervals)
        
        def build(v, tl, tr):
            if tl == tr:
                node_range_len[v] = float(sorted_x[tl + 1] - sorted_x[tl])
            else:
                tm = (tl + tr) // 2
                build(2 * v, tl, tm)
                build(2 * v + 1, tm + 1, tr)
                node_range_len[v] = node_range_len[2 * v] + node_range_len[2 * v + 1]
        
        build(1, 0, num_intervals - 1)
        
        def update(v, tl, tr, l, r, add):
            if l <= tl and tr <= r:
                tree_cnt[v] += add
            else:
                tm = (tl + tr) // 2
                if l <= tm:
                    update(2 * v, tl, tm, l, r, add)
                if r > tm:
                    update(2 * v + 1, tm + 1, tr, l, r, add)
            
            # Logic for Union Area: if count > 0, the whole range is covered
            if tree_cnt[v] > 0:
                tree_len[v] = node_range_len[v]
            elif tl < tr:
                tree_len[v] = tree_len[2 * v] + tree_len[2 * v + 1]
            else:
                tree_len[v] = 0.0

        # 3. Sweep Line through Y-coordinates
        events.sort()
        durations = [] 
        total_area = 0.0
        last_y = events[0][0]
        
        for y, delta, x1, x2 in events:
            if y > last_y:
                current_width = tree_len[1]
                total_area += current_width * (y - last_y)
                durations.append((current_width, y - last_y, last_y))
            
            update(1, 0, num_intervals - 1, x_map[x1], x_map[x2] - 1, delta)
            last_y = y
        
        # 4. Find the Y-coordinate that splits the total area in half
        target_area = total_area / 2.0
        current_acc_area = 0.0
        
        for width, dy, y_start in durations:
            if width > 0:
                if current_acc_area + width * dy >= target_area - 1e-9:
                    return float(y_start + (target_area - current_acc_area) / width)
                current_acc_area += width * dy
            else:
                # If width is 0, we are in a gap between squares
                if current_acc_area >= target_area - 1e-9:
                    return float(y_start)
            
        return float(last_y)
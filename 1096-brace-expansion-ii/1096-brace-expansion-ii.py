class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expr(idx: int) -> tuple[set[str], int]:
            # Each expression level is a union of comma-separated terms.
            # R({e1, e2, ...}) = R(e1) U R(e2) U ...
            res_set = set()
            cur_term = {""}  # Start with an empty string for cartesian product concatenation

            while idx < len(expression):
                char = expression[idx]

                if char == '{':
                    # Parse nested expression inside braces
                    sub_set, idx = parse_expr(idx + 1)
                    # Concatenate (Cartesian Product) with current term
                    cur_term = {a + b for a in cur_term for b in sub_set}
                elif char == '}':
                    # End of current brace group
                    res_set.update(cur_term)
                    return res_set, idx + 1
                elif char == ',':
                    # Union boundary: collect current term and reset for the next option
                    res_set.update(cur_term)
                    cur_term = {""}
                    idx += 1
                else:
                    # Single lowercase character
                    cur_term = {a + char for a in cur_term}
                    idx += 1

            res_set.update(cur_term)
            return res_set, idx

        res, _ = parse_expr(0)
        return sorted(list(res))
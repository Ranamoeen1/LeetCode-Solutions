class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t into 2, 3, 5, and 7
        t2 = t3 = t5 = t7 = 0
        temp_t = t
        for p in (2, 3, 5, 7):
            c = 0
            while temp_t % p == 0:
                c += 1
                temp_t //= p
            if p == 2:
                t2 = c
            elif p == 3:
                t3 = c
            elif p == 5:
                t5 = c
            elif p == 7:
                t7 = c

        # Prime factors other than 2, 3, 5, 7 cannot be formed by single digits
        if temp_t > 1:
            return "-1"

        # Factor contributions for digits 1..9: (f2, f3, f5, f7)
        DIGIT_FACTORS = [
            (0, 0, 0, 0),  # 0 (unused)
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        def get_suffix_digits(rc2: int, rc3: int, rc5: int, rc7: int) -> list:
            """Returns the lexicographically smallest sorted list of digits

            needed to satisfy remaining factor requirements.
            """
            rc2, rc3, rc5, rc7 = (
                max(0, rc2),
                max(0, rc3),
                max(0, rc5),
                max(0, rc7),
            )

            best_digits = None
            best_key = (float("inf"), "")

            # Iterate over the count of '6's (combining one 2 and one 3)
            max_k = min(rc2, rc3)
            for k in range(max_k + 1):
                rem2 = rc2 - k
                rem3 = rc3 - k

                c8, r2 = divmod(rem2, 3)
                c9, r3 = divmod(rem3, 2)

                digits = [6] * k + [8] * c8 + [9] * c9
                if r2 == 2:
                    digits.append(4)
                elif r2 == 1:
                    digits.append(2)

                if r3 == 1:
                    digits.append(3)

                digits.extend([5] * rc5)
                digits.extend([7] * rc7)
                digits.sort()

                key = (len(digits), "".join(map(str, digits)))
                if key < best_key:
                    best_key = key
                    best_digits = digits

            return best_digits if best_digits is not None else []

        n = len(num)
        first_zero = num.find("0")

        # Step 2: Precompute prefix factor counts up to the first zero (if any)
        pref2, pref3, pref5, pref7 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        limit = n if first_zero == -1 else first_zero

        for k in range(limit):
            f2, f3, f5, f7 = DIGIT_FACTORS[int(num[k])]
            pref2[k + 1] = pref2[k] + f2
            pref3[k + 1] = pref3[k] + f3
            pref5[k + 1] = pref5[k] + f5
            pref7[k + 1] = pref7[k] + f7

        # Step 3: Check if num itself is valid
        if first_zero == -1:
            if (
                pref2[n] >= t2
                and pref3[n] >= t3
                and pref5[n] >= t5
                and pref7[n] >= t7
            ):
                return num

        # Step 4: Search right-to-left for the first valid (i, d) replacement
        start_i = n - 1 if first_zero == -1 else first_zero

        for i in range(start_i, -1, -1):
            c2_pref, c3_pref, c5_pref, c7_pref = (
                pref2[i],
                pref3[i],
                pref5[i],
                pref7[i],
            )
            start_d = 1 if (first_zero != -1 and i == first_zero) else int(num[i]) + 1

            for d in range(start_d, 10):
                f2, f3, f5, f7 = DIGIT_FACTORS[d]
                rc2 = t2 - (c2_pref + f2)
                rc3 = t3 - (c3_pref + f3)
                rc5 = t5 - (c5_pref + f5)
                rc7 = t7 - (c7_pref + f7)

                suffix_digits = get_suffix_digits(rc2, rc3, rc5, rc7)
                rem_len = n - 1 - i

                if len(suffix_digits) <= rem_len:
                    ones_count = rem_len - len(suffix_digits)
                    suffix_str = "1" * ones_count + "".join(
                        map(str, suffix_digits)
                    )
                    return num[:i] + str(d) + suffix_str

        # Step 5: If no valid number of length n exists, expand to length > n
        min_s_digits = get_suffix_digits(t2, t3, t5, t7)
        target_len = max(n + 1, len(min_s_digits))
        ones_count = target_len - len(min_s_digits)

        return "1" * ones_count + "".join(map(str, min_s_digits))
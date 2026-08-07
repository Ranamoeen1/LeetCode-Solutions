class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        # Prime factorize t into 2, 3, 5, and 7
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

        # If t has prime factors other than 2, 3, 5, 7, it's impossible
        if temp_t > 1:
            return "-1"

        # Factor contributions for digits 1..9
        DIGIT_FACTORS = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        def min_digits(rc2, rc3, rc5, rc7):
            """Calculates minimum digits needed to achieve at least required factor counts."""
            if rc2 <= 0 and rc3 <= 0 and rc5 <= 0 and rc7 <= 0:
                return 0
            rc2 = max(0, rc2)
            rc3 = max(0, rc3)
            rc5 = max(0, rc5)
            rc7 = max(0, rc7)

            ans = rc5 + rc7
            min_23 = float("inf")
            max_k = min(rc2, rc3)

            # Try using k sixes (which cover one 2 and one 3 each)
            for k in range(max_k + 1):
                rem3 = rc3 - k
                rem2 = rc2 - k
                d3 = (rem3 + 1) // 2 if rem3 > 0 else 0
                d2 = (rem2 + 2) // 3 if rem2 > 0 else 0
                min_23 = min(min_23, k + d3 + d2)

            return ans + min_23

        n = len(num)
        first_zero = num.find("0")

        # Precompute prefix factor counts
        pref2 = [0] * (n + 1)
        pref3 = [0] * (n + 1)
        pref5 = [0] * (n + 1)
        pref7 = [0] * (n + 1)

        limit = n if first_zero == -1 else first_zero
        for k in range(limit):
            d_val = int(num[k])
            f2, f3, f5, f7 = DIGIT_FACTORS[d_val]
            pref2[k + 1] = pref2[k] + f2
            pref3[k + 1] = pref3[k] + f3
            pref5[k + 1] = pref5[k] + f5
            pref7[k + 1] = pref7[k] + f7

        # Check if num itself is valid
        if first_zero == -1:
            if (
                pref2[n] >= t2
                and pref3[n] >= t3
                and pref5[n] >= t5
                and pref7[n] >= t7
            ):
                return num

        # Search for valid number of length n by changing digit at index i
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
                rc2 = max(0, t2 - (c2_pref + f2))
                rc3 = max(0, t3 - (c3_pref + f3))
                rc5 = max(0, t5 - (c5_pref + f5))
                rc7 = max(0, t7 - (c7_pref + f7))

                rem_len = n - 1 - i
                if min_digits(rc2, rc3, rc5, rc7) <= rem_len:
                    # Construct smallest valid suffix greedily
                    ans_list = [num[:i], str(d)]
                    curr_c2 = c2_pref + f2
                    curr_c3 = c3_pref + f3
                    curr_c5 = c5_pref + f5
                    curr_c7 = c7_pref + f7

                    for j in range(rem_len):
                        rem_pos = rem_len - 1 - j
                        for sd in range(1, 10):
                            sf2, sf3, sf5, sf7 = DIGIT_FACTORS[sd]
                            n_rc2 = max(0, t2 - (curr_c2 + sf2))
                            n_rc3 = max(0, t3 - (curr_c3 + sf3))
                            n_rc5 = max(0, t5 - (curr_c5 + sf5))
                            n_rc7 = max(0, t7 - (curr_c7 + sf7))

                            if min_digits(n_rc2, n_rc3, n_rc5, n_rc7) <= rem_pos:
                                ans_list.append(str(sd))
                                curr_c2 += sf2
                                curr_c3 += sf3
                                curr_c5 += sf5
                                curr_c7 += sf7
                                break

                    return "".join(ans_list)

        # If length n is not possible, construct for length target_len > n
        target_len = max(n + 1, min_digits(t2, t3, t5, t7))
        ans_list = []
        curr_c2 = curr_c3 = curr_c5 = curr_c7 = 0

        for j in range(target_len):
            rem_pos = target_len - 1 - j
            for sd in range(1, 10):
                sf2, sf3, sf5, sf7 = DIGIT_FACTORS[sd]
                n_rc2 = max(0, t2 - (curr_c2 + sf2))
                n_rc3 = max(0, t3 - (curr_c3 + sf3))
                n_rc5 = max(0, t5 - (curr_c5 + sf5))
                n_rc7 = max(0, t7 - (curr_c7 + sf7))

                if min_digits(n_rc2, n_rc3, n_rc5, n_rc7) <= rem_pos:
                    ans_list.append(str(sd))
                    curr_c2 += sf2
                    curr_c3 += sf3
                    curr_c5 += sf5
                    curr_c7 += sf7
                    break

        return "".join(ans_list)
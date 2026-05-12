class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by (minimum - actual) in descending order
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:
            # If current energy is less than required minimum,
            # increase initial energy
            if current < minimum:
                energy += (minimum - current)
                current = minimum

            # Perform the task
            current -= actual

        return energy
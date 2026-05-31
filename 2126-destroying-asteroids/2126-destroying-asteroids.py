class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Sort the asteroids to always absorb the smallest ones first
        asteroids.sort()
        
        for asteroid in asteroids:
            # If the planet is too small, it gets destroyed
            if mass < asteroid:
                return False
            # Otherwise, the planet absorbs the asteroid's mass
            mass += asteroid
            
        return True
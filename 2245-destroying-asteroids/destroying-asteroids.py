class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        curr = mass
        asteroids.sort()
        
        for value in asteroids:
            if (value<=curr):
                curr+=value
            else:
                return False

        return True
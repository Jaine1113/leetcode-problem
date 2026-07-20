class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        for charge in gain:
            altitude += charge 
            highest = max(highest, altitude)
        return highest    
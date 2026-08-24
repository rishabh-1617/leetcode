class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kel = float(celsius + 273.15)
        fahrenheit = float(celsius * 1.80 + 32)
        ans = [kel, fahrenheit]
        return ans
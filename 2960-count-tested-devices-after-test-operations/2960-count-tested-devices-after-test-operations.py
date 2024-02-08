class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        tested_devices = 0
        for i,bat in enumerate(batteryPercentages):
            if batteryPercentages[i] > tested_devices:
                tested_devices += 1
        return tested_devices
                
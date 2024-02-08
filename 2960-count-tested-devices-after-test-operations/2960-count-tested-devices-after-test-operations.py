class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        tested_devices = 0
        for bat in batteryPercentages:
            if bat > tested_devices:
                tested_devices += 1
        return tested_devices
                
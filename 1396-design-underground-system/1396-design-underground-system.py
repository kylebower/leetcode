class UndergroundSystem:

    def __init__(self):
        self.customers = defaultdict(list)
        self.tripLengths = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id].append([stationName, t])
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.tripLengths[(self.customers[id][-1][0],stationName)].append(t-self.customers[id][-1][1])
        self.customers[id].append([stationName, t])
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self.tripLengths[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keysFound = {}
        roomsVisited = {}
        canVisitAll = False
        
        keysFound.update({"0":0})
        canVisitMoreRooms = True
        while canVisitMoreRooms:
            s1 = set(list(roomsVisited.values()))
            s2 = set(list(keysFound.values()))
            unopenedRoomsWithKeysFound = s2 - s1
            for x in unopenedRoomsWithKeysFound:
                roomsVisited.update({str(x):x})
                for y in rooms[x]:
                    keysFound.update({str(y):y})
            
            nkeysFound = len(list(keysFound.values()))
            nRoomsVisited = len(list(roomsVisited.values()))
            canVisitMoreRooms = nkeysFound > nRoomsVisited
        
        nRooms = len(rooms)
        nRoomsVisited = len(list(roomsVisited.values()))
        canVisitAll = nRoomsVisited == nRooms
        return canVisitAll
    
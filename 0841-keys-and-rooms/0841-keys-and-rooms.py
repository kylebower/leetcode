class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # define dictionary of all keys found
        keysFound = {"0":0}
        # define dictionary of all rooms visited
        roomsVisited = {}
        
        canVisitAll = False
        canVisitMoreRooms = True
        
        # iterate to visit all rooms that we can
        while canVisitMoreRooms:
            # find unvisited rooms that we have keys for
            s1 = set(list(roomsVisited.values()))
            s2 = set(list(keysFound.values()))
            unopenedRoomsWithKeysFound = s2 - s1
            
            # visit the unvisited rooms that we can
            for x in unopenedRoomsWithKeysFound:
                # add rooms to dictionary of all rooms visited
                roomsVisited.update({str(x):x})
                for y in rooms[x]:
                    # add keys to dictionary of all keys found
                    keysFound.update({str(y):y})
            
            # check whether we can visit any more rooms
            nkeysFound = len(list(keysFound.values()))
            nRoomsVisited = len(list(roomsVisited.values()))
            canVisitMoreRooms = nkeysFound > nRoomsVisited
        
        # determine whether we can visit all the rooms
        nRooms = len(rooms)
        nRoomsVisited = len(list(roomsVisited.values()))
        canVisitAll = nRoomsVisited == nRooms
        
        # return true if you can visit all the rooms, or false otherwise
        return canVisitAll
    
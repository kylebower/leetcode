class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        mTravelSinceLastStop = 0
        pTravelSinceLastStop = 0
        gTravelSinceLastStop = 0
        
        res = 0
        
        # go to first stop
        stop = garbage[0]        
        mAmount = stop.count('M')
        pAmount = stop.count('P')
        gAmount = stop.count('G')        
        res += mAmount + pAmount + gAmount
            
        for i,stop in enumerate(garbage[1:]):
            # travle to each subsequent stop
            mTravelSinceLastStop += travel[i]
            pTravelSinceLastStop += travel[i]
            gTravelSinceLastStop += travel[i]
            
            mAmount = stop.count('M')
            pAmount = stop.count('P')
            gAmount = stop.count('G')
            
            if mAmount > 0:
                res += mAmount + mTravelSinceLastStop
                mTravelSinceLastStop = 0            
            
            if pAmount > 0:
                res += pAmount + pTravelSinceLastStop
                pTravelSinceLastStop = 0
            
            if gAmount > 0:
                res += gAmount + gTravelSinceLastStop
                gTravelSinceLastStop = 0
                
        # Return the minimum number of minutes needed to pick up all the garbage    
        return res
        
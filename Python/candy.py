class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        temp = []
        tracker = []
        #first go through and find the slope to each point combination
        for i in range(0, len(points)-1):
            a = points[i]
            for x in range(i, len(points)-1):
                b = points[x+1]
                deltax = b[0] - a[0]
                if deltax != 0:
                    res = []
                    slope = (b[1] - a[1]) / float(deltax)
                    print(slope)
                    temp.append(slope)
                    res.append(a)
                    res.append(b)
                    tracker.append(res)         
        #find the most occuring slope!
        x = max(set(temp), key=temp.count)
        
        
        result = []
        for i in range(0, len(temp)):
            if temp[i] == x:
                y = tracker[i]
                result.append(y[0])
                result.append(y[1])
        print(result)
        l1 = []
        count = 0
        for item in result:
            if item not in l1:
                count += 1
                l1.append(item)
        print(l1)
        return count
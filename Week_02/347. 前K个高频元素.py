# 借助heapq
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        heap_max = []
        dic_fre = {}
        ans = []
        for i in nums:
            if i in dic_fre:
                dic_fre[i]+=1
            else:
                dic_fre[i] = 1
        for i in dic_fre:
            heapq.heappush(heap_max,(-dic_fre[i],i))
        for j in range(k):
            p = heapq.heappop(heap_max)
            ans.append(p[1])
        return ans
 
 
# 非调用heapq库
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1    
        max_time = max(map.values())
        TongList = [[] for i in range(max_time+1)] 
        for key, value in map.items():
            TongList[value].append(key) 
        res = []
        for i in range(max_time, 0, -1): 
            if TongList[i]:
                res.extend(TongList[i])
            if len(res) >= k:
                return res[:k]

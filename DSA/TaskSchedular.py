from collections import Counter

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        # Step 1: Count frequency of tasks
        freq = Counter(tasks)
        
        # Step 2: Find the maximum frequency
        maxFreq = max(freq.values())
        
        # Step 3: Count how many tasks have this max frequency
        maxCount = sum(1 for v in freq.values() if v == maxFreq)
        
        # Step 4: Compute formula
        # (maxFreq - 1) * (n + 1) makes blocks
        # + maxCount adds the last batch of most frequent tasks
        partCount = (maxFreq - 1) * (n + 1) + maxCount
        
        # Step 5: Take maximum of formula and total tasks
        return max(partCount, len(tasks))

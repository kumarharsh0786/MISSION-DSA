import heapq

def runningMedian(a):
    min_heap = []   
    max_heap = []   
    medians = []

    for num in a:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        if len(max_heap) > len(min_heap) + 1:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        elif len(min_heap) > len(max_heap) + 1:
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2.0
        elif len(max_heap) > len(min_heap):
            median = float(-max_heap[0])
        else:
            median = float(min_heap[0])

        medians.append(median)

    return medians

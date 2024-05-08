from collections import deque
import time

class Node:
    def __init__(self, level, profit, weight, bestset):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bestset = bestset

def knapsack(n, p, w, W): 
    maxprofit = 0
    PQ = PriorityQueue()

    v = Node(0, 0, 0, [])
    v.bound = bound(v)
    PQ.insert(v)

    while not PQ.isempty():
        v = PQ.dequeue()
        if v.bound > maxprofit:
            u = Node(0, 0, 0, [])
            u.level = v.level + 1
            u.weight = v.weight + w[u.level]
            u.profit = v.profit + p[u.level]

            if u.weight <= W and u.profit > maxprofit:
                maxprofit = u.profit

            u.bound = bound(u)
            if u.bound > maxprofit:
                PQ.insert(u)

            u.weight = v.weight
            u.profit = v.profit
            u.bound = bound(u) 
            if u.bound > maxprofit:
                PQ.insert(u)

    return maxprofit

def bound(u):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while j < n:
            if totweight + w[j] <= W:
                totweight += w[j]
                result += p[j]
            j += 1
        k = j
        if k < n:
            result += (W - totweight) * p[k] / w[k]

        return result


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        if not self.queue or item.bound > self.queue[-1].bound:
            self.queue.append(item)
        else:
            i = len(self.queue) - 1
            while i >= 0 and item.bound < self.queue[i].bound:
                i -= 1
            self.queue.insert(i + 1, item)

    def dequeue(self):
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def isempty(self):
        return not self.queue
        
# Example usage
n = 4  # Number of items
W = 16  # Capacity of the knapsack
p = [40, 30, 50, 10]  # Profits of items
w = [2, 5, 10, 5]  # Weights of items
maxprofit = 0

start = time.perf_counter()
maxprofit = knapsack(n, p, w, W)
end = time.perf_counter()

print("Execution Time:", end - start)
print("Max Profit:", maxprofit)


# Example usage
n = 4  # Number of items
W = 18  # Capacity of the knapsack
p = [40, 30, 50, 10]  # Profits of items
w = [2, 5, 10, 5]  # Weights of items
maxprofit = 0

start = time.perf_counter()
maxprofit = knapsack(n, p, w, W)
end = time.perf_counter()

print("Execution Time:", end - start)
print("Max Profit:", maxprofit)


# Example usage
n = 4  # Number of items
W = 25  # Capacity of the knapsack
p = [50, 55, 15, 50]  # Profits of items
w = [2, 10, 5, 20]  # Weights of items
maxprofit = 0

start = time.perf_counter()
maxprofit = knapsack(n, p, w, W)
end = time.perf_counter()

print("Execution Time:", end - start)
print("Max Profit:", maxprofit)

# Example usage
n = 4  # Number of items
W = 40  # Capacity of the knapsack
p = [50, 55, 15, 50]  # Profits of items
w = [2, 10, 5, 20]  # Weights of items
maxprofit = 0

start = time.perf_counter()
maxprofit = knapsack(n, p, w, W)
end = time.perf_counter()

print("Execution Time:", end - start)
print("Max Profit:", maxprofit)

# Example usage
n = 4  # Number of items
W = 1  # Capacity of the knapsack
p = [1, 1, 1, 1]  # Profits of items
w = [2, 3, 4, 5]  # Weights of items
maxprofit = 0

start = time.perf_counter()
maxprofit = knapsack(n, p, w, W)
end = time.perf_counter()

print("Execution Time:", end - start)
print("Max Profit:", maxprofit)
from collections import deque
import time


def knapsack(n, p, w, W): 
    Q = deque()
    v = Node(0, 0, 0, [])

    maxprofit = 0
    enqueue(Q, v)

    while not isempty(Q):
        v = dequeue(Q)
        u = Node(0, 0, 0, v.bestset[:])
        u.level = v.level + 1
        u.weight = v.weight + w[u.level - 1]
        u.profit = v.profit + p[u.level - 1]

        if u.level < n:
            u.bestset.append("yes")

        if u.weight <= W and u.profit > maxprofit:
            maxprofit = u.profit

        if bound(u) > maxprofit:
            enqueue(Q, u)

        u.weight = v.weight
        u.profit = v.profit

        if bound(u) > maxprofit:
            enqueue(Q, u)

    return maxprofit    



def bound(u):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while j <= n and totweight + w[j - 1] <= W:
            totweight += w[j - 1]
            result += p[j - 1]
            j += 1
        k = j
        if k <= n:
            result += (W - totweight) * p[k - 1] / w[k - 1]

        return result
    
def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if queue:
        return queue.popleft()
    else:
        raise IndexError("Queue is empty")
    
def isempty(queue):
    return not queue

    
class Node:
    def __init__(self, level, profit, weight, bestset):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bestset = bestset

# Example usage
n = 4  # Number of items
W = 16  # Capacity of the knapsack
p = [40, 30, 50, 10]  # Profits of items
w = [2, 5, 10, 5]  # Weights of items


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
import time

# Global variable
nodes_visited = 0

def knapsack_backtrack(i, profit, weight):
    global maxprofit, numbest, bestset, nodes_visited
    nodes_visited += 1  # Increment the counter for each node visited
    
    if weight <= W and profit > maxprofit:
        maxprofit = profit
        numbest = i
        bestset = include.copy()

    if promising(i, profit, weight):
        include[i + 1] = "yes"
        knapsack_backtrack(i + 1, profit + p[i], weight + w[i])
        include[i + 1] = "no"
        knapsack_backtrack(i + 1, profit, weight)

def promising(i, profit, weight):
    global W, n, maxprofit, p, w
    if weight >= W:
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while j <= n and totweight + w[j - 1] <= W:
            totweight += w[j - 1]
            bound += p[j - 1]
            j += 1
        
        k = j
        if k <= n:
            bound += (W - totweight) * (p[k - 1] / w[k - 1])

        return bound > maxprofit

# Example usage
n = 4  # Number of items
W = 16  # Capacity of the knapsack
p = [40, 30, 50, 10]  # Profits of items
w = [2, 5, 10, 5]  # Weights of items
maxprofit = 0
numbest = 0
bestset = []
include = ["no"] * (n + 1)
nodes_visited = 0

start = time.perf_counter()
knapsack_backtrack(0, 0, 0)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Max Profit:", maxprofit)
print("Items included:")
num = 0
for j in bestset:
    if j == "yes":
        print("Item", num)
    num += 1

print("Nodes visited:", nodes_visited - 1)


# Example usage
n = 4  # Number of items
W = 18  # Capacity of the knapsack
p = [40, 30, 50, 10]  # Profits of items
w = [2, 5, 10, 5]  # Weights of items
maxprofit = 0
numbest = 0
bestset = []
include = ["no"] * (n + 1)
nodes_visited = 0

start = time.perf_counter()
knapsack_backtrack(0, 0, 0)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Max Profit:", maxprofit)
print("Items included:")
num = 0
for j in bestset:
    if j == "yes":
        print("Item", num)
    num += 1

print("Nodes visited:", nodes_visited - 1)


# Example usage
n = 4  # Number of items
W = 25  # Capacity of the knapsack
p = [50, 55, 15, 50]  # Profits of items
w = [2, 10, 5, 20]  # Weights of items
maxprofit = 0
numbest = 0
bestset = []
include = ["no"] * (n + 1)
nodes_visited = 0

start = time.perf_counter()
knapsack_backtrack(0, 0, 0)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Max Profit:", maxprofit)
print("Items included:")
num = 0
for j in bestset:
    if j == "yes":
        print("Item", num)
    num += 1

print("Nodes visited:", nodes_visited - 1)


# Example usage
n = 4  # Number of items
W = 40  # Capacity of the knapsack
p = [50, 55, 15, 50]  # Profits of items
w = [2, 10, 5, 20]  # Weights of items
maxprofit = 0
numbest = 0
bestset = []
include = ["no"] * (n + 1)
nodes_visited = 0

start = time.perf_counter()
knapsack_backtrack(0, 0, 0)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Max Profit:", maxprofit)
print("Items included:")
num = 0
for j in bestset:
    if j == "yes":
        print("Item", num)
    num += 1

print("Nodes visited:", nodes_visited - 1)


# Example usage
n = 4  # Number of items
W = 1 # Capacity of the knapsack
p = [1, 1, 1, 1]  # Profits of items
w = [2, 3, 4, 5]  # Weights of items
maxprofit = 0
numbest = 0
bestset = []
include = ["no"] * (n + 1)
nodes_visited = 0

start = time.perf_counter()
knapsack_backtrack(0, 0, 0)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Max Profit:", maxprofit)
print("Items included:")
num = 0
for j in bestset:
    if j == "yes":
        print("Item", num)
    num += 1

print("Nodes visited:", nodes_visited - 1)
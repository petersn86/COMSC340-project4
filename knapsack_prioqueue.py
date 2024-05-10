from queue import PriorityQueue
import time

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, weight, items_selected):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.items_selected = items_selected  # List to keep track of selected items

def bound(u, n, W, arr):
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    while j < n and total_weight + arr[j].weight <= W:
        total_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    if j < n:
        profit_bound += (W - total_weight) * arr[j].value / arr[j].weight

    return profit_bound

def knapsack(W, arr, n):
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)

    priority_queue = PriorityQueue()
    u = Node(-1, 0, 0, [])  # Initialize with an empty list for selected items
    priority_queue.put((0, u))  # Prioritize nodes with lower bounds

    max_profit = 0
    nodes_visited = 0  # Counter for nodes visited

    while not priority_queue.empty():
        _, u = priority_queue.get()
        nodes_visited += 1  # Increment nodes visited counter

        if u.level == -1:
            v = Node(0, 0, 0, [])
        elif u.level == n - 1:
            continue
        else:
            v = Node(u.level + 1, u.profit, u.weight, u.items_selected[:])  # Copy items_selected list

        v.weight += arr[v.level].weight
        v.profit += arr[v.level].value
        v.items_selected.append(v.level)  # Add the index of the selected item

        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit
            max_items_selected = v.items_selected  # Keep track of the best items selected

        v_bound = bound(v, n, W, arr)
        if v_bound > max_profit:
            priority_queue.put((-v_bound, v))  # Negate bound for priority ordering

        v = Node(u.level + 1, u.profit, u.weight, u.items_selected[:])  # Copy items_selected list
        v_bound = bound(v, n, W, arr)
        if v_bound > max_profit:
            priority_queue.put((-v_bound, v))  # Negate bound for priority ordering
        
    if max_profit == 0:
        max_items_selected = [0]

    return max_profit, nodes_visited, max_items_selected

W = 16
arr = [
    Item(2, 40),
    Item(5, 30),
    Item(10, 50),
    Item(5, 10),
]
n = len(arr)
start = time.perf_counter()
max_profit, nodes_visited, max_items_selected = knapsack(W, arr, n)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Maximum possible profit =", max_profit)
print("Nodes visited:", nodes_visited)
print("Items selected:", max_items_selected)


W = 18
arr = [
    Item(2, 40),
    Item(5, 30),
    Item(10, 50),
    Item(5, 10),
]
n = len(arr)
start = time.perf_counter()
max_profit, nodes_visited, max_items_selected = knapsack(W, arr, n)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Maximum possible profit =", max_profit)
print("Nodes visited:", nodes_visited)
print("Items selected:", max_items_selected)


W = 25
arr = [
    Item(2, 50),
    Item(10, 55),
    Item(5, 15),
    Item(20, 50),
]
n = len(arr)
start = time.perf_counter()
max_profit, nodes_visited, max_items_selected = knapsack(W, arr, n)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Maximum possible profit =", max_profit)
print("Nodes visited:", nodes_visited)
print("Items selected:", max_items_selected)


W = 40
arr = [
    Item(2, 50),
    Item(10, 55),
    Item(5, 15),
    Item(20, 50),
]
n = len(arr)
start = time.perf_counter()
max_profit, nodes_visited, max_items_selected = knapsack(W, arr, n)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Maximum possible profit =", max_profit)
print("Nodes visited:", nodes_visited)
print("Items selected:", max_items_selected)


W = 1
arr = [
    Item(2, 1),
    Item(3, 1),
    Item(4, 1),
    Item(5, 1),
]
n = len(arr)
start = time.perf_counter()
max_profit, nodes_visited, max_items_selected = knapsack(W, arr, n)
end = time.perf_counter()
print("Time taken:", "{:0.10f}".format(end - start))
print("Maximum possible profit =", max_profit)
print("Nodes visited:", nodes_visited)
print("Items selected:", max_items_selected)
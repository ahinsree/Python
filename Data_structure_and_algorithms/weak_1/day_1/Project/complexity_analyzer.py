import timeit
import matplotlib.pyplot as plt
import numpy as np

def linear_search(arr, target):
    """Simple linear search for timing (O(n))."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Simple binary search for timing (O(log n); assumes sorted)."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def time_algorithm(algorithm, sizes, num_runs=1000):
    """Time a given algorithm across input sizes."""
    times = []
    for n in sizes:
        arr = list(range(n))  # Sorted ascending for binary search
        target = n // 2       # Middle element for average-case timing
        def wrapper():
            return algorithm(arr, target)
        total_time = timeit.timeit(wrapper, number=num_runs)
        times.append(total_time)
    return times

def estimate_big_o(times, sizes):
    """Estimate Big O class using log-log linear regression (slope approximates exponent)."""
    log_sizes = np.log(sizes)
    log_times = np.log(times)
    slope, _ = np.polyfit(log_sizes, log_times, 1)
    if slope < 0.1:
        return "O(1)"
    elif slope < 0.8:
        return "O(log n)"
    elif slope < 1.2:
        return "O(n)"
    elif slope < 1.8:
        return "O(n log n)"
    else:
        return "O(n²)"

def plot_times(sizes, times_dict, title="Time Complexity Comparison", log_scale=True):
    """Plot timing data for multiple algorithms."""
    plt.figure(figsize=(10, 6))
    for algo, times in times_dict.items():
        plt.plot(sizes, times, marker='o', linestyle='-', label=algo)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Total Time for 1,000 Runs (seconds)')
    plt.title(title)
    if log_scale:
        plt.yscale('log')  # Log y-axis to highlight growth rates
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()  # Displays the plot; or use plt.savefig('plot.png') to export

# Demo: Run the analyzer
if __name__ == "__main__":
    # Customize these!
    sizes = [100, 500, 1000, 2000, 5000, 10000]
    algorithms = [linear_search, binary_search]
    
    times_data = {}
    for algo in algorithms:
        times_data[algo.__name__.replace('_', ' ').title()] = time_algorithm(algo, sizes)
    
    print("Time Complexity Analysis Results:\n")
    for algo, times in times_data.items():
        big_o = estimate_big_o(times, sizes)
        print(f"{algo}:")
        print(f"  Big O Estimate: {big_o}")
        print(f"  Times (s): {[f'{t:.6f}' for t in times]}")
        print()
    
    # Generate plot
    plot_times(sizes, times_data)
import timeit
import matplotlib.pyplot as plt

def linear_search(arr, target):
    """Simple linear search for timing."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def time_linear_search(n, num_runs=1000):
    """Time linear search for a given array size."""
    arr = list(range(n))
    target = n // 2  # Middle for average case (best case would be 0, worst case n-1)
    
    # Pass variables to timeit using 'globals' to avoid large string formatting.
    # This is much more efficient than embedding the list into the setup string.
    setup = ""  # Setup is not needed as all variables are passed via 'globals'.
    stmt = "linear_search(arr, target)"
    return timeit.timeit(stmt, setup=setup, number=num_runs, globals={'linear_search': linear_search, 'arr': arr, 'target': target})

def plot_times(sizes, times, title="Linear Search Time Growth", xlabel="Array Size (n)", ylabel="Total Time for 1,000 Runs (s)"):
    """Plot timing data using matplotlib."""
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='b')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.show()  # Or plt.savefig('linear_search_plot.png') to save as image

# Main execution
if __name__ == "__main__":
    # Define sizes to test
    sizes = [100, 500, 1000, 2000, 5000, 10000]
    times = []

    print("Timing linear searches...\n")
    for n in sizes:
        total_time = time_linear_search(n)
        times.append(total_time)
        print(f"Size {n}: {total_time:.6f} seconds")

    # Print data for easy reference (e.g., CSV export)
    print("\nData for plot (size, time):")
    for size, time in zip(sizes, times):
        print(f"{size}, {time}")

    # Generate the plot
    plot_times(sizes, times)
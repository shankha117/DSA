import heapq

class HeapDemo:
    def __init__(self):
        self.min_heap = []  # Min-heap
        self.max_heap = []  # Max-heap simulated by negating values

    def add_to_min_heap(self, value):
        """Adds a value to the min-heap."""
        heapq.heappush(self.min_heap, value)
        print(f"Added {value} to min-heap: {self.min_heap}")

    def add_to_max_heap(self, value):
        """Adds a value to the max-heap by pushing its negated value."""
        heapq.heappush(self.max_heap, -value)
        print(f"Added {value} to max-heap: {[-val for val in self.max_heap]}")

    def pop_from_min_heap(self):
        """Removes and returns the smallest element from the min-heap."""
        smallest = heapq.heappop(self.min_heap)
        print(f"Removed {smallest} from min-heap: {self.min_heap}")
        return smallest

    def pop_from_max_heap(self):
        """Removes and returns the largest element from the max-heap."""
        largest = -heapq.heappop(self.max_heap)
        print(f"Removed {largest} from max-heap: {[-val for val in self.max_heap]}")
        return largest

    def replace_in_min_heap(self, value):
        """Replaces the smallest element in the min-heap with a new value."""
        replaced = heapq.heapreplace(self.min_heap, value)
        print(f"Replaced {replaced} with {value} in min-heap: {self.min_heap}")
        return replaced

    def pushpop_min_heap(self, value):
        """Pushes a value onto the min-heap and then pops the smallest element."""
        result = heapq.heappushpop(self.min_heap, value)
        print(f"Pushed {value} and popped {result} from min-heap: {self.min_heap}")
        return result

    def heapify_list(self, data):
        """Transforms a list into a heap in-place."""
        heapq.heapify(data)
        print(f"Heapified list: {data}")
        return data

    def get_n_largest(self, n):
        """Returns the n largest elements from the min-heap."""
        largest = heapq.nlargest(n, self.min_heap)
        print(f"{n} largest elements in min-heap: {largest}")
        return largest

    def get_n_smallest(self, n):
        """Returns the n smallest elements from the min-heap."""
        smallest = heapq.nsmallest(n, self.min_heap)
        print(f"{n} smallest elements in min-heap: {smallest}")
        return smallest

# Example usage
def main():
    heap_demo = HeapDemo()

    # Add elements to the min-heap
    heap_demo.add_to_min_heap(10)
    heap_demo.add_to_min_heap(5)
    heap_demo.add_to_min_heap(15)

    # Add elements to the max-heap
    heap_demo.add_to_max_heap(10)
    heap_demo.add_to_max_heap(5)
    heap_demo.add_to_max_heap(15)

    # Remove elements from the heaps
    heap_demo.pop_from_min_heap()
    heap_demo.pop_from_max_heap()

    # Replace the smallest element in the min-heap
    heap_demo.replace_in_min_heap(12)

    # Push a value onto the heap and then pop the smallest element
    heap_demo.pushpop_min_heap(7)

    # Heapify a list
    data = [20, 1, 15, 5, 10]
    heap_demo.heapify_list(data)

    # Get the 2 largest and smallest elements from the min-heap
    heap_demo.get_n_largest(2)
    heap_demo.get_n_smallest(2)

if __name__ == "__main__":
    main()

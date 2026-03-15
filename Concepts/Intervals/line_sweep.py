def max_overlapping_intervals(intervals):
    events = []

    # Step 1: Create (time, delta) events
    for start, end in intervals:
        events.append((start, +1))  # interval starts
        events.append((end, -1))    # interval ends

    print(events)
    # Step 2: Sort events by time, with ends before starts at same time
    events.sort()

    print(events)

    # Step 3: Sweep line
    active = 0
    max_active = 0

    for time, delta in events:
        active += delta
        max_active = max(max_active, active)

    return max_active

def test_max_overlapping_intervals():
    test_cases = [
        # 1. Simple overlap
        ([(1, 3), (2, 4), (3, 5)], 2),

        # 2. No overlap at all
        ([(1, 2), (3, 4), (5, 6)], 1),

        # 3. All intervals overlap fully
        ([(1, 10), (2, 9), (3, 8)], 3),

        # 4. Intervals just touching — no real overlap
        ([(1, 3), (3, 5), (5, 7)], 1),

        # 5. Multiple start and end at the same time
        ([(1, 5), (1, 5), (1, 5)], 3),

        # 6. Overlap spike in the middle
        ([(1, 4), (2, 5), (3, 6), (4, 7)], 3),

        # 7. Edge case with single interval
        ([(0, 100)], 1),
    ]

    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = max_overlapping_intervals(intervals)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    print("All test cases passed!")

test_max_overlapping_intervals()

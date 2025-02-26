


def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array.
    LPS[i] contains the length of the longest proper prefix
    which is also a suffix for pattern[:i+1].
    """
    lps = [0] * len(pattern)
    i = 0  # length of previous longest prefix suffix
    j = 1

    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            if i != 0:
                i = lps[i - 1]  # Reduce length and retry
            else:
                j += 1
    return lps


def kmp_search(text, pattern):
    """
    Searches for occurrences of 'pattern' in 'text' using the KMP algorithm.
    Returns the starting indices of all occurrences.
    """
    if not pattern:
        return []

    lps = compute_lps(pattern)
    print(lps)
    i = j = 0  # i -> index for text, j -> index for pattern
    result = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):  # Found a match
                result.append(i - j)
                j = lps[j - 1]  # Use LPS to continue searching

        elif j > 0:
            j = lps[j - 1]  # Use LPS to skip unnecessary comparisons
        else:
            i += 1  # Move to the next character in text

    return result


# Example usage
text = "ababcababcabc"
pattern = "abc"
print(kmp_search(text, pattern))  # Output: [2, 7, 10]

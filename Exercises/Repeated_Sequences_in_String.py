def find_repeated_sequences(text, min_length=2, min_occurrences=2):
    """
    Find all repeated character sequences in a string.

    Args:
        text: The input string to analyze
        min_length: Minimum length of sequences to find (default: 2)
        min_occurrences: Minimum number of times a sequence must appear (default: 2)

    Returns:
        Dictionary with sequences as keys and their count as values
    """
    sequences = {}
    text_len = len(text)

    # Try all possible sequence lengths starting from min_length
    for length in range(min_length, text_len // 2 + 1):
        # Slide through the text to extract all substrings of this length
        for i in range(text_len - length + 1):
            seq = text[i : i + length]

            # Count this sequence
            if seq in sequences:
                sequences[seq] += 1
                print(f"Found sequence: '{seq}' (count: {sequences[seq]})")
            else:
                sequences[seq] = 1

    # Filter to only sequences that appear at least min_occurrences times
    repeated = {
        seq: count for seq, count in sequences.items() if count >= min_occurrences
    }

    return repeated


# Example usage
if __name__ == "__main__":
    # Test string
    test_string = "abcabcdefdefabcabc"

    print(f"Analyzing string: '{test_string}'")
    print()

    results = find_repeated_sequences(test_string)

    # Sort by length (descending) then by count (descending)
    sorted_results = sorted(
        results.items(), key=lambda x: (len(x[0]), x[1]), reverse=True
    )

    print("Repeated sequences:")
    for seq, count in sorted_results:
        print(f"  '{seq}' - appears {count} times")

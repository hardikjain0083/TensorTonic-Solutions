import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # 1. Create a lookup dictionary for the vocabulary
    # This maps each word to its corresponding index (e.g., {"i": 0, "love": 1, ...})
    vocab_index_map = {word: index for index, word in enumerate(vocab)}
    
    # 2. Initialize a numpy array of zeros with the same length as the vocabulary
    bow_vector = np.zeros(len(vocab), dtype=int)
    
    # 3. Iterate through the tokens and count occurrences
    for token in tokens:
        if token in vocab_index_map:
            # If the token is in our vocab, increment its count at the mapped index
            target_index = vocab_index_map[token]
            bow_vector[target_index] += 1
            
    return bow_vector
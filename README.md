
## Hashsort

A linear(ish) time sorting algorithm. The actual time complexity is O(n + d), where d is the difference between the largest and smallest elements of the array. This makes it very easy to construct an adversarial input (e.g. [-1000000,10000000], but for inputs where d is not significantly larger than n, it performs quite well.

Note: due to using the array values themselves as indexes, hashsort ONLY works for arrays of integers. This means its real-world applications are fairly limited, but it was a fun thought experiment for me.

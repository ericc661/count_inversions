'''
Problem definition: Given a sequence of unique numbers from 1 to n
    (not necessarily in that order), count how many inversions it contains. An
    inversion is a pair of indices i, j such that i < j but ai > aj. That is,
    the later number is less than the earlier number. An upward counting sequence
    from 1 to n has 0 inversions, and the opposite (completely inverted)
    has n(n-1)/2 inversions.
'''

class InversionCounter:

    '''
    summary: Counts inversions in list A
    requires: A to be the list
    effects: Returns a 2-tuple: 1) the # inversions,
               2) the final sorted list
    '''
    def count_inversions(self, A):
        if len(A) == 1:
            return (0, A)

        # divide array into two pieces
        cut = len(A) // 2 # the first index of the right half
        L = A[:cut]
        R = A[cut:]
        (count_L, list_L) = self.count_inversions(L)
        (count_R, list_R) = self.count_inversions(R)
        (count_across, list_merged) = self.merge_and_count(list_L, list_R)

        total_count = count_L + count_R + count_across
        return(total_count, list_merged)

    '''
    summary: merges two sorted lists and counts inversions across the divide
    requires: L to be the left sorted lists, R the right
    effects: returns 1) count of inversions across the divide (every time an
                item is added from  R, add # of remaining elements in L to
                count) and 2) the merged list.

    '''
    def merge_and_count(self, L, R):
        C = [] # final sorted list
        count = 0
        i, j = 0, 0 # indices for L and R elements

        # loop until one of the lists has been completely copied over
        while (i<len(L) and j<len(R)):
            if L[i] < R[j]: # no new inversions
                C.append(L[i])
                i = i+1
            elif R[j] < L[i]: # new inversions = # elements remaining in L
                remaining = len(L)-i
                count = count + remaining
                C.append(R[j])
                j = j+1
            else:
                raise ValueError('Duplicate values found in list')

        # at this point: copy the rest of the single remaining list into C
        if (i<len(L)): # if elements in L still remaining
            C.extend(L[i:])
        else: # otherwise, elements in R still remaining (due to while loop condition)
            C.extend(R[j:])

        return (count, C)


def main():
    ic = InversionCounter()

if __name__ == '__main__':
    main()

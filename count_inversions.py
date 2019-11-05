
class InversionCounter:

    # handles all the recursion: sorts and counts inversions on left half
    #   and right half, then merges and count all inversions that go across
    #   the divide. A is the input list
    def count_inversions(self, A):
        if len(A) == 1:
            return (0, A)

        # divide array into two pieces
        cut = len(A) // 2 # the first index of the right half
        L = A[:cut]
        R = A[cut:]
        (count_L, list_L) = self.count_inversions(L)
        (count_R, list_R) = self.count_inversions(R)

        return (10, [1, 3, 5]) # return garbage for now

    # given two sorted lists, merges them and counts inversions
    #   across the boundary
    #   TODO: define inversions across boundary more clearly
    def merge_and_count(self, L, R):

def main():
    ic = InversionCounter()
    print(ic.count_inversions([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()


class InversionCounter:

    # handles all the recursion: sorts and counts inversions on left half
    #   and right half, then merges and count all inversions that go across
    #   the divide. A is the input list
    def count_inversions(self, A):
        if len(A) == 1:
            return (0, A)

        # divide array into two pieces
        cut = (len(A) - 1) // 2 # the last index of the left half
        L = [5]

        return (10, [1, 3, 5]) # return garbage for now

def main():
    ic = InversionCounter()
    print(ic.count_inversions([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()

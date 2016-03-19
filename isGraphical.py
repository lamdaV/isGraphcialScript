import sys

def main():
    """
        Determine if a degree sequence is graphical.
        Grabs command line arguments that are space separated.
    """
    # Script use to solve problems in:
    #   "A First Course in Graph Theory"
    #       by Gary Chartrand and Ping Zhang

    # 2.32
    # a = [5, 3, 3, 3, 3, 2, 2, 2, 1]
    # b = [6, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1]
    # c = [6, 5, 5, 4, 3, 2, 1]
    # d = [7, 5, 4, 4, 4, 3, 2, 1]
    # e = [7, 6, 5, 4, 4, 3, 2, 1]
    # prob = [a, b, c, d, e]
    # for part in prob:
    #     print(isGraphical(part))

    # 2.33
    # for x in range(6):
    #     a = [1, 2, 3, 5, 5]
    #     a.append(x)
    #     a.sort(reverse = True)
    #     print(isGraphical(a))

    # 2.34
    # for x in range(8):
    #     a = [7, 6, 5, 4, 4, 3, 2, 1]
    #     a.append(x)
    #     print(isGraphical(a, False))
    #     if (isGraphical(a, False)):
    #         print(x)

    # 2.35
    # for x in range(8):
    #     a = [7, 7, 5, 5, 4, 3, 2]
    #     a.append(x)
    #     a.sort(reverse = True)
    #     print(str(x) + " : " + str(isGraphical(a)))

    degSeq = []
    verbose = False

    # Grab command line arguments.
    for k in range(1, len(sys.argv)):
        # Allows for the "-v" flag to be appear anywhere.
        if (sys.argv[k] == "-v"):
            verbose = True
        else:
            degSeq.append(int(sys.argv[k]))

    # Sort it in descending order.
    degSeq.sort(reverse = True)

    # Print Value(s).
    print(isGraphical(degSeq, verbose))

def isGraphical(degSeq, verbose = False):
    """
        Checks if a given degSeq is Graphical.

        Arguments:
            :type degSeq :      list
               List of integers representing a graphs degree sequence.
        Optional Parameters:
            :type verbose :     boolean
                Flag used to print each stage of the degSeq.

        Returns True if degSeq is Graphical.
                False otherwise.
    """
    # Main Loop.
    while (isValid(degSeq)):
        # Grab first element.
        current = degSeq[0]

        # Print stage if verbose.
        if (verbose):
            print(degSeq)

        # Decrement degSeg.
        # If IndexError, it is not graphical.
        try:
            for k in range(1, current + 1):
                degSeq[k] -= 1
        except IndexError:
            return False
        degSeq.remove(current)
        degSeq.sort(reverse = True)

        # Passing condition.
        if (isZero(degSeq)):
            return True

    return False

def isZero(degSeq):
    """
        Checks if a given degSeq is all zeros.

        Arguments:
            :type degSeq :      list
               List of integers representing a graphs degree sequence.

        Returns True if degSeq contains only zero.
                False otherwise.
    """
    for element in degSeq:
        if (element != 0):
            return False
    return True

def isValid(degSeq):
    """
        Checks if a given degSeq is still valid (no negatives).

        Arguments:
            :type degSeq :      list
               List of integers representing a graphs degree sequence.

        Returns True if degSeq contains no negatives.
                False otherwise.
    """
    # Ensure that degSeq is not empty.
    if (len(degSeq) == 0):
        return False

    for element in degSeq:
        if (element < 0):
            return False
    return True

if __name__ == "__main__":
    main()

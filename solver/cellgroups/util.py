def uniques(li):
    uniquesli = []
    for e in li:
        if not e in uniquesli:
            uniquesli.append(e)
    return uniquesli

class RangeError(RuntimeError):
    def __init__(self, min, max, actual):
        super(RangeError, self).__init__("range exceeded: value " + str(actual) + " does not fall within the range of " + str(min) + " to " + str(max))

class DuplicateValuesError(RuntimeError):
    def __init__(self):
        super(DuplicateValuesError, self).__init__("duplicate values found in list")

class AmbiguousPuzzleException(Exception):
    def __init__(self, passes):
        super(AmbiguousPuzzleException, self).__init__("ambiguous puzzle (" + str(passes) + " passes)")

if __name__ == "__main__":
    print "error: this is not a standalone script; run \"./solver\" instead"


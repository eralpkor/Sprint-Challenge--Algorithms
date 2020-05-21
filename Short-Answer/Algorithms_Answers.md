#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity of this block of code would be `O(n^3)`, where n is the input size. This is because the while loop is running on the order on `n^3` times. While the code in the loop is incrementing by a value on the order of `n^2`, the higher polynomial order of `n^3` will dominate the `n^2` for large inputs.


b) The runtime complexity of this block of code would be `O(n log n)`, where `n` is the input size. This is because the outer for loop runs `n` times, for a runtime complexity of `O(n)`. Meanwhile, the value of `j` in the inner while loop is doubling rather than incrementing, resulting in a runtime complexity of `O(log n)`. For nested loops, we want to multiply the runtime complexities, so we would get a combined runtime complexity of `O(n log n)`


c) The runtime complexity of this block of code would be `O(n)` (linear), where `n` is bunnies. This block of code demonstrates recursion and will run `n` times, decrementing bunnies down to the base case value of zero.

## Exercise II

Proposed algorithm:

    Start at the middle floor.
    Drop an egg from this floor. If the egg breaks, eliminate all the floors above.
    If the egg doesn't break, eliminate current floor and all the floors below.
    Repeat the process with the none eliminated floors until there are only two floors left; f would be the higher of the two floors.

Pseudo code (iterative solution):

Solution assume a function dropped_egg_breaks() that returns True if the egg dropped from a particular floor breaks or False if the dropped egg doesn't break.

``` python
def iterative_minimize_broken_eggs(floors):
    # initialize low floor and high floors
    low_floor = 0
    high_floor = len(floors) - 1

    # run code while there are more than two floors remaining
    while low_floor <= high_floor - 1:

        # find middle floor
        middle_floor = (low_floor + high_floor)) // 2

        # if dropped egg breaks, reset high floor to eliminate above floors
        if dropped_egg_breaks(middle_floor):
            high_floor = middle_floor

        # if dropped egg doesn't break, reset low floor to eliminate current floor and all floors below
        elif not dropped_egg_breaks(middle_floor):
            low_floor = middle_floor + 1

    # while loops ends when we're left with two floors, return the higher floor as f
    return high_floor

    # keep in mind that floors list is 0 indexed, so f would correspond to the "f +1"th floor
  ```

Runtime complexity:

This solution implements a variation on a Binary Search and thus has a logarithmic runtime complexity of `O(log n)`. As the number of floors increases, the runtime used will grow at a slightly slower rate, so this solution would perform better than linear `O(n)`.

MOVES = 0
PEGS = {"a": [], "b": [], "c": []}

def towers_of_hanoi(num_of_disks, from_peg, to_peg, rem_peg, moves):
    # Base case: If no disks to move, return.
    if num_of_disks == 0:
        return

    # Move n-1 disks from "from_peg" to "rem_peg".
    towers_of_hanoi(num_of_disks - 1, from_peg, rem_peg, to_peg, moves)
    
    # Move the nth disk from "from_peg" to "to_peg"
    disk = PEGS[from_peg].pop()
    PEGS[to_peg].append(disk)
    moves[0] += 1
    print(f"Move {moves[0]}: Peg {from_peg} to Peg {to_peg}")
    print(f"Peg a: {PEGS['a']}\nPeg b: {PEGS['b']}\nPeg c: {PEGS['c']}\n")

    # Move n-1 disks from "rem_peg" to "to_peg".
    towers_of_hanoi(num_of_disks - 1, rem_peg, to_peg, from_peg, moves)

def init_towers(num_of_disks):
    PEGS["a"] = []
    PEGS["b"] = []
    PEGS["c"] = []

    for i in range(0, num_of_disks):
        PEGS["a"].append(i)

init_towers(3)
MOVES = [0]  # Using a list to hold moves count by reference
towers_of_hanoi(3, "a", "c", "b", MOVES)

print(f"Success in {MOVES[0]} moves")

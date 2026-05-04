#!/usr/bin/env python3


def print_rods(rods):
    print(f"A: {rods['A']}")
    print(f"B: {rods['B']}")
    print(f"C: {rods['C']}")
    print("-" * 25)


def move_disk(rods, source, target):
    disk = rods[source].pop()
    rods[target].append(disk)

    print(f"Move disk {disk} from {source} to {target}")
    print_rods(rods)


def hanoi(n, source, target, auxiliary, rods):
    # If there are no disks to move, stop the recursion.
    if n == 0:
        return

    # Move n-1 disks from source to auxiliary using target as temporary storage.
    hanoi(n - 1, source, auxiliary, target, rods)

    # Move the remaining largest disk to the target rod.
    move_disk(rods, source, target)

    # Move the n-1 disks from auxiliary to target using source as temporary storage.
    hanoi(n - 1, auxiliary, target, source, rods)


def main():
    n = 3

    rods = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": [],
    }

    print("Initial state:")
    print_rods(rods)

    hanoi(n, "A", "C", "B", rods)


if __name__ == "__main__":
    main()

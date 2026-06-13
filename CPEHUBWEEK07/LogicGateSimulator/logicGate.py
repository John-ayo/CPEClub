# Uses: functions, list comprehensions, tuples

# Basic Gates

def AND(a, b):
    return 1 if a == 1 and b == 1 else 0

def OR(a, b):
    return 1 if a == 1 or b == 1 else 0

def NOT(a):
    return 1 if a == 0 else 0

def XOR(a, b):
    return 1 if a != b else 0


# Half Adder 

def half_adder(a, b):
    sum_bit = XOR(a, b)    # XOR gives the sum
    carry = AND(a, b)      # AND gives the carry
    return sum_bit, carry


# Test All Cases 

test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("===== Logic Gate Tests =====\n")

print("AND Gate:")
[print(f"  AND({a}, {b}) = {AND(a, b)}") for a, b in test_cases]

print("\nOR Gate:")
[print(f"  OR({a}, {b}) = {OR(a, b)}") for a, b in test_cases]

print("\nNOT Gate:")
[print(f"  NOT({a}) = {NOT(a)}") for a, _ in test_cases[:2]]

print("\nXOR Gate:")
[print(f"  XOR({a}, {b}) = {XOR(a, b)}") for a, b in test_cases]

print("\n===== Half Adder Truth Table =====")
print(f"  {'A':<5} {'B':<5} {'Sum':<8} {'Carry'}")
print("  " + "-" * 25)

results = [(a, b, *half_adder(a, b)) for a, b in test_cases]
for a, b, s, c in results:
    print(f"  {a:<5} {b:<5} {s:<8} {c}")

print("\n  1 + 1 in binary:")
s, c = half_adder(1, 1)
print(f"  Sum = {s}, Carry = {c}  (which means the answer is '10' in binary = 2 in decimal)")
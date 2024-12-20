def enrollment_stats(univers):
    total = [university[1] for university in univers]
    fees = [university[2] for university in univers]
    return total, fees

def mean(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)

def median(arr):
    arr.sort()
    md = len(arr) // 2
    return arr[md]

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

total, fees = enrollment_stats(universities)

print("******************************")

print(f"Total students: {sum(total):,}")
print(f"Total tuition: $ {sum(fees):,}")

print()

print(f"Student mean: {mean(total):,.2f}")
print(f"Student median: {median(total):,}")

print()

print(f"Tuition mean: $ {mean(fees):,.2f}")
print(f"Tuition median: $ {median(fees):,}")

print("******************************")
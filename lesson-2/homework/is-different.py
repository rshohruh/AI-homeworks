nums = [int(input(f"Enter number {i+1}: ")) for i in range(3)]
print("All different" if len(set(nums)) == 3 else "Not all different")

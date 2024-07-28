import numpy as np

# Create the initial 10x2 array
day_number = np.arange(1, 11)
steps_walked = np.array([6012, 7079, 6886, 7230, 4598, 5564, 6971, 7763, 8032, 9569])
data = np.column_stack((day_number, steps_walked))

print("Original data:")
print(data)
print()

# Add 2000 steps to all observations
data[:, 1] += 2000

print("Data after adding 2000 steps:")
print(data)
print()

# Return steps walked if more than 9000
steps_over_9000 = data[data[:, 1] > 9000]
print("Days with over 9000 steps:")
print(steps_over_9000)
print()

# Print array with steps walked in sorted order
sorted_data = data[data[:, 1].argsort()]
print("Data sorted by steps walked:")
print(sorted_data)
print()

# Additional analysis
total_steps = np.sum(data[:, 1])
average_steps = np.mean(data[:, 1])
max_steps = np.max(data[:, 1])
min_steps = np.min(data[:, 1])

print(f"Total steps walked: {total_steps}")
print(f"Average steps per day: {average_steps:.2f}")
print(f"Maximum steps walked in a day: {max_steps}")
print(f"Minimum steps walked in a day: {min_steps}")
print()

# Count days reaching the 10000 steps goal
days_reached_goal = np.sum(data[:, 1] >= 10000)
print(f"Number of days Lee reached his goal of 10000 steps: {days_reached_goal}")

# Q1. Select the person who is neither the shortest nor
# tallest from each group of 5
# Problem: You have 20 people split into 4 groups of 5. Pick the (3rd tallest) from each group.

import numpy as np

heights = np.array([160, 170, 180, 150, 165,
                    175, 165, 185, 160, 170,
                    155, 165, 160, 170, 180,
                    180, 190, 185, 175, 160])

groups = heights.reshape(4, 5)
sorted_groups = np.sort(groups, axis=1)
third_tallest = sorted_groups[:, 2]

print(third_tallest)


# Q2. Get top 2 tallest from each group of 4 people
# heights = np.array([160, 170, 180, 150,
# 175, 165, 185, 160,
# 155, 165, 160, 170])

heights = np.array([160, 170, 180, 150,
                    175, 165, 185, 160,
                    155, 165, 160, 170])

groups = heights.reshape(3, 4)
sorted_groups = np.sort(groups, axis=1)
top_2_tallest = sorted_groups[:, -2:]
print(top_2_tallest)

# Q4. From each group of 3, pick only tallest
# heights = np.array([160, 170, 180,
# 175, 185, 165,
# 155, 165, 150])

import numpy as np

heights = np.array([160, 170, 180,
                    175, 185, 165,
                    155, 165, 150])

groups = heights.reshape(3, 3)
tallest = np.max(groups, axis=1)
print(tallest)

# Q5. From each group of 4, return height and
# original index of the shortest person
# heights = np.array([
# 160, 170, 150, 180,
# 175, 165, 155, 185
# ])

import numpy as np

heights = np.array([
    160, 170, 150, 180,
    175, 165, 155, 185
])

groups = heights.reshape(-1, 4)

min_indices = np.argmin(groups, axis=1)
original_indices = min_indices + np.arange(groups.shape[0]) * 4
shortest_heights = heights[original_indices]
results = list(zip(shortest_heights, original_indices))

print(results)

# Q6. From each group of 5, return second
# shortest person
# import numpy as np
# heights = np.array([
# 160, 170, 150, 180, 165,
# 175, 165, 185, 160, 170,
# 155, 165, 160, 170, 180
# ])

import numpy as np

heights = np.array([
    160, 170, 150, 180, 165,
    175, 165, 185, 160, 170,
    155, 165, 160, 170, 180
])

groups = heights.reshape(-1, 5)
sorted_groups = np.sort(groups, axis=1)
second_shortest = sorted_groups[:, 1]
print(second_shortest)


# Q7. For each group of 4, return all but the
# tallest person
# python
# CopyEdit
# heights = np.array([
# 160, 170, 150, 180,
# 175, 165, 155, 185,
# 165, 150, 155, 160
# ])

import numpy as np

heights = np.array([
    160, 170, 150, 180,
    175, 165, 155, 185,
    165, 150, 155, 160
])

groups = heights.reshape(-1, 4)
sorted_groups = np.sort(groups, axis=1)
all_but_tallest = sorted_groups[:, :-1]
print(all_but_tallest)

# Q8. From each group of 6, return the median
# height
# heights = np.array([
# 160, 170, 150, 180, 165, 155,
# 175, 165, 185, 160, 170, 155
# ])

import numpy as np

heights = np.array([
    160, 170, 150, 180, 165, 155,
    175, 165, 185, 160, 170, 155
])

groups = heights.reshape(-1, 6)
sorted_groups = np.sort(groups, axis=1)
medians = (sorted_groups[:, 2] + sorted_groups[:, 3]) / 2
print(medians)


# Q9. From each group of 5, return height gap
# between tallest and shortest
# heights = np.array([
# 160, 170, 150, 180, 165,
# 175, 185, 155, 160, 170
# ])

import numpy as np

heights = np.array([
    160, 170, 150, 180, 165,
    175, 185, 155, 160, 170
])

groups = heights.reshape(-1, 5)
height_gaps = np.max(groups, axis=1) - np.min(groups, axis=1)
print(height_gaps)

# Q10. From each group of 3, return person
# whose height is closest to the group average
# heights = np.array([
# 160, 170, 165,
# 180, 190, 175,
# 155, 160, 150
# ])

import numpy as np

heights = np.array([
    160, 170, 165,
    180, 190, 175,
    155, 160, 150
])

groups = heights.reshape(-1, 3)

group_means = np.mean(groups, axis=1)
diffs = np.abs(groups - group_means[:, np.newaxis])
closest_indices = np.argmin(diffs, axis=1)
closest_heights = groups[np.arange(groups.shape[0]), closest_indices]
print(closest_heights)

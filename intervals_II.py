'''
Given a collection of three intervals, check if they are overlapping and return the overlapping intervals.

#?Example 1:

Given a list of intervals [1,3],[2,6],[8,10]

return a list of intervals [1,6],[8,10]

#?Example 2:

Given a list of intervals [1,3],[2,6],[5,10],

return a list of intervals [1,10]

You can assume the input intervals are sorted.
'''
'''
res = []
if intervals[0][1] and intervals[1][0] do not overlap:
  res.append(intervals[0])
  res.append(intervals[1])
else:
  if intervals[0][1] > intervals[1][1]:
    res.append(intervals[0])
  else:
    res.append([intervals[0][0], intervals[1][1]])

if res[len(res) - 1][1] and intervals[2][0] do not overlap:
  res.append(intervals[2])
else:
  if res[len(res) - 1][1] < intervals[2][1]:
    res[len(res) - 1][1] = intervals[2][1]  else:



'''


def merge_intervals_II(intervals):
  res = []

  if intervals[0][1] < intervals[1][0]:
    res.append(intervals[0])
    res.append(intervals[1])
  else:
    if intervals[0][1] > intervals[1][1]:
      res.append(intervals[0])
    else:
      res.append([intervals[0][0], intervals[1][1]])

  if res[len(res) - 1][1] < intervals[2][0]:
    res.append(intervals[2])
  else:
    if res[len(res) -1][1] > intervals[2][1]:
      return res
    else:
      res[len(res) -1][1] = intervals[2][1]
  return res



print(merge_intervals_II([






[3, 8], [7, 10], [9, 15]]))

num_records = 2
counts = {}
for i in range(num_records):
  record = input().split()
  candidate = record[0]
  current = int(record[1])
  if candidate in counts:
    counts[candidate] += current
  else:
    counts[candidate] = current

sorted_candidates = sorted(counts.keys())

for candidate in sorted_candidates:
  print(candidate, counts[candidate])

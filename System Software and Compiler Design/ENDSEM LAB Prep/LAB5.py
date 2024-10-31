transition_table = {
  'A': {'a':'B', 'b':'A'},
  'B': {'a':'B', 'b':'C'},
  'C': {'a':'B', 'b':'D'},
  'D': {'a':'B', 'b':'A'},
}
start = 'A'
end = 'D'
input_str = "aabb"

states = [start]
for x in input_str:
  for trans, state in transition_table[states[-1]].items():
    if trans == x:
      states.append(state)

if states[-1] == end:
  print("accepted")
else:
  print("rejected")

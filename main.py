from PriorityQueue import PriorityQueue
from State import State

def turn_state_into_array(init):
  state_array = [0 for i in range(9)]
  for i in range(3):
    for j in range(3):
      state_array[i*3+j] = init.matrix[i][j]

  return state_array

def is_solvable(init):
  cont = 0
  array = turn_state_into_array(init)

  for i in range(8):
    for j in range(i+1, 9):
      if array[i] != 0 and array[j] != 0 and array[i] > array[j]:
        cont += 1

  return cont%2 == 0

def gen_children(state, children):
  i, j = state.get_empty_space()

  if i < 2:
    s = State(state)
    s.set_parent(state)
    s.move_down(i, j)

    if not s.compare(state):
      children.append(s)

  if i > 0:
    s = State(state)
    s.set_parent(state)
    s.move_up(i, j)

    if not s.compare(state):
      children.append(s)
  
  if j < 2:
    s = State(state)
    s.set_parent(state)
    s.move_right(i, j)

    if not s.compare(state):
      children.append(s)

  if j > 0:
    s = State(state)
    s.set_parent(state)
    s.move_left(i, j)

    if not s.compare(state):
      children.append(s)

def print_path(state):
  if state != None:
	  print_path(state.parent)
  state.print_state()  

def main():
  init_state = State()
  goal_state = State()
  init_state.gen_random_state()
  goal_state.gen_goal_state()

  print('Initial')
  init_state.print_state()
    

#  goal_state = State()
#  goal_state.gen_goal_state()
#  print('Goal')
#  goal_state.print_state()

if __name__ == "__main__":
	main()

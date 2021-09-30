from PriorityQueue import PriorityQueue
from State import State
from Search import Search

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

def print_path(state):
  if state.parent != None:
	  print_path(state.parent)
  state.print_state()

def menu(state):
  print ("Input 1 - input a state\nInput 2 - generate a random state\n")
  choice = int(input())
  if choice == 1:
    state.input_state()
  elif choice == 2:
    state.gen_random_state()
  else:
    menu(state)

def print_result(state, opened_left, visited):
  print_path(state)
  print('Number of states left as opened: ' + str(opened_left))
  print('Number of visited states: ' + str(len(visited)))
  print("\n--------------------------------------------------------------------------------------")

def main(): 
  init_state = State()
  menu(init_state)
  
  goal_state = State()
  goal_state.gen_goal_state()

  print('Initial state')
  init_state.print_state()
  print('Goal state')
  goal_state.print_state()

  print('Is solvable: ' + str(is_solvable(init_state)))
  print("\n--------------------------------------------------------------------------------------")

  visited = []

  if is_solvable(init_state):
    s = Search()
  
    print("\nA* with h1 (sum of pieces out of place):\n")
    state, opened_left = s.a_star(init_state, goal_state, visited)
    print_result(state, opened_left, visited)

    print("\nA* with h2 (Euclidean distance):\n")
    state, opened_left = s.a_star_h2(init_state, goal_state, visited)
    print_result(state, opened_left, visited)
    
    print("\nGreedy with h3 (Manhattan distance):\n")
    state, opened_left = s.greedy(init_state, goal_state, visited)
    print_result(state, opened_left, visited)
    
    print("\nBFS:\n")
    state, opened_left = s.bfs(init_state, goal_state, visited)
    print_result(state, opened_left, visited)

  else:
    print("\nNot solvable. Initial state and goal state are not in the same connected component.")

if __name__ == "__main__":
	main()

import copy
import random
import math

# Def dict to final state positions
indexes = {
  '0': (2, 2),
  '1': (0, 0),
  '2': (1, 0),
  '3': (2, 0),
  '4': (0, 1),
  '5': (1, 1),
  '6': (2, 1),
  '7': (2, 0),
  '8': (2, 1)
}
class State:
  def __init__(self, parent=None):
    self.parent = parent
    self.gn = 0
    self.fn = 0
    self.h1 = 0
    self.h2 = 0
    self.h3 = 0

    if self.parent == None:
      self.matrix =  [ [ 0 for i in range(3) ] for j in range(3) ]
    else:
      self.matrix = copy.deepcopy(parent.matrix)

  def get_parent(self):
    return self.parent
  
  def set_parent(self, parent):
    self.parent = parent

  def get_fn(self):
    return self.fn

  def set_fn(self, fn):
    self.fn = fn

  def get_gn(self):
    return self.gn

  def set_gn(self, value):
    self.gn = value

  def get_h1(self):
    return self.h1

  def get_h2(self):
    return self.h2
  
  def get_h3(self):
    return self.h3

  def get_empty_space(self):
    for i in range(3):
      for j in range(3):
        if self.matrix[i][j] == 0:
          return i, j

  def input_state(self):
    for i in range(3):
      self.matrix[i] = [int(j) for j in input().strip().split(" ")]

  def gen_random_state(self):
    blocks = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(blocks)
    
    for i in range(3):
      for j in range(3):
        self.matrix[i][j] = blocks.pop()

  def gen_goal_state(self):
    blocks = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for i in range(3):
      for j in range(3):
        self.matrix[i][j] = blocks.pop(0)

  def print_state(self):
    for i in range(3):
      for j in range(3):
        if self.matrix[i][j] == 0:
          print('[ ]', end=" ")
        else:
          print('[' + str(self.matrix[i][j]) + ']', end=" ")
      print()
    print()

  def move_down(self, i, j):
    self.matrix[i][j] = self.matrix[i+1][j]
    self.matrix[i+1][j] = 0

  def move_up(self, i, j):
    self.matrix[i][j] = self.matrix[i-1][j]
    self.matrix[i-1][j] = 0
      
  def move_right(self, i, j):
    self.matrix[i][j] = self.matrix[i][j+1]
    self.matrix[i][j+1] = 0
      
  def move_left(self, i, j):
    self.matrix[i][j] = self.matrix[i][j-1]
    self.matrix[i][j-1] = 0

  def compare(self, other):
    for i in range(3):
      for j in range(3):
        if self.matrix[i][j] != other.matrix[i][j]:
          return False
    
    return True

  def calc_gn(self):
    if self.parent != None:
      self.set_gn(self.parent.get_gn() + 1)

  def calc_h1(self, goal_state):
    for i in range(3):
      for j in range(3):
        if self.matrix[i][j] != goal_state.matrix[i][j]:
          self.h1 += 1
  
  def calc_h2(self, goal_state):
    sum = 0
    for i in range(3):
      for j in range(3):
        i_j = indexes[str(self.matrix[i][j])]
        goal_i = i_j[0]
        goal_j = i_j[1]
        sum += abs(i - goal_i) + abs(goal_j - j)
    self.h2 = sum
  
  def calc_h3(self, goal_state):
    sum = 0
    for i in range(3):
      for j in range(3):
        i_j = indexes[str(self.matrix[i][j])]
        goal_i = i_j[0]
        goal_j = i_j[1]
        sum += math.sqrt((goal_i - i)**2 + (goal_j - j)**2)
    self.h3 = sum

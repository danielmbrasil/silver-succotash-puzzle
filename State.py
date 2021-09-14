import copy
import random

class State:
  def __init__(self, parent=None):
    if parent == None:
      self.matrix =  [ [ 0 for i in range(3) ] for j in range(3) ]
    else:
      self.matrix = copy.deepcopy(parent.matrix)

  def set_parent(self, parent):
    self.parent = parent

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
    
  def get_empty_space(self):
    for i in range(3):
      for j in range(3):
        if self.matrix[i][j] == 0:
          return i, j

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

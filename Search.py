from State import State
from PriorityQueue import PriorityQueue
import copy

class Search:
  def gen_children(self, state, children):
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

  def bfs(self, init_state, goal_state, visited):
    children = []
    opened = []
    opened.append(init_state)
    visited.clear()

    while len(opened) > 0:
      s = opened.pop(0)
      
      if s.compare(goal_state):
        return s, len(opened)

      children.clear()
      self.gen_children(s, children)
      
      visited.append(s)

      if len(children) > 1:
        states = copy.deepcopy(opened)
        states.extend(visited)
        for i in states:
          for c in children:
            if (i.compare(c)):
              children.remove(c)
        opened.extend(children) 
    return None, None

  def greedy(self, init_state, goal_state, visited):
    visited.clear()
    children = []
    
    init_state.calc_h3(goal_state)
    init_state.set_fn(init_state.get_h3())

    q = PriorityQueue()
    q.push(init_state)

    while not q.is_empty():
      s = q.pop()

      if s.compare(goal_state):
        return s, len(q.get_queue())
      
      children.clear()
      self.gen_children(s, children)

      visited.append(s)
      if len(children) > 1:
        states = copy.deepcopy(q.get_queue())
        states.extend(visited)
        for i in states:
          for c in children:
            if (i.compare(c)):
              children.remove(c)
        for c in children:
          c.calc_h3(goal_state)
          c.set_fn(c.get_h3())
          q.push(c)
    return None, None

  def a_star(self, init_state, goal_state, visited):
    visited.clear()
    children = []
    
    init_state.calc_gn()
    init_state.calc_h1(goal_state)
    init_state.set_fn(init_state.get_gn() + init_state.get_h1())

    q = PriorityQueue()
    q.push(init_state)

    while not q.is_empty():
      s = q.pop()

      if s.compare(goal_state):
        return s, len(q.get_queue())
      
      children.clear()
      self.gen_children(s, children)

      visited.append(s)
      if len(children) > 1:
        states = copy.deepcopy(q.get_queue())
        states.extend(visited)
        for i in states:
          for c in children:
            if (i.compare(c)):
              children.remove(c)
        for c in children:
          c.calc_gn()
          c.calc_h1(goal_state)
          c.set_fn(c.get_gn() + c.get_h1())
          q.push(c)
    return None, None

  def a_star_h2(self, init_state, goal_state, visited):
    visited.clear()
    children = []

    init_state.calc_gn()
    init_state.calc_h2(goal_state)
    init_state.set_fn(init_state.get_gn() + init_state.get_h2())

    q = PriorityQueue()
    q.push(init_state)
    
    while not q.is_empty():
      s = q.pop()

      if s.compare(goal_state):
        return s, len(q.get_queue())
      
      children.clear()
      self.gen_children(s, children)

      visited.append(s)

      if len(children) > 1:
        states = copy.deepcopy(q.get_queue())
        states.extend(visited)
        for i in states:
          for c in children:
            if (i.compare(c)):
              children.remove(c)
        for c in children:
          c.calc_gn()
          c.calc_h2(goal_state)
          c.set_fn(c.get_gn() + c.get_h2())
          q.push(c)

    return None, None

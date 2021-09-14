class PriorityQueue:
  def __init__(self) -> None:
    self.queue = []

  def is_empty(self):
    return len(self.queue) == 0

  def sort_func(self, e):
    return e.getFn()

  def push(self, element):
    self.queue.append(element)
    self.queue.sort(key=self.sort_func)

  def pop(self):
    if len(self.queue) > 0:
      return self.queue.pop(0)

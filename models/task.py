class task:
  def __init__(self, title, description, status):
    self.title = title
    self.description = description
    self.status = status
  
  def describe_task(self):
    print(f'title: {self.title} task: {self.description} status: {self.status}')

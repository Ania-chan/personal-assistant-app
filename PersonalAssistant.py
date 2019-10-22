class PersonalAssistant:
  def __init__(self, todos):
    self.contacts = {'Agata': '080-8273-9484', 'Agnieszka': '080-3425-92749', 'Shigeru': '080-7253-8833', 'Pawel': '080-4620-0384', 'Beata': '080-2795-3252'}
    self.birthdays = {"Shigeru":"01/07/85!", "Agata": "12/29/88!", "Agnieszka": "07/15/95!"
    }
    self.todos = todos

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "There's no contact with this name!"

  def add_contact(self, name, position):
    if name in self.contacts:
      return "Contact already exists!"
    else:
      self.contacts[name] = position

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name, None)
    else:
      return "That contact isn't saved."

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      index = self.todos.index(todo_item)
      self.todos.pop(index)
    else:
      return "Todo is not in the list!"

  def get_todo(self):
    return self.todos

  def get_birthday(self, name):
    if name in self.birthdays:
      return self.birthdays[name]
    else:
      return "Can't find a birthday for this person..."

  def add_birthday(self, name, birthday):
    if name in self.burthdays:
      return "Birthday is already saved for this person"
    else:
      self.birthday[name] = birthday

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
    else:
      return "There is no birthday data for this person"

data = ["one", "1", "two", "2", "ten", "10", "15", "-2", "some long text goes here", "16.9", "&"]
def get_max_value(data):
  l = list()
  for element in data:
    m = element.replace(" ", "")
    if not m.isalpha() and not m=='&':
     l.append(float(element))
  return int(max(l))
print(get_max_value(data))

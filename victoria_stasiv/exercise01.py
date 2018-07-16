data = ["one", "1", "two", "2", "ten", "10", "15", "-2", "some long text goes here", "16.9", "&"]
def get_max_value(data):
  all = list()
  l = list()
  for element in data:
    m = element.replace(" ", "")
    k = m.split('.')
    lst =[k[0]]
    for l in k:
     if m.lstrip('-').isdigit() or l.isdigit():
        all.append(float(m));
  print(int(max(all)))

get_max_value(data)

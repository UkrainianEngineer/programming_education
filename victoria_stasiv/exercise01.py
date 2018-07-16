import math
data = ["one", "1", "two", "2", "ten", "10", "15", "-2", "some long text goes here", "16.9", "&"]
def get_max_value(data):
  all = list()
  for element in data:
 
    if element.isdigit():
      all.append(int(element))
 
    
    if "." in element:
      val = math.floor(float(element))
      all.append(int(val))
 
    
    if "-" in element:
      if element.lstrip('-').isdigit():
        all.append(int(element))
 
  print(max(all))
 
get_max_value(data)

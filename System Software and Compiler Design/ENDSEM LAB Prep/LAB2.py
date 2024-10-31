input_str = '''
int a  , b = 5 ;
char c = 'd' ;
double Add (double_x,int_y)
'''
keywords = ["public", "static", "void", "main", "int", "double"]
operators = "+-*%/="

for x in input_str.split(';'):
  data_type = ""
  for y in x.split():
    if y in keywords and len(y)>1:
      data_type = y
    elif y.isalpha() and y not in "=,":
      identifier = y
    elif y.isdigit() or "'" in y:
      print(f" identifier: {identifier}  data_type:  {data_type}  value: {y} ")

    if y == ',':
      print(f" identifier: {identifier}  data_type:  {data_type}  value: 0 ")
      identifier = ""

    parameters = 0
    if "(" in y:
      y = y.replace("_"," ")
      y = y.replace("(","( ")
      y = y.replace(")"," )")
      y = y.replace(",","  , ")
      parameter_types = []
      for z in y.split():
        if z in keywords:
          parameter_types.append(z)
          parameters += 1
        if ")" in z:
          print(f" identifier: {identifier}  return_type:  {data_type}  parameters: {parameters}  Types_of_parameter: {parameter_types} ")
          identifier = ""
          break

  data_type = ""

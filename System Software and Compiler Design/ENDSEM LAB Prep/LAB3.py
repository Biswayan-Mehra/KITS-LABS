file_path = "ENDSEM LAB Prep\LAB3_input.txt"

with open(file_path, "r") as file:
        input_str = file.read()

dict = {}
for x in input_str.split("\n"):
  if "#define" in x:
    for y in x.split():
      y = y.replace("("," ( ")
      y = y.replace(")"," )")
      for z in y.split():
        if len(z)>1 and z not in "#define":
          if "=" in z:
            z = z.replace("="," = ")
            z = z.replace("/"," / ")
            z += " ;"
            dict[namTab] = z.replace(defTab, "_")
          else:
            namTab = z
        elif len(z)==1 and z not in "()":
          defTab = z
    continue

  flag = 0
  name = ""
  variable = ""
  for y in x.split():
    for key, value in dict.items():
      if key in y:
        flag = 1
        name = key
      else:
        break

  if flag == 1:
    for y in x.split():
      if "(" in y:
          y = y.replace("(","")
          y = y.replace(")","")
          variable += y
    print(dict[name].replace("_", variable))
    flag = 0
  else:
    print(x)


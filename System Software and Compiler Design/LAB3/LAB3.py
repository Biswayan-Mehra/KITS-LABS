with open('input_data.txt', 'r') as file:
    lines = file.readlines()

name_to_func = {}
variables = {}

for line in lines:
    if '#define' in line:
        if '(' in line:
            name, params = line.split('(')
            name = name.replace('#define', '').strip()
            params = params.split(')')[0].replace(' ', '').split(',')
            func_body = line.split('{', 1)[1].split('}', 1)[0].strip()
            name_to_func[name] = f"{func_body}({','.join(params)})"
        else:
            name, value = line.replace('#define', '').replace(';', '').split()
            variables[name] = value
    else:
        for var, val in variables.items():
            line = line.replace(var, val)
        if '(' in line:
            func_name = line.split('(')[0].strip()
            if func_name in name_to_func:
                print(name_to_func[func_name])
        else:
            print(line.strip())

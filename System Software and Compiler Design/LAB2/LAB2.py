import re

program_code = '''
int a, b=5;
char c='d';
double Add(double x, double y)
'''

symbol_table = {
    'ID': [],
    'DataType': [],
    'ReturnType': [],
    'Initial Value': [],
    'No. of Parameters': [],
    'Parameter Types': []
}

variables = re.findall(r'(\w+)\s+([\w, ]+)(?:;|\s*=\s*([^;]+))', program_code)
functions = re.findall(r'(\w+)\s+(\w+)\((.*?)\)', program_code)

for data_type, var_list, initial_value in variables:
    for name in var_list.split(','):
        symbol_table['ID'].append(name.strip())
        symbol_table['DataType'].append(data_type)
        symbol_table['ReturnType'].append('')
        symbol_table['Initial Value'].append(initial_value.strip() if initial_value else '0')
        symbol_table['No. of Parameters'].append('')
        symbol_table['Parameter Types'].append('')

for return_type, func_name, params in functions:
    symbol_table['ID'].append(func_name)
    symbol_table['DataType'].append('Function')
    symbol_table['ReturnType'].append(return_type)
    param_types = ', '.join(p.split()[0] for p in params.split(',')) if params.strip() else ''
    symbol_table['No. of Parameters'].append(str(param_types.count(',') + 1))
    symbol_table['Parameter Types'].append(param_types)
    symbol_table['Initial Value'].append('')

symbol_table_output = 'ID\t\tDataType\t\tReturnType\tInitial Value\tNo. of Parameters\tParameter Types\n'
symbol_table_output += '\n'.join('{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format(
    symbol_table['ID'][i],
    symbol_table['DataType'][i],
    symbol_table['ReturnType'][i],
    symbol_table['Initial Value'][i],
    symbol_table['No. of Parameters'][i],
    symbol_table['Parameter Types'][i]
) for i in range(len(symbol_table['ID'])))

print(symbol_table_output.strip())
def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5: return 'Error: Too many problems.'
    arr = {'first': [],
           'sec': [],
           'third': []
           }

    for problem in problems:
        first_arg, operator, sec_arg = problem.split()
        if operator != '+' and operator != '-': return "Error: Operator must be '+' or '-'."
        if not first_arg.isdigit() or not sec_arg.isdigit(): return "Error: Numbers must only contain digits."
        if len(first_arg) > 4 or len(sec_arg) > 4: return "Error: Numbers cannot be more than four digits."
        size = len(first_arg) if len(first_arg) > len(sec_arg) else len(sec_arg)
        size += 2
        while len(first_arg) < size:
            first_arg = ' ' + first_arg
        while len(sec_arg) < size - 1:
            sec_arg = ' ' + sec_arg
        sec_arg = operator + sec_arg
        
        arr['third'].append('-' * size)
        arr['first'].append(first_arg)
        arr['sec'].append(sec_arg)

    arranged_problems = '    '.join(arr['first']) + "\n" + '    '.join(arr['sec']) + '\n' + '    '.join(arr['third'])
    if answer:
        a = []
        for i, value in enumerate(arr['first']):
            s = str(eval(value + arr['sec'][i]))
            while len(s) < len(value):
                s = ' ' + s
            a.append(s)
        arranged_problems += '\n' + '    '.join(a)
    return arranged_problems

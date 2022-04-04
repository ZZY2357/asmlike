#!/usr/bin/env python3
import sys
import re

memory = []
for i in range(64):
    memory.append(0)

next_line = 0
jump_marks = []

def run_line(code, line_number, lines):
    global next_line

    l = code.split()

    if l[0] == 'add':
        memory[int(l[1])] += 1
    if l[0] == 'write':
        memory[int(l[1])] = int(l[2])
    if l[0] == 'input_num':
        memory[int(l[1])] = int(input())
    if l[0] == 'input_char':
        memory[int(l[1])] = ord(input())
    if l[0] == 'jump':
        for i in jump_marks:
            if i[0] == l[1]:
                next_line = i[1]
                break
    if l[0] == 'jumpif':
        if memory[int(l[2])] != 0:
            for i in jump_marks:
                if i[0] == l[1]:
                    next_line = i[1]
                    break
    if l[0] == 'print_num':
        print(memory[int(l[1])], end='')
    if l[0] == 'print_char':
        print(chr(memory[int(l[1])]), end='')
    if l[0] == 'end':
        next_line = len(lines)

def run(code):
    global next_line
    lines = code.split('\n')

    for i in range(len(lines)):
        if lines[i].split()[0] == 'mark':
            jump_marks.append((lines[i].split()[1], i))

    while next_line < len(lines):
        run_line(lines[next_line], next_line, lines)
        next_line += 1

if sys.argv[1] == 'help':
    print('$ asmlike [file]')
else:
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        code = re.sub('(\n\n+)|(\n//.*\n)', '\n', f.read()).strip()
        if code != '':
            run(code)

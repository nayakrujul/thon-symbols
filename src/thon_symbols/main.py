from math import *
from string import *
from thon_symbols.List import List

def run(code, _stack=()):
    index = 0
    stack = List(_stack)
    while index < len(code):
        char = code[index]
        if char in '0123456789.':
            string = char
            index += 1
            try:
                while code[index] in '0123456789.':
                    string += code[index]
                    index += 1
            except:
                pass
            index -= 1
            stack.push(eval(string))
        elif char == '"':
            string = char
            index += 1
            try:
                while code[index] != '"':
                    string += code[index]
                    index += 1
            except:
                pass
            string += code[index]
            stack.push(eval(string))
        elif char == 'ï':
            stack.push(int(input()))
        elif char == 'Ï':
            stack.push(list(map(int, input().split())))
        elif char == 'ş':
            stack.push(input())
        elif char == 'Ş':
            stack.push(input().split())
        elif char == 'Ś':
            stack.push(list(stack).copy())
        elif char == 'Σ':
            stack.push(List(stack.first(list)).sum)
        elif char == '∏':
            stack.push(List(stack.first(list)).product)
        elif char == '↑':
            stack.push(max(stack.first(list)))
        elif char == '↓':
            stack.push(min(stack.first(list)))
        elif char == '∧':
            stack.push(gcd(stack.first(list)))
        elif char == '∨':
            stack.push(lcm(stack.first(list)))
        elif char == ')':
            stack.push([])
        elif char == ';':
            stack.push(stack.first(list) + [stack.first(list, False)])
        elif char == '&':
            a, b = stack.first(list, k=2)
            stack.push(a + b)
        elif char == '←':
            a = stack.first((list, str))
            if isinstance(a, list):
                stack.push(list(reversed(a)))
            else:
                stack.push(''.join(reversed(a)))
        elif char == 'đ':
            stack.push(list(set(stack.first(list))))
        elif char == '[':
            a, b = stack.first(str, k=2)
            stack.push(b.split(a))
        elif char == ']':
            stack.push(stack.first(str).join(stack.first(list)))
        elif char == 'ṡ':
            stack.push(str(stack[0]))
        elif char == 'Ṡ':
            stack.push(list(map(str, stack.first(list))))
        elif char == 'í':
            stack.push(int(stack[0]))
        elif char == 'Í':
            stack.push(list(map(int, stack.first(list))))
        elif char == 'ŀ':
            stack.push(list(str(stack[0])))
        elif char == 'ŕ':
            a = stack.first(list).copy()
            a.remove(stack.first(list, False))
            stack.push(a)
        elif char == 'Ŕ':
            a = stack.first(list).copy()
            b = stack.first(list, False)
            while b in a:
                a.remove(b)
            stack.push(a)
        elif char == 'ř':
            stack.push(list(range(stack.first(int))))
        elif char == 'Ř':
            stack.push(list(range(len(stack.first((list, str))))))
        elif char == 'ⱡ':
            stack.push(len(stack.first((list, str))))
        elif char == '`':
            stack.push(stack.first((list, str))[stack.first(int)])
        elif char == '+':
            a, b = stack.first((int, float), k=2)
            stack.push(a + b)
        elif char == '-':
            a, b = stack.first((int, float), k=2)
            stack.push(a - b)
        elif char == '*':
            a, b = stack.first((int, float), k=2)
            stack.push(a * b)
        elif char == '/':
            a, b = stack.first((int, float), k=2)
            stack.push(a / b)
        elif char == '^':
            a, b = stack.first((int, float), k=2)
            stack.push(a ** b)
        elif char == '%':
            a, b = stack.first((int, float), k=2)
            stack.push(a % b)
        elif char == '£':
            a, b = stack.first((int, float), k=2)
            stack.push(list(divmod(a, b)))
        elif char == '>':
            a, b = stack.first((int, float), k=2)
            stack.push(a > b)
        elif char == '≥':
            a, b = stack.first((int, float), k=2)
            stack.push(a >= b)
        elif char == '<':
            a, b = stack.first((int, float), k=2)
            stack.push(a < b)
        elif char == '≤':
            a, b = stack.first((int, float), k=2)
            stack.push(a <= b)
        elif char == '=':
            stack.push(stack[0] == stack[1])
        elif char == '≠':
            stack.push(stack[0] != stack[1])
        elif char == '&':
            stack.push(stack[0] and stack[1])
        elif char == '|':
            stack.push(stack[0] or stack[1])
        elif char == '@':
            stack.push(bool(stack[0]) ^ bool(stack[1]))
        elif char == '~':
            stack.push(not stack[0])
        elif char == '?':
            if_true = ''
            index += 1
            while code[index] != ':':
                if_true += code[index]
                index += 1
            index += 1
            try:
                if_false = ''
                while code[index] != ';':
                    if_false += code[index]
                    index += 1
            except:
                pass
            if stack[0]:
                stack = run(if_true, stack)
            else:
                stack = run(if_false, stack)
        elif char == '{':
            string = ''
            index += 1
            try:
                while code[index] != '}':
                    string += code[index]
                    index += 1
            except:
                pass
            a = stack.first((list, str))
            for i in a:
                stack = run(string, [i] + stack)
        elif char == '\\':
            index += 1
            if isinstance(stack[0], str):
                stack[0] += code[index]
            else:
                stack.push(code[index])
        elif char == 'å':
            stack.push(ascii_lowercase)
        elif char == 'Å':
            stack.push(ascii_uppercase)
        elif char == 'Ḷ':
            a, b = stack.first(str, k=2)
            stack.push(b.ljust(stack.first(int), 2))
        elif char == 'Ṛ':
            a, b = stack.first(str, k=2)
            stack.push(b.rjust(stack.first(int), 2))
        elif char == 'ṕ':
            print(stack[0], end='')
        elif char == 'Ṕ':
            print(stack[0])
        else:
            if isinstance(stack[0], str):
                stack[0] += code[index]
            else:
                stack.push(code[index])
        index += 1
    return stack

def from_cmdline():
    code = input()
    out = run(code)[0]
    print(out)
    print('\n- - - - - - - - - -\n')
    print('Code Golf SE Submission:\n')
    print(f'# [Thon (Symbols)][1], {len(code)} [bytes][2]\n')
    print(f'```\n{code}\n```\n')
    print('  [1]: https://github.com/nayakrujul/thon-symbols')
    print('  [2]: https://github.com/nayakrujul/thon-symbols/blob/main/Codepage.md')

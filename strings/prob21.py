## https://www.hackerrank.com/challenges/text-wrap/problem


import textwrap

def wrap(string, max_width):
    wrapped_string = ''
    for i in range(0, len(string)):
        wrapped_string+= string[i]
        if((i+1) % max_width == 0):
           wrapped_string+= '\n'
    return wrapped_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# def wrap(string, max_width):
#     return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
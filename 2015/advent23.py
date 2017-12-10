#!/usr/bin/python


def run_program(program, registers):
  ip = 0
  while ip >=0 and ip < len(program):
    instr = program[ip]
    parts = instr.split(' ', 1)
    if parts[0] == 'hlf':
      registers[parts[1]] /= 2
    elif parts[0] == 'tpl':
      registers[parts[1]] *= 3
    elif parts[0] == 'inc':
      registers[parts[1]] += 1
    elif parts[0] == 'inc':
      registers[parts[1]] += 1
    elif parts[0] == 'jmp':
      offset = int(parts[1])
      ip += offset - 1
    elif parts[0] == 'jie':
      r, offset = parts[1].split(', ')
      if registers[r] % 2 == 0:
        ip += int(offset) - 1
    elif parts[0] == 'jio':
      r, offset = parts[1].split(', ')
      if registers[r] == 1:
        ip += int(offset) - 1
    else:
      raise Exception

    ip += 1
    print '%s -> ip: %s | %s' %  (instr.ljust(10), str(ip).ljust(3), registers)

def main():
  i = open('advent23')

  program = []
  for line in i:
    line = line.strip()
    program.append(line)

  print '--------- Part 1 -------------'
  registers = {'a': 0, 'b': 0}
  run_program(program, registers)
  print '--------- Part 2 -------------'
  registers = {'a': 1, 'b': 0}
  run_program(program, registers)

if __name__ == '__main__':
  main()

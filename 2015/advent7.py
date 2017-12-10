#!/usr/bin/python

class NoOut(Exception):
    pass

class Port(object):
    def __init__(self, wires, a, b=None):
        self._a = None
        self._b = None
        self.wires = wires
        try:
            self._a = int(a)
        except ValueError:
            self._a = a
        if not b:
            return
        try:
            self._b = int(b)
        except ValueError:
            self._b = b

    @property
    def a(self):
        if type(self._a) == int:
            return self._a
        if type(self.wires[self._a]) == int:
            return self.wires[self._a]
        raise NoOut

    @property
    def b(self):
        if type(self._b) == int:
            return self._b
        if type(self.wires[self._b]) == int:
            return self.wires[self._b]
        raise NoOut


class And(Port):
    def out(self):
        return self.a & self.b


class Or(Port):
    def out(self):
        return self.a | self.b


class Signal(Port):
    def out(self):
        return self.a


class LShift(Port):
    def out(self):
        return self.a << self.b


class RShift(Port):
    def out(self):
        return self.a >> self.b


class Not(Port):
    def out(self):
        return ~self.a

class Circuit(object):
    def solve(self):
        solved = False
        while not solved:
            solved = True
            for out, p in self.out_wires.iteritems():
                if type(p) == int:
                    continue
                try:
                    self.out_wires[out] = p.out()
                    print 'Solved %s: %d' % (out, p.out())
                except NoOut:
                    solved = False

    def build_circuit(self, i):
        self.out_wires = {}
        count = 0
        for line in i:
            count += 1
            line = line.strip()
            op, res = line.split(' -> ')
            print '----line %s' % line
            if op.startswith('NOT '):
                wire = op[len('NOT '):]
                self.out_wires[res] = Not(self.out_wires, wire)
                print 'NOT .%s. -> .%s.' % (wire, res)
                continue
            try:
                a, b = op.split(' AND ')
                self.out_wires[res] = And(self.out_wires, a, b)
                print '.%s. AND .%s. -> .%s.' % (a, b, res)
                continue
            except ValueError:
                pass
            try:
                a, b = op.split(' OR ')
                self.out_wires[res] = Or(self.out_wires, a, b)
                print '.%s. AND .%s. -> .%s.' % (a, b, res)
                continue
            except ValueError:
                pass
            try:
                a, b = op.split(' LSHIFT ')
                self.out_wires[res] = LShift(self.out_wires, a, b)
                print '.%s. L .%s. -> .%s.' % (a, b, res)
                continue
            except ValueError:
                pass
            try:
                a, b = op.split(' RSHIFT ')
                self.out_wires[res] = RShift(self.out_wires, a, b)
                print '.%s. R .%s. -> .%s.' % (a, b, res)
                continue
            except ValueError:
                pass
            try:
                a = int(op)
            except ValueError:
                a = op
            self.out_wires[res] = Signal(self.out_wires, a)
            print '.%s. -> .%s.' % (a, res)
        print 'Lines %d ports %d' % (count, len(self.out_wires))

def main():
    i = open('advent7')
    c = Circuit()
    c.build_circuit(i)
    c.solve()

    i = open('advent7-2')
    c = Circuit()
    c.build_circuit(i)
    c.solve()

if __name__ == "__main__":
    main()

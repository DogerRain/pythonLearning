import foo
import sys;

a = [1, 'python']
a = 'a string'

def func():
    a = 1
    b = 257
    print(a + b)


print(a)

if __name__ == '__main__':
    func()
    result = foo.add(1, 2)
    print(result)

print('Python %s on %s' % (sys.version, sys.platform))


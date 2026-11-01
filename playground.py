x = 10        # int
y = 10.0      # float
z = "10"      # str
b = True      # bool
n = None      # NoneType

print(int(y), int(z), float(x), str(x), bool(0), bool(""))
# 10 10 10.0 10 False False

print(10 / 3, 10 // 3, 10 % 3, 2 ** 10)
# 3.3333333333333335 3 1 1024

# int("10.5")   # ValueError: invalid literal for int() with base 10: '10.5'
# Uncomment, read the traceback, then re-comment it.

a = [1, 2, 3]
b = a            # alias, NOT a copy
b.append(4)
print(a)         # [1, 2, 3, 4]

c = a.copy()     # or a[:]
c.append(99)
print(a, c)      # [1, 2, 3, 4] [1, 2, 3, 4, 99]

s = "hello"
# s[0] = "H"     # TypeError: 'str' object does not support item assignment
s2 = s.upper()   # strings are immutable; methods return new values
print(s, s2)     # hello HELLO

t = (1, 2, 3)
# t[0] = 9       # TypeError: 'tuple' object does not support item assignment

for i in range(3):
    print(i)
# 0
# 1
# 2

for i, ch in enumerate("abc"):
    print(i, ch)
# 0 a
# 1 b
# 2 c

for name, age in {"alice": 30, "bob": 25}.items():
    print(name, age)
# alice 30
# bob 25

n = 0
while n < 3:
    n += 1
# (no output — n ends at 3)

for v in [0, "", [], {}, None, "x", [0], 1]:
    print(repr(v), bool(v))
# 0 False
# '' False
# [] False
# {} False
# None False
# 'x' True
# [0] True
# 1 True

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ada"))                       # Hello, Ada!
print(greet("Ada", greeting="Hi"))        # Hi, Ada!
print(greet(greeting="Yo", name="Ada"))   # Yo, Ada!

def divide(a, b):
    if b == 0:
        return None
    return a / b

def total(*nums):
    return sum(nums)

def show(**kwargs):
    return kwargs

print(divide(10, 0), total(1, 2, 3), show(a=1, b=2))
# None 6 {'a': 1, 'b': 2}

def list_ops():
    xs = [3, 1, 2]
    xs.append(4)                        # xs = [3, 1, 2, 4]
    print(xs[0], xs[-1])                # 3 4
    xs.sort()                           # in-place -> xs = [1, 2, 3, 4]
    print(sorted(xs, reverse=True))     # [4, 3, 2, 1]  (new list; xs unchanged)
    xs.remove(3)                        # xs = [1, 2, 4]
    del xs[0]                           # xs = [2, 4]
    print(xs, len(xs), 1 in xs)         # [2, 4] 2 False

def dict_ops():
    d = {"a": 1}
    d["b"] = 2                          # d = {'a': 1, 'b': 2}
    print(d["a"], d.get("zz", 0))       # 1 0
    d["a"] = 10                         # d = {'a': 10, 'b': 2}
    for k, v in d.items():
        print(k, v)
    # a 10
    # b 2
    del d["a"]                          # d = {'b': 2}
    print(d, "b" in d, list(d.keys()))  # {'b': 2} True ['b']

def set_ops():
    s = {1, 2, 2, 3}                    # duplicates dropped -> {1, 2, 3}
    s.add(4)                            # s = {1, 2, 3, 4}
    print(s, 4 in s, len(s))            # {1, 2, 3, 4} True 4
    s.discard(99)                       # no error (remove(99) would KeyError)
    print({1, 2, 3} & {2, 3, 4},
          {1, 2, 3} | {2, 3, 4})
    # {2, 3} {1, 2, 3, 4}

list_ops(); dict_ops(); set_ops()


a = [1, 2]
b = [1, 2]
print(a == b)                    # True   (value equality)
print(a is b)                    # False  (different objects)
print(None is None, [] is [])    # True False
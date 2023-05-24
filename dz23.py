import itertools

def permutations_generator(s):
  for a in itertools.permutations(s):
    yield ''.join(a)

print(list(permutations_generator('abc')))
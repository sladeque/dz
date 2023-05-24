m = [1,7,9,3,2,8,5,6,4,

4,3,8,6,5,9,1,7,2,

2,5,6,7,1,4,3,8,9,

3,2,4,8,9,1,7,5,6,

7,9,5,4,3,6,2,1,8,

8,6,1,2,7,5,9,4,3,

5,8,2,1,4,3,6,9,7,

9,4,7,5,6,2,8,3,1,

6,1,3,9,8,7,4,2,5]

def get_row(n):
  start = n*9
  end = start + 9
  return m[start:end]

def get_column(n):
  result = []
  for i in range(9):
    result.append(m[i*9+n])
  return result

def get_squares():
    result = []
    for i in range(9):
        start = i*9
        end = start + 9
        sub_list = m[start:end]

        square = []
        for j in range(3):
            square.append(sub_list[j*3:j*3+3])

        result.append(square)
    return result
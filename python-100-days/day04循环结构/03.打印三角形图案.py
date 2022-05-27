"""
打印三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""

row = int(input('请输入行数：'))

for i in range(1, row + 1):
    for _ in range(1, i + 1):
        print('*', end='')
    print('')


for i in range(1, row + 1):
    for j in range(1, row + 1):
        if j < row - i +1:
            print(' ', end='')
        else:
            print('*', end='')
    print()


for i in range(1, row + 1):
    for j in range(row - i):
        print(' ', end='')

    for j in range(2 * i - 1):
        print('*', end='')
    print('')

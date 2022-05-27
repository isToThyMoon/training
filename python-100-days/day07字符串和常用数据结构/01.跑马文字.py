import os
import time


# 需要在terminal中运行
def main():
    li = '南京欢迎你啊……'

    while True:
        os.system('clear')
        print(li)
        time.sleep(0.2)
        li = li[1:] + li[0]


if __name__ == '__main__':
    main()

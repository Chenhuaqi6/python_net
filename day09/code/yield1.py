def fun():
    print("开始生成器")
    # for i in range(5)
    #     yield i
    yield from range(5)
    print("结束生成器")

g = fun()
while True:
    try:
        print(next(g))
    except:
        break


# 无限循环，让用户决定何时退出系统
import cards_tools
import pymysql

while True:
    # TODO 显示功能菜单
    cards_tools.show_menu()

    action_str = input('请选择希望执行的操作: ')
    print('你选择的操作是 【%s】' % action_str)
    # 1，2，3是针对名片的操作
    if action_str in ["1", '2', '3']:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == '2':
            cards_tools.show_all()
        # 查询名片
        elif action_str == '3':
            cards_tools.search_card()


    # 0是退出系统
    elif action_str == "0":
        print('欢迎再次使用名片操作系统')
        break
        # 如果在开发程序时，不希望立刻编写分支内部的代码
        # 可以使用pass 关键字，表示一个占位符，能够保证代码结构正确
        # 程序运行时，pass不会执行任何操作
    # 其他内容输入错误， 需要提示用户
    else:
        print('您输入的不正确，请重新输入')







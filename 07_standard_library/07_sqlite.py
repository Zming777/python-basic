"""sqlite3（选学）：使用 Python 自带的小型关系数据库。

适用场景：本地工具需要保存、查询结构化数据。
本例使用内存数据库，程序结束即释放，不需要安装数据库服务。
"""

import sqlite3
from contextlib import closing


# closing 保证连接关闭；with connection 管理事务，不负责关闭连接。
with closing(sqlite3.connect(":memory:")) as connection:
    with connection:
        connection.execute(
            "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, pages INTEGER)"
        )
        books = [("Python 入门", 180), ("数据处理", 260), ("自动化脚本", 220)]
        connection.executemany(
            "INSERT INTO books (title, pages) VALUES (?, ?)", books
        )

        minimum = 200
        # 参数用 ? 占位并单独传入，避免把用户输入拼进 SQL。
        rows = connection.execute(
            "SELECT title, pages FROM books WHERE pages >= ? ORDER BY pages",
            (minimum,),  # 单元素元组需要逗号。
        ).fetchall()
        print("1. 页数不少于 200 的书：")
        for title, pages in rows:
            print(f"   {title}：{pages} 页")

        connection.execute(
            "UPDATE books SET pages = ? WHERE title = ?", (190, "Python 入门")
        )
        total = connection.execute("SELECT SUM(pages) FROM books").fetchone()[0]
        print("2. 修改后的总页数：", total)


# 小练习：增加一本书，使用 SELECT COUNT(*) 查询书的数量。

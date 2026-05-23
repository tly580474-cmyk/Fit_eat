"""
数据库迁移脚本：添加 account_id 字段
将现有用户的 username 复制到 account_id
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'light_diet.db')


def migrate():
    if not os.path.exists(DB_PATH):
        print(f"数据库文件不存在: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # 检查 account_id 列是否已存在
        cursor.execute("PRAGMA table_info(users)")
        columns = [col[1] for col in cursor.fetchall()]

        if 'account_id' in columns:
            print("account_id 列已存在，跳过迁移")
            return

        # 添加 account_id 列
        print("添加 account_id 列...")
        cursor.execute("ALTER TABLE users ADD COLUMN account_id VARCHAR(64)")

        # 将现有用户的 username 复制到 account_id
        print("迁移现有用户数据...")
        cursor.execute("UPDATE users SET account_id = username")

        # 创建唯一索引
        print("创建索引...")
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS ix_users_account_id ON users(account_id)")

        conn.commit()
        print("迁移完成！")

        # 验证迁移结果
        cursor.execute("SELECT id, account_id, username FROM users")
        users = cursor.fetchall()
        print(f"\n迁移后的用户数据 ({len(users)} 个用户):")
        for user in users:
            print(f"  ID: {user[0]}, Account ID: {user[1]}, Username: {user[2]}")

    except Exception as e:
        conn.rollback()
        print(f"迁移失败: {e}")
        raise
    finally:
        conn.close()


if __name__ == '__main__':
    migrate()

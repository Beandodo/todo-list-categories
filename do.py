# todo_app/
# ├── todo.py
# ├── todos.txt  # 儲存你的待辦清單
#%%
import os

DATA_DIR = "."  # 可改為你想儲存 todos 的資料夾

def get_existing_categories():
    """掃描目前資料夾中所有 todos_分類.txt 檔案，取得分類名稱"""
    files = os.listdir(DATA_DIR)
    categories = []
    for f in files:
        if f.startswith("todos_") and f.endswith(".txt"):
            category = f[len("todos_"):-len(".txt")]
            categories.append(category)
    return categories

def get_filename_by_category(category):
    return os.path.join(DATA_DIR, f"todos_{category}.txt")

def load_todos(filename="todos.txt"):  #讀取資料
    try:  #錯誤處理工具：try / except！
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_todos(todos, filename="todos.txt"): #儲存資料
    print(f"✔ 正在儲存到：{os.path.abspath(filename)}")
    with open(filename, "w", encoding="utf-8") as f:
        for item in todos:
            f.write(item + "\n")

def choose_category():
    categories = get_existing_categories()
    print("\n📁 目前已有的分類：")
    if categories:
        for i, cat in enumerate(categories, start=1):  #列舉
            print(f"{i}. {cat}")
    else:
        print("（目前尚無分類，請自行輸入）")

    category = input("請輸入你要使用的分類名稱（或輸入新名稱建立）：").strip()
    return category

def main():
    print("🗂️ 歡迎使用進階版多分類待辦清單")

    category = choose_category()
    filename = get_filename_by_category(category)
    todos = load_todos(filename)

    while True:
        print(f"\n📌 [{category}] 的待辦事項：")
        for i, item in enumerate(todos, start=1):
            print(f"{i}. {item}")

        print("\n選擇操作：")
        print("1. 新增待辦")
        print("2. 刪除待辦")
        print("3. 更換分類")
        print("4. 離開")

        choice = input("請輸入選項（1/2/3/4）：")

        if choice == "1":
            new_item = input("輸入新的待辦事項：")
            todos.append(new_item)
            save_todos(todos, filename)
        elif choice == "2":
            delete_index = int(input("輸入要刪除的編號：")) - 1
            if 0 <= delete_index < len(todos):
                deleted = todos.pop(delete_index)
                print(f"✅ 已刪除：{deleted}")
                save_todos(todos, filename)
            else:
                print("⚠️ 輸入錯誤")
        elif choice == "3":
            category = choose_category()
            filename = get_filename_by_category(category)
            todos = load_todos(filename)
        elif choice == "4":
            print("👋 Bye～期待再次使用！")
            break
        else:
            print("⚠️ 無效選項")

if __name__ == "__main__":
    main()
#%%
import os

# 假設你有一個檔案 todos.txt
path = os.path.abspath("todos.txt")
print("檔案絕對路徑：", path)
#%%
# 離開 Python 互動模式，回到終端機！
# 你可以這樣做：
# 按兩次 Ctrl + D（Mac 是 Cmd + D），或輸入 exit() 離開 Python 模式
# 回到正常終端機的情況（前面不是 >>>）
# 然後再輸入你想要執行的指令，例如：
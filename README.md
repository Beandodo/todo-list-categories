# 📋 分類式待辦清單小專案

一個使用 Python 製作的簡單 CLI 待辦事項應用程式，支援多種分類（如：工作、生活、學習），並能將資料儲存於不同檔案中。

---

## 🔧 技術使用

- Python 3
- 基礎檔案處理（File I/O）
- Git / GitHub 版本控管

---

## 🚀 功能介紹

- ✅ 新增待辦事項（依分類）
- 🗑 刪除指定編號的待辦事項
- 💾 自動儲存到對應的 txt 檔
- 🔁 多分類清單管理（如：`work.txt`、`life.txt`、`study.txt`）

---

## 📦 專案結構

todo-list-categories/ ├── do.py # 主程式 ├── work.txt # 工作清單 ├── life.txt # 生活清單 ├── study.txt # 學習清單 └── README.md # 專案說明文件

yaml
複製
編輯

---

## 🖥 使用方式

```bash
# 進入虛擬環境（如有）
source .venv/bin/activate

# 執行程式
python do.py
執行後可選擇分類、瀏覽待辦、進行新增或刪除，所有資料將自動存入對應分類的 .txt 檔。

📚 學習紀錄
這是我轉職學習 Python 過程中的第一個 CLI 小專案，練習了：

檔案操作

錯誤處理 try/except

清單處理與迴圈

Git 操作與上傳 GitHub

🙋‍♀️ 關於我
Hi，我是 Jiaxue，一位正在轉職成為 Python 後端工程師的學習者，歡迎來我的 GitHub 看更多作品，或交流學習心得！

👉 Beandodo GitHub


import tkinter as tk
from tkinter import messagebox
from discord_webhook import DiscordWebhook
from datetime import datetime, timedelta

def send_message():
    webhook_url = url_entry.get()
    message = message_entry.get()
    delay_minutes = delay_entry.get()
    repeat_times = repeat_entry.get()

    if not delay_minutes:
        delay_minutes = 0
    else:
        delay_minutes = int(delay_minutes)

    if not repeat_times:
        repeat_times = 1
    else:
        repeat_times = int(repeat_times)

    # メッセージ送信
    for i in range(repeat_times):
        webhook = DiscordWebhook(url=webhook_url, content=message)
        if delay_minutes > 0:
            time_to_send = datetime.now() + timedelta(minutes=delay_minutes)
            while datetime.now() < time_to_send:
                pass
        webhook.execute()

    messagebox.showinfo("送信", "messageが送信されました")

# GUIの作成
root = tk.Tk()
root.title("webhook spam")
root.iconbitmap()

instruction_label = tk.Label(root, text="by/M:p")
instruction_label.pack()

# URL入力欄
url_label = tk.Label(root, text="URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# メッセージ入力欄
message_label = tk.Label(root, text="Message:")
message_label.pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

# 送信時刻入力欄
delay_label = tk.Label(root, text="Delay (minutes):")
delay_label.pack()
delay_entry = tk.Entry(root, width=10)
delay_entry.pack()

# 送信回数入力欄
repeat_label = tk.Label(root, text="Repeat:")
repeat_label.pack()
repeat_entry = tk.Entry(root, width=10)
repeat_entry.pack()

# 送信ボタン
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
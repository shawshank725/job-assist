import threading
import tkinter as tk
from src.llm import create_cover_letter


def process_jd(text_box):
    jd_text = text_box.get("1.0", tk.END).strip()
    print("Gotten the JD... processing the information...")
    create_cover_letter(jd_text)


def start_processing(text_box):
    threading.Thread(
        target=process_jd,
        args=(text_box,),
        daemon=True
    ).start()


def main():
    root = tk.Tk()
    root.title("JD Processor")

    text_box = tk.Text(root, height=10, width=50)
    text_box.pack(padx=10, pady=10)

    process_button = tk.Button(
        root,
        text="Process JD",
        command=lambda: start_processing(text_box),
    )
    process_button.pack()

    root.mainloop()
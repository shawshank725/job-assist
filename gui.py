import tkinter as tk
from src.llm import send_jd_to_model
from src.llm import create_cover_letter

root = tk.Tk()
root.title("JD Processor")

label = tk.Label(root, text="Enter your JD")
label.pack(pady=10)

text_box = tk.Text(root, height=10, width=50)
text_box.pack(padx=10, pady=10)

def process_jd():
    jd_text = text_box.get("1.0", tk.END).strip()
    print("Gotten the JD... processing the information...")
    create_cover_letter(jd_text)
    pass

process_button = tk.Button(root, text="Process JD", command=process_jd, 
                          height=2, width=20, bg="#4CAF50", fg="white")
process_button.pack(pady=15)

root.mainloop()
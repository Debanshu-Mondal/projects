import tkinter as tk
from tkinter import filedialog, messagebox
import string
def pig_latin_word(word):
    vowels = 'aeiou'
    prefix_punct = ''
    suffix_punct = ''
    while word and word[0] in string.punctuation:
        prefix_punct += word[0]
        word = word[1:]
    while word and word[-1] in string.punctuation:
        suffix_punct = word[-1] + suffix_punct
        word = word[:-1]
    if not word:
        return prefix_punct + suffix_punct
    is_cap = word[0].isupper()
    word = word.lower()
    if word[0] in vowels:
        pig_word = word + "way"
    else:
        pig_word = word[1:] + word[0] + "ay"
    if is_cap:
        pig_word = pig_word.capitalize()
    return prefix_punct + pig_word + suffix_punct
def pig_latin_sentence(sentence):
    words = sentence.split()
    translated_words = [pig_latin_word(word) for word in words]
    return " ".join(translated_words)
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "r") as file:
            content = file.read()
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, content)
def save_file():
    output = output_text.get("1.0", tk.END).strip()
    if not output:
        messagebox.showinfo("No Output", "There is nothing to save.")
        return
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(output)
        messagebox.showinfo("Saved", f"File saved to:\n{filepath}")
def convert_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text to convert.")
        return
    translated = pig_latin_sentence(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)
root = tk.Tk()
root.title("Pig Latin Converter")
root.geometry("700x500")
tk.Label(root, text="Enter text or open a file:").pack(anchor="w", padx=10, pady=(10, 0))
input_text = tk.Text(root, height=10, wrap="word", font=("Arial", 12))
input_text.pack(fill="x", padx=10, pady=5)
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Open File", command=open_file).pack(side="left", padx=10)
tk.Button(btn_frame, text="Convert to Pig Latin", command=convert_text).pack(side="left", padx=10)
tk.Button(btn_frame, text="Save Output", command=save_file).pack(side="left", padx=10)
tk.Label(root, text="Pig Latin Output:").pack(anchor="w", padx=10, pady=(10, 0))
output_text = tk.Text(root, height=10, wrap="word", font=("Arial", 12), fg="blue")
output_text.pack(fill="x", padx=10, pady=5)
root.mainloop()

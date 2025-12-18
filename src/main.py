import json
import pyperclip
import tkinter as tk
from tkinter import scrolledtext, messagebox
from typing import Dict

def generate_code_snippet_from_text(text: str,
                                    title: str = "New code snippet",
                                    prefix: str = "snippet",
                                    description: str = "Code snippet description") -> str:
    """Return a JSON string for a VSCode snippet built from `text`."""
    lines = text.splitlines() or [""]
    inner = {
        "prefix": prefix,
        "body": lines,
        "description": description
    }
    inner_json = json.dumps(inner, indent=2, ensure_ascii=False)
    title_json = json.dumps(title, ensure_ascii=False)
    return f"{title_json}: {inner_json}"

class SnippetGeneratorGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("VS Code Snippet Generator")
        self.root.geometry("600x500")
        
        # Title
        tk.Label(root, text="VS Code Snippet Generator", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Title input
        title_frame = tk.Frame(root)
        title_frame.pack(anchor="w", padx=20, pady=5)
        tk.Label(title_frame, text="Snippet Title:", width=15, anchor="w").pack(side="left")
        self.title_entry = tk.Entry(title_frame, width=40)
        self.title_entry.insert(0, "New code snippet")
        self.title_entry.pack(side="left", padx=5)
        
        # Prefix input
        prefix_frame = tk.Frame(root)
        prefix_frame.pack(anchor="w", padx=20, pady=5)
        tk.Label(prefix_frame, text="Prefix:", width=15, anchor="w").pack(side="left")
        self.prefix_entry = tk.Entry(prefix_frame, width=40)
        self.prefix_entry.insert(0, "snippet")
        self.prefix_entry.pack(side="left", padx=5)
        
        # Description input
        description_frame = tk.Frame(root)
        description_frame.pack(anchor="w", padx=20, pady=5)
        tk.Label(description_frame, text="Description:", width=15, anchor="w").pack(side="left")
        self.description_entry = tk.Entry(description_frame, width=40)
        self.description_entry.insert(0, "Code snippet description")
        self.description_entry.pack(side="left", padx=5)
        
        # Code preview
        tk.Label(root, text="Code from Clipboard (Read-only):").pack(anchor="w", padx=20, pady=(20, 5))
        self.code_display = scrolledtext.ScrolledText(root, height=8, width=70, state="disabled")
        self.code_display.pack(padx=20, pady=5)
        self.update_code_preview()
        
        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="Refresh Code", command=self.update_code_preview).pack(side="left", padx=5)
        tk.Button(button_frame, text="Generate & Copy", command=self.generate_snippet).pack(side="left", padx=5)
    
    def update_code_preview(self) -> None:
        """Update the code preview from clipboard."""
        code = pyperclip.paste() or ""
        self.code_display.config(state="normal")
        self.code_display.delete(1.0, tk.END)
        self.code_display.insert(1.0, code)
        self.code_display.config(state="disabled")
    
    def generate_snippet(self) -> None:
        """Generate the snippet and copy to clipboard."""
        title = self.title_entry.get().strip() or "New code snippet"
        prefix = self.prefix_entry.get().strip() or "snippet"
        description = self.description_entry.get().strip() or "Code snippet description"
        code = pyperclip.paste() or ""
        
        output = generate_code_snippet_from_text(code, title, prefix, description)
        pyperclip.copy(output)
        messagebox.showinfo("Success", "Snippet JSON copied to clipboard!")

def main() -> None:
    root = tk.Tk()
    SnippetGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

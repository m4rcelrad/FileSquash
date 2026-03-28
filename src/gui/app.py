import os
import customtkinter as ctk
from tkinter import filedialog
from src.core import aggregate_files


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FileSquash")
        self.geometry("600x500")
        self.grid_columnconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="FileSquash", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10))

        self.target_label = ctk.CTkLabel(self, text="Target Directory:")
        self.target_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.target_entry = ctk.CTkEntry(self)
        self.target_entry.grid(row=1, column=1, padx=(0, 20), pady=10, sticky="ew")
        self.target_button = ctk.CTkButton(self, text="Browse", command=self.browse_target)
        self.target_button.grid(row=1, column=2, padx=(0, 20), pady=10)

        self.ext_label = ctk.CTkLabel(self, text="Extensions:")
        self.ext_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.ext_entry = ctk.CTkEntry(self)
        self.ext_entry.insert(0, ".cs, .py, .txt, .razor, .csproj")
        self.ext_entry.grid(row=2, column=1, columnspan=2, padx=(0, 20), pady=10, sticky="ew")

        self.excl_label = ctk.CTkLabel(self, text="Exclude Dirs:")
        self.excl_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.excl_entry = ctk.CTkEntry(self)
        self.excl_entry.insert(0, "bin, obj, .vs, .git, Properties, lib, node_modules")
        self.excl_entry.grid(row=3, column=1, columnspan=2, padx=(0, 20), pady=10, sticky="ew")

        self.out_label = ctk.CTkLabel(self, text="Output File:")
        self.out_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.out_entry = ctk.CTkEntry(self)
        self.out_entry.insert(0, "project_context.txt")
        self.out_entry.grid(row=4, column=1, padx=(0, 20), pady=10, sticky="ew")
        self.out_button = ctk.CTkButton(self, text="Browse", command=self.browse_output)
        self.out_button.grid(row=4, column=2, padx=(0, 20), pady=10)

        self.run_button = ctk.CTkButton(self, text="Squash Files", command=self.run_aggregation, height=40)
        self.run_button.grid(row=5, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="ew")

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.grid(row=6, column=0, columnspan=3, padx=20, pady=10)

    def browse_target(self):
        directory = filedialog.askdirectory()
        if directory:
            self.target_entry.delete(0, "end")
            self.target_entry.insert(0, directory)

            default_output = os.path.join(directory, "project_context.txt")
            self.out_entry.delete(0, "end")
            self.out_entry.insert(0, default_output)

    def browse_output(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.out_entry.delete(0, "end")
            self.out_entry.insert(0, file_path)

    def run_aggregation(self):
        target_dir = self.target_entry.get().strip()
        output_file = self.out_entry.get().strip()

        if not target_dir or not os.path.isdir(target_dir):
            self.status_label.configure(text="Error: Invalid target directory", text_color="red")
            return

        if not output_file:
            self.status_label.configure(text="Error: Invalid output file", text_color="red")
            return

        ext_raw = self.ext_entry.get()
        allowed_extensions = [ext.strip() for ext in ext_raw.split(",") if ext.strip()]

        excl_raw = self.excl_entry.get()
        exclude_dirs = {d.strip() for d in excl_raw.split(",") if d.strip()}

        try:
            aggregate_files(target_dir, output_file, allowed_extensions, exclude_dirs)
            self.status_label.configure(text=f"Success! Saved to:\n{output_file}", text_color="green")
        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}", text_color="red")


def run_app():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()

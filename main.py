import customtkinter as ctk
from tkinter import filedialog, messagebox
import numpy as np
from utils.util1 import Numpy_array_manuplator
from utils.util2 import NPY_file_changer
import sys

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MatricesManipulatorApp(ctk.CTk):
    def __init__(self):
        super(MatricesManipulatorApp, self).__init__()

        # Configure window
        self.title("Matrices Manipulator")
        self.geometry("900x700")
        
        # Initialize utility classes
        self.array_manipulator = Numpy_array_manuplator()
        self.file_changer = NPY_file_changer()
        
        # Store arrays for operations
        self.array1 = None
        self.array2 = None
        self.current_file_path = None
        self.created_array = None
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Create tabview
        self.tabview = ctk.CTkTabview(self, width=850, height=650)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Add tabs
        self.tabview.add("Array Operations")
        self.tabview.add("File Operations")
        self.tabview.add("Create Array")
        
        # Setup each tab
        self.setup_array_operations_tab()
        self.setup_file_operations_tab()
        self.setup_create_array_tab()
    
    def setup_array_operations_tab(self):
        tab = self.tabview.tab("Array Operations")
        
        # Array 1 Frame
        array1_frame = ctk.CTkFrame(tab)
        array1_frame.pack(padx=10, pady=10, fill="x")
        
        ctk.CTkLabel(array1_frame, text="Array 1:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        self.array1_text = ctk.CTkTextbox(array1_frame, height=80)
        self.array1_text.pack(padx=10, pady=5, fill="x")
        
        btn_frame1 = ctk.CTkFrame(array1_frame)
        btn_frame1.pack(padx=10, pady=5, fill="x")
        ctk.CTkButton(btn_frame1, text="Load Array 1", command=self.load_array1).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame1, text="Info", command=self.show_array1_info).pack(side="left", padx=5)
        
        # Array 2 Frame
        array2_frame = ctk.CTkFrame(tab)
        array2_frame.pack(padx=10, pady=10, fill="x")
        
        ctk.CTkLabel(array2_frame, text="Array 2:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        self.array2_text = ctk.CTkTextbox(array2_frame, height=80)
        self.array2_text.pack(padx=10, pady=5, fill="x")
        
        btn_frame2 = ctk.CTkFrame(array2_frame)
        btn_frame2.pack(padx=10, pady=5, fill="x")
        ctk.CTkButton(btn_frame2, text="Load Array 2", command=self.load_array2).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame2, text="Info", command=self.show_array2_info).pack(side="left", padx=5)
        
        # Operations Frame
        ops_frame = ctk.CTkFrame(tab)
        ops_frame.pack(padx=10, pady=10, fill="x")
        
        ctk.CTkLabel(ops_frame, text="Operations:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        
        operations_btn_frame = ctk.CTkFrame(ops_frame)
        operations_btn_frame.pack(padx=10, pady=5, fill="x")
        
        ctk.CTkButton(operations_btn_frame, text="Add", command=self.add_arrays).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(operations_btn_frame, text="Subtract", command=self.subtract_arrays).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(operations_btn_frame, text="Multiply", command=self.multiply_arrays).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(operations_btn_frame, text="Divide", command=self.divide_arrays).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(operations_btn_frame, text="Transpose Array 1", command=self.transpose_array1).pack(side="left", padx=5, pady=5)
        
        # Result Frame
        result_frame = ctk.CTkFrame(tab)
        result_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        ctk.CTkLabel(result_frame, text="Result:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        self.result_text = ctk.CTkTextbox(result_frame, height=150)
        self.result_text.pack(padx=10, pady=5, fill="both", expand=True)
    
    def setup_file_operations_tab(self):
        tab = self.tabview.tab("File Operations")
        
        # File path frame
        file_frame = ctk.CTkFrame(tab)
        file_frame.pack(padx=10, pady=10, fill="x")
        
        ctk.CTkLabel(file_frame, text="NPY File Operations:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        
        path_frame = ctk.CTkFrame(file_frame)
        path_frame.pack(padx=10, pady=5, fill="x")
        
        ctk.CTkLabel(path_frame, text="File Path:").pack(side="left", padx=5)
        self.file_path_entry = ctk.CTkEntry(path_frame, width=400)
        self.file_path_entry.pack(side="left", padx=5, fill="x", expand=True)
        ctk.CTkButton(path_frame, text="Browse", command=self.browse_file).pack(side="left", padx=5)
        
        # File operations buttons
        btn_frame = ctk.CTkFrame(file_frame)
        btn_frame.pack(padx=10, pady=10, fill="x")
        
        ctk.CTkButton(btn_frame, text="Load NPY File", command=self.load_npy_file).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Show File Info", command=self.show_file_info).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Copy File", command=self.copy_npy_file).pack(side="left", padx=5)
        
        # File content display
        content_frame = ctk.CTkFrame(tab)
        content_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        ctk.CTkLabel(content_frame, text="File Content:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        self.file_content_text = ctk.CTkTextbox(content_frame)
        self.file_content_text.pack(padx=10, pady=5, fill="both", expand=True)
    
    def setup_create_array_tab(self):
        tab = self.tabview.tab("Create Array")
        
        # Create array frame
        create_frame = ctk.CTkFrame(tab)
        create_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        ctk.CTkLabel(create_frame, text="Create NumPy Array:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        
        # Array input
        ctk.CTkLabel(create_frame, text="Enter array data (e.g., [[1,2,3],[4,5,6]]):").pack(anchor="w", padx=10, pady=5)
        self.create_array_text = ctk.CTkTextbox(create_frame, height=150)
        self.create_array_text.pack(padx=10, pady=5, fill="x")
        
        # Buttons
        btn_frame = ctk.CTkFrame(create_frame)
        btn_frame.pack(padx=10, pady=10, fill="x")
        
        ctk.CTkButton(btn_frame, text="Create & Preview", command=self.create_array).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Save to Array 1", command=lambda: self.save_created_array(1)).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Save to Array 2", command=lambda: self.save_created_array(2)).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Save to NPY File", command=self.save_to_npy).pack(side="left", padx=5)
        
        # Preview
        ctk.CTkLabel(create_frame, text="Preview:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
        self.preview_text = ctk.CTkTextbox(create_frame, height=150)
        self.preview_text.pack(padx=10, pady=5, fill="both", expand=True)
    
    # Array Operations Methods
    def load_array1(self):
        try:
            array_str = self.array1_text.get("1.0", "end-1c")
            self.array1 = np.array(eval(array_str))
            messagebox.showinfo("Success", "Array 1 loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", "Failed to load array: {}".format(str(e)))
    
    def load_array2(self):
        try:
            array_str = self.array2_text.get("1.0", "end-1c")
            self.array2 = np.array(eval(array_str))
            messagebox.showinfo("Success", "Array 2 loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", "Failed to load array: {}".format(str(e)))
    
    def show_array1_info(self):
        if self.array1 is None:
            messagebox.showwarning("Warning", "Please load Array 1 first!")
            return
        
        info = "Shape: {}\n".format(self.array1.shape)
        info += "Size: {}\n".format(self.array1.size)
        info += "Dtype: {}\n".format(self.array1.dtype)
        info += "Max: {}\n".format(np.max(self.array1))
        info += "Min: {}\n".format(np.min(self.array1))
        info += "Sum: {}\n".format(np.sum(self.array1))
        
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", "Array 1 Info:\n" + "="*40 + "\n" + info)
    
    def show_array2_info(self):
        if self.array2 is None:
            messagebox.showwarning("Warning", "Please load Array 2 first!")
            return
        
        info = "Shape: {}\n".format(self.array2.shape)
        info += "Size: {}\n".format(self.array2.size)
        info += "Dtype: {}\n".format(self.array2.dtype)
        info += "Max: {}\n".format(np.max(self.array2))
        info += "Min: {}\n".format(np.min(self.array2))
        info += "Sum: {}\n".format(np.sum(self.array2))
        
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", "Array 2 Info:\n" + "="*40 + "\n" + info)
    
    def add_arrays(self):
        if self.array1 is None or self.array2 is None:
            messagebox.showwarning("Warning", "Please load both arrays first!")
            return
        
        try:
            result = self.array_manipulator.add_two_arrays(self.array1, self.array2)
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", "Addition Result:\n{}".format(result))
        except Exception as e:
            messagebox.showerror("Error", "Failed to add arrays: {}".format(str(e)))
    
    def subtract_arrays(self):
        if self.array1 is None or self.array2 is None:
            messagebox.showwarning("Warning", "Please load both arrays first!")
            return
        
        try:
            result = self.array_manipulator.subtract_two_arrays(self.array1, self.array2)
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", "Subtraction Result:\n{}".format(result))
        except Exception as e:
            messagebox.showerror("Error", "Failed to subtract arrays: {}".format(str(e)))
    
    def multiply_arrays(self):
        if self.array1 is None or self.array2 is None:
            messagebox.showwarning("Warning", "Please load both arrays first!")
            return
        
        try:
            result = self.array_manipulator.multply_two_arrays(self.array1, self.array2)
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", "Multiplication Result:\n{}".format(result))
        except Exception as e:
            messagebox.showerror("Error", "Failed to multiply arrays: {}".format(str(e)))
    
    def divide_arrays(self):
        if self.array1 is None or self.array2 is None:
            messagebox.showwarning("Warning", "Please load both arrays first!")
            return
        
        try:
            result = self.array_manipulator.devide_two_arrays(self.array1, self.array2)
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", "Division Result:\n{}".format(result))
        except Exception as e:
            messagebox.showerror("Error", "Failed to divide arrays: {}".format(str(e)))
    
    def transpose_array1(self):
        if self.array1 is None:
            messagebox.showwarning("Warning", "Please load Array 1 first!")
            return
        
        try:
            result = self.array_manipulator.transpose_the_array(self.array1, speak_also=False)
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", "Transpose Result:\n{}".format(result))
        except Exception as e:
            messagebox.showerror("Error", "Failed to transpose array: {}".format(str(e)))
    
    # File Operations Methods
    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Select NPY File",
            filetypes=[("NumPy Files", "*.npy"), ("All Files", "*.*")]
        )
        if filename:
            self.file_path_entry.delete(0, "end")
            self.file_path_entry.insert(0, filename)
            self.current_file_path = filename
    
    def load_npy_file(self):
        file_path = self.file_path_entry.get()
        if not file_path:
            messagebox.showwarning("Warning", "Please enter or browse for a file path!")
            return
        
        try:
            data = np.load(file_path, allow_pickle=True)
            self.file_content_text.delete("1.0", "end")
            self.file_content_text.insert("1.0", "File: {}\n\nContent:\n{}".format(file_path, data))
            messagebox.showinfo("Success", "File loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", "Failed to load file: {}".format(str(e)))
    
    def show_file_info(self):
        file_path = self.file_path_entry.get()
        if not file_path:
            messagebox.showwarning("Warning", "Please enter or browse for a file path!")
            return
        
        try:
            data = np.load(file_path, allow_pickle=True)
            info = "File: {}\n\n".format(file_path)
            info += "Shape: {}\n".format(data.shape)
            info += "Size: {}\n".format(data.size)
            info += "Dtype: {}\n".format(data.dtype)
            info += "Max: {}\n".format(np.max(data))
            info += "Min: {}\n".format(np.min(data))
            info += "Sum: {}\n".format(np.sum(data))
            
            self.file_content_text.delete("1.0", "end")
            self.file_content_text.insert("1.0", info)
        except Exception as e:
            messagebox.showerror("Error", "Failed to get file info: {}".format(str(e)))
    
    def copy_npy_file(self):
        src = self.file_path_entry.get()
        if not src:
            messagebox.showwarning("Warning", "Please enter or browse for a source file!")
            return
        
        dest = filedialog.asksaveasfilename(
            title="Save Copy As",
            defaultextension=".npy",
            filetypes=[("NumPy Files", "*.npy"), ("All Files", "*.*")]
        )
        
        if dest:
            try:
                self.file_changer.copy_npy_file(src, dest)
                messagebox.showinfo("Success", "File copied to {}".format(dest))
            except Exception as e:
                messagebox.showerror("Error", "Failed to copy file: {}".format(str(e)))
    
    # Create Array Methods
    def create_array(self):
        try:
            array_str = self.create_array_text.get("1.0", "end-1c")
            self.created_array = np.array(eval(array_str))
            
            preview = "Array created successfully!\n\n"
            preview += "Content:\n{}\n\n".format(self.created_array)
            preview += "Shape: {}\n".format(self.created_array.shape)
            preview += "Size: {}\n".format(self.created_array.size)
            preview += "Dtype: {}\n".format(self.created_array.dtype)
            
            self.preview_text.delete("1.0", "end")
            self.preview_text.insert("1.0", preview)
        except Exception as e:
            messagebox.showerror("Error", "Failed to create array: {}".format(str(e)))
    
    def save_created_array(self, array_num):
        if self.created_array is None:
            messagebox.showwarning("Warning", "Please create an array first!")
            return
        
        if array_num == 1:
            self.array1 = self.created_array
            self.array1_text.delete("1.0", "end")
            self.array1_text.insert("1.0", str(self.created_array.tolist()))
            messagebox.showinfo("Success", "Array saved to Array 1!")
        else:
            self.array2 = self.created_array
            self.array2_text.delete("1.0", "end")
            self.array2_text.insert("1.0", str(self.created_array.tolist()))
            messagebox.showinfo("Success", "Array saved to Array 2!")
    
    def save_to_npy(self):
        if self.created_array is None:
            messagebox.showwarning("Warning", "Please create an array first!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save Array As",
            defaultextension=".npy",
            filetypes=[("NumPy Files", "*.npy"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                self.file_changer.move_to_npy(self.created_array, file_path)
                messagebox.showinfo("Success", "Array saved to {}".format(file_path))
            except Exception as e:
                messagebox.showerror("Error", "Failed to save array: {}".format(str(e)))


def main():
    app = MatricesManipulatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()

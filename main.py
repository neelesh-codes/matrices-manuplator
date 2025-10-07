import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import numpy as np
from utils.util1 import Numpy_array_manipulator
from utils.util2 import NPY_file_changer
import traceback


class MatricesManipulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrices Manipulator")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Initialize manipulators
        self.array_manipulator = Numpy_array_manipulator()
        self.file_manipulator = NPY_file_changer()
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create main container
        main_container = ttk.Frame(root, padding="10")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        main_container.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_container, text="Matrices Manipulator", 
                                font=('Arial', 20, 'bold'))
        title_label.grid(row=0, column=0, pady=10)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_container)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create tabs
        self.create_array_operations_tab()
        self.create_file_operations_tab()
        self.create_quick_create_tab()
        
        # Output area at bottom
        output_frame = ttk.LabelFrame(main_container, text="Output", padding="5")
        output_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        main_container.rowconfigure(2, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=10, 
                                                      wrap=tk.WORD, font=('Consolas', 9))
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        # Clear output button
        clear_btn = ttk.Button(output_frame, text="Clear Output", 
                               command=self.clear_output)
        clear_btn.grid(row=1, column=0, pady=(5, 0))
    
    def create_array_operations_tab(self):
        """Create tab for array operations"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Array Operations")
        
        # Input frames
        input_frame = ttk.LabelFrame(tab, text="Input Arrays", padding="10")
        input_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Array 1
        ttk.Label(input_frame, text="Array 1:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.array1_entry = ttk.Entry(input_frame, width=50)
        self.array1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.array1_entry.insert(0, "[[1, 2, 3], [4, 5, 6]]")
        
        # Array 2
        ttk.Label(input_frame, text="Array 2:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.array2_entry = ttk.Entry(input_frame, width=50)
        self.array2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.array2_entry.insert(0, "[[7, 8], [9, 10], [11, 12]]")
        
        # Operations frame
        ops_frame = ttk.LabelFrame(tab, text="Operations", padding="10")
        ops_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Buttons for operations
        btn_width = 15
        
        ttk.Button(ops_frame, text="Add Arrays", width=btn_width,
                   command=lambda: self.perform_operation('add')).grid(row=0, column=0, padx=5, pady=5)
        
        ttk.Button(ops_frame, text="Subtract Arrays", width=btn_width,
                   command=lambda: self.perform_operation('subtract')).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(ops_frame, text="Multiply Arrays", width=btn_width,
                   command=lambda: self.perform_operation('multiply')).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Button(ops_frame, text="Divide Arrays", width=btn_width,
                   command=lambda: self.perform_operation('divide')).grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Button(ops_frame, text="Transpose Array 1", width=btn_width,
                   command=lambda: self.perform_operation('transpose')).grid(row=1, column=0, padx=5, pady=5)
        
        ttk.Button(ops_frame, text="Array 1 Info", width=btn_width,
                   command=lambda: self.perform_operation('info')).grid(row=1, column=1, padx=5, pady=5)
    
    def create_file_operations_tab(self):
        """Create tab for file operations"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="File Operations")
        
        # Load file section
        load_frame = ttk.LabelFrame(tab, text="Load .npy File", padding="10")
        load_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.file_path_var = tk.StringVar()
        ttk.Entry(load_frame, textvariable=self.file_path_var, width=50).grid(row=0, column=0, padx=5)
        ttk.Button(load_frame, text="Browse", command=self.browse_file).grid(row=0, column=1, padx=5)
        ttk.Button(load_frame, text="Load & Display", command=self.load_npy_file).grid(row=0, column=2, padx=5)
        ttk.Button(load_frame, text="Show Info", command=self.show_file_info).grid(row=0, column=3, padx=5)
        
        # Save array to file section
        save_frame = ttk.LabelFrame(tab, text="Save Array to .npy File", padding="10")
        save_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(save_frame, text="Array Data:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.save_array_entry = ttk.Entry(save_frame, width=50)
        self.save_array_entry.grid(row=0, column=1, padx=5, pady=5)
        self.save_array_entry.insert(0, "[[1, 2, 3], [4, 5, 6]]")
        
        ttk.Label(save_frame, text="Save As:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.save_path_var = tk.StringVar()
        ttk.Entry(save_frame, textvariable=self.save_path_var, width=50).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(save_frame, text="Browse Location", 
                   command=self.browse_save_location).grid(row=1, column=2, padx=5)
        ttk.Button(save_frame, text="Save", command=self.save_to_npy).grid(row=2, column=1, pady=10)
        
        # Copy file section
        copy_frame = ttk.LabelFrame(tab, text="Copy .npy File", padding="10")
        copy_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(copy_frame, text="Source:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.copy_src_var = tk.StringVar()
        ttk.Entry(copy_frame, textvariable=self.copy_src_var, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(copy_frame, text="Browse", 
                   command=lambda: self.browse_file_for_copy('src')).grid(row=0, column=2, padx=5)
        
        ttk.Label(copy_frame, text="Destination:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.copy_dest_var = tk.StringVar()
        ttk.Entry(copy_frame, textvariable=self.copy_dest_var, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(copy_frame, text="Browse", 
                   command=lambda: self.browse_file_for_copy('dest')).grid(row=1, column=2, padx=5)
        
        ttk.Button(copy_frame, text="Copy File", command=self.copy_npy_file).grid(row=2, column=1, pady=10)
    
    def create_quick_create_tab(self):
        """Create tab for quickly creating arrays"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Quick Create")
        
        # Zeros array
        zeros_frame = ttk.LabelFrame(tab, text="Create Zeros Array", padding="10")
        zeros_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(zeros_frame, text="Shape (rows, cols):").grid(row=0, column=0, pady=5)
        self.zeros_shape = ttk.Entry(zeros_frame, width=20)
        self.zeros_shape.grid(row=0, column=1, padx=5, pady=5)
        self.zeros_shape.insert(0, "3, 3")
        ttk.Button(zeros_frame, text="Create", 
                   command=lambda: self.create_special_array('zeros')).grid(row=0, column=2, padx=5)
        
        # Ones array
        ones_frame = ttk.LabelFrame(tab, text="Create Ones Array", padding="10")
        ones_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(ones_frame, text="Shape (rows, cols):").grid(row=0, column=0, pady=5)
        self.ones_shape = ttk.Entry(ones_frame, width=20)
        self.ones_shape.grid(row=0, column=1, padx=5, pady=5)
        self.ones_shape.insert(0, "3, 3")
        ttk.Button(ones_frame, text="Create", 
                   command=lambda: self.create_special_array('ones')).grid(row=0, column=2, padx=5)
        
        # Identity array
        identity_frame = ttk.LabelFrame(tab, text="Create Identity Matrix", padding="10")
        identity_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(identity_frame, text="Size:").grid(row=0, column=0, pady=5)
        self.identity_size = ttk.Entry(identity_frame, width=20)
        self.identity_size.grid(row=0, column=1, padx=5, pady=5)
        self.identity_size.insert(0, "3")
        ttk.Button(identity_frame, text="Create", 
                   command=lambda: self.create_special_array('identity')).grid(row=0, column=2, padx=5)
        
        # Random array
        random_frame = ttk.LabelFrame(tab, text="Create Random Array", padding="10")
        random_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(random_frame, text="Shape (rows, cols):").grid(row=0, column=0, pady=5)
        self.random_shape = ttk.Entry(random_frame, width=20)
        self.random_shape.grid(row=0, column=1, padx=5, pady=5)
        self.random_shape.insert(0, "3, 3")
        ttk.Button(random_frame, text="Create", 
                   command=lambda: self.create_special_array('random')).grid(row=0, column=2, padx=5)
        
        # Linspace array
        linspace_frame = ttk.LabelFrame(tab, text="Create Linspace Array", padding="10")
        linspace_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(linspace_frame, text="Start:").grid(row=0, column=0, pady=5)
        self.linspace_start = ttk.Entry(linspace_frame, width=10)
        self.linspace_start.grid(row=0, column=1, padx=5, pady=5)
        self.linspace_start.insert(0, "0")
        
        ttk.Label(linspace_frame, text="Stop:").grid(row=0, column=2, pady=5)
        self.linspace_stop = ttk.Entry(linspace_frame, width=10)
        self.linspace_stop.grid(row=0, column=3, padx=5, pady=5)
        self.linspace_stop.insert(0, "10")
        
        ttk.Label(linspace_frame, text="Num:").grid(row=0, column=4, pady=5)
        self.linspace_num = ttk.Entry(linspace_frame, width=10)
        self.linspace_num.grid(row=0, column=5, padx=5, pady=5)
        self.linspace_num.insert(0, "11")
        
        ttk.Button(linspace_frame, text="Create", 
                   command=lambda: self.create_special_array('linspace')).grid(row=0, column=6, padx=5)
    
    def log_output(self, message):
        """Log message to output text area"""
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)
        self.root.update_idletasks()
    
    def clear_output(self):
        """Clear output text area"""
        self.output_text.delete(1.0, tk.END)
    
    def parse_array(self, array_str):
        """Parse string to numpy array"""
        try:
            # Use eval with numpy available
            array = eval(array_str, {"__builtins__": {}, "array": np.array}, {"np": np})
            return np.array(array)
        except Exception as e:
            raise ValueError(f"Invalid array format: {e}")
    
    def perform_operation(self, operation):
        """Perform array operation"""
        try:
            array1_str = self.array1_entry.get()
            array1 = self.parse_array(array1_str)
            
            self.log_output(f"\n{'='*60}")
            self.log_output(f"Operation: {operation.upper()}")
            self.log_output(f"{'='*60}")
            
            if operation == 'info':
                self.log_output(f"Array 1:\n{array1}\n")
                self.log_output("Basic Information:")
                self.log_output(f"  Max value: {np.max(array1)}")
                self.log_output(f"  Min value: {np.min(array1)}")
                self.log_output(f"  Sum: {np.sum(array1)}")
                self.log_output(f"  Data type: {array1.dtype}")
                self.log_output(f"  Shape: {array1.shape}")
                self.log_output(f"  Size: {array1.size}")
                
            elif operation == 'transpose':
                result = self.array_manipulator.transpose_the_array(array1)
                self.log_output(f"Original Array:\n{array1}\n")
                self.log_output(f"Transposed Array:\n{result}")
                
            else:
                array2_str = self.array2_entry.get()
                array2 = self.parse_array(array2_str)
                
                self.log_output(f"Array 1:\n{array1}\n")
                self.log_output(f"Array 2:\n{array2}\n")
                
                if operation == 'add':
                    result = self.array_manipulator.add_two_arrays(array1, array2)
                elif operation == 'subtract':
                    result = self.array_manipulator.subtract_two_arrays(array1, array2)
                elif operation == 'multiply':
                    result = self.array_manipulator.multiply_two_arrays(array1, array2)
                elif operation == 'divide':
                    result = self.array_manipulator.divide_two_arrays(array1, array2)
                
                self.log_output(f"Result:\n{result}")
            
            self.log_output(f"{'='*60}\n")
            messagebox.showinfo("Success", f"{operation.capitalize()} operation completed!")
            
        except Exception as e:
            self.log_output(f"ERROR: {str(e)}\n{traceback.format_exc()}")
            messagebox.showerror("Error", f"Operation failed: {str(e)}")
    
    def browse_file(self):
        """Browse for .npy file"""
        filename = filedialog.askopenfilename(
            title="Select .npy file",
            filetypes=[("NumPy files", "*.npy"), ("All files", "*.*")]
        )
        if filename:
            self.file_path_var.set(filename)
    
    def load_npy_file(self):
        """Load and display .npy file"""
        try:
            file_path = self.file_path_var.get()
            if not file_path:
                messagebox.showwarning("Warning", "Please select a file first!")
                return
            
            self.log_output(f"\n{'='*60}")
            self.log_output(f"Loading file: {file_path}")
            self.log_output(f"{'='*60}")
            
            array = self.file_manipulator.load_npy_file(file_path)
            self.log_output(f"File loaded successfully!\n")
            self.log_output(f"Data:\n{array}")
            self.log_output(f"{'='*60}\n")
            
            messagebox.showinfo("Success", "File loaded successfully!")
            
        except Exception as e:
            self.log_output(f"ERROR: {str(e)}\n{traceback.format_exc()}")
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
    
    def show_file_info(self):
        """Show file information"""
        try:
            file_path = self.file_path_var.get()
            if not file_path:
                messagebox.showwarning("Warning", "Please select a file first!")
                return
            
            self.log_output(f"\n{'='*60}")
            self.log_output(f"File Information: {file_path}")
            self.log_output(f"{'='*60}")
            
            array = np.load(file_path)
            self.log_output(f"Data:\n{array}\n")
            self.log_output("Basic Information:")
            self.log_output(f"  Max value: {np.max(array)}")
            self.log_output(f"  Min value: {np.min(array)}")
            self.log_output(f"  Sum: {np.sum(array)}")
            self.log_output(f"  Data type: {array.dtype}")
            self.log_output(f"  Shape: {array.shape}")
            self.log_output(f"  Size: {array.size}")
            self.log_output(f"{'='*60}\n")
            
            messagebox.showinfo("Success", "File info displayed!")
            
        except Exception as e:
            self.log_output(f"ERROR: {str(e)}\n{traceback.format_exc()}")
            messagebox.showerror("Error", f"Failed to show file info: {str(e)}")
    
    def browse_save_location(self):
        """Browse for save location"""
        filename = filedialog.asksaveasfilename(
            title="Save as",
            defaultextension=".npy",
            filetypes=[("NumPy files", "*.npy"), ("All files", "*.*")]
        )
        if filename:
            self.save_path_var.set(filename)
    
    def save_to_npy(self):
        """Save array to .npy file"""
        try:
            array_str = self.save_array_entry.get()
            array = self.parse_array(array_str)
            
            save_path = self.save_path_var.get()
            if not save_path:
                messagebox.showwarning("Warning", "Please specify save location!")
                return
            
            self.log_output(f"\n{'='*60}")
            self.log_output(f"Saving to: {save_path}")
            self.log_output(f"{'='*60}")
            
            self.file_manipulator.move_to_npy(array, save_path)
            
            self.log_output(f"Array saved successfully!")
            self.log_output(f"Data:\n{array}")
            self.log_output(f"{'='*60}\n")
            
            messagebox.showinfo("Success", f"Array saved to {save_path}")
            
        except Exception as e:
            self.log_output(f"ERROR: {str(e)}\n{traceback.format_exc()}")
            messagebox.showerror("Error", f"Failed to save array: {str(e)}")
    
    def browse_file_for_copy(self, src_or_dest):
        """Browse for file to copy"""
        if src_or_dest == 'src':
            filename = filedialog.askopenfilename(
                title="Select source file",
                filetypes=[("NumPy files", "*.npy"), ("All files", "*.*")]
            )
            if filename:
                self.copy_src_var.set(filename)
        else:
            filename = filedialog.asksaveasfilename(
                title="Select destination",
                defaultextension=".npy",
                filetypes=[("NumPy files", "*.npy"), ("All files", "*.*")]
            )
            if filename:
                self.copy_dest_var.set(filename)
    
    def copy_npy_file(self):
        """Copy .npy file"""
        try:
            src = self.copy_src_var.get()
            dest = self.copy_dest_var.get()
            
            if not src or not dest:
                messagebox.showwarning("Warning", "Please specify both source and destination!")
                return
            
            self.log_output(f"\n{'='*60}")
            self.log_output(f"Copying file")
            self.log_output(f"From: {src}")
            self.log_output(f"To: {dest}")
            self.log_output(f"{'='*60}")
            
            array = self.file_manipulator.copy_npy_file(src, dest)
            
            self.log_output(f"File copied successfully!")
            self.log_output(f"Data:\n{array}")
            self.log_output(f"{'='*60}\n")
            
            messagebox.showinfo("Success", "File copied successfully!")
            
        except Exception as e:
            self.log_output(f"ERROR: {str(e)}\n{traceback.format_exc()}")
            messagebox.showerror("Error", f"Failed to copy file: {str(e)}")
    
    def create_special_array(self, array_type):
        """Create special arrays"""
        try:
            self.log_output(f"\n{'='*60}")
            self.log_output(f"Creating {array_type.upper()} array")
            self.log_output(f"{'='*60}")
            
            if array_type == 'zeros':
                shape_str = self.zeros_shape.get()
                shape = tuple(map(int, shape_str.split(',')))
                array = np.zeros(shape)
                
            elif array_type == 'ones':
                shape_str = self.ones_shape.get()
                shape = tuple(map(int, shape_str.split(',')))
                array = np.ones(shape)
                
            elif array_type == 'identity':
                size = int(self.identity_size.get())
                array = np.eye(size)
                
            elif array_type == 'random':
                shape_str = self.random_shape.get()
                shape = tuple(map(int, shape_str.split(',')))
                array = np.random.rand(*shape)
                
            elif array_type == 'linspace':
                start = float(self.linspace_start.get())
                stop = float(self.linspace_stop.get())
                num = int(self.linspace_num.get())
                array = np.linspace(start, stop, num)
            
            self.log_output(f"Array created successfully!")
            self.log_output(f"Shape: {array.shape}")
            self.log_output(f"Data:\n{array}")
            self.log_output(f"{'='*60}\n")
            
            # Update Array 1 field with the new array
            self.array1_entry.delete(0, tk.END)
            self.array1_entry.insert(0, str(array.tolist()))
            
            messagebox.showinfo("Success", f"{array_type.capitalize()} array created and loaded into Array 1!")
            
        except Exception as e:
            self.log_output(f"ERROR: {str(e)}\n{traceback.format_exc()}")
            messagebox.showerror("Error", f"Failed to create array: {str(e)}")


def main():
    root = tk.Tk()
    app = MatricesManipulatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
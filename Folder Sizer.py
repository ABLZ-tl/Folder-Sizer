import os
import time
import multiprocessing
import webbrowser
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk


def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            try:
                total_size += os.stat(fp).st_size
            except OSError:
                pass
    return total_size


def process_folder(folder, results):
    size = get_folder_size(folder)
    results.append((folder, size))


def calculate_sizes(progress_label, progress_bar):
    try:
        input_dir = filedialog.askdirectory()
        if not input_dir:
            return

        dirs = [folder for folder in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, folder))]

        manager = multiprocessing.Manager()
        result_list = manager.list()

        num_processes = multiprocessing.cpu_count()

        processes = []

        for folder in dirs:
            if __name__ == '__main__':
                p = multiprocessing.Process(target=process_folder, args=(os.path.join(input_dir, folder), result_list))
                p.start()
                processes.append(p)

        num_folders = len(dirs)

        while len(processes) > 0:
            time.sleep(0.1)
            for p in processes:
                if not p.is_alive():
                    processes.remove(p)
                    percent_complete = len(result_list) / num_folders * 100
                    progress_label.config(text=f"Procesando... {len(result_list)} de {num_folders} carpetas procesadas")
                    progress_bar["value"] = percent_complete
                    progress_bar.update()

        results = sorted(result_list, key=lambda x: x[1], reverse=True)

        with open("Reporte {folder}.html", "w") as f:
            f.write("<html><body><table><tr><th>Nombre de la carpeta</th><th>Tamaño (MB)</th></tr>\n")
            for folder, size in results:
                f.write(f"<tr><td>{folder}</td><td>{size / (1024 * 1024):.2f}</td></tr>\n")
            f.write("</table></body></html>")

        if os.path.exists("tempfile.html"):
            print("Archivo 'Reporte {folder}.html' creado exitosamente.")
        else:
            print("No se pudo crear el archivo 'Reporte {folder}.html'.")

        webbrowser.open_new_tab("Reporte {folder}.html")

        messagebox.showinfo("Listo!", "El proceso ha terminado.")
    except Exception as e:
        with open("error-log.txt", "w") as f:
            f.write(str(e))
        messagebox.showerror("Error!", f"Ha ocurrido un error.\n\n{str(e)}")


def main():
    root = tk.Tk()
    root.withdraw()

    progress_window = tk.Toplevel()
    progress_window.title("Procesando...")
    progress_label = tk.Label(progress_window, text="Procesando...")
    progress_label.pack()
    progress_bar = ttk.Progressbar(progress_window, length=300)
    progress_bar.pack()
    progress_bar["value"] = 0
    progress_bar["maximum"] = 100

    calculate_sizes(progress_label, progress_bar)

    progress_window.destroy()


if __name__ == "__main__":
    main()

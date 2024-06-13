import os
import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime, timedelta

# Verifica e cria o diretório 'db' se não existir
if not os.path.exists('db'):
    os.makedirs('db')

# Função para obter o nome do arquivo JSON com base na data atual
def get_json_filename():
    now = datetime.now()
    # Considera que o período é de 26 de um mês até 25 do próximo mês
    if now.day < 26:
        month = now.month
        year = now.year
    else:
        month = now.month + 1 if now.month < 12 else 1
        year = now.year if now.month < 12 else now.year + 1
    return f"{month:02d}_{year}.json"

# Função para carregar os registros do arquivo JSON
def load_records():
    filename = get_json_filename()
    filepath = os.path.join('db', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    else:
        return []

# Função para salvar os registros no arquivo JSON
def save_records(records):
    filename = get_json_filename()
    filepath = os.path.join('db', filename)
    with open(filepath, 'w') as file:
        json.dump(records, file, indent=4)

# Função para calcular a diferença entre duas datas
def calculate_hours(start, end):
    fmt = '%d/%m/%Y %H:%M:%S'
    tdelta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
    return tdelta.total_seconds() / 3600

# Função para atualizar o total de horas trabalhadas no arquivo JSON
def update_total_hours(records):
    total_hours = 0
    for record in records:
        if 'saida' in record:
            total_hours += calculate_hours(record['entrada'], record['saida'])
    return total_hours

# Função para atualizar o temporizador
def update_timer():
    if start_time:
        elapsed_time = datetime.now() - start_time
        timer_label.config(text=str(elapsed_time).split('.')[0])
        root.after(1000, update_timer)

# Função para bater o ponto
def punch_clock():
    global start_time
    now = datetime.now()
    project_name = project_entry.get().strip()
    if not project_name:
        messagebox.showwarning("Aviso", "Por favor, insira o nome do projeto.")
        return
    
    records = load_records()
    
    if records and 'saida' not in records[-1]:
        # Registro de saída
        records[-1]['saida'] = now.strftime('%d/%m/%Y %H:%M:%S')
        total_hours = update_total_hours(records)
        records[-1]['total_horas'] = total_hours
        start_time = None
        timer_label.config(text="00:00:00")
        status_canvas.itemconfig(status_rect, fill="red")
        messagebox.showinfo("Ponto", "Saída registrada!")
    else:
        # Registro de entrada com o nome do projeto
        records.append({'entrada': now.strftime('%d/%m/%Y %H:%M:%S'), 'projeto': project_name})
        start_time = now
        update_timer()
        status_canvas.itemconfig(status_rect, fill="green")
        messagebox.showinfo("Ponto", "Entrada registrada!")
    
    save_records(records)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Registro de Ponto")
root.geometry("310x360")  # Define o tamanho da janela
root.resizable(False, False) 
root.configure(bg="#FFFFFF") 

# Define o ícone da janela
ico_path = "Future-80_icon-icons.com_57322.ico" # Substitua pelo caminho do seu arquivo .ico
root.iconbitmap(ico_path)

frame = tk.Frame(root)
frame.pack(pady=20)
frame.configure(bg="#FFFFFF")   

# Carregar e redimensionar a imagem
img_path = "pix_force_logo.png"  # Caminho da imagem a ser usada
img = Image.open(img_path)
img = img.resize((100, 100), Image.LANCZOS)  # Redimensionar a imagem com antialiasing
img = ImageTk.PhotoImage(img)

img_label = tk.Label(frame, image=img)
img_label.pack(pady=5)
img_label.configure(bg="#FFFFFF")

project_label = tk.Label(frame, text="Nome do Projeto", font=("Arial", 12))
project_label.pack(pady=5)
project_label.configure(bg="#FFFFFF")

project_entry = tk.Entry(frame, width=30, font=("Arial", 12))  # Diminuir a largura do campo de entrada
project_entry.pack(pady=5)

label = tk.Label(frame, text="Clique no botão para bater o ponto", font=("Arial", 12))
label.pack(pady=10)
label.configure(bg="#FFFFFF")

button = tk.Button(frame, text="Bater Ponto!", command=punch_clock, font=("Arial", 12, "bold"), bg="#003d99", fg="#FFFFFF")
button.pack(pady=10)

timer_frame = tk.Frame(frame)
timer_frame.pack(pady=10)

timer_label = tk.Label(timer_frame, text="00:00:00", font=("Helvetica", 16))
timer_label.pack(side=tk.LEFT)

status_canvas = tk.Canvas(timer_frame, width=20, height=20)
status_rect = status_canvas.create_rectangle(0, 0, 20, 20, fill="red")
status_canvas.pack(side=tk.LEFT, padx=10)

start_time = None

root.mainloop()

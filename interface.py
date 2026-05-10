import customtkinter as ctk
from app import criptografar, descriptografar
ctk.set_appearance_mode("light")

def pegar_texto(text: str):
     for widget in result_scroll.winfo_children():
        widget.destroy()

     mensagem = ctk.CTkLabel(result_scroll,width=400, wraplength=400, text=criptografar(text.replace(' ','#')), anchor='w', font=ctk.CTkFont(size=20))
     mensagem.pack(pady=10)
     input.delete("1.0", "end-1c") #Limpa o campo de texto após enviar a mensagem para criptografia
     app.clipboard_clear()
     app.clipboard_append(criptografar(text.replace(' ','#'))) #Adiciona a mensagem criptografada à área de transferência para fácil cópia

def devolver_texto(text: str):
     for widget in result_dec_scroll.winfo_children():
        widget.destroy()
     retorno = ctk.CTkLabel(result_dec_scroll,width=400, wraplength=400, text=descriptografar(text), font=ctk.CTkFont(size=20))
     retorno.pack( pady=10)
     input_dec.delete("1.0", "end-1c") #Limpa o campo de texto após enviar a mensagem para descriptografia

app = ctk.CTk()
app.geometry("950x650")
app.resizable(False, False)

label_cripto = ctk.CTkLabel(app, text="Criptografia", width= 425,font=ctk.CTkFont(size=30, weight="bold"))
label_cripto.grid(row=0, column=0, pady=15)
label_input = ctk.CTkLabel(app, text="Digite a mensagem a ser criptografada: ", font=ctk.CTkFont(size=20))
label_input.grid(row=1, column=0, padx=20, pady=5)

input = ctk.CTkTextbox(app, width= 425, height=200, font=ctk.CTkFont(size=20))
input.grid(row=2, column=0, pady=10)

button_crip = ctk.CTkButton(app, text='Enviar', fg_color='dark red', command= lambda:pegar_texto(input.get("1.0", "end-1c").upper()),font=ctk.CTkFont(size=20))
button_crip.grid(row=3, column=0, padx=20, pady=10)

result = ctk.CTkFrame(app, width= 415)
result.grid(row=4, column=0, padx= 15, pady=10)
result_scroll = ctk.CTkScrollableFrame(result,width= 425)
result_scroll.pack()




#Parte da Criptografia
label_descripto = ctk.CTkLabel(app, text="Descriptografia",width= 425, font=ctk.CTkFont(size=30, weight="bold"))
label_descripto.grid(row=0, column=1, pady=15)
label_input = ctk.CTkLabel(app, text="Digite os números inteiros separados por espaço\nOu pressione Ctrl+V", font=ctk.CTkFont(size=20))
label_input.grid(row=1, column=1, padx=20, pady=5)

input_dec = ctk.CTkTextbox(app, width= 425, height=200, font=ctk.CTkFont(size=20))
input_dec.grid(row=2, column=1, pady=10)

button_crip = ctk.CTkButton(app, text='Enviar', fg_color='dark red', command= lambda:devolver_texto(input_dec.get("1.0", "end-1c").upper()), font=ctk.CTkFont(size=20))
button_crip.grid(row=3, column=1, padx=20, pady=10)

result_dec = ctk.CTkFrame(app, width= 415)
result_dec.grid(row=4, column=1, padx= 15, pady=10)
result_dec_scroll = ctk.CTkScrollableFrame(result_dec,width= 425)
result_dec_scroll.pack()




app.mainloop()

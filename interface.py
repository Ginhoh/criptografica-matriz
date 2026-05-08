import customtkinter as ctk
from app import criptografar, descriptografar
ctk.set_appearance_mode("light")

def pegar_texto(text: str):
     mensagem = ctk.CTkLabel(result_scroll, wraplength=400, text=criptografar(text))
     mensagem.grid(row=0, column=0, pady=5)


app = ctk.CTk()
app.geometry("850x650")
app.resizable(False, False)

label_cripto = ctk.CTkLabel(app, text="Criptografia", width= 425,font=ctk.CTkFont(size=30, weight="bold"))
label_cripto.grid(row=0, column=0, pady=15)
label_input = ctk.CTkLabel(app, text="Digite a mensagem a ser criptografada: ", font=ctk.CTkFont(size=20))
label_input.grid(row=1, column=0, padx=20, pady=5)

input = ctk.CTkTextbox(app, width= 400, height=200, font=ctk.CTkFont(size=20))
input.grid(row=2, column=0, padx=20, pady=10)

button_crip = ctk.CTkButton(app, text='Enviar', bg_color='grey', command= lambda:pegar_texto(input.get("1.0", "end-1c").upper()))
button_crip.grid(row=3, column=0, padx=20, pady=10)

result = ctk.CTkFrame(app,width= 425)
result.grid(row=4, column=0, padx=20, pady=10)
result_scroll = ctk.CTkScrollableFrame(result,width= 425).pack()

#Parte da Criptografia
label_descripto = ctk.CTkLabel(app, text="Descriptografia",width= 425, font=ctk.CTkFont(size=30, weight="bold"))
label_descripto.grid(row=0, column=1, pady=15)




app.mainloop()
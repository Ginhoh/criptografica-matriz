import customtkinter as ctk
ctk.set_appearance_mode("light")

app = ctk.CTk()
app.geometry("850x650")
app.resizable(False, False)

label_cripto = ctk.CTkLabel(app, text="Criptografia", width= 425,font=ctk.CTkFont(size=30, weight="bold"))
label_cripto.grid(row=0, column=0, pady=20)
label_input = ctk.CTkLabel(app, text="Digite a mensagem a ser criptografada: ", font=ctk.CTkFont(size=20))
label_input.grid(row=1, column=0, padx=20, pady=10)

entry_input = ctk.CTkEntry(app, width= 400, height=200, placeholder_text = 'Seu texto aqui...', font=ctk.CTkFont(size=20))
entry_input.grid(row=2, column=0, padx=20, pady=10)


label_descripto = ctk.CTkLabel(app, text="Descriptografia",width= 425, font=ctk.CTkFont(size=30, weight="bold"))
label_descripto.grid(row=0, column=1, pady=20)




app.mainloop()
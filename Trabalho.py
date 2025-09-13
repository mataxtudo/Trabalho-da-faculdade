from datetime import datetime
import customtkinter as ctk
import re

# Usuários e dados globais
usuarios = {
    "123": {
        "senha": "123",
        "nome": "",
        "cpf": "",
        "telefone": "",
        "cep": "",
        "endereco": "",
        "escolaridade": "",
        "arrecadacao": ""
    }
}

# Aparência do sistema
ctk.set_appearance_mode("Dark")

# Fontes
fonte_titulo = ("Segoe UI", 20)
fonte_labels = ("Segoe UI", 14)
fonte_botao = ("Segoe UI", 16)


# Atualiza data e hora
def atualizar_hora():
    agora = datetime.now()
    data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")
    label_data_hora.configure(text=data_hora)
    label_data_hora.after(1000, atualizar_hora)


# Validação numérica
def validar_numeros(valor, tamanho_max=None):
    if not valor.isdigit():
        return False
    if tamanho_max and len(valor) != tamanho_max:
        return False
    return True


# Máscaras
def formatar_cpf(valor):
    valor = re.sub("[^0-9]", "", valor)
    return valor[:11]


def formatar_telefone(valor):
    valor = re.sub("[^0-9]", "", valor)
    return valor[:11]


def formatar_cep(valor):
    valor = re.sub("[^0-9]", "", valor)
    return valor[:8]


# Login
def validar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        resultado_login.configure(text='Login realizado!', text_color='green')
        for widget in app.winfo_children():
            widget.destroy()
        abrir_menu_principal(usuario)
    else:
        resultado_login.configure(text='Usuário ou senha inválidos',
                                  text_color='red')


# Cadastro
def abrir_cadastro():
    for widget in app.winfo_children():
        widget.destroy()
    ctk.CTkLabel(app, text="Cadastro de Usuário",
                 font=fonte_titulo).pack(pady=10)

    entrada_nome = ctk.CTkEntry(app,
                                placeholder_text="Nome completo",
                                font=fonte_labels)
    entrada_nome.pack(pady=3)
    entrada_cpf = ctk.CTkEntry(app,
                               placeholder_text="CPF (somente números)",
                               font=fonte_labels)
    entrada_cpf.pack(pady=3)
    entrada_telefone = ctk.CTkEntry(app,
                                    placeholder_text="Telefone (BR)",
                                    font=fonte_labels)
    entrada_telefone.pack(pady=3)
    entrada_cep = ctk.CTkEntry(app, placeholder_text="CEP", font=fonte_labels)
    entrada_cep.pack(pady=3)
    entrada_endereco = ctk.CTkEntry(app,
                                    placeholder_text="Rua / Endereço",
                                    font=fonte_labels)
    entrada_endereco.pack(pady=3)
    entrada_escolaridade = ctk.CTkEntry(app,
                                        placeholder_text="Escolaridade",
                                        font=fonte_labels)
    entrada_escolaridade.pack(pady=3)
    entrada_arrecadacao = ctk.CTkEntry(
        app,
        placeholder_text="Valor de arrecadação da casa",
        font=fonte_labels)
    entrada_arrecadacao.pack(pady=3)
    entrada_novo_usuario = ctk.CTkEntry(app,
                                        placeholder_text="Novo usuário",
                                        font=fonte_labels)
    entrada_novo_usuario.pack(pady=3)
    entrada_nova_senha = ctk.CTkEntry(app,
                                      placeholder_text="Nova senha",
                                      font=fonte_labels,
                                      show="*")
    entrada_nova_senha.pack(pady=3)
    entrada_confirmar_senha = ctk.CTkEntry(app,
                                           placeholder_text="Confirmar senha",
                                           font=fonte_labels,
                                           show="*")
    entrada_confirmar_senha.pack(pady=3)

    resultado_cadastro = ctk.CTkLabel(app, text="", font=fonte_labels)
    resultado_cadastro.pack(pady=5)

    def cadastrar():
        usuario = entrada_novo_usuario.get()
        senha = entrada_nova_senha.get()
        confirmar_senha = entrada_confirmar_senha.get()

        cpf_val = formatar_cpf(entrada_cpf.get())
        telefone_val = formatar_telefone(entrada_telefone.get())
        cep_val = formatar_cep(entrada_cep.get())
        arrecadacao_val = entrada_arrecadacao.get()

        if not validar_numeros(cpf_val, 11):
            resultado_cadastro.configure(text="CPF inválido!",
                                         text_color="red")
            return
        if not validar_numeros(telefone_val):
            resultado_cadastro.configure(text="Telefone inválido!",
                                         text_color="red")
            return
        if not validar_numeros(cep_val):
            resultado_cadastro.configure(text="CEP inválido!",
                                         text_color="red")
            return
        if not validar_numeros(arrecadacao_val):
            resultado_cadastro.configure(text="Valor de arrecadação inválido!",
                                         text_color="red")
            return
        if usuario and senha == confirmar_senha:
            usuarios[usuario] = {
                "senha": senha,
                "nome": entrada_nome.get(),
                "cpf": cpf_val,
                "telefone": telefone_val,
                "cep": cep_val,
                "endereco": entrada_endereco.get(),
                "escolaridade": entrada_escolaridade.get(),
                "arrecadacao": arrecadacao_val
            }
            resultado_cadastro.configure(
                text="Cadastro realizado com sucesso!", text_color="green")
        else:
            resultado_cadastro.configure(
                text="Erro no cadastro. Verifique os dados.", text_color="red")

    ctk.CTkButton(app, text="Cadastrar", command=cadastrar,
                  font=fonte_botao).pack(pady=3)
    ctk.CTkButton(app,
                  text="Voltar ao Login",
                  command=iniciar_login,
                  font=fonte_botao).pack(pady=3)


# Login inicial
def iniciar_login():
    for widget in app.winfo_children():
        widget.destroy()

    ctk.CTkLabel(app, text="Usuário", font=fonte_titulo).pack(pady=10)
    global entrada_usuario
    entrada_usuario = ctk.CTkEntry(app,
                                   placeholder_text="Digite seu usuário",
                                   font=fonte_labels)
    entrada_usuario.pack(pady=5)
    ctk.CTkLabel(app, text="Senha", font=fonte_titulo).pack(pady=5)
    global entrada_senha
    entrada_senha = ctk.CTkEntry(app,
                                 placeholder_text="Digite sua senha",
                                 font=fonte_labels,
                                 show="*")
    entrada_senha.pack(pady=5)

    botao_login = ctk.CTkButton(app,
                                text="Entrar",
                                command=validar_login,
                                font=fonte_botao)
    botao_login.pack(pady=5)
    global resultado_login
    resultado_login = ctk.CTkLabel(app, text="", font=fonte_labels)
    resultado_login.pack(pady=5)
    ctk.CTkButton(app,
                  text="Não tem conta? Cadastre-se",
                  command=abrir_cadastro,
                  font=fonte_botao).pack(pady=5)


# Menu principal
def abrir_menu_principal(usuario):
    for widget in app.winfo_children():
        widget.destroy()

    ctk.CTkLabel(app, text=f"Bem-vindo, {usuario}!",
                 font=fonte_titulo).pack(pady=10)
    global label_data_hora
    label_data_hora = ctk.CTkLabel(app, text="", font=("Segoe UI", 12))
    label_data_hora.place(x=10, y=470)
    atualizar_hora()

    ctk.CTkButton(app,
                  text="Curso de Excel",
                  font=fonte_botao,
                  command=abrir_curso_excel).pack(pady=3)
    ctk.CTkButton(app,
                  text="Curso de Informática Básica",
                  font=fonte_botao,
                  command=abrir_curso_informatica).pack(pady=3)
    ctk.CTkButton(app,
                  text="Curso de Inglês",
                  font=fonte_botao,
                  command=abrir_curso_ingles).pack(pady=3)
    ctk.CTkButton(app,
                  text="Certificados",
                  font=fonte_botao,
                  command=abrir_certificados).pack(pady=3)
    ctk.CTkButton(app,
                  text="Meu Usuário",
                  font=fonte_botao,
                  command=lambda: abrir_meu_usuario(usuario)).pack(pady=3)
    ctk.CTkButton(app, text="Sair", font=fonte_botao,
                  command=iniciar_login).pack(pady=3)


# Curso de Excel
def abrir_curso_excel():
    for widget in app.winfo_children():
        widget.destroy()
    ctk.CTkLabel(app, text="Curso de Excel", font=fonte_titulo).pack(pady=10)

    for i in range(1, 6):
        ctk.CTkButton(app,
                      text=f"Módulo {i}",
                      font=fonte_botao,
                      command=lambda i=i: abrir_modulo_excel(i)).pack(pady=3)

    ctk.CTkButton(
        app,
        text="Voltar ao Menu",
        font=fonte_botao,
        command=lambda: abrir_menu_principal(entrada_usuario.get())).pack(
            pady=20)


def abrir_modulo_excel(modulo):
    for widget in app.winfo_children():
        widget.destroy()

    conteudo = {
        1:
        "Módulo 1 – Introdução ao Excel\n- Conceitos básicos\n- Navegação\n- Inserção de dados",
        2:
        "Módulo 2 – Formatação e Estilos\n- Formatar células\n- Estilos de texto\n- Cores e bordas",
        3:
        "Módulo 3 – Fórmulas e Funções\n- Soma, Média, Contagem\n- Funções lógicas\n- Referências",
        4:
        "Módulo 4 – Gráficos\n- Criar gráficos\n- Alterar tipos\n- Personalizar gráficos",
        5:
        "Módulo 5 – Tabelas e Filtragem\n- Criar tabelas\n- Filtrar e classificar\n- Formatação condicional"
    }

    ctk.CTkLabel(app, text=conteudo[modulo], font=fonte_labels,
                 justify="left").pack(padx=20, pady=20)
    ctk.CTkButton(app,
                  text="Voltar ao Curso",
                  font=fonte_botao,
                  command=abrir_curso_excel).pack(pady=10)
    ctk.CTkButton(
        app,
        text="Voltar ao Menu",
        font=fonte_botao,
        command=lambda: abrir_menu_principal(entrada_usuario.get())).pack(
            pady=10)


# Outros cursos
def abrir_curso_informatica():
    for widget in app.winfo_children():
        widget.destroy()
    ctk.CTkLabel(app, text="Curso de Informática Básica",
                 font=fonte_titulo).pack(pady=20)
    ctk.CTkButton(
        app,
        text="Voltar ao Menu",
        font=fonte_botao,
        command=lambda: abrir_menu_principal(entrada_usuario.get())).pack(
            pady=20)


def abrir_curso_ingles():
    for widget in app.winfo_children():
        widget.destroy()
    ctk.CTkLabel(app, text="Curso de Inglês", font=fonte_titulo).pack(pady=20)
    ctk.CTkButton(
        app,
        text="Voltar ao Menu",
        font=fonte_botao,
        command=lambda: abrir_menu_principal(entrada_usuario.get())).pack(
            pady=20)


# Usuário e certificados
def abrir_certificados():
    for widget in app.winfo_children():
        widget.destroy()
    ctk.CTkLabel(app, text="Meus Certificados",
                 font=fonte_titulo).pack(pady=20)
    ctk.CTkButton(
        app,
        text="Voltar ao Menu",
        font=fonte_botao,
        command=lambda: abrir_menu_principal(entrada_usuario.get())).pack(
            pady=20)


def abrir_meu_usuario(usuario):
    for widget in app.winfo_children():
        widget.destroy()
    ctk.CTkLabel(app, text="Dados do Usuário:",
                 font=fonte_titulo).pack(pady=10)

    dados = usuarios[usuario]
    for campo, valor in dados.items():
        if campo != "senha":
            ctk.CTkLabel(app,
                         text=f"{campo.capitalize()}: {valor}",
                         font=fonte_labels,
                         anchor="w").pack(fill="x", padx=20, pady=2)

    ctk.CTkButton(app,
                  text="Voltar ao Menu",
                  font=fonte_botao,
                  command=lambda: abrir_menu_principal(usuario)).pack(pady=20)


# Criação da janela
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("600x500")

iniciar_login()
app.mainloop()

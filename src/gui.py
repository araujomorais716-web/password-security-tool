import tkinter as tk
from tkinter import messagebox

from password_generator import (
    gerar_senha_segura,
    calcular_entropia,
    classificar_entropia,
)


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Security Tool")
        self.root.geometry("520x600")
        self.root.resizable(False, False)

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.root,
            text="🔐 Password Security Tool",
            font=("Arial", 20, "bold"),
        )
        titulo.pack(pady=20)

        subtitulo = tk.Label(
            self.root,
            text="Gerador de senhas com análise de entropia",
            font=("Arial", 10),
        )
        subtitulo.pack()

        frame_config = tk.LabelFrame(
            self.root,
            text="Configurações",
            padx=20,
            pady=15,
        )
        frame_config.pack(padx=30, pady=20, fill="x")

        tk.Label(
            frame_config,
            text="Tamanho da senha:",
        ).grid(row=0, column=0, sticky="w")

        self.tamanho = tk.IntVar(value=16)

        tk.Spinbox(
            frame_config,
            from_=12,
            to=128,
            textvariable=self.tamanho,
            width=10,
        ).grid(row=0, column=1, padx=10)

        self.maiusculas = tk.BooleanVar(value=True)
        self.minusculas = tk.BooleanVar(value=True)
        self.numeros = tk.BooleanVar(value=True)
        self.simbolos = tk.BooleanVar(value=True)

        tk.Checkbutton(
            frame_config,
            text="Letras maiúsculas",
            variable=self.maiusculas,
        ).grid(row=1, column=0, sticky="w", pady=5)

        tk.Checkbutton(
            frame_config,
            text="Letras minúsculas",
            variable=self.minusculas,
        ).grid(row=2, column=0, sticky="w", pady=5)

        tk.Checkbutton(
            frame_config,
            text="Números",
            variable=self.numeros,
        ).grid(row=3, column=0, sticky="w", pady=5)

        tk.Checkbutton(
            frame_config,
            text="Símbolos",
            variable=self.simbolos,
        ).grid(row=4, column=0, sticky="w", pady=5)

        botao = tk.Button(
            self.root,
            text="GERAR SENHA",
            command=self.gerar,
            font=("Arial", 12, "bold"),
            bg="#2563eb",
            fg="white",
            padx=20,
            pady=10,
        )
        botao.pack(pady=10)

        self.senha = tk.Entry(
            self.root,
            font=("Consolas", 14),
            justify="center",
            width=38,
        )
        self.senha.pack(pady=15)

        self.resultado = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
            justify="left",
        )
        self.resultado.pack(pady=10)

        rodape = tk.Label(
            self.root,
            text="Projeto  Python + Cibersegurança",
            font=("Arial", 9),
            fg="gray",
        )
        rodape.pack(side="bottom", pady=15)

    def gerar(self):
        try:
            senha, conjunto = gerar_senha_segura(
                tamanho=self.tamanho.get(),
                usar_maiusculas=self.maiusculas.get(),
                usar_minusculas=self.minusculas.get(),
                usar_numeros=self.numeros.get(),
                usar_simbolos=self.simbolos.get(),
            )

            entropia = calcular_entropia(senha, conjunto)
            nivel = classificar_entropia(entropia)

            self.senha.delete(0, tk.END)
            self.senha.insert(0, senha)

            self.resultado.config(
                text=(
                    f"Tamanho: {len(senha)} caracteres\n"
                    f"Entropia estimada: {entropia:.2f} bits\n"
                    f"Classificação: {nivel}"
                )
            )

        except (TypeError, ValueError) as erro:
            messagebox.showerror("Erro", str(erro))


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

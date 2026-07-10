import socket
import threading
from tkinter import *
from tkinter import simpledialog
from queue import Queue


class Chat:
    def __init__(self):
        HOST = "127.0.0.1"
        PORT = 55556

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        self.fila = Queue()

        login = Tk()
        login.withdraw()

        self.nome = simpledialog.askstring(
            "Nome",
            "Digite seu nome!",
            parent=login
        )

        self.sala = simpledialog.askstring(
            "Sala",
            "Digite a sala que deseja entrar!",
            parent=login
        )

        login.destroy()

        self.janela()

        thread = threading.Thread(target=self.conecta, daemon=True)
        thread.start()

        self.atualizar_chat()

        self.root.mainloop()

    def janela(self):
        self.root = Tk()
        self.root.title("Chat")
        self.root.geometry("800x700")

        self.caixa_texto = Text(self.root, state=NORMAL)
        self.caixa_texto.place(relx=0.05, rely=0.02, width=700, height=550)

        self.envia_mensagem = Entry(self.root)
        self.envia_mensagem.place(relx=0.05, rely=0.85, width=500, height=25)

        self.envia_mensagem.bind("<Return>", self.enviarMensagem)

        self.btn_enviar = Button(
            self.root,
            text="Enviar",
            command=self.enviarMensagem
        )
        self.btn_enviar.place(relx=0.70, rely=0.85, width=100, height=25)

        self.root.protocol("WM_DELETE_WINDOW", self.fechar)

    def atualizar_chat(self):
        while not self.fila.empty():
            mensagem = self.fila.get()
            self.caixa_texto.insert(END, mensagem)
            self.caixa_texto.see(END)

        self.root.after(100, self.atualizar_chat)

    def conecta(self):
        try:
            while True:
                recebido = self.client.recv(1024)

                if not recebido:
                    break

                if recebido == b"SALA":
                    self.client.sendall((self.sala + "\n").encode())
                    self.client.sendall((self.nome + "\n").encode())
                else:
                    self.fila.put(recebido.decode())

        except (ConnectionResetError, OSError):
            pass

        self.fila.put("\nConexão encerrada.\n")

    def enviarMensagem(self, event=None):
        mensagem = self.envia_mensagem.get().strip()

        if not mensagem:
            return

        try:
            self.client.sendall(mensagem.encode())
            self.envia_mensagem.delete(0, END)
        except OSError:
            pass

    def fechar(self):
        try:
            self.client.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass

        self.client.close()
        self.root.destroy()


if __name__ == "__main__":
    Chat()
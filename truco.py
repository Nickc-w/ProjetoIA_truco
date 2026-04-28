import tkinter as tk
import random
from PIL import Image, ImageTk

VALORES = ['4','5','6','7','Q','J','K','A','2','3']
NAIPES = ['♠','♥','♦','♣']

NAIPE_MAP = {
    '♠': 'espadas',
    '♥': 'copas',
    '♦': 'ouros',
    '♣': 'paus'
}

def gerar_baralho():
    return [f"{v}{n}" for v in VALORES for n in NAIPES]

def proxima_carta(valor):
    idx = VALORES.index(valor)
    return VALORES[(idx + 1) % len(VALORES)]

def valor_carta(carta, manilha):
    valor = carta[:-1]
    naipe = carta[-1]

    if valor == manilha:
        ordem_naipes = ['♣','♥','♠','♦']
        return 100 + ordem_naipes.index(naipe)

    ordem = ['4','5','6','7','Q','J','K','A','2','3']
    return ordem.index(valor)

class TrucoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Truco 1v1")
        self.root.configure(bg='#0b6623')
        self.root.geometry("900x580")

        # ===== IMAGENS =====
        self.imagens = {}

        for valor in VALORES:
            for naipe in NAIPES:
                pasta = NAIPE_MAP[naipe]
                nome = valor if valor != 'A' else 'as'
                caminho = f"cartasImg/{pasta}/{nome}.png"

                img = Image.open(caminho).resize((80,120))
                self.imagens[f"{valor}{naipe}"] = ImageTk.PhotoImage(img)

        self.verso = ImageTk.PhotoImage(
            Image.open("cartasImg/virada.png").resize((80,120))
        )

        # ===== CPU =====
        self.frame_cpu = tk.Frame(root, bg='#0b6623')
        self.frame_cpu.pack(pady=10)

        self.cpu_labels = []
        for i in range(3):
            lbl = tk.Label(self.frame_cpu, image=self.verso, bg='#0b6623')
            lbl.grid(row=0, column=i, padx=15)
            self.cpu_labels.append(lbl)

        # ===== MESA =====
        self.frame_mesa = tk.Frame(root, bg='#0b6623', width=900, height=260)
        self.frame_mesa.pack()
        self.frame_mesa.pack_propagate(False)

        self.label_cpu_mesa = tk.Label(self.frame_mesa, bg='#0b6623')
        self.label_cpu_mesa.place(x=350, y=20)

        self.label_jogador_mesa = tk.Label(self.frame_mesa, bg='#0b6623')
        self.label_jogador_mesa.place(x=370, y=140)

        # ===== PILHA =====
        self.stack1 = tk.Label(self.frame_mesa, image=self.verso, bg='#0b6623')
        self.stack1.place(x=720, y=110)

        self.stack2 = tk.Label(self.frame_mesa, image=self.verso, bg='#0b6623')
        self.stack2.place(x=730, y=120)

        # ===== MANILHA =====
        self.label_vira_img = tk.Label(self.frame_mesa, bg='#0b6623')
        self.label_vira_img.place(x=700, y=90)
        self.label_vira_img.lift()

        # ===== JOGADOR =====
        self.frame_jogador = tk.Frame(root, bg='#0b6623')
        self.frame_jogador.pack(pady=15)

        self.cartas_btn = []
        for i in range(3):
            btn = tk.Button(self.frame_jogador, bg='#0b6623',
                            command=lambda i=i: self.jogar(i))
            btn.grid(row=0, column=i, padx=15)
            self.cartas_btn.append(btn)

        # ===== STATUS =====
        self.label_status = tk.Label(root, text="", font=('Arial',12),
                                    bg='#0b6623', fg='white')
        self.label_status.pack()

        self.nova_rodada()

    def animar_carta(self, label, img, x0, y0, xf, yf):
        label.config(image=img)
        label.image = img

        x, y = x0, y0

        def mover():
            nonlocal x, y

            if x < xf: x += 10
            elif x > xf: x -= 10

            if y < yf: y += 10
            elif y > yf: y -= 10

            label.place(x=x, y=y)

            if abs(x-xf) > 5 or abs(y-yf) > 5:
                self.root.after(20, mover)
            else:
                label.place(x=xf, y=yf)

        mover()

    def nova_rodada(self):
        baralho = gerar_baralho()
        random.shuffle(baralho)

        self.jogador = baralho[:3]
        self.cpu = baralho[3:6]

        self.vira = random.choice(baralho)
        self.manilha = proxima_carta(self.vira[:-1])

        self.label_vira_img.config(image=self.imagens[self.vira])
        self.label_vira_img.lift()

        self.rodadas = 0
        self.pontos_jogador = 0
        self.pontos_cpu = 0

        # 🧹 LIMPA MESA (CORREÇÃO)
        self.label_cpu_mesa.config(image='')
        self.label_jogador_mesa.config(image='')
        self.label_cpu_mesa.image = None
        self.label_jogador_mesa.image = None

        for i in range(3):
            carta = self.jogador[i]
            self.cartas_btn[i].config(image=self.imagens[carta], state='normal')
            self.cpu_labels[i].config(image=self.verso)

        self.label_status.config(text="Rodada 1/3 - Jogue sua carta")

    def jogar(self, i):
        carta_jogador = self.jogador[i]
        img_jog = self.imagens[carta_jogador]

        self.animar_carta(self.label_jogador_mesa, img_jog, 370, 350, 370, 140)
        self.cartas_btn[i].config(state='disabled')

        self.root.after(800, lambda: self.jogada_cpu(carta_jogador))

    def jogada_cpu(self, carta_jogador):
        carta_cpu = random.choice(self.cpu)
        self.cpu.remove(carta_cpu)

        img_cpu = self.imagens[carta_cpu]

        self.animar_carta(self.label_cpu_mesa, img_cpu, 350, -100, 350, 20)
        self.cpu_labels[self.rodadas].config(image=img_cpu)

        v1 = valor_carta(carta_jogador, self.manilha)
        v2 = valor_carta(carta_cpu, self.manilha)

        if v1 > v2:
            self.pontos_jogador += 1
            resultado = "Você ganhou"
        elif v2 > v1:
            self.pontos_cpu += 1
            resultado = "CPU ganhou"
        else:
            resultado = "Empate"

        self.rodadas += 1

        self.label_status.config(
            text=f"Rodada {self.rodadas}/3 - {resultado}"
        )

        if self.pontos_jogador == 2 or self.pontos_cpu == 2 or self.rodadas == 3:
            self.root.after(1000, self.fim_partida)

    def fim_partida(self):
        if self.pontos_jogador > self.pontos_cpu:
            texto = "Você venceu!"
        elif self.pontos_cpu > self.pontos_jogador:
            texto = "CPU venceu!"
        else:
            texto = "Empate!"

        self.label_status.config(text=texto)
        self.root.after(2000, self.nova_rodada)

if __name__ == "__main__":
    root = tk.Tk()
    app = TrucoGUI(root)
    root.mainloop()
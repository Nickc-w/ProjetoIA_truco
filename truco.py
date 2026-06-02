import tkinter as tk
import random
import pickle
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
        #ordem_naipes = ['♣','♥','♠','♦']
        # Ordem crescente de força: Ouros(0), Espadas(1), Copas(2), Paus/Zap(3)
        ordem_naipes = ['♦', '♠', '♥', '♣'] 
        return 100 + ordem_naipes.index(naipe)

    ordem = ['4','5','6','7','Q','J','K','A','2','3']
    return ordem.index(valor)


class QLearningAgent:
    def __init__(self):
        self.q_table = {}
        self.epsilon = 0.2  # 20% de chance de explorar
        self.alpha = 0.3    # taxa de aprendizado
        self.gamma = 0.9    # fator de desconto

    def get_state(self, mao_cpu, manilha, carta_jogador=None):
        valores_mao = sorted([valor_carta(c, manilha) for c in mao_cpu])
        carta_jog_valor = valor_carta(carta_jogador, manilha) if carta_jogador else None
        return (tuple(valores_mao), carta_jog_valor)

    def get_available_actions(self, mao_cpu):
        return list(range(len(mao_cpu)))

    def choose_action(self, state, available_actions):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_actions)
        else:
            if state not in self.q_table:
                self.q_table[state] = {a: 0.0 for a in available_actions}
            max_q = max(self.q_table[state].values())
            best_actions = [a for a in available_actions if self.q_table[state][a] == max_q]
            return random.choice(best_actions)

    def update_q_value(self, state, action, reward, next_state, next_available_actions):
        if state not in self.q_table:
            self.q_table[state] = {a: 0.0 for a in self.get_available_actions_from_state(state)}
        
        current_q = self.q_table[state][action]
        
        if next_state not in self.q_table or not next_available_actions:
            max_next_q = 0.0
        else:
            max_next_q = max(self.q_table[next_state].get(a, 0.0) for a in next_available_actions)
        
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table[state][action] = new_q

    def get_available_actions_from_state(self, state):
        return list(range(len(state[0])))

#apenas para fins de explicação, não necessário para o código principal
    def imprimir_q_table(self):
        if not self.q_table:
            print("Q-table está vazia!")
            return
        
        print("\n" + "="*150)
        print(f"{'Q-TABLE':^150}")
        print("="*150)
        print(f"{'Estado (Cartas CPU)':<35} | {'Carta Jogador':<15} | {'Ação 0':<10} | {'Ação 1':<10} | {'Ação 2':<10}")
        print("-"*150)
        
        for state in self.q_table:
            cartas_cpu, carta_jog = state
            q_values = self.q_table[state]
            
            q0 = f"{q_values.get(0, 0.0):.2f}"
            q1 = f"{q_values.get(1, 0.0):.2f}"
            q2 = f"{q_values.get(2, 0.0):.2f}"
            
            str_cartas = str(cartas_cpu)[:32]
            str_jogador = str(carta_jog)[:13]
            
            print(f"{str_cartas:<35} | {str_jogador:<15} | {q0:<10} | {q1:<10} | {q2:<10}")
        
        print("-"*150)
        print(f"Total de estados: {len(self.q_table)}\n")

    def save_q_table(self, filename="q_table.pkl"):
        with open(filename, 'wb') as f:
            pickle.dump(self.q_table, f)
        print(f"Q-table salva com {len(self.q_table)} estados")
        self.imprimir_q_table() # imprime a q-table no terminal

    def load_q_table(self, filename="q_table.pkl"):
        try:
            with open(filename, 'rb') as f:
                self.q_table = pickle.load(f)
            print(f"Q-table carregada com {len(self.q_table)} estados")
        except FileNotFoundError:
            print("Q-table não encontrada, começando do zero")


class TrucoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Truco 1v1")
        self.root.configure(bg='#0b6623')
        self.root.geometry("900x650") #aumentei de 580 para 650 por causa do score

        # adicionado: 
        # ===== SCORE =====
        self.score_total = 0
        
        self.agent = QLearningAgent()
        self.agent.load_q_table()

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

        # adicionado: 
        # ===== PLACAR SCORE =====
        self.label_score = tk.Label(root, text=f"Score: ", font=('Arial', 14, 'bold'), bg='#0b6623', fg='yellow')
        self.label_score.pack(pady=5)

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

        # adicionado: (AVALIAR)
        self.label_feedback_score = tk.Label(root, text="", font=('Arial',10, 'italic'), bg='#0b6623', fg='cyan')
        self.label_feedback_score.pack()

        self.nova_rodada()

    # adicionado: (AVALIAR)
    def atualizar_score(self, pontos, motivo):
        #Atualiza a pontuação total e exibe um feedback visual do motivo
        self.score_total += pontos
        self.label_score.config(text=f"Score: {self.score_total}")
        self.label_feedback_score.config(text=f"{motivo}")

        # mostra o score no terminal
        print(f"[{motivo}] -> Ganho: {pontos} pontos | Score Total: {self.score_total} pontos")

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
        # NOVA PARTIDA NO TERMINAL
        print("\n" + "=" * 10 + " NOVA PARTIDA " + "=" * 10)

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

        # LIMPA MESA 
        self.label_cpu_mesa.config(image='')
        self.label_jogador_mesa.config(image='')
        self.label_cpu_mesa.image = None
        self.label_jogador_mesa.image = None
        self.label_feedback_score.config(text="")

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
        reward = 0
        
        state = self.agent.get_state(self.cpu.copy(), self.manilha, carta_jogador)
        available_actions = self.agent.get_available_actions(self.cpu)
        action = self.agent.choose_action(state, available_actions)
        
        carta_cpu = self.cpu[action]
        self.cpu.remove(carta_cpu)

        img_cpu = self.imagens[carta_cpu]
        self.animar_carta(self.label_cpu_mesa, img_cpu, 350, -100, 350, 20)
        self.cpu_labels[self.rodadas].config(image=img_cpu)

        v1 = valor_carta(carta_jogador, self.manilha)
        v2 = valor_carta(carta_cpu, self.manilha)

        print(f"Rodada {self.rodadas + 1}: Jogador jogou [{carta_jogador}] e a CPU jogou [{carta_cpu}]")

        if v1 > v2:
            self.pontos_jogador += 1
            resultado = "Cpu perdeu! Score reduzido"
            if v2 >= 100:
                self.atualizar_score(-25, "Desperdício de Manilha (-25)")
                reward = -25
                print("Manilha utilizada:", carta_cpu)
            else:
                self.atualizar_score(-10, "Derrota na Rodada (-10)")
                reward = -10
       
        elif v2 > v1:
            self.pontos_cpu += 1
            resultado = "CPU ganhou"
            if v2 < 100:
                self.atualizar_score(15,"Vitória sem gastar Manilha (+15)")
                reward = 15
            else:
                self.atualizar_score(10,"Vitória na Rodada (+10)")
                reward = 10
                print("Manilha utilizada:", carta_cpu)

        else:
            resultado = "Empate"
            self.atualizar_score(0, "Rodada Empatada (0)")
            reward = 0

        next_state = self.agent.get_state(self.cpu.copy(), self.manilha)
        next_available_actions = self.agent.get_available_actions(self.cpu)
        self.agent.update_q_value(state, action, reward, next_state, next_available_actions)

        self.rodadas += 1
        self.label_status.config(text=f"Rodada {self.rodadas}/3 - {resultado}")

        if self.pontos_jogador == 2 or self.pontos_cpu == 2 or self.rodadas == 3:
            for btn in self.cartas_btn:
                btn.config(state='disabled')
            self.root.after(1000, self.fim_partida)

    def fim_partida(self):
        if self.pontos_cpu < self.pontos_jogador:
            texto = "CPU perdeu a mão!"
            self.atualizar_score(-50, "Perdeu a Mão (-50)")
        elif self.pontos_cpu > self.pontos_jogador:
            texto = "CPU venceu a mão!"
            self.atualizar_score(50, "Venceu a Mão (+50)")
        else:
            texto = "Empate na mão!"
            self.atualizar_score(0, "Empate Geral (0 pontos)")
        
        self.agent.save_q_table()
        
        self.label_status.config(text=texto)
        self.root.after(2000, self.nova_rodada)

if __name__ == "__main__":
    root = tk.Tk()
    app = TrucoGUI(root)
    root.mainloop()

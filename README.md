# MARIO AI
Este repositório é a base de códigos python para o agente que roda no servidor java.

  https://github.com/renatopp/marioai
  
# SUMÁRIO
    1 - Como executar o servidor
    2 - Como chamar o agent python
    3 - Funções básicas do agente
    4 - Técnicas do Decision Tree Agent
    
# 1 - Como Executar o Servidor

Primeiro abra um terminal dentro da pasta server.
Após fazer isto acione o servidor com o seguinte comeando:
    
    java ch.idsia.scenarios.MainRun -server on

# 2 - Como chama o agent python
Com o servidor já rodando execute o arquivo main:

    python2 main.py
    
O servido logo reconhecerá que existe um agente se comunicando via TCP/IP.
Assim vc verá o agente jogando.

# 3 - Funções básicas do agente
O agente, disponibilizado por padrão na competition marioai, vem com as seguinte funções:
    
        def __init__(self):
            self.level_scene = None
            self.on_ground = None
            self.can_jump = None
            self.mario_floats = None
            self.enemies_floats = None
            self.episode_over = False
            
Essa função representa o construtor da classe
As variáveis declaradas no construtor guardão informações do cenário:
    
    self.level_scene -> retorna uma matriz 22x22 que presenta todo o cenário (a posição [11][11] é ondeo mario está).
    self.on_ground -> informa se o mario encontra-se no chão ou não.
    self.can_jump -> informa se o mario pode pular.
    self.mario_floats -> A posição de Mario no level.
    self.enemies_floats -> informa a posição do inimigo no level.
    self.episode_over -> informa o fim do jogo.
    
A possiveis informações da matriz level_scen são as seguinte:

    Valar -> Significado
    -11 -> obstáculo suave, pode saltar através
    -10 -> obstáculo, não da para passar é necessário pular
    0 -> não há obstaculo, nem inimigos. Ex.: pode representar um buraco.
    1 -> mario
    2 -> Inimigo goomba
    3 -> Inimigo goomba winged
    4 -> Inimigo red koopa
    5 -> Inimigo red koopa winged
    6 -> Inimigo green koopa
    7 -> Inimigo green koopa winged
    8 -> Inimigo bullet bill
    9 -> Inimigo spiky
    10 -> Inimigo spiky winged
    12 -> Inimigo flower
    13 -> Inimigo shell

Outra função do servidor é a reset
    
    def reset(self):
        '''New episode.'''
        self.episode_over = False
        
Ela é usada sempre que irá iniciar outra fase, para seta a variavel episode_over como false.
Existe também a variável sense, ela analisa constantemente o cenário e seta as variaveis do agente.
    
    def sense(self, obs):
        '''Receive sense.'''

        if len(obs) != 6:
            self.episode_over = True
        else:
            self.can_jump = obs[0]
            self.on_ground = obs[1]
            self.mario_floats = obs[2]
            self.enemies_floats = obs[3]
            self.level_scene = obs[4]
            
Por fim temos as funções act e give_rewards
    
    def act(self):
        '''Return an action.'''
        pass

    def give_rewards(self, reward, cum_reward):
        '''Register current reward.'''
        pass
        
A função give_rewards é chamada sempre que troca o cenário, ela serve para caso
sejá necessario o registro de informações durante a execução do agente.

No entando a função que realmente faz o agente jogar e interagir com o cenário é a função act
Ela returna um vetor, de inteiros (0 ou 1), onde cada elemento do vetor representa um botão, que são:

    [Esquerda, Direita, Abaixar, Pular, Aticar/Correr]

Por exemplo: - Ação de andar para direita, pular e atirar

    return [0, 1, 0, 1, 1]
    
# 4 - Técnicas do Decision Tree Agent
Nesse agente foi usada a técnica árvore de decisão.
    
Com isto criamos três árvores, a primeira árvore foi ultilizada para decidir se o cenário é perigoso ou não.
Para isto foi necessário a obtenção de um banco de dados com vários cenários e a informação se o cenário é perigoso ou não (a forma como obtemos esse banco será explicado em breve).

Depois desenvolvemos duas árvores de decisão, uma focada na obtenção de moedas e outra em matar inimigos e sair de zonas de perigo o mais rápido posspivel.
Nelas também obtemos um banco de dados de cenários.

Para obtermos o banco de dados para usarmos na regressão e na árvore, foi desenvolvido um agente pseudo aleatório.
O desenvolvimento desse agente um pouco mais esperto, fez-se necessário para evitar-mos o máximo possível de telas repitidas no nosso banco de dados.
Com isto, fizemos várias execuções deste agente e salvamos em um arquivo txt a matriz da variavel level_scene, resultado em um arquivo da seguinte forma:
    
    D
    (
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
    )
    
Essas execuções resultou em um banco de dados com exatamente 241 matrizes. Após a obtenção das matrizes, foi feita a classificação das matrizes (ND - not dante e ID - is danger), juntamente com a validação dos movimentos.
Resultando em um arquivo da seguinte maneira:

    D
    ND
    228
    (
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
      0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
    )
    
Após concluir o precesso supervisionado, foi feita uma linearização da matriz, isso foi necessário para que foi possível ensinar a máquina como se comportar de acordo com os cenários.
Convertemos então nosso bando de dados para o formato: 
    
    D
    ND
    228
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ...
    
Feito estre processo obtemos de fato nossa base de dados para o agente, criamos então no arquivo "decision_tree_agent.py" quatro novas funções e sobrescrevemos o construtor.
Uma das quatro funções é a função leitura, nela é feita a leitura do banco de dados e armazenadas em variaveis (temporarias) para serem usadas no algoritmo de apredizado.

    def leitura(self):
        j = 0  # MARCADOR DE LEITURA
        lista_matrizes = []

        lista_act = []
        lista_dang = []

        mt_IsDg = []
        mt_IsDg_act = []

        mt_NotDG = []
        mt_NotDG_act = []

        arq = open('matrixFinal.txt', 'r')

        for line in arq:
            j += 1
            if j == 1:
                lista_act.append(line.rstrip('\n'))
            elif j == 2:
                lista_dang.append(line.rstrip('\n'))
            elif j == 4:
                j = 0
                matrizSTRG = line.rstrip('\n').split(" ")

                matrizINT = [int(i) for i in matrizSTRG]

                lista_matrizes.append(matrizINT)

                ''' SEPARANDO MATRIZ PERIGOSA E NAO PERIGOSA '''
                if (lista_dang[len(lista_dang) - 1][0] == 'N') and (lista_dang[len(lista_dang) - 1][1] == 'D'):
                    mt_NotDG_act.append(lista_act[len(lista_dang) - 1])
                    mt_NotDG.append(matrizINT)
                elif (lista_dang[len(lista_dang) - 1][0] == 'I') and (lista_dang[len(lista_dang) - 1][1] == 'D'):
                    mt_IsDg_act.append(lista_act[len(lista_dang) - 1])
                    mt_IsDg.append(matrizINT)

        self.tree_danger = self.DecisionTreeCreateFIT(lista_matrizes, lista_dang)
        self.tree_act_danger = self.DecisionTreeCreateFIT(mt_IsDg, mt_IsDg_act)
        self.tree_act_not_danger = self.DecisionTreeCreateFIT(mt_NotDG, mt_NotDG_act)
        
Com o arquivo de leitura pronto, fizemos uma função "DecisionTreeCreateFIT" que recebe como parametro, uma matriz dos cenários e uma matriz das ações ou classificações.

    def DecisionTreeCreateFIT(self, matrizes, info):  # CRIA A ARVORE E A TREINA BASEADO NAS RELACAO ENTRE AS MATRIZES E INFORMACOES
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(matrizes, info)

        return clf
        
Por fim criamos mais duas funções, "DecisionTreePredict" e "action_tree", a action chama a função decision e retorna uma ação baseada no cenário atual.

    def DecisionTreePredict(self, tree_predict, scenario):  # RECEBE A ARVORE TREINADA E O CENARIO , RETORNA A PREDICAO DE ACAO
        user_result = tree_predict.predict([scenario])

        return user_result

    def action_tree(self, scenario):
        decision = self.DecisionTreePredict(self.tree_danger, scenario)

        a = str(decision[0])
        if a[0] == 'I' and a[1] == 'D':
            return self.DecisionTreePredict(self.tree_act_danger, scenario)
        elif a[0] == 'N' and a[1] == 'D':
            return self.DecisionTreePredict(self.tree_act_not_danger, scenario)
            
Por fim usamos a função action_tree no método act do nosso agente e retornamos as ações baseadas nas nossas árvores de decisões.

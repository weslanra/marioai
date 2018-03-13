import marioai
from sklearn import tree

_all_ = ['DecisionTreeAgent']


class DecisionTreeAgent(marioai.Agent):
    flag = 0

    def __init__(self):
        '''Contructor.'''
        self.tree_danger = None
        self.tree_act_danger = None
        self.tree_act_not_danger = None
        self.leitura()

        self.level_scene = None
        self.on_ground = None
        self.can_jump = None
        self.mario_floats = None
        self.enemies_floats = None
        self.episode_over = False
        self.flagD = 0
        self.flagP = 0
        self.flagDP = 0
        self.flagDPA = 0
        self.flagDA = 0
        self.flag = 0
        self.flag2 = 0

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

    def DecisionTreePredict(self, tree_predict, scenario):  # RECEBE A ARVORE TREINADA E O CENARIO , RETORNA A PREDICAO DE ACAO
        user_result = tree_predict.predict([scenario])

        return user_result

    def DecisionTreeCreateFIT(self, matrizes, info):  # CRIA A ARVORE E A TREINA BASEADO NAS RELACAO ENTRE AS MATRIZES E INFORMACOES
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(matrizes, info)

        return clf

    def action_tree(self, scenario):
        decision = self.DecisionTreePredict(self.tree_danger, scenario)

        a = str(decision[0])
        if a[0] == 'I' and a[1] == 'D':
            return self.DecisionTreePredict(self.tree_act_danger, scenario)
        elif a[0] == 'N' and a[1] == 'D':
            return self.DecisionTreePredict(self.tree_act_not_danger, scenario)

    def sense(self, obs):
        super(DecisionTreeAgent, self).sense(obs)

    # def give_rewards(self, reward, cum_reward):
    #     print "Recompensa: " + str(reward) + "Cum-reward: " + str(cum_reward)

    def act(self):
        matriz_amb = []
        for i in range(0, 22):  # LINEARIZAR MATRIZ
            for j in range(0, 22):
                matriz_amb.append(self.level_scene[i][j])

        mov = self.action_tree(matriz_amb)

        mov_string = mov[0]

        if len(mov[0]) == 2:
            if mov_string[0] == 'D':
                self.flagP = 0
                self.flagDP = 0
                self.flagDPA = 0
                self.flagDA = 0

                print 'D'
                if (self.flagD % 50) == 0:
                    self.flag2 += 1
                    if (self.flag2 % 10) == 0:
                        self.flagD += 1
                        self.flag2 += 1
                    else:
                        self.flag2 += 1
                        return [0, 1, 0, 1, 0]
                else:
                    self.flagD += 1
                    return [0, 1, 0, 0, 0]
            if mov_string[0] == 'P':
                self.flagD = 0
                self.flagDP = 0
                self.flagDPA = 0
                self.flagDA = 0

                print 'P'
                if (self.flagP % 10) == 0:
                    self.flagP += 1
                    return [0, 1, 0, 0, 0]
                else:
                    self.flagP += 1
                    return [0, 0, 0, 1, 0]
        elif len(mov[0]) == 3:
            if mov_string[0] == 'D' and mov_string[1] == 'P':
                self.flagD = 0
                self.flagP = 0
                self.flagDPA = 0
                self.flagDA = 0

                print 'DP'
                if (self.flagDP % 20) == 0:
                    self.flagDP += 1
                    return [0, 1, 0, 0, 0]
                else:
                    self.flagDP += 1
                    return [0, 1, 0, 1, 0]
            if mov_string[0] == 'D' and mov_string[1] == 'A':
                self.flagD = 0
                self.flagDP = 0
                self.flagP = 0
                self.flagDPA = 0

                print 'DA'
                if (self.flagDA % 5) == 0:
                    self.flagDA += 1
                    return [0, 1, 0, 0, 1]
                else:
                    self.flagDA += 1
                    return [0, 1, 0, 1, 1]
        elif len(mov[0]) == 4:
            if mov_string[0] == 'D' and mov_string[1] == 'P' and mov_string[2] == 'A':
                self.flagD = 0
                self.flagDA = 0
                self.flagDP = 0
                self.flagP = 0

                print 'DPA'
                if (self.flagDPA % 20) == 0:
                    self.flagDPA += 1
                    return [0, 1, 0, 0, 0]
                else:
                    self.flagDPA += 1
                    return [0, 1, 0, 1, 1]

        return [0, 1, 0, 0, 0]
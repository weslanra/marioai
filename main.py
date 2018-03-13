import marioai
import agents
import random

def main():
    agent = agents.DecisionTreeAgent()
    task = marioai.Task()
    exp = marioai.Experiment(task, agent)
    
    exp.max_fps = 20
    task.env.level_type = 0
    task.env.level_difficulty = 1
    task.env.init_mario_mode = 2
    task.env.time_limit = 100

    random.seed(20)

    #fase random - 1
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 2
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 3
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 4
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 5
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 6
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 7
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 8
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 9
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)

    #fase random - 10
    task.env.level_seed = random.randint(0, 500)
    print "Level: " + str(task.env.level_seed)
    exp.doEpisodes(1)


if __name__ == '__main__':
    main()

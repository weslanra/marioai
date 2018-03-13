import marioai
import agents

def main():
    agent = agents.DecisionTreeAgent()
    task = marioai.Task()
    exp = marioai.Experiment(task, agent)
    
    exp.max_fps = 20
    task.env.level_type = 0
    task.env.level_difficulty = 1
    task.env.init_mario_mode = 2
    task.env.level_seed = 20
    task.env.time_limit = 100

    exp.doEpisodes(1)


if __name__ == '__main__':
    main()

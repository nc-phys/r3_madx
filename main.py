from src import R3MADX

if __name__ == "__main__":
    sim = R3MADX()
    sim.config()
    sim.survey()
    sim.match()
    sim.twiss()
    sim.repl()

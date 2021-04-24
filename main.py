from utils import*
from glove import glove

g = glove.Glove()


if __name__ == "__main__":
    print(isGripNeeded())
    while True:
        if isGripNeeded():
            g.gripObject(2)
            g.relax()

import pants
import inspect
print(inspect.getsource(pants))
print(inspect.getsource(pants),file = open("pants.py","w"))
print(inspect.getsource(pants.Ant),file = open("Ant.py","w"))
print(inspect.getsource(pants.World),file = open("World.py","w"))
print(inspect.getsource(pants.Edge),file = open("Edge.py","w"))
print(inspect.getsource(pants.Solver),file = open("Solver.py","w"))
print(inspect.getsource(pants.ant),file = open("1ant.py","w"))
print(inspect.getsource(pants.world),file = open("1world.py","w"))
print(inspect.getsource(pants.solver),file = open("1solver.py","w"))
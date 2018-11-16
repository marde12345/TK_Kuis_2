import pants
import math
import random
import matplotlib.pyplot as plt

nodes = []
for _ in range(20):
	x = random.uniform(-10, 10)
	y = random.uniform(-10, 10)
	nodes.append((x, y))

def euclidean(a, b):
	return math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))

world = pants.World(nodes, euclidean)

solver = pants.Solver()

solution = solver.solve(world)
# or
solutions = solver.solutions(world)

# print(solution.distance)
# print(solution.tour)    # Nodes visited in order
# print(solution.path)    # Edges taken in order


# or
best = float("inf")
for solution in solutions:
	assert solution.distance < best
	best = solution.distance
print(solution.tour)
plotx = []
ploty = []
for node in nodes:
	plotx.append(node[0])
	ploty.append(node[1])
plt.plot(plotx,ploty,"bo")
plt.grid(color="r")

for ko in range(1,len(solution.tour)):
	fa = solution.tour[ko]
	ka = solution.tour[ko-1]
	print(ka,fa)
	plt.arrow(ka[0],ka[1],fa[0]-ka[0],fa[1]-ka[1])
#plt.arrow(0,0,1,1)

plt.show()
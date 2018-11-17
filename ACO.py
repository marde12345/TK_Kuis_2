import pants
import math
import random
import matplotlib.pyplot as plt

# nodes=[]
nodes = [
[1.0,-5.2],
[2.3,4.5],
[0.7,-6.4],
[-0.4,3.2],
[-4.8,-5.6],
[-2.3,5.2],
[0.2,-0.3],
[4.5,-4.3],
[1.8,0.9],
[-4.3,3.2],
[3.4,-6.1],
[-2.9,4.5],
[5.0,5.0],
[4.3,3.6],
[-2.2,-0.2],
[-5.5,-3.6],
[-4.3,3.1],
[3.2,4.9],
[3.2,3.9],
[-1.5,-3.0]
]
# for _ in range(20):
# 	x = random.uniform(-10, 10)
# 	y = random.uniform(-10, 10)
# 	nodes.append((x, y))

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


fig = plt.figure()
ax = fig.add_subplot(111)
# or
k = 1
best = float("inf")
for solution in solutions:
	ax.grid(True)
	plotx = []
	ploty = []
	for node in nodes:
		plotx.append(node[0])
		ploty.append(node[1])
	ax.plot(plotx,ploty,"bo")
	for ko in range(1,len(solution.tour)):
		fa = solution.tour[ko]
		ka = solution.tour[ko-1]
		plt.arrow(ka[0],ka[1],fa[0]-ka[0],fa[1]-ka[1])
	fig.savefig('./evol_conc_v'+str(k)+'.png')
	k+=1
	ax.clear()
	assert solution.distance < best
	best = solution.distance

ax.grid(True)
plotx = []
ploty = []
for node in nodes:
	plotx.append(node[0])
	ploty.append(node[1])
ax.plot(plotx,ploty,"bo")
for ko in range(1,len(solution.tour)):
	fa = solution.tour[ko]
	ka = solution.tour[ko-1]
	plt.arrow(ka[0],ka[1],fa[0]-ka[0],fa[1]-ka[1])
fig.savefig('./evol_conc_v'+str(k)+'.png')
k += 1
ax.clear()
ax.plot(plotx,ploty,"bo")
fig.savefig('./evol_conc_v'+str(k)+'.png')



# plotx = []
# ploty = []
# for node in nodes:
# 	plotx.append(node[0])
# 	ploty.append(node[1])
# plt.plot(plotx,ploty,"bo")
# plt.grid(color="r")

# for ko in range(1,len(solution.tour)):
# 	fa = solution.tour[ko]
# 	ka = solution.tour[ko-1]
# 	print(ka,fa)
# 	plt.arrow(ka[0],ka[1],fa[0]-ka[0],fa[1]-ka[1])
# plt.savefig('plot.png')
# plt.show()

for i in solution.tour:
	print (round(i[0],2),round(i[1],2))

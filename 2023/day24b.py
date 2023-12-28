from z3 import Int, sat, Solver
stones=[]
with open('day24.txt') as file:
    for line in file:
        pos,vel=line.split('@')
        stones.append([list(map(int,pos.split(','))),list(map(int,vel.split(',')))])
xPos=Int('xPos')
yPos=Int('yPos')
zPos=Int('zPos')
xVel=Int('xVel')
yVel=Int('yVel')
zVel=Int('zVel')
solver=Solver()
for i in range(len(stones)):
    pos=stones[i][0]
    vel=stones[i][1]
    t=Int(f't{i}')
    solver.add(t>0,
                  xPos+xVel*t==pos[0]+vel[0]*t,
                  yPos+yVel*t==pos[1]+vel[1]*t,
                  zPos+zVel*t==pos[2]+vel[2]*t)
    
if solver.check()==sat:
    model=solver.model()
    print(f'Starting X: {model[xPos]}')
    print(f'Starting Y: {model[yPos]}')
    print(f'Starting Z: {model[zPos]}')
    print(f'X velocity: {model[xVel]}')
    print(f'Y velocity: {model[yVel]}')
    print(f'Z velocity: {model[zVel]}')
    print(f'Part 2 Answer: {model.eval(xPos+yPos+zPos)}')
else:
    print('NO SOLUTION')

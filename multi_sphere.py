from vpython import sphere,vector,rate,color,mag,norm

RA = 0.01
RB = 0.009
RC = 0.01
bA = sphere(pos=vector(-8*RA,0.5*RA,0),radius=RA,color=color.yellow,make_trail=True)
bB = sphere(pos=vector(0,0,0),radius=RB,color=color.cyan,make_trail=True)
bC = sphere(pos=vector(0,5*RC,0),radius=RC,color=color.red,make_trail=True)
bA.m = 3
bB.m = 1
bC.m = 2
v0 = 0.05
v1 = 0.01
bA.p = bA.m*vector(0.5*v0,0,0)
bB.p = bB.m*vector(0,0,0)
bC.p = bC.m*vector(0,-v1,0)

spheres = [bA,bB,bC]

t = 0
dt = 0.02
k = 500
while t < 7:
    rate(100)
    F = vector(0,0,0)
    FAB = vector(0,0,0)
    FAC = vector(0,0,0)
    for particle in spheres:
        for other in spheres:
            # check each particle against each other for collisions
            rParticle = particle.pos - other.pos
            
    # rAB = bA.pos - bB.pos
    # rAC = bA.pos - bC.pos
    
    # check A collision w/ B
    if mag(rAB) < (RA+RB):      
        FAB = k*((RA+RB)-mag(rAB))*norm(rAB)
        F = FAB
        # print(F)
    # check A collision w/ C
    if mag(rAC) < (RA+RC):      
        FAC = k*((RA+RC)-mag(rAC))*norm(rAC)
        F = FAC
        # print(F)
    bA.p = bA.p + F*dt
    bB.p = bB.p - FAB*dt
    bC.p = bC.p - FAC*dt
    bA.pos = bA.pos + bA.p*dt/bA.m
    bB.pos = bB.pos + bB.p*dt/bB.m
    bC.pos = bC.pos + bC.p*dt/bC.m
    t = t + dt

from vpython import sphere,vector,rate,color,mag,norm

RA = 0.01
RB = 0.009
RC = 0.01
bA = sphere(pos=vector(-8*RA,0.5*RA,0),radius=RA,color=color.yellow,make_trail=True)
bB = sphere(pos=vector(0,0,0),radius=RB,color=color.cyan,make_trail=True)
bC = sphere(pos=vector(0,5*RC,0),radius=RC,color=color.red,make_trail=True)
bA.m = 4
bB.m = 1
v0 = 0.05
bA.p = bA.m*vector(v0,0,0)
bB.p = bB.m*vector(0,0,0)

t = 0
dt = 0.01
k = 500
while t < 3:
    rate(100)
    rAB = bA.pos - bB.pos
    F = vector(0,0,0)
    # check A collision w/ B

    if mag(rAB) < (RA+RB):
        F = k*((RA+RB)-mag(rAB))*norm(rAB)
    bA.p = bA.p + F*dt
    bB.p = bB.p - F*dt
    bA.pos = bA.pos + bA.p*dt/bA.m
    bB.pos = bB.pos + bB.p*dt/bB.m
    t = t + dt

from vpython import sphere,vector,rate,color,mag,norm

R = 0.01
bA = sphere(pos=vector(-8*R,0.75*R,0),radius=1.5*R,color=color.yellow,make_trail=True)
bB = sphere(pos=vector(0,0,0),radius=R,color=color.cyan,make_trail=True)
bA.m = 5
bB.m = 1
v0 = 0.05
bA.p = bA.m*vector(v0,0,0)
bB.p = bB.m*vector(0,0,0)

t = 0
dt = 0.01
k = 500
while t < 3:
    rate(100)
    r = bA.pos - bB.pos
    F = vector(0,0,0)
    if mag(r) < 2*R:
        F = k*(2*R-mag(r))*norm(r)
    bA.p = bA.p + F*dt
    bB.p = bB.p - F*dt
    bA.pos = bA.pos + bA.p*dt/bA.m
    bB.pos = bB.pos + bB.p*dt/bB.m
    t = t + dt

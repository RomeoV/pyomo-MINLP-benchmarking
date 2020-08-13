#  MINLP written by GAMS Convert at 08/13/20 17:37:59
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         91       31       18       42        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         77       61       16        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        301      259       42        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(320,500),initialize=500)
m.x18 = Var(within=Reals,bounds=(320,500),initialize=500)
m.x19 = Var(within=Reals,bounds=(320,500),initialize=500)
m.x20 = Var(within=Reals,bounds=(380,480),initialize=480)
m.x21 = Var(within=Reals,bounds=(380,480),initialize=480)
m.x22 = Var(within=Reals,bounds=(380,480),initialize=480)
m.x23 = Var(within=Reals,bounds=(360,460),initialize=460)
m.x24 = Var(within=Reals,bounds=(360,460),initialize=460)
m.x25 = Var(within=Reals,bounds=(360,460),initialize=460)
m.x26 = Var(within=Reals,bounds=(360,380),initialize=380)
m.x27 = Var(within=Reals,bounds=(360,380),initialize=380)
m.x28 = Var(within=Reals,bounds=(360,380),initialize=380)
m.x29 = Var(within=Reals,bounds=(320,380),initialize=380)
m.x30 = Var(within=Reals,bounds=(320,380),initialize=380)
m.x31 = Var(within=Reals,bounds=(320,380),initialize=380)
m.x32 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x33 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x34 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=1080)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=1080)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=400)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=400)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=600)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=600)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=400)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=400)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=720)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=720)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(10,None),initialize=210)
m.x57 = Var(within=Reals,bounds=(10,None),initialize=210)
m.x58 = Var(within=Reals,bounds=(10,None),initialize=210)
m.x59 = Var(within=Reals,bounds=(10,None),initialize=190)
m.x60 = Var(within=Reals,bounds=(10,None),initialize=190)
m.x61 = Var(within=Reals,bounds=(10,None),initialize=190)
m.x62 = Var(within=Reals,bounds=(10,None),initialize=170)
m.x63 = Var(within=Reals,bounds=(10,None),initialize=170)
m.x64 = Var(within=Reals,bounds=(10,None),initialize=170)
m.x65 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x66 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x67 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x68 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x69 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x70 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x71 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x72 = Var(within=Reals,bounds=(10,None),initialize=160)
m.x73 = Var(within=Reals,bounds=(10,None),initialize=140)
m.x74 = Var(within=Reals,bounds=(10,None),initialize=60)
m.x75 = Var(within=Reals,bounds=(10,None),initialize=60)
m.x76 = Var(within=Reals,bounds=(10,None),initialize=410)

m.obj = Objective(expr=1200*((1e-6 + m.x35/(1e-6 + (1e-6 + 0.5*m.x56*m.x57*(m.x56 + m.x57))**0.33333))**0.6 + (1e-6 + 
                       m.x36/(1e-6 + (1e-6 + 0.5*m.x57*m.x58*(m.x57 + m.x58))**0.33333))**0.6 + (1e-6 + 99.9853968566039
                       *m.x37)**0.6 + (1e-6 + m.x38/(1e-6 + (1e-6 + 0.5*m.x59*m.x60*(m.x59 + m.x60))**0.33333))**0.6 + (
                       1e-6 + m.x39/(1e-6 + (1e-6 + 0.5*m.x60*m.x61*(m.x60 + m.x61))**0.33333))**0.6 + (1e-6 + 
                       99.9853968566039*m.x40)**0.6 + (1e-6 + m.x41/(1e-6 + (1e-6 + 0.5*m.x62*m.x63*(m.x62 + m.x63))**
                       0.33333))**0.6 + (1e-6 + m.x42/(1e-6 + (1e-6 + 0.5*m.x63*m.x64*(m.x63 + m.x64))**0.33333))**0.6
                        + (1e-6 + 99.9853968566039*m.x43)**0.6 + (1e-6 + m.x44/(1e-6 + (1e-6 + 0.5*m.x65*m.x66*(m.x65 + 
                       m.x66))**0.33333))**0.6 + (1e-6 + m.x45/(1e-6 + (1e-6 + 0.5*m.x66*m.x67*(m.x66 + m.x67))**0.33333
                       ))**0.6 + (1e-6 + 99.9853968566039*m.x46)**0.6 + (1e-6 + m.x47/(1e-6 + (1e-6 + 0.5*m.x68*m.x69*(
                       m.x68 + m.x69))**0.33333))**0.6 + (1e-6 + m.x48/(1e-6 + (1e-6 + 0.5*m.x69*m.x70*(m.x69 + m.x70))
                       **0.33333))**0.6 + (1e-6 + 99.9853968566039*m.x49)**0.6) + 1200*(1e-6 + m.x55/(1e-6 + 40*m.x76*(
                       20 + 0.5*m.x76))**0.33333)**0.6 + 140*m.x55 + 1200*((1e-6 + m.x50/(1e-6 + 10*m.x71*(20 + m.x71))
                       **0.33333)**0.6 + (1e-6 + m.x51/(1e-6 + 40*m.x72*(80 + m.x72))**0.33333)**0.6 + (1e-6 + m.x52/(
                       1e-6 + 30*m.x73*(60 + m.x73))**0.33333)**0.6 + (1e-6 + m.x53/(1e-6 + 30*m.x74*(60 + m.x74))**
                       0.33333)**0.6 + (1e-6 + m.x54/(1e-6 + 10*m.x75*(20 + m.x75))**0.33333)**0.6) + 10*m.x50 + 10*
                       m.x51 + 10*m.x52 + 10*m.x53 + 10*m.x54 + 5500*m.b1 + 5500*m.b2 + 5500*m.b3 + 5500*m.b4
                        + 5500*m.b5 + 5500*m.b6 + 5500*m.b7 + 5500*m.b8 + 5500*m.b9 + 5500*m.b10 + 5500*m.b11
                        + 5500*m.b12 + 5500*m.b13 + 5500*m.b14 + 5500*m.b15 + 5500*m.b16, sense=minimize)

m.c1 = Constraint(expr=   6*m.x17 - 6*m.x18 - m.x35 == 0)

m.c2 = Constraint(expr=   6*m.x18 - 6*m.x19 - m.x36 == 0)

m.c3 = Constraint(expr=   4*m.x20 - 4*m.x21 - m.x38 == 0)

m.c4 = Constraint(expr=   4*m.x21 - 4*m.x22 - m.x39 == 0)

m.c5 = Constraint(expr=   6*m.x23 - 6*m.x24 - m.x41 == 0)

m.c6 = Constraint(expr=   6*m.x24 - 6*m.x25 - m.x42 == 0)

m.c7 = Constraint(expr=   20*m.x26 - 20*m.x27 - m.x44 == 0)

m.c8 = Constraint(expr=   20*m.x27 - 20*m.x28 - m.x45 == 0)

m.c9 = Constraint(expr=   12*m.x29 - 12*m.x30 - m.x47 == 0)

m.c10 = Constraint(expr=   12*m.x30 - 12*m.x31 - m.x48 == 0)

m.c11 = Constraint(expr=   18*m.x32 - 18*m.x33 - m.x35 - m.x38 - m.x41 - m.x44 - m.x47 == 0)

m.c12 = Constraint(expr=   18*m.x33 - 18*m.x34 - m.x36 - m.x39 - m.x42 - m.x45 - m.x48 == 0)

m.c13 = Constraint(expr=   6*m.x19 - m.x50 == 1920)

m.c14 = Constraint(expr=   4*m.x22 - m.x51 == 1520)

m.c15 = Constraint(expr=   6*m.x25 - m.x52 == 2160)

m.c16 = Constraint(expr=   20*m.x28 - m.x53 == 7200)

m.c17 = Constraint(expr=   12*m.x31 - m.x54 == 3840)

m.c18 = Constraint(expr= - m.x35 - m.x36 - m.x50 == -1080)

m.c19 = Constraint(expr= - m.x38 - m.x39 - m.x51 == -400)

m.c20 = Constraint(expr= - m.x41 - m.x42 - m.x52 == -600)

m.c21 = Constraint(expr= - m.x44 - m.x45 - m.x53 == -400)

m.c22 = Constraint(expr= - m.x47 - m.x48 - m.x54 == -720)

m.c23 = Constraint(expr= - 18*m.x32 - m.x55 == -11880)

m.c24 = Constraint(expr= - m.x35 - m.x36 - m.x38 - m.x39 - m.x41 - m.x42 - m.x44 - m.x45 - m.x47 - m.x48 - m.x55
                         == -6660)

m.c25 = Constraint(expr=   m.x17 - m.x18 >= 0)

m.c26 = Constraint(expr=   m.x18 - m.x19 >= 0)

m.c27 = Constraint(expr=   m.x20 - m.x21 >= 0)

m.c28 = Constraint(expr=   m.x21 - m.x22 >= 0)

m.c29 = Constraint(expr=   m.x23 - m.x24 >= 0)

m.c30 = Constraint(expr=   m.x24 - m.x25 >= 0)

m.c31 = Constraint(expr=   m.x26 - m.x27 >= 0)

m.c32 = Constraint(expr=   m.x27 - m.x28 >= 0)

m.c33 = Constraint(expr=   m.x29 - m.x30 >= 0)

m.c34 = Constraint(expr=   m.x30 - m.x31 >= 0)

m.c35 = Constraint(expr=   m.x32 - m.x33 >= 0)

m.c36 = Constraint(expr=   m.x33 - m.x34 >= 0)

m.c37 = Constraint(expr=   m.x19 >= 320)

m.c38 = Constraint(expr=   m.x22 >= 380)

m.c39 = Constraint(expr=   m.x25 >= 360)

m.c40 = Constraint(expr=   m.x28 >= 360)

m.c41 = Constraint(expr=   m.x31 >= 320)

m.c42 = Constraint(expr= - m.x32 >= -660)

m.c43 = Constraint(expr= - m.x17 == -500)

m.c44 = Constraint(expr= - m.x20 == -480)

m.c45 = Constraint(expr= - m.x23 == -460)

m.c46 = Constraint(expr= - m.x26 == -380)

m.c47 = Constraint(expr= - m.x29 == -380)

m.c48 = Constraint(expr= - m.x34 == -290)

m.c49 = Constraint(expr= - 1080*m.b1 + m.x35 <= 0)

m.c50 = Constraint(expr= - 1080*m.b2 + m.x36 <= 0)

m.c51 = Constraint(expr= - 400*m.b3 + m.x38 <= 0)

m.c52 = Constraint(expr= - 400*m.b4 + m.x39 <= 0)

m.c53 = Constraint(expr= - 600*m.b5 + m.x41 <= 0)

m.c54 = Constraint(expr= - 600*m.b6 + m.x42 <= 0)

m.c55 = Constraint(expr= - 400*m.b7 + m.x44 <= 0)

m.c56 = Constraint(expr= - 400*m.b8 + m.x45 <= 0)

m.c57 = Constraint(expr= - 720*m.b9 + m.x47 <= 0)

m.c58 = Constraint(expr= - 720*m.b10 + m.x48 <= 0)

m.c59 = Constraint(expr= - 6660*m.b16 + m.x55 <= 0)

m.c60 = Constraint(expr= - 1080*m.b11 + m.x50 <= 0)

m.c61 = Constraint(expr= - 400*m.b12 + m.x51 <= 0)

m.c62 = Constraint(expr= - 600*m.b13 + m.x52 <= 0)

m.c63 = Constraint(expr= - 400*m.b14 + m.x53 <= 0)

m.c64 = Constraint(expr= - 720*m.b15 + m.x54 <= 0)

m.c65 = Constraint(expr=   340*m.b1 - m.x17 + m.x32 + m.x56 <= 340)

m.c66 = Constraint(expr=   340*m.b2 - m.x18 + m.x33 + m.x57 <= 340)

m.c67 = Constraint(expr=   280*m.b3 - m.x20 + m.x32 + m.x59 <= 280)

m.c68 = Constraint(expr=   280*m.b4 - m.x21 + m.x33 + m.x60 <= 280)

m.c69 = Constraint(expr=   300*m.b5 - m.x23 + m.x32 + m.x62 <= 300)

m.c70 = Constraint(expr=   300*m.b6 - m.x24 + m.x33 + m.x63 <= 300)

m.c71 = Constraint(expr=   300*m.b7 - m.x26 + m.x32 + m.x65 <= 300)

m.c72 = Constraint(expr=   300*m.b8 - m.x27 + m.x33 + m.x66 <= 300)

m.c73 = Constraint(expr=   340*m.b9 - m.x29 + m.x32 + m.x68 <= 340)

m.c74 = Constraint(expr=   340*m.b10 - m.x30 + m.x33 + m.x69 <= 340)

m.c75 = Constraint(expr=   340*m.b1 - m.x18 + m.x33 + m.x57 <= 340)

m.c76 = Constraint(expr=   340*m.b2 - m.x19 + m.x34 + m.x58 <= 340)

m.c77 = Constraint(expr=   280*m.b3 - m.x21 + m.x33 + m.x60 <= 280)

m.c78 = Constraint(expr=   280*m.b4 - m.x22 + m.x34 + m.x61 <= 280)

m.c79 = Constraint(expr=   300*m.b5 - m.x24 + m.x33 + m.x63 <= 300)

m.c80 = Constraint(expr=   300*m.b6 - m.x25 + m.x34 + m.x64 <= 300)

m.c81 = Constraint(expr=   300*m.b7 - m.x27 + m.x33 + m.x66 <= 300)

m.c82 = Constraint(expr=   300*m.b8 - m.x28 + m.x34 + m.x67 <= 300)

m.c83 = Constraint(expr=   340*m.b9 - m.x30 + m.x33 + m.x69 <= 340)

m.c84 = Constraint(expr=   340*m.b10 - m.x31 + m.x34 + m.x70 <= 340)

m.c85 = Constraint(expr= - m.x19 + m.x71 <= -320)

m.c86 = Constraint(expr= - m.x22 + m.x72 <= -320)

m.c87 = Constraint(expr= - m.x25 + m.x73 <= -320)

m.c88 = Constraint(expr= - m.x28 + m.x74 <= -320)

m.c89 = Constraint(expr= - m.x31 + m.x75 <= -320)

m.c90 = Constraint(expr=   m.x32 + m.x76 <= 700)

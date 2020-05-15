#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         31        1        2       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         37       12       25        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        237      110      127        0
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
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(2,4.5),initialize=2)
m.x27 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x28 = Var(within=Reals,bounds=(3,9),initialize=8)
m.x29 = Var(within=Reals,bounds=(0,5),initialize=4)
m.x30 = Var(within=Reals,bounds=(4,10),initialize=4.5)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=-(-0.6*m.x26**2 - 0.1*m.x29**2) - m.b1 - 0.2*m.b2 - m.b3 - 0.2*m.b4 - 0.9*m.b5 - 0.9*m.b6
                        - 0.1*m.b7 - 0.8*m.b8 - m.b9 - 0.4*m.b10 - m.b11 - 0.3*m.b12 - 0.1*m.b13 - 0.3*m.b14 - 0.5*m.b15
                        - 0.9*m.b16 - 0.8*m.b17 - 0.1*m.b18 - 0.9*m.b19 - m.b20 - m.b21 - m.b22 - 0.2*m.b23 - 0.7*m.b24
                        - 0.7*m.b25 - 0.9*m.x27 - 0.5*m.x28 + m.x30 + 1000*m.x32 + 1000*m.x33 + 1000*m.x34 + 1000*m.x35
                        + 1000*m.x36 + 1000*m.x37, sense=minimize)

m.c1 = Constraint(expr=9.57*(-2.26 + m.x26)**2 + 2.74*(-5.15 + m.x27)**2 + 9.75*(-4.03 + m.x28)**2 + 3.96*(-1.74 + m.x29
                       )**2 + 8.67*(-4.74 + m.x30)**2 + 1000*m.b1 - m.x32 <= 1077.839848)

m.c2 = Constraint(expr=8.38*(-5.51 + m.x26)**2 + 3.93*(-9.01 + m.x27)**2 + 5.18*(-3.84 + m.x28)**2 + 5.2*(-1.47 + m.x29)
                       **2 + 7.82*(-9.92 + m.x30)**2 + 1000*m.b2 - m.x32 <= 1175.970966)

m.c3 = Constraint(expr=9.81*(-4.06 + m.x26)**2 + 0.04*(-1.8 + m.x27)**2 + 4.21*(-0.71 + m.x28)**2 + 7.38*(-9.09 + m.x29)
                       **2 + 4.11*(-8.13 + m.x30)**2 + 1000*m.b3 - m.x32 <= 1201.822621)

m.c4 = Constraint(expr=7.41*(-6.3 + m.x26)**2 + 6.08*(-0.11 + m.x27)**2 + 5.46*(-4.08 + m.x28)**2 + 4.86*(-7.29 + m.x29)
                       **2 + 1.48*(-4.24 + m.x30)**2 + 1000*m.b4 - m.x32 <= 1143.953331)

m.c5 = Constraint(expr=9.96*(-2.81 + m.x26)**2 + 9.13*(-1.65 + m.x27)**2 + 2.95*(-8.08 + m.x28)**2 + 8.25*(-3.99 + m.x29
                       )**2 + 3.58*(-3.51 + m.x30)**2 + 1000*m.b5 - m.x32 <= 1154.389533)

m.c6 = Constraint(expr=9.39*(-4.29 + m.x26)**2 + 4.27*(-9.49 + m.x27)**2 + 5.09*(-2.24 + m.x28)**2 + 1.81*(-9.78 + m.x29
                       )**2 + 7.58*(-1.52 + m.x30)**2 + 1000*m.b6 - m.x32 <= 1433.317653)

m.c7 = Constraint(expr=1.88*(-9.76 + m.x26)**2 + 7.2*(-3.64 + m.x27)**2 + 6.65*(-6.62 + m.x28)**2 + 1.74*(-3.66 + m.x29)
                       **2 + 2.86*(-9.08 + m.x30)**2 + 1000*m.b7 - m.x32 <= 1109.07636)

m.c8 = Constraint(expr=4.01*(-1.37 + m.x26)**2 + 2.67*(-6.99 + m.x27)**2 + 4.86*(-7.19 + m.x28)**2 + 2.55*(-3.03 + m.x29
                       )**2 + 6.91*(-3.39 + m.x30)**2 + 1000*m.b8 - m.x32 <= 1041.595916)

m.c9 = Constraint(expr=4.18*(-8.89 + m.x26)**2 + 1.92*(-8.29 + m.x27)**2 + 2.6*(-6.05 + m.x28)**2 + 7.15*(-7.48 + m.x29)
                       **2 + 2.86*(-4.09 + m.x30)**2 + 1000*m.b9 - m.x32 <= 1144.062266)

m.c10 = Constraint(expr=7.81*(-7.42 + m.x26)**2 + 2.14*(-4.6 + m.x27)**2 + 9.63*(-0.3 + m.x28)**2 + 7.61*(-0.97 + m.x29)
                        **2 + 9.17*(-8.77 + m.x30)**2 + 1000*m.b10 - m.x32 <= 1099.834164)

m.c11 = Constraint(expr=8.96*(-1.54 + m.x26)**2 + 3.47*(-7.06 + m.x27)**2 + 5.49*(-0.01 + m.x28)**2 + 4.73*(-1.23 + 
                        m.x29)**2 + 9.43*(-3.11 + m.x30)**2 + 1000*m.b11 - m.x32 <= 1149.179125)

m.c12 = Constraint(expr=9.94*(-7.74 + m.x26)**2 + 1.63*(-4.4 + m.x27)**2 + 1.23*(-7.93 + m.x28)**2 + 4.33*(-5.95 + m.x29
                        )**2 + 7.08*(-4.88 + m.x30)**2 + 1000*m.b12 - m.x32 <= 1123.807402)

m.c13 = Constraint(expr=0.31*(-9.94 + m.x26)**2 + 5*(-5.21 + m.x27)**2 + 0.16*(-8.58 + m.x28)**2 + 2.52*(-0.13 + m.x29)
                        **2 + 3.08*(-4.57 + m.x30)**2 + 1000*m.b13 - m.x32 <= 1027.221972)

m.c14 = Constraint(expr=6.02*(-9.54 + m.x26)**2 + 0.92*(-1.57 + m.x27)**2 + 7.47*(-9.66 + m.x28)**2 + 9.74*(-5.24 + 
                        m.x29)**2 + 1.76*(-7.9 + m.x30)**2 + 1000*m.b14 - m.x32 <= 1089.926827)

m.c15 = Constraint(expr=5.06*(-7.46 + m.x26)**2 + 4.52*(-8.81 + m.x27)**2 + 1.89*(-1.67 + m.x28)**2 + 1.22*(-6.47 + 
                        m.x29)**2 + 9.05*(-1.81 + m.x30)**2 + 1000*m.b15 - m.x32 <= 1293.076557)

m.c16 = Constraint(expr=5.92*(-0.56 + m.x26)**2 + 2.56*(-8.1 + m.x27)**2 + 7.74*(-0.19 + m.x28)**2 + 6.96*(-6.11 + m.x29
                        )**2 + 5.18*(-6.4 + m.x30)**2 + 1000*m.b16 - m.x32 <= 1174.31702)

m.c17 = Constraint(expr=6.45*(-3.86 + m.x26)**2 + 1.52*(-6.68 + m.x27)**2 + 0.06*(-6.42 + m.x28)**2 + 5.34*(-7.29 + 
                        m.x29)**2 + 8.47*(-4.66 + m.x30)**2 + 1000*m.b17 - m.x32 <= 1125.102783)

m.c18 = Constraint(expr=1.04*(-2.98 + m.x26)**2 + 1.36*(-2.98 + m.x27)**2 + 5.99*(-3.03 + m.x28)**2 + 8.1*(-0.02 + m.x29
                        )**2 + 5.22*(-0.67 + m.x30)**2 + 1000*m.b18 - m.x32 <= 1222.841697)

m.c19 = Constraint(expr=1.4*(-3.61 + m.x26)**2 + 1.35*(-7.62 + m.x27)**2 + 0.59*(-1.79 + m.x28)**2 + 8.58*(-7.8 + m.x29)
                        **2 + 1.21*(-9.81 + m.x30)**2 + 1000*m.b19 - m.x32 <= 1050.485931)

m.c20 = Constraint(expr=6.68*(-5.68 + m.x26)**2 + 9.48*(-4.24 + m.x27)**2 + 1.6*(-4.17 + m.x28)**2 + 6.74*(-6.75 + m.x29
                        )**2 + 8.92*(-1.08 + m.x30)**2 + 1000*m.b20 - m.x32 <= 1361.197344)

m.c21 = Constraint(expr=1.95*(-5.48 + m.x26)**2 + 0.46*(-3.74 + m.x27)**2 + 2.9*(-3.34 + m.x28)**2 + 1.79*(-6.22 + m.x29
                        )**2 + 0.99*(-7.94 + m.x30)**2 + 1000*m.b21 - m.x32 <= 1040.326419)

m.c22 = Constraint(expr=5.18*(-8.13 + m.x26)**2 + 5.1*(-8.72 + m.x27)**2 + 8.81*(-3.93 + m.x28)**2 + 3.27*(-8.8 + m.x29)
                        **2 + 9.63*(-8.56 + m.x30)**2 + 1000*m.b22 - m.x32 <= 1161.851799)

m.c23 = Constraint(expr=1.47*(-1.37 + m.x26)**2 + 5.71*(-0.54 + m.x27)**2 + 6.95*(-1.55 + m.x28)**2 + 1.42*(-5.56 + 
                        m.x29)**2 + 3.49*(-5.85 + m.x30)**2 + 1000*m.b23 - m.x32 <= 1066.858266)

m.c24 = Constraint(expr=5.4*(-8.79 + m.x26)**2 + 3.12*(-5.04 + m.x27)**2 + 5.37*(-4.83 + m.x28)**2 + 6.1*(-6.94 + m.x29)
                        **2 + 3.71*(-0.38 + m.x30)**2 + 1000*m.b24 - m.x32 <= 1340.580732)

m.c25 = Constraint(expr=6.32*(-2.66 + m.x26)**2 + 0.81*(-4.19 + m.x27)**2 + 6.12*(-6.49 + m.x28)**2 + 6.73*(-8.04 + 
                        m.x29)**2 + 7.93*(-1.66 + m.x30)**2 + 1000*m.b25 - m.x32 <= 1407.519966)

m.c26 = Constraint(expr=   m.x26 - m.x27 + m.x28 + m.x29 + m.x30 - m.x33 <= 10)

m.c27 = Constraint(expr=   0.6*m.x26 - 0.9*m.x27 - 0.5*m.x28 + 0.1*m.x29 + m.x30 - m.x34 <= -0.64)

m.c28 = Constraint(expr=   m.x26 - m.x27 + m.x28 - m.x29 + m.x30 + m.x35 >= 0.69)

m.c29 = Constraint(expr=   0.157*m.x26 + 0.05*m.x27 - m.x36 <= 1.5)

m.c30 = Constraint(expr=   0.25*m.x27 + 1.05*m.x29 - 0.3*m.x30 - m.x37 >= 4.5)

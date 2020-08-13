#  MINLP written by GAMS Convert at 08/13/20 17:37:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         23       13        3        7        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         29       14       15        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         78       71        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x5 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x6 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=100)
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
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=-((416000 - 416000*exp(-0.1*m.x1/m.x4))*m.x4 + 37440*m.x1 - 100*m.x4 + (124615.384615385 - 
                       124615.384615385*exp(-0.13*m.x2/m.x5))*m.x5 + 9000*m.x2 - 90*m.x5 + (278666.666666667 - 
                       278666.666666667*exp(-0.09*m.x3/m.x6))*m.x6 + 15840*m.x3 - 80*m.x6)/m.x13, sense=minimize)

m.c2 = Constraint(expr= - 1300*m.x1 + m.x7 + 350*m.x13 == 0)

m.c3 = Constraint(expr= - 1000*m.x2 + m.x8 + 300*m.x13 == 0)

m.c4 = Constraint(expr= - 1100*m.x3 + m.x9 + 300*m.x13 == 0)

m.c5 = Constraint(expr=   m.x7 - 300*m.x13 <= 0)

m.c6 = Constraint(expr=   m.x8 - 300*m.x13 <= 0)

m.c7 = Constraint(expr=   m.x9 - 300*m.x13 <= 0)

m.c8 = Constraint(expr=   m.x4 - 0.01*m.b14 - m.b15 - 2*m.b16 - 3*m.b17 - 4*m.b18 == 0)

m.c9 = Constraint(expr=   m.x5 - 0.01*m.b19 - m.b20 - 2*m.b21 - 3*m.b22 - 4*m.b23 == 0)

m.c10 = Constraint(expr=   m.x6 - 0.01*m.b24 - m.b25 - 2*m.b26 - 3*m.b27 - 4*m.b28 == 0)

m.c11 = Constraint(expr= - m.b14 - m.b15 - m.b16 - m.b17 - m.b18 == -1)

m.c12 = Constraint(expr= - m.b19 - m.b20 - m.b21 - m.b22 - m.b23 == -1)

m.c13 = Constraint(expr= - m.b24 - m.b25 - m.b26 - m.b27 - m.b28 == -1)

m.c14 = Constraint(expr= - m.x1 - 2*m.x4 + m.x10 == 0)

m.c15 = Constraint(expr= - m.x2 - 3*m.x5 + m.x11 == 0)

m.c16 = Constraint(expr= - m.x3 - 3*m.x6 + m.x12 == 0)

m.c17 = Constraint(expr=   m.x10 + m.x11 + m.x12 - m.x13 <= 0)

m.c18 = Constraint(expr=   m.x1 + 150*m.b14 <= 150)

m.c19 = Constraint(expr=   m.x2 + 150*m.b19 <= 150)

m.c20 = Constraint(expr=   m.x3 + 150*m.b24 <= 150)

m.c21 = Constraint(expr=   m.x4 >= 1)

m.c22 = Constraint(expr=   m.x5 >= 1)

m.c23 = Constraint(expr=   m.x6 >= 1)

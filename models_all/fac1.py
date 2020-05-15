#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         19       11        2        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         23       17        6        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         75       59       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,300),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=50*(m.x1 + m.x2 + m.x3 + m.x4 + m.x9 + m.x10 + m.x11 + m.x12)**2.5 + 70*(m.x5 + m.x6 + m.x7 + 
                       m.x8 + m.x13 + m.x14 + m.x15 + m.x16)**2.5 + 10*m.x1 + 15*m.x2 + 20*m.x3 + 10*m.x4 + 5*m.x5 + 5*
                       m.x6 + 30*m.x7 + 10*m.x8 + 25*m.x9 + 20*m.x10 + 15*m.x11 + 20*m.x12 + 30*m.x13 + 10*m.x14 + 10*
                       m.x15 + 30*m.x16 + 2000*m.b21 + 2500*m.b22, sense=minimize)

m.c2 = Constraint(expr=   m.x1 + m.x3 + m.x5 + m.x7 <= 100)

m.c3 = Constraint(expr=   m.x2 + m.x4 + m.x6 + m.x8 <= 200)

m.c4 = Constraint(expr=   m.x9 + m.x11 + m.x13 + m.x15 <= 150)

m.c5 = Constraint(expr=   m.x10 + m.x12 + m.x14 + m.x16 <= 120)

m.c6 = Constraint(expr=   m.x1 + m.x9 - 120*m.b17 == 0)

m.c7 = Constraint(expr=   m.x2 + m.x10 - 140*m.b17 == 0)

m.c8 = Constraint(expr=   m.x3 + m.x11 - 130*m.b18 == 0)

m.c9 = Constraint(expr=   m.x4 + m.x12 - 180*m.b18 == 0)

m.c10 = Constraint(expr=   m.x5 + m.x13 - 120*m.b19 == 0)

m.c11 = Constraint(expr=   m.x6 + m.x14 - 140*m.b19 == 0)

m.c12 = Constraint(expr=   m.x7 + m.x15 - 130*m.b20 == 0)

m.c13 = Constraint(expr=   m.x8 + m.x16 - 180*m.b20 == 0)

m.c14 = Constraint(expr=   260*m.b17 + 310*m.b18 - 2500*m.b21 <= 0)

m.c15 = Constraint(expr=   260*m.b19 + 310*m.b20 - 3200*m.b22 <= 0)

m.c16 = Constraint(expr=   260*m.b17 + 310*m.b18 - 50*m.b21 >= 0)

m.c17 = Constraint(expr=   260*m.b19 + 310*m.b20 - 50*m.b22 >= 0)

m.c18 = Constraint(expr=   m.b17 + m.b19 == 1)

m.c19 = Constraint(expr=   m.b18 + m.b20 == 1)

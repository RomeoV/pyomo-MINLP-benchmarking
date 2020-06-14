#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         24        3        0       21        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         18       10        8        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         91       79       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,3),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=exp(m.x1) - 10*m.x1 + exp(0.833333*m.x2) - 15*m.x2 - 65*log(1 + m.x3 + m.x4) + 15*m.x3 + 80*m.x4
                        - 90*log(1 + m.x5) + 25*m.x5 - 80*log(1 + m.x6) + 35*m.x6 - 40*m.x7 + 15*m.x8 - 35*m.x9
                        + 5*m.b10 + 8*m.b11 + 6*m.b12 + 10*m.b13 + 6*m.b14 + 7*m.b15 + 4*m.b16 + 5*m.b17
                        + 120, sense=minimize)

m.c1 = Constraint(expr=(-1.5*log(1 + m.x5)) - log(1 + m.x6) - m.x8 <= 0)

m.c2 = Constraint(expr=-log(1 + m.x3 + m.x4) <= 0)

m.c3 = Constraint(expr= - m.x1 - m.x2 + m.x3 + 2*m.x4 + 0.8*m.x5 + 0.8*m.x6 - 0.5*m.x7 - m.x8 - 2*m.x9 <= 0)

m.c4 = Constraint(expr= - m.x1 - m.x2 + 2*m.x4 + 0.8*m.x5 + 0.8*m.x6 - 2*m.x7 - m.x8 - 2*m.x9 <= 0)

m.c5 = Constraint(expr= - 2*m.x4 - 0.8*m.x5 - 0.8*m.x6 + 2*m.x7 + m.x8 + 2*m.x9 <= 0)

m.c6 = Constraint(expr= - 0.8*m.x5 - 0.8*m.x6 + m.x8 <= 0)

m.c7 = Constraint(expr= - m.x4 + m.x7 + m.x9 <= 0)

m.c8 = Constraint(expr= - 0.4*m.x5 - 0.4*m.x6 + 1.5*m.x8 <= 0)

m.c9 = Constraint(expr=   0.16*m.x5 + 0.16*m.x6 - 1.2*m.x8 <= 0)

m.c10 = Constraint(expr=   m.x3 - 0.8*m.x4 <= 0)

m.c11 = Constraint(expr= - m.x3 + 0.4*m.x4 <= 0)

m.c12 = Constraint(expr=exp(m.x1) - 10*m.b10 <= 1)

m.c13 = Constraint(expr=exp(0.833333*m.x2) - 10*m.b11 <= 1)

m.c14 = Constraint(expr=   m.x7 - 10*m.b12 <= 0)

m.c15 = Constraint(expr=   0.8*m.x5 + 0.8*m.x6 - 10*m.b13 <= 0)

m.c16 = Constraint(expr=   2*m.x4 - 2*m.x7 - 2*m.x9 - 10*m.b14 <= 0)

m.c17 = Constraint(expr=   m.x5 - 10*m.b15 <= 0)

m.c18 = Constraint(expr=   m.x6 - 10*m.b16 <= 0)

m.c19 = Constraint(expr=   m.x3 + m.x4 - 10*m.b17 <= 0)

m.c20 = Constraint(expr=   m.b10 + m.b11 == 1)

m.c21 = Constraint(expr=   m.b13 + m.b14 <= 1)

m.c22 = Constraint(expr= - m.b13 + m.b15 + m.b16 == 0)

m.c23 = Constraint(expr=   m.b12 - m.b17 <= 0)

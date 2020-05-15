#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         15        2        0       13        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         12        7        5        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         49       41        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,3),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=exp(m.x1) - 10*m.x1 + exp(0.833333*m.x2) - 15*m.x2 - 60*log(1 + m.x4 + m.x5) + 15*m.x4 + 5*m.x5
                        - 15*m.x3 - 20*m.x6 + 5*m.b7 + 8*m.b8 + 6*m.b9 + 10*m.b10 + 6*m.b11 + 140, sense=minimize)

m.c1 = Constraint(expr=-log(1 + m.x4 + m.x5) <= 0)

m.c2 = Constraint(expr=exp(m.x1) - 10*m.b7 <= 1)

m.c3 = Constraint(expr=exp(0.833333*m.x2) - 10*m.b8 <= 1)

m.c4 = Constraint(expr=   1.25*m.x3 - 10*m.b9 <= 0)

m.c5 = Constraint(expr=   m.x4 + m.x5 - 10*m.b10 <= 0)

m.c6 = Constraint(expr= - 2*m.x3 + 2*m.x6 - 10*m.b11 <= 0)

m.c7 = Constraint(expr= - m.x1 - m.x2 - 2*m.x3 + m.x4 + 2*m.x6 <= 0)

m.c8 = Constraint(expr= - m.x1 - m.x2 - 0.75*m.x3 + m.x4 + 2*m.x6 <= 0)

m.c9 = Constraint(expr=   m.x3 - m.x6 <= 0)

m.c10 = Constraint(expr=   2*m.x3 - m.x4 - 2*m.x6 <= 0)

m.c11 = Constraint(expr= - 0.5*m.x4 + m.x5 <= 0)

m.c12 = Constraint(expr= - 0.2*m.x4 - m.x5 <= 0)

m.c13 = Constraint(expr=   m.b7 + m.b8 == 1)

m.c14 = Constraint(expr=   m.b10 + m.b11 <= 1)

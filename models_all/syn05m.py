#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         29        6        6       17        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       16        5        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         84       81        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   5*m.x8 - 2*m.x13 + 200*m.x14 + 250*m.x15 + 300*m.x16 - 5*m.b17 - 8*m.b18 - 6*m.b19 - 10*m.b20
                        - 6*m.b21, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c3 = Constraint(expr= - m.x5 - m.x6 + m.x7 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c5 = Constraint(expr=   m.x9 - m.x10 - m.x11 - m.x12 == 0)

m.c6 = Constraint(expr=-log(1 + m.x3) + m.x5 + m.b17 <= 1)

m.c7 = Constraint(expr=   m.x3 - 10*m.b17 <= 0)

m.c8 = Constraint(expr=   m.x5 - 2.39789527279837*m.b17 <= 0)

m.c9 = Constraint(expr=-1.2*log(1 + m.x4) + m.x6 + m.b18 <= 1)

m.c10 = Constraint(expr=   m.x4 - 10*m.b18 <= 0)

m.c11 = Constraint(expr=   m.x6 - 2.87747432735804*m.b18 <= 0)

m.c12 = Constraint(expr= - 0.75*m.x10 + m.x14 + m.b19 <= 1)

m.c13 = Constraint(expr= - 0.75*m.x10 + m.x14 - m.b19 >= -1)

m.c14 = Constraint(expr=   m.x10 - 2.87747432735804*m.b19 <= 0)

m.c15 = Constraint(expr=   m.x14 - 2.15810574551853*m.b19 <= 0)

m.c16 = Constraint(expr=-1.5*log(1 + m.x11) + m.x15 + m.b20 <= 1)

m.c17 = Constraint(expr=   m.x11 - 2.87747432735804*m.b20 <= 0)

m.c18 = Constraint(expr=   m.x15 - 2.03277599268042*m.b20 <= 0)

m.c19 = Constraint(expr= - m.x12 + m.x16 + m.b21 <= 1)

m.c20 = Constraint(expr= - m.x12 + m.x16 - m.b21 >= -1)

m.c21 = Constraint(expr= - 0.5*m.x13 + m.x16 + m.b21 <= 1)

m.c22 = Constraint(expr= - 0.5*m.x13 + m.x16 - m.b21 >= -1)

m.c23 = Constraint(expr=   m.x12 - 2.87747432735804*m.b21 <= 0)

m.c24 = Constraint(expr=   m.x13 - 7*m.b21 <= 0)

m.c25 = Constraint(expr=   m.x16 - 3.5*m.b21 <= 0)

m.c26 = Constraint(expr=   m.b17 + m.b18 == 1)

m.c27 = Constraint(expr=   m.b17 + m.b18 - m.b19 >= 0)

m.c28 = Constraint(expr=   m.b17 + m.b18 - m.b20 >= 0)

m.c29 = Constraint(expr=   m.b17 + m.b18 - m.b21 >= 0)

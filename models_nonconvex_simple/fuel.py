#  MINLP written by GAMS Convert at 08/13/20 17:37:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         16        7        6        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         16       13        3        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         39       33        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=100)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=100)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=100)
m.x7 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x8 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x9 = Var(within=Reals,bounds=(50,700),initialize=50)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,4000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,4000),initialize=0)
m.x15 = Var(within=Reals,bounds=(2000,4000),initialize=2000)

m.obj = Objective(expr=0.0025*m.x7**2 + 6*m.x7 + 0.0025*m.x8**2 + 6*m.x8 + 0.0025*m.x9**2 + 6*m.x9
                        + 900, sense=minimize)

m.c2 = Constraint(expr= - 100*m.b1 + m.x4 >= 0)

m.c3 = Constraint(expr= - 100*m.b2 + m.x5 >= 0)

m.c4 = Constraint(expr= - 100*m.b3 + m.x6 >= 0)

m.c5 = Constraint(expr= - 500*m.b1 + m.x4 <= 0)

m.c6 = Constraint(expr= - 500*m.b2 + m.x5 <= 0)

m.c7 = Constraint(expr= - 500*m.b3 + m.x6 <= 0)

m.c8 = Constraint(expr=   m.x10 + m.x13 == 3500)

m.c9 = Constraint(expr=   m.x11 - m.x13 + m.x14 == 500)

m.c10 = Constraint(expr=   m.x12 - m.x14 + m.x15 == 500)

m.c11 = Constraint(expr=   m.x4 + m.x7 >= 400)

m.c12 = Constraint(expr=   m.x5 + m.x8 >= 900)

m.c13 = Constraint(expr=   m.x6 + m.x9 >= 700)

m.c14 = Constraint(expr=-(0.005*m.x4**2 + m.x4) - 50*m.b1 + m.x10 == 0)

m.c15 = Constraint(expr=-(0.005*m.x5**2 + m.x5) - 50*m.b2 + m.x11 == 0)

m.c16 = Constraint(expr=-(0.005*m.x6**2 + m.x6) - 50*m.b3 + m.x12 == 0)

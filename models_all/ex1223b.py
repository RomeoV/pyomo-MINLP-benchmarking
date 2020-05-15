#  MINLP written by GAMS Convert at 05/15/20 00:53:32
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10        1        0        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          8        4        4        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         32       15       17        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,10),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=(-1 + m.b4)**2 + (-2 + m.b5)**2 + (-1 + m.b6)**2 - log(1 + m.b7) + (-1 + m.x1)**2 + (-2 + m.x2)**
                       2 + (-3 + m.x3)**2, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.b4 + m.b5 + m.b6 <= 5)

m.c2 = Constraint(expr=m.b6**2 + m.x1**2 + m.x2**2 + m.x3**2 <= 5.5)

m.c3 = Constraint(expr=   m.x1 + m.b4 <= 1.2)

m.c4 = Constraint(expr=   m.x2 + m.b5 <= 1.8)

m.c5 = Constraint(expr=   m.x3 + m.b6 <= 2.5)

m.c6 = Constraint(expr=   m.x1 + m.b7 <= 1.2)

m.c7 = Constraint(expr=m.b5**2 + m.x2**2 <= 1.64)

m.c8 = Constraint(expr=m.b6**2 + m.x3**2 <= 4.25)

m.c9 = Constraint(expr=m.b5**2 + m.x3**2 <= 4.64)

#  MINLP written by GAMS Convert at 08/13/20 17:37:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        1        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        3        1        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          9        7        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x2 = Var(within=Reals,bounds=(-2.22554,-1),initialize=-1)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=5*(-0.5 + m.x1)**2 - 0.7*m.b3 + 0.8, sense=minimize)

m.c1 = Constraint(expr=-exp((-0.2) + m.x1) - m.x2 <= 0)

m.c2 = Constraint(expr=   m.x2 + 1.1*m.b3 <= -1)

m.c3 = Constraint(expr=   m.x1 - 1.2*m.b3 <= 0)

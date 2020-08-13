#  MINLP written by GAMS Convert at 08/13/20 17:37:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        1        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        2        1        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#          7        6        1        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1.6),initialize=0)

m.obj = Objective(expr=   m.b1 + 2*m.x2, sense=minimize)

m.c1 = Constraint(expr=-m.x2**2 - m.b1 <= -1.25)

m.c2 = Constraint(expr=   m.b1 + m.x2 <= 1.6)

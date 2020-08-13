#  MINLP written by GAMS Convert at 08/13/20 17:37:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        1        0        7        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         17        1       16        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        123        1      122        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0.171747132)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0.843266708)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0.550375356)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0.301137904)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0.292212117)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0.224052867)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0.349830504)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0.998117627)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0.578733378)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0.991133039)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0.130692483)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0.639718759)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0.159517864)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0.250080533)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0.668928609)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0.435356381)

m.obj = Objective(expr=10*m.b5*m.b7*m.b9*m.b10*m.b14*m.b15*m.b16 + 7*m.b1*m.b2*m.b3*m.b4*m.b8*m.b11 + m.b3*m.b4*m.b6*
                       m.b7*m.b8 + 12*m.b3*m.b4*m.b8*m.b11 + 8*m.b6*m.b7*m.b8*m.b12 + 3*m.b6*m.b7*m.b9*m.b14*m.b16 + 
                       m.b9*m.b10*m.b14*m.b16 + 5*m.b5*m.b10*m.b14*m.b15*m.b16 + 3*m.b1*m.b2*m.b11*m.b12
                       , sense=minimize)

m.c2 = Constraint(expr=3*m.b5*m.b7*m.b9*m.b10*m.b14*m.b15*m.b16 - 12*m.b1*m.b2*m.b3*m.b4*m.b8*m.b11 - 8*m.b3*m.b4*m.b6*
                       m.b7*m.b8 + m.b3*m.b4*m.b8*m.b11 - 7*m.b1*m.b2*m.b11*m.b12 + 2*m.b13*m.b14*m.b15*m.b16 <= -2)

m.c3 = Constraint(expr=m.b1*m.b2*m.b3*m.b4*m.b8*m.b11 - 10*m.b3*m.b4*m.b6*m.b7*m.b8 - 5*m.b6*m.b7*m.b8*m.b12 + m.b6*m.b7
                       *m.b9*m.b14*m.b16 + 7*m.b9*m.b10*m.b14*m.b16 + m.b5*m.b10*m.b14*m.b15*m.b16 <= -1)

m.c4 = Constraint(expr=5*m.b5*m.b7*m.b9*m.b10*m.b14*m.b15*m.b16 - 3*m.b1*m.b2*m.b3*m.b4*m.b8*m.b11 - m.b3*m.b4*m.b6*m.b7
                       *m.b8 - 2*m.b5*m.b10*m.b14*m.b15*m.b16 + m.b13*m.b14*m.b15*m.b16 <= -1)

m.c5 = Constraint(expr=3*m.b1*m.b2*m.b3*m.b4*m.b8*m.b11 - 5*m.b5*m.b7*m.b9*m.b10*m.b14*m.b15*m.b16 + m.b3*m.b4*m.b6*m.b7
                       *m.b8 + 2*m.b5*m.b10*m.b14*m.b15*m.b16 - m.b13*m.b14*m.b15*m.b16 <= 1)

m.c6 = Constraint(expr=(-4*m.b3*m.b4*m.b6*m.b7*m.b8) - 2*m.b3*m.b4*m.b8*m.b11 - 5*m.b6*m.b7*m.b9*m.b14*m.b16 + m.b9*
                       m.b10*m.b14*m.b16 - 9*m.b5*m.b10*m.b14*m.b15*m.b16 - 2*m.b1*m.b2*m.b11*m.b12 <= -3)

m.c7 = Constraint(expr=9*m.b1*m.b2*m.b3*m.b4*m.b8*m.b11 - 12*m.b3*m.b4*m.b8*m.b11 - 7*m.b6*m.b7*m.b8*m.b12 + 6*m.b6*m.b7
                       *m.b9*m.b14*m.b16 + 2*m.b5*m.b10*m.b14*m.b15*m.b16 - 15*m.b1*m.b2*m.b11*m.b12 + 3*m.b13*m.b14*
                       m.b15*m.b16 <= -7)

m.c8 = Constraint(expr=5*m.b1*m.b2*m.b3*m.b4*m.b8*m.b11 - 8*m.b5*m.b7*m.b9*m.b10*m.b14*m.b15*m.b16 + 2*m.b3*m.b4*m.b6*
                       m.b7*m.b8 - 7*m.b3*m.b4*m.b8*m.b11 - m.b6*m.b7*m.b8*m.b12 - 5*m.b9*m.b10*m.b14*m.b16 - 10*m.b1*
                       m.b2*m.b11*m.b12 <= -1)

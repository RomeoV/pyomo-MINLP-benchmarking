#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         25        7        0       18        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         38        5       31        2        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        210      202        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i4 = Var(within=Integers,bounds=(1,100),initialize=1)
m.x5 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x6 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x7 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x8 = Var(within=Reals,bounds=(1,None),initialize=1)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + m.b9 + 2*m.b10 + 3*m.b11 + 4*m.b12 + 5*m.b13 + 6*m.b14 + 7*m.b15
                        + 8*m.b16 + m.b17 + 2*m.b18 + 3*m.b19 + 4*m.b20 + 5*m.b21 + 6*m.b22 + 7*m.b23, sense=minimize)

m.c2 = Constraint(expr=   460*m.b24 + 920*m.b25 + 1380*m.b26 + 1840*m.b27 + 570*m.b32 + 1140*m.b33 + 1710*m.b34 <= 1900)

m.c3 = Constraint(expr=   460*m.b28 + 920*m.b29 + 1380*m.b30 + 1840*m.b31 + 570*m.b35 + 1140*m.b36 + 1710*m.b37 <= 1900)

m.c4 = Constraint(expr= - 460*m.b24 - 920*m.b25 - 1380*m.b26 - 1840*m.b27 - 570*m.b32 - 1140*m.b33 - 1710*m.b34
                        <= -1700)

m.c5 = Constraint(expr= - 460*m.b28 - 920*m.b29 - 1380*m.b30 - 1840*m.b31 - 570*m.b35 - 1140*m.b36 - 1710*m.b37
                        <= -1700)

m.c6 = Constraint(expr=   m.b24 + 2*m.b25 + 3*m.b26 + 4*m.b27 + m.b32 + 2*m.b33 + 3*m.b34 <= 5)

m.c7 = Constraint(expr=   m.b28 + 2*m.b29 + 3*m.b30 + 4*m.b31 + m.b35 + 2*m.b36 + 3*m.b37 <= 5)

m.c8 = Constraint(expr=   m.b1 - m.b9 - 2*m.b10 - 3*m.b11 - 4*m.b12 - 5*m.b13 - 6*m.b14 - 7*m.b15 - 8*m.b16 <= 0)

m.c9 = Constraint(expr=   m.b2 - m.b17 - 2*m.b18 - 3*m.b19 - 4*m.b20 - 5*m.b21 - 6*m.b22 - 7*m.b23 <= 0)

m.c10 = Constraint(expr= - 8*m.b1 + m.b9 + 2*m.b10 + 3*m.b11 + 4*m.b12 + 5*m.b13 + 6*m.b14 + 7*m.b15 + 8*m.b16 <= 0)

m.c11 = Constraint(expr= - 7*m.b2 + m.b17 + 2*m.b18 + 3*m.b19 + 4*m.b20 + 5*m.b21 + 6*m.b22 + 7*m.b23 <= 0)

m.c12 = Constraint(expr=   m.i3 - 3*m.b9 - 8*m.b10 - 15*m.b11 - 24*m.b12 - 35*m.b13 - 48*m.b14 - 63*m.b15 - 80*m.b16
                         == 1)

m.c13 = Constraint(expr=   m.i4 - 3*m.b17 - 8*m.b18 - 15*m.b19 - 24*m.b20 - 35*m.b21 - 48*m.b22 - 63*m.b23 == 1)

m.c14 = Constraint(expr=   m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 <= 1)

m.c15 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 <= 1)

m.c16 = Constraint(expr=   m.x5 - 3*m.b24 - 8*m.b25 - 15*m.b26 - 24*m.b27 == 1)

m.c17 = Constraint(expr=   m.x6 - 3*m.b28 - 8*m.b29 - 15*m.b30 - 24*m.b31 == 1)

m.c18 = Constraint(expr=   m.x7 - 3*m.b32 - 8*m.b33 - 15*m.b34 == 1)

m.c19 = Constraint(expr=   m.x8 - 3*m.b35 - 8*m.b36 - 15*m.b37 == 1)

m.c20 = Constraint(expr=   m.b24 + m.b25 + m.b26 + m.b27 <= 1)

m.c21 = Constraint(expr=   m.b28 + m.b29 + m.b30 + m.b31 <= 1)

m.c22 = Constraint(expr=   m.b32 + m.b33 + m.b34 <= 1)

m.c23 = Constraint(expr=   m.b35 + m.b36 + m.b37 <= 1)

m.c24 = Constraint(expr=-(sqrt(m.i3*m.x5) + sqrt(m.i4*m.x6)) + m.b9 + 2*m.b10 + 3*m.b11 + 4*m.b12 + 5*m.b13 + 6*m.b14
                         + 7*m.b15 + 8*m.b16 + m.b17 + 2*m.b18 + 3*m.b19 + 4*m.b20 + 5*m.b21 + 6*m.b22 + 7*m.b23 + m.b24
                         + 2*m.b25 + 3*m.b26 + 4*m.b27 + m.b28 + 2*m.b29 + 3*m.b30 + 4*m.b31 <= -10)

m.c25 = Constraint(expr=-(sqrt(m.i3*m.x7) + sqrt(m.i4*m.x8)) + m.b9 + 2*m.b10 + 3*m.b11 + 4*m.b12 + 5*m.b13 + 6*m.b14
                         + 7*m.b15 + 8*m.b16 + m.b17 + 2*m.b18 + 3*m.b19 + 4*m.b20 + 5*m.b21 + 6*m.b22 + 7*m.b23 + m.b32
                         + 2*m.b33 + 3*m.b34 + m.b35 + 2*m.b36 + 3*m.b37 <= -9)

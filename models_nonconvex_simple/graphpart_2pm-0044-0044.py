#  MINLP written by GAMS Convert at 08/13/20 17:37:50
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         17       17        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         49        1       48        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         97       49       48        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=(-m.b1*m.b4) - m.b1*m.b10 + m.b1*m.b13 + m.b1*m.b37 - m.b2*m.b5 - m.b2*m.b11 + m.b2*m.b14 + m.b2*
                       m.b38 - m.b3*m.b6 - m.b3*m.b12 + m.b3*m.b15 + m.b3*m.b39 + m.b4*m.b7 + m.b4*m.b16 - m.b4*m.b40 + 
                       m.b5*m.b8 + m.b5*m.b17 - m.b5*m.b41 + m.b6*m.b9 + m.b6*m.b18 - m.b6*m.b42 - m.b7*m.b10 + m.b7*
                       m.b19 + m.b7*m.b43 - m.b8*m.b11 + m.b8*m.b20 + m.b8*m.b44 - m.b9*m.b12 + m.b9*m.b21 + m.b9*m.b45
                        - m.b10*m.b22 + m.b10*m.b46 - m.b11*m.b23 + m.b11*m.b47 - m.b12*m.b24 + m.b12*m.b48 - m.b13*
                       m.b16 + m.b13*m.b22 - m.b13*m.b25 - m.b14*m.b17 + m.b14*m.b23 - m.b14*m.b26 - m.b15*m.b18 + m.b15
                       *m.b24 - m.b15*m.b27 - m.b16*m.b19 + m.b16*m.b28 - m.b17*m.b20 + m.b17*m.b29 - m.b18*m.b21 + 
                       m.b18*m.b30 + m.b19*m.b22 - m.b19*m.b31 + m.b20*m.b23 - m.b20*m.b32 + m.b21*m.b24 - m.b21*m.b33
                        - m.b22*m.b34 - m.b23*m.b35 - m.b24*m.b36 + m.b25*m.b28 + m.b25*m.b34 - m.b25*m.b37 + m.b26*
                       m.b29 + m.b26*m.b35 - m.b26*m.b38 + m.b27*m.b30 + m.b27*m.b36 - m.b27*m.b39 + m.b28*m.b31 + m.b28
                       *m.b40 + m.b29*m.b32 + m.b29*m.b41 + m.b30*m.b33 + m.b30*m.b42 - m.b31*m.b34 - m.b31*m.b43 - 
                       m.b32*m.b35 - m.b32*m.b44 - m.b33*m.b36 - m.b33*m.b45 - m.b34*m.b46 - m.b35*m.b47 - m.b36*m.b48
                        + m.b37*m.b40 - m.b37*m.b46 + m.b38*m.b41 - m.b38*m.b47 + m.b39*m.b42 - m.b39*m.b48 - m.b40*
                       m.b43 - m.b41*m.b44 - m.b42*m.b45 + m.b43*m.b46 + m.b44*m.b47 + m.b45*m.b48, sense=minimize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 == 1)

m.c2 = Constraint(expr=   m.b4 + m.b5 + m.b6 == 1)

m.c3 = Constraint(expr=   m.b7 + m.b8 + m.b9 == 1)

m.c4 = Constraint(expr=   m.b10 + m.b11 + m.b12 == 1)

m.c5 = Constraint(expr=   m.b13 + m.b14 + m.b15 == 1)

m.c6 = Constraint(expr=   m.b16 + m.b17 + m.b18 == 1)

m.c7 = Constraint(expr=   m.b19 + m.b20 + m.b21 == 1)

m.c8 = Constraint(expr=   m.b22 + m.b23 + m.b24 == 1)

m.c9 = Constraint(expr=   m.b25 + m.b26 + m.b27 == 1)

m.c10 = Constraint(expr=   m.b28 + m.b29 + m.b30 == 1)

m.c11 = Constraint(expr=   m.b31 + m.b32 + m.b33 == 1)

m.c12 = Constraint(expr=   m.b34 + m.b35 + m.b36 == 1)

m.c13 = Constraint(expr=   m.b37 + m.b38 + m.b39 == 1)

m.c14 = Constraint(expr=   m.b40 + m.b41 + m.b42 == 1)

m.c15 = Constraint(expr=   m.b43 + m.b44 + m.b45 == 1)

m.c16 = Constraint(expr=   m.b46 + m.b47 + m.b48 == 1)

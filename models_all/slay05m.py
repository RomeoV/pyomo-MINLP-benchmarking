#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         91       11       40       40        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         71       31       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        311      301       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x2 = Var(within=Reals,bounds=(3.5,26.5),initialize=3.5)
m.x3 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(1,29),initialize=1)
m.x5 = Var(within=Reals,bounds=(2,28),initialize=2)
m.x6 = Var(within=Reals,bounds=(3,27),initialize=3)
m.x7 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x8 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x9 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x10 = Var(within=Reals,bounds=(2,28),initialize=2)
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
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x6)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x7)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x8)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x9)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x10)**2) + 300*m.x51 + 240*m.x52 + 210*m.x53 + 140*m.x54 + 100*m.x55 + 150*m.x56 + 220*m.x57
                        + 120*m.x58 + 300*m.x59 + 100*m.x60 + 300*m.x61 + 240*m.x62 + 210*m.x63 + 140*m.x64 + 100*m.x65
                        + 150*m.x66 + 220*m.x67 + 120*m.x68 + 300*m.x69 + 100*m.x70, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x51 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x52 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x53 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x54 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x3 + m.x55 >= 0)

m.c7 = Constraint(expr= - m.x2 + m.x4 + m.x56 >= 0)

m.c8 = Constraint(expr= - m.x2 + m.x5 + m.x57 >= 0)

m.c9 = Constraint(expr= - m.x3 + m.x4 + m.x58 >= 0)

m.c10 = Constraint(expr= - m.x3 + m.x5 + m.x59 >= 0)

m.c11 = Constraint(expr= - m.x4 + m.x5 + m.x60 >= 0)

m.c12 = Constraint(expr=   m.x1 - m.x2 + m.x51 >= 0)

m.c13 = Constraint(expr=   m.x1 - m.x3 + m.x52 >= 0)

m.c14 = Constraint(expr=   m.x1 - m.x4 + m.x53 >= 0)

m.c15 = Constraint(expr=   m.x1 - m.x5 + m.x54 >= 0)

m.c16 = Constraint(expr=   m.x2 - m.x3 + m.x55 >= 0)

m.c17 = Constraint(expr=   m.x2 - m.x4 + m.x56 >= 0)

m.c18 = Constraint(expr=   m.x2 - m.x5 + m.x57 >= 0)

m.c19 = Constraint(expr=   m.x3 - m.x4 + m.x58 >= 0)

m.c20 = Constraint(expr=   m.x3 - m.x5 + m.x59 >= 0)

m.c21 = Constraint(expr=   m.x4 - m.x5 + m.x60 >= 0)

m.c22 = Constraint(expr= - m.x6 + m.x7 + m.x61 >= 0)

m.c23 = Constraint(expr= - m.x6 + m.x8 + m.x62 >= 0)

m.c24 = Constraint(expr= - m.x6 + m.x9 + m.x63 >= 0)

m.c25 = Constraint(expr= - m.x6 + m.x10 + m.x64 >= 0)

m.c26 = Constraint(expr= - m.x7 + m.x8 + m.x65 >= 0)

m.c27 = Constraint(expr= - m.x7 + m.x9 + m.x66 >= 0)

m.c28 = Constraint(expr= - m.x7 + m.x10 + m.x67 >= 0)

m.c29 = Constraint(expr= - m.x8 + m.x9 + m.x68 >= 0)

m.c30 = Constraint(expr= - m.x8 + m.x10 + m.x69 >= 0)

m.c31 = Constraint(expr= - m.x9 + m.x10 + m.x70 >= 0)

m.c32 = Constraint(expr=   m.x6 - m.x7 + m.x61 >= 0)

m.c33 = Constraint(expr=   m.x6 - m.x8 + m.x62 >= 0)

m.c34 = Constraint(expr=   m.x6 - m.x9 + m.x63 >= 0)

m.c35 = Constraint(expr=   m.x6 - m.x10 + m.x64 >= 0)

m.c36 = Constraint(expr=   m.x7 - m.x8 + m.x65 >= 0)

m.c37 = Constraint(expr=   m.x7 - m.x9 + m.x66 >= 0)

m.c38 = Constraint(expr=   m.x7 - m.x10 + m.x67 >= 0)

m.c39 = Constraint(expr=   m.x8 - m.x9 + m.x68 >= 0)

m.c40 = Constraint(expr=   m.x8 - m.x10 + m.x69 >= 0)

m.c41 = Constraint(expr=   m.x9 - m.x10 + m.x70 >= 0)

m.c42 = Constraint(expr=   m.x1 - m.x2 + 30*m.b11 <= 24)

m.c43 = Constraint(expr=   m.x1 - m.x3 + 30*m.b12 <= 26)

m.c44 = Constraint(expr=   m.x1 - m.x4 + 30*m.b13 <= 26.5)

m.c45 = Constraint(expr=   m.x1 - m.x5 + 30*m.b14 <= 25.5)

m.c46 = Constraint(expr=   m.x2 - m.x3 + 30*m.b15 <= 25)

m.c47 = Constraint(expr=   m.x2 - m.x4 + 30*m.b16 <= 25.5)

m.c48 = Constraint(expr=   m.x2 - m.x5 + 30*m.b17 <= 24.5)

m.c49 = Constraint(expr=   m.x3 - m.x4 + 30*m.b18 <= 27.5)

m.c50 = Constraint(expr=   m.x3 - m.x5 + 30*m.b19 <= 26.5)

m.c51 = Constraint(expr=   m.x4 - m.x5 + 30*m.b20 <= 27)

m.c52 = Constraint(expr= - m.x1 + m.x2 + 30*m.b21 <= 24)

m.c53 = Constraint(expr= - m.x1 + m.x3 + 30*m.b22 <= 26)

m.c54 = Constraint(expr= - m.x1 + m.x4 + 30*m.b23 <= 26.5)

m.c55 = Constraint(expr= - m.x1 + m.x5 + 30*m.b24 <= 25.5)

m.c56 = Constraint(expr= - m.x2 + m.x3 + 30*m.b25 <= 25)

m.c57 = Constraint(expr= - m.x2 + m.x4 + 30*m.b26 <= 25.5)

m.c58 = Constraint(expr= - m.x2 + m.x5 + 30*m.b27 <= 24.5)

m.c59 = Constraint(expr= - m.x3 + m.x4 + 30*m.b28 <= 27.5)

m.c60 = Constraint(expr= - m.x3 + m.x5 + 30*m.b29 <= 26.5)

m.c61 = Constraint(expr= - m.x4 + m.x5 + 30*m.b30 <= 27)

m.c62 = Constraint(expr=   m.x6 - m.x7 + 30*m.b31 <= 24.5)

m.c63 = Constraint(expr=   m.x6 - m.x8 + 30*m.b32 <= 25.5)

m.c64 = Constraint(expr=   m.x6 - m.x9 + 30*m.b33 <= 25.5)

m.c65 = Constraint(expr=   m.x6 - m.x10 + 30*m.b34 <= 25)

m.c66 = Constraint(expr=   m.x7 - m.x8 + 30*m.b35 <= 26)

m.c67 = Constraint(expr=   m.x7 - m.x9 + 30*m.b36 <= 26)

m.c68 = Constraint(expr=   m.x7 - m.x10 + 30*m.b37 <= 25.5)

m.c69 = Constraint(expr=   m.x8 - m.x9 + 30*m.b38 <= 27)

m.c70 = Constraint(expr=   m.x8 - m.x10 + 30*m.b39 <= 26.5)

m.c71 = Constraint(expr=   m.x9 - m.x10 + 30*m.b40 <= 26.5)

m.c72 = Constraint(expr= - m.x6 + m.x7 + 30*m.b41 <= 24.5)

m.c73 = Constraint(expr= - m.x6 + m.x8 + 30*m.b42 <= 25.5)

m.c74 = Constraint(expr= - m.x6 + m.x9 + 30*m.b43 <= 25.5)

m.c75 = Constraint(expr= - m.x6 + m.x10 + 30*m.b44 <= 25)

m.c76 = Constraint(expr= - m.x7 + m.x8 + 30*m.b45 <= 26)

m.c77 = Constraint(expr= - m.x7 + m.x9 + 30*m.b46 <= 26)

m.c78 = Constraint(expr= - m.x7 + m.x10 + 30*m.b47 <= 25.5)

m.c79 = Constraint(expr= - m.x8 + m.x9 + 30*m.b48 <= 27)

m.c80 = Constraint(expr= - m.x8 + m.x10 + 30*m.b49 <= 26.5)

m.c81 = Constraint(expr= - m.x9 + m.x10 + 30*m.b50 <= 26.5)

m.c82 = Constraint(expr=   m.b11 + m.b21 + m.b31 + m.b41 == 1)

m.c83 = Constraint(expr=   m.b12 + m.b22 + m.b32 + m.b42 == 1)

m.c84 = Constraint(expr=   m.b13 + m.b23 + m.b33 + m.b43 == 1)

m.c85 = Constraint(expr=   m.b14 + m.b24 + m.b34 + m.b44 == 1)

m.c86 = Constraint(expr=   m.b15 + m.b25 + m.b35 + m.b45 == 1)

m.c87 = Constraint(expr=   m.b16 + m.b26 + m.b36 + m.b46 == 1)

m.c88 = Constraint(expr=   m.b17 + m.b27 + m.b37 + m.b47 == 1)

m.c89 = Constraint(expr=   m.b18 + m.b28 + m.b38 + m.b48 == 1)

m.c90 = Constraint(expr=   m.b19 + m.b29 + m.b39 + m.b49 == 1)

m.c91 = Constraint(expr=   m.b20 + m.b30 + m.b40 + m.b50 == 1)

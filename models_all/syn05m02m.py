#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        102       11       22       69        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         61       41       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        264      258        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 + 5*m.x14 + 10*m.x15 - 2*m.x24 - m.x25 + 80*m.x26 + 90*m.x27 + 285*m.x28
                        + 390*m.x29 + 290*m.x30 + 405*m.x31 - 5*m.b42 - 4*m.b43 - 8*m.b44 - 7*m.b45 - 6*m.b46 - 9*m.b47
                        - 10*m.b48 - 9*m.b49 - 6*m.b50 - 10*m.b51, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x4 - m.x6 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x5 - m.x7 == 0)

m.c4 = Constraint(expr= - m.x8 - m.x10 + m.x12 == 0)

m.c5 = Constraint(expr= - m.x9 - m.x11 + m.x13 == 0)

m.c6 = Constraint(expr=   m.x12 - m.x14 - m.x16 == 0)

m.c7 = Constraint(expr=   m.x13 - m.x15 - m.x17 == 0)

m.c8 = Constraint(expr=   m.x16 - m.x18 - m.x20 - m.x22 == 0)

m.c9 = Constraint(expr=   m.x17 - m.x19 - m.x21 - m.x23 == 0)

m.c10 = Constraint(expr=-log(1 + m.x4) + m.x8 + m.b32 <= 1)

m.c11 = Constraint(expr=-log(1 + m.x5) + m.x9 + m.b33 <= 1)

m.c12 = Constraint(expr=   m.x4 - 40*m.b32 <= 0)

m.c13 = Constraint(expr=   m.x5 - 40*m.b33 <= 0)

m.c14 = Constraint(expr=   m.x8 - 3.71357206670431*m.b32 <= 0)

m.c15 = Constraint(expr=   m.x9 - 3.71357206670431*m.b33 <= 0)

m.c16 = Constraint(expr=-1.2*log(1 + m.x6) + m.x10 + m.b34 <= 1)

m.c17 = Constraint(expr=-1.2*log(1 + m.x7) + m.x11 + m.b35 <= 1)

m.c18 = Constraint(expr=   m.x6 - 40*m.b34 <= 0)

m.c19 = Constraint(expr=   m.x7 - 40*m.b35 <= 0)

m.c20 = Constraint(expr=   m.x10 - 4.45628648004517*m.b34 <= 0)

m.c21 = Constraint(expr=   m.x11 - 4.45628648004517*m.b35 <= 0)

m.c22 = Constraint(expr= - 0.75*m.x18 + m.x26 + m.b36 <= 1)

m.c23 = Constraint(expr= - 0.75*m.x19 + m.x27 + m.b37 <= 1)

m.c24 = Constraint(expr= - 0.75*m.x18 + m.x26 - m.b36 >= -1)

m.c25 = Constraint(expr= - 0.75*m.x19 + m.x27 - m.b37 >= -1)

m.c26 = Constraint(expr=   m.x18 - 4.45628648004517*m.b36 <= 0)

m.c27 = Constraint(expr=   m.x19 - 4.45628648004517*m.b37 <= 0)

m.c28 = Constraint(expr=   m.x26 - 3.34221486003388*m.b36 <= 0)

m.c29 = Constraint(expr=   m.x27 - 3.34221486003388*m.b37 <= 0)

m.c30 = Constraint(expr=-1.5*log(1 + m.x20) + m.x28 + m.b38 <= 1)

m.c31 = Constraint(expr=-1.5*log(1 + m.x21) + m.x29 + m.b39 <= 1)

m.c32 = Constraint(expr=   m.x20 - 4.45628648004517*m.b38 <= 0)

m.c33 = Constraint(expr=   m.x21 - 4.45628648004517*m.b39 <= 0)

m.c34 = Constraint(expr=   m.x28 - 2.54515263975353*m.b38 <= 0)

m.c35 = Constraint(expr=   m.x29 - 2.54515263975353*m.b39 <= 0)

m.c36 = Constraint(expr= - m.x22 + m.x30 + m.b40 <= 1)

m.c37 = Constraint(expr= - m.x23 + m.x31 + m.b41 <= 1)

m.c38 = Constraint(expr= - m.x22 + m.x30 - m.b40 >= -1)

m.c39 = Constraint(expr= - m.x23 + m.x31 - m.b41 >= -1)

m.c40 = Constraint(expr= - 0.5*m.x24 + m.x30 + m.b40 <= 1)

m.c41 = Constraint(expr= - 0.5*m.x25 + m.x31 + m.b41 <= 1)

m.c42 = Constraint(expr= - 0.5*m.x24 + m.x30 - m.b40 >= -1)

m.c43 = Constraint(expr= - 0.5*m.x25 + m.x31 - m.b41 >= -1)

m.c44 = Constraint(expr=   m.x22 - 4.45628648004517*m.b40 <= 0)

m.c45 = Constraint(expr=   m.x23 - 4.45628648004517*m.b41 <= 0)

m.c46 = Constraint(expr=   m.x24 - 30*m.b40 <= 0)

m.c47 = Constraint(expr=   m.x25 - 30*m.b41 <= 0)

m.c48 = Constraint(expr=   m.x30 - 15*m.b40 <= 0)

m.c49 = Constraint(expr=   m.x31 - 15*m.b41 <= 0)

m.c50 = Constraint(expr=   5*m.b42 + m.x52 <= 0)

m.c51 = Constraint(expr=   4*m.b43 + m.x53 <= 0)

m.c52 = Constraint(expr=   8*m.b44 + m.x54 <= 0)

m.c53 = Constraint(expr=   7*m.b45 + m.x55 <= 0)

m.c54 = Constraint(expr=   6*m.b46 + m.x56 <= 0)

m.c55 = Constraint(expr=   9*m.b47 + m.x57 <= 0)

m.c56 = Constraint(expr=   10*m.b48 + m.x58 <= 0)

m.c57 = Constraint(expr=   9*m.b49 + m.x59 <= 0)

m.c58 = Constraint(expr=   6*m.b50 + m.x60 <= 0)

m.c59 = Constraint(expr=   10*m.b51 + m.x61 <= 0)

m.c60 = Constraint(expr=   5*m.b42 + m.x52 >= 0)

m.c61 = Constraint(expr=   4*m.b43 + m.x53 >= 0)

m.c62 = Constraint(expr=   8*m.b44 + m.x54 >= 0)

m.c63 = Constraint(expr=   7*m.b45 + m.x55 >= 0)

m.c64 = Constraint(expr=   6*m.b46 + m.x56 >= 0)

m.c65 = Constraint(expr=   9*m.b47 + m.x57 >= 0)

m.c66 = Constraint(expr=   10*m.b48 + m.x58 >= 0)

m.c67 = Constraint(expr=   9*m.b49 + m.x59 >= 0)

m.c68 = Constraint(expr=   6*m.b50 + m.x60 >= 0)

m.c69 = Constraint(expr=   10*m.b51 + m.x61 >= 0)

m.c70 = Constraint(expr=   m.b32 - m.b33 <= 0)

m.c71 = Constraint(expr=   m.b34 - m.b35 <= 0)

m.c72 = Constraint(expr=   m.b36 - m.b37 <= 0)

m.c73 = Constraint(expr=   m.b38 - m.b39 <= 0)

m.c74 = Constraint(expr=   m.b40 - m.b41 <= 0)

m.c75 = Constraint(expr=   m.b42 + m.b43 <= 1)

m.c76 = Constraint(expr=   m.b42 + m.b43 <= 1)

m.c77 = Constraint(expr=   m.b44 + m.b45 <= 1)

m.c78 = Constraint(expr=   m.b44 + m.b45 <= 1)

m.c79 = Constraint(expr=   m.b46 + m.b47 <= 1)

m.c80 = Constraint(expr=   m.b46 + m.b47 <= 1)

m.c81 = Constraint(expr=   m.b48 + m.b49 <= 1)

m.c82 = Constraint(expr=   m.b48 + m.b49 <= 1)

m.c83 = Constraint(expr=   m.b50 + m.b51 <= 1)

m.c84 = Constraint(expr=   m.b50 + m.b51 <= 1)

m.c85 = Constraint(expr=   m.b32 - m.b42 <= 0)

m.c86 = Constraint(expr= - m.b32 + m.b33 - m.b43 <= 0)

m.c87 = Constraint(expr=   m.b34 - m.b44 <= 0)

m.c88 = Constraint(expr= - m.b34 + m.b35 - m.b45 <= 0)

m.c89 = Constraint(expr=   m.b36 - m.b46 <= 0)

m.c90 = Constraint(expr= - m.b36 + m.b37 - m.b47 <= 0)

m.c91 = Constraint(expr=   m.b38 - m.b48 <= 0)

m.c92 = Constraint(expr= - m.b38 + m.b39 - m.b49 <= 0)

m.c93 = Constraint(expr=   m.b40 - m.b50 <= 0)

m.c94 = Constraint(expr= - m.b40 + m.b41 - m.b51 <= 0)

m.c95 = Constraint(expr=   m.b32 + m.b34 == 1)

m.c96 = Constraint(expr=   m.b33 + m.b35 == 1)

m.c97 = Constraint(expr=   m.b32 + m.b34 - m.b36 >= 0)

m.c98 = Constraint(expr=   m.b33 + m.b35 - m.b37 >= 0)

m.c99 = Constraint(expr=   m.b32 + m.b34 - m.b38 >= 0)

m.c100 = Constraint(expr=   m.b33 + m.b35 - m.b39 >= 0)

m.c101 = Constraint(expr=   m.b32 + m.b34 - m.b40 >= 0)

m.c102 = Constraint(expr=   m.b33 + m.b35 - m.b41 >= 0)

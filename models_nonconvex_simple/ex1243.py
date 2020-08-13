#  MINLP written by GAMS Convert at 08/13/20 17:37:58
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         97       25        0       72        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         69       53       16        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        329      293       36        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(333,443),initialize=333)
m.x2 = Var(within=Reals,bounds=(333,443),initialize=333)
m.x3 = Var(within=Reals,bounds=(333,443),initialize=333)
m.x4 = Var(within=Reals,bounds=(333,443),initialize=333)
m.x5 = Var(within=Reals,bounds=(303,423),initialize=303)
m.x6 = Var(within=Reals,bounds=(303,423),initialize=303)
m.x7 = Var(within=Reals,bounds=(303,423),initialize=303)
m.x8 = Var(within=Reals,bounds=(303,423),initialize=303)
m.x9 = Var(within=Reals,bounds=(293,408),initialize=293)
m.x10 = Var(within=Reals,bounds=(293,408),initialize=293)
m.x11 = Var(within=Reals,bounds=(293,408),initialize=293)
m.x12 = Var(within=Reals,bounds=(293,408),initialize=293)
m.x13 = Var(within=Reals,bounds=(353,413),initialize=353)
m.x14 = Var(within=Reals,bounds=(353,413),initialize=353)
m.x15 = Var(within=Reals,bounds=(353,413),initialize=353)
m.x16 = Var(within=Reals,bounds=(353,413),initialize=353)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x34 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x35 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x36 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x37 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x38 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x39 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x40 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x41 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x42 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x43 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x44 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x45 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x46 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x47 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x48 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x49 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x50 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x51 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x52 = Var(within=Reals,bounds=(1,None),initialize=1)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=208.15*m.x17/(m.x33 + m.x34) + 208.15*m.x18/(m.x34 + m.x35) + 208.15*m.x19/(m.x35 + m.x36) + 
                       208.15*m.x20/(m.x37 + m.x38) + 208.15*m.x21/(m.x38 + m.x39) + 208.15*m.x22/(m.x39 + m.x40) + 
                       208.15*m.x23/(m.x41 + m.x42) + 208.15*m.x24/(m.x42 + m.x43) + 208.15*m.x25/(m.x43 + m.x44) + 
                       208.15*m.x26/(m.x45 + m.x46) + 208.15*m.x27/(m.x46 + m.x47) + 208.15*m.x28/(m.x47 + m.x48) + 
                       208.15*m.x29/(40 + m.x49) + 208.15*m.x30/(10 + m.x50) + 166.516666666667*m.x31/(42 + m.x51) + 
                       166.516666666667*m.x32/(37 + m.x52) + 80*m.x31 + 80*m.x32 + 20*m.x29 + 20*m.x30 + 6250*m.b53
                        + 6250*m.b54 + 6250*m.b55 + 6250*m.b56 + 6250*m.b57 + 6250*m.b58 + 6250*m.b59 + 6250*m.b60
                        + 6250*m.b61 + 6250*m.b62 + 6250*m.b63 + 6250*m.b64 + 6250*m.b65 + 6250*m.b66 + 6250*m.b67
                        + 6250*m.b68, sense=minimize)

m.c2 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x29 == 3300)

m.c3 = Constraint(expr=   m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x30 == 1800)

m.c4 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x23 + m.x24 + m.x25 + m.x31 == 2300)

m.c5 = Constraint(expr=   m.x20 + m.x21 + m.x22 + m.x26 + m.x27 + m.x28 + m.x32 == 2400)

m.c6 = Constraint(expr=   30*m.x1 - 30*m.x2 - m.x17 - m.x20 == 0)

m.c7 = Constraint(expr=   30*m.x2 - 30*m.x3 - m.x18 - m.x21 == 0)

m.c8 = Constraint(expr=   30*m.x3 - 30*m.x4 - m.x19 - m.x22 == 0)

m.c9 = Constraint(expr=   15*m.x5 - 15*m.x6 - m.x23 - m.x26 == 0)

m.c10 = Constraint(expr=   15*m.x6 - 15*m.x7 - m.x24 - m.x27 == 0)

m.c11 = Constraint(expr=   15*m.x7 - 15*m.x8 - m.x25 - m.x28 == 0)

m.c12 = Constraint(expr=   20*m.x9 - 20*m.x10 - m.x17 - m.x23 == 0)

m.c13 = Constraint(expr=   20*m.x10 - 20*m.x11 - m.x18 - m.x24 == 0)

m.c14 = Constraint(expr=   20*m.x11 - 20*m.x12 - m.x19 - m.x25 == 0)

m.c15 = Constraint(expr=   40*m.x13 - 40*m.x14 - m.x20 - m.x26 == 0)

m.c16 = Constraint(expr=   40*m.x14 - 40*m.x15 - m.x21 - m.x27 == 0)

m.c17 = Constraint(expr=   40*m.x15 - 40*m.x16 - m.x22 - m.x28 == 0)

m.c18 = Constraint(expr=   m.x1 == 443)

m.c19 = Constraint(expr=   m.x5 == 423)

m.c20 = Constraint(expr=   m.x11 == 293)

m.c21 = Constraint(expr=   m.x15 == 353)

m.c22 = Constraint(expr= - m.x1 + m.x2 <= 0)

m.c23 = Constraint(expr= - m.x2 + m.x3 <= 0)

m.c24 = Constraint(expr= - m.x3 + m.x4 <= 0)

m.c25 = Constraint(expr= - m.x5 + m.x6 <= 0)

m.c26 = Constraint(expr= - m.x6 + m.x7 <= 0)

m.c27 = Constraint(expr= - m.x7 + m.x8 <= 0)

m.c28 = Constraint(expr= - m.x9 + m.x10 <= 0)

m.c29 = Constraint(expr= - m.x10 + m.x11 <= 0)

m.c30 = Constraint(expr= - m.x11 + m.x12 <= 0)

m.c31 = Constraint(expr= - m.x13 + m.x14 <= 0)

m.c32 = Constraint(expr= - m.x14 + m.x15 <= 0)

m.c33 = Constraint(expr= - m.x15 + m.x16 <= 0)

m.c34 = Constraint(expr= - m.x3 <= -333)

m.c35 = Constraint(expr= - m.x7 <= -303)

m.c36 = Constraint(expr=   m.x9 <= 408)

m.c37 = Constraint(expr=   m.x13 <= 413)

m.c38 = Constraint(expr=   30*m.x3 - m.x29 == 9990)

m.c39 = Constraint(expr=   15*m.x7 - m.x30 == 4545)

m.c40 = Constraint(expr=   20*m.x9 + m.x31 == 8160)

m.c41 = Constraint(expr=   40*m.x13 + m.x32 == 16520)

m.c42 = Constraint(expr=   m.x17 - 2300*m.b53 <= 0)

m.c43 = Constraint(expr=   m.x18 - 2300*m.b54 <= 0)

m.c44 = Constraint(expr=   m.x19 - 2300*m.b55 <= 0)

m.c45 = Constraint(expr=   m.x20 - 2400*m.b56 <= 0)

m.c46 = Constraint(expr=   m.x21 - 2400*m.b57 <= 0)

m.c47 = Constraint(expr=   m.x22 - 2400*m.b58 <= 0)

m.c48 = Constraint(expr=   m.x23 - 1800*m.b59 <= 0)

m.c49 = Constraint(expr=   m.x24 - 1800*m.b60 <= 0)

m.c50 = Constraint(expr=   m.x25 - 1800*m.b61 <= 0)

m.c51 = Constraint(expr=   m.x26 - 1800*m.b62 <= 0)

m.c52 = Constraint(expr=   m.x27 - 1800*m.b63 <= 0)

m.c53 = Constraint(expr=   m.x28 - 1800*m.b64 <= 0)

m.c54 = Constraint(expr=   m.x29 - 3300*m.b65 <= 0)

m.c55 = Constraint(expr=   m.x30 - 1800*m.b66 <= 0)

m.c56 = Constraint(expr=   m.x31 - 2300*m.b67 <= 0)

m.c57 = Constraint(expr=   m.x32 - 2400*m.b68 <= 0)

m.c58 = Constraint(expr= - m.x1 + m.x9 + m.x33 + 150*m.b53 <= 150)

m.c59 = Constraint(expr= - m.x2 + m.x10 + m.x34 + 150*m.b54 <= 150)

m.c60 = Constraint(expr= - m.x3 + m.x11 + m.x35 + 150*m.b55 <= 150)

m.c61 = Constraint(expr= - m.x1 + m.x13 + m.x37 + 90*m.b56 <= 90)

m.c62 = Constraint(expr= - m.x2 + m.x14 + m.x38 + 90*m.b57 <= 90)

m.c63 = Constraint(expr= - m.x3 + m.x15 + m.x39 + 90*m.b58 <= 90)

m.c64 = Constraint(expr= - m.x5 + m.x9 + m.x41 + 130*m.b59 <= 130)

m.c65 = Constraint(expr= - m.x6 + m.x10 + m.x42 + 130*m.b60 <= 130)

m.c66 = Constraint(expr= - m.x7 + m.x11 + m.x43 + 130*m.b61 <= 130)

m.c67 = Constraint(expr= - m.x5 + m.x13 + m.x45 + 70*m.b62 <= 70)

m.c68 = Constraint(expr= - m.x6 + m.x14 + m.x46 + 70*m.b63 <= 70)

m.c69 = Constraint(expr= - m.x7 + m.x15 + m.x47 + 70*m.b64 <= 70)

m.c70 = Constraint(expr= - m.x2 + m.x10 + m.x34 + 150*m.b53 <= 150)

m.c71 = Constraint(expr= - m.x3 + m.x11 + m.x35 + 150*m.b54 <= 150)

m.c72 = Constraint(expr= - m.x4 + m.x12 + m.x36 + 150*m.b55 <= 150)

m.c73 = Constraint(expr= - m.x2 + m.x14 + m.x38 + 90*m.b56 <= 90)

m.c74 = Constraint(expr= - m.x3 + m.x15 + m.x39 + 90*m.b57 <= 90)

m.c75 = Constraint(expr= - m.x4 + m.x16 + m.x40 + 90*m.b58 <= 90)

m.c76 = Constraint(expr= - m.x6 + m.x10 + m.x42 + 130*m.b59 <= 130)

m.c77 = Constraint(expr= - m.x7 + m.x11 + m.x43 + 130*m.b60 <= 130)

m.c78 = Constraint(expr= - m.x8 + m.x12 + m.x44 + 130*m.b61 <= 130)

m.c79 = Constraint(expr= - m.x6 + m.x14 + m.x46 + 70*m.b62 <= 70)

m.c80 = Constraint(expr= - m.x7 + m.x15 + m.x47 + 70*m.b63 <= 70)

m.c81 = Constraint(expr= - m.x8 + m.x16 + m.x48 + 70*m.b64 <= 70)

m.c82 = Constraint(expr= - m.x3 + m.x49 <= -313)

m.c83 = Constraint(expr= - m.x7 + m.x50 <= -313)

m.c84 = Constraint(expr=   m.x9 + m.x51 <= 450)

m.c85 = Constraint(expr=   m.x13 + m.x52 <= 450)

m.c86 = Constraint(expr=   m.b53 + m.b59 <= 1)

m.c87 = Constraint(expr=   m.b54 + m.b60 <= 1)

m.c88 = Constraint(expr=   m.b55 + m.b61 <= 1)

m.c89 = Constraint(expr=   m.b56 + m.b62 <= 1)

m.c90 = Constraint(expr=   m.b57 + m.b63 <= 1)

m.c91 = Constraint(expr=   m.b58 + m.b64 <= 1)

m.c92 = Constraint(expr=   m.b53 + m.b56 <= 1)

m.c93 = Constraint(expr=   m.b54 + m.b57 <= 1)

m.c94 = Constraint(expr=   m.b55 + m.b58 <= 1)

m.c95 = Constraint(expr=   m.b59 + m.b62 <= 1)

m.c96 = Constraint(expr=   m.b60 + m.b63 <= 1)

m.c97 = Constraint(expr=   m.b61 + m.b64 <= 1)

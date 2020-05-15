#  MINLP written by GAMS Convert at 05/15/20 00:50:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        212        1        0      211        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        115       73       42        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        869      855       14        0
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
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x87 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x88 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x89 = Var(within=Reals,bounds=(3,8.5399),initialize=3)
m.x90 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x91 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x92 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x93 = Var(within=Reals,bounds=(8.54,8.54),initialize=8.54)
m.x94 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x95 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x96 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x97 = Var(within=Reals,bounds=(4.2155,12),initialize=4.2155)
m.x98 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x99 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x100 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x101 = Var(within=Reals,bounds=(13,13),initialize=13)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x44 + m.x45 + m.x56 + m.x57 + m.x66 + m.x67 + m.x74 + m.x75 + m.x80 + m.x81 + m.x84 + m.x85
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x102 - m.x103 <= 0)

m.c3 = Constraint(expr=   0.5*m.x86 - m.x93 + m.x102 <= 0)

m.c4 = Constraint(expr=   0.5*m.x86 - m.x102 <= 0)

m.c5 = Constraint(expr=   0.5*m.x94 - m.x101 + m.x109 <= 0)

m.c6 = Constraint(expr=   0.5*m.x94 - m.x109 <= 0)

m.c7 = Constraint(expr=   0.5*m.x87 - m.x93 + m.x103 <= 0)

m.c8 = Constraint(expr=   0.5*m.x87 - m.x103 <= 0)

m.c9 = Constraint(expr=   0.5*m.x95 - m.x101 + m.x110 <= 0)

m.c10 = Constraint(expr=   0.5*m.x95 - m.x110 <= 0)

m.c11 = Constraint(expr=   0.5*m.x88 - m.x93 + m.x104 <= 0)

m.c12 = Constraint(expr=   0.5*m.x88 - m.x104 <= 0)

m.c13 = Constraint(expr=   0.5*m.x96 - m.x101 + m.x111 <= 0)

m.c14 = Constraint(expr=   0.5*m.x96 - m.x111 <= 0)

m.c15 = Constraint(expr=   0.5*m.x89 - m.x93 + m.x105 <= 0)

m.c16 = Constraint(expr=   0.5*m.x89 - m.x105 <= 0)

m.c17 = Constraint(expr=   0.5*m.x97 - m.x101 + m.x112 <= 0)

m.c18 = Constraint(expr=   0.5*m.x97 - m.x112 <= 0)

m.c19 = Constraint(expr=   0.5*m.x90 - m.x93 + m.x106 <= 0)

m.c20 = Constraint(expr=   0.5*m.x90 - m.x106 <= 0)

m.c21 = Constraint(expr=   0.5*m.x98 - m.x101 + m.x113 <= 0)

m.c22 = Constraint(expr=   0.5*m.x98 - m.x113 <= 0)

m.c23 = Constraint(expr=   0.5*m.x91 - m.x93 + m.x107 <= 0)

m.c24 = Constraint(expr=   0.5*m.x91 - m.x107 <= 0)

m.c25 = Constraint(expr=   0.5*m.x99 - m.x101 + m.x114 <= 0)

m.c26 = Constraint(expr=   0.5*m.x99 - m.x114 <= 0)

m.c27 = Constraint(expr=   0.5*m.x92 - m.x93 + m.x108 <= 0)

m.c28 = Constraint(expr=   0.5*m.x92 - m.x108 <= 0)

m.c29 = Constraint(expr=   0.5*m.x100 - m.x101 + m.x115 <= 0)

m.c30 = Constraint(expr=   0.5*m.x100 - m.x115 <= 0)

m.c31 = Constraint(expr= - m.x44 + m.x102 - m.x103 <= 0)

m.c32 = Constraint(expr= - m.x44 - m.x102 + m.x103 <= 0)

m.c33 = Constraint(expr= - m.x45 + m.x109 - m.x110 <= 0)

m.c34 = Constraint(expr= - m.x45 - m.x109 + m.x110 <= 0)

m.c35 = Constraint(expr= - 8.54*m.b1 - 8.54*m.b2 + 0.5*m.x86 + 0.5*m.x87 - m.x102 + m.x103 <= 0)

m.c36 = Constraint(expr= - 8.54*m.b1 + 8.54*m.b2 + 0.5*m.x86 + 0.5*m.x87 + m.x102 - m.x103 <= 8.54)

m.c37 = Constraint(expr=   13*m.b1 - 13*m.b2 + 0.5*m.x94 + 0.5*m.x95 - m.x109 + m.x110 <= 13)

m.c38 = Constraint(expr=   13*m.b1 + 13*m.b2 + 0.5*m.x94 + 0.5*m.x95 + m.x109 - m.x110 <= 26)

m.c39 = Constraint(expr= - m.x46 + m.x102 - m.x104 <= 0)

m.c40 = Constraint(expr= - m.x46 - m.x102 + m.x104 <= 0)

m.c41 = Constraint(expr= - m.x47 + m.x109 - m.x111 <= 0)

m.c42 = Constraint(expr= - m.x47 - m.x109 + m.x111 <= 0)

m.c43 = Constraint(expr= - 8.54*m.b3 - 8.54*m.b4 + 0.5*m.x86 + 0.5*m.x88 - m.x102 + m.x104 <= 0)

m.c44 = Constraint(expr= - 8.54*m.b3 + 8.54*m.b4 + 0.5*m.x86 + 0.5*m.x88 + m.x102 - m.x104 <= 8.54)

m.c45 = Constraint(expr=   13*m.b3 - 13*m.b4 + 0.5*m.x94 + 0.5*m.x96 - m.x109 + m.x111 <= 13)

m.c46 = Constraint(expr=   13*m.b3 + 13*m.b4 + 0.5*m.x94 + 0.5*m.x96 + m.x109 - m.x111 <= 26)

m.c47 = Constraint(expr= - m.x48 + m.x102 - m.x105 <= 0)

m.c48 = Constraint(expr= - m.x48 - m.x102 + m.x105 <= 0)

m.c49 = Constraint(expr= - m.x49 + m.x109 - m.x112 <= 0)

m.c50 = Constraint(expr= - m.x49 - m.x109 + m.x112 <= 0)

m.c51 = Constraint(expr= - 8.54*m.b5 - 8.54*m.b6 + 0.5*m.x86 + 0.5*m.x89 - m.x102 + m.x105 <= 0)

m.c52 = Constraint(expr= - 8.54*m.b5 + 8.54*m.b6 + 0.5*m.x86 + 0.5*m.x89 + m.x102 - m.x105 <= 8.54)

m.c53 = Constraint(expr=   13*m.b5 - 13*m.b6 + 0.5*m.x94 + 0.5*m.x97 - m.x109 + m.x112 <= 13)

m.c54 = Constraint(expr=   13*m.b5 + 13*m.b6 + 0.5*m.x94 + 0.5*m.x97 + m.x109 - m.x112 <= 26)

m.c55 = Constraint(expr= - m.x50 + m.x102 - m.x106 <= 0)

m.c56 = Constraint(expr= - m.x50 - m.x102 + m.x106 <= 0)

m.c57 = Constraint(expr= - m.x51 + m.x109 - m.x113 <= 0)

m.c58 = Constraint(expr= - m.x51 - m.x109 + m.x113 <= 0)

m.c59 = Constraint(expr= - 8.54*m.b7 - 8.54*m.b8 + 0.5*m.x86 + 0.5*m.x90 - m.x102 + m.x106 <= 0)

m.c60 = Constraint(expr= - 8.54*m.b7 + 8.54*m.b8 + 0.5*m.x86 + 0.5*m.x90 + m.x102 - m.x106 <= 8.54)

m.c61 = Constraint(expr=   13*m.b7 - 13*m.b8 + 0.5*m.x94 + 0.5*m.x98 - m.x109 + m.x113 <= 13)

m.c62 = Constraint(expr=   13*m.b7 + 13*m.b8 + 0.5*m.x94 + 0.5*m.x98 + m.x109 - m.x113 <= 26)

m.c63 = Constraint(expr= - m.x52 + m.x102 - m.x107 <= 0)

m.c64 = Constraint(expr= - m.x52 - m.x102 + m.x107 <= 0)

m.c65 = Constraint(expr= - m.x53 + m.x109 - m.x114 <= 0)

m.c66 = Constraint(expr= - m.x53 - m.x109 + m.x114 <= 0)

m.c67 = Constraint(expr= - 8.54*m.b9 - 8.54*m.b10 + 0.5*m.x86 + 0.5*m.x91 - m.x102 + m.x107 <= 0)

m.c68 = Constraint(expr= - 8.54*m.b9 + 8.54*m.b10 + 0.5*m.x86 + 0.5*m.x91 + m.x102 - m.x107 <= 8.54)

m.c69 = Constraint(expr=   13*m.b9 - 13*m.b10 + 0.5*m.x94 + 0.5*m.x99 - m.x109 + m.x114 <= 13)

m.c70 = Constraint(expr=   13*m.b9 + 13*m.b10 + 0.5*m.x94 + 0.5*m.x99 + m.x109 - m.x114 <= 26)

m.c71 = Constraint(expr= - m.x54 + m.x102 - m.x108 <= 0)

m.c72 = Constraint(expr= - m.x54 - m.x102 + m.x108 <= 0)

m.c73 = Constraint(expr= - m.x55 + m.x109 - m.x115 <= 0)

m.c74 = Constraint(expr= - m.x55 - m.x109 + m.x115 <= 0)

m.c75 = Constraint(expr= - 8.54*m.b11 - 8.54*m.b12 + 0.5*m.x86 + 0.5*m.x92 - m.x102 + m.x108 <= 0)

m.c76 = Constraint(expr= - 8.54*m.b11 + 8.54*m.b12 + 0.5*m.x86 + 0.5*m.x92 + m.x102 - m.x108 <= 8.54)

m.c77 = Constraint(expr=   13*m.b11 - 13*m.b12 + 0.5*m.x94 + 0.5*m.x100 - m.x109 + m.x115 <= 13)

m.c78 = Constraint(expr=   13*m.b11 + 13*m.b12 + 0.5*m.x94 + 0.5*m.x100 + m.x109 - m.x115 <= 26)

m.c79 = Constraint(expr= - m.x56 + m.x103 - m.x104 <= 0)

m.c80 = Constraint(expr= - m.x56 - m.x103 + m.x104 <= 0)

m.c81 = Constraint(expr= - m.x57 + m.x110 - m.x111 <= 0)

m.c82 = Constraint(expr= - m.x57 - m.x110 + m.x111 <= 0)

m.c83 = Constraint(expr= - 8.54*m.b13 - 8.54*m.b14 + 0.5*m.x87 + 0.5*m.x88 - m.x103 + m.x104 <= 0)

m.c84 = Constraint(expr= - 8.54*m.b13 + 8.54*m.b14 + 0.5*m.x87 + 0.5*m.x88 + m.x103 - m.x104 <= 8.54)

m.c85 = Constraint(expr=   13*m.b13 - 13*m.b14 + 0.5*m.x95 + 0.5*m.x96 - m.x110 + m.x111 <= 13)

m.c86 = Constraint(expr=   13*m.b13 + 13*m.b14 + 0.5*m.x95 + 0.5*m.x96 + m.x110 - m.x111 <= 26)

m.c87 = Constraint(expr= - m.x58 + m.x103 - m.x105 <= 0)

m.c88 = Constraint(expr= - m.x58 - m.x103 + m.x105 <= 0)

m.c89 = Constraint(expr= - m.x59 + m.x110 - m.x112 <= 0)

m.c90 = Constraint(expr= - m.x59 - m.x110 + m.x112 <= 0)

m.c91 = Constraint(expr= - 8.54*m.b15 - 8.54*m.b16 + 0.5*m.x87 + 0.5*m.x89 - m.x103 + m.x105 <= 0)

m.c92 = Constraint(expr= - 8.54*m.b15 + 8.54*m.b16 + 0.5*m.x87 + 0.5*m.x89 + m.x103 - m.x105 <= 8.54)

m.c93 = Constraint(expr=   13*m.b15 - 13*m.b16 + 0.5*m.x95 + 0.5*m.x97 - m.x110 + m.x112 <= 13)

m.c94 = Constraint(expr=   13*m.b15 + 13*m.b16 + 0.5*m.x95 + 0.5*m.x97 + m.x110 - m.x112 <= 26)

m.c95 = Constraint(expr= - m.x60 + m.x103 - m.x106 <= 0)

m.c96 = Constraint(expr= - m.x60 - m.x103 + m.x106 <= 0)

m.c97 = Constraint(expr= - m.x61 + m.x110 - m.x113 <= 0)

m.c98 = Constraint(expr= - m.x61 - m.x110 + m.x113 <= 0)

m.c99 = Constraint(expr= - 8.54*m.b17 - 8.54*m.b18 + 0.5*m.x87 + 0.5*m.x90 - m.x103 + m.x106 <= 0)

m.c100 = Constraint(expr= - 8.54*m.b17 + 8.54*m.b18 + 0.5*m.x87 + 0.5*m.x90 + m.x103 - m.x106 <= 8.54)

m.c101 = Constraint(expr=   13*m.b17 - 13*m.b18 + 0.5*m.x95 + 0.5*m.x98 - m.x110 + m.x113 <= 13)

m.c102 = Constraint(expr=   13*m.b17 + 13*m.b18 + 0.5*m.x95 + 0.5*m.x98 + m.x110 - m.x113 <= 26)

m.c103 = Constraint(expr= - m.x62 + m.x103 - m.x107 <= 0)

m.c104 = Constraint(expr= - m.x62 - m.x103 + m.x107 <= 0)

m.c105 = Constraint(expr= - m.x63 + m.x110 - m.x114 <= 0)

m.c106 = Constraint(expr= - m.x63 - m.x110 + m.x114 <= 0)

m.c107 = Constraint(expr= - 8.54*m.b19 - 8.54*m.b20 + 0.5*m.x87 + 0.5*m.x91 - m.x103 + m.x107 <= 0)

m.c108 = Constraint(expr= - 8.54*m.b19 + 8.54*m.b20 + 0.5*m.x87 + 0.5*m.x91 + m.x103 - m.x107 <= 8.54)

m.c109 = Constraint(expr=   13*m.b19 - 13*m.b20 + 0.5*m.x95 + 0.5*m.x99 - m.x110 + m.x114 <= 13)

m.c110 = Constraint(expr=   13*m.b19 + 13*m.b20 + 0.5*m.x95 + 0.5*m.x99 + m.x110 - m.x114 <= 26)

m.c111 = Constraint(expr= - m.x64 + m.x103 - m.x108 <= 0)

m.c112 = Constraint(expr= - m.x64 - m.x103 + m.x108 <= 0)

m.c113 = Constraint(expr= - m.x65 + m.x110 - m.x115 <= 0)

m.c114 = Constraint(expr= - m.x65 - m.x110 + m.x115 <= 0)

m.c115 = Constraint(expr= - 8.54*m.b21 - 8.54*m.b22 + 0.5*m.x87 + 0.5*m.x92 - m.x103 + m.x108 <= 0)

m.c116 = Constraint(expr= - 8.54*m.b21 + 8.54*m.b22 + 0.5*m.x87 + 0.5*m.x92 + m.x103 - m.x108 <= 8.54)

m.c117 = Constraint(expr=   13*m.b21 - 13*m.b22 + 0.5*m.x95 + 0.5*m.x100 - m.x110 + m.x115 <= 13)

m.c118 = Constraint(expr=   13*m.b21 + 13*m.b22 + 0.5*m.x95 + 0.5*m.x100 + m.x110 - m.x115 <= 26)

m.c119 = Constraint(expr= - m.x66 + m.x104 - m.x105 <= 0)

m.c120 = Constraint(expr= - m.x66 - m.x104 + m.x105 <= 0)

m.c121 = Constraint(expr= - m.x67 + m.x111 - m.x112 <= 0)

m.c122 = Constraint(expr= - m.x67 - m.x111 + m.x112 <= 0)

m.c123 = Constraint(expr= - 8.54*m.b23 - 8.54*m.b24 + 0.5*m.x88 + 0.5*m.x89 - m.x104 + m.x105 <= 0)

m.c124 = Constraint(expr= - 8.54*m.b23 + 8.54*m.b24 + 0.5*m.x88 + 0.5*m.x89 + m.x104 - m.x105 <= 8.54)

m.c125 = Constraint(expr=   13*m.b23 - 13*m.b24 + 0.5*m.x96 + 0.5*m.x97 - m.x111 + m.x112 <= 13)

m.c126 = Constraint(expr=   13*m.b23 + 13*m.b24 + 0.5*m.x96 + 0.5*m.x97 + m.x111 - m.x112 <= 26)

m.c127 = Constraint(expr= - m.x68 + m.x104 - m.x106 <= 0)

m.c128 = Constraint(expr= - m.x68 - m.x104 + m.x106 <= 0)

m.c129 = Constraint(expr= - m.x69 + m.x111 - m.x113 <= 0)

m.c130 = Constraint(expr= - m.x69 - m.x111 + m.x113 <= 0)

m.c131 = Constraint(expr= - 8.54*m.b25 - 8.54*m.b26 + 0.5*m.x88 + 0.5*m.x90 - m.x104 + m.x106 <= 0)

m.c132 = Constraint(expr= - 8.54*m.b25 + 8.54*m.b26 + 0.5*m.x88 + 0.5*m.x90 + m.x104 - m.x106 <= 8.54)

m.c133 = Constraint(expr=   13*m.b25 - 13*m.b26 + 0.5*m.x96 + 0.5*m.x98 - m.x111 + m.x113 <= 13)

m.c134 = Constraint(expr=   13*m.b25 + 13*m.b26 + 0.5*m.x96 + 0.5*m.x98 + m.x111 - m.x113 <= 26)

m.c135 = Constraint(expr= - m.x70 + m.x104 - m.x107 <= 0)

m.c136 = Constraint(expr= - m.x70 - m.x104 + m.x107 <= 0)

m.c137 = Constraint(expr= - m.x71 + m.x111 - m.x114 <= 0)

m.c138 = Constraint(expr= - m.x71 - m.x111 + m.x114 <= 0)

m.c139 = Constraint(expr= - 8.54*m.b27 - 8.54*m.b28 + 0.5*m.x88 + 0.5*m.x91 - m.x104 + m.x107 <= 0)

m.c140 = Constraint(expr= - 8.54*m.b27 + 8.54*m.b28 + 0.5*m.x88 + 0.5*m.x91 + m.x104 - m.x107 <= 8.54)

m.c141 = Constraint(expr=   13*m.b27 - 13*m.b28 + 0.5*m.x96 + 0.5*m.x99 - m.x111 + m.x114 <= 13)

m.c142 = Constraint(expr=   13*m.b27 + 13*m.b28 + 0.5*m.x96 + 0.5*m.x99 + m.x111 - m.x114 <= 26)

m.c143 = Constraint(expr= - m.x72 + m.x104 - m.x108 <= 0)

m.c144 = Constraint(expr= - m.x72 - m.x104 + m.x108 <= 0)

m.c145 = Constraint(expr= - m.x73 + m.x111 - m.x115 <= 0)

m.c146 = Constraint(expr= - m.x73 - m.x111 + m.x115 <= 0)

m.c147 = Constraint(expr= - 8.54*m.b29 - 8.54*m.b30 + 0.5*m.x88 + 0.5*m.x92 - m.x104 + m.x108 <= 0)

m.c148 = Constraint(expr= - 8.54*m.b29 + 8.54*m.b30 + 0.5*m.x88 + 0.5*m.x92 + m.x104 - m.x108 <= 8.54)

m.c149 = Constraint(expr=   13*m.b29 - 13*m.b30 + 0.5*m.x96 + 0.5*m.x100 - m.x111 + m.x115 <= 13)

m.c150 = Constraint(expr=   13*m.b29 + 13*m.b30 + 0.5*m.x96 + 0.5*m.x100 + m.x111 - m.x115 <= 26)

m.c151 = Constraint(expr= - m.x74 + m.x105 - m.x106 <= 0)

m.c152 = Constraint(expr= - m.x74 - m.x105 + m.x106 <= 0)

m.c153 = Constraint(expr= - m.x75 + m.x112 - m.x113 <= 0)

m.c154 = Constraint(expr= - m.x75 - m.x112 + m.x113 <= 0)

m.c155 = Constraint(expr= - 8.54*m.b31 - 8.54*m.b32 + 0.5*m.x89 + 0.5*m.x90 - m.x105 + m.x106 <= 0)

m.c156 = Constraint(expr= - 8.54*m.b31 + 8.54*m.b32 + 0.5*m.x89 + 0.5*m.x90 + m.x105 - m.x106 <= 8.54)

m.c157 = Constraint(expr=   13*m.b31 - 13*m.b32 + 0.5*m.x97 + 0.5*m.x98 - m.x112 + m.x113 <= 13)

m.c158 = Constraint(expr=   13*m.b31 + 13*m.b32 + 0.5*m.x97 + 0.5*m.x98 + m.x112 - m.x113 <= 26)

m.c159 = Constraint(expr= - m.x76 + m.x105 - m.x107 <= 0)

m.c160 = Constraint(expr= - m.x76 - m.x105 + m.x107 <= 0)

m.c161 = Constraint(expr= - m.x77 + m.x112 - m.x114 <= 0)

m.c162 = Constraint(expr= - m.x77 - m.x112 + m.x114 <= 0)

m.c163 = Constraint(expr= - 8.54*m.b33 - 8.54*m.b34 + 0.5*m.x89 + 0.5*m.x91 - m.x105 + m.x107 <= 0)

m.c164 = Constraint(expr= - 8.54*m.b33 + 8.54*m.b34 + 0.5*m.x89 + 0.5*m.x91 + m.x105 - m.x107 <= 8.54)

m.c165 = Constraint(expr=   13*m.b33 - 13*m.b34 + 0.5*m.x97 + 0.5*m.x99 - m.x112 + m.x114 <= 13)

m.c166 = Constraint(expr=   13*m.b33 + 13*m.b34 + 0.5*m.x97 + 0.5*m.x99 + m.x112 - m.x114 <= 26)

m.c167 = Constraint(expr= - m.x78 + m.x105 - m.x108 <= 0)

m.c168 = Constraint(expr= - m.x78 - m.x105 + m.x108 <= 0)

m.c169 = Constraint(expr= - m.x79 + m.x112 - m.x115 <= 0)

m.c170 = Constraint(expr= - m.x79 - m.x112 + m.x115 <= 0)

m.c171 = Constraint(expr= - 8.54*m.b35 - 8.54*m.b36 + 0.5*m.x89 + 0.5*m.x92 - m.x105 + m.x108 <= 0)

m.c172 = Constraint(expr= - 8.54*m.b35 + 8.54*m.b36 + 0.5*m.x89 + 0.5*m.x92 + m.x105 - m.x108 <= 8.54)

m.c173 = Constraint(expr=   13*m.b35 - 13*m.b36 + 0.5*m.x97 + 0.5*m.x100 - m.x112 + m.x115 <= 13)

m.c174 = Constraint(expr=   13*m.b35 + 13*m.b36 + 0.5*m.x97 + 0.5*m.x100 + m.x112 - m.x115 <= 26)

m.c175 = Constraint(expr= - m.x80 + m.x106 - m.x107 <= 0)

m.c176 = Constraint(expr= - m.x80 - m.x106 + m.x107 <= 0)

m.c177 = Constraint(expr= - m.x81 + m.x113 - m.x114 <= 0)

m.c178 = Constraint(expr= - m.x81 - m.x113 + m.x114 <= 0)

m.c179 = Constraint(expr= - 8.54*m.b37 - 8.54*m.b38 + 0.5*m.x90 + 0.5*m.x91 - m.x106 + m.x107 <= 0)

m.c180 = Constraint(expr= - 8.54*m.b37 + 8.54*m.b38 + 0.5*m.x90 + 0.5*m.x91 + m.x106 - m.x107 <= 8.54)

m.c181 = Constraint(expr=   13*m.b37 - 13*m.b38 + 0.5*m.x98 + 0.5*m.x99 - m.x113 + m.x114 <= 13)

m.c182 = Constraint(expr=   13*m.b37 + 13*m.b38 + 0.5*m.x98 + 0.5*m.x99 + m.x113 - m.x114 <= 26)

m.c183 = Constraint(expr= - m.x82 + m.x106 - m.x108 <= 0)

m.c184 = Constraint(expr= - m.x82 - m.x106 + m.x108 <= 0)

m.c185 = Constraint(expr= - m.x83 + m.x113 - m.x115 <= 0)

m.c186 = Constraint(expr= - m.x83 - m.x113 + m.x115 <= 0)

m.c187 = Constraint(expr= - 8.54*m.b39 - 8.54*m.b40 + 0.5*m.x90 + 0.5*m.x92 - m.x106 + m.x108 <= 0)

m.c188 = Constraint(expr= - 8.54*m.b39 + 8.54*m.b40 + 0.5*m.x90 + 0.5*m.x92 + m.x106 - m.x108 <= 8.54)

m.c189 = Constraint(expr=   13*m.b39 - 13*m.b40 + 0.5*m.x98 + 0.5*m.x100 - m.x113 + m.x115 <= 13)

m.c190 = Constraint(expr=   13*m.b39 + 13*m.b40 + 0.5*m.x98 + 0.5*m.x100 + m.x113 - m.x115 <= 26)

m.c191 = Constraint(expr= - m.x84 + m.x107 - m.x108 <= 0)

m.c192 = Constraint(expr= - m.x84 - m.x107 + m.x108 <= 0)

m.c193 = Constraint(expr= - m.x85 + m.x114 - m.x115 <= 0)

m.c194 = Constraint(expr= - m.x85 - m.x114 + m.x115 <= 0)

m.c195 = Constraint(expr= - 8.54*m.b41 - 8.54*m.b42 + 0.5*m.x91 + 0.5*m.x92 - m.x107 + m.x108 <= 0)

m.c196 = Constraint(expr= - 8.54*m.b41 + 8.54*m.b42 + 0.5*m.x91 + 0.5*m.x92 + m.x107 - m.x108 <= 8.54)

m.c197 = Constraint(expr=   13*m.b41 - 13*m.b42 + 0.5*m.x99 + 0.5*m.x100 - m.x114 + m.x115 <= 13)

m.c198 = Constraint(expr=   13*m.b41 + 13*m.b42 + 0.5*m.x99 + 0.5*m.x100 + m.x114 - m.x115 <= 26)

m.c199 = Constraint(expr=16/m.x86 - m.x94 <= 0)

m.c200 = Constraint(expr=16/m.x94 - m.x86 <= 0)

m.c201 = Constraint(expr=16/m.x87 - m.x95 <= 0)

m.c202 = Constraint(expr=16/m.x95 - m.x87 <= 0)

m.c203 = Constraint(expr=16/m.x88 - m.x96 <= 0)

m.c204 = Constraint(expr=16/m.x96 - m.x88 <= 0)

m.c205 = Constraint(expr=36/m.x89 - m.x97 <= 0)

m.c206 = Constraint(expr=36/m.x97 - m.x89 <= 0)

m.c207 = Constraint(expr=9/m.x90 - m.x98 <= 0)

m.c208 = Constraint(expr=9/m.x98 - m.x90 <= 0)

m.c209 = Constraint(expr=9/m.x91 - m.x99 <= 0)

m.c210 = Constraint(expr=9/m.x99 - m.x91 <= 0)

m.c211 = Constraint(expr=9/m.x92 - m.x100 <= 0)

m.c212 = Constraint(expr=9/m.x100 - m.x92 <= 0)

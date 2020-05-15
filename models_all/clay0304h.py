#  MINLP written by GAMS Convert at 05/15/20 00:50:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        259       43       24      192        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        177      141       36        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        729      585      144        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(11.5,52.5),initialize=11.5)
m.x2 = Var(within=Reals,bounds=(12.5,51.5),initialize=12.5)
m.x3 = Var(within=Reals,bounds=(10.5,53.5),initialize=10.5)
m.x4 = Var(within=Reals,bounds=(10,54),initialize=10)
m.x5 = Var(within=Reals,bounds=(7,82),initialize=7)
m.x6 = Var(within=Reals,bounds=(6.5,82.5),initialize=6.5)
m.x7 = Var(within=Reals,bounds=(5.5,83.5),initialize=5.5)
m.x8 = Var(within=Reals,bounds=(5.5,83.5),initialize=5.5)
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
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   300*m.x165 + 240*m.x166 + 210*m.x167 + 100*m.x168 + 150*m.x169 + 120*m.x170 + 300*m.x171
                        + 240*m.x172 + 210*m.x173 + 100*m.x174 + 150*m.x175 + 120*m.x176, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x165 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x166 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x167 >= 0)

m.c5 = Constraint(expr= - m.x2 + m.x3 + m.x168 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x4 + m.x169 >= 0)

m.c7 = Constraint(expr= - m.x3 + m.x4 + m.x170 >= 0)

m.c8 = Constraint(expr=   m.x1 - m.x2 + m.x165 >= 0)

m.c9 = Constraint(expr=   m.x1 - m.x3 + m.x166 >= 0)

m.c10 = Constraint(expr=   m.x1 - m.x4 + m.x167 >= 0)

m.c11 = Constraint(expr=   m.x2 - m.x3 + m.x168 >= 0)

m.c12 = Constraint(expr=   m.x2 - m.x4 + m.x169 >= 0)

m.c13 = Constraint(expr=   m.x3 - m.x4 + m.x170 >= 0)

m.c14 = Constraint(expr= - m.x5 + m.x6 + m.x171 >= 0)

m.c15 = Constraint(expr= - m.x5 + m.x7 + m.x172 >= 0)

m.c16 = Constraint(expr= - m.x5 + m.x8 + m.x173 >= 0)

m.c17 = Constraint(expr= - m.x6 + m.x7 + m.x174 >= 0)

m.c18 = Constraint(expr= - m.x6 + m.x8 + m.x175 >= 0)

m.c19 = Constraint(expr= - m.x7 + m.x8 + m.x176 >= 0)

m.c20 = Constraint(expr=   m.x5 - m.x6 + m.x171 >= 0)

m.c21 = Constraint(expr=   m.x5 - m.x7 + m.x172 >= 0)

m.c22 = Constraint(expr=   m.x5 - m.x8 + m.x173 >= 0)

m.c23 = Constraint(expr=   m.x6 - m.x7 + m.x174 >= 0)

m.c24 = Constraint(expr=   m.x6 - m.x8 + m.x175 >= 0)

m.c25 = Constraint(expr=   m.x7 - m.x8 + m.x176 >= 0)

m.c26 = Constraint(expr=   m.x1 - m.x9 - m.x12 - m.x15 - m.x18 == 0)

m.c27 = Constraint(expr=   m.x1 - m.x10 - m.x13 - m.x16 - m.x19 == 0)

m.c28 = Constraint(expr=   m.x1 - m.x11 - m.x14 - m.x17 - m.x20 == 0)

m.c29 = Constraint(expr=   m.x2 - m.x21 - m.x24 - m.x27 - m.x30 == 0)

m.c30 = Constraint(expr=   m.x2 - m.x22 - m.x25 - m.x28 - m.x31 == 0)

m.c31 = Constraint(expr=   m.x2 - m.x23 - m.x26 - m.x29 - m.x32 == 0)

m.c32 = Constraint(expr=   m.x3 - m.x33 - m.x36 - m.x39 - m.x42 == 0)

m.c33 = Constraint(expr=   m.x3 - m.x34 - m.x37 - m.x40 - m.x43 == 0)

m.c34 = Constraint(expr=   m.x3 - m.x35 - m.x38 - m.x41 - m.x44 == 0)

m.c35 = Constraint(expr=   m.x4 - m.x45 - m.x48 - m.x51 - m.x54 == 0)

m.c36 = Constraint(expr=   m.x4 - m.x46 - m.x49 - m.x52 - m.x55 == 0)

m.c37 = Constraint(expr=   m.x4 - m.x47 - m.x50 - m.x53 - m.x56 == 0)

m.c38 = Constraint(expr=   m.x5 - m.x57 - m.x60 - m.x63 - m.x66 == 0)

m.c39 = Constraint(expr=   m.x5 - m.x58 - m.x61 - m.x64 - m.x67 == 0)

m.c40 = Constraint(expr=   m.x5 - m.x59 - m.x62 - m.x65 - m.x68 == 0)

m.c41 = Constraint(expr=   m.x6 - m.x69 - m.x72 - m.x75 - m.x78 == 0)

m.c42 = Constraint(expr=   m.x6 - m.x70 - m.x73 - m.x76 - m.x79 == 0)

m.c43 = Constraint(expr=   m.x6 - m.x71 - m.x74 - m.x77 - m.x80 == 0)

m.c44 = Constraint(expr=   m.x7 - m.x81 - m.x84 - m.x87 - m.x90 == 0)

m.c45 = Constraint(expr=   m.x7 - m.x82 - m.x85 - m.x88 - m.x91 == 0)

m.c46 = Constraint(expr=   m.x7 - m.x83 - m.x86 - m.x89 - m.x92 == 0)

m.c47 = Constraint(expr=   m.x8 - m.x93 - m.x96 - m.x99 - m.x102 == 0)

m.c48 = Constraint(expr=   m.x8 - m.x94 - m.x97 - m.x100 - m.x103 == 0)

m.c49 = Constraint(expr=   m.x8 - m.x95 - m.x98 - m.x101 - m.x104 == 0)

m.c50 = Constraint(expr=   m.x9 - 52.5*m.b129 <= 0)

m.c51 = Constraint(expr=   m.x10 - 52.5*m.b130 <= 0)

m.c52 = Constraint(expr=   m.x11 - 52.5*m.b131 <= 0)

m.c53 = Constraint(expr=   m.x12 - 52.5*m.b135 <= 0)

m.c54 = Constraint(expr=   m.x13 - 52.5*m.b136 <= 0)

m.c55 = Constraint(expr=   m.x14 - 52.5*m.b137 <= 0)

m.c56 = Constraint(expr=   m.x15 - 52.5*m.b141 <= 0)

m.c57 = Constraint(expr=   m.x16 - 52.5*m.b142 <= 0)

m.c58 = Constraint(expr=   m.x17 - 52.5*m.b143 <= 0)

m.c59 = Constraint(expr=   m.x18 - 52.5*m.b147 <= 0)

m.c60 = Constraint(expr=   m.x19 - 52.5*m.b148 <= 0)

m.c61 = Constraint(expr=   m.x20 - 52.5*m.b149 <= 0)

m.c62 = Constraint(expr=   m.x21 - 52.5*m.b129 <= 0)

m.c63 = Constraint(expr=   m.x22 - 51.5*m.b132 <= 0)

m.c64 = Constraint(expr=   m.x23 - 51.5*m.b133 <= 0)

m.c65 = Constraint(expr=   m.x24 - 52.5*m.b135 <= 0)

m.c66 = Constraint(expr=   m.x25 - 51.5*m.b138 <= 0)

m.c67 = Constraint(expr=   m.x26 - 51.5*m.b139 <= 0)

m.c68 = Constraint(expr=   m.x27 - 52.5*m.b141 <= 0)

m.c69 = Constraint(expr=   m.x28 - 51.5*m.b144 <= 0)

m.c70 = Constraint(expr=   m.x29 - 51.5*m.b145 <= 0)

m.c71 = Constraint(expr=   m.x30 - 52.5*m.b147 <= 0)

m.c72 = Constraint(expr=   m.x31 - 51.5*m.b150 <= 0)

m.c73 = Constraint(expr=   m.x32 - 51.5*m.b151 <= 0)

m.c74 = Constraint(expr=   m.x33 - 52.5*m.b130 <= 0)

m.c75 = Constraint(expr=   m.x34 - 51.5*m.b132 <= 0)

m.c76 = Constraint(expr=   m.x35 - 53.5*m.b134 <= 0)

m.c77 = Constraint(expr=   m.x36 - 52.5*m.b136 <= 0)

m.c78 = Constraint(expr=   m.x37 - 51.5*m.b138 <= 0)

m.c79 = Constraint(expr=   m.x38 - 53.5*m.b140 <= 0)

m.c80 = Constraint(expr=   m.x39 - 52.5*m.b142 <= 0)

m.c81 = Constraint(expr=   m.x40 - 51.5*m.b144 <= 0)

m.c82 = Constraint(expr=   m.x41 - 53.5*m.b146 <= 0)

m.c83 = Constraint(expr=   m.x42 - 52.5*m.b148 <= 0)

m.c84 = Constraint(expr=   m.x43 - 51.5*m.b150 <= 0)

m.c85 = Constraint(expr=   m.x44 - 53.5*m.b152 <= 0)

m.c86 = Constraint(expr=   m.x45 - 52.5*m.b131 <= 0)

m.c87 = Constraint(expr=   m.x46 - 51.5*m.b133 <= 0)

m.c88 = Constraint(expr=   m.x47 - 53.5*m.b134 <= 0)

m.c89 = Constraint(expr=   m.x48 - 52.5*m.b137 <= 0)

m.c90 = Constraint(expr=   m.x49 - 51.5*m.b139 <= 0)

m.c91 = Constraint(expr=   m.x50 - 53.5*m.b140 <= 0)

m.c92 = Constraint(expr=   m.x51 - 52.5*m.b143 <= 0)

m.c93 = Constraint(expr=   m.x52 - 51.5*m.b145 <= 0)

m.c94 = Constraint(expr=   m.x53 - 53.5*m.b146 <= 0)

m.c95 = Constraint(expr=   m.x54 - 52.5*m.b149 <= 0)

m.c96 = Constraint(expr=   m.x55 - 51.5*m.b151 <= 0)

m.c97 = Constraint(expr=   m.x56 - 53.5*m.b152 <= 0)

m.c98 = Constraint(expr=   m.x57 - 82*m.b129 <= 0)

m.c99 = Constraint(expr=   m.x58 - 82*m.b130 <= 0)

m.c100 = Constraint(expr=   m.x59 - 82*m.b131 <= 0)

m.c101 = Constraint(expr=   m.x60 - 82*m.b135 <= 0)

m.c102 = Constraint(expr=   m.x61 - 82*m.b136 <= 0)

m.c103 = Constraint(expr=   m.x62 - 82*m.b137 <= 0)

m.c104 = Constraint(expr=   m.x63 - 82*m.b141 <= 0)

m.c105 = Constraint(expr=   m.x64 - 82*m.b142 <= 0)

m.c106 = Constraint(expr=   m.x65 - 82*m.b143 <= 0)

m.c107 = Constraint(expr=   m.x66 - 82*m.b147 <= 0)

m.c108 = Constraint(expr=   m.x67 - 82*m.b148 <= 0)

m.c109 = Constraint(expr=   m.x68 - 82*m.b149 <= 0)

m.c110 = Constraint(expr=   m.x69 - 82*m.b129 <= 0)

m.c111 = Constraint(expr=   m.x70 - 82.5*m.b132 <= 0)

m.c112 = Constraint(expr=   m.x71 - 82.5*m.b133 <= 0)

m.c113 = Constraint(expr=   m.x72 - 82*m.b135 <= 0)

m.c114 = Constraint(expr=   m.x73 - 82.5*m.b138 <= 0)

m.c115 = Constraint(expr=   m.x74 - 82.5*m.b139 <= 0)

m.c116 = Constraint(expr=   m.x75 - 82*m.b141 <= 0)

m.c117 = Constraint(expr=   m.x76 - 82.5*m.b144 <= 0)

m.c118 = Constraint(expr=   m.x77 - 82.5*m.b145 <= 0)

m.c119 = Constraint(expr=   m.x78 - 82*m.b147 <= 0)

m.c120 = Constraint(expr=   m.x79 - 82.5*m.b150 <= 0)

m.c121 = Constraint(expr=   m.x80 - 82.5*m.b151 <= 0)

m.c122 = Constraint(expr=   m.x81 - 82*m.b130 <= 0)

m.c123 = Constraint(expr=   m.x82 - 82.5*m.b132 <= 0)

m.c124 = Constraint(expr=   m.x83 - 83.5*m.b134 <= 0)

m.c125 = Constraint(expr=   m.x84 - 82*m.b136 <= 0)

m.c126 = Constraint(expr=   m.x85 - 82.5*m.b138 <= 0)

m.c127 = Constraint(expr=   m.x86 - 83.5*m.b140 <= 0)

m.c128 = Constraint(expr=   m.x87 - 82*m.b142 <= 0)

m.c129 = Constraint(expr=   m.x88 - 82.5*m.b144 <= 0)

m.c130 = Constraint(expr=   m.x89 - 83.5*m.b146 <= 0)

m.c131 = Constraint(expr=   m.x90 - 82*m.b148 <= 0)

m.c132 = Constraint(expr=   m.x91 - 82.5*m.b150 <= 0)

m.c133 = Constraint(expr=   m.x92 - 83.5*m.b152 <= 0)

m.c134 = Constraint(expr=   m.x93 - 82*m.b131 <= 0)

m.c135 = Constraint(expr=   m.x94 - 82.5*m.b133 <= 0)

m.c136 = Constraint(expr=   m.x95 - 83.5*m.b134 <= 0)

m.c137 = Constraint(expr=   m.x96 - 82*m.b137 <= 0)

m.c138 = Constraint(expr=   m.x97 - 82.5*m.b139 <= 0)

m.c139 = Constraint(expr=   m.x98 - 83.5*m.b140 <= 0)

m.c140 = Constraint(expr=   m.x99 - 82*m.b143 <= 0)

m.c141 = Constraint(expr=   m.x100 - 82.5*m.b145 <= 0)

m.c142 = Constraint(expr=   m.x101 - 83.5*m.b146 <= 0)

m.c143 = Constraint(expr=   m.x102 - 82*m.b149 <= 0)

m.c144 = Constraint(expr=   m.x103 - 82.5*m.b151 <= 0)

m.c145 = Constraint(expr=   m.x104 - 83.5*m.b152 <= 0)

m.c146 = Constraint(expr=   m.x9 - m.x21 + 6*m.b129 <= 0)

m.c147 = Constraint(expr=   m.x10 - m.x33 + 4*m.b130 <= 0)

m.c148 = Constraint(expr=   m.x11 - m.x45 + 3.5*m.b131 <= 0)

m.c149 = Constraint(expr=   m.x22 - m.x34 + 5*m.b132 <= 0)

m.c150 = Constraint(expr=   m.x23 - m.x46 + 4.5*m.b133 <= 0)

m.c151 = Constraint(expr=   m.x35 - m.x47 + 2.5*m.b134 <= 0)

m.c152 = Constraint(expr= - m.x12 + m.x24 + 6*m.b135 <= 0)

m.c153 = Constraint(expr= - m.x13 + m.x36 + 4*m.b136 <= 0)

m.c154 = Constraint(expr= - m.x14 + m.x48 + 3.5*m.b137 <= 0)

m.c155 = Constraint(expr= - m.x25 + m.x37 + 5*m.b138 <= 0)

m.c156 = Constraint(expr= - m.x26 + m.x49 + 4.5*m.b139 <= 0)

m.c157 = Constraint(expr= - m.x38 + m.x50 + 2.5*m.b140 <= 0)

m.c158 = Constraint(expr=   m.x63 - m.x75 + 5.5*m.b141 <= 0)

m.c159 = Constraint(expr=   m.x64 - m.x87 + 4.5*m.b142 <= 0)

m.c160 = Constraint(expr=   m.x65 - m.x99 + 4.5*m.b143 <= 0)

m.c161 = Constraint(expr=   m.x76 - m.x88 + 4*m.b144 <= 0)

m.c162 = Constraint(expr=   m.x77 - m.x100 + 4*m.b145 <= 0)

m.c163 = Constraint(expr=   m.x89 - m.x101 + 3*m.b146 <= 0)

m.c164 = Constraint(expr= - m.x66 + m.x78 + 5.5*m.b147 <= 0)

m.c165 = Constraint(expr= - m.x67 + m.x90 + 4.5*m.b148 <= 0)

m.c166 = Constraint(expr= - m.x68 + m.x102 + 4.5*m.b149 <= 0)

m.c167 = Constraint(expr= - m.x79 + m.x91 + 4*m.b150 <= 0)

m.c168 = Constraint(expr= - m.x80 + m.x103 + 4*m.b151 <= 0)

m.c169 = Constraint(expr= - m.x92 + m.x104 + 3*m.b152 <= 0)

m.c170 = Constraint(expr=   m.b129 + m.b135 + m.b141 + m.b147 == 1)

m.c171 = Constraint(expr=   m.b130 + m.b136 + m.b142 + m.b148 == 1)

m.c172 = Constraint(expr=   m.b131 + m.b137 + m.b143 + m.b149 == 1)

m.c173 = Constraint(expr=   m.b132 + m.b138 + m.b144 + m.b150 == 1)

m.c174 = Constraint(expr=   m.b133 + m.b139 + m.b145 + m.b151 == 1)

m.c175 = Constraint(expr=   m.b134 + m.b140 + m.b146 + m.b152 == 1)

m.c176 = Constraint(expr=   m.x1 - m.x105 - m.x109 - m.x113 == 0)

m.c177 = Constraint(expr=   m.x2 - m.x106 - m.x110 - m.x114 == 0)

m.c178 = Constraint(expr=   m.x3 - m.x107 - m.x111 - m.x115 == 0)

m.c179 = Constraint(expr=   m.x4 - m.x108 - m.x112 - m.x116 == 0)

m.c180 = Constraint(expr=   m.x5 - m.x117 - m.x121 - m.x125 == 0)

m.c181 = Constraint(expr=   m.x6 - m.x118 - m.x122 - m.x126 == 0)

m.c182 = Constraint(expr=   m.x7 - m.x119 - m.x123 - m.x127 == 0)

m.c183 = Constraint(expr=   m.x8 - m.x120 - m.x124 - m.x128 == 0)

m.c184 = Constraint(expr=   m.x105 - 18.5*m.b153 <= 0)

m.c185 = Constraint(expr=   m.x106 - 17.5*m.b154 <= 0)

m.c186 = Constraint(expr=   m.x107 - 19.5*m.b155 <= 0)

m.c187 = Constraint(expr=   m.x108 - 20*m.b156 <= 0)

m.c188 = Constraint(expr=   m.x109 - 52.5*m.b157 <= 0)

m.c189 = Constraint(expr=   m.x110 - 51.5*m.b158 <= 0)

m.c190 = Constraint(expr=   m.x111 - 53.5*m.b159 <= 0)

m.c191 = Constraint(expr=   m.x112 - 54*m.b160 <= 0)

m.c192 = Constraint(expr=   m.x113 - 31.5*m.b161 <= 0)

m.c193 = Constraint(expr=   m.x114 - 30.5*m.b162 <= 0)

m.c194 = Constraint(expr=   m.x115 - 32.5*m.b163 <= 0)

m.c195 = Constraint(expr=   m.x116 - 33*m.b164 <= 0)

m.c196 = Constraint(expr=   m.x117 - 13*m.b153 <= 0)

m.c197 = Constraint(expr=   m.x118 - 13.5*m.b154 <= 0)

m.c198 = Constraint(expr=   m.x119 - 14.5*m.b155 <= 0)

m.c199 = Constraint(expr=   m.x120 - 14.5*m.b156 <= 0)

m.c200 = Constraint(expr=   m.x121 - 82*m.b157 <= 0)

m.c201 = Constraint(expr=   m.x122 - 82.5*m.b158 <= 0)

m.c202 = Constraint(expr=   m.x123 - 83.5*m.b159 <= 0)

m.c203 = Constraint(expr=   m.x124 - 83.5*m.b160 <= 0)

m.c204 = Constraint(expr=   m.x125 - 51*m.b161 <= 0)

m.c205 = Constraint(expr=   m.x126 - 51.5*m.b162 <= 0)

m.c206 = Constraint(expr=   m.x127 - 52.5*m.b163 <= 0)

m.c207 = Constraint(expr=   m.x128 - 52.5*m.b164 <= 0)

m.c208 = Constraint(expr=((m.x105/(1e-6 + m.b153))**2 - 35*m.x105/(1e-6 + m.b153) + 306.25*m.b153 + (m.x117/(1e-6 + 
                         m.b153))**2 - 14*m.x117/(1e-6 + m.b153) + 49*m.b153 - 36*m.b153)*(1e-6 + m.b153) <= 0)

m.c209 = Constraint(expr=((m.x106/(1e-6 + m.b154))**2 - 37*m.x106/(1e-6 + m.b154) + 342.25*m.b154 + (m.x118/(1e-6 + 
                         m.b154))**2 - 15*m.x118/(1e-6 + m.b154) + 56.25*m.b154 - 36*m.b154)*(1e-6 + m.b154) <= 0)

m.c210 = Constraint(expr=((m.x107/(1e-6 + m.b155))**2 - 33*m.x107/(1e-6 + m.b155) + 272.25*m.b155 + (m.x119/(1e-6 + 
                         m.b155))**2 - 17*m.x119/(1e-6 + m.b155) + 72.25*m.b155 - 36*m.b155)*(1e-6 + m.b155) <= 0)

m.c211 = Constraint(expr=((m.x108/(1e-6 + m.b156))**2 - 32*m.x108/(1e-6 + m.b156) + 256*m.b156 + (m.x120/(1e-6 + m.b156)
                         )**2 - 17*m.x120/(1e-6 + m.b156) + 72.25*m.b156 - 36*m.b156)*(1e-6 + m.b156) <= 0)

m.c212 = Constraint(expr=((m.x109/(1e-6 + m.b157))**2 - 105*m.x109/(1e-6 + m.b157) + 2756.25*m.b157 + (m.x121/(1e-6 + 
                         m.b157))**2 - 154*m.x121/(1e-6 + m.b157) + 5929*m.b157 - 25*m.b157)*(1e-6 + m.b157) <= 0)

m.c213 = Constraint(expr=((m.x110/(1e-6 + m.b158))**2 - 107*m.x110/(1e-6 + m.b158) + 2862.25*m.b158 + (m.x122/(1e-6 + 
                         m.b158))**2 - 155*m.x122/(1e-6 + m.b158) + 6006.25*m.b158 - 25*m.b158)*(1e-6 + m.b158) <= 0)

m.c214 = Constraint(expr=((m.x111/(1e-6 + m.b159))**2 - 103*m.x111/(1e-6 + m.b159) + 2652.25*m.b159 + (m.x123/(1e-6 + 
                         m.b159))**2 - 157*m.x123/(1e-6 + m.b159) + 6162.25*m.b159 - 25*m.b159)*(1e-6 + m.b159) <= 0)

m.c215 = Constraint(expr=((m.x112/(1e-6 + m.b160))**2 - 102*m.x112/(1e-6 + m.b160) + 2601*m.b160 + (m.x124/(1e-6 + 
                         m.b160))**2 - 157*m.x124/(1e-6 + m.b160) + 6162.25*m.b160 - 25*m.b160)*(1e-6 + m.b160) <= 0)

m.c216 = Constraint(expr=((m.x113/(1e-6 + m.b161))**2 - 65*m.x113/(1e-6 + m.b161) + 1056.25*m.b161 + (m.x125/(1e-6 + 
                         m.b161))**2 - 94*m.x125/(1e-6 + m.b161) + 2209*m.b161 - 16*m.b161)*(1e-6 + m.b161) <= 0)

m.c217 = Constraint(expr=((m.x114/(1e-6 + m.b162))**2 - 67*m.x114/(1e-6 + m.b162) + 1122.25*m.b162 + (m.x126/(1e-6 + 
                         m.b162))**2 - 95*m.x126/(1e-6 + m.b162) + 2256.25*m.b162 - 16*m.b162)*(1e-6 + m.b162) <= 0)

m.c218 = Constraint(expr=((m.x115/(1e-6 + m.b163))**2 - 63*m.x115/(1e-6 + m.b163) + 992.25*m.b163 + (m.x127/(1e-6 + 
                         m.b163))**2 - 97*m.x127/(1e-6 + m.b163) + 2352.25*m.b163 - 16*m.b163)*(1e-6 + m.b163) <= 0)

m.c219 = Constraint(expr=((m.x116/(1e-6 + m.b164))**2 - 62*m.x116/(1e-6 + m.b164) + 961*m.b164 + (m.x128/(1e-6 + m.b164)
                         )**2 - 97*m.x128/(1e-6 + m.b164) + 2352.25*m.b164 - 16*m.b164)*(1e-6 + m.b164) <= 0)

m.c220 = Constraint(expr=((m.x105/(1e-6 + m.b153))**2 - 35*m.x105/(1e-6 + m.b153) + 306.25*m.b153 + (m.x117/(1e-6 + 
                         m.b153))**2 - 26*m.x117/(1e-6 + m.b153) + 169*m.b153 - 36*m.b153)*(1e-6 + m.b153) <= 0)

m.c221 = Constraint(expr=((m.x106/(1e-6 + m.b154))**2 - 37*m.x106/(1e-6 + m.b154) + 342.25*m.b154 + (m.x118/(1e-6 + 
                         m.b154))**2 - 25*m.x118/(1e-6 + m.b154) + 156.25*m.b154 - 36*m.b154)*(1e-6 + m.b154) <= 0)

m.c222 = Constraint(expr=((m.x107/(1e-6 + m.b155))**2 - 33*m.x107/(1e-6 + m.b155) + 272.25*m.b155 + (m.x119/(1e-6 + 
                         m.b155))**2 - 23*m.x119/(1e-6 + m.b155) + 132.25*m.b155 - 36*m.b155)*(1e-6 + m.b155) <= 0)

m.c223 = Constraint(expr=((m.x108/(1e-6 + m.b156))**2 - 32*m.x108/(1e-6 + m.b156) + 256*m.b156 + (m.x120/(1e-6 + m.b156)
                         )**2 - 23*m.x120/(1e-6 + m.b156) + 132.25*m.b156 - 36*m.b156)*(1e-6 + m.b156) <= 0)

m.c224 = Constraint(expr=((m.x109/(1e-6 + m.b157))**2 - 105*m.x109/(1e-6 + m.b157) + 2756.25*m.b157 + (m.x121/(1e-6 + 
                         m.b157))**2 - 166*m.x121/(1e-6 + m.b157) + 6889*m.b157 - 25*m.b157)*(1e-6 + m.b157) <= 0)

m.c225 = Constraint(expr=((m.x110/(1e-6 + m.b158))**2 - 107*m.x110/(1e-6 + m.b158) + 2862.25*m.b158 + (m.x122/(1e-6 + 
                         m.b158))**2 - 165*m.x122/(1e-6 + m.b158) + 6806.25*m.b158 - 25*m.b158)*(1e-6 + m.b158) <= 0)

m.c226 = Constraint(expr=((m.x111/(1e-6 + m.b159))**2 - 103*m.x111/(1e-6 + m.b159) + 2652.25*m.b159 + (m.x123/(1e-6 + 
                         m.b159))**2 - 163*m.x123/(1e-6 + m.b159) + 6642.25*m.b159 - 25*m.b159)*(1e-6 + m.b159) <= 0)

m.c227 = Constraint(expr=((m.x112/(1e-6 + m.b160))**2 - 102*m.x112/(1e-6 + m.b160) + 2601*m.b160 + (m.x124/(1e-6 + 
                         m.b160))**2 - 163*m.x124/(1e-6 + m.b160) + 6642.25*m.b160 - 25*m.b160)*(1e-6 + m.b160) <= 0)

m.c228 = Constraint(expr=((m.x113/(1e-6 + m.b161))**2 - 65*m.x113/(1e-6 + m.b161) + 1056.25*m.b161 + (m.x125/(1e-6 + 
                         m.b161))**2 - 106*m.x125/(1e-6 + m.b161) + 2809*m.b161 - 16*m.b161)*(1e-6 + m.b161) <= 0)

m.c229 = Constraint(expr=((m.x114/(1e-6 + m.b162))**2 - 67*m.x114/(1e-6 + m.b162) + 1122.25*m.b162 + (m.x126/(1e-6 + 
                         m.b162))**2 - 105*m.x126/(1e-6 + m.b162) + 2756.25*m.b162 - 16*m.b162)*(1e-6 + m.b162) <= 0)

m.c230 = Constraint(expr=((m.x115/(1e-6 + m.b163))**2 - 63*m.x115/(1e-6 + m.b163) + 992.25*m.b163 + (m.x127/(1e-6 + 
                         m.b163))**2 - 103*m.x127/(1e-6 + m.b163) + 2652.25*m.b163 - 16*m.b163)*(1e-6 + m.b163) <= 0)

m.c231 = Constraint(expr=((m.x116/(1e-6 + m.b164))**2 - 62*m.x116/(1e-6 + m.b164) + 961*m.b164 + (m.x128/(1e-6 + m.b164)
                         )**2 - 103*m.x128/(1e-6 + m.b164) + 2652.25*m.b164 - 16*m.b164)*(1e-6 + m.b164) <= 0)

m.c232 = Constraint(expr=((m.x105/(1e-6 + m.b153))**2 - 25*m.x105/(1e-6 + m.b153) + 156.25*m.b153 + (m.x117/(1e-6 + 
                         m.b153))**2 - 14*m.x117/(1e-6 + m.b153) + 49*m.b153 - 36*m.b153)*(1e-6 + m.b153) <= 0)

m.c233 = Constraint(expr=((m.x106/(1e-6 + m.b154))**2 - 23*m.x106/(1e-6 + m.b154) + 132.25*m.b154 + (m.x118/(1e-6 + 
                         m.b154))**2 - 15*m.x118/(1e-6 + m.b154) + 56.25*m.b154 - 36*m.b154)*(1e-6 + m.b154) <= 0)

m.c234 = Constraint(expr=((m.x107/(1e-6 + m.b155))**2 - 27*m.x107/(1e-6 + m.b155) + 182.25*m.b155 + (m.x119/(1e-6 + 
                         m.b155))**2 - 17*m.x119/(1e-6 + m.b155) + 72.25*m.b155 - 36*m.b155)*(1e-6 + m.b155) <= 0)

m.c235 = Constraint(expr=((m.x108/(1e-6 + m.b156))**2 - 28*m.x108/(1e-6 + m.b156) + 196*m.b156 + (m.x120/(1e-6 + m.b156)
                         )**2 - 17*m.x120/(1e-6 + m.b156) + 72.25*m.b156 - 36*m.b156)*(1e-6 + m.b156) <= 0)

m.c236 = Constraint(expr=((m.x109/(1e-6 + m.b157))**2 - 95*m.x109/(1e-6 + m.b157) + 2256.25*m.b157 + (m.x121/(1e-6 + 
                         m.b157))**2 - 154*m.x121/(1e-6 + m.b157) + 5929*m.b157 - 25*m.b157)*(1e-6 + m.b157) <= 0)

m.c237 = Constraint(expr=((m.x110/(1e-6 + m.b158))**2 - 93*m.x110/(1e-6 + m.b158) + 2162.25*m.b158 + (m.x122/(1e-6 + 
                         m.b158))**2 - 155*m.x122/(1e-6 + m.b158) + 6006.25*m.b158 - 25*m.b158)*(1e-6 + m.b158) <= 0)

m.c238 = Constraint(expr=((m.x111/(1e-6 + m.b159))**2 - 97*m.x111/(1e-6 + m.b159) + 2352.25*m.b159 + (m.x123/(1e-6 + 
                         m.b159))**2 - 157*m.x123/(1e-6 + m.b159) + 6162.25*m.b159 - 25*m.b159)*(1e-6 + m.b159) <= 0)

m.c239 = Constraint(expr=((m.x112/(1e-6 + m.b160))**2 - 98*m.x112/(1e-6 + m.b160) + 2401*m.b160 + (m.x124/(1e-6 + m.b160
                         ))**2 - 157*m.x124/(1e-6 + m.b160) + 6162.25*m.b160 - 25*m.b160)*(1e-6 + m.b160) <= 0)

m.c240 = Constraint(expr=((m.x113/(1e-6 + m.b161))**2 - 55*m.x113/(1e-6 + m.b161) + 756.25*m.b161 + (m.x125/(1e-6 + 
                         m.b161))**2 - 94*m.x125/(1e-6 + m.b161) + 2209*m.b161 - 16*m.b161)*(1e-6 + m.b161) <= 0)

m.c241 = Constraint(expr=((m.x114/(1e-6 + m.b162))**2 - 53*m.x114/(1e-6 + m.b162) + 702.25*m.b162 + (m.x126/(1e-6 + 
                         m.b162))**2 - 95*m.x126/(1e-6 + m.b162) + 2256.25*m.b162 - 16*m.b162)*(1e-6 + m.b162) <= 0)

m.c242 = Constraint(expr=((m.x115/(1e-6 + m.b163))**2 - 57*m.x115/(1e-6 + m.b163) + 812.25*m.b163 + (m.x127/(1e-6 + 
                         m.b163))**2 - 97*m.x127/(1e-6 + m.b163) + 2352.25*m.b163 - 16*m.b163)*(1e-6 + m.b163) <= 0)

m.c243 = Constraint(expr=((m.x116/(1e-6 + m.b164))**2 - 58*m.x116/(1e-6 + m.b164) + 841*m.b164 + (m.x128/(1e-6 + m.b164)
                         )**2 - 97*m.x128/(1e-6 + m.b164) + 2352.25*m.b164 - 16*m.b164)*(1e-6 + m.b164) <= 0)

m.c244 = Constraint(expr=((m.x105/(1e-6 + m.b153))**2 - 25*m.x105/(1e-6 + m.b153) + 156.25*m.b153 + (m.x117/(1e-6 + 
                         m.b153))**2 - 26*m.x117/(1e-6 + m.b153) + 169*m.b153 - 36*m.b153)*(1e-6 + m.b153) <= 0)

m.c245 = Constraint(expr=((m.x106/(1e-6 + m.b154))**2 - 23*m.x106/(1e-6 + m.b154) + 132.25*m.b154 + (m.x118/(1e-6 + 
                         m.b154))**2 - 25*m.x118/(1e-6 + m.b154) + 156.25*m.b154 - 36*m.b154)*(1e-6 + m.b154) <= 0)

m.c246 = Constraint(expr=((m.x107/(1e-6 + m.b155))**2 - 27*m.x107/(1e-6 + m.b155) + 182.25*m.b155 + (m.x119/(1e-6 + 
                         m.b155))**2 - 23*m.x119/(1e-6 + m.b155) + 132.25*m.b155 - 36*m.b155)*(1e-6 + m.b155) <= 0)

m.c247 = Constraint(expr=((m.x108/(1e-6 + m.b156))**2 - 28*m.x108/(1e-6 + m.b156) + 196*m.b156 + (m.x120/(1e-6 + m.b156)
                         )**2 - 23*m.x120/(1e-6 + m.b156) + 132.25*m.b156 - 36*m.b156)*(1e-6 + m.b156) <= 0)

m.c248 = Constraint(expr=((m.x109/(1e-6 + m.b157))**2 - 95*m.x109/(1e-6 + m.b157) + 2256.25*m.b157 + (m.x121/(1e-6 + 
                         m.b157))**2 - 166*m.x121/(1e-6 + m.b157) + 6889*m.b157 - 25*m.b157)*(1e-6 + m.b157) <= 0)

m.c249 = Constraint(expr=((m.x110/(1e-6 + m.b158))**2 - 93*m.x110/(1e-6 + m.b158) + 2162.25*m.b158 + (m.x122/(1e-6 + 
                         m.b158))**2 - 165*m.x122/(1e-6 + m.b158) + 6806.25*m.b158 - 25*m.b158)*(1e-6 + m.b158) <= 0)

m.c250 = Constraint(expr=((m.x111/(1e-6 + m.b159))**2 - 97*m.x111/(1e-6 + m.b159) + 2352.25*m.b159 + (m.x123/(1e-6 + 
                         m.b159))**2 - 163*m.x123/(1e-6 + m.b159) + 6642.25*m.b159 - 25*m.b159)*(1e-6 + m.b159) <= 0)

m.c251 = Constraint(expr=((m.x112/(1e-6 + m.b160))**2 - 98*m.x112/(1e-6 + m.b160) + 2401*m.b160 + (m.x124/(1e-6 + m.b160
                         ))**2 - 163*m.x124/(1e-6 + m.b160) + 6642.25*m.b160 - 25*m.b160)*(1e-6 + m.b160) <= 0)

m.c252 = Constraint(expr=((m.x113/(1e-6 + m.b161))**2 - 55*m.x113/(1e-6 + m.b161) + 756.25*m.b161 + (m.x125/(1e-6 + 
                         m.b161))**2 - 106*m.x125/(1e-6 + m.b161) + 2809*m.b161 - 16*m.b161)*(1e-6 + m.b161) <= 0)

m.c253 = Constraint(expr=((m.x114/(1e-6 + m.b162))**2 - 53*m.x114/(1e-6 + m.b162) + 702.25*m.b162 + (m.x126/(1e-6 + 
                         m.b162))**2 - 105*m.x126/(1e-6 + m.b162) + 2756.25*m.b162 - 16*m.b162)*(1e-6 + m.b162) <= 0)

m.c254 = Constraint(expr=((m.x115/(1e-6 + m.b163))**2 - 57*m.x115/(1e-6 + m.b163) + 812.25*m.b163 + (m.x127/(1e-6 + 
                         m.b163))**2 - 103*m.x127/(1e-6 + m.b163) + 2652.25*m.b163 - 16*m.b163)*(1e-6 + m.b163) <= 0)

m.c255 = Constraint(expr=((m.x116/(1e-6 + m.b164))**2 - 58*m.x116/(1e-6 + m.b164) + 841*m.b164 + (m.x128/(1e-6 + m.b164)
                         )**2 - 103*m.x128/(1e-6 + m.b164) + 2652.25*m.b164 - 16*m.b164)*(1e-6 + m.b164) <= 0)

m.c256 = Constraint(expr=   m.b153 + m.b157 + m.b161 == 1)

m.c257 = Constraint(expr=   m.b154 + m.b158 + m.b162 == 1)

m.c258 = Constraint(expr=   m.b155 + m.b159 + m.b163 == 1)

m.c259 = Constraint(expr=   m.b156 + m.b160 + m.b164 == 1)

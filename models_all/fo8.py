#  MINLP written by GAMS Convert at 05/15/20 00:50:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        274        1        0      273        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        147       91       56        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1137     1121       16        0
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
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x114 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x115 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x116 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x117 = Var(within=Reals,bounds=(3,11.31),initialize=3)
m.x118 = Var(within=Reals,bounds=(3,11.31),initialize=3)
m.x119 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x120 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x121 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x122 = Var(within=Reals,bounds=(11.31,11.31),initialize=11.31)
m.x123 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x124 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x125 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x126 = Var(within=Reals,bounds=(3.183,12),initialize=3.183)
m.x127 = Var(within=Reals,bounds=(3.183,12),initialize=3.183)
m.x128 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x129 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x130 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x131 = Var(within=Reals,bounds=(13,13),initialize=13)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x58 + m.x59 + m.x72 + m.x73 + m.x84 + m.x85 + m.x94 + m.x95 + m.x102 + m.x103 + m.x108
                        + m.x109 + m.x112 + m.x113, sense=minimize)

m.c2 = Constraint(expr=   m.x132 - m.x133 <= 0)

m.c3 = Constraint(expr=   0.5*m.x114 - m.x122 + m.x132 <= 0)

m.c4 = Constraint(expr=   0.5*m.x114 - m.x132 <= 0)

m.c5 = Constraint(expr=   0.5*m.x123 - m.x131 + m.x140 <= 0)

m.c6 = Constraint(expr=   0.5*m.x123 - m.x140 <= 0)

m.c7 = Constraint(expr=   0.5*m.x115 - m.x122 + m.x133 <= 0)

m.c8 = Constraint(expr=   0.5*m.x115 - m.x133 <= 0)

m.c9 = Constraint(expr=   0.5*m.x124 - m.x131 + m.x141 <= 0)

m.c10 = Constraint(expr=   0.5*m.x124 - m.x141 <= 0)

m.c11 = Constraint(expr=   0.5*m.x116 - m.x122 + m.x134 <= 0)

m.c12 = Constraint(expr=   0.5*m.x116 - m.x134 <= 0)

m.c13 = Constraint(expr=   0.5*m.x125 - m.x131 + m.x142 <= 0)

m.c14 = Constraint(expr=   0.5*m.x125 - m.x142 <= 0)

m.c15 = Constraint(expr=   0.5*m.x117 - m.x122 + m.x135 <= 0)

m.c16 = Constraint(expr=   0.5*m.x117 - m.x135 <= 0)

m.c17 = Constraint(expr=   0.5*m.x126 - m.x131 + m.x143 <= 0)

m.c18 = Constraint(expr=   0.5*m.x126 - m.x143 <= 0)

m.c19 = Constraint(expr=   0.5*m.x118 - m.x122 + m.x136 <= 0)

m.c20 = Constraint(expr=   0.5*m.x118 - m.x136 <= 0)

m.c21 = Constraint(expr=   0.5*m.x127 - m.x131 + m.x144 <= 0)

m.c22 = Constraint(expr=   0.5*m.x127 - m.x144 <= 0)

m.c23 = Constraint(expr=   0.5*m.x119 - m.x122 + m.x137 <= 0)

m.c24 = Constraint(expr=   0.5*m.x119 - m.x137 <= 0)

m.c25 = Constraint(expr=   0.5*m.x128 - m.x131 + m.x145 <= 0)

m.c26 = Constraint(expr=   0.5*m.x128 - m.x145 <= 0)

m.c27 = Constraint(expr=   0.5*m.x120 - m.x122 + m.x138 <= 0)

m.c28 = Constraint(expr=   0.5*m.x120 - m.x138 <= 0)

m.c29 = Constraint(expr=   0.5*m.x129 - m.x131 + m.x146 <= 0)

m.c30 = Constraint(expr=   0.5*m.x129 - m.x146 <= 0)

m.c31 = Constraint(expr=   0.5*m.x121 - m.x122 + m.x139 <= 0)

m.c32 = Constraint(expr=   0.5*m.x121 - m.x139 <= 0)

m.c33 = Constraint(expr=   0.5*m.x130 - m.x131 + m.x147 <= 0)

m.c34 = Constraint(expr=   0.5*m.x130 - m.x147 <= 0)

m.c35 = Constraint(expr= - m.x58 + m.x132 - m.x133 <= 0)

m.c36 = Constraint(expr= - m.x58 - m.x132 + m.x133 <= 0)

m.c37 = Constraint(expr= - m.x59 + m.x140 - m.x141 <= 0)

m.c38 = Constraint(expr= - m.x59 - m.x140 + m.x141 <= 0)

m.c39 = Constraint(expr= - 11.31*m.b1 - 11.31*m.b2 + 0.5*m.x114 + 0.5*m.x115 - m.x132 + m.x133 <= 0)

m.c40 = Constraint(expr= - 11.31*m.b1 + 11.31*m.b2 + 0.5*m.x114 + 0.5*m.x115 + m.x132 - m.x133 <= 11.31)

m.c41 = Constraint(expr=   13*m.b1 - 13*m.b2 + 0.5*m.x123 + 0.5*m.x124 - m.x140 + m.x141 <= 13)

m.c42 = Constraint(expr=   13*m.b1 + 13*m.b2 + 0.5*m.x123 + 0.5*m.x124 + m.x140 - m.x141 <= 26)

m.c43 = Constraint(expr= - m.x60 + m.x132 - m.x134 <= 0)

m.c44 = Constraint(expr= - m.x60 - m.x132 + m.x134 <= 0)

m.c45 = Constraint(expr= - m.x61 + m.x140 - m.x142 <= 0)

m.c46 = Constraint(expr= - m.x61 - m.x140 + m.x142 <= 0)

m.c47 = Constraint(expr= - 11.31*m.b3 - 11.31*m.b4 + 0.5*m.x114 + 0.5*m.x116 - m.x132 + m.x134 <= 0)

m.c48 = Constraint(expr= - 11.31*m.b3 + 11.31*m.b4 + 0.5*m.x114 + 0.5*m.x116 + m.x132 - m.x134 <= 11.31)

m.c49 = Constraint(expr=   13*m.b3 - 13*m.b4 + 0.5*m.x123 + 0.5*m.x125 - m.x140 + m.x142 <= 13)

m.c50 = Constraint(expr=   13*m.b3 + 13*m.b4 + 0.5*m.x123 + 0.5*m.x125 + m.x140 - m.x142 <= 26)

m.c51 = Constraint(expr= - m.x62 + m.x132 - m.x135 <= 0)

m.c52 = Constraint(expr= - m.x62 - m.x132 + m.x135 <= 0)

m.c53 = Constraint(expr= - m.x63 + m.x140 - m.x143 <= 0)

m.c54 = Constraint(expr= - m.x63 - m.x140 + m.x143 <= 0)

m.c55 = Constraint(expr= - 11.31*m.b5 - 11.31*m.b6 + 0.5*m.x114 + 0.5*m.x117 - m.x132 + m.x135 <= 0)

m.c56 = Constraint(expr= - 11.31*m.b5 + 11.31*m.b6 + 0.5*m.x114 + 0.5*m.x117 + m.x132 - m.x135 <= 11.31)

m.c57 = Constraint(expr=   13*m.b5 - 13*m.b6 + 0.5*m.x123 + 0.5*m.x126 - m.x140 + m.x143 <= 13)

m.c58 = Constraint(expr=   13*m.b5 + 13*m.b6 + 0.5*m.x123 + 0.5*m.x126 + m.x140 - m.x143 <= 26)

m.c59 = Constraint(expr= - m.x64 + m.x132 - m.x136 <= 0)

m.c60 = Constraint(expr= - m.x64 - m.x132 + m.x136 <= 0)

m.c61 = Constraint(expr= - m.x65 + m.x140 - m.x144 <= 0)

m.c62 = Constraint(expr= - m.x65 - m.x140 + m.x144 <= 0)

m.c63 = Constraint(expr= - 11.31*m.b7 - 11.31*m.b8 + 0.5*m.x114 + 0.5*m.x118 - m.x132 + m.x136 <= 0)

m.c64 = Constraint(expr= - 11.31*m.b7 + 11.31*m.b8 + 0.5*m.x114 + 0.5*m.x118 + m.x132 - m.x136 <= 11.31)

m.c65 = Constraint(expr=   13*m.b7 - 13*m.b8 + 0.5*m.x123 + 0.5*m.x127 - m.x140 + m.x144 <= 13)

m.c66 = Constraint(expr=   13*m.b7 + 13*m.b8 + 0.5*m.x123 + 0.5*m.x127 + m.x140 - m.x144 <= 26)

m.c67 = Constraint(expr= - m.x66 + m.x132 - m.x137 <= 0)

m.c68 = Constraint(expr= - m.x66 - m.x132 + m.x137 <= 0)

m.c69 = Constraint(expr= - m.x67 + m.x140 - m.x145 <= 0)

m.c70 = Constraint(expr= - m.x67 - m.x140 + m.x145 <= 0)

m.c71 = Constraint(expr= - 11.31*m.b9 - 11.31*m.b10 + 0.5*m.x114 + 0.5*m.x119 - m.x132 + m.x137 <= 0)

m.c72 = Constraint(expr= - 11.31*m.b9 + 11.31*m.b10 + 0.5*m.x114 + 0.5*m.x119 + m.x132 - m.x137 <= 11.31)

m.c73 = Constraint(expr=   13*m.b9 - 13*m.b10 + 0.5*m.x123 + 0.5*m.x128 - m.x140 + m.x145 <= 13)

m.c74 = Constraint(expr=   13*m.b9 + 13*m.b10 + 0.5*m.x123 + 0.5*m.x128 + m.x140 - m.x145 <= 26)

m.c75 = Constraint(expr= - m.x68 + m.x132 - m.x138 <= 0)

m.c76 = Constraint(expr= - m.x68 - m.x132 + m.x138 <= 0)

m.c77 = Constraint(expr= - m.x69 + m.x140 - m.x146 <= 0)

m.c78 = Constraint(expr= - m.x69 - m.x140 + m.x146 <= 0)

m.c79 = Constraint(expr= - 11.31*m.b11 - 11.31*m.b12 + 0.5*m.x114 + 0.5*m.x120 - m.x132 + m.x138 <= 0)

m.c80 = Constraint(expr= - 11.31*m.b11 + 11.31*m.b12 + 0.5*m.x114 + 0.5*m.x120 + m.x132 - m.x138 <= 11.31)

m.c81 = Constraint(expr=   13*m.b11 - 13*m.b12 + 0.5*m.x123 + 0.5*m.x129 - m.x140 + m.x146 <= 13)

m.c82 = Constraint(expr=   13*m.b11 + 13*m.b12 + 0.5*m.x123 + 0.5*m.x129 + m.x140 - m.x146 <= 26)

m.c83 = Constraint(expr= - m.x70 + m.x132 - m.x139 <= 0)

m.c84 = Constraint(expr= - m.x70 - m.x132 + m.x139 <= 0)

m.c85 = Constraint(expr= - m.x71 + m.x140 - m.x147 <= 0)

m.c86 = Constraint(expr= - m.x71 - m.x140 + m.x147 <= 0)

m.c87 = Constraint(expr= - 11.31*m.b13 - 11.31*m.b14 + 0.5*m.x114 + 0.5*m.x121 - m.x132 + m.x139 <= 0)

m.c88 = Constraint(expr= - 11.31*m.b13 + 11.31*m.b14 + 0.5*m.x114 + 0.5*m.x121 + m.x132 - m.x139 <= 11.31)

m.c89 = Constraint(expr=   13*m.b13 - 13*m.b14 + 0.5*m.x123 + 0.5*m.x130 - m.x140 + m.x147 <= 13)

m.c90 = Constraint(expr=   13*m.b13 + 13*m.b14 + 0.5*m.x123 + 0.5*m.x130 + m.x140 - m.x147 <= 26)

m.c91 = Constraint(expr= - m.x72 + m.x133 - m.x134 <= 0)

m.c92 = Constraint(expr= - m.x72 - m.x133 + m.x134 <= 0)

m.c93 = Constraint(expr= - m.x73 + m.x141 - m.x142 <= 0)

m.c94 = Constraint(expr= - m.x73 - m.x141 + m.x142 <= 0)

m.c95 = Constraint(expr= - 11.31*m.b15 - 11.31*m.b16 + 0.5*m.x115 + 0.5*m.x116 - m.x133 + m.x134 <= 0)

m.c96 = Constraint(expr= - 11.31*m.b15 + 11.31*m.b16 + 0.5*m.x115 + 0.5*m.x116 + m.x133 - m.x134 <= 11.31)

m.c97 = Constraint(expr=   13*m.b15 - 13*m.b16 + 0.5*m.x124 + 0.5*m.x125 - m.x141 + m.x142 <= 13)

m.c98 = Constraint(expr=   13*m.b15 + 13*m.b16 + 0.5*m.x124 + 0.5*m.x125 + m.x141 - m.x142 <= 26)

m.c99 = Constraint(expr= - m.x74 + m.x133 - m.x135 <= 0)

m.c100 = Constraint(expr= - m.x74 - m.x133 + m.x135 <= 0)

m.c101 = Constraint(expr= - m.x75 + m.x141 - m.x143 <= 0)

m.c102 = Constraint(expr= - m.x75 - m.x141 + m.x143 <= 0)

m.c103 = Constraint(expr= - 11.31*m.b17 - 11.31*m.b18 + 0.5*m.x115 + 0.5*m.x117 - m.x133 + m.x135 <= 0)

m.c104 = Constraint(expr= - 11.31*m.b17 + 11.31*m.b18 + 0.5*m.x115 + 0.5*m.x117 + m.x133 - m.x135 <= 11.31)

m.c105 = Constraint(expr=   13*m.b17 - 13*m.b18 + 0.5*m.x124 + 0.5*m.x126 - m.x141 + m.x143 <= 13)

m.c106 = Constraint(expr=   13*m.b17 + 13*m.b18 + 0.5*m.x124 + 0.5*m.x126 + m.x141 - m.x143 <= 26)

m.c107 = Constraint(expr= - m.x76 + m.x133 - m.x136 <= 0)

m.c108 = Constraint(expr= - m.x76 - m.x133 + m.x136 <= 0)

m.c109 = Constraint(expr= - m.x77 + m.x141 - m.x144 <= 0)

m.c110 = Constraint(expr= - m.x77 - m.x141 + m.x144 <= 0)

m.c111 = Constraint(expr= - 11.31*m.b19 - 11.31*m.b20 + 0.5*m.x115 + 0.5*m.x118 - m.x133 + m.x136 <= 0)

m.c112 = Constraint(expr= - 11.31*m.b19 + 11.31*m.b20 + 0.5*m.x115 + 0.5*m.x118 + m.x133 - m.x136 <= 11.31)

m.c113 = Constraint(expr=   13*m.b19 - 13*m.b20 + 0.5*m.x124 + 0.5*m.x127 - m.x141 + m.x144 <= 13)

m.c114 = Constraint(expr=   13*m.b19 + 13*m.b20 + 0.5*m.x124 + 0.5*m.x127 + m.x141 - m.x144 <= 26)

m.c115 = Constraint(expr= - m.x78 + m.x133 - m.x137 <= 0)

m.c116 = Constraint(expr= - m.x78 - m.x133 + m.x137 <= 0)

m.c117 = Constraint(expr= - m.x79 + m.x141 - m.x145 <= 0)

m.c118 = Constraint(expr= - m.x79 - m.x141 + m.x145 <= 0)

m.c119 = Constraint(expr= - 11.31*m.b21 - 11.31*m.b22 + 0.5*m.x115 + 0.5*m.x119 - m.x133 + m.x137 <= 0)

m.c120 = Constraint(expr= - 11.31*m.b21 + 11.31*m.b22 + 0.5*m.x115 + 0.5*m.x119 + m.x133 - m.x137 <= 11.31)

m.c121 = Constraint(expr=   13*m.b21 - 13*m.b22 + 0.5*m.x124 + 0.5*m.x128 - m.x141 + m.x145 <= 13)

m.c122 = Constraint(expr=   13*m.b21 + 13*m.b22 + 0.5*m.x124 + 0.5*m.x128 + m.x141 - m.x145 <= 26)

m.c123 = Constraint(expr= - m.x80 + m.x133 - m.x138 <= 0)

m.c124 = Constraint(expr= - m.x80 - m.x133 + m.x138 <= 0)

m.c125 = Constraint(expr= - m.x81 + m.x141 - m.x146 <= 0)

m.c126 = Constraint(expr= - m.x81 - m.x141 + m.x146 <= 0)

m.c127 = Constraint(expr= - 11.31*m.b23 - 11.31*m.b24 + 0.5*m.x115 + 0.5*m.x120 - m.x133 + m.x138 <= 0)

m.c128 = Constraint(expr= - 11.31*m.b23 + 11.31*m.b24 + 0.5*m.x115 + 0.5*m.x120 + m.x133 - m.x138 <= 11.31)

m.c129 = Constraint(expr=   13*m.b23 - 13*m.b24 + 0.5*m.x124 + 0.5*m.x129 - m.x141 + m.x146 <= 13)

m.c130 = Constraint(expr=   13*m.b23 + 13*m.b24 + 0.5*m.x124 + 0.5*m.x129 + m.x141 - m.x146 <= 26)

m.c131 = Constraint(expr= - m.x82 + m.x133 - m.x139 <= 0)

m.c132 = Constraint(expr= - m.x82 - m.x133 + m.x139 <= 0)

m.c133 = Constraint(expr= - m.x83 + m.x141 - m.x147 <= 0)

m.c134 = Constraint(expr= - m.x83 - m.x141 + m.x147 <= 0)

m.c135 = Constraint(expr= - 11.31*m.b25 - 11.31*m.b26 + 0.5*m.x115 + 0.5*m.x121 - m.x133 + m.x139 <= 0)

m.c136 = Constraint(expr= - 11.31*m.b25 + 11.31*m.b26 + 0.5*m.x115 + 0.5*m.x121 + m.x133 - m.x139 <= 11.31)

m.c137 = Constraint(expr=   13*m.b25 - 13*m.b26 + 0.5*m.x124 + 0.5*m.x130 - m.x141 + m.x147 <= 13)

m.c138 = Constraint(expr=   13*m.b25 + 13*m.b26 + 0.5*m.x124 + 0.5*m.x130 + m.x141 - m.x147 <= 26)

m.c139 = Constraint(expr= - m.x84 + m.x134 - m.x135 <= 0)

m.c140 = Constraint(expr= - m.x84 - m.x134 + m.x135 <= 0)

m.c141 = Constraint(expr= - m.x85 + m.x142 - m.x143 <= 0)

m.c142 = Constraint(expr= - m.x85 - m.x142 + m.x143 <= 0)

m.c143 = Constraint(expr= - 11.31*m.b27 - 11.31*m.b28 + 0.5*m.x116 + 0.5*m.x117 - m.x134 + m.x135 <= 0)

m.c144 = Constraint(expr= - 11.31*m.b27 + 11.31*m.b28 + 0.5*m.x116 + 0.5*m.x117 + m.x134 - m.x135 <= 11.31)

m.c145 = Constraint(expr=   13*m.b27 - 13*m.b28 + 0.5*m.x125 + 0.5*m.x126 - m.x142 + m.x143 <= 13)

m.c146 = Constraint(expr=   13*m.b27 + 13*m.b28 + 0.5*m.x125 + 0.5*m.x126 + m.x142 - m.x143 <= 26)

m.c147 = Constraint(expr= - m.x86 + m.x134 - m.x136 <= 0)

m.c148 = Constraint(expr= - m.x86 - m.x134 + m.x136 <= 0)

m.c149 = Constraint(expr= - m.x87 + m.x142 - m.x144 <= 0)

m.c150 = Constraint(expr= - m.x87 - m.x142 + m.x144 <= 0)

m.c151 = Constraint(expr= - 11.31*m.b29 - 11.31*m.b30 + 0.5*m.x116 + 0.5*m.x118 - m.x134 + m.x136 <= 0)

m.c152 = Constraint(expr= - 11.31*m.b29 + 11.31*m.b30 + 0.5*m.x116 + 0.5*m.x118 + m.x134 - m.x136 <= 11.31)

m.c153 = Constraint(expr=   13*m.b29 - 13*m.b30 + 0.5*m.x125 + 0.5*m.x127 - m.x142 + m.x144 <= 13)

m.c154 = Constraint(expr=   13*m.b29 + 13*m.b30 + 0.5*m.x125 + 0.5*m.x127 + m.x142 - m.x144 <= 26)

m.c155 = Constraint(expr= - m.x88 + m.x134 - m.x137 <= 0)

m.c156 = Constraint(expr= - m.x88 - m.x134 + m.x137 <= 0)

m.c157 = Constraint(expr= - m.x89 + m.x142 - m.x145 <= 0)

m.c158 = Constraint(expr= - m.x89 - m.x142 + m.x145 <= 0)

m.c159 = Constraint(expr= - 11.31*m.b31 - 11.31*m.b32 + 0.5*m.x116 + 0.5*m.x119 - m.x134 + m.x137 <= 0)

m.c160 = Constraint(expr= - 11.31*m.b31 + 11.31*m.b32 + 0.5*m.x116 + 0.5*m.x119 + m.x134 - m.x137 <= 11.31)

m.c161 = Constraint(expr=   13*m.b31 - 13*m.b32 + 0.5*m.x125 + 0.5*m.x128 - m.x142 + m.x145 <= 13)

m.c162 = Constraint(expr=   13*m.b31 + 13*m.b32 + 0.5*m.x125 + 0.5*m.x128 + m.x142 - m.x145 <= 26)

m.c163 = Constraint(expr= - m.x90 + m.x134 - m.x138 <= 0)

m.c164 = Constraint(expr= - m.x90 - m.x134 + m.x138 <= 0)

m.c165 = Constraint(expr= - m.x91 + m.x142 - m.x146 <= 0)

m.c166 = Constraint(expr= - m.x91 - m.x142 + m.x146 <= 0)

m.c167 = Constraint(expr= - 11.31*m.b33 - 11.31*m.b34 + 0.5*m.x116 + 0.5*m.x120 - m.x134 + m.x138 <= 0)

m.c168 = Constraint(expr= - 11.31*m.b33 + 11.31*m.b34 + 0.5*m.x116 + 0.5*m.x120 + m.x134 - m.x138 <= 11.31)

m.c169 = Constraint(expr=   13*m.b33 - 13*m.b34 + 0.5*m.x125 + 0.5*m.x129 - m.x142 + m.x146 <= 13)

m.c170 = Constraint(expr=   13*m.b33 + 13*m.b34 + 0.5*m.x125 + 0.5*m.x129 + m.x142 - m.x146 <= 26)

m.c171 = Constraint(expr= - m.x92 + m.x134 - m.x139 <= 0)

m.c172 = Constraint(expr= - m.x92 - m.x134 + m.x139 <= 0)

m.c173 = Constraint(expr= - m.x93 + m.x142 - m.x147 <= 0)

m.c174 = Constraint(expr= - m.x93 - m.x142 + m.x147 <= 0)

m.c175 = Constraint(expr= - 11.31*m.b35 - 11.31*m.b36 + 0.5*m.x116 + 0.5*m.x121 - m.x134 + m.x139 <= 0)

m.c176 = Constraint(expr= - 11.31*m.b35 + 11.31*m.b36 + 0.5*m.x116 + 0.5*m.x121 + m.x134 - m.x139 <= 11.31)

m.c177 = Constraint(expr=   13*m.b35 - 13*m.b36 + 0.5*m.x125 + 0.5*m.x130 - m.x142 + m.x147 <= 13)

m.c178 = Constraint(expr=   13*m.b35 + 13*m.b36 + 0.5*m.x125 + 0.5*m.x130 + m.x142 - m.x147 <= 26)

m.c179 = Constraint(expr= - m.x94 + m.x135 - m.x136 <= 0)

m.c180 = Constraint(expr= - m.x94 - m.x135 + m.x136 <= 0)

m.c181 = Constraint(expr= - m.x95 + m.x143 - m.x144 <= 0)

m.c182 = Constraint(expr= - m.x95 - m.x143 + m.x144 <= 0)

m.c183 = Constraint(expr= - 11.31*m.b37 - 11.31*m.b38 + 0.5*m.x117 + 0.5*m.x118 - m.x135 + m.x136 <= 0)

m.c184 = Constraint(expr= - 11.31*m.b37 + 11.31*m.b38 + 0.5*m.x117 + 0.5*m.x118 + m.x135 - m.x136 <= 11.31)

m.c185 = Constraint(expr=   13*m.b37 - 13*m.b38 + 0.5*m.x126 + 0.5*m.x127 - m.x143 + m.x144 <= 13)

m.c186 = Constraint(expr=   13*m.b37 + 13*m.b38 + 0.5*m.x126 + 0.5*m.x127 + m.x143 - m.x144 <= 26)

m.c187 = Constraint(expr= - m.x96 + m.x135 - m.x137 <= 0)

m.c188 = Constraint(expr= - m.x96 - m.x135 + m.x137 <= 0)

m.c189 = Constraint(expr= - m.x97 + m.x143 - m.x145 <= 0)

m.c190 = Constraint(expr= - m.x97 - m.x143 + m.x145 <= 0)

m.c191 = Constraint(expr= - 11.31*m.b39 - 11.31*m.b40 + 0.5*m.x117 + 0.5*m.x119 - m.x135 + m.x137 <= 0)

m.c192 = Constraint(expr= - 11.31*m.b39 + 11.31*m.b40 + 0.5*m.x117 + 0.5*m.x119 + m.x135 - m.x137 <= 11.31)

m.c193 = Constraint(expr=   13*m.b39 - 13*m.b40 + 0.5*m.x126 + 0.5*m.x128 - m.x143 + m.x145 <= 13)

m.c194 = Constraint(expr=   13*m.b39 + 13*m.b40 + 0.5*m.x126 + 0.5*m.x128 + m.x143 - m.x145 <= 26)

m.c195 = Constraint(expr= - m.x98 + m.x135 - m.x138 <= 0)

m.c196 = Constraint(expr= - m.x98 - m.x135 + m.x138 <= 0)

m.c197 = Constraint(expr= - m.x99 + m.x143 - m.x146 <= 0)

m.c198 = Constraint(expr= - m.x99 - m.x143 + m.x146 <= 0)

m.c199 = Constraint(expr= - 11.31*m.b41 - 11.31*m.b42 + 0.5*m.x117 + 0.5*m.x120 - m.x135 + m.x138 <= 0)

m.c200 = Constraint(expr= - 11.31*m.b41 + 11.31*m.b42 + 0.5*m.x117 + 0.5*m.x120 + m.x135 - m.x138 <= 11.31)

m.c201 = Constraint(expr=   13*m.b41 - 13*m.b42 + 0.5*m.x126 + 0.5*m.x129 - m.x143 + m.x146 <= 13)

m.c202 = Constraint(expr=   13*m.b41 + 13*m.b42 + 0.5*m.x126 + 0.5*m.x129 + m.x143 - m.x146 <= 26)

m.c203 = Constraint(expr= - m.x100 + m.x135 - m.x139 <= 0)

m.c204 = Constraint(expr= - m.x100 - m.x135 + m.x139 <= 0)

m.c205 = Constraint(expr= - m.x101 + m.x143 - m.x147 <= 0)

m.c206 = Constraint(expr= - m.x101 - m.x143 + m.x147 <= 0)

m.c207 = Constraint(expr= - 11.31*m.b43 - 11.31*m.b44 + 0.5*m.x117 + 0.5*m.x121 - m.x135 + m.x139 <= 0)

m.c208 = Constraint(expr= - 11.31*m.b43 + 11.31*m.b44 + 0.5*m.x117 + 0.5*m.x121 + m.x135 - m.x139 <= 11.31)

m.c209 = Constraint(expr=   13*m.b43 - 13*m.b44 + 0.5*m.x126 + 0.5*m.x130 - m.x143 + m.x147 <= 13)

m.c210 = Constraint(expr=   13*m.b43 + 13*m.b44 + 0.5*m.x126 + 0.5*m.x130 + m.x143 - m.x147 <= 26)

m.c211 = Constraint(expr= - m.x102 + m.x136 - m.x137 <= 0)

m.c212 = Constraint(expr= - m.x102 - m.x136 + m.x137 <= 0)

m.c213 = Constraint(expr= - m.x103 + m.x144 - m.x145 <= 0)

m.c214 = Constraint(expr= - m.x103 - m.x144 + m.x145 <= 0)

m.c215 = Constraint(expr= - 11.31*m.b45 - 11.31*m.b46 + 0.5*m.x118 + 0.5*m.x119 - m.x136 + m.x137 <= 0)

m.c216 = Constraint(expr= - 11.31*m.b45 + 11.31*m.b46 + 0.5*m.x118 + 0.5*m.x119 + m.x136 - m.x137 <= 11.31)

m.c217 = Constraint(expr=   13*m.b45 - 13*m.b46 + 0.5*m.x127 + 0.5*m.x128 - m.x144 + m.x145 <= 13)

m.c218 = Constraint(expr=   13*m.b45 + 13*m.b46 + 0.5*m.x127 + 0.5*m.x128 + m.x144 - m.x145 <= 26)

m.c219 = Constraint(expr= - m.x104 + m.x136 - m.x138 <= 0)

m.c220 = Constraint(expr= - m.x104 - m.x136 + m.x138 <= 0)

m.c221 = Constraint(expr= - m.x105 + m.x144 - m.x146 <= 0)

m.c222 = Constraint(expr= - m.x105 - m.x144 + m.x146 <= 0)

m.c223 = Constraint(expr= - 11.31*m.b47 - 11.31*m.b48 + 0.5*m.x118 + 0.5*m.x120 - m.x136 + m.x138 <= 0)

m.c224 = Constraint(expr= - 11.31*m.b47 + 11.31*m.b48 + 0.5*m.x118 + 0.5*m.x120 + m.x136 - m.x138 <= 11.31)

m.c225 = Constraint(expr=   13*m.b47 - 13*m.b48 + 0.5*m.x127 + 0.5*m.x129 - m.x144 + m.x146 <= 13)

m.c226 = Constraint(expr=   13*m.b47 + 13*m.b48 + 0.5*m.x127 + 0.5*m.x129 + m.x144 - m.x146 <= 26)

m.c227 = Constraint(expr= - m.x106 + m.x136 - m.x139 <= 0)

m.c228 = Constraint(expr= - m.x106 - m.x136 + m.x139 <= 0)

m.c229 = Constraint(expr= - m.x107 + m.x144 - m.x147 <= 0)

m.c230 = Constraint(expr= - m.x107 - m.x144 + m.x147 <= 0)

m.c231 = Constraint(expr= - 11.31*m.b49 - 11.31*m.b50 + 0.5*m.x118 + 0.5*m.x121 - m.x136 + m.x139 <= 0)

m.c232 = Constraint(expr= - 11.31*m.b49 + 11.31*m.b50 + 0.5*m.x118 + 0.5*m.x121 + m.x136 - m.x139 <= 11.31)

m.c233 = Constraint(expr=   13*m.b49 - 13*m.b50 + 0.5*m.x127 + 0.5*m.x130 - m.x144 + m.x147 <= 13)

m.c234 = Constraint(expr=   13*m.b49 + 13*m.b50 + 0.5*m.x127 + 0.5*m.x130 + m.x144 - m.x147 <= 26)

m.c235 = Constraint(expr= - m.x108 + m.x137 - m.x138 <= 0)

m.c236 = Constraint(expr= - m.x108 - m.x137 + m.x138 <= 0)

m.c237 = Constraint(expr= - m.x109 + m.x145 - m.x146 <= 0)

m.c238 = Constraint(expr= - m.x109 - m.x145 + m.x146 <= 0)

m.c239 = Constraint(expr= - 11.31*m.b51 - 11.31*m.b52 + 0.5*m.x119 + 0.5*m.x120 - m.x137 + m.x138 <= 0)

m.c240 = Constraint(expr= - 11.31*m.b51 + 11.31*m.b52 + 0.5*m.x119 + 0.5*m.x120 + m.x137 - m.x138 <= 11.31)

m.c241 = Constraint(expr=   13*m.b51 - 13*m.b52 + 0.5*m.x128 + 0.5*m.x129 - m.x145 + m.x146 <= 13)

m.c242 = Constraint(expr=   13*m.b51 + 13*m.b52 + 0.5*m.x128 + 0.5*m.x129 + m.x145 - m.x146 <= 26)

m.c243 = Constraint(expr= - m.x110 + m.x137 - m.x139 <= 0)

m.c244 = Constraint(expr= - m.x110 - m.x137 + m.x139 <= 0)

m.c245 = Constraint(expr= - m.x111 + m.x145 - m.x147 <= 0)

m.c246 = Constraint(expr= - m.x111 - m.x145 + m.x147 <= 0)

m.c247 = Constraint(expr= - 11.31*m.b53 - 11.31*m.b54 + 0.5*m.x119 + 0.5*m.x121 - m.x137 + m.x139 <= 0)

m.c248 = Constraint(expr= - 11.31*m.b53 + 11.31*m.b54 + 0.5*m.x119 + 0.5*m.x121 + m.x137 - m.x139 <= 11.31)

m.c249 = Constraint(expr=   13*m.b53 - 13*m.b54 + 0.5*m.x128 + 0.5*m.x130 - m.x145 + m.x147 <= 13)

m.c250 = Constraint(expr=   13*m.b53 + 13*m.b54 + 0.5*m.x128 + 0.5*m.x130 + m.x145 - m.x147 <= 26)

m.c251 = Constraint(expr= - m.x112 + m.x138 - m.x139 <= 0)

m.c252 = Constraint(expr= - m.x112 - m.x138 + m.x139 <= 0)

m.c253 = Constraint(expr= - m.x113 + m.x146 - m.x147 <= 0)

m.c254 = Constraint(expr= - m.x113 - m.x146 + m.x147 <= 0)

m.c255 = Constraint(expr= - 11.31*m.b55 - 11.31*m.b56 + 0.5*m.x120 + 0.5*m.x121 - m.x138 + m.x139 <= 0)

m.c256 = Constraint(expr= - 11.31*m.b55 + 11.31*m.b56 + 0.5*m.x120 + 0.5*m.x121 + m.x138 - m.x139 <= 11.31)

m.c257 = Constraint(expr=   13*m.b55 - 13*m.b56 + 0.5*m.x129 + 0.5*m.x130 - m.x146 + m.x147 <= 13)

m.c258 = Constraint(expr=   13*m.b55 + 13*m.b56 + 0.5*m.x129 + 0.5*m.x130 + m.x146 - m.x147 <= 26)

m.c259 = Constraint(expr=16/m.x114 - m.x123 <= 0)

m.c260 = Constraint(expr=16/m.x123 - m.x114 <= 0)

m.c261 = Constraint(expr=16/m.x115 - m.x124 <= 0)

m.c262 = Constraint(expr=16/m.x124 - m.x115 <= 0)

m.c263 = Constraint(expr=16/m.x116 - m.x125 <= 0)

m.c264 = Constraint(expr=16/m.x125 - m.x116 <= 0)

m.c265 = Constraint(expr=36/m.x117 - m.x126 <= 0)

m.c266 = Constraint(expr=36/m.x126 - m.x117 <= 0)

m.c267 = Constraint(expr=36/m.x118 - m.x127 <= 0)

m.c268 = Constraint(expr=36/m.x127 - m.x118 <= 0)

m.c269 = Constraint(expr=9/m.x119 - m.x128 <= 0)

m.c270 = Constraint(expr=9/m.x128 - m.x119 <= 0)

m.c271 = Constraint(expr=9/m.x120 - m.x129 <= 0)

m.c272 = Constraint(expr=9/m.x129 - m.x120 <= 0)

m.c273 = Constraint(expr=9/m.x121 - m.x130 <= 0)

m.c274 = Constraint(expr=9/m.x130 - m.x121 <= 0)

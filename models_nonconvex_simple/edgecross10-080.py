#  MINLP written by GAMS Convert at 08/13/20 17:38:08
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        481        0        1      480        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         91       17       74        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1529     1441       88        0


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
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x91, sense=minimize)

m.c1 = Constraint(expr= - m.b1 + m.b2 + m.b3 <= 1)

m.c2 = Constraint(expr=   m.b3 - m.b4 + m.b5 <= 1)

m.c3 = Constraint(expr=   m.b3 - m.b6 + m.b7 <= 1)

m.c4 = Constraint(expr=   m.b3 - m.b8 + m.b9 <= 1)

m.c5 = Constraint(expr=   m.b3 - m.b10 + m.b11 <= 1)

m.c6 = Constraint(expr=   m.b3 - m.b12 + m.b13 <= 1)

m.c7 = Constraint(expr=   m.b3 - m.b14 + m.b15 <= 1)

m.c8 = Constraint(expr=   m.b3 - m.b16 + m.b17 <= 1)

m.c9 = Constraint(expr=   m.b1 - m.b4 + m.b18 <= 1)

m.c10 = Constraint(expr=   m.b1 - m.b6 + m.b19 <= 1)

m.c11 = Constraint(expr=   m.b1 - m.b8 + m.b20 <= 1)

m.c12 = Constraint(expr=   m.b1 - m.b10 + m.b21 <= 1)

m.c13 = Constraint(expr=   m.b1 - m.b12 + m.b22 <= 1)

m.c14 = Constraint(expr=   m.b1 - m.b14 + m.b23 <= 1)

m.c15 = Constraint(expr=   m.b1 - m.b16 + m.b24 <= 1)

m.c16 = Constraint(expr=   m.b4 - m.b6 + m.b25 <= 1)

m.c17 = Constraint(expr=   m.b4 - m.b8 + m.b26 <= 1)

m.c18 = Constraint(expr=   m.b4 - m.b10 + m.b27 <= 1)

m.c19 = Constraint(expr=   m.b4 - m.b12 + m.b28 <= 1)

m.c20 = Constraint(expr=   m.b4 - m.b14 + m.b29 <= 1)

m.c21 = Constraint(expr=   m.b4 - m.b16 + m.b30 <= 1)

m.c22 = Constraint(expr=   m.b6 - m.b8 + m.b31 <= 1)

m.c23 = Constraint(expr=   m.b6 - m.b10 + m.b32 <= 1)

m.c24 = Constraint(expr=   m.b6 - m.b12 + m.b33 <= 1)

m.c25 = Constraint(expr=   m.b6 - m.b14 + m.b34 <= 1)

m.c26 = Constraint(expr=   m.b6 - m.b16 + m.b35 <= 1)

m.c27 = Constraint(expr=   m.b8 - m.b10 + m.b36 <= 1)

m.c28 = Constraint(expr=   m.b8 - m.b12 + m.b37 <= 1)

m.c29 = Constraint(expr=   m.b8 - m.b14 + m.b38 <= 1)

m.c30 = Constraint(expr=   m.b8 - m.b16 + m.b39 <= 1)

m.c31 = Constraint(expr=   m.b10 - m.b12 + m.b40 <= 1)

m.c32 = Constraint(expr=   m.b10 - m.b14 + m.b41 <= 1)

m.c33 = Constraint(expr=   m.b10 - m.b16 + m.b42 <= 1)

m.c34 = Constraint(expr=   m.b12 - m.b14 + m.b43 <= 1)

m.c35 = Constraint(expr=   m.b12 - m.b16 + m.b44 <= 1)

m.c36 = Constraint(expr=   m.b14 - m.b16 + m.b45 <= 1)

m.c37 = Constraint(expr=   m.b2 - m.b5 + m.b18 <= 1)

m.c38 = Constraint(expr=   m.b2 - m.b7 + m.b19 <= 1)

m.c39 = Constraint(expr=   m.b2 - m.b9 + m.b20 <= 1)

m.c40 = Constraint(expr=   m.b2 - m.b11 + m.b21 <= 1)

m.c41 = Constraint(expr=   m.b2 - m.b13 + m.b22 <= 1)

m.c42 = Constraint(expr=   m.b2 - m.b15 + m.b23 <= 1)

m.c43 = Constraint(expr=   m.b2 - m.b17 + m.b24 <= 1)

m.c44 = Constraint(expr=   m.b5 - m.b7 + m.b25 <= 1)

m.c45 = Constraint(expr=   m.b5 - m.b9 + m.b26 <= 1)

m.c46 = Constraint(expr=   m.b5 - m.b11 + m.b27 <= 1)

m.c47 = Constraint(expr=   m.b5 - m.b13 + m.b28 <= 1)

m.c48 = Constraint(expr=   m.b5 - m.b15 + m.b29 <= 1)

m.c49 = Constraint(expr=   m.b5 - m.b17 + m.b30 <= 1)

m.c50 = Constraint(expr=   m.b7 - m.b9 + m.b31 <= 1)

m.c51 = Constraint(expr=   m.b7 - m.b11 + m.b32 <= 1)

m.c52 = Constraint(expr=   m.b7 - m.b13 + m.b33 <= 1)

m.c53 = Constraint(expr=   m.b7 - m.b15 + m.b34 <= 1)

m.c54 = Constraint(expr=   m.b7 - m.b17 + m.b35 <= 1)

m.c55 = Constraint(expr=   m.b9 - m.b11 + m.b36 <= 1)

m.c56 = Constraint(expr=   m.b9 - m.b13 + m.b37 <= 1)

m.c57 = Constraint(expr=   m.b9 - m.b15 + m.b38 <= 1)

m.c58 = Constraint(expr=   m.b9 - m.b17 + m.b39 <= 1)

m.c59 = Constraint(expr=   m.b11 - m.b13 + m.b40 <= 1)

m.c60 = Constraint(expr=   m.b11 - m.b15 + m.b41 <= 1)

m.c61 = Constraint(expr=   m.b11 - m.b17 + m.b42 <= 1)

m.c62 = Constraint(expr=   m.b13 - m.b15 + m.b43 <= 1)

m.c63 = Constraint(expr=   m.b13 - m.b17 + m.b44 <= 1)

m.c64 = Constraint(expr=   m.b15 - m.b17 + m.b45 <= 1)

m.c65 = Constraint(expr=   m.b18 - m.b19 + m.b25 <= 1)

m.c66 = Constraint(expr=   m.b18 - m.b20 + m.b26 <= 1)

m.c67 = Constraint(expr=   m.b18 - m.b21 + m.b27 <= 1)

m.c68 = Constraint(expr=   m.b18 - m.b22 + m.b28 <= 1)

m.c69 = Constraint(expr=   m.b18 - m.b23 + m.b29 <= 1)

m.c70 = Constraint(expr=   m.b18 - m.b24 + m.b30 <= 1)

m.c71 = Constraint(expr=   m.b19 - m.b20 + m.b31 <= 1)

m.c72 = Constraint(expr=   m.b19 - m.b21 + m.b32 <= 1)

m.c73 = Constraint(expr=   m.b19 - m.b22 + m.b33 <= 1)

m.c74 = Constraint(expr=   m.b19 - m.b23 + m.b34 <= 1)

m.c75 = Constraint(expr=   m.b19 - m.b24 + m.b35 <= 1)

m.c76 = Constraint(expr=   m.b20 - m.b21 + m.b36 <= 1)

m.c77 = Constraint(expr=   m.b20 - m.b22 + m.b37 <= 1)

m.c78 = Constraint(expr=   m.b20 - m.b23 + m.b38 <= 1)

m.c79 = Constraint(expr=   m.b20 - m.b24 + m.b39 <= 1)

m.c80 = Constraint(expr=   m.b21 - m.b22 + m.b40 <= 1)

m.c81 = Constraint(expr=   m.b21 - m.b23 + m.b41 <= 1)

m.c82 = Constraint(expr=   m.b21 - m.b24 + m.b42 <= 1)

m.c83 = Constraint(expr=   m.b22 - m.b23 + m.b43 <= 1)

m.c84 = Constraint(expr=   m.b22 - m.b24 + m.b44 <= 1)

m.c85 = Constraint(expr=   m.b23 - m.b24 + m.b45 <= 1)

m.c86 = Constraint(expr=   m.b25 - m.b26 + m.b31 <= 1)

m.c87 = Constraint(expr=   m.b25 - m.b27 + m.b32 <= 1)

m.c88 = Constraint(expr=   m.b25 - m.b28 + m.b33 <= 1)

m.c89 = Constraint(expr=   m.b25 - m.b29 + m.b34 <= 1)

m.c90 = Constraint(expr=   m.b25 - m.b30 + m.b35 <= 1)

m.c91 = Constraint(expr=   m.b26 - m.b27 + m.b36 <= 1)

m.c92 = Constraint(expr=   m.b26 - m.b28 + m.b37 <= 1)

m.c93 = Constraint(expr=   m.b26 - m.b29 + m.b38 <= 1)

m.c94 = Constraint(expr=   m.b26 - m.b30 + m.b39 <= 1)

m.c95 = Constraint(expr=   m.b27 - m.b28 + m.b40 <= 1)

m.c96 = Constraint(expr=   m.b27 - m.b29 + m.b41 <= 1)

m.c97 = Constraint(expr=   m.b27 - m.b30 + m.b42 <= 1)

m.c98 = Constraint(expr=   m.b28 - m.b29 + m.b43 <= 1)

m.c99 = Constraint(expr=   m.b28 - m.b30 + m.b44 <= 1)

m.c100 = Constraint(expr=   m.b29 - m.b30 + m.b45 <= 1)

m.c101 = Constraint(expr=   m.b31 - m.b32 + m.b36 <= 1)

m.c102 = Constraint(expr=   m.b31 - m.b33 + m.b37 <= 1)

m.c103 = Constraint(expr=   m.b31 - m.b34 + m.b38 <= 1)

m.c104 = Constraint(expr=   m.b31 - m.b35 + m.b39 <= 1)

m.c105 = Constraint(expr=   m.b32 - m.b33 + m.b40 <= 1)

m.c106 = Constraint(expr=   m.b32 - m.b34 + m.b41 <= 1)

m.c107 = Constraint(expr=   m.b32 - m.b35 + m.b42 <= 1)

m.c108 = Constraint(expr=   m.b33 - m.b34 + m.b43 <= 1)

m.c109 = Constraint(expr=   m.b33 - m.b35 + m.b44 <= 1)

m.c110 = Constraint(expr=   m.b34 - m.b35 + m.b45 <= 1)

m.c111 = Constraint(expr=   m.b36 - m.b37 + m.b40 <= 1)

m.c112 = Constraint(expr=   m.b36 - m.b38 + m.b41 <= 1)

m.c113 = Constraint(expr=   m.b36 - m.b39 + m.b42 <= 1)

m.c114 = Constraint(expr=   m.b37 - m.b38 + m.b43 <= 1)

m.c115 = Constraint(expr=   m.b37 - m.b39 + m.b44 <= 1)

m.c116 = Constraint(expr=   m.b38 - m.b39 + m.b45 <= 1)

m.c117 = Constraint(expr=   m.b40 - m.b41 + m.b43 <= 1)

m.c118 = Constraint(expr=   m.b40 - m.b42 + m.b44 <= 1)

m.c119 = Constraint(expr=   m.b41 - m.b42 + m.b45 <= 1)

m.c120 = Constraint(expr=   m.b43 - m.b44 + m.b45 <= 1)

m.c121 = Constraint(expr=   m.b1 - m.b2 - m.b3 <= 0)

m.c122 = Constraint(expr= - m.b3 + m.b4 - m.b5 <= 0)

m.c123 = Constraint(expr= - m.b3 + m.b6 - m.b7 <= 0)

m.c124 = Constraint(expr= - m.b3 + m.b8 - m.b9 <= 0)

m.c125 = Constraint(expr= - m.b3 + m.b10 - m.b11 <= 0)

m.c126 = Constraint(expr= - m.b3 + m.b12 - m.b13 <= 0)

m.c127 = Constraint(expr= - m.b3 + m.b14 - m.b15 <= 0)

m.c128 = Constraint(expr= - m.b3 + m.b16 - m.b17 <= 0)

m.c129 = Constraint(expr= - m.b1 + m.b4 - m.b18 <= 0)

m.c130 = Constraint(expr= - m.b1 + m.b6 - m.b19 <= 0)

m.c131 = Constraint(expr= - m.b1 + m.b8 - m.b20 <= 0)

m.c132 = Constraint(expr= - m.b1 + m.b10 - m.b21 <= 0)

m.c133 = Constraint(expr= - m.b1 + m.b12 - m.b22 <= 0)

m.c134 = Constraint(expr= - m.b1 + m.b14 - m.b23 <= 0)

m.c135 = Constraint(expr= - m.b1 + m.b16 - m.b24 <= 0)

m.c136 = Constraint(expr= - m.b4 + m.b6 - m.b25 <= 0)

m.c137 = Constraint(expr= - m.b4 + m.b8 - m.b26 <= 0)

m.c138 = Constraint(expr= - m.b4 + m.b10 - m.b27 <= 0)

m.c139 = Constraint(expr= - m.b4 + m.b12 - m.b28 <= 0)

m.c140 = Constraint(expr= - m.b4 + m.b14 - m.b29 <= 0)

m.c141 = Constraint(expr= - m.b4 + m.b16 - m.b30 <= 0)

m.c142 = Constraint(expr= - m.b6 + m.b8 - m.b31 <= 0)

m.c143 = Constraint(expr= - m.b6 + m.b10 - m.b32 <= 0)

m.c144 = Constraint(expr= - m.b6 + m.b12 - m.b33 <= 0)

m.c145 = Constraint(expr= - m.b6 + m.b14 - m.b34 <= 0)

m.c146 = Constraint(expr= - m.b6 + m.b16 - m.b35 <= 0)

m.c147 = Constraint(expr= - m.b8 + m.b10 - m.b36 <= 0)

m.c148 = Constraint(expr= - m.b8 + m.b12 - m.b37 <= 0)

m.c149 = Constraint(expr= - m.b8 + m.b14 - m.b38 <= 0)

m.c150 = Constraint(expr= - m.b8 + m.b16 - m.b39 <= 0)

m.c151 = Constraint(expr= - m.b10 + m.b12 - m.b40 <= 0)

m.c152 = Constraint(expr= - m.b10 + m.b14 - m.b41 <= 0)

m.c153 = Constraint(expr= - m.b10 + m.b16 - m.b42 <= 0)

m.c154 = Constraint(expr= - m.b12 + m.b14 - m.b43 <= 0)

m.c155 = Constraint(expr= - m.b12 + m.b16 - m.b44 <= 0)

m.c156 = Constraint(expr= - m.b14 + m.b16 - m.b45 <= 0)

m.c157 = Constraint(expr= - m.b2 + m.b5 - m.b18 <= 0)

m.c158 = Constraint(expr= - m.b2 + m.b7 - m.b19 <= 0)

m.c159 = Constraint(expr= - m.b2 + m.b9 - m.b20 <= 0)

m.c160 = Constraint(expr= - m.b2 + m.b11 - m.b21 <= 0)

m.c161 = Constraint(expr= - m.b2 + m.b13 - m.b22 <= 0)

m.c162 = Constraint(expr= - m.b2 + m.b15 - m.b23 <= 0)

m.c163 = Constraint(expr= - m.b2 + m.b17 - m.b24 <= 0)

m.c164 = Constraint(expr= - m.b5 + m.b7 - m.b25 <= 0)

m.c165 = Constraint(expr= - m.b5 + m.b9 - m.b26 <= 0)

m.c166 = Constraint(expr= - m.b5 + m.b11 - m.b27 <= 0)

m.c167 = Constraint(expr= - m.b5 + m.b13 - m.b28 <= 0)

m.c168 = Constraint(expr= - m.b5 + m.b15 - m.b29 <= 0)

m.c169 = Constraint(expr= - m.b5 + m.b17 - m.b30 <= 0)

m.c170 = Constraint(expr= - m.b7 + m.b9 - m.b31 <= 0)

m.c171 = Constraint(expr= - m.b7 + m.b11 - m.b32 <= 0)

m.c172 = Constraint(expr= - m.b7 + m.b13 - m.b33 <= 0)

m.c173 = Constraint(expr= - m.b7 + m.b15 - m.b34 <= 0)

m.c174 = Constraint(expr= - m.b7 + m.b17 - m.b35 <= 0)

m.c175 = Constraint(expr= - m.b9 + m.b11 - m.b36 <= 0)

m.c176 = Constraint(expr= - m.b9 + m.b13 - m.b37 <= 0)

m.c177 = Constraint(expr= - m.b9 + m.b15 - m.b38 <= 0)

m.c178 = Constraint(expr= - m.b9 + m.b17 - m.b39 <= 0)

m.c179 = Constraint(expr= - m.b11 + m.b13 - m.b40 <= 0)

m.c180 = Constraint(expr= - m.b11 + m.b15 - m.b41 <= 0)

m.c181 = Constraint(expr= - m.b11 + m.b17 - m.b42 <= 0)

m.c182 = Constraint(expr= - m.b13 + m.b15 - m.b43 <= 0)

m.c183 = Constraint(expr= - m.b13 + m.b17 - m.b44 <= 0)

m.c184 = Constraint(expr= - m.b15 + m.b17 - m.b45 <= 0)

m.c185 = Constraint(expr= - m.b18 + m.b19 - m.b25 <= 0)

m.c186 = Constraint(expr= - m.b18 + m.b20 - m.b26 <= 0)

m.c187 = Constraint(expr= - m.b18 + m.b21 - m.b27 <= 0)

m.c188 = Constraint(expr= - m.b18 + m.b22 - m.b28 <= 0)

m.c189 = Constraint(expr= - m.b18 + m.b23 - m.b29 <= 0)

m.c190 = Constraint(expr= - m.b18 + m.b24 - m.b30 <= 0)

m.c191 = Constraint(expr= - m.b19 + m.b20 - m.b31 <= 0)

m.c192 = Constraint(expr= - m.b19 + m.b21 - m.b32 <= 0)

m.c193 = Constraint(expr= - m.b19 + m.b22 - m.b33 <= 0)

m.c194 = Constraint(expr= - m.b19 + m.b23 - m.b34 <= 0)

m.c195 = Constraint(expr= - m.b19 + m.b24 - m.b35 <= 0)

m.c196 = Constraint(expr= - m.b20 + m.b21 - m.b36 <= 0)

m.c197 = Constraint(expr= - m.b20 + m.b22 - m.b37 <= 0)

m.c198 = Constraint(expr= - m.b20 + m.b23 - m.b38 <= 0)

m.c199 = Constraint(expr= - m.b20 + m.b24 - m.b39 <= 0)

m.c200 = Constraint(expr= - m.b21 + m.b22 - m.b40 <= 0)

m.c201 = Constraint(expr= - m.b21 + m.b23 - m.b41 <= 0)

m.c202 = Constraint(expr= - m.b21 + m.b24 - m.b42 <= 0)

m.c203 = Constraint(expr= - m.b22 + m.b23 - m.b43 <= 0)

m.c204 = Constraint(expr= - m.b22 + m.b24 - m.b44 <= 0)

m.c205 = Constraint(expr= - m.b23 + m.b24 - m.b45 <= 0)

m.c206 = Constraint(expr= - m.b25 + m.b26 - m.b31 <= 0)

m.c207 = Constraint(expr= - m.b25 + m.b27 - m.b32 <= 0)

m.c208 = Constraint(expr= - m.b25 + m.b28 - m.b33 <= 0)

m.c209 = Constraint(expr= - m.b25 + m.b29 - m.b34 <= 0)

m.c210 = Constraint(expr= - m.b25 + m.b30 - m.b35 <= 0)

m.c211 = Constraint(expr= - m.b26 + m.b27 - m.b36 <= 0)

m.c212 = Constraint(expr= - m.b26 + m.b28 - m.b37 <= 0)

m.c213 = Constraint(expr= - m.b26 + m.b29 - m.b38 <= 0)

m.c214 = Constraint(expr= - m.b26 + m.b30 - m.b39 <= 0)

m.c215 = Constraint(expr= - m.b27 + m.b28 - m.b40 <= 0)

m.c216 = Constraint(expr= - m.b27 + m.b29 - m.b41 <= 0)

m.c217 = Constraint(expr= - m.b27 + m.b30 - m.b42 <= 0)

m.c218 = Constraint(expr= - m.b28 + m.b29 - m.b43 <= 0)

m.c219 = Constraint(expr= - m.b28 + m.b30 - m.b44 <= 0)

m.c220 = Constraint(expr= - m.b29 + m.b30 - m.b45 <= 0)

m.c221 = Constraint(expr= - m.b31 + m.b32 - m.b36 <= 0)

m.c222 = Constraint(expr= - m.b31 + m.b33 - m.b37 <= 0)

m.c223 = Constraint(expr= - m.b31 + m.b34 - m.b38 <= 0)

m.c224 = Constraint(expr= - m.b31 + m.b35 - m.b39 <= 0)

m.c225 = Constraint(expr= - m.b32 + m.b33 - m.b40 <= 0)

m.c226 = Constraint(expr= - m.b32 + m.b34 - m.b41 <= 0)

m.c227 = Constraint(expr= - m.b32 + m.b35 - m.b42 <= 0)

m.c228 = Constraint(expr= - m.b33 + m.b34 - m.b43 <= 0)

m.c229 = Constraint(expr= - m.b33 + m.b35 - m.b44 <= 0)

m.c230 = Constraint(expr= - m.b34 + m.b35 - m.b45 <= 0)

m.c231 = Constraint(expr= - m.b36 + m.b37 - m.b40 <= 0)

m.c232 = Constraint(expr= - m.b36 + m.b38 - m.b41 <= 0)

m.c233 = Constraint(expr= - m.b36 + m.b39 - m.b42 <= 0)

m.c234 = Constraint(expr= - m.b37 + m.b38 - m.b43 <= 0)

m.c235 = Constraint(expr= - m.b37 + m.b39 - m.b44 <= 0)

m.c236 = Constraint(expr= - m.b38 + m.b39 - m.b45 <= 0)

m.c237 = Constraint(expr= - m.b40 + m.b41 - m.b43 <= 0)

m.c238 = Constraint(expr= - m.b40 + m.b42 - m.b44 <= 0)

m.c239 = Constraint(expr= - m.b41 + m.b42 - m.b45 <= 0)

m.c240 = Constraint(expr= - m.b43 + m.b44 - m.b45 <= 0)

m.c241 = Constraint(expr= - m.b46 + m.b47 + m.b48 <= 1)

m.c242 = Constraint(expr=   m.b48 - m.b49 + m.b50 <= 1)

m.c243 = Constraint(expr=   m.b48 - m.b51 + m.b52 <= 1)

m.c244 = Constraint(expr=   m.b48 - m.b53 + m.b54 <= 1)

m.c245 = Constraint(expr=   m.b48 - m.b55 + m.b56 <= 1)

m.c246 = Constraint(expr=   m.b48 - m.b57 + m.b58 <= 1)

m.c247 = Constraint(expr=   m.b48 - m.b59 + m.b60 <= 1)

m.c248 = Constraint(expr=   m.b48 - m.b61 + m.b62 <= 1)

m.c249 = Constraint(expr=   m.b46 - m.b49 + m.b63 <= 1)

m.c250 = Constraint(expr=   m.b46 - m.b51 + m.b64 <= 1)

m.c251 = Constraint(expr=   m.b46 - m.b53 + m.b65 <= 1)

m.c252 = Constraint(expr=   m.b46 - m.b55 + m.b66 <= 1)

m.c253 = Constraint(expr=   m.b46 - m.b57 + m.b67 <= 1)

m.c254 = Constraint(expr=   m.b46 - m.b59 + m.b68 <= 1)

m.c255 = Constraint(expr=   m.b46 - m.b61 + m.b69 <= 1)

m.c256 = Constraint(expr=   m.b49 - m.b51 + m.b70 <= 1)

m.c257 = Constraint(expr=   m.b49 - m.b53 + m.b71 <= 1)

m.c258 = Constraint(expr=   m.b49 - m.b55 + m.b72 <= 1)

m.c259 = Constraint(expr=   m.b49 - m.b57 + m.b73 <= 1)

m.c260 = Constraint(expr=   m.b49 - m.b59 + m.b74 <= 1)

m.c261 = Constraint(expr=   m.b49 - m.b61 + m.x75 <= 1)

m.c262 = Constraint(expr=   m.b51 - m.b53 + m.x76 <= 1)

m.c263 = Constraint(expr=   m.b51 - m.b55 + m.x77 <= 1)

m.c264 = Constraint(expr=   m.b51 - m.b57 + m.x78 <= 1)

m.c265 = Constraint(expr=   m.b51 - m.b59 + m.x79 <= 1)

m.c266 = Constraint(expr=   m.b51 - m.b61 + m.x80 <= 1)

m.c267 = Constraint(expr=   m.b53 - m.b55 + m.x81 <= 1)

m.c268 = Constraint(expr=   m.b53 - m.b57 + m.x82 <= 1)

m.c269 = Constraint(expr=   m.b53 - m.b59 + m.x83 <= 1)

m.c270 = Constraint(expr=   m.b53 - m.b61 + m.x84 <= 1)

m.c271 = Constraint(expr=   m.b55 - m.b57 + m.x85 <= 1)

m.c272 = Constraint(expr=   m.b55 - m.b59 + m.x86 <= 1)

m.c273 = Constraint(expr=   m.b55 - m.b61 + m.x87 <= 1)

m.c274 = Constraint(expr=   m.b57 - m.b59 + m.x88 <= 1)

m.c275 = Constraint(expr=   m.b57 - m.b61 + m.x89 <= 1)

m.c276 = Constraint(expr=   m.b59 - m.b61 + m.x90 <= 1)

m.c277 = Constraint(expr=   m.b47 - m.b50 + m.b63 <= 1)

m.c278 = Constraint(expr=   m.b47 - m.b52 + m.b64 <= 1)

m.c279 = Constraint(expr=   m.b47 - m.b54 + m.b65 <= 1)

m.c280 = Constraint(expr=   m.b47 - m.b56 + m.b66 <= 1)

m.c281 = Constraint(expr=   m.b47 - m.b58 + m.b67 <= 1)

m.c282 = Constraint(expr=   m.b47 - m.b60 + m.b68 <= 1)

m.c283 = Constraint(expr=   m.b47 - m.b62 + m.b69 <= 1)

m.c284 = Constraint(expr=   m.b50 - m.b52 + m.b70 <= 1)

m.c285 = Constraint(expr=   m.b50 - m.b54 + m.b71 <= 1)

m.c286 = Constraint(expr=   m.b50 - m.b56 + m.b72 <= 1)

m.c287 = Constraint(expr=   m.b50 - m.b58 + m.b73 <= 1)

m.c288 = Constraint(expr=   m.b50 - m.b60 + m.b74 <= 1)

m.c289 = Constraint(expr=   m.b50 - m.b62 + m.x75 <= 1)

m.c290 = Constraint(expr=   m.b52 - m.b54 + m.x76 <= 1)

m.c291 = Constraint(expr=   m.b52 - m.b56 + m.x77 <= 1)

m.c292 = Constraint(expr=   m.b52 - m.b58 + m.x78 <= 1)

m.c293 = Constraint(expr=   m.b52 - m.b60 + m.x79 <= 1)

m.c294 = Constraint(expr=   m.b52 - m.b62 + m.x80 <= 1)

m.c295 = Constraint(expr=   m.b54 - m.b56 + m.x81 <= 1)

m.c296 = Constraint(expr=   m.b54 - m.b58 + m.x82 <= 1)

m.c297 = Constraint(expr=   m.b54 - m.b60 + m.x83 <= 1)

m.c298 = Constraint(expr=   m.b54 - m.b62 + m.x84 <= 1)

m.c299 = Constraint(expr=   m.b56 - m.b58 + m.x85 <= 1)

m.c300 = Constraint(expr=   m.b56 - m.b60 + m.x86 <= 1)

m.c301 = Constraint(expr=   m.b56 - m.b62 + m.x87 <= 1)

m.c302 = Constraint(expr=   m.b58 - m.b60 + m.x88 <= 1)

m.c303 = Constraint(expr=   m.b58 - m.b62 + m.x89 <= 1)

m.c304 = Constraint(expr=   m.b60 - m.b62 + m.x90 <= 1)

m.c305 = Constraint(expr=   m.b63 - m.b64 + m.b70 <= 1)

m.c306 = Constraint(expr=   m.b63 - m.b65 + m.b71 <= 1)

m.c307 = Constraint(expr=   m.b63 - m.b66 + m.b72 <= 1)

m.c308 = Constraint(expr=   m.b63 - m.b67 + m.b73 <= 1)

m.c309 = Constraint(expr=   m.b63 - m.b68 + m.b74 <= 1)

m.c310 = Constraint(expr=   m.b63 - m.b69 + m.x75 <= 1)

m.c311 = Constraint(expr=   m.b64 - m.b65 + m.x76 <= 1)

m.c312 = Constraint(expr=   m.b64 - m.b66 + m.x77 <= 1)

m.c313 = Constraint(expr=   m.b64 - m.b67 + m.x78 <= 1)

m.c314 = Constraint(expr=   m.b64 - m.b68 + m.x79 <= 1)

m.c315 = Constraint(expr=   m.b64 - m.b69 + m.x80 <= 1)

m.c316 = Constraint(expr=   m.b65 - m.b66 + m.x81 <= 1)

m.c317 = Constraint(expr=   m.b65 - m.b67 + m.x82 <= 1)

m.c318 = Constraint(expr=   m.b65 - m.b68 + m.x83 <= 1)

m.c319 = Constraint(expr=   m.b65 - m.b69 + m.x84 <= 1)

m.c320 = Constraint(expr=   m.b66 - m.b67 + m.x85 <= 1)

m.c321 = Constraint(expr=   m.b66 - m.b68 + m.x86 <= 1)

m.c322 = Constraint(expr=   m.b66 - m.b69 + m.x87 <= 1)

m.c323 = Constraint(expr=   m.b67 - m.b68 + m.x88 <= 1)

m.c324 = Constraint(expr=   m.b67 - m.b69 + m.x89 <= 1)

m.c325 = Constraint(expr=   m.b68 - m.b69 + m.x90 <= 1)

m.c326 = Constraint(expr=   m.b70 - m.b71 + m.x76 <= 1)

m.c327 = Constraint(expr=   m.b70 - m.b72 + m.x77 <= 1)

m.c328 = Constraint(expr=   m.b70 - m.b73 + m.x78 <= 1)

m.c329 = Constraint(expr=   m.b70 - m.b74 + m.x79 <= 1)

m.c330 = Constraint(expr=   m.b70 - m.x75 + m.x80 <= 1)

m.c331 = Constraint(expr=   m.b71 - m.b72 + m.x81 <= 1)

m.c332 = Constraint(expr=   m.b71 - m.b73 + m.x82 <= 1)

m.c333 = Constraint(expr=   m.b71 - m.b74 + m.x83 <= 1)

m.c334 = Constraint(expr=   m.b71 - m.x75 + m.x84 <= 1)

m.c335 = Constraint(expr=   m.b72 - m.b73 + m.x85 <= 1)

m.c336 = Constraint(expr=   m.b72 - m.b74 + m.x86 <= 1)

m.c337 = Constraint(expr=   m.b72 - m.x75 + m.x87 <= 1)

m.c338 = Constraint(expr=   m.b73 - m.b74 + m.x88 <= 1)

m.c339 = Constraint(expr=   m.b73 - m.x75 + m.x89 <= 1)

m.c340 = Constraint(expr=   m.b74 - m.x75 + m.x90 <= 1)

m.c341 = Constraint(expr=   m.x76 - m.x77 + m.x81 <= 1)

m.c342 = Constraint(expr=   m.x76 - m.x78 + m.x82 <= 1)

m.c343 = Constraint(expr=   m.x76 - m.x79 + m.x83 <= 1)

m.c344 = Constraint(expr=   m.x76 - m.x80 + m.x84 <= 1)

m.c345 = Constraint(expr=   m.x77 - m.x78 + m.x85 <= 1)

m.c346 = Constraint(expr=   m.x77 - m.x79 + m.x86 <= 1)

m.c347 = Constraint(expr=   m.x77 - m.x80 + m.x87 <= 1)

m.c348 = Constraint(expr=   m.x78 - m.x79 + m.x88 <= 1)

m.c349 = Constraint(expr=   m.x78 - m.x80 + m.x89 <= 1)

m.c350 = Constraint(expr=   m.x79 - m.x80 + m.x90 <= 1)

m.c351 = Constraint(expr=   m.x81 - m.x82 + m.x85 <= 1)

m.c352 = Constraint(expr=   m.x81 - m.x83 + m.x86 <= 1)

m.c353 = Constraint(expr=   m.x81 - m.x84 + m.x87 <= 1)

m.c354 = Constraint(expr=   m.x82 - m.x83 + m.x88 <= 1)

m.c355 = Constraint(expr=   m.x82 - m.x84 + m.x89 <= 1)

m.c356 = Constraint(expr=   m.x83 - m.x84 + m.x90 <= 1)

m.c357 = Constraint(expr=   m.x85 - m.x86 + m.x88 <= 1)

m.c358 = Constraint(expr=   m.x85 - m.x87 + m.x89 <= 1)

m.c359 = Constraint(expr=   m.x86 - m.x87 + m.x90 <= 1)

m.c360 = Constraint(expr=   m.x88 - m.x89 + m.x90 <= 1)

m.c361 = Constraint(expr=   m.b46 - m.b47 - m.b48 <= 0)

m.c362 = Constraint(expr= - m.b48 + m.b49 - m.b50 <= 0)

m.c363 = Constraint(expr= - m.b48 + m.b51 - m.b52 <= 0)

m.c364 = Constraint(expr= - m.b48 + m.b53 - m.b54 <= 0)

m.c365 = Constraint(expr= - m.b48 + m.b55 - m.b56 <= 0)

m.c366 = Constraint(expr= - m.b48 + m.b57 - m.b58 <= 0)

m.c367 = Constraint(expr= - m.b48 + m.b59 - m.b60 <= 0)

m.c368 = Constraint(expr= - m.b48 + m.b61 - m.b62 <= 0)

m.c369 = Constraint(expr= - m.b46 + m.b49 - m.b63 <= 0)

m.c370 = Constraint(expr= - m.b46 + m.b51 - m.b64 <= 0)

m.c371 = Constraint(expr= - m.b46 + m.b53 - m.b65 <= 0)

m.c372 = Constraint(expr= - m.b46 + m.b55 - m.b66 <= 0)

m.c373 = Constraint(expr= - m.b46 + m.b57 - m.b67 <= 0)

m.c374 = Constraint(expr= - m.b46 + m.b59 - m.b68 <= 0)

m.c375 = Constraint(expr= - m.b46 + m.b61 - m.b69 <= 0)

m.c376 = Constraint(expr= - m.b49 + m.b51 - m.b70 <= 0)

m.c377 = Constraint(expr= - m.b49 + m.b53 - m.b71 <= 0)

m.c378 = Constraint(expr= - m.b49 + m.b55 - m.b72 <= 0)

m.c379 = Constraint(expr= - m.b49 + m.b57 - m.b73 <= 0)

m.c380 = Constraint(expr= - m.b49 + m.b59 - m.b74 <= 0)

m.c381 = Constraint(expr= - m.b49 + m.b61 - m.x75 <= 0)

m.c382 = Constraint(expr= - m.b51 + m.b53 - m.x76 <= 0)

m.c383 = Constraint(expr= - m.b51 + m.b55 - m.x77 <= 0)

m.c384 = Constraint(expr= - m.b51 + m.b57 - m.x78 <= 0)

m.c385 = Constraint(expr= - m.b51 + m.b59 - m.x79 <= 0)

m.c386 = Constraint(expr= - m.b51 + m.b61 - m.x80 <= 0)

m.c387 = Constraint(expr= - m.b53 + m.b55 - m.x81 <= 0)

m.c388 = Constraint(expr= - m.b53 + m.b57 - m.x82 <= 0)

m.c389 = Constraint(expr= - m.b53 + m.b59 - m.x83 <= 0)

m.c390 = Constraint(expr= - m.b53 + m.b61 - m.x84 <= 0)

m.c391 = Constraint(expr= - m.b55 + m.b57 - m.x85 <= 0)

m.c392 = Constraint(expr= - m.b55 + m.b59 - m.x86 <= 0)

m.c393 = Constraint(expr= - m.b55 + m.b61 - m.x87 <= 0)

m.c394 = Constraint(expr= - m.b57 + m.b59 - m.x88 <= 0)

m.c395 = Constraint(expr= - m.b57 + m.b61 - m.x89 <= 0)

m.c396 = Constraint(expr= - m.b59 + m.b61 - m.x90 <= 0)

m.c397 = Constraint(expr= - m.b47 + m.b50 - m.b63 <= 0)

m.c398 = Constraint(expr= - m.b47 + m.b52 - m.b64 <= 0)

m.c399 = Constraint(expr= - m.b47 + m.b54 - m.b65 <= 0)

m.c400 = Constraint(expr= - m.b47 + m.b56 - m.b66 <= 0)

m.c401 = Constraint(expr= - m.b47 + m.b58 - m.b67 <= 0)

m.c402 = Constraint(expr= - m.b47 + m.b60 - m.b68 <= 0)

m.c403 = Constraint(expr= - m.b47 + m.b62 - m.b69 <= 0)

m.c404 = Constraint(expr= - m.b50 + m.b52 - m.b70 <= 0)

m.c405 = Constraint(expr= - m.b50 + m.b54 - m.b71 <= 0)

m.c406 = Constraint(expr= - m.b50 + m.b56 - m.b72 <= 0)

m.c407 = Constraint(expr= - m.b50 + m.b58 - m.b73 <= 0)

m.c408 = Constraint(expr= - m.b50 + m.b60 - m.b74 <= 0)

m.c409 = Constraint(expr= - m.b50 + m.b62 - m.x75 <= 0)

m.c410 = Constraint(expr= - m.b52 + m.b54 - m.x76 <= 0)

m.c411 = Constraint(expr= - m.b52 + m.b56 - m.x77 <= 0)

m.c412 = Constraint(expr= - m.b52 + m.b58 - m.x78 <= 0)

m.c413 = Constraint(expr= - m.b52 + m.b60 - m.x79 <= 0)

m.c414 = Constraint(expr= - m.b52 + m.b62 - m.x80 <= 0)

m.c415 = Constraint(expr= - m.b54 + m.b56 - m.x81 <= 0)

m.c416 = Constraint(expr= - m.b54 + m.b58 - m.x82 <= 0)

m.c417 = Constraint(expr= - m.b54 + m.b60 - m.x83 <= 0)

m.c418 = Constraint(expr= - m.b54 + m.b62 - m.x84 <= 0)

m.c419 = Constraint(expr= - m.b56 + m.b58 - m.x85 <= 0)

m.c420 = Constraint(expr= - m.b56 + m.b60 - m.x86 <= 0)

m.c421 = Constraint(expr= - m.b56 + m.b62 - m.x87 <= 0)

m.c422 = Constraint(expr= - m.b58 + m.b60 - m.x88 <= 0)

m.c423 = Constraint(expr= - m.b58 + m.b62 - m.x89 <= 0)

m.c424 = Constraint(expr= - m.b60 + m.b62 - m.x90 <= 0)

m.c425 = Constraint(expr= - m.b63 + m.b64 - m.b70 <= 0)

m.c426 = Constraint(expr= - m.b63 + m.b65 - m.b71 <= 0)

m.c427 = Constraint(expr= - m.b63 + m.b66 - m.b72 <= 0)

m.c428 = Constraint(expr= - m.b63 + m.b67 - m.b73 <= 0)

m.c429 = Constraint(expr= - m.b63 + m.b68 - m.b74 <= 0)

m.c430 = Constraint(expr= - m.b63 + m.b69 - m.x75 <= 0)

m.c431 = Constraint(expr= - m.b64 + m.b65 - m.x76 <= 0)

m.c432 = Constraint(expr= - m.b64 + m.b66 - m.x77 <= 0)

m.c433 = Constraint(expr= - m.b64 + m.b67 - m.x78 <= 0)

m.c434 = Constraint(expr= - m.b64 + m.b68 - m.x79 <= 0)

m.c435 = Constraint(expr= - m.b64 + m.b69 - m.x80 <= 0)

m.c436 = Constraint(expr= - m.b65 + m.b66 - m.x81 <= 0)

m.c437 = Constraint(expr= - m.b65 + m.b67 - m.x82 <= 0)

m.c438 = Constraint(expr= - m.b65 + m.b68 - m.x83 <= 0)

m.c439 = Constraint(expr= - m.b65 + m.b69 - m.x84 <= 0)

m.c440 = Constraint(expr= - m.b66 + m.b67 - m.x85 <= 0)

m.c441 = Constraint(expr= - m.b66 + m.b68 - m.x86 <= 0)

m.c442 = Constraint(expr= - m.b66 + m.b69 - m.x87 <= 0)

m.c443 = Constraint(expr= - m.b67 + m.b68 - m.x88 <= 0)

m.c444 = Constraint(expr= - m.b67 + m.b69 - m.x89 <= 0)

m.c445 = Constraint(expr= - m.b68 + m.b69 - m.x90 <= 0)

m.c446 = Constraint(expr= - m.b70 + m.b71 - m.x76 <= 0)

m.c447 = Constraint(expr= - m.b70 + m.b72 - m.x77 <= 0)

m.c448 = Constraint(expr= - m.b70 + m.b73 - m.x78 <= 0)

m.c449 = Constraint(expr= - m.b70 + m.b74 - m.x79 <= 0)

m.c450 = Constraint(expr= - m.b70 + m.x75 - m.x80 <= 0)

m.c451 = Constraint(expr= - m.b71 + m.b72 - m.x81 <= 0)

m.c452 = Constraint(expr= - m.b71 + m.b73 - m.x82 <= 0)

m.c453 = Constraint(expr= - m.b71 + m.b74 - m.x83 <= 0)

m.c454 = Constraint(expr= - m.b71 + m.x75 - m.x84 <= 0)

m.c455 = Constraint(expr= - m.b72 + m.b73 - m.x85 <= 0)

m.c456 = Constraint(expr= - m.b72 + m.b74 - m.x86 <= 0)

m.c457 = Constraint(expr= - m.b72 + m.x75 - m.x87 <= 0)

m.c458 = Constraint(expr= - m.b73 + m.b74 - m.x88 <= 0)

m.c459 = Constraint(expr= - m.b73 + m.x75 - m.x89 <= 0)

m.c460 = Constraint(expr= - m.b74 + m.x75 - m.x90 <= 0)

m.c461 = Constraint(expr= - m.x76 + m.x77 - m.x81 <= 0)

m.c462 = Constraint(expr= - m.x76 + m.x78 - m.x82 <= 0)

m.c463 = Constraint(expr= - m.x76 + m.x79 - m.x83 <= 0)

m.c464 = Constraint(expr= - m.x76 + m.x80 - m.x84 <= 0)

m.c465 = Constraint(expr= - m.x77 + m.x78 - m.x85 <= 0)

m.c466 = Constraint(expr= - m.x77 + m.x79 - m.x86 <= 0)

m.c467 = Constraint(expr= - m.x77 + m.x80 - m.x87 <= 0)

m.c468 = Constraint(expr= - m.x78 + m.x79 - m.x88 <= 0)

m.c469 = Constraint(expr= - m.x78 + m.x80 - m.x89 <= 0)

m.c470 = Constraint(expr= - m.x79 + m.x80 - m.x90 <= 0)

m.c471 = Constraint(expr= - m.x81 + m.x82 - m.x85 <= 0)

m.c472 = Constraint(expr= - m.x81 + m.x83 - m.x86 <= 0)

m.c473 = Constraint(expr= - m.x81 + m.x84 - m.x87 <= 0)

m.c474 = Constraint(expr= - m.x82 + m.x83 - m.x88 <= 0)

m.c475 = Constraint(expr= - m.x82 + m.x84 - m.x89 <= 0)

m.c476 = Constraint(expr= - m.x83 + m.x84 - m.x90 <= 0)

m.c477 = Constraint(expr= - m.x85 + m.x86 - m.x88 <= 0)

m.c478 = Constraint(expr= - m.x85 + m.x87 - m.x89 <= 0)

m.c479 = Constraint(expr= - m.x86 + m.x87 - m.x90 <= 0)

m.c480 = Constraint(expr= - m.x88 + m.x89 - m.x90 <= 0)

m.c481 = Constraint(expr=2*m.b1*m.b47 - 4*m.b1 + 2*m.b47 - 2*m.b1*m.b50 + 17*m.b50 + 2*m.b1*m.b60 + 9*m.b60 - 2*m.b1*
                         m.b63 + 11*m.b63 - 2*m.b1*m.b64 + m.b64 - 2*m.b1*m.b65 + 9*m.b65 - 2*m.b1*m.b66 + 4*m.b66 - 2*
                         m.b1*m.b67 + 5*m.b67 - 2*m.b1*m.b69 + 9*m.b69 + 2*m.b1*m.b70 - 13*m.b70 + 2*m.b1*m.b71 - m.b71
                          + 2*m.b1*m.b72 - 3*m.b72 + 2*m.b1*m.b73 - 7*m.b73 + 2*m.b1*m.b74 - 5*m.b74 + 2*m.b1*m.x75 - 
                         m.x75 + 2*m.b1*m.x79 + 5*m.x79 + 2*m.b1*m.x83 - 3*m.x83 + 2*m.b1*m.x86 + 2*m.b1*m.x88 + m.x88
                          - 2*m.b1*m.x90 + 3*m.x90 + 2*m.b2*m.b47 + 8*m.b2 - 2*m.b2*m.b54 + 15*m.b54 - 2*m.b2*m.b56 + 7*
                         m.b56 + 2*m.b2*m.b60 - 2*m.b2*m.b62 + 15*m.b62 - 2*m.b2*m.b63 - 2*m.b2*m.b64 - 2*m.b2*m.b65 - 2
                         *m.b2*m.b66 - 2*m.b2*m.b67 - 2*m.b2*m.b69 - 2*m.b2*m.b71 - 2*m.b2*m.b72 + 2*m.b2*m.b74 - 2*m.b2
                         *m.x75 - 2*m.b2*m.x76 + 11*m.x76 - 2*m.b2*m.x77 + 5*m.x77 + 2*m.b2*m.x79 - 2*m.b2*m.x80 + 11*
                         m.x80 + 2*m.b2*m.x82 - 5*m.x82 + 2*m.b2*m.x83 + 2*m.b2*m.x85 - m.x85 + 2*m.b2*m.x86 + 2*m.b2*
                         m.x88 - 2*m.b2*m.x89 + 5*m.x89 - 2*m.b2*m.x90 - 2*m.b3*m.b50 - 11*m.b3 + 2*m.b3*m.b54 + 2*m.b3*
                         m.b56 + 2*m.b3*m.b62 - 2*m.b3*m.b63 + 2*m.b3*m.b65 + 2*m.b3*m.b66 + 2*m.b3*m.b69 + 2*m.b3*m.b70
                          + 2*m.b3*m.b71 + 2*m.b3*m.b72 + 2*m.b3*m.b73 + 2*m.b3*m.b74 + 2*m.b3*m.x75 + 2*m.b3*m.x76 + 2*
                         m.b3*m.x77 + 2*m.b3*m.x80 - 2*m.b3*m.x82 - 2*m.b3*m.x83 - 2*m.b3*m.x85 - 2*m.b3*m.x86 + 2*m.b3*
                         m.x89 + 2*m.b3*m.x90 + 2*m.b4*m.b46 - 13*m.b4 - 14*m.b46 + 2*m.b4*m.b48 - 21*m.b48 - 2*m.b4*
                         m.b50 + 2*m.b4*m.b51 - 18*m.b51 + 2*m.b4*m.b53 - 12*m.b53 + 2*m.b4*m.b55 - 8*m.b55 + 2*m.b4*
                         m.b56 + 2*m.b4*m.b57 - 14*m.b57 + 2*m.b4*m.b59 - 12*m.b59 + 2*m.b4*m.b61 - 12*m.b61 - 2*m.b4*
                         m.b63 + 2*m.b4*m.b66 + 2*m.b4*m.b70 + 2*m.b4*m.b71 + 2*m.b4*m.b72 + 2*m.b4*m.b73 + 2*m.b4*m.b74
                          + 2*m.b4*m.x75 + 2*m.b4*m.x77 + 2*m.b4*m.x81 - 2*m.x81 - 2*m.b4*m.x85 - 2*m.b4*m.x86 - 2*m.b4*
                         m.x87 + 2*m.x87 + 2*m.b5*m.b46 + 2*m.b5 + 2*m.b5*m.b48 + 2*m.b5*m.b49 - 12*m.b49 + 2*m.b5*m.b51
                          - 2*m.b5*m.b54 + 2*m.b5*m.b57 + 2*m.b5*m.b59 - 2*m.b5*m.b62 - 2*m.b5*m.b65 - 2*m.b5*m.b69 - 2*
                         m.b5*m.b71 - 2*m.b5*m.x75 - 2*m.b5*m.x76 - 2*m.b5*m.x80 + 2*m.b5*m.x82 + 2*m.b5*m.x83 - 2*m.b5*
                         m.x89 - 2*m.b5*m.x90 - 2*m.b6*m.b50 - 7*m.b6 + 2*m.b6*m.b58 + 9*m.b58 - 2*m.b6*m.b63 + 2*m.b6*
                         m.b67 + 2*m.b6*m.b70 + 2*m.b6*m.b71 + 2*m.b6*m.b72 + 2*m.b6*m.b73 + 2*m.b6*m.b74 + 2*m.b6*m.x75
                          + 2*m.b6*m.x78 + 5*m.x78 + 2*m.b6*m.x82 + 2*m.b6*m.x85 - 2*m.b6*m.x88 - 2*m.b6*m.x89 - 2*m.b7*
                         m.b54 + 7*m.b7 - 2*m.b7*m.b56 + 2*m.b7*m.b58 - 2*m.b7*m.b62 - 2*m.b7*m.b65 - 2*m.b7*m.b66 + 2*
                         m.b7*m.b67 - 2*m.b7*m.b69 - 2*m.b7*m.b71 - 2*m.b7*m.b72 + 2*m.b7*m.b73 - 2*m.b7*m.x75 - 2*m.b7*
                         m.x76 - 2*m.b7*m.x77 + 2*m.b7*m.x78 - 2*m.b7*m.x80 + 2*m.b7*m.x82 + 2*m.b7*m.x83 + 2*m.b7*m.x85
                          + 2*m.b7*m.x86 - 2*m.b7*m.x88 - 2*m.b7*m.x89 - 2*m.b7*m.x90 + 2*m.b8*m.b46 - 8*m.b8 + 2*m.b8*
                         m.b47 + 2*m.b8*m.b48 - 2*m.b8*m.b50 + 2*m.b8*m.b51 + 2*m.b8*m.b53 + 2*m.b8*m.b55 + 2*m.b8*m.b56
                          + 2*m.b8*m.b57 + 2*m.b8*m.b59 + 2*m.b8*m.b61 - 2*m.b8*m.b63 - 2*m.b8*m.b64 - 2*m.b8*m.b65 - 2*
                         m.b8*m.b67 - 2*m.b8*m.b68 + 6*m.b68 - 2*m.b8*m.b69 + 2*m.b8*m.b70 + 2*m.b8*m.b71 + 2*m.b8*m.b72
                          + 2*m.b8*m.b73 + 2*m.b8*m.b74 + 2*m.b8*m.x75 + 2*m.b8*m.x77 + 2*m.b8*m.x81 - 2*m.b8*m.x85 - 2*
                         m.b8*m.x86 - 2*m.b8*m.x87 + 2*m.b9*m.b46 + 5*m.b9 + 2*m.b9*m.b47 + 2*m.b9*m.b48 + 2*m.b9*m.b49
                          + 2*m.b9*m.b51 - 2*m.b9*m.b54 + 2*m.b9*m.b57 + 2*m.b9*m.b59 - 2*m.b9*m.b62 - 2*m.b9*m.b63 - 2*
                         m.b9*m.b64 - 2*m.b9*m.b65 - 2*m.b9*m.b67 - 2*m.b9*m.b68 - 2*m.b9*m.b69 - 2*m.b9*m.b71 - 2*m.b9*
                         m.x75 - 2*m.b9*m.x76 - 2*m.b9*m.x80 + 2*m.b9*m.x82 + 2*m.b9*m.x83 - 2*m.b9*m.x89 - 2*m.b9*m.x90
                          + 2*m.b10*m.b46 - 17*m.b10 + 2*m.b10*m.b48 - 2*m.b10*m.b50 + 2*m.b10*m.b51 + 2*m.b10*m.b53 + 2
                         *m.b10*m.b55 + 2*m.b10*m.b57 + 2*m.b10*m.b59 + 2*m.b10*m.b60 + 2*m.b10*m.b61 - 2*m.b10*m.b63 + 
                         2*m.b10*m.b68 + 2*m.b10*m.b70 + 2*m.b10*m.b71 + 2*m.b10*m.b72 + 2*m.b10*m.b73 + 2*m.b10*m.b74
                          + 2*m.b10*m.x75 + 2*m.b10*m.x79 + 2*m.b10*m.x83 + 2*m.b10*m.x86 + 2*m.b10*m.x88 - 2*m.b10*
                         m.x90 + 2*m.b11*m.b46 - m.b11 + 2*m.b11*m.b48 + 2*m.b11*m.b49 + 2*m.b11*m.b51 - 2*m.b11*m.b54
                          - 2*m.b11*m.b56 + 2*m.b11*m.b57 + 2*m.b11*m.b59 + 2*m.b11*m.b60 - 2*m.b11*m.b62 - 2*m.b11*
                         m.b65 - 2*m.b11*m.b66 + 2*m.b11*m.b68 - 2*m.b11*m.b69 - 2*m.b11*m.b71 - 2*m.b11*m.b72 + 2*m.b11
                         *m.b74 - 2*m.b11*m.x75 - 2*m.b11*m.x76 - 2*m.b11*m.x77 + 2*m.b11*m.x79 - 2*m.b11*m.x80 + 2*
                         m.b11*m.x82 + 2*m.b11*m.x83 + 2*m.b11*m.x85 + 2*m.b11*m.x86 + 2*m.b11*m.x88 - 2*m.b11*m.x89 - 2
                         *m.b11*m.x90 - 2*m.b12*m.b50 - m.b12 + 2*m.b12*m.b52 + 3*m.b52 - 2*m.b12*m.b63 + 2*m.b12*m.b64
                          + 2*m.b12*m.b70 + 2*m.b12*m.b71 + 2*m.b12*m.b72 + 2*m.b12*m.b73 + 2*m.b12*m.b74 + 2*m.b12*
                         m.x75 - 2*m.b12*m.x76 - 2*m.b12*m.x77 - 2*m.b12*m.x78 - 2*m.b12*m.x79 - 2*m.b12*m.x80 + 2*m.b13
                         *m.b52 + 9*m.b13 - 2*m.b13*m.b54 - 2*m.b13*m.b56 - 2*m.b13*m.b62 + 2*m.b13*m.b64 - 2*m.b13*
                         m.b65 - 2*m.b13*m.b66 - 2*m.b13*m.b69 + 2*m.b13*m.b70 - 2*m.b13*m.b71 - 2*m.b13*m.b72 - 2*m.b13
                         *m.x75 - 2*m.b13*m.x76 - 2*m.b13*m.x77 - 2*m.b13*m.x78 - 2*m.b13*m.x79 - 2*m.b13*m.x80 + 2*
                         m.b13*m.x82 + 2*m.b13*m.x83 + 2*m.b13*m.x85 + 2*m.b13*m.x86 - 2*m.b13*m.x89 - 2*m.b13*m.x90 + 2
                         *m.b14*m.b46 - 13*m.b14 + 2*m.b14*m.b48 - 2*m.b14*m.b50 + 2*m.b14*m.b51 + 2*m.b14*m.b53 + 2*
                         m.b14*m.b55 + 2*m.b14*m.b56 + 2*m.b14*m.b57 + 2*m.b14*m.b59 + 2*m.b14*m.b61 - 2*m.b14*m.b63 + 2
                         *m.b14*m.b66 + 2*m.b14*m.b70 + 2*m.b14*m.b71 + 2*m.b14*m.b72 + 2*m.b14*m.b73 + 2*m.b14*m.b74 + 
                         2*m.b14*m.x75 + 2*m.b14*m.x77 + 2*m.b14*m.x81 - 2*m.b14*m.x85 - 2*m.b14*m.x86 - 2*m.b14*m.x87
                          + 2*m.b15*m.b46 + 2*m.b15 + 2*m.b15*m.b48 + 2*m.b15*m.b49 + 2*m.b15*m.b51 - 2*m.b15*m.b54 + 2*
                         m.b15*m.b57 + 2*m.b15*m.b59 - 2*m.b15*m.b62 - 2*m.b15*m.b65 - 2*m.b15*m.b69 - 2*m.b15*m.b71 - 2
                         *m.b15*m.x75 - 2*m.b15*m.x76 - 2*m.b15*m.x80 + 2*m.b15*m.x82 + 2*m.b15*m.x83 - 2*m.b15*m.x89 - 
                         2*m.b15*m.x90 + 2*m.b16*m.b46 + 2*m.b16*m.b48 - 2*m.b16*m.b50 + 2*m.b16*m.b51 - 2*m.b16*m.b52
                          + 2*m.b16*m.b53 - 2*m.b16*m.b54 + 2*m.b16*m.b55 - 2*m.b16*m.b56 + 2*m.b16*m.b57 - 2*m.b16*
                         m.b58 + 2*m.b16*m.b59 - 2*m.b16*m.b60 + 2*m.b16*m.b61 - 2*m.b16*m.b62 - 2*m.b16*m.b63 - 2*m.b16
                         *m.b64 - 2*m.b16*m.b65 - 2*m.b16*m.b66 - 2*m.b16*m.b67 - 2*m.b16*m.b68 - 2*m.b16*m.b69 + 2*
                         m.b16*m.b70 + 2*m.b16*m.b71 + 2*m.b16*m.b72 + 2*m.b16*m.b73 + 2*m.b16*m.b74 + 2*m.b16*m.x75 + 2
                         *m.b17*m.b46 + 12*m.b17 + 2*m.b17*m.b48 + 2*m.b17*m.b49 - 2*m.b17*m.b50 + 2*m.b17*m.b51 - 2*
                         m.b17*m.b52 - 2*m.b17*m.b54 - 2*m.b17*m.b56 + 2*m.b17*m.b57 - 2*m.b17*m.b58 + 2*m.b17*m.b59 - 2
                         *m.b17*m.b60 - 2*m.b17*m.b62 - 2*m.b17*m.b63 - 2*m.b17*m.b64 - 2*m.b17*m.b65 - 2*m.b17*m.b66 - 
                         2*m.b17*m.b67 - 2*m.b17*m.b68 - 2*m.b17*m.b69 - 2*m.b17*m.b71 - 2*m.b17*m.b72 - 2*m.b17*m.x75
                          - 2*m.b17*m.x76 - 2*m.b17*m.x77 - 2*m.b17*m.x80 + 2*m.b17*m.x82 + 2*m.b17*m.x83 + 2*m.b17*
                         m.x85 + 2*m.b17*m.x86 - 2*m.b17*m.x89 - 2*m.b17*m.x90 - 2*m.b18*m.b47 - 9*m.b18 + 2*m.b18*m.b48
                          + 2*m.b18*m.b49 + 2*m.b18*m.b51 + 2*m.b18*m.b53 + 2*m.b18*m.b55 + 2*m.b18*m.b56 + 2*m.b18*
                         m.b57 - 2*m.b18*m.b60 + 2*m.b18*m.b61 + 2*m.b18*m.b63 + 2*m.b18*m.b64 + 2*m.b18*m.b65 + 2*m.b18
                         *m.b66 + 2*m.b18*m.b67 + 2*m.b18*m.b69 + 2*m.b18*m.b72 - 2*m.b18*m.b74 + 2*m.b18*m.x77 - 2*
                         m.b18*m.x79 + 2*m.b18*m.x81 - 2*m.b18*m.x83 - 2*m.b18*m.x85 - 2*m.b18*m.x86 - 2*m.b18*m.x87 - 2
                         *m.b18*m.x88 + 2*m.b18*m.x90 - 2*m.b19*m.b47 - 4*m.b19 + 2*m.b19*m.b58 - 2*m.b19*m.b60 + 2*
                         m.b19*m.b63 + 2*m.b19*m.b64 + 2*m.b19*m.b65 + 2*m.b19*m.b66 + 2*m.b19*m.b67 + 2*m.b19*m.b69 + 2
                         *m.b19*m.b73 - 2*m.b19*m.b74 + 2*m.b19*m.x78 - 2*m.b19*m.x79 + 2*m.b19*m.x82 - 2*m.b19*m.x83 + 
                         2*m.b19*m.x85 - 2*m.b19*m.x86 - 2*m.b19*m.x88 - 2*m.b19*m.x89 + 2*m.b19*m.x90 + 2*m.b20*m.b48
                          - 4*m.b20 + 2*m.b20*m.b49 + 2*m.b20*m.b51 + 2*m.b20*m.b53 + 2*m.b20*m.b55 + 2*m.b20*m.b56 + 2*
                         m.b20*m.b57 - 2*m.b20*m.b60 + 2*m.b20*m.b61 + 2*m.b20*m.b72 - 2*m.b20*m.b74 + 2*m.b20*m.x77 - 2
                         *m.b20*m.x79 + 2*m.b20*m.x81 - 2*m.b20*m.x83 - 2*m.b20*m.x85 - 2*m.b20*m.x86 - 2*m.b20*m.x87 - 
                         2*m.b20*m.x88 + 2*m.b20*m.x90 - 2*m.b21*m.b47 - 12*m.b21 + 2*m.b21*m.b48 + 2*m.b21*m.b49 + 2*
                         m.b21*m.b51 + 2*m.b21*m.b53 + 2*m.b21*m.b55 + 2*m.b21*m.b57 + 2*m.b21*m.b61 + 2*m.b21*m.b63 + 2
                         *m.b21*m.b64 + 2*m.b21*m.b65 + 2*m.b21*m.b66 + 2*m.b21*m.b67 + 2*m.b21*m.b69 - 2*m.b22*m.b47 + 
                         2*m.b22 + 2*m.b22*m.b52 - 2*m.b22*m.b60 + 2*m.b22*m.b63 + 2*m.b22*m.b64 + 2*m.b22*m.b65 + 2*
                         m.b22*m.b66 + 2*m.b22*m.b67 + 2*m.b22*m.b69 + 2*m.b22*m.b70 - 2*m.b22*m.b74 - 2*m.b22*m.x76 - 2
                         *m.b22*m.x77 - 2*m.b22*m.x78 - 2*m.b22*m.x79 - 2*m.b22*m.x80 - 2*m.b22*m.x83 - 2*m.b22*m.x86 - 
                         2*m.b22*m.x88 + 2*m.b22*m.x90 - 2*m.b23*m.b47 - 9*m.b23 + 2*m.b23*m.b48 + 2*m.b23*m.b49 + 2*
                         m.b23*m.b51 + 2*m.b23*m.b53 + 2*m.b23*m.b55 + 2*m.b23*m.b56 + 2*m.b23*m.b57 - 2*m.b23*m.b60 + 2
                         *m.b23*m.b61 + 2*m.b23*m.b63 + 2*m.b23*m.b64 + 2*m.b23*m.b65 + 2*m.b23*m.b66 + 2*m.b23*m.b67 + 
                         2*m.b23*m.b69 + 2*m.b23*m.b72 - 2*m.b23*m.b74 + 2*m.b23*m.x77 - 2*m.b23*m.x79 + 2*m.b23*m.x81
                          - 2*m.b23*m.x83 - 2*m.b23*m.x85 - 2*m.b23*m.x86 - 2*m.b23*m.x87 - 2*m.b23*m.x88 + 2*m.b23*
                         m.x90 + 2*m.b24*m.b48 + 4*m.b24 + 2*m.b24*m.b49 - 2*m.b24*m.b50 + 2*m.b24*m.b51 - 2*m.b24*m.b52
                          + 2*m.b24*m.b53 - 2*m.b24*m.b54 + 2*m.b24*m.b55 - 2*m.b24*m.b56 + 2*m.b24*m.b57 - 2*m.b24*
                         m.b58 - 2*m.b24*m.b60 + 2*m.b24*m.b61 - 2*m.b24*m.b62 - 2*m.b24*m.b74 - 2*m.b24*m.x79 - 2*m.b24
                         *m.x83 - 2*m.b24*m.x86 - 2*m.b24*m.x88 + 2*m.b24*m.x90 - 2*m.b25*m.b46 + 7*m.b25 - 2*m.b25*
                         m.b48 - 2*m.b25*m.b49 - 2*m.b25*m.b51 - 2*m.b25*m.b53 - 2*m.b25*m.b55 - 2*m.b25*m.b56 + 2*m.b25
                         *m.b58 - 2*m.b25*m.b59 - 2*m.b25*m.b61 - 2*m.b25*m.b66 + 2*m.b25*m.b67 - 2*m.b25*m.b72 + 2*
                         m.b25*m.b73 - 2*m.b25*m.x77 + 2*m.b25*m.x78 - 2*m.b25*m.x81 + 2*m.b25*m.x82 + 2*m.b25*m.x85 + 2
                         *m.b25*m.x86 + 2*m.b25*m.x87 - 2*m.b25*m.x88 - 2*m.b25*m.x89 + 2*m.b26*m.b46 + 4*m.b26 + 2*
                         m.b26*m.b47 - 2*m.b26*m.b63 - 2*m.b26*m.b64 - 2*m.b26*m.b65 - 2*m.b26*m.b67 - 2*m.b26*m.b68 - 2
                         *m.b26*m.b69 - 2*m.b27*m.b55 - 3*m.b27 - 2*m.b27*m.b56 + 2*m.b27*m.b59 + 2*m.b27*m.b60 - 2*
                         m.b27*m.b66 + 2*m.b27*m.b68 - 2*m.b27*m.b72 + 2*m.b27*m.b74 - 2*m.b27*m.x77 + 2*m.b27*m.x79 - 2
                         *m.b27*m.x81 + 2*m.b27*m.x83 + 2*m.b27*m.x85 + 2*m.b27*m.x86 + 2*m.b27*m.x87 + 2*m.b27*m.x88 - 
                         2*m.b27*m.x90 - 2*m.b28*m.b46 + 11*m.b28 - 2*m.b28*m.b48 - 2*m.b28*m.b49 + 2*m.b28*m.b52 - 2*
                         m.b28*m.b53 - 2*m.b28*m.b55 - 2*m.b28*m.b56 - 2*m.b28*m.b57 - 2*m.b28*m.b59 - 2*m.b28*m.b61 + 2
                         *m.b28*m.b64 - 2*m.b28*m.b66 + 2*m.b28*m.b70 - 2*m.b28*m.b72 - 2*m.b28*m.x76 - 2*m.b28*m.x77 - 
                         2*m.b28*m.x78 - 2*m.b28*m.x79 - 2*m.b28*m.x80 - 2*m.b28*m.x81 + 2*m.b28*m.x85 + 2*m.b28*m.x86
                          + 2*m.b28*m.x87 + 2*m.b30*m.b46 + 13*m.b30 + 2*m.b30*m.b48 - 2*m.b30*m.b50 - 2*m.b30*m.b52 - 2
                         *m.b30*m.b54 - 2*m.b30*m.b55 - 2*m.b30*m.b56 - 2*m.b30*m.b58 - 2*m.b30*m.b60 - 2*m.b30*m.b62 - 
                         2*m.b30*m.b63 - 2*m.b30*m.b64 - 2*m.b30*m.b65 - 2*m.b30*m.b66 - 2*m.b30*m.b67 - 2*m.b30*m.b68
                          - 2*m.b30*m.b69 - 2*m.b30*m.b72 - 2*m.b30*m.x77 - 2*m.b30*m.x81 + 2*m.b30*m.x85 + 2*m.b30*
                         m.x86 + 2*m.b30*m.x87 + 2*m.b31*m.b46 - 2*m.b31 + 2*m.b31*m.b47 + 2*m.b31*m.b48 + 2*m.b31*m.b49
                          + 2*m.b31*m.b51 + 2*m.b31*m.b53 + 2*m.b31*m.b55 + 2*m.b31*m.b56 - 2*m.b31*m.b58 + 2*m.b31*
                         m.b59 + 2*m.b31*m.b61 - 2*m.b31*m.b63 - 2*m.b31*m.b64 - 2*m.b31*m.b65 - 2*m.b31*m.b67 - 2*m.b31
                         *m.b68 - 2*m.b31*m.b69 + 2*m.b31*m.b72 - 2*m.b31*m.b73 + 2*m.b31*m.x77 - 2*m.b31*m.x78 + 2*
                         m.b31*m.x81 - 2*m.b31*m.x82 - 2*m.b31*m.x85 - 2*m.b31*m.x86 - 2*m.b31*m.x87 + 2*m.b31*m.x88 + 2
                         *m.b31*m.x89 + 2*m.b32*m.b46 - 9*m.b32 + 2*m.b32*m.b48 + 2*m.b32*m.b49 + 2*m.b32*m.b51 + 2*
                         m.b32*m.b53 + 2*m.b32*m.b55 - 2*m.b32*m.b58 + 2*m.b32*m.b59 + 2*m.b32*m.b60 + 2*m.b32*m.b61 - 2
                         *m.b32*m.b67 + 2*m.b32*m.b68 - 2*m.b32*m.b73 + 2*m.b32*m.b74 - 2*m.b32*m.x78 + 2*m.b32*m.x79 - 
                         2*m.b32*m.x82 + 2*m.b32*m.x83 - 2*m.b32*m.x85 + 2*m.b32*m.x86 + 2*m.b32*m.x88 + 2*m.b32*m.x89
                          - 2*m.b32*m.x90 + 2*m.b33*m.b52 + 5*m.b33 - 2*m.b33*m.b58 + 2*m.b33*m.b64 - 2*m.b33*m.b67 + 2*
                         m.b33*m.b70 - 2*m.b33*m.b73 - 2*m.b33*m.x76 - 2*m.b33*m.x77 - 2*m.b33*m.x78 - 2*m.b33*m.x79 - 2
                         *m.b33*m.x80 - 2*m.b33*m.x82 - 2*m.b33*m.x85 + 2*m.b33*m.x88 + 2*m.b33*m.x89 + 2*m.b34*m.b46 - 
                         7*m.b34 + 2*m.b34*m.b48 + 2*m.b34*m.b49 + 2*m.b34*m.b51 + 2*m.b34*m.b53 + 2*m.b34*m.b55 + 2*
                         m.b34*m.b56 - 2*m.b34*m.b58 + 2*m.b34*m.b59 + 2*m.b34*m.b61 + 2*m.b34*m.b66 - 2*m.b34*m.b67 + 2
                         *m.b34*m.b72 - 2*m.b34*m.b73 + 2*m.b34*m.x77 - 2*m.b34*m.x78 + 2*m.b34*m.x81 - 2*m.b34*m.x82 - 
                         2*m.b34*m.x85 - 2*m.b34*m.x86 - 2*m.b34*m.x87 + 2*m.b34*m.x88 + 2*m.b34*m.x89 + 2*m.b35*m.b46
                          + 8*m.b35 + 2*m.b35*m.b48 + 2*m.b35*m.b49 - 2*m.b35*m.b50 + 2*m.b35*m.b51 - 2*m.b35*m.b52 + 2*
                         m.b35*m.b53 - 2*m.b35*m.b54 + 2*m.b35*m.b55 - 2*m.b35*m.b56 - 2*m.b35*m.b58 + 2*m.b35*m.b59 - 2
                         *m.b35*m.b60 + 2*m.b35*m.b61 - 2*m.b35*m.b62 - 2*m.b35*m.b63 - 2*m.b35*m.b64 - 2*m.b35*m.b65 - 
                         2*m.b35*m.b66 - 2*m.b35*m.b67 - 2*m.b35*m.b68 - 2*m.b35*m.b69 - 2*m.b35*m.b73 - 2*m.b35*m.x78
                          - 2*m.b35*m.x82 - 2*m.b35*m.x85 + 2*m.b35*m.x88 + 2*m.b35*m.x89 - 2*m.b36*m.b46 - 7*m.b36 - 2*
                         m.b36*m.b47 - 2*m.b36*m.b55 - 2*m.b36*m.b56 + 2*m.b36*m.b59 + 2*m.b36*m.b60 + 2*m.b36*m.b63 + 2
                         *m.b36*m.b64 + 2*m.b36*m.b65 + 2*m.b36*m.b67 + 2*m.b36*m.b68 + 2*m.b36*m.b69 - 2*m.b36*m.b72 + 
                         2*m.b36*m.b74 - 2*m.b36*m.x77 + 2*m.b36*m.x79 - 2*m.b36*m.x81 + 2*m.b36*m.x83 + 2*m.b36*m.x85
                          + 2*m.b36*m.x86 + 2*m.b36*m.x87 + 2*m.b36*m.x88 - 2*m.b36*m.x90 - 2*m.b37*m.b46 + 6*m.b37 - 2*
                         m.b37*m.b47 - 2*m.b37*m.b48 - 2*m.b37*m.b49 + 2*m.b37*m.b52 - 2*m.b37*m.b53 - 2*m.b37*m.b55 - 2
                         *m.b37*m.b56 - 2*m.b37*m.b57 - 2*m.b37*m.b59 - 2*m.b37*m.b61 + 2*m.b37*m.b63 + 2*m.b37*m.b64 + 
                         2*m.b37*m.b65 + 2*m.b37*m.b67 + 2*m.b37*m.b68 + 2*m.b37*m.b69 + 2*m.b37*m.b70 - 2*m.b37*m.b72
                          - 2*m.b37*m.x76 - 2*m.b37*m.x77 - 2*m.b37*m.x78 - 2*m.b37*m.x79 - 2*m.b37*m.x80 - 2*m.b37*
                         m.x81 + 2*m.b37*m.x85 + 2*m.b37*m.x86 + 2*m.b37*m.x87 - 2*m.b38*m.b46 - 4*m.b38 - 2*m.b38*m.b47
                          + 2*m.b38*m.b63 + 2*m.b38*m.b64 + 2*m.b38*m.b65 + 2*m.b38*m.b67 + 2*m.b38*m.b68 + 2*m.b38*
                         m.b69 + 2*m.b39*m.b48 + 7*m.b39 - 2*m.b39*m.b50 - 2*m.b39*m.b52 - 2*m.b39*m.b54 - 2*m.b39*m.b55
                          - 2*m.b39*m.b56 - 2*m.b39*m.b58 - 2*m.b39*m.b60 - 2*m.b39*m.b62 - 2*m.b39*m.b72 - 2*m.b39*
                         m.x77 - 2*m.b39*m.x81 + 2*m.b39*m.x85 + 2*m.b39*m.x86 + 2*m.b39*m.x87 - 2*m.b40*m.b46 + 15*
                         m.b40 - 2*m.b40*m.b48 - 2*m.b40*m.b49 + 2*m.b40*m.b52 - 2*m.b40*m.b53 - 2*m.b40*m.b55 - 2*m.b40
                         *m.b57 - 2*m.b40*m.b59 - 2*m.b40*m.b60 - 2*m.b40*m.b61 + 2*m.b40*m.b64 - 2*m.b40*m.b68 + 2*
                         m.b40*m.b70 - 2*m.b40*m.b74 - 2*m.b40*m.x76 - 2*m.b40*m.x77 - 2*m.b40*m.x78 - 2*m.b40*m.x79 - 2
                         *m.b40*m.x80 - 2*m.b40*m.x83 - 2*m.b40*m.x86 - 2*m.b40*m.x88 + 2*m.b40*m.x90 + 2*m.b41*m.b55 + 
                         3*m.b41 + 2*m.b41*m.b56 - 2*m.b41*m.b59 - 2*m.b41*m.b60 + 2*m.b41*m.b66 - 2*m.b41*m.b68 + 2*
                         m.b41*m.b72 - 2*m.b41*m.b74 + 2*m.b41*m.x77 - 2*m.b41*m.x79 + 2*m.b41*m.x81 - 2*m.b41*m.x83 - 2
                         *m.b41*m.x85 - 2*m.b41*m.x86 - 2*m.b41*m.x87 - 2*m.b41*m.x88 + 2*m.b41*m.x90 + 2*m.b42*m.b46 + 
                         17*m.b42 + 2*m.b42*m.b48 - 2*m.b42*m.b50 - 2*m.b42*m.b52 - 2*m.b42*m.b54 - 2*m.b42*m.b56 - 2*
                         m.b42*m.b58 - 2*m.b42*m.b59 - 2*m.b42*m.b60 - 2*m.b42*m.b62 - 2*m.b42*m.b63 - 2*m.b42*m.b64 - 2
                         *m.b42*m.b65 - 2*m.b42*m.b66 - 2*m.b42*m.b67 - 2*m.b42*m.b68 - 2*m.b42*m.b69 - 2*m.b42*m.b74 - 
                         2*m.b42*m.x79 - 2*m.b42*m.x83 - 2*m.b42*m.x86 - 2*m.b42*m.x88 + 2*m.b42*m.x90 + 2*m.b43*m.b46
                          - 11*m.b43 + 2*m.b43*m.b48 + 2*m.b43*m.b49 - 2*m.b43*m.b52 + 2*m.b43*m.b53 + 2*m.b43*m.b55 + 2
                         *m.b43*m.b56 + 2*m.b43*m.b57 + 2*m.b43*m.b59 + 2*m.b43*m.b61 - 2*m.b43*m.b64 + 2*m.b43*m.b66 - 
                         2*m.b43*m.b70 + 2*m.b43*m.b72 + 2*m.b43*m.x76 + 2*m.b43*m.x77 + 2*m.b43*m.x78 + 2*m.b43*m.x79
                          + 2*m.b43*m.x80 + 2*m.b43*m.x81 - 2*m.b43*m.x85 - 2*m.b43*m.x86 - 2*m.b43*m.x87 + 2*m.b44*
                         m.b46 + 2*m.b44 + 2*m.b44*m.b48 + 2*m.b44*m.b49 - 2*m.b44*m.b50 - 2*m.b44*m.b52 + 2*m.b44*m.b53
                          - 2*m.b44*m.b54 + 2*m.b44*m.b55 - 2*m.b44*m.b56 + 2*m.b44*m.b57 - 2*m.b44*m.b58 + 2*m.b44*
                         m.b59 - 2*m.b44*m.b60 + 2*m.b44*m.b61 - 2*m.b44*m.b62 - 2*m.b44*m.b63 - 2*m.b44*m.b64 - 2*m.b44
                         *m.b65 - 2*m.b44*m.b66 - 2*m.b44*m.b67 - 2*m.b44*m.b68 - 2*m.b44*m.b69 - 2*m.b44*m.b70 + 2*
                         m.b44*m.x76 + 2*m.b44*m.x77 + 2*m.b44*m.x78 + 2*m.b44*m.x79 + 2*m.b44*m.x80 + 2*m.b45*m.b46 + 
                         13*m.b45 + 2*m.b45*m.b48 - 2*m.b45*m.b50 - 2*m.b45*m.b52 - 2*m.b45*m.b54 - 2*m.b45*m.b55 - 2*
                         m.b45*m.b56 - 2*m.b45*m.b58 - 2*m.b45*m.b60 - 2*m.b45*m.b62 - 2*m.b45*m.b63 - 2*m.b45*m.b64 - 2
                         *m.b45*m.b65 - 2*m.b45*m.b66 - 2*m.b45*m.b67 - 2*m.b45*m.b68 - 2*m.b45*m.b69 - 2*m.b45*m.b72 - 
                         2*m.b45*m.x77 - 2*m.b45*m.x81 + 2*m.b45*m.x85 + 2*m.b45*m.x86 + 2*m.b45*m.x87 + m.x91 >= 1296)

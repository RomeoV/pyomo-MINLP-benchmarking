#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        363      141       12      210        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        209      169       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        843      807       36        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x66 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x22 - m.x23 - m.x24 - m.x25 + 5*m.x46 + 10*m.x47 + 5*m.x48 + 10*m.x49 - 2*m.x66 - m.x67
                        - 2*m.x68 - m.x69 + 80*m.x70 + 90*m.x71 + 120*m.x72 + 100*m.x73 + 285*m.x74 + 390*m.x75
                        + 350*m.x76 + 300*m.x77 + 290*m.x78 + 405*m.x79 + 190*m.x80 + 340*m.x81 - 5*m.b190 - 4*m.b191
                        - 6*m.b192 - 3*m.b193 - 8*m.b194 - 7*m.b195 - 6*m.b196 - 5*m.b197 - 6*m.b198 - 9*m.b199
                        - 4*m.b200 - 3*m.b201 - 10*m.b202 - 9*m.b203 - 5*m.b204 - 6*m.b205 - 6*m.b206 - 10*m.b207
                        - 6*m.b208 - 9*m.b209, sense=maximize)

m.c2 = Constraint(expr=   m.x22 - m.x26 - m.x30 == 0)

m.c3 = Constraint(expr=   m.x23 - m.x27 - m.x31 == 0)

m.c4 = Constraint(expr=   m.x24 - m.x28 - m.x32 == 0)

m.c5 = Constraint(expr=   m.x25 - m.x29 - m.x33 == 0)

m.c6 = Constraint(expr= - m.x34 - m.x38 + m.x42 == 0)

m.c7 = Constraint(expr= - m.x35 - m.x39 + m.x43 == 0)

m.c8 = Constraint(expr= - m.x36 - m.x40 + m.x44 == 0)

m.c9 = Constraint(expr= - m.x37 - m.x41 + m.x45 == 0)

m.c10 = Constraint(expr=   m.x42 - m.x46 - m.x50 == 0)

m.c11 = Constraint(expr=   m.x43 - m.x47 - m.x51 == 0)

m.c12 = Constraint(expr=   m.x44 - m.x48 - m.x52 == 0)

m.c13 = Constraint(expr=   m.x45 - m.x49 - m.x53 == 0)

m.c14 = Constraint(expr=   m.x50 - m.x54 - m.x58 - m.x62 == 0)

m.c15 = Constraint(expr=   m.x51 - m.x55 - m.x59 - m.x63 == 0)

m.c16 = Constraint(expr=   m.x52 - m.x56 - m.x60 - m.x64 == 0)

m.c17 = Constraint(expr=   m.x53 - m.x57 - m.x61 - m.x65 == 0)

m.c18 = Constraint(expr=(m.x98/(1e-6 + m.b170) - log(1 + m.x82/(1e-6 + m.b170)))*(1e-6 + m.b170) <= 0)

m.c19 = Constraint(expr=(m.x99/(1e-6 + m.b171) - log(1 + m.x83/(1e-6 + m.b171)))*(1e-6 + m.b171) <= 0)

m.c20 = Constraint(expr=(m.x100/(1e-6 + m.b172) - log(1 + m.x84/(1e-6 + m.b172)))*(1e-6 + m.b172) <= 0)

m.c21 = Constraint(expr=(m.x101/(1e-6 + m.b173) - log(1 + m.x85/(1e-6 + m.b173)))*(1e-6 + m.b173) <= 0)

m.c22 = Constraint(expr=   m.x86 == 0)

m.c23 = Constraint(expr=   m.x87 == 0)

m.c24 = Constraint(expr=   m.x88 == 0)

m.c25 = Constraint(expr=   m.x89 == 0)

m.c26 = Constraint(expr=   m.x102 == 0)

m.c27 = Constraint(expr=   m.x103 == 0)

m.c28 = Constraint(expr=   m.x104 == 0)

m.c29 = Constraint(expr=   m.x105 == 0)

m.c30 = Constraint(expr=   m.x26 - m.x82 - m.x86 == 0)

m.c31 = Constraint(expr=   m.x27 - m.x83 - m.x87 == 0)

m.c32 = Constraint(expr=   m.x28 - m.x84 - m.x88 == 0)

m.c33 = Constraint(expr=   m.x29 - m.x85 - m.x89 == 0)

m.c34 = Constraint(expr=   m.x34 - m.x98 - m.x102 == 0)

m.c35 = Constraint(expr=   m.x35 - m.x99 - m.x103 == 0)

m.c36 = Constraint(expr=   m.x36 - m.x100 - m.x104 == 0)

m.c37 = Constraint(expr=   m.x37 - m.x101 - m.x105 == 0)

m.c38 = Constraint(expr=   m.x82 - 40*m.b170 <= 0)

m.c39 = Constraint(expr=   m.x83 - 40*m.b171 <= 0)

m.c40 = Constraint(expr=   m.x84 - 40*m.b172 <= 0)

m.c41 = Constraint(expr=   m.x85 - 40*m.b173 <= 0)

m.c42 = Constraint(expr=   m.x86 + 40*m.b170 <= 40)

m.c43 = Constraint(expr=   m.x87 + 40*m.b171 <= 40)

m.c44 = Constraint(expr=   m.x88 + 40*m.b172 <= 40)

m.c45 = Constraint(expr=   m.x89 + 40*m.b173 <= 40)

m.c46 = Constraint(expr=   m.x98 - 3.71357206670431*m.b170 <= 0)

m.c47 = Constraint(expr=   m.x99 - 3.71357206670431*m.b171 <= 0)

m.c48 = Constraint(expr=   m.x100 - 3.71357206670431*m.b172 <= 0)

m.c49 = Constraint(expr=   m.x101 - 3.71357206670431*m.b173 <= 0)

m.c50 = Constraint(expr=   m.x102 + 3.71357206670431*m.b170 <= 3.71357206670431)

m.c51 = Constraint(expr=   m.x103 + 3.71357206670431*m.b171 <= 3.71357206670431)

m.c52 = Constraint(expr=   m.x104 + 3.71357206670431*m.b172 <= 3.71357206670431)

m.c53 = Constraint(expr=   m.x105 + 3.71357206670431*m.b173 <= 3.71357206670431)

m.c54 = Constraint(expr=(m.x106/(1e-6 + m.b174) - 1.2*log(1 + m.x90/(1e-6 + m.b174)))*(1e-6 + m.b174) <= 0)

m.c55 = Constraint(expr=(m.x107/(1e-6 + m.b175) - 1.2*log(1 + m.x91/(1e-6 + m.b175)))*(1e-6 + m.b175) <= 0)

m.c56 = Constraint(expr=(m.x108/(1e-6 + m.b176) - 1.2*log(1 + m.x92/(1e-6 + m.b176)))*(1e-6 + m.b176) <= 0)

m.c57 = Constraint(expr=(m.x109/(1e-6 + m.b177) - 1.2*log(1 + m.x93/(1e-6 + m.b177)))*(1e-6 + m.b177) <= 0)

m.c58 = Constraint(expr=   m.x94 == 0)

m.c59 = Constraint(expr=   m.x95 == 0)

m.c60 = Constraint(expr=   m.x96 == 0)

m.c61 = Constraint(expr=   m.x97 == 0)

m.c62 = Constraint(expr=   m.x110 == 0)

m.c63 = Constraint(expr=   m.x111 == 0)

m.c64 = Constraint(expr=   m.x112 == 0)

m.c65 = Constraint(expr=   m.x113 == 0)

m.c66 = Constraint(expr=   m.x30 - m.x90 - m.x94 == 0)

m.c67 = Constraint(expr=   m.x31 - m.x91 - m.x95 == 0)

m.c68 = Constraint(expr=   m.x32 - m.x92 - m.x96 == 0)

m.c69 = Constraint(expr=   m.x33 - m.x93 - m.x97 == 0)

m.c70 = Constraint(expr=   m.x38 - m.x106 - m.x110 == 0)

m.c71 = Constraint(expr=   m.x39 - m.x107 - m.x111 == 0)

m.c72 = Constraint(expr=   m.x40 - m.x108 - m.x112 == 0)

m.c73 = Constraint(expr=   m.x41 - m.x109 - m.x113 == 0)

m.c74 = Constraint(expr=   m.x90 - 40*m.b174 <= 0)

m.c75 = Constraint(expr=   m.x91 - 40*m.b175 <= 0)

m.c76 = Constraint(expr=   m.x92 - 40*m.b176 <= 0)

m.c77 = Constraint(expr=   m.x93 - 40*m.b177 <= 0)

m.c78 = Constraint(expr=   m.x94 + 40*m.b174 <= 40)

m.c79 = Constraint(expr=   m.x95 + 40*m.b175 <= 40)

m.c80 = Constraint(expr=   m.x96 + 40*m.b176 <= 40)

m.c81 = Constraint(expr=   m.x97 + 40*m.b177 <= 40)

m.c82 = Constraint(expr=   m.x106 - 4.45628648004517*m.b174 <= 0)

m.c83 = Constraint(expr=   m.x107 - 4.45628648004517*m.b175 <= 0)

m.c84 = Constraint(expr=   m.x108 - 4.45628648004517*m.b176 <= 0)

m.c85 = Constraint(expr=   m.x109 - 4.45628648004517*m.b177 <= 0)

m.c86 = Constraint(expr=   m.x110 + 4.45628648004517*m.b174 <= 4.45628648004517)

m.c87 = Constraint(expr=   m.x111 + 4.45628648004517*m.b175 <= 4.45628648004517)

m.c88 = Constraint(expr=   m.x112 + 4.45628648004517*m.b176 <= 4.45628648004517)

m.c89 = Constraint(expr=   m.x113 + 4.45628648004517*m.b177 <= 4.45628648004517)

m.c90 = Constraint(expr= - 0.75*m.x114 + m.x146 == 0)

m.c91 = Constraint(expr= - 0.75*m.x115 + m.x147 == 0)

m.c92 = Constraint(expr= - 0.75*m.x116 + m.x148 == 0)

m.c93 = Constraint(expr= - 0.75*m.x117 + m.x149 == 0)

m.c94 = Constraint(expr=   m.x118 == 0)

m.c95 = Constraint(expr=   m.x119 == 0)

m.c96 = Constraint(expr=   m.x120 == 0)

m.c97 = Constraint(expr=   m.x121 == 0)

m.c98 = Constraint(expr=   m.x150 == 0)

m.c99 = Constraint(expr=   m.x151 == 0)

m.c100 = Constraint(expr=   m.x152 == 0)

m.c101 = Constraint(expr=   m.x153 == 0)

m.c102 = Constraint(expr=   m.x54 - m.x114 - m.x118 == 0)

m.c103 = Constraint(expr=   m.x55 - m.x115 - m.x119 == 0)

m.c104 = Constraint(expr=   m.x56 - m.x116 - m.x120 == 0)

m.c105 = Constraint(expr=   m.x57 - m.x117 - m.x121 == 0)

m.c106 = Constraint(expr=   m.x70 - m.x146 - m.x150 == 0)

m.c107 = Constraint(expr=   m.x71 - m.x147 - m.x151 == 0)

m.c108 = Constraint(expr=   m.x72 - m.x148 - m.x152 == 0)

m.c109 = Constraint(expr=   m.x73 - m.x149 - m.x153 == 0)

m.c110 = Constraint(expr=   m.x114 - 4.45628648004517*m.b178 <= 0)

m.c111 = Constraint(expr=   m.x115 - 4.45628648004517*m.b179 <= 0)

m.c112 = Constraint(expr=   m.x116 - 4.45628648004517*m.b180 <= 0)

m.c113 = Constraint(expr=   m.x117 - 4.45628648004517*m.b181 <= 0)

m.c114 = Constraint(expr=   m.x118 + 4.45628648004517*m.b178 <= 4.45628648004517)

m.c115 = Constraint(expr=   m.x119 + 4.45628648004517*m.b179 <= 4.45628648004517)

m.c116 = Constraint(expr=   m.x120 + 4.45628648004517*m.b180 <= 4.45628648004517)

m.c117 = Constraint(expr=   m.x121 + 4.45628648004517*m.b181 <= 4.45628648004517)

m.c118 = Constraint(expr=   m.x146 - 3.34221486003388*m.b178 <= 0)

m.c119 = Constraint(expr=   m.x147 - 3.34221486003388*m.b179 <= 0)

m.c120 = Constraint(expr=   m.x148 - 3.34221486003388*m.b180 <= 0)

m.c121 = Constraint(expr=   m.x149 - 3.34221486003388*m.b181 <= 0)

m.c122 = Constraint(expr=   m.x150 + 3.34221486003388*m.b178 <= 3.34221486003388)

m.c123 = Constraint(expr=   m.x151 + 3.34221486003388*m.b179 <= 3.34221486003388)

m.c124 = Constraint(expr=   m.x152 + 3.34221486003388*m.b180 <= 3.34221486003388)

m.c125 = Constraint(expr=   m.x153 + 3.34221486003388*m.b181 <= 3.34221486003388)

m.c126 = Constraint(expr=(m.x154/(1e-6 + m.b182) - 1.5*log(1 + m.x122/(1e-6 + m.b182)))*(1e-6 + m.b182) <= 0)

m.c127 = Constraint(expr=(m.x155/(1e-6 + m.b183) - 1.5*log(1 + m.x123/(1e-6 + m.b183)))*(1e-6 + m.b183) <= 0)

m.c128 = Constraint(expr=(m.x156/(1e-6 + m.b184) - 1.5*log(1 + m.x124/(1e-6 + m.b184)))*(1e-6 + m.b184) <= 0)

m.c129 = Constraint(expr=(m.x157/(1e-6 + m.b185) - 1.5*log(1 + m.x125/(1e-6 + m.b185)))*(1e-6 + m.b185) <= 0)

m.c130 = Constraint(expr=   m.x126 == 0)

m.c131 = Constraint(expr=   m.x127 == 0)

m.c132 = Constraint(expr=   m.x128 == 0)

m.c133 = Constraint(expr=   m.x129 == 0)

m.c134 = Constraint(expr=   m.x158 == 0)

m.c135 = Constraint(expr=   m.x159 == 0)

m.c136 = Constraint(expr=   m.x160 == 0)

m.c137 = Constraint(expr=   m.x161 == 0)

m.c138 = Constraint(expr=   m.x58 - m.x122 - m.x126 == 0)

m.c139 = Constraint(expr=   m.x59 - m.x123 - m.x127 == 0)

m.c140 = Constraint(expr=   m.x60 - m.x124 - m.x128 == 0)

m.c141 = Constraint(expr=   m.x61 - m.x125 - m.x129 == 0)

m.c142 = Constraint(expr=   m.x74 - m.x154 - m.x158 == 0)

m.c143 = Constraint(expr=   m.x75 - m.x155 - m.x159 == 0)

m.c144 = Constraint(expr=   m.x76 - m.x156 - m.x160 == 0)

m.c145 = Constraint(expr=   m.x77 - m.x157 - m.x161 == 0)

m.c146 = Constraint(expr=   m.x122 - 4.45628648004517*m.b182 <= 0)

m.c147 = Constraint(expr=   m.x123 - 4.45628648004517*m.b183 <= 0)

m.c148 = Constraint(expr=   m.x124 - 4.45628648004517*m.b184 <= 0)

m.c149 = Constraint(expr=   m.x125 - 4.45628648004517*m.b185 <= 0)

m.c150 = Constraint(expr=   m.x126 + 4.45628648004517*m.b182 <= 4.45628648004517)

m.c151 = Constraint(expr=   m.x127 + 4.45628648004517*m.b183 <= 4.45628648004517)

m.c152 = Constraint(expr=   m.x128 + 4.45628648004517*m.b184 <= 4.45628648004517)

m.c153 = Constraint(expr=   m.x129 + 4.45628648004517*m.b185 <= 4.45628648004517)

m.c154 = Constraint(expr=   m.x154 - 2.54515263975353*m.b182 <= 0)

m.c155 = Constraint(expr=   m.x155 - 2.54515263975353*m.b183 <= 0)

m.c156 = Constraint(expr=   m.x156 - 2.54515263975353*m.b184 <= 0)

m.c157 = Constraint(expr=   m.x157 - 2.54515263975353*m.b185 <= 0)

m.c158 = Constraint(expr=   m.x158 + 2.54515263975353*m.b182 <= 2.54515263975353)

m.c159 = Constraint(expr=   m.x159 + 2.54515263975353*m.b183 <= 2.54515263975353)

m.c160 = Constraint(expr=   m.x160 + 2.54515263975353*m.b184 <= 2.54515263975353)

m.c161 = Constraint(expr=   m.x161 + 2.54515263975353*m.b185 <= 2.54515263975353)

m.c162 = Constraint(expr= - m.x130 + m.x162 == 0)

m.c163 = Constraint(expr= - m.x131 + m.x163 == 0)

m.c164 = Constraint(expr= - m.x132 + m.x164 == 0)

m.c165 = Constraint(expr= - m.x133 + m.x165 == 0)

m.c166 = Constraint(expr= - 0.5*m.x138 + m.x162 == 0)

m.c167 = Constraint(expr= - 0.5*m.x139 + m.x163 == 0)

m.c168 = Constraint(expr= - 0.5*m.x140 + m.x164 == 0)

m.c169 = Constraint(expr= - 0.5*m.x141 + m.x165 == 0)

m.c170 = Constraint(expr=   m.x134 == 0)

m.c171 = Constraint(expr=   m.x135 == 0)

m.c172 = Constraint(expr=   m.x136 == 0)

m.c173 = Constraint(expr=   m.x137 == 0)

m.c174 = Constraint(expr=   m.x142 == 0)

m.c175 = Constraint(expr=   m.x143 == 0)

m.c176 = Constraint(expr=   m.x144 == 0)

m.c177 = Constraint(expr=   m.x145 == 0)

m.c178 = Constraint(expr=   m.x166 == 0)

m.c179 = Constraint(expr=   m.x167 == 0)

m.c180 = Constraint(expr=   m.x168 == 0)

m.c181 = Constraint(expr=   m.x169 == 0)

m.c182 = Constraint(expr=   m.x62 - m.x130 - m.x134 == 0)

m.c183 = Constraint(expr=   m.x63 - m.x131 - m.x135 == 0)

m.c184 = Constraint(expr=   m.x64 - m.x132 - m.x136 == 0)

m.c185 = Constraint(expr=   m.x65 - m.x133 - m.x137 == 0)

m.c186 = Constraint(expr=   m.x66 - m.x138 - m.x142 == 0)

m.c187 = Constraint(expr=   m.x67 - m.x139 - m.x143 == 0)

m.c188 = Constraint(expr=   m.x68 - m.x140 - m.x144 == 0)

m.c189 = Constraint(expr=   m.x69 - m.x141 - m.x145 == 0)

m.c190 = Constraint(expr=   m.x78 - m.x162 - m.x166 == 0)

m.c191 = Constraint(expr=   m.x79 - m.x163 - m.x167 == 0)

m.c192 = Constraint(expr=   m.x80 - m.x164 - m.x168 == 0)

m.c193 = Constraint(expr=   m.x81 - m.x165 - m.x169 == 0)

m.c194 = Constraint(expr=   m.x130 - 4.45628648004517*m.b186 <= 0)

m.c195 = Constraint(expr=   m.x131 - 4.45628648004517*m.b187 <= 0)

m.c196 = Constraint(expr=   m.x132 - 4.45628648004517*m.b188 <= 0)

m.c197 = Constraint(expr=   m.x133 - 4.45628648004517*m.b189 <= 0)

m.c198 = Constraint(expr=   m.x134 + 4.45628648004517*m.b186 <= 4.45628648004517)

m.c199 = Constraint(expr=   m.x135 + 4.45628648004517*m.b187 <= 4.45628648004517)

m.c200 = Constraint(expr=   m.x136 + 4.45628648004517*m.b188 <= 4.45628648004517)

m.c201 = Constraint(expr=   m.x137 + 4.45628648004517*m.b189 <= 4.45628648004517)

m.c202 = Constraint(expr=   m.x138 - 30*m.b186 <= 0)

m.c203 = Constraint(expr=   m.x139 - 30*m.b187 <= 0)

m.c204 = Constraint(expr=   m.x140 - 30*m.b188 <= 0)

m.c205 = Constraint(expr=   m.x141 - 30*m.b189 <= 0)

m.c206 = Constraint(expr=   m.x142 + 30*m.b186 <= 30)

m.c207 = Constraint(expr=   m.x143 + 30*m.b187 <= 30)

m.c208 = Constraint(expr=   m.x144 + 30*m.b188 <= 30)

m.c209 = Constraint(expr=   m.x145 + 30*m.b189 <= 30)

m.c210 = Constraint(expr=   m.x162 - 15*m.b186 <= 0)

m.c211 = Constraint(expr=   m.x163 - 15*m.b187 <= 0)

m.c212 = Constraint(expr=   m.x164 - 15*m.b188 <= 0)

m.c213 = Constraint(expr=   m.x165 - 15*m.b189 <= 0)

m.c214 = Constraint(expr=   m.x166 + 15*m.b186 <= 15)

m.c215 = Constraint(expr=   m.x167 + 15*m.b187 <= 15)

m.c216 = Constraint(expr=   m.x168 + 15*m.b188 <= 15)

m.c217 = Constraint(expr=   m.x169 + 15*m.b189 <= 15)

m.c218 = Constraint(expr=   m.x2 + 5*m.b190 == 0)

m.c219 = Constraint(expr=   m.x3 + 4*m.b191 == 0)

m.c220 = Constraint(expr=   m.x4 + 6*m.b192 == 0)

m.c221 = Constraint(expr=   m.x5 + 3*m.b193 == 0)

m.c222 = Constraint(expr=   m.x6 + 8*m.b194 == 0)

m.c223 = Constraint(expr=   m.x7 + 7*m.b195 == 0)

m.c224 = Constraint(expr=   m.x8 + 6*m.b196 == 0)

m.c225 = Constraint(expr=   m.x9 + 5*m.b197 == 0)

m.c226 = Constraint(expr=   m.x10 + 6*m.b198 == 0)

m.c227 = Constraint(expr=   m.x11 + 9*m.b199 == 0)

m.c228 = Constraint(expr=   m.x12 + 4*m.b200 == 0)

m.c229 = Constraint(expr=   m.x13 + 3*m.b201 == 0)

m.c230 = Constraint(expr=   m.x14 + 10*m.b202 == 0)

m.c231 = Constraint(expr=   m.x15 + 9*m.b203 == 0)

m.c232 = Constraint(expr=   m.x16 + 5*m.b204 == 0)

m.c233 = Constraint(expr=   m.x17 + 6*m.b205 == 0)

m.c234 = Constraint(expr=   m.x18 + 6*m.b206 == 0)

m.c235 = Constraint(expr=   m.x19 + 10*m.b207 == 0)

m.c236 = Constraint(expr=   m.x20 + 6*m.b208 == 0)

m.c237 = Constraint(expr=   m.x21 + 9*m.b209 == 0)

m.c238 = Constraint(expr=   m.b170 - m.b171 <= 0)

m.c239 = Constraint(expr=   m.b170 - m.b172 <= 0)

m.c240 = Constraint(expr=   m.b170 - m.b173 <= 0)

m.c241 = Constraint(expr=   m.b171 - m.b172 <= 0)

m.c242 = Constraint(expr=   m.b171 - m.b173 <= 0)

m.c243 = Constraint(expr=   m.b172 - m.b173 <= 0)

m.c244 = Constraint(expr=   m.b174 - m.b175 <= 0)

m.c245 = Constraint(expr=   m.b174 - m.b176 <= 0)

m.c246 = Constraint(expr=   m.b174 - m.b177 <= 0)

m.c247 = Constraint(expr=   m.b175 - m.b176 <= 0)

m.c248 = Constraint(expr=   m.b175 - m.b177 <= 0)

m.c249 = Constraint(expr=   m.b176 - m.b177 <= 0)

m.c250 = Constraint(expr=   m.b178 - m.b179 <= 0)

m.c251 = Constraint(expr=   m.b178 - m.b180 <= 0)

m.c252 = Constraint(expr=   m.b178 - m.b181 <= 0)

m.c253 = Constraint(expr=   m.b179 - m.b180 <= 0)

m.c254 = Constraint(expr=   m.b179 - m.b181 <= 0)

m.c255 = Constraint(expr=   m.b180 - m.b181 <= 0)

m.c256 = Constraint(expr=   m.b182 - m.b183 <= 0)

m.c257 = Constraint(expr=   m.b182 - m.b184 <= 0)

m.c258 = Constraint(expr=   m.b182 - m.b185 <= 0)

m.c259 = Constraint(expr=   m.b183 - m.b184 <= 0)

m.c260 = Constraint(expr=   m.b183 - m.b185 <= 0)

m.c261 = Constraint(expr=   m.b184 - m.b185 <= 0)

m.c262 = Constraint(expr=   m.b186 - m.b187 <= 0)

m.c263 = Constraint(expr=   m.b186 - m.b188 <= 0)

m.c264 = Constraint(expr=   m.b186 - m.b189 <= 0)

m.c265 = Constraint(expr=   m.b187 - m.b188 <= 0)

m.c266 = Constraint(expr=   m.b187 - m.b189 <= 0)

m.c267 = Constraint(expr=   m.b188 - m.b189 <= 0)

m.c268 = Constraint(expr=   m.b190 + m.b191 <= 1)

m.c269 = Constraint(expr=   m.b190 + m.b192 <= 1)

m.c270 = Constraint(expr=   m.b190 + m.b193 <= 1)

m.c271 = Constraint(expr=   m.b190 + m.b191 <= 1)

m.c272 = Constraint(expr=   m.b191 + m.b192 <= 1)

m.c273 = Constraint(expr=   m.b191 + m.b193 <= 1)

m.c274 = Constraint(expr=   m.b190 + m.b192 <= 1)

m.c275 = Constraint(expr=   m.b191 + m.b192 <= 1)

m.c276 = Constraint(expr=   m.b192 + m.b193 <= 1)

m.c277 = Constraint(expr=   m.b190 + m.b193 <= 1)

m.c278 = Constraint(expr=   m.b191 + m.b193 <= 1)

m.c279 = Constraint(expr=   m.b192 + m.b193 <= 1)

m.c280 = Constraint(expr=   m.b194 + m.b195 <= 1)

m.c281 = Constraint(expr=   m.b194 + m.b196 <= 1)

m.c282 = Constraint(expr=   m.b194 + m.b197 <= 1)

m.c283 = Constraint(expr=   m.b194 + m.b195 <= 1)

m.c284 = Constraint(expr=   m.b195 + m.b196 <= 1)

m.c285 = Constraint(expr=   m.b195 + m.b197 <= 1)

m.c286 = Constraint(expr=   m.b194 + m.b196 <= 1)

m.c287 = Constraint(expr=   m.b195 + m.b196 <= 1)

m.c288 = Constraint(expr=   m.b196 + m.b197 <= 1)

m.c289 = Constraint(expr=   m.b194 + m.b197 <= 1)

m.c290 = Constraint(expr=   m.b195 + m.b197 <= 1)

m.c291 = Constraint(expr=   m.b196 + m.b197 <= 1)

m.c292 = Constraint(expr=   m.b198 + m.b199 <= 1)

m.c293 = Constraint(expr=   m.b198 + m.b200 <= 1)

m.c294 = Constraint(expr=   m.b198 + m.b201 <= 1)

m.c295 = Constraint(expr=   m.b198 + m.b199 <= 1)

m.c296 = Constraint(expr=   m.b199 + m.b200 <= 1)

m.c297 = Constraint(expr=   m.b199 + m.b201 <= 1)

m.c298 = Constraint(expr=   m.b198 + m.b200 <= 1)

m.c299 = Constraint(expr=   m.b199 + m.b200 <= 1)

m.c300 = Constraint(expr=   m.b200 + m.b201 <= 1)

m.c301 = Constraint(expr=   m.b198 + m.b201 <= 1)

m.c302 = Constraint(expr=   m.b199 + m.b201 <= 1)

m.c303 = Constraint(expr=   m.b200 + m.b201 <= 1)

m.c304 = Constraint(expr=   m.b202 + m.b203 <= 1)

m.c305 = Constraint(expr=   m.b202 + m.b204 <= 1)

m.c306 = Constraint(expr=   m.b202 + m.b205 <= 1)

m.c307 = Constraint(expr=   m.b202 + m.b203 <= 1)

m.c308 = Constraint(expr=   m.b203 + m.b204 <= 1)

m.c309 = Constraint(expr=   m.b203 + m.b205 <= 1)

m.c310 = Constraint(expr=   m.b202 + m.b204 <= 1)

m.c311 = Constraint(expr=   m.b203 + m.b204 <= 1)

m.c312 = Constraint(expr=   m.b204 + m.b205 <= 1)

m.c313 = Constraint(expr=   m.b202 + m.b205 <= 1)

m.c314 = Constraint(expr=   m.b203 + m.b205 <= 1)

m.c315 = Constraint(expr=   m.b204 + m.b205 <= 1)

m.c316 = Constraint(expr=   m.b206 + m.b207 <= 1)

m.c317 = Constraint(expr=   m.b206 + m.b208 <= 1)

m.c318 = Constraint(expr=   m.b206 + m.b209 <= 1)

m.c319 = Constraint(expr=   m.b206 + m.b207 <= 1)

m.c320 = Constraint(expr=   m.b207 + m.b208 <= 1)

m.c321 = Constraint(expr=   m.b207 + m.b209 <= 1)

m.c322 = Constraint(expr=   m.b206 + m.b208 <= 1)

m.c323 = Constraint(expr=   m.b207 + m.b208 <= 1)

m.c324 = Constraint(expr=   m.b208 + m.b209 <= 1)

m.c325 = Constraint(expr=   m.b206 + m.b209 <= 1)

m.c326 = Constraint(expr=   m.b207 + m.b209 <= 1)

m.c327 = Constraint(expr=   m.b208 + m.b209 <= 1)

m.c328 = Constraint(expr=   m.b170 - m.b190 <= 0)

m.c329 = Constraint(expr= - m.b170 + m.b171 - m.b191 <= 0)

m.c330 = Constraint(expr= - m.b170 - m.b171 + m.b172 - m.b192 <= 0)

m.c331 = Constraint(expr= - m.b170 - m.b171 - m.b172 + m.b173 - m.b193 <= 0)

m.c332 = Constraint(expr=   m.b174 - m.b194 <= 0)

m.c333 = Constraint(expr= - m.b174 + m.b175 - m.b195 <= 0)

m.c334 = Constraint(expr= - m.b174 - m.b175 + m.b176 - m.b196 <= 0)

m.c335 = Constraint(expr= - m.b174 - m.b175 - m.b176 + m.b177 - m.b197 <= 0)

m.c336 = Constraint(expr=   m.b178 - m.b198 <= 0)

m.c337 = Constraint(expr= - m.b178 + m.b179 - m.b199 <= 0)

m.c338 = Constraint(expr= - m.b178 - m.b179 + m.b180 - m.b200 <= 0)

m.c339 = Constraint(expr= - m.b178 - m.b179 - m.b180 + m.b181 - m.b201 <= 0)

m.c340 = Constraint(expr=   m.b182 - m.b202 <= 0)

m.c341 = Constraint(expr= - m.b182 + m.b183 - m.b203 <= 0)

m.c342 = Constraint(expr= - m.b182 - m.b183 + m.b184 - m.b204 <= 0)

m.c343 = Constraint(expr= - m.b182 - m.b183 - m.b184 + m.b185 - m.b205 <= 0)

m.c344 = Constraint(expr=   m.b186 - m.b206 <= 0)

m.c345 = Constraint(expr= - m.b186 + m.b187 - m.b207 <= 0)

m.c346 = Constraint(expr= - m.b186 - m.b187 + m.b188 - m.b208 <= 0)

m.c347 = Constraint(expr= - m.b186 - m.b187 - m.b188 + m.b189 - m.b209 <= 0)

m.c348 = Constraint(expr=   m.b170 + m.b174 == 1)

m.c349 = Constraint(expr=   m.b171 + m.b175 == 1)

m.c350 = Constraint(expr=   m.b172 + m.b176 == 1)

m.c351 = Constraint(expr=   m.b173 + m.b177 == 1)

m.c352 = Constraint(expr=   m.b170 + m.b174 - m.b178 >= 0)

m.c353 = Constraint(expr=   m.b171 + m.b175 - m.b179 >= 0)

m.c354 = Constraint(expr=   m.b172 + m.b176 - m.b180 >= 0)

m.c355 = Constraint(expr=   m.b173 + m.b177 - m.b181 >= 0)

m.c356 = Constraint(expr=   m.b170 + m.b174 - m.b182 >= 0)

m.c357 = Constraint(expr=   m.b171 + m.b175 - m.b183 >= 0)

m.c358 = Constraint(expr=   m.b172 + m.b176 - m.b184 >= 0)

m.c359 = Constraint(expr=   m.b173 + m.b177 - m.b185 >= 0)

m.c360 = Constraint(expr=   m.b170 + m.b174 - m.b186 >= 0)

m.c361 = Constraint(expr=   m.b171 + m.b175 - m.b187 >= 0)

m.c362 = Constraint(expr=   m.b172 + m.b176 - m.b188 >= 0)

m.c363 = Constraint(expr=   m.b173 + m.b177 - m.b189 >= 0)

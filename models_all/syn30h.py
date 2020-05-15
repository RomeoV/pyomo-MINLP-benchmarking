#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        346      161       37      148        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        229      199       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        795      735       60        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x30 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x58 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x2 + 5*m.x8 - 2*m.x13 - 10*m.x30 - 5*m.x31 + 40*m.x38 + 15*m.x39 + 10*m.x40 + 30*m.x41
                        + 35*m.x42 + 20*m.x43 + 25*m.x44 + 15*m.x45 + 30*m.x53 - m.x58 + 80*m.x66 + 285*m.x67
                        + 290*m.x68 + 280*m.x69 + 290*m.x70 + 350*m.x71 - 5*m.b200 - 8*m.b201 - 6*m.b202 - 10*m.b203
                        - 6*m.b204 - 7*m.b205 - 4*m.b206 - 5*m.b207 - 2*m.b208 - 4*m.b209 - 3*m.b210 - 7*m.b211
                        - 3*m.b212 - 2*m.b213 - 4*m.b214 - 2*m.b215 - 3*m.b216 - 5*m.b217 - 2*m.b218 - m.b219 - 2*m.b220
                        - 9*m.b221 - 5*m.b222 - 2*m.b223 - 10*m.b224 - 4*m.b225 - 7*m.b226 - 4*m.b227 - 2*m.b228
                        - 8*m.b229, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c3 = Constraint(expr= - m.x5 - m.x6 + m.x7 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c5 = Constraint(expr=   m.x9 - m.x10 - m.x11 - m.x12 == 0)

m.c6 = Constraint(expr=   m.x14 - m.x17 - m.x18 == 0)

m.c7 = Constraint(expr=   m.x16 - m.x19 - m.x20 - m.x21 == 0)

m.c8 = Constraint(expr=   m.x24 - m.x28 - m.x29 == 0)

m.c9 = Constraint(expr= - m.x25 - m.x31 + m.x32 == 0)

m.c10 = Constraint(expr=   m.x26 - m.x33 - m.x34 == 0)

m.c11 = Constraint(expr=   m.x27 - m.x35 - m.x36 - m.x37 == 0)

m.c12 = Constraint(expr=   m.x46 - m.x47 == 0)

m.c13 = Constraint(expr=   m.x47 - m.x48 - m.x49 == 0)

m.c14 = Constraint(expr= - m.x50 - m.x51 + m.x52 == 0)

m.c15 = Constraint(expr=   m.x52 - m.x53 - m.x54 == 0)

m.c16 = Constraint(expr=   m.x54 - m.x55 - m.x56 - m.x57 == 0)

m.c17 = Constraint(expr=   m.x59 - m.x62 - m.x63 == 0)

m.c18 = Constraint(expr=   m.x61 - m.x64 - m.x65 - m.x66 == 0)

m.c19 = Constraint(expr=(m.x76/(1e-6 + m.b200) - log(1 + m.x72/(1e-6 + m.b200)))*(1e-6 + m.b200) <= 0)

m.c20 = Constraint(expr=   m.x73 == 0)

m.c21 = Constraint(expr=   m.x77 == 0)

m.c22 = Constraint(expr=   m.x3 - m.x72 - m.x73 == 0)

m.c23 = Constraint(expr=   m.x5 - m.x76 - m.x77 == 0)

m.c24 = Constraint(expr=   m.x72 - 40*m.b200 <= 0)

m.c25 = Constraint(expr=   m.x73 + 40*m.b200 <= 40)

m.c26 = Constraint(expr=   m.x76 - 3.71357206670431*m.b200 <= 0)

m.c27 = Constraint(expr=   m.x77 + 3.71357206670431*m.b200 <= 3.71357206670431)

m.c28 = Constraint(expr=(m.x78/(1e-6 + m.b201) - 1.2*log(1 + m.x74/(1e-6 + m.b201)))*(1e-6 + m.b201) <= 0)

m.c29 = Constraint(expr=   m.x75 == 0)

m.c30 = Constraint(expr=   m.x79 == 0)

m.c31 = Constraint(expr=   m.x4 - m.x74 - m.x75 == 0)

m.c32 = Constraint(expr=   m.x6 - m.x78 - m.x79 == 0)

m.c33 = Constraint(expr=   m.x74 - 40*m.b201 <= 0)

m.c34 = Constraint(expr=   m.x75 + 40*m.b201 <= 40)

m.c35 = Constraint(expr=   m.x78 - 4.45628648004517*m.b201 <= 0)

m.c36 = Constraint(expr=   m.x79 + 4.45628648004517*m.b201 <= 4.45628648004517)

m.c37 = Constraint(expr= - 0.75*m.x80 + m.x88 == 0)

m.c38 = Constraint(expr=   m.x81 == 0)

m.c39 = Constraint(expr=   m.x89 == 0)

m.c40 = Constraint(expr=   m.x10 - m.x80 - m.x81 == 0)

m.c41 = Constraint(expr=   m.x14 - m.x88 - m.x89 == 0)

m.c42 = Constraint(expr=   m.x80 - 4.45628648004517*m.b202 <= 0)

m.c43 = Constraint(expr=   m.x81 + 4.45628648004517*m.b202 <= 4.45628648004517)

m.c44 = Constraint(expr=   m.x88 - 3.34221486003388*m.b202 <= 0)

m.c45 = Constraint(expr=   m.x89 + 3.34221486003388*m.b202 <= 3.34221486003388)

m.c46 = Constraint(expr=(m.x90/(1e-6 + m.b203) - 1.5*log(1 + m.x82/(1e-6 + m.b203)))*(1e-6 + m.b203) <= 0)

m.c47 = Constraint(expr=   m.x83 == 0)

m.c48 = Constraint(expr=   m.x92 == 0)

m.c49 = Constraint(expr=   m.x11 - m.x82 - m.x83 == 0)

m.c50 = Constraint(expr=   m.x15 - m.x90 - m.x92 == 0)

m.c51 = Constraint(expr=   m.x82 - 4.45628648004517*m.b203 <= 0)

m.c52 = Constraint(expr=   m.x83 + 4.45628648004517*m.b203 <= 4.45628648004517)

m.c53 = Constraint(expr=   m.x90 - 2.54515263975353*m.b203 <= 0)

m.c54 = Constraint(expr=   m.x92 + 2.54515263975353*m.b203 <= 2.54515263975353)

m.c55 = Constraint(expr= - m.x84 + m.x94 == 0)

m.c56 = Constraint(expr= - 0.5*m.x86 + m.x94 == 0)

m.c57 = Constraint(expr=   m.x85 == 0)

m.c58 = Constraint(expr=   m.x87 == 0)

m.c59 = Constraint(expr=   m.x95 == 0)

m.c60 = Constraint(expr=   m.x12 - m.x84 - m.x85 == 0)

m.c61 = Constraint(expr=   m.x13 - m.x86 - m.x87 == 0)

m.c62 = Constraint(expr=   m.x16 - m.x94 - m.x95 == 0)

m.c63 = Constraint(expr=   m.x84 - 4.45628648004517*m.b204 <= 0)

m.c64 = Constraint(expr=   m.x85 + 4.45628648004517*m.b204 <= 4.45628648004517)

m.c65 = Constraint(expr=   m.x86 - 30*m.b204 <= 0)

m.c66 = Constraint(expr=   m.x87 + 30*m.b204 <= 30)

m.c67 = Constraint(expr=   m.x94 - 15*m.b204 <= 0)

m.c68 = Constraint(expr=   m.x95 + 15*m.b204 <= 15)

m.c69 = Constraint(expr=(m.x106/(1e-6 + m.b205) - 1.25*log(1 + m.x96/(1e-6 + m.b205)))*(1e-6 + m.b205) <= 0)

m.c70 = Constraint(expr=   m.x97 == 0)

m.c71 = Constraint(expr=   m.x108 == 0)

m.c72 = Constraint(expr=   m.x17 - m.x96 - m.x97 == 0)

m.c73 = Constraint(expr=   m.x22 - m.x106 - m.x108 == 0)

m.c74 = Constraint(expr=   m.x96 - 3.34221486003388*m.b205 <= 0)

m.c75 = Constraint(expr=   m.x97 + 3.34221486003388*m.b205 <= 3.34221486003388)

m.c76 = Constraint(expr=   m.x106 - 1.83548069293539*m.b205 <= 0)

m.c77 = Constraint(expr=   m.x108 + 1.83548069293539*m.b205 <= 1.83548069293539)

m.c78 = Constraint(expr=(m.x110/(1e-6 + m.b206) - 0.9*log(1 + m.x98/(1e-6 + m.b206)))*(1e-6 + m.b206) <= 0)

m.c79 = Constraint(expr=   m.x99 == 0)

m.c80 = Constraint(expr=   m.x112 == 0)

m.c81 = Constraint(expr=   m.x18 - m.x98 - m.x99 == 0)

m.c82 = Constraint(expr=   m.x23 - m.x110 - m.x112 == 0)

m.c83 = Constraint(expr=   m.x98 - 3.34221486003388*m.b206 <= 0)

m.c84 = Constraint(expr=   m.x99 + 3.34221486003388*m.b206 <= 3.34221486003388)

m.c85 = Constraint(expr=   m.x110 - 1.32154609891348*m.b206 <= 0)

m.c86 = Constraint(expr=   m.x112 + 1.32154609891348*m.b206 <= 1.32154609891348)

m.c87 = Constraint(expr=(m.x114/(1e-6 + m.b207) - log(1 + m.x91/(1e-6 + m.b207)))*(1e-6 + m.b207) <= 0)

m.c88 = Constraint(expr=   m.x93 == 0)

m.c89 = Constraint(expr=   m.x115 == 0)

m.c90 = Constraint(expr=   m.x15 - m.x91 - m.x93 == 0)

m.c91 = Constraint(expr=   m.x24 - m.x114 - m.x115 == 0)

m.c92 = Constraint(expr=   m.x91 - 2.54515263975353*m.b207 <= 0)

m.c93 = Constraint(expr=   m.x93 + 2.54515263975353*m.b207 <= 2.54515263975353)

m.c94 = Constraint(expr=   m.x114 - 1.26558121681553*m.b207 <= 0)

m.c95 = Constraint(expr=   m.x115 + 1.26558121681553*m.b207 <= 1.26558121681553)

m.c96 = Constraint(expr= - 0.9*m.x100 + m.x116 == 0)

m.c97 = Constraint(expr=   m.x101 == 0)

m.c98 = Constraint(expr=   m.x117 == 0)

m.c99 = Constraint(expr=   m.x19 - m.x100 - m.x101 == 0)

m.c100 = Constraint(expr=   m.x25 - m.x116 - m.x117 == 0)

m.c101 = Constraint(expr=   m.x100 - 15*m.b208 <= 0)

m.c102 = Constraint(expr=   m.x101 + 15*m.b208 <= 15)

m.c103 = Constraint(expr=   m.x116 - 13.5*m.b208 <= 0)

m.c104 = Constraint(expr=   m.x117 + 13.5*m.b208 <= 13.5)

m.c105 = Constraint(expr= - 0.6*m.x102 + m.x118 == 0)

m.c106 = Constraint(expr=   m.x103 == 0)

m.c107 = Constraint(expr=   m.x119 == 0)

m.c108 = Constraint(expr=   m.x20 - m.x102 - m.x103 == 0)

m.c109 = Constraint(expr=   m.x26 - m.x118 - m.x119 == 0)

m.c110 = Constraint(expr=   m.x102 - 15*m.b209 <= 0)

m.c111 = Constraint(expr=   m.x103 + 15*m.b209 <= 15)

m.c112 = Constraint(expr=   m.x118 - 9*m.b209 <= 0)

m.c113 = Constraint(expr=   m.x119 + 9*m.b209 <= 9)

m.c114 = Constraint(expr=(m.x120/(1e-6 + m.b210) - 1.1*log(1 + m.x104/(1e-6 + m.b210)))*(1e-6 + m.b210) <= 0)

m.c115 = Constraint(expr=   m.x105 == 0)

m.c116 = Constraint(expr=   m.x121 == 0)

m.c117 = Constraint(expr=   m.x21 - m.x104 - m.x105 == 0)

m.c118 = Constraint(expr=   m.x27 - m.x120 - m.x121 == 0)

m.c119 = Constraint(expr=   m.x104 - 15*m.b210 <= 0)

m.c120 = Constraint(expr=   m.x105 + 15*m.b210 <= 15)

m.c121 = Constraint(expr=   m.x120 - 3.04984759446376*m.b210 <= 0)

m.c122 = Constraint(expr=   m.x121 + 3.04984759446376*m.b210 <= 3.04984759446376)

m.c123 = Constraint(expr= - 0.9*m.x107 + m.x140 == 0)

m.c124 = Constraint(expr= - m.x126 + m.x140 == 0)

m.c125 = Constraint(expr=   m.x109 == 0)

m.c126 = Constraint(expr=   m.x127 == 0)

m.c127 = Constraint(expr=   m.x141 == 0)

m.c128 = Constraint(expr=   m.x22 - m.x107 - m.x109 == 0)

m.c129 = Constraint(expr=   m.x30 - m.x126 - m.x127 == 0)

m.c130 = Constraint(expr=   m.x38 - m.x140 - m.x141 == 0)

m.c131 = Constraint(expr=   m.x107 - 1.83548069293539*m.b211 <= 0)

m.c132 = Constraint(expr=   m.x109 + 1.83548069293539*m.b211 <= 1.83548069293539)

m.c133 = Constraint(expr=   m.x126 - 20*m.b211 <= 0)

m.c134 = Constraint(expr=   m.x127 + 20*m.b211 <= 20)

m.c135 = Constraint(expr=   m.x140 - 20*m.b211 <= 0)

m.c136 = Constraint(expr=   m.x141 + 20*m.b211 <= 20)

m.c137 = Constraint(expr=(m.x142/(1e-6 + m.b212) - log(1 + m.x111/(1e-6 + m.b212)))*(1e-6 + m.b212) <= 0)

m.c138 = Constraint(expr=   m.x113 == 0)

m.c139 = Constraint(expr=   m.x143 == 0)

m.c140 = Constraint(expr=   m.x23 - m.x111 - m.x113 == 0)

m.c141 = Constraint(expr=   m.x39 - m.x142 - m.x143 == 0)

m.c142 = Constraint(expr=   m.x111 - 1.32154609891348*m.b212 <= 0)

m.c143 = Constraint(expr=   m.x113 + 1.32154609891348*m.b212 <= 1.32154609891348)

m.c144 = Constraint(expr=   m.x142 - 0.842233385663186*m.b212 <= 0)

m.c145 = Constraint(expr=   m.x143 + 0.842233385663186*m.b212 <= 0.842233385663186)

m.c146 = Constraint(expr=(m.x144/(1e-6 + m.b213) - 0.7*log(1 + m.x122/(1e-6 + m.b213)))*(1e-6 + m.b213) <= 0)

m.c147 = Constraint(expr=   m.x123 == 0)

m.c148 = Constraint(expr=   m.x145 == 0)

m.c149 = Constraint(expr=   m.x28 - m.x122 - m.x123 == 0)

m.c150 = Constraint(expr=   m.x40 - m.x144 - m.x145 == 0)

m.c151 = Constraint(expr=   m.x122 - 1.26558121681553*m.b213 <= 0)

m.c152 = Constraint(expr=   m.x123 + 1.26558121681553*m.b213 <= 1.26558121681553)

m.c153 = Constraint(expr=   m.x144 - 0.572481933717686*m.b213 <= 0)

m.c154 = Constraint(expr=   m.x145 + 0.572481933717686*m.b213 <= 0.572481933717686)

m.c155 = Constraint(expr=(m.x146/(1e-6 + m.b214) - 0.65*log(1 + m.x124/(1e-6 + m.b214)))*(1e-6 + m.b214) <= 0)

m.c156 = Constraint(expr=(m.x146/(1e-6 + m.b214) - 0.65*log(1 + m.x128/(1e-6 + m.b214)))*(1e-6 + m.b214) <= 0)

m.c157 = Constraint(expr=   m.x125 == 0)

m.c158 = Constraint(expr=   m.x129 == 0)

m.c159 = Constraint(expr=   m.x147 == 0)

m.c160 = Constraint(expr=   m.x29 - m.x124 - m.x125 == 0)

m.c161 = Constraint(expr=   m.x32 - m.x128 - m.x129 == 0)

m.c162 = Constraint(expr=   m.x41 - m.x146 - m.x147 == 0)

m.c163 = Constraint(expr=   m.x124 - 1.26558121681553*m.b214 <= 0)

m.c164 = Constraint(expr=   m.x125 + 1.26558121681553*m.b214 <= 1.26558121681553)

m.c165 = Constraint(expr=   m.x128 - 33.5*m.b214 <= 0)

m.c166 = Constraint(expr=   m.x129 + 33.5*m.b214 <= 33.5)

m.c167 = Constraint(expr=   m.x146 - 2.30162356062425*m.b214 <= 0)

m.c168 = Constraint(expr=   m.x147 + 2.30162356062425*m.b214 <= 2.30162356062425)

m.c169 = Constraint(expr= - m.x130 + m.x148 == 0)

m.c170 = Constraint(expr=   m.x131 == 0)

m.c171 = Constraint(expr=   m.x149 == 0)

m.c172 = Constraint(expr=   m.x33 - m.x130 - m.x131 == 0)

m.c173 = Constraint(expr=   m.x42 - m.x148 - m.x149 == 0)

m.c174 = Constraint(expr=   m.x130 - 9*m.b215 <= 0)

m.c175 = Constraint(expr=   m.x131 + 9*m.b215 <= 9)

m.c176 = Constraint(expr=   m.x148 - 9*m.b215 <= 0)

m.c177 = Constraint(expr=   m.x149 + 9*m.b215 <= 9)

m.c178 = Constraint(expr= - m.x132 + m.x150 == 0)

m.c179 = Constraint(expr=   m.x133 == 0)

m.c180 = Constraint(expr=   m.x151 == 0)

m.c181 = Constraint(expr=   m.x34 - m.x132 - m.x133 == 0)

m.c182 = Constraint(expr=   m.x43 - m.x150 - m.x151 == 0)

m.c183 = Constraint(expr=   m.x132 - 9*m.b216 <= 0)

m.c184 = Constraint(expr=   m.x133 + 9*m.b216 <= 9)

m.c185 = Constraint(expr=   m.x150 - 9*m.b216 <= 0)

m.c186 = Constraint(expr=   m.x151 + 9*m.b216 <= 9)

m.c187 = Constraint(expr=(m.x152/(1e-6 + m.b217) - 0.75*log(1 + m.x134/(1e-6 + m.b217)))*(1e-6 + m.b217) <= 0)

m.c188 = Constraint(expr=   m.x135 == 0)

m.c189 = Constraint(expr=   m.x153 == 0)

m.c190 = Constraint(expr=   m.x35 - m.x134 - m.x135 == 0)

m.c191 = Constraint(expr=   m.x44 - m.x152 - m.x153 == 0)

m.c192 = Constraint(expr=   m.x134 - 3.04984759446376*m.b217 <= 0)

m.c193 = Constraint(expr=   m.x135 + 3.04984759446376*m.b217 <= 3.04984759446376)

m.c194 = Constraint(expr=   m.x152 - 1.04900943706034*m.b217 <= 0)

m.c195 = Constraint(expr=   m.x153 + 1.04900943706034*m.b217 <= 1.04900943706034)

m.c196 = Constraint(expr=(m.x154/(1e-6 + m.b218) - 0.8*log(1 + m.x136/(1e-6 + m.b218)))*(1e-6 + m.b218) <= 0)

m.c197 = Constraint(expr=   m.x137 == 0)

m.c198 = Constraint(expr=   m.x155 == 0)

m.c199 = Constraint(expr=   m.x36 - m.x136 - m.x137 == 0)

m.c200 = Constraint(expr=   m.x45 - m.x154 - m.x155 == 0)

m.c201 = Constraint(expr=   m.x136 - 3.04984759446376*m.b218 <= 0)

m.c202 = Constraint(expr=   m.x137 + 3.04984759446376*m.b218 <= 3.04984759446376)

m.c203 = Constraint(expr=   m.x154 - 1.11894339953103*m.b218 <= 0)

m.c204 = Constraint(expr=   m.x155 + 1.11894339953103*m.b218 <= 1.11894339953103)

m.c205 = Constraint(expr=(m.x156/(1e-6 + m.b219) - 0.85*log(1 + m.x138/(1e-6 + m.b219)))*(1e-6 + m.b219) <= 0)

m.c206 = Constraint(expr=   m.x139 == 0)

m.c207 = Constraint(expr=   m.x157 == 0)

m.c208 = Constraint(expr=   m.x37 - m.x138 - m.x139 == 0)

m.c209 = Constraint(expr=   m.x46 - m.x156 - m.x157 == 0)

m.c210 = Constraint(expr=   m.x138 - 3.04984759446376*m.b219 <= 0)

m.c211 = Constraint(expr=   m.x139 + 3.04984759446376*m.b219 <= 3.04984759446376)

m.c212 = Constraint(expr=   m.x156 - 1.18887736200171*m.b219 <= 0)

m.c213 = Constraint(expr=   m.x157 + 1.18887736200171*m.b219 <= 1.18887736200171)

m.c214 = Constraint(expr=(m.x162/(1e-6 + m.b220) - log(1 + m.x158/(1e-6 + m.b220)))*(1e-6 + m.b220) <= 0)

m.c215 = Constraint(expr=   m.x159 == 0)

m.c216 = Constraint(expr=   m.x163 == 0)

m.c217 = Constraint(expr=   m.x48 - m.x158 - m.x159 == 0)

m.c218 = Constraint(expr=   m.x50 - m.x162 - m.x163 == 0)

m.c219 = Constraint(expr=   m.x158 - 1.18887736200171*m.b220 <= 0)

m.c220 = Constraint(expr=   m.x159 + 1.18887736200171*m.b220 <= 1.18887736200171)

m.c221 = Constraint(expr=   m.x162 - 0.78338879230327*m.b220 <= 0)

m.c222 = Constraint(expr=   m.x163 + 0.78338879230327*m.b220 <= 0.78338879230327)

m.c223 = Constraint(expr=(m.x164/(1e-6 + m.b221) - 1.2*log(1 + m.x160/(1e-6 + m.b221)))*(1e-6 + m.b221) <= 0)

m.c224 = Constraint(expr=   m.x161 == 0)

m.c225 = Constraint(expr=   m.x165 == 0)

m.c226 = Constraint(expr=   m.x49 - m.x160 - m.x161 == 0)

m.c227 = Constraint(expr=   m.x51 - m.x164 - m.x165 == 0)

m.c228 = Constraint(expr=   m.x160 - 1.18887736200171*m.b221 <= 0)

m.c229 = Constraint(expr=   m.x161 + 1.18887736200171*m.b221 <= 1.18887736200171)

m.c230 = Constraint(expr=   m.x164 - 0.940066550763924*m.b221 <= 0)

m.c231 = Constraint(expr=   m.x165 + 0.940066550763924*m.b221 <= 0.940066550763924)

m.c232 = Constraint(expr= - 0.75*m.x166 + m.x174 == 0)

m.c233 = Constraint(expr=   m.x167 == 0)

m.c234 = Constraint(expr=   m.x175 == 0)

m.c235 = Constraint(expr=   m.x55 - m.x166 - m.x167 == 0)

m.c236 = Constraint(expr=   m.x59 - m.x174 - m.x175 == 0)

m.c237 = Constraint(expr=   m.x166 - 0.940066550763924*m.b222 <= 0)

m.c238 = Constraint(expr=   m.x167 + 0.940066550763924*m.b222 <= 0.940066550763924)

m.c239 = Constraint(expr=   m.x174 - 0.705049913072943*m.b222 <= 0)

m.c240 = Constraint(expr=   m.x175 + 0.705049913072943*m.b222 <= 0.705049913072943)

m.c241 = Constraint(expr=(m.x176/(1e-6 + m.b223) - 1.5*log(1 + m.x168/(1e-6 + m.b223)))*(1e-6 + m.b223) <= 0)

m.c242 = Constraint(expr=   m.x169 == 0)

m.c243 = Constraint(expr=   m.x178 == 0)

m.c244 = Constraint(expr=   m.x56 - m.x168 - m.x169 == 0)

m.c245 = Constraint(expr=   m.x60 - m.x176 - m.x178 == 0)

m.c246 = Constraint(expr=   m.x168 - 0.940066550763924*m.b223 <= 0)

m.c247 = Constraint(expr=   m.x169 + 0.940066550763924*m.b223 <= 0.940066550763924)

m.c248 = Constraint(expr=   m.x176 - 0.994083415506506*m.b223 <= 0)

m.c249 = Constraint(expr=   m.x178 + 0.994083415506506*m.b223 <= 0.994083415506506)

m.c250 = Constraint(expr= - m.x170 + m.x180 == 0)

m.c251 = Constraint(expr= - 0.5*m.x172 + m.x180 == 0)

m.c252 = Constraint(expr=   m.x171 == 0)

m.c253 = Constraint(expr=   m.x173 == 0)

m.c254 = Constraint(expr=   m.x181 == 0)

m.c255 = Constraint(expr=   m.x57 - m.x170 - m.x171 == 0)

m.c256 = Constraint(expr=   m.x58 - m.x172 - m.x173 == 0)

m.c257 = Constraint(expr=   m.x61 - m.x180 - m.x181 == 0)

m.c258 = Constraint(expr=   m.x170 - 0.940066550763924*m.b224 <= 0)

m.c259 = Constraint(expr=   m.x171 + 0.940066550763924*m.b224 <= 0.940066550763924)

m.c260 = Constraint(expr=   m.x172 - 30*m.b224 <= 0)

m.c261 = Constraint(expr=   m.x173 + 30*m.b224 <= 30)

m.c262 = Constraint(expr=   m.x180 - 15*m.b224 <= 0)

m.c263 = Constraint(expr=   m.x181 + 15*m.b224 <= 15)

m.c264 = Constraint(expr=(m.x190/(1e-6 + m.b225) - 1.25*log(1 + m.x182/(1e-6 + m.b225)))*(1e-6 + m.b225) <= 0)

m.c265 = Constraint(expr=   m.x183 == 0)

m.c266 = Constraint(expr=   m.x191 == 0)

m.c267 = Constraint(expr=   m.x62 - m.x182 - m.x183 == 0)

m.c268 = Constraint(expr=   m.x67 - m.x190 - m.x191 == 0)

m.c269 = Constraint(expr=   m.x182 - 0.705049913072943*m.b225 <= 0)

m.c270 = Constraint(expr=   m.x183 + 0.705049913072943*m.b225 <= 0.705049913072943)

m.c271 = Constraint(expr=   m.x190 - 0.666992981045719*m.b225 <= 0)

m.c272 = Constraint(expr=   m.x191 + 0.666992981045719*m.b225 <= 0.666992981045719)

m.c273 = Constraint(expr=(m.x192/(1e-6 + m.b226) - 0.9*log(1 + m.x184/(1e-6 + m.b226)))*(1e-6 + m.b226) <= 0)

m.c274 = Constraint(expr=   m.x185 == 0)

m.c275 = Constraint(expr=   m.x193 == 0)

m.c276 = Constraint(expr=   m.x63 - m.x184 - m.x185 == 0)

m.c277 = Constraint(expr=   m.x68 - m.x192 - m.x193 == 0)

m.c278 = Constraint(expr=   m.x184 - 0.705049913072943*m.b226 <= 0)

m.c279 = Constraint(expr=   m.x185 + 0.705049913072943*m.b226 <= 0.705049913072943)

m.c280 = Constraint(expr=   m.x192 - 0.480234946352917*m.b226 <= 0)

m.c281 = Constraint(expr=   m.x193 + 0.480234946352917*m.b226 <= 0.480234946352917)

m.c282 = Constraint(expr=(m.x194/(1e-6 + m.b227) - log(1 + m.x177/(1e-6 + m.b227)))*(1e-6 + m.b227) <= 0)

m.c283 = Constraint(expr=   m.x179 == 0)

m.c284 = Constraint(expr=   m.x195 == 0)

m.c285 = Constraint(expr=   m.x60 - m.x177 - m.x179 == 0)

m.c286 = Constraint(expr=   m.x69 - m.x194 - m.x195 == 0)

m.c287 = Constraint(expr=   m.x177 - 0.994083415506506*m.b227 <= 0)

m.c288 = Constraint(expr=   m.x179 + 0.994083415506506*m.b227 <= 0.994083415506506)

m.c289 = Constraint(expr=   m.x194 - 0.690184503917672*m.b227 <= 0)

m.c290 = Constraint(expr=   m.x195 + 0.690184503917672*m.b227 <= 0.690184503917672)

m.c291 = Constraint(expr= - 0.9*m.x186 + m.x196 == 0)

m.c292 = Constraint(expr=   m.x187 == 0)

m.c293 = Constraint(expr=   m.x197 == 0)

m.c294 = Constraint(expr=   m.x64 - m.x186 - m.x187 == 0)

m.c295 = Constraint(expr=   m.x70 - m.x196 - m.x197 == 0)

m.c296 = Constraint(expr=   m.x186 - 15*m.b228 <= 0)

m.c297 = Constraint(expr=   m.x187 + 15*m.b228 <= 15)

m.c298 = Constraint(expr=   m.x196 - 13.5*m.b228 <= 0)

m.c299 = Constraint(expr=   m.x197 + 13.5*m.b228 <= 13.5)

m.c300 = Constraint(expr= - 0.6*m.x188 + m.x198 == 0)

m.c301 = Constraint(expr=   m.x189 == 0)

m.c302 = Constraint(expr=   m.x199 == 0)

m.c303 = Constraint(expr=   m.x65 - m.x188 - m.x189 == 0)

m.c304 = Constraint(expr=   m.x71 - m.x198 - m.x199 == 0)

m.c305 = Constraint(expr=   m.x188 - 15*m.b229 <= 0)

m.c306 = Constraint(expr=   m.x189 + 15*m.b229 <= 15)

m.c307 = Constraint(expr=   m.x198 - 9*m.b229 <= 0)

m.c308 = Constraint(expr=   m.x199 + 9*m.b229 <= 9)

m.c309 = Constraint(expr=   m.b200 + m.b201 == 1)

m.c310 = Constraint(expr= - m.b202 + m.b205 + m.b206 >= 0)

m.c311 = Constraint(expr= - m.b205 + m.b211 >= 0)

m.c312 = Constraint(expr= - m.b206 + m.b212 >= 0)

m.c313 = Constraint(expr= - m.b203 + m.b207 >= 0)

m.c314 = Constraint(expr= - m.b207 + m.b213 + m.b214 >= 0)

m.c315 = Constraint(expr= - m.b204 + m.b208 + m.b209 + m.b210 >= 0)

m.c316 = Constraint(expr= - m.b208 + m.b214 >= 0)

m.c317 = Constraint(expr= - m.b209 + m.b215 + m.b216 >= 0)

m.c318 = Constraint(expr= - m.b210 + m.b217 + m.b218 + m.b219 >= 0)

m.c319 = Constraint(expr=   m.b200 + m.b201 - m.b202 >= 0)

m.c320 = Constraint(expr=   m.b200 + m.b201 - m.b203 >= 0)

m.c321 = Constraint(expr=   m.b200 + m.b201 - m.b204 >= 0)

m.c322 = Constraint(expr=   m.b202 - m.b205 >= 0)

m.c323 = Constraint(expr=   m.b202 - m.b206 >= 0)

m.c324 = Constraint(expr=   m.b203 - m.b207 >= 0)

m.c325 = Constraint(expr=   m.b204 - m.b208 >= 0)

m.c326 = Constraint(expr=   m.b204 - m.b209 >= 0)

m.c327 = Constraint(expr=   m.b204 - m.b210 >= 0)

m.c328 = Constraint(expr=   m.b205 - m.b211 >= 0)

m.c329 = Constraint(expr=   m.b206 - m.b212 >= 0)

m.c330 = Constraint(expr=   m.b207 - m.b213 >= 0)

m.c331 = Constraint(expr=   m.b207 - m.b214 >= 0)

m.c332 = Constraint(expr=   m.b209 - m.b215 >= 0)

m.c333 = Constraint(expr=   m.b209 - m.b216 >= 0)

m.c334 = Constraint(expr=   m.b210 - m.b217 >= 0)

m.c335 = Constraint(expr=   m.b210 - m.b218 >= 0)

m.c336 = Constraint(expr=   m.b210 - m.b219 >= 0)

m.c337 = Constraint(expr= - m.b219 + m.b220 + m.b221 >= 0)

m.c338 = Constraint(expr= - m.b222 + m.b225 + m.b226 >= 0)

m.c339 = Constraint(expr= - m.b223 + m.b227 >= 0)

m.c340 = Constraint(expr=   m.b219 - m.b220 >= 0)

m.c341 = Constraint(expr=   m.b219 - m.b221 >= 0)

m.c342 = Constraint(expr=   m.b222 - m.b225 >= 0)

m.c343 = Constraint(expr=   m.b222 - m.b226 >= 0)

m.c344 = Constraint(expr=   m.b223 - m.b227 >= 0)

m.c345 = Constraint(expr=   m.b224 - m.b228 >= 0)

m.c346 = Constraint(expr=   m.b224 - m.b229 >= 0)

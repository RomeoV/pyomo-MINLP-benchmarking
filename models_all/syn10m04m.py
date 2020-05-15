#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        517       29      100      388        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        221      141       80        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1281     1257       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x46 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x182 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x217 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 - m.x5 + 5*m.x26 + 10*m.x27 + 5*m.x28 + 10*m.x29 - 2*m.x46 - m.x47
                        - 2*m.x48 - m.x49 + 80*m.x78 + 90*m.x79 + 120*m.x80 + 100*m.x81 + 285*m.x82 + 390*m.x83
                        + 350*m.x84 + 300*m.x85 + 290*m.x86 + 405*m.x87 + 190*m.x88 + 340*m.x89 + 280*m.x90 + 400*m.x91
                        + 430*m.x92 + 260*m.x93 + 290*m.x94 + 300*m.x95 + 240*m.x96 + 310*m.x97 + 350*m.x98 + 250*m.x99
                        + 300*m.x100 + 400*m.x101 - 5*m.b142 - 4*m.b143 - 6*m.b144 - 3*m.b145 - 8*m.b146 - 7*m.b147
                        - 6*m.b148 - 5*m.b149 - 6*m.b150 - 9*m.b151 - 4*m.b152 - 3*m.b153 - 10*m.b154 - 9*m.b155
                        - 5*m.b156 - 6*m.b157 - 6*m.b158 - 10*m.b159 - 6*m.b160 - 9*m.b161 - 7*m.b162 - 7*m.b163
                        - 4*m.b164 - 2*m.b165 - 4*m.b166 - 3*m.b167 - 2*m.b168 - 8*m.b169 - 5*m.b170 - 6*m.b171
                        - 7*m.b172 - 4*m.b173 - 2*m.b174 - 5*m.b175 - 2*m.b176 - 6*m.b177 - 4*m.b178 - 7*m.b179
                        - 4*m.b180 - 7*m.b181, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x6 - m.x10 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x7 - m.x11 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x8 - m.x12 == 0)

m.c5 = Constraint(expr=   m.x5 - m.x9 - m.x13 == 0)

m.c6 = Constraint(expr= - m.x14 - m.x18 + m.x22 == 0)

m.c7 = Constraint(expr= - m.x15 - m.x19 + m.x23 == 0)

m.c8 = Constraint(expr= - m.x16 - m.x20 + m.x24 == 0)

m.c9 = Constraint(expr= - m.x17 - m.x21 + m.x25 == 0)

m.c10 = Constraint(expr=   m.x22 - m.x26 - m.x30 == 0)

m.c11 = Constraint(expr=   m.x23 - m.x27 - m.x31 == 0)

m.c12 = Constraint(expr=   m.x24 - m.x28 - m.x32 == 0)

m.c13 = Constraint(expr=   m.x25 - m.x29 - m.x33 == 0)

m.c14 = Constraint(expr=   m.x30 - m.x34 - m.x38 - m.x42 == 0)

m.c15 = Constraint(expr=   m.x31 - m.x35 - m.x39 - m.x43 == 0)

m.c16 = Constraint(expr=   m.x32 - m.x36 - m.x40 - m.x44 == 0)

m.c17 = Constraint(expr=   m.x33 - m.x37 - m.x41 - m.x45 == 0)

m.c18 = Constraint(expr=   m.x50 - m.x62 - m.x66 == 0)

m.c19 = Constraint(expr=   m.x51 - m.x63 - m.x67 == 0)

m.c20 = Constraint(expr=   m.x52 - m.x64 - m.x68 == 0)

m.c21 = Constraint(expr=   m.x53 - m.x65 - m.x69 == 0)

m.c22 = Constraint(expr=   m.x58 - m.x70 - m.x74 - m.x78 == 0)

m.c23 = Constraint(expr=   m.x59 - m.x71 - m.x75 - m.x79 == 0)

m.c24 = Constraint(expr=   m.x60 - m.x72 - m.x76 - m.x80 == 0)

m.c25 = Constraint(expr=   m.x61 - m.x73 - m.x77 - m.x81 == 0)

m.c26 = Constraint(expr=-log(1 + m.x6) + m.x14 + m.b102 <= 1)

m.c27 = Constraint(expr=-log(1 + m.x7) + m.x15 + m.b103 <= 1)

m.c28 = Constraint(expr=-log(1 + m.x8) + m.x16 + m.b104 <= 1)

m.c29 = Constraint(expr=-log(1 + m.x9) + m.x17 + m.b105 <= 1)

m.c30 = Constraint(expr=   m.x6 - 40*m.b102 <= 0)

m.c31 = Constraint(expr=   m.x7 - 40*m.b103 <= 0)

m.c32 = Constraint(expr=   m.x8 - 40*m.b104 <= 0)

m.c33 = Constraint(expr=   m.x9 - 40*m.b105 <= 0)

m.c34 = Constraint(expr=   m.x14 - 3.71357206670431*m.b102 <= 0)

m.c35 = Constraint(expr=   m.x15 - 3.71357206670431*m.b103 <= 0)

m.c36 = Constraint(expr=   m.x16 - 3.71357206670431*m.b104 <= 0)

m.c37 = Constraint(expr=   m.x17 - 3.71357206670431*m.b105 <= 0)

m.c38 = Constraint(expr=-1.2*log(1 + m.x10) + m.x18 + m.b106 <= 1)

m.c39 = Constraint(expr=-1.2*log(1 + m.x11) + m.x19 + m.b107 <= 1)

m.c40 = Constraint(expr=-1.2*log(1 + m.x12) + m.x20 + m.b108 <= 1)

m.c41 = Constraint(expr=-1.2*log(1 + m.x13) + m.x21 + m.b109 <= 1)

m.c42 = Constraint(expr=   m.x10 - 40*m.b106 <= 0)

m.c43 = Constraint(expr=   m.x11 - 40*m.b107 <= 0)

m.c44 = Constraint(expr=   m.x12 - 40*m.b108 <= 0)

m.c45 = Constraint(expr=   m.x13 - 40*m.b109 <= 0)

m.c46 = Constraint(expr=   m.x18 - 4.45628648004517*m.b106 <= 0)

m.c47 = Constraint(expr=   m.x19 - 4.45628648004517*m.b107 <= 0)

m.c48 = Constraint(expr=   m.x20 - 4.45628648004517*m.b108 <= 0)

m.c49 = Constraint(expr=   m.x21 - 4.45628648004517*m.b109 <= 0)

m.c50 = Constraint(expr= - 0.75*m.x34 + m.x50 + m.b110 <= 1)

m.c51 = Constraint(expr= - 0.75*m.x35 + m.x51 + m.b111 <= 1)

m.c52 = Constraint(expr= - 0.75*m.x36 + m.x52 + m.b112 <= 1)

m.c53 = Constraint(expr= - 0.75*m.x37 + m.x53 + m.b113 <= 1)

m.c54 = Constraint(expr= - 0.75*m.x34 + m.x50 - m.b110 >= -1)

m.c55 = Constraint(expr= - 0.75*m.x35 + m.x51 - m.b111 >= -1)

m.c56 = Constraint(expr= - 0.75*m.x36 + m.x52 - m.b112 >= -1)

m.c57 = Constraint(expr= - 0.75*m.x37 + m.x53 - m.b113 >= -1)

m.c58 = Constraint(expr=   m.x34 - 4.45628648004517*m.b110 <= 0)

m.c59 = Constraint(expr=   m.x35 - 4.45628648004517*m.b111 <= 0)

m.c60 = Constraint(expr=   m.x36 - 4.45628648004517*m.b112 <= 0)

m.c61 = Constraint(expr=   m.x37 - 4.45628648004517*m.b113 <= 0)

m.c62 = Constraint(expr=   m.x50 - 3.34221486003388*m.b110 <= 0)

m.c63 = Constraint(expr=   m.x51 - 3.34221486003388*m.b111 <= 0)

m.c64 = Constraint(expr=   m.x52 - 3.34221486003388*m.b112 <= 0)

m.c65 = Constraint(expr=   m.x53 - 3.34221486003388*m.b113 <= 0)

m.c66 = Constraint(expr=-1.5*log(1 + m.x38) + m.x54 + m.b114 <= 1)

m.c67 = Constraint(expr=-1.5*log(1 + m.x39) + m.x55 + m.b115 <= 1)

m.c68 = Constraint(expr=-1.5*log(1 + m.x40) + m.x56 + m.b116 <= 1)

m.c69 = Constraint(expr=-1.5*log(1 + m.x41) + m.x57 + m.b117 <= 1)

m.c70 = Constraint(expr=   m.x38 - 4.45628648004517*m.b114 <= 0)

m.c71 = Constraint(expr=   m.x39 - 4.45628648004517*m.b115 <= 0)

m.c72 = Constraint(expr=   m.x40 - 4.45628648004517*m.b116 <= 0)

m.c73 = Constraint(expr=   m.x41 - 4.45628648004517*m.b117 <= 0)

m.c74 = Constraint(expr=   m.x54 - 2.54515263975353*m.b114 <= 0)

m.c75 = Constraint(expr=   m.x55 - 2.54515263975353*m.b115 <= 0)

m.c76 = Constraint(expr=   m.x56 - 2.54515263975353*m.b116 <= 0)

m.c77 = Constraint(expr=   m.x57 - 2.54515263975353*m.b117 <= 0)

m.c78 = Constraint(expr= - m.x42 + m.x58 + m.b118 <= 1)

m.c79 = Constraint(expr= - m.x43 + m.x59 + m.b119 <= 1)

m.c80 = Constraint(expr= - m.x44 + m.x60 + m.b120 <= 1)

m.c81 = Constraint(expr= - m.x45 + m.x61 + m.b121 <= 1)

m.c82 = Constraint(expr= - m.x42 + m.x58 - m.b118 >= -1)

m.c83 = Constraint(expr= - m.x43 + m.x59 - m.b119 >= -1)

m.c84 = Constraint(expr= - m.x44 + m.x60 - m.b120 >= -1)

m.c85 = Constraint(expr= - m.x45 + m.x61 - m.b121 >= -1)

m.c86 = Constraint(expr= - 0.5*m.x46 + m.x58 + m.b118 <= 1)

m.c87 = Constraint(expr= - 0.5*m.x47 + m.x59 + m.b119 <= 1)

m.c88 = Constraint(expr= - 0.5*m.x48 + m.x60 + m.b120 <= 1)

m.c89 = Constraint(expr= - 0.5*m.x49 + m.x61 + m.b121 <= 1)

m.c90 = Constraint(expr= - 0.5*m.x46 + m.x58 - m.b118 >= -1)

m.c91 = Constraint(expr= - 0.5*m.x47 + m.x59 - m.b119 >= -1)

m.c92 = Constraint(expr= - 0.5*m.x48 + m.x60 - m.b120 >= -1)

m.c93 = Constraint(expr= - 0.5*m.x49 + m.x61 - m.b121 >= -1)

m.c94 = Constraint(expr=   m.x42 - 4.45628648004517*m.b118 <= 0)

m.c95 = Constraint(expr=   m.x43 - 4.45628648004517*m.b119 <= 0)

m.c96 = Constraint(expr=   m.x44 - 4.45628648004517*m.b120 <= 0)

m.c97 = Constraint(expr=   m.x45 - 4.45628648004517*m.b121 <= 0)

m.c98 = Constraint(expr=   m.x46 - 30*m.b118 <= 0)

m.c99 = Constraint(expr=   m.x47 - 30*m.b119 <= 0)

m.c100 = Constraint(expr=   m.x48 - 30*m.b120 <= 0)

m.c101 = Constraint(expr=   m.x49 - 30*m.b121 <= 0)

m.c102 = Constraint(expr=   m.x58 - 15*m.b118 <= 0)

m.c103 = Constraint(expr=   m.x59 - 15*m.b119 <= 0)

m.c104 = Constraint(expr=   m.x60 - 15*m.b120 <= 0)

m.c105 = Constraint(expr=   m.x61 - 15*m.b121 <= 0)

m.c106 = Constraint(expr=-1.25*log(1 + m.x62) + m.x82 + m.b122 <= 1)

m.c107 = Constraint(expr=-1.25*log(1 + m.x63) + m.x83 + m.b123 <= 1)

m.c108 = Constraint(expr=-1.25*log(1 + m.x64) + m.x84 + m.b124 <= 1)

m.c109 = Constraint(expr=-1.25*log(1 + m.x65) + m.x85 + m.b125 <= 1)

m.c110 = Constraint(expr=   m.x62 - 3.34221486003388*m.b122 <= 0)

m.c111 = Constraint(expr=   m.x63 - 3.34221486003388*m.b123 <= 0)

m.c112 = Constraint(expr=   m.x64 - 3.34221486003388*m.b124 <= 0)

m.c113 = Constraint(expr=   m.x65 - 3.34221486003388*m.b125 <= 0)

m.c114 = Constraint(expr=   m.x82 - 1.83548069293539*m.b122 <= 0)

m.c115 = Constraint(expr=   m.x83 - 1.83548069293539*m.b123 <= 0)

m.c116 = Constraint(expr=   m.x84 - 1.83548069293539*m.b124 <= 0)

m.c117 = Constraint(expr=   m.x85 - 1.83548069293539*m.b125 <= 0)

m.c118 = Constraint(expr=-0.9*log(1 + m.x66) + m.x86 + m.b126 <= 1)

m.c119 = Constraint(expr=-0.9*log(1 + m.x67) + m.x87 + m.b127 <= 1)

m.c120 = Constraint(expr=-0.9*log(1 + m.x68) + m.x88 + m.b128 <= 1)

m.c121 = Constraint(expr=-0.9*log(1 + m.x69) + m.x89 + m.b129 <= 1)

m.c122 = Constraint(expr=   m.x66 - 3.34221486003388*m.b126 <= 0)

m.c123 = Constraint(expr=   m.x67 - 3.34221486003388*m.b127 <= 0)

m.c124 = Constraint(expr=   m.x68 - 3.34221486003388*m.b128 <= 0)

m.c125 = Constraint(expr=   m.x69 - 3.34221486003388*m.b129 <= 0)

m.c126 = Constraint(expr=   m.x86 - 1.32154609891348*m.b126 <= 0)

m.c127 = Constraint(expr=   m.x87 - 1.32154609891348*m.b127 <= 0)

m.c128 = Constraint(expr=   m.x88 - 1.32154609891348*m.b128 <= 0)

m.c129 = Constraint(expr=   m.x89 - 1.32154609891348*m.b129 <= 0)

m.c130 = Constraint(expr=-log(1 + m.x54) + m.x90 + m.b130 <= 1)

m.c131 = Constraint(expr=-log(1 + m.x55) + m.x91 + m.b131 <= 1)

m.c132 = Constraint(expr=-log(1 + m.x56) + m.x92 + m.b132 <= 1)

m.c133 = Constraint(expr=-log(1 + m.x57) + m.x93 + m.b133 <= 1)

m.c134 = Constraint(expr=   m.x54 - 2.54515263975353*m.b130 <= 0)

m.c135 = Constraint(expr=   m.x55 - 2.54515263975353*m.b131 <= 0)

m.c136 = Constraint(expr=   m.x56 - 2.54515263975353*m.b132 <= 0)

m.c137 = Constraint(expr=   m.x57 - 2.54515263975353*m.b133 <= 0)

m.c138 = Constraint(expr=   m.x90 - 1.26558121681553*m.b130 <= 0)

m.c139 = Constraint(expr=   m.x91 - 1.26558121681553*m.b131 <= 0)

m.c140 = Constraint(expr=   m.x92 - 1.26558121681553*m.b132 <= 0)

m.c141 = Constraint(expr=   m.x93 - 1.26558121681553*m.b133 <= 0)

m.c142 = Constraint(expr= - 0.9*m.x70 + m.x94 + m.b134 <= 1)

m.c143 = Constraint(expr= - 0.9*m.x71 + m.x95 + m.b135 <= 1)

m.c144 = Constraint(expr= - 0.9*m.x72 + m.x96 + m.b136 <= 1)

m.c145 = Constraint(expr= - 0.9*m.x73 + m.x97 + m.b137 <= 1)

m.c146 = Constraint(expr= - 0.9*m.x70 + m.x94 - m.b134 >= -1)

m.c147 = Constraint(expr= - 0.9*m.x71 + m.x95 - m.b135 >= -1)

m.c148 = Constraint(expr= - 0.9*m.x72 + m.x96 - m.b136 >= -1)

m.c149 = Constraint(expr= - 0.9*m.x73 + m.x97 - m.b137 >= -1)

m.c150 = Constraint(expr=   m.x70 - 15*m.b134 <= 0)

m.c151 = Constraint(expr=   m.x71 - 15*m.b135 <= 0)

m.c152 = Constraint(expr=   m.x72 - 15*m.b136 <= 0)

m.c153 = Constraint(expr=   m.x73 - 15*m.b137 <= 0)

m.c154 = Constraint(expr=   m.x94 - 13.5*m.b134 <= 0)

m.c155 = Constraint(expr=   m.x95 - 13.5*m.b135 <= 0)

m.c156 = Constraint(expr=   m.x96 - 13.5*m.b136 <= 0)

m.c157 = Constraint(expr=   m.x97 - 13.5*m.b137 <= 0)

m.c158 = Constraint(expr= - 0.6*m.x74 + m.x98 + m.b138 <= 1)

m.c159 = Constraint(expr= - 0.6*m.x75 + m.x99 + m.b139 <= 1)

m.c160 = Constraint(expr= - 0.6*m.x76 + m.x100 + m.b140 <= 1)

m.c161 = Constraint(expr= - 0.6*m.x77 + m.x101 + m.b141 <= 1)

m.c162 = Constraint(expr= - 0.6*m.x74 + m.x98 - m.b138 >= -1)

m.c163 = Constraint(expr= - 0.6*m.x75 + m.x99 - m.b139 >= -1)

m.c164 = Constraint(expr= - 0.6*m.x76 + m.x100 - m.b140 >= -1)

m.c165 = Constraint(expr= - 0.6*m.x77 + m.x101 - m.b141 >= -1)

m.c166 = Constraint(expr=   m.x74 - 15*m.b138 <= 0)

m.c167 = Constraint(expr=   m.x75 - 15*m.b139 <= 0)

m.c168 = Constraint(expr=   m.x76 - 15*m.b140 <= 0)

m.c169 = Constraint(expr=   m.x77 - 15*m.b141 <= 0)

m.c170 = Constraint(expr=   m.x98 - 9*m.b138 <= 0)

m.c171 = Constraint(expr=   m.x99 - 9*m.b139 <= 0)

m.c172 = Constraint(expr=   m.x100 - 9*m.b140 <= 0)

m.c173 = Constraint(expr=   m.x101 - 9*m.b141 <= 0)

m.c174 = Constraint(expr=   5*m.b142 + m.x182 <= 0)

m.c175 = Constraint(expr=   4*m.b143 + m.x183 <= 0)

m.c176 = Constraint(expr=   6*m.b144 + m.x184 <= 0)

m.c177 = Constraint(expr=   3*m.b145 + m.x185 <= 0)

m.c178 = Constraint(expr=   8*m.b146 + m.x186 <= 0)

m.c179 = Constraint(expr=   7*m.b147 + m.x187 <= 0)

m.c180 = Constraint(expr=   6*m.b148 + m.x188 <= 0)

m.c181 = Constraint(expr=   5*m.b149 + m.x189 <= 0)

m.c182 = Constraint(expr=   6*m.b150 + m.x190 <= 0)

m.c183 = Constraint(expr=   9*m.b151 + m.x191 <= 0)

m.c184 = Constraint(expr=   4*m.b152 + m.x192 <= 0)

m.c185 = Constraint(expr=   3*m.b153 + m.x193 <= 0)

m.c186 = Constraint(expr=   10*m.b154 + m.x194 <= 0)

m.c187 = Constraint(expr=   9*m.b155 + m.x195 <= 0)

m.c188 = Constraint(expr=   5*m.b156 + m.x196 <= 0)

m.c189 = Constraint(expr=   6*m.b157 + m.x197 <= 0)

m.c190 = Constraint(expr=   6*m.b158 + m.x198 <= 0)

m.c191 = Constraint(expr=   10*m.b159 + m.x199 <= 0)

m.c192 = Constraint(expr=   6*m.b160 + m.x200 <= 0)

m.c193 = Constraint(expr=   9*m.b161 + m.x201 <= 0)

m.c194 = Constraint(expr=   7*m.b162 + m.x202 <= 0)

m.c195 = Constraint(expr=   7*m.b163 + m.x203 <= 0)

m.c196 = Constraint(expr=   4*m.b164 + m.x204 <= 0)

m.c197 = Constraint(expr=   2*m.b165 + m.x205 <= 0)

m.c198 = Constraint(expr=   4*m.b166 + m.x206 <= 0)

m.c199 = Constraint(expr=   3*m.b167 + m.x207 <= 0)

m.c200 = Constraint(expr=   2*m.b168 + m.x208 <= 0)

m.c201 = Constraint(expr=   8*m.b169 + m.x209 <= 0)

m.c202 = Constraint(expr=   5*m.b170 + m.x210 <= 0)

m.c203 = Constraint(expr=   6*m.b171 + m.x211 <= 0)

m.c204 = Constraint(expr=   7*m.b172 + m.x212 <= 0)

m.c205 = Constraint(expr=   4*m.b173 + m.x213 <= 0)

m.c206 = Constraint(expr=   2*m.b174 + m.x214 <= 0)

m.c207 = Constraint(expr=   5*m.b175 + m.x215 <= 0)

m.c208 = Constraint(expr=   2*m.b176 + m.x216 <= 0)

m.c209 = Constraint(expr=   6*m.b177 + m.x217 <= 0)

m.c210 = Constraint(expr=   4*m.b178 + m.x218 <= 0)

m.c211 = Constraint(expr=   7*m.b179 + m.x219 <= 0)

m.c212 = Constraint(expr=   4*m.b180 + m.x220 <= 0)

m.c213 = Constraint(expr=   7*m.b181 + m.x221 <= 0)

m.c214 = Constraint(expr=   5*m.b142 + m.x182 >= 0)

m.c215 = Constraint(expr=   4*m.b143 + m.x183 >= 0)

m.c216 = Constraint(expr=   6*m.b144 + m.x184 >= 0)

m.c217 = Constraint(expr=   3*m.b145 + m.x185 >= 0)

m.c218 = Constraint(expr=   8*m.b146 + m.x186 >= 0)

m.c219 = Constraint(expr=   7*m.b147 + m.x187 >= 0)

m.c220 = Constraint(expr=   6*m.b148 + m.x188 >= 0)

m.c221 = Constraint(expr=   5*m.b149 + m.x189 >= 0)

m.c222 = Constraint(expr=   6*m.b150 + m.x190 >= 0)

m.c223 = Constraint(expr=   9*m.b151 + m.x191 >= 0)

m.c224 = Constraint(expr=   4*m.b152 + m.x192 >= 0)

m.c225 = Constraint(expr=   3*m.b153 + m.x193 >= 0)

m.c226 = Constraint(expr=   10*m.b154 + m.x194 >= 0)

m.c227 = Constraint(expr=   9*m.b155 + m.x195 >= 0)

m.c228 = Constraint(expr=   5*m.b156 + m.x196 >= 0)

m.c229 = Constraint(expr=   6*m.b157 + m.x197 >= 0)

m.c230 = Constraint(expr=   6*m.b158 + m.x198 >= 0)

m.c231 = Constraint(expr=   10*m.b159 + m.x199 >= 0)

m.c232 = Constraint(expr=   6*m.b160 + m.x200 >= 0)

m.c233 = Constraint(expr=   9*m.b161 + m.x201 >= 0)

m.c234 = Constraint(expr=   7*m.b162 + m.x202 >= 0)

m.c235 = Constraint(expr=   7*m.b163 + m.x203 >= 0)

m.c236 = Constraint(expr=   4*m.b164 + m.x204 >= 0)

m.c237 = Constraint(expr=   2*m.b165 + m.x205 >= 0)

m.c238 = Constraint(expr=   4*m.b166 + m.x206 >= 0)

m.c239 = Constraint(expr=   3*m.b167 + m.x207 >= 0)

m.c240 = Constraint(expr=   2*m.b168 + m.x208 >= 0)

m.c241 = Constraint(expr=   8*m.b169 + m.x209 >= 0)

m.c242 = Constraint(expr=   5*m.b170 + m.x210 >= 0)

m.c243 = Constraint(expr=   6*m.b171 + m.x211 >= 0)

m.c244 = Constraint(expr=   7*m.b172 + m.x212 >= 0)

m.c245 = Constraint(expr=   4*m.b173 + m.x213 >= 0)

m.c246 = Constraint(expr=   2*m.b174 + m.x214 >= 0)

m.c247 = Constraint(expr=   5*m.b175 + m.x215 >= 0)

m.c248 = Constraint(expr=   2*m.b176 + m.x216 >= 0)

m.c249 = Constraint(expr=   6*m.b177 + m.x217 >= 0)

m.c250 = Constraint(expr=   4*m.b178 + m.x218 >= 0)

m.c251 = Constraint(expr=   7*m.b179 + m.x219 >= 0)

m.c252 = Constraint(expr=   4*m.b180 + m.x220 >= 0)

m.c253 = Constraint(expr=   7*m.b181 + m.x221 >= 0)

m.c254 = Constraint(expr=   m.b102 - m.b103 <= 0)

m.c255 = Constraint(expr=   m.b102 - m.b104 <= 0)

m.c256 = Constraint(expr=   m.b102 - m.b105 <= 0)

m.c257 = Constraint(expr=   m.b103 - m.b104 <= 0)

m.c258 = Constraint(expr=   m.b103 - m.b105 <= 0)

m.c259 = Constraint(expr=   m.b104 - m.b105 <= 0)

m.c260 = Constraint(expr=   m.b106 - m.b107 <= 0)

m.c261 = Constraint(expr=   m.b106 - m.b108 <= 0)

m.c262 = Constraint(expr=   m.b106 - m.b109 <= 0)

m.c263 = Constraint(expr=   m.b107 - m.b108 <= 0)

m.c264 = Constraint(expr=   m.b107 - m.b109 <= 0)

m.c265 = Constraint(expr=   m.b108 - m.b109 <= 0)

m.c266 = Constraint(expr=   m.b110 - m.b111 <= 0)

m.c267 = Constraint(expr=   m.b110 - m.b112 <= 0)

m.c268 = Constraint(expr=   m.b110 - m.b113 <= 0)

m.c269 = Constraint(expr=   m.b111 - m.b112 <= 0)

m.c270 = Constraint(expr=   m.b111 - m.b113 <= 0)

m.c271 = Constraint(expr=   m.b112 - m.b113 <= 0)

m.c272 = Constraint(expr=   m.b114 - m.b115 <= 0)

m.c273 = Constraint(expr=   m.b114 - m.b116 <= 0)

m.c274 = Constraint(expr=   m.b114 - m.b117 <= 0)

m.c275 = Constraint(expr=   m.b115 - m.b116 <= 0)

m.c276 = Constraint(expr=   m.b115 - m.b117 <= 0)

m.c277 = Constraint(expr=   m.b116 - m.b117 <= 0)

m.c278 = Constraint(expr=   m.b118 - m.b119 <= 0)

m.c279 = Constraint(expr=   m.b118 - m.b120 <= 0)

m.c280 = Constraint(expr=   m.b118 - m.b121 <= 0)

m.c281 = Constraint(expr=   m.b119 - m.b120 <= 0)

m.c282 = Constraint(expr=   m.b119 - m.b121 <= 0)

m.c283 = Constraint(expr=   m.b120 - m.b121 <= 0)

m.c284 = Constraint(expr=   m.b122 - m.b123 <= 0)

m.c285 = Constraint(expr=   m.b122 - m.b124 <= 0)

m.c286 = Constraint(expr=   m.b122 - m.b125 <= 0)

m.c287 = Constraint(expr=   m.b123 - m.b124 <= 0)

m.c288 = Constraint(expr=   m.b123 - m.b125 <= 0)

m.c289 = Constraint(expr=   m.b124 - m.b125 <= 0)

m.c290 = Constraint(expr=   m.b126 - m.b127 <= 0)

m.c291 = Constraint(expr=   m.b126 - m.b128 <= 0)

m.c292 = Constraint(expr=   m.b126 - m.b129 <= 0)

m.c293 = Constraint(expr=   m.b127 - m.b128 <= 0)

m.c294 = Constraint(expr=   m.b127 - m.b129 <= 0)

m.c295 = Constraint(expr=   m.b128 - m.b129 <= 0)

m.c296 = Constraint(expr=   m.b130 - m.b131 <= 0)

m.c297 = Constraint(expr=   m.b130 - m.b132 <= 0)

m.c298 = Constraint(expr=   m.b130 - m.b133 <= 0)

m.c299 = Constraint(expr=   m.b131 - m.b132 <= 0)

m.c300 = Constraint(expr=   m.b131 - m.b133 <= 0)

m.c301 = Constraint(expr=   m.b132 - m.b133 <= 0)

m.c302 = Constraint(expr=   m.b134 - m.b135 <= 0)

m.c303 = Constraint(expr=   m.b134 - m.b136 <= 0)

m.c304 = Constraint(expr=   m.b134 - m.b137 <= 0)

m.c305 = Constraint(expr=   m.b135 - m.b136 <= 0)

m.c306 = Constraint(expr=   m.b135 - m.b137 <= 0)

m.c307 = Constraint(expr=   m.b136 - m.b137 <= 0)

m.c308 = Constraint(expr=   m.b138 - m.b139 <= 0)

m.c309 = Constraint(expr=   m.b138 - m.b140 <= 0)

m.c310 = Constraint(expr=   m.b138 - m.b141 <= 0)

m.c311 = Constraint(expr=   m.b139 - m.b140 <= 0)

m.c312 = Constraint(expr=   m.b139 - m.b141 <= 0)

m.c313 = Constraint(expr=   m.b140 - m.b141 <= 0)

m.c314 = Constraint(expr=   m.b142 + m.b143 <= 1)

m.c315 = Constraint(expr=   m.b142 + m.b144 <= 1)

m.c316 = Constraint(expr=   m.b142 + m.b145 <= 1)

m.c317 = Constraint(expr=   m.b142 + m.b143 <= 1)

m.c318 = Constraint(expr=   m.b143 + m.b144 <= 1)

m.c319 = Constraint(expr=   m.b143 + m.b145 <= 1)

m.c320 = Constraint(expr=   m.b142 + m.b144 <= 1)

m.c321 = Constraint(expr=   m.b143 + m.b144 <= 1)

m.c322 = Constraint(expr=   m.b144 + m.b145 <= 1)

m.c323 = Constraint(expr=   m.b142 + m.b145 <= 1)

m.c324 = Constraint(expr=   m.b143 + m.b145 <= 1)

m.c325 = Constraint(expr=   m.b144 + m.b145 <= 1)

m.c326 = Constraint(expr=   m.b146 + m.b147 <= 1)

m.c327 = Constraint(expr=   m.b146 + m.b148 <= 1)

m.c328 = Constraint(expr=   m.b146 + m.b149 <= 1)

m.c329 = Constraint(expr=   m.b146 + m.b147 <= 1)

m.c330 = Constraint(expr=   m.b147 + m.b148 <= 1)

m.c331 = Constraint(expr=   m.b147 + m.b149 <= 1)

m.c332 = Constraint(expr=   m.b146 + m.b148 <= 1)

m.c333 = Constraint(expr=   m.b147 + m.b148 <= 1)

m.c334 = Constraint(expr=   m.b148 + m.b149 <= 1)

m.c335 = Constraint(expr=   m.b146 + m.b149 <= 1)

m.c336 = Constraint(expr=   m.b147 + m.b149 <= 1)

m.c337 = Constraint(expr=   m.b148 + m.b149 <= 1)

m.c338 = Constraint(expr=   m.b150 + m.b151 <= 1)

m.c339 = Constraint(expr=   m.b150 + m.b152 <= 1)

m.c340 = Constraint(expr=   m.b150 + m.b153 <= 1)

m.c341 = Constraint(expr=   m.b150 + m.b151 <= 1)

m.c342 = Constraint(expr=   m.b151 + m.b152 <= 1)

m.c343 = Constraint(expr=   m.b151 + m.b153 <= 1)

m.c344 = Constraint(expr=   m.b150 + m.b152 <= 1)

m.c345 = Constraint(expr=   m.b151 + m.b152 <= 1)

m.c346 = Constraint(expr=   m.b152 + m.b153 <= 1)

m.c347 = Constraint(expr=   m.b150 + m.b153 <= 1)

m.c348 = Constraint(expr=   m.b151 + m.b153 <= 1)

m.c349 = Constraint(expr=   m.b152 + m.b153 <= 1)

m.c350 = Constraint(expr=   m.b154 + m.b155 <= 1)

m.c351 = Constraint(expr=   m.b154 + m.b156 <= 1)

m.c352 = Constraint(expr=   m.b154 + m.b157 <= 1)

m.c353 = Constraint(expr=   m.b154 + m.b155 <= 1)

m.c354 = Constraint(expr=   m.b155 + m.b156 <= 1)

m.c355 = Constraint(expr=   m.b155 + m.b157 <= 1)

m.c356 = Constraint(expr=   m.b154 + m.b156 <= 1)

m.c357 = Constraint(expr=   m.b155 + m.b156 <= 1)

m.c358 = Constraint(expr=   m.b156 + m.b157 <= 1)

m.c359 = Constraint(expr=   m.b154 + m.b157 <= 1)

m.c360 = Constraint(expr=   m.b155 + m.b157 <= 1)

m.c361 = Constraint(expr=   m.b156 + m.b157 <= 1)

m.c362 = Constraint(expr=   m.b158 + m.b159 <= 1)

m.c363 = Constraint(expr=   m.b158 + m.b160 <= 1)

m.c364 = Constraint(expr=   m.b158 + m.b161 <= 1)

m.c365 = Constraint(expr=   m.b158 + m.b159 <= 1)

m.c366 = Constraint(expr=   m.b159 + m.b160 <= 1)

m.c367 = Constraint(expr=   m.b159 + m.b161 <= 1)

m.c368 = Constraint(expr=   m.b158 + m.b160 <= 1)

m.c369 = Constraint(expr=   m.b159 + m.b160 <= 1)

m.c370 = Constraint(expr=   m.b160 + m.b161 <= 1)

m.c371 = Constraint(expr=   m.b158 + m.b161 <= 1)

m.c372 = Constraint(expr=   m.b159 + m.b161 <= 1)

m.c373 = Constraint(expr=   m.b160 + m.b161 <= 1)

m.c374 = Constraint(expr=   m.b162 + m.b163 <= 1)

m.c375 = Constraint(expr=   m.b162 + m.b164 <= 1)

m.c376 = Constraint(expr=   m.b162 + m.b165 <= 1)

m.c377 = Constraint(expr=   m.b162 + m.b163 <= 1)

m.c378 = Constraint(expr=   m.b163 + m.b164 <= 1)

m.c379 = Constraint(expr=   m.b163 + m.b165 <= 1)

m.c380 = Constraint(expr=   m.b162 + m.b164 <= 1)

m.c381 = Constraint(expr=   m.b163 + m.b164 <= 1)

m.c382 = Constraint(expr=   m.b164 + m.b165 <= 1)

m.c383 = Constraint(expr=   m.b162 + m.b165 <= 1)

m.c384 = Constraint(expr=   m.b163 + m.b165 <= 1)

m.c385 = Constraint(expr=   m.b164 + m.b165 <= 1)

m.c386 = Constraint(expr=   m.b166 + m.b167 <= 1)

m.c387 = Constraint(expr=   m.b166 + m.b168 <= 1)

m.c388 = Constraint(expr=   m.b166 + m.b169 <= 1)

m.c389 = Constraint(expr=   m.b166 + m.b167 <= 1)

m.c390 = Constraint(expr=   m.b167 + m.b168 <= 1)

m.c391 = Constraint(expr=   m.b167 + m.b169 <= 1)

m.c392 = Constraint(expr=   m.b166 + m.b168 <= 1)

m.c393 = Constraint(expr=   m.b167 + m.b168 <= 1)

m.c394 = Constraint(expr=   m.b168 + m.b169 <= 1)

m.c395 = Constraint(expr=   m.b166 + m.b169 <= 1)

m.c396 = Constraint(expr=   m.b167 + m.b169 <= 1)

m.c397 = Constraint(expr=   m.b168 + m.b169 <= 1)

m.c398 = Constraint(expr=   m.b170 + m.b171 <= 1)

m.c399 = Constraint(expr=   m.b170 + m.b172 <= 1)

m.c400 = Constraint(expr=   m.b170 + m.b173 <= 1)

m.c401 = Constraint(expr=   m.b170 + m.b171 <= 1)

m.c402 = Constraint(expr=   m.b171 + m.b172 <= 1)

m.c403 = Constraint(expr=   m.b171 + m.b173 <= 1)

m.c404 = Constraint(expr=   m.b170 + m.b172 <= 1)

m.c405 = Constraint(expr=   m.b171 + m.b172 <= 1)

m.c406 = Constraint(expr=   m.b172 + m.b173 <= 1)

m.c407 = Constraint(expr=   m.b170 + m.b173 <= 1)

m.c408 = Constraint(expr=   m.b171 + m.b173 <= 1)

m.c409 = Constraint(expr=   m.b172 + m.b173 <= 1)

m.c410 = Constraint(expr=   m.b174 + m.b175 <= 1)

m.c411 = Constraint(expr=   m.b174 + m.b176 <= 1)

m.c412 = Constraint(expr=   m.b174 + m.b177 <= 1)

m.c413 = Constraint(expr=   m.b174 + m.b175 <= 1)

m.c414 = Constraint(expr=   m.b175 + m.b176 <= 1)

m.c415 = Constraint(expr=   m.b175 + m.b177 <= 1)

m.c416 = Constraint(expr=   m.b174 + m.b176 <= 1)

m.c417 = Constraint(expr=   m.b175 + m.b176 <= 1)

m.c418 = Constraint(expr=   m.b176 + m.b177 <= 1)

m.c419 = Constraint(expr=   m.b174 + m.b177 <= 1)

m.c420 = Constraint(expr=   m.b175 + m.b177 <= 1)

m.c421 = Constraint(expr=   m.b176 + m.b177 <= 1)

m.c422 = Constraint(expr=   m.b178 + m.b179 <= 1)

m.c423 = Constraint(expr=   m.b178 + m.b180 <= 1)

m.c424 = Constraint(expr=   m.b178 + m.b181 <= 1)

m.c425 = Constraint(expr=   m.b178 + m.b179 <= 1)

m.c426 = Constraint(expr=   m.b179 + m.b180 <= 1)

m.c427 = Constraint(expr=   m.b179 + m.b181 <= 1)

m.c428 = Constraint(expr=   m.b178 + m.b180 <= 1)

m.c429 = Constraint(expr=   m.b179 + m.b180 <= 1)

m.c430 = Constraint(expr=   m.b180 + m.b181 <= 1)

m.c431 = Constraint(expr=   m.b178 + m.b181 <= 1)

m.c432 = Constraint(expr=   m.b179 + m.b181 <= 1)

m.c433 = Constraint(expr=   m.b180 + m.b181 <= 1)

m.c434 = Constraint(expr=   m.b102 - m.b142 <= 0)

m.c435 = Constraint(expr= - m.b102 + m.b103 - m.b143 <= 0)

m.c436 = Constraint(expr= - m.b102 - m.b103 + m.b104 - m.b144 <= 0)

m.c437 = Constraint(expr= - m.b102 - m.b103 - m.b104 + m.b105 - m.b145 <= 0)

m.c438 = Constraint(expr=   m.b106 - m.b146 <= 0)

m.c439 = Constraint(expr= - m.b106 + m.b107 - m.b147 <= 0)

m.c440 = Constraint(expr= - m.b106 - m.b107 + m.b108 - m.b148 <= 0)

m.c441 = Constraint(expr= - m.b106 - m.b107 - m.b108 + m.b109 - m.b149 <= 0)

m.c442 = Constraint(expr=   m.b110 - m.b150 <= 0)

m.c443 = Constraint(expr= - m.b110 + m.b111 - m.b151 <= 0)

m.c444 = Constraint(expr= - m.b110 - m.b111 + m.b112 - m.b152 <= 0)

m.c445 = Constraint(expr= - m.b110 - m.b111 - m.b112 + m.b113 - m.b153 <= 0)

m.c446 = Constraint(expr=   m.b114 - m.b154 <= 0)

m.c447 = Constraint(expr= - m.b114 + m.b115 - m.b155 <= 0)

m.c448 = Constraint(expr= - m.b114 - m.b115 + m.b116 - m.b156 <= 0)

m.c449 = Constraint(expr= - m.b114 - m.b115 - m.b116 + m.b117 - m.b157 <= 0)

m.c450 = Constraint(expr=   m.b118 - m.b158 <= 0)

m.c451 = Constraint(expr= - m.b118 + m.b119 - m.b159 <= 0)

m.c452 = Constraint(expr= - m.b118 - m.b119 + m.b120 - m.b160 <= 0)

m.c453 = Constraint(expr= - m.b118 - m.b119 - m.b120 + m.b121 - m.b161 <= 0)

m.c454 = Constraint(expr=   m.b122 - m.b162 <= 0)

m.c455 = Constraint(expr= - m.b122 + m.b123 - m.b163 <= 0)

m.c456 = Constraint(expr= - m.b122 - m.b123 + m.b124 - m.b164 <= 0)

m.c457 = Constraint(expr= - m.b122 - m.b123 - m.b124 + m.b125 - m.b165 <= 0)

m.c458 = Constraint(expr=   m.b126 - m.b166 <= 0)

m.c459 = Constraint(expr= - m.b126 + m.b127 - m.b167 <= 0)

m.c460 = Constraint(expr= - m.b126 - m.b127 + m.b128 - m.b168 <= 0)

m.c461 = Constraint(expr= - m.b126 - m.b127 - m.b128 + m.b129 - m.b169 <= 0)

m.c462 = Constraint(expr=   m.b130 - m.b170 <= 0)

m.c463 = Constraint(expr= - m.b130 + m.b131 - m.b171 <= 0)

m.c464 = Constraint(expr= - m.b130 - m.b131 + m.b132 - m.b172 <= 0)

m.c465 = Constraint(expr= - m.b130 - m.b131 - m.b132 + m.b133 - m.b173 <= 0)

m.c466 = Constraint(expr=   m.b134 - m.b174 <= 0)

m.c467 = Constraint(expr= - m.b134 + m.b135 - m.b175 <= 0)

m.c468 = Constraint(expr= - m.b134 - m.b135 + m.b136 - m.b176 <= 0)

m.c469 = Constraint(expr= - m.b134 - m.b135 - m.b136 + m.b137 - m.b177 <= 0)

m.c470 = Constraint(expr=   m.b138 - m.b178 <= 0)

m.c471 = Constraint(expr= - m.b138 + m.b139 - m.b179 <= 0)

m.c472 = Constraint(expr= - m.b138 - m.b139 + m.b140 - m.b180 <= 0)

m.c473 = Constraint(expr= - m.b138 - m.b139 - m.b140 + m.b141 - m.b181 <= 0)

m.c474 = Constraint(expr=   m.b102 + m.b106 == 1)

m.c475 = Constraint(expr=   m.b103 + m.b107 == 1)

m.c476 = Constraint(expr=   m.b104 + m.b108 == 1)

m.c477 = Constraint(expr=   m.b105 + m.b109 == 1)

m.c478 = Constraint(expr= - m.b110 + m.b122 + m.b126 >= 0)

m.c479 = Constraint(expr= - m.b111 + m.b123 + m.b127 >= 0)

m.c480 = Constraint(expr= - m.b112 + m.b124 + m.b128 >= 0)

m.c481 = Constraint(expr= - m.b113 + m.b125 + m.b129 >= 0)

m.c482 = Constraint(expr= - m.b114 + m.b130 >= 0)

m.c483 = Constraint(expr= - m.b115 + m.b131 >= 0)

m.c484 = Constraint(expr= - m.b116 + m.b132 >= 0)

m.c485 = Constraint(expr= - m.b117 + m.b133 >= 0)

m.c486 = Constraint(expr=   m.b102 + m.b106 - m.b110 >= 0)

m.c487 = Constraint(expr=   m.b103 + m.b107 - m.b111 >= 0)

m.c488 = Constraint(expr=   m.b104 + m.b108 - m.b112 >= 0)

m.c489 = Constraint(expr=   m.b105 + m.b109 - m.b113 >= 0)

m.c490 = Constraint(expr=   m.b102 + m.b106 - m.b114 >= 0)

m.c491 = Constraint(expr=   m.b103 + m.b107 - m.b115 >= 0)

m.c492 = Constraint(expr=   m.b104 + m.b108 - m.b116 >= 0)

m.c493 = Constraint(expr=   m.b105 + m.b109 - m.b117 >= 0)

m.c494 = Constraint(expr=   m.b102 + m.b106 - m.b118 >= 0)

m.c495 = Constraint(expr=   m.b103 + m.b107 - m.b119 >= 0)

m.c496 = Constraint(expr=   m.b104 + m.b108 - m.b120 >= 0)

m.c497 = Constraint(expr=   m.b105 + m.b109 - m.b121 >= 0)

m.c498 = Constraint(expr=   m.b110 - m.b122 >= 0)

m.c499 = Constraint(expr=   m.b111 - m.b123 >= 0)

m.c500 = Constraint(expr=   m.b112 - m.b124 >= 0)

m.c501 = Constraint(expr=   m.b113 - m.b125 >= 0)

m.c502 = Constraint(expr=   m.b110 - m.b126 >= 0)

m.c503 = Constraint(expr=   m.b111 - m.b127 >= 0)

m.c504 = Constraint(expr=   m.b112 - m.b128 >= 0)

m.c505 = Constraint(expr=   m.b113 - m.b129 >= 0)

m.c506 = Constraint(expr=   m.b114 - m.b130 >= 0)

m.c507 = Constraint(expr=   m.b115 - m.b131 >= 0)

m.c508 = Constraint(expr=   m.b116 - m.b132 >= 0)

m.c509 = Constraint(expr=   m.b117 - m.b133 >= 0)

m.c510 = Constraint(expr=   m.b118 - m.b134 >= 0)

m.c511 = Constraint(expr=   m.b119 - m.b135 >= 0)

m.c512 = Constraint(expr=   m.b120 - m.b136 >= 0)

m.c513 = Constraint(expr=   m.b121 - m.b137 >= 0)

m.c514 = Constraint(expr=   m.b118 - m.b138 >= 0)

m.c515 = Constraint(expr=   m.b119 - m.b139 >= 0)

m.c516 = Constraint(expr=   m.b120 - m.b140 >= 0)

m.c517 = Constraint(expr=   m.b121 - m.b141 >= 0)

#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        538       34      126      378        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        256      166       90        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1333     1300       33        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x35 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x86 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x222 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x237 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x238 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x241 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x243 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x244 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x245 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x247 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x249 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x250 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x251 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x252 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x253 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x254 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x255 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x256 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 + 5*m.x20 + 10*m.x21 + 5*m.x22 - 2*m.x35 - m.x36 - 2*m.x37 + 500*m.x74
                        + 600*m.x75 + 350*m.x76 + 350*m.x77 + 400*m.x78 + 450*m.x79 - 10*m.x86 - 5*m.x87 - 5*m.x88
                        - 5*m.x89 - 5*m.x90 - 5*m.x91 + 80*m.x110 + 130*m.x111 + 215*m.x112 + 110*m.x113 + 120*m.x114
                        + 125*m.x115 + 110*m.x116 + 130*m.x117 + 140*m.x118 + 80*m.x119 + 90*m.x120 + 120*m.x121
                        - 5*m.b167 - 4*m.b168 - 6*m.b169 - 8*m.b170 - 7*m.b171 - 6*m.b172 - 6*m.b173 - 9*m.b174
                        - 4*m.b175 - 10*m.b176 - 9*m.b177 - 5*m.b178 - 6*m.b179 - 10*m.b180 - 6*m.b181 - 7*m.b182
                        - 7*m.b183 - 4*m.b184 - 4*m.b185 - 3*m.b186 - 2*m.b187 - 5*m.b188 - 6*m.b189 - 7*m.b190
                        - 2*m.b191 - 5*m.b192 - 2*m.b193 - 4*m.b194 - 7*m.b195 - 4*m.b196 - 3*m.b197 - 9*m.b198
                        - 3*m.b199 - 7*m.b200 - 2*m.b201 - 9*m.b202 - 3*m.b203 - m.b204 - 9*m.b205 - 2*m.b206 - 6*m.b207
                        - 3*m.b208 - 4*m.b209 - 8*m.b210 - m.b211, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x5 - m.x8 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x6 - m.x9 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x7 - m.x10 == 0)

m.c5 = Constraint(expr= - m.x11 - m.x14 + m.x17 == 0)

m.c6 = Constraint(expr= - m.x12 - m.x15 + m.x18 == 0)

m.c7 = Constraint(expr= - m.x13 - m.x16 + m.x19 == 0)

m.c8 = Constraint(expr=   m.x17 - m.x20 - m.x23 == 0)

m.c9 = Constraint(expr=   m.x18 - m.x21 - m.x24 == 0)

m.c10 = Constraint(expr=   m.x19 - m.x22 - m.x25 == 0)

m.c11 = Constraint(expr=   m.x23 - m.x26 - m.x29 - m.x32 == 0)

m.c12 = Constraint(expr=   m.x24 - m.x27 - m.x30 - m.x33 == 0)

m.c13 = Constraint(expr=   m.x25 - m.x28 - m.x31 - m.x34 == 0)

m.c14 = Constraint(expr=   m.x38 - m.x47 - m.x50 == 0)

m.c15 = Constraint(expr=   m.x39 - m.x48 - m.x51 == 0)

m.c16 = Constraint(expr=   m.x40 - m.x49 - m.x52 == 0)

m.c17 = Constraint(expr=   m.x44 - m.x53 - m.x56 - m.x59 == 0)

m.c18 = Constraint(expr=   m.x45 - m.x54 - m.x57 - m.x60 == 0)

m.c19 = Constraint(expr=   m.x46 - m.x55 - m.x58 - m.x61 == 0)

m.c20 = Constraint(expr=   m.x68 - m.x80 - m.x83 == 0)

m.c21 = Constraint(expr=   m.x69 - m.x81 - m.x84 == 0)

m.c22 = Constraint(expr=   m.x70 - m.x82 - m.x85 == 0)

m.c23 = Constraint(expr= - m.x71 - m.x89 + m.x92 == 0)

m.c24 = Constraint(expr= - m.x72 - m.x90 + m.x93 == 0)

m.c25 = Constraint(expr= - m.x73 - m.x91 + m.x94 == 0)

m.c26 = Constraint(expr=   m.x74 - m.x95 - m.x98 == 0)

m.c27 = Constraint(expr=   m.x75 - m.x96 - m.x99 == 0)

m.c28 = Constraint(expr=   m.x76 - m.x97 - m.x100 == 0)

m.c29 = Constraint(expr=   m.x77 - m.x101 - m.x104 - m.x107 == 0)

m.c30 = Constraint(expr=   m.x78 - m.x102 - m.x105 - m.x108 == 0)

m.c31 = Constraint(expr=   m.x79 - m.x103 - m.x106 - m.x109 == 0)

m.c32 = Constraint(expr=-log(1 + m.x5) + m.x11 + m.b122 <= 1)

m.c33 = Constraint(expr=-log(1 + m.x6) + m.x12 + m.b123 <= 1)

m.c34 = Constraint(expr=-log(1 + m.x7) + m.x13 + m.b124 <= 1)

m.c35 = Constraint(expr=   m.x5 - 40*m.b122 <= 0)

m.c36 = Constraint(expr=   m.x6 - 40*m.b123 <= 0)

m.c37 = Constraint(expr=   m.x7 - 40*m.b124 <= 0)

m.c38 = Constraint(expr=   m.x11 - 3.71357206670431*m.b122 <= 0)

m.c39 = Constraint(expr=   m.x12 - 3.71357206670431*m.b123 <= 0)

m.c40 = Constraint(expr=   m.x13 - 3.71357206670431*m.b124 <= 0)

m.c41 = Constraint(expr=-1.2*log(1 + m.x8) + m.x14 + m.b125 <= 1)

m.c42 = Constraint(expr=-1.2*log(1 + m.x9) + m.x15 + m.b126 <= 1)

m.c43 = Constraint(expr=-1.2*log(1 + m.x10) + m.x16 + m.b127 <= 1)

m.c44 = Constraint(expr=   m.x8 - 40*m.b125 <= 0)

m.c45 = Constraint(expr=   m.x9 - 40*m.b126 <= 0)

m.c46 = Constraint(expr=   m.x10 - 40*m.b127 <= 0)

m.c47 = Constraint(expr=   m.x14 - 4.45628648004517*m.b125 <= 0)

m.c48 = Constraint(expr=   m.x15 - 4.45628648004517*m.b126 <= 0)

m.c49 = Constraint(expr=   m.x16 - 4.45628648004517*m.b127 <= 0)

m.c50 = Constraint(expr= - 0.75*m.x26 + m.x38 + m.b128 <= 1)

m.c51 = Constraint(expr= - 0.75*m.x27 + m.x39 + m.b129 <= 1)

m.c52 = Constraint(expr= - 0.75*m.x28 + m.x40 + m.b130 <= 1)

m.c53 = Constraint(expr= - 0.75*m.x26 + m.x38 - m.b128 >= -1)

m.c54 = Constraint(expr= - 0.75*m.x27 + m.x39 - m.b129 >= -1)

m.c55 = Constraint(expr= - 0.75*m.x28 + m.x40 - m.b130 >= -1)

m.c56 = Constraint(expr=   m.x26 - 4.45628648004517*m.b128 <= 0)

m.c57 = Constraint(expr=   m.x27 - 4.45628648004517*m.b129 <= 0)

m.c58 = Constraint(expr=   m.x28 - 4.45628648004517*m.b130 <= 0)

m.c59 = Constraint(expr=   m.x38 - 3.34221486003388*m.b128 <= 0)

m.c60 = Constraint(expr=   m.x39 - 3.34221486003388*m.b129 <= 0)

m.c61 = Constraint(expr=   m.x40 - 3.34221486003388*m.b130 <= 0)

m.c62 = Constraint(expr=-1.5*log(1 + m.x29) + m.x41 + m.b131 <= 1)

m.c63 = Constraint(expr=-1.5*log(1 + m.x30) + m.x42 + m.b132 <= 1)

m.c64 = Constraint(expr=-1.5*log(1 + m.x31) + m.x43 + m.b133 <= 1)

m.c65 = Constraint(expr=   m.x29 - 4.45628648004517*m.b131 <= 0)

m.c66 = Constraint(expr=   m.x30 - 4.45628648004517*m.b132 <= 0)

m.c67 = Constraint(expr=   m.x31 - 4.45628648004517*m.b133 <= 0)

m.c68 = Constraint(expr=   m.x41 - 2.54515263975353*m.b131 <= 0)

m.c69 = Constraint(expr=   m.x42 - 2.54515263975353*m.b132 <= 0)

m.c70 = Constraint(expr=   m.x43 - 2.54515263975353*m.b133 <= 0)

m.c71 = Constraint(expr= - m.x32 + m.x44 + m.b134 <= 1)

m.c72 = Constraint(expr= - m.x33 + m.x45 + m.b135 <= 1)

m.c73 = Constraint(expr= - m.x34 + m.x46 + m.b136 <= 1)

m.c74 = Constraint(expr= - m.x32 + m.x44 - m.b134 >= -1)

m.c75 = Constraint(expr= - m.x33 + m.x45 - m.b135 >= -1)

m.c76 = Constraint(expr= - m.x34 + m.x46 - m.b136 >= -1)

m.c77 = Constraint(expr= - 0.5*m.x35 + m.x44 + m.b134 <= 1)

m.c78 = Constraint(expr= - 0.5*m.x36 + m.x45 + m.b135 <= 1)

m.c79 = Constraint(expr= - 0.5*m.x37 + m.x46 + m.b136 <= 1)

m.c80 = Constraint(expr= - 0.5*m.x35 + m.x44 - m.b134 >= -1)

m.c81 = Constraint(expr= - 0.5*m.x36 + m.x45 - m.b135 >= -1)

m.c82 = Constraint(expr= - 0.5*m.x37 + m.x46 - m.b136 >= -1)

m.c83 = Constraint(expr=   m.x32 - 4.45628648004517*m.b134 <= 0)

m.c84 = Constraint(expr=   m.x33 - 4.45628648004517*m.b135 <= 0)

m.c85 = Constraint(expr=   m.x34 - 4.45628648004517*m.b136 <= 0)

m.c86 = Constraint(expr=   m.x35 - 30*m.b134 <= 0)

m.c87 = Constraint(expr=   m.x36 - 30*m.b135 <= 0)

m.c88 = Constraint(expr=   m.x37 - 30*m.b136 <= 0)

m.c89 = Constraint(expr=   m.x44 - 15*m.b134 <= 0)

m.c90 = Constraint(expr=   m.x45 - 15*m.b135 <= 0)

m.c91 = Constraint(expr=   m.x46 - 15*m.b136 <= 0)

m.c92 = Constraint(expr=-1.25*log(1 + m.x47) + m.x62 + m.b137 <= 1)

m.c93 = Constraint(expr=-1.25*log(1 + m.x48) + m.x63 + m.b138 <= 1)

m.c94 = Constraint(expr=-1.25*log(1 + m.x49) + m.x64 + m.b139 <= 1)

m.c95 = Constraint(expr=   m.x47 - 3.34221486003388*m.b137 <= 0)

m.c96 = Constraint(expr=   m.x48 - 3.34221486003388*m.b138 <= 0)

m.c97 = Constraint(expr=   m.x49 - 3.34221486003388*m.b139 <= 0)

m.c98 = Constraint(expr=   m.x62 - 1.83548069293539*m.b137 <= 0)

m.c99 = Constraint(expr=   m.x63 - 1.83548069293539*m.b138 <= 0)

m.c100 = Constraint(expr=   m.x64 - 1.83548069293539*m.b139 <= 0)

m.c101 = Constraint(expr=-0.9*log(1 + m.x50) + m.x65 + m.b140 <= 1)

m.c102 = Constraint(expr=-0.9*log(1 + m.x51) + m.x66 + m.b141 <= 1)

m.c103 = Constraint(expr=-0.9*log(1 + m.x52) + m.x67 + m.b142 <= 1)

m.c104 = Constraint(expr=   m.x50 - 3.34221486003388*m.b140 <= 0)

m.c105 = Constraint(expr=   m.x51 - 3.34221486003388*m.b141 <= 0)

m.c106 = Constraint(expr=   m.x52 - 3.34221486003388*m.b142 <= 0)

m.c107 = Constraint(expr=   m.x65 - 1.32154609891348*m.b140 <= 0)

m.c108 = Constraint(expr=   m.x66 - 1.32154609891348*m.b141 <= 0)

m.c109 = Constraint(expr=   m.x67 - 1.32154609891348*m.b142 <= 0)

m.c110 = Constraint(expr=-log(1 + m.x41) + m.x68 + m.b143 <= 1)

m.c111 = Constraint(expr=-log(1 + m.x42) + m.x69 + m.b144 <= 1)

m.c112 = Constraint(expr=-log(1 + m.x43) + m.x70 + m.b145 <= 1)

m.c113 = Constraint(expr=   m.x41 - 2.54515263975353*m.b143 <= 0)

m.c114 = Constraint(expr=   m.x42 - 2.54515263975353*m.b144 <= 0)

m.c115 = Constraint(expr=   m.x43 - 2.54515263975353*m.b145 <= 0)

m.c116 = Constraint(expr=   m.x68 - 1.26558121681553*m.b143 <= 0)

m.c117 = Constraint(expr=   m.x69 - 1.26558121681553*m.b144 <= 0)

m.c118 = Constraint(expr=   m.x70 - 1.26558121681553*m.b145 <= 0)

m.c119 = Constraint(expr= - 0.9*m.x53 + m.x71 + m.b146 <= 1)

m.c120 = Constraint(expr= - 0.9*m.x54 + m.x72 + m.b147 <= 1)

m.c121 = Constraint(expr= - 0.9*m.x55 + m.x73 + m.b148 <= 1)

m.c122 = Constraint(expr= - 0.9*m.x53 + m.x71 - m.b146 >= -1)

m.c123 = Constraint(expr= - 0.9*m.x54 + m.x72 - m.b147 >= -1)

m.c124 = Constraint(expr= - 0.9*m.x55 + m.x73 - m.b148 >= -1)

m.c125 = Constraint(expr=   m.x53 - 15*m.b146 <= 0)

m.c126 = Constraint(expr=   m.x54 - 15*m.b147 <= 0)

m.c127 = Constraint(expr=   m.x55 - 15*m.b148 <= 0)

m.c128 = Constraint(expr=   m.x71 - 13.5*m.b146 <= 0)

m.c129 = Constraint(expr=   m.x72 - 13.5*m.b147 <= 0)

m.c130 = Constraint(expr=   m.x73 - 13.5*m.b148 <= 0)

m.c131 = Constraint(expr= - 0.6*m.x56 + m.x74 + m.b149 <= 1)

m.c132 = Constraint(expr= - 0.6*m.x57 + m.x75 + m.b150 <= 1)

m.c133 = Constraint(expr= - 0.6*m.x58 + m.x76 + m.b151 <= 1)

m.c134 = Constraint(expr= - 0.6*m.x56 + m.x74 - m.b149 >= -1)

m.c135 = Constraint(expr= - 0.6*m.x57 + m.x75 - m.b150 >= -1)

m.c136 = Constraint(expr= - 0.6*m.x58 + m.x76 - m.b151 >= -1)

m.c137 = Constraint(expr=   m.x56 - 15*m.b149 <= 0)

m.c138 = Constraint(expr=   m.x57 - 15*m.b150 <= 0)

m.c139 = Constraint(expr=   m.x58 - 15*m.b151 <= 0)

m.c140 = Constraint(expr=   m.x74 - 9*m.b149 <= 0)

m.c141 = Constraint(expr=   m.x75 - 9*m.b150 <= 0)

m.c142 = Constraint(expr=   m.x76 - 9*m.b151 <= 0)

m.c143 = Constraint(expr=-1.1*log(1 + m.x59) + m.x77 + m.b152 <= 1)

m.c144 = Constraint(expr=-1.1*log(1 + m.x60) + m.x78 + m.b153 <= 1)

m.c145 = Constraint(expr=-1.1*log(1 + m.x61) + m.x79 + m.b154 <= 1)

m.c146 = Constraint(expr=   m.x59 - 15*m.b152 <= 0)

m.c147 = Constraint(expr=   m.x60 - 15*m.b153 <= 0)

m.c148 = Constraint(expr=   m.x61 - 15*m.b154 <= 0)

m.c149 = Constraint(expr=   m.x77 - 3.04984759446376*m.b152 <= 0)

m.c150 = Constraint(expr=   m.x78 - 3.04984759446376*m.b153 <= 0)

m.c151 = Constraint(expr=   m.x79 - 3.04984759446376*m.b154 <= 0)

m.c152 = Constraint(expr= - 0.9*m.x62 + m.x110 + m.b155 <= 1)

m.c153 = Constraint(expr= - 0.9*m.x63 + m.x111 + m.b156 <= 1)

m.c154 = Constraint(expr= - 0.9*m.x64 + m.x112 + m.b157 <= 1)

m.c155 = Constraint(expr= - 0.9*m.x62 + m.x110 - m.b155 >= -1)

m.c156 = Constraint(expr= - 0.9*m.x63 + m.x111 - m.b156 >= -1)

m.c157 = Constraint(expr= - 0.9*m.x64 + m.x112 - m.b157 >= -1)

m.c158 = Constraint(expr= - m.x86 + m.x110 + m.b155 <= 1)

m.c159 = Constraint(expr= - m.x87 + m.x111 + m.b156 <= 1)

m.c160 = Constraint(expr= - m.x88 + m.x112 + m.b157 <= 1)

m.c161 = Constraint(expr= - m.x86 + m.x110 - m.b155 >= -1)

m.c162 = Constraint(expr= - m.x87 + m.x111 - m.b156 >= -1)

m.c163 = Constraint(expr= - m.x88 + m.x112 - m.b157 >= -1)

m.c164 = Constraint(expr=   m.x62 - 1.83548069293539*m.b155 <= 0)

m.c165 = Constraint(expr=   m.x63 - 1.83548069293539*m.b156 <= 0)

m.c166 = Constraint(expr=   m.x64 - 1.83548069293539*m.b157 <= 0)

m.c167 = Constraint(expr=   m.x86 - 20*m.b155 <= 0)

m.c168 = Constraint(expr=   m.x87 - 20*m.b156 <= 0)

m.c169 = Constraint(expr=   m.x88 - 20*m.b157 <= 0)

m.c170 = Constraint(expr=   m.x110 - 20*m.b155 <= 0)

m.c171 = Constraint(expr=   m.x111 - 20*m.b156 <= 0)

m.c172 = Constraint(expr=   m.x112 - 20*m.b157 <= 0)

m.c173 = Constraint(expr=-log(1 + m.x65) + m.x113 + m.b158 <= 1)

m.c174 = Constraint(expr=-log(1 + m.x66) + m.x114 + m.b159 <= 1)

m.c175 = Constraint(expr=-log(1 + m.x67) + m.x115 + m.b160 <= 1)

m.c176 = Constraint(expr=   m.x65 - 1.32154609891348*m.b158 <= 0)

m.c177 = Constraint(expr=   m.x66 - 1.32154609891348*m.b159 <= 0)

m.c178 = Constraint(expr=   m.x67 - 1.32154609891348*m.b160 <= 0)

m.c179 = Constraint(expr=   m.x113 - 0.842233385663186*m.b158 <= 0)

m.c180 = Constraint(expr=   m.x114 - 0.842233385663186*m.b159 <= 0)

m.c181 = Constraint(expr=   m.x115 - 0.842233385663186*m.b160 <= 0)

m.c182 = Constraint(expr=-0.7*log(1 + m.x80) + m.x116 + m.b161 <= 1)

m.c183 = Constraint(expr=-0.7*log(1 + m.x81) + m.x117 + m.b162 <= 1)

m.c184 = Constraint(expr=-0.7*log(1 + m.x82) + m.x118 + m.b163 <= 1)

m.c185 = Constraint(expr=   m.x80 - 1.26558121681553*m.b161 <= 0)

m.c186 = Constraint(expr=   m.x81 - 1.26558121681553*m.b162 <= 0)

m.c187 = Constraint(expr=   m.x82 - 1.26558121681553*m.b163 <= 0)

m.c188 = Constraint(expr=   m.x116 - 0.572481933717686*m.b161 <= 0)

m.c189 = Constraint(expr=   m.x117 - 0.572481933717686*m.b162 <= 0)

m.c190 = Constraint(expr=   m.x118 - 0.572481933717686*m.b163 <= 0)

m.c191 = Constraint(expr=-0.65*log(1 + m.x83) + m.x119 + m.b164 <= 1)

m.c192 = Constraint(expr=-0.65*log(1 + m.x84) + m.x120 + m.b165 <= 1)

m.c193 = Constraint(expr=-0.65*log(1 + m.x85) + m.x121 + m.b166 <= 1)

m.c194 = Constraint(expr=-0.65*log(1 + m.x92) + m.x119 + m.b164 <= 1)

m.c195 = Constraint(expr=-0.65*log(1 + m.x93) + m.x120 + m.b165 <= 1)

m.c196 = Constraint(expr=-0.65*log(1 + m.x94) + m.x121 + m.b166 <= 1)

m.c197 = Constraint(expr=   m.x83 - 1.26558121681553*m.b164 <= 0)

m.c198 = Constraint(expr=   m.x84 - 1.26558121681553*m.b165 <= 0)

m.c199 = Constraint(expr=   m.x85 - 1.26558121681553*m.b166 <= 0)

m.c200 = Constraint(expr=   m.x92 - 33.5*m.b164 <= 0)

m.c201 = Constraint(expr=   m.x93 - 33.5*m.b165 <= 0)

m.c202 = Constraint(expr=   m.x94 - 33.5*m.b166 <= 0)

m.c203 = Constraint(expr=   m.x119 - 2.30162356062425*m.b164 <= 0)

m.c204 = Constraint(expr=   m.x120 - 2.30162356062425*m.b165 <= 0)

m.c205 = Constraint(expr=   m.x121 - 2.30162356062425*m.b166 <= 0)

m.c206 = Constraint(expr=   5*m.b167 + m.x212 <= 0)

m.c207 = Constraint(expr=   4*m.b168 + m.x213 <= 0)

m.c208 = Constraint(expr=   6*m.b169 + m.x214 <= 0)

m.c209 = Constraint(expr=   8*m.b170 + m.x215 <= 0)

m.c210 = Constraint(expr=   7*m.b171 + m.x216 <= 0)

m.c211 = Constraint(expr=   6*m.b172 + m.x217 <= 0)

m.c212 = Constraint(expr=   6*m.b173 + m.x218 <= 0)

m.c213 = Constraint(expr=   9*m.b174 + m.x219 <= 0)

m.c214 = Constraint(expr=   4*m.b175 + m.x220 <= 0)

m.c215 = Constraint(expr=   10*m.b176 + m.x221 <= 0)

m.c216 = Constraint(expr=   9*m.b177 + m.x222 <= 0)

m.c217 = Constraint(expr=   5*m.b178 + m.x223 <= 0)

m.c218 = Constraint(expr=   6*m.b179 + m.x224 <= 0)

m.c219 = Constraint(expr=   10*m.b180 + m.x225 <= 0)

m.c220 = Constraint(expr=   6*m.b181 + m.x226 <= 0)

m.c221 = Constraint(expr=   7*m.b182 + m.x227 <= 0)

m.c222 = Constraint(expr=   7*m.b183 + m.x228 <= 0)

m.c223 = Constraint(expr=   4*m.b184 + m.x229 <= 0)

m.c224 = Constraint(expr=   4*m.b185 + m.x230 <= 0)

m.c225 = Constraint(expr=   3*m.b186 + m.x231 <= 0)

m.c226 = Constraint(expr=   2*m.b187 + m.x232 <= 0)

m.c227 = Constraint(expr=   5*m.b188 + m.x233 <= 0)

m.c228 = Constraint(expr=   6*m.b189 + m.x234 <= 0)

m.c229 = Constraint(expr=   7*m.b190 + m.x235 <= 0)

m.c230 = Constraint(expr=   2*m.b191 + m.x236 <= 0)

m.c231 = Constraint(expr=   5*m.b192 + m.x237 <= 0)

m.c232 = Constraint(expr=   2*m.b193 + m.x238 <= 0)

m.c233 = Constraint(expr=   4*m.b194 + m.x239 <= 0)

m.c234 = Constraint(expr=   7*m.b195 + m.x240 <= 0)

m.c235 = Constraint(expr=   4*m.b196 + m.x241 <= 0)

m.c236 = Constraint(expr=   3*m.b197 + m.x242 <= 0)

m.c237 = Constraint(expr=   9*m.b198 + m.x243 <= 0)

m.c238 = Constraint(expr=   3*m.b199 + m.x244 <= 0)

m.c239 = Constraint(expr=   7*m.b200 + m.x245 <= 0)

m.c240 = Constraint(expr=   2*m.b201 + m.x246 <= 0)

m.c241 = Constraint(expr=   9*m.b202 + m.x247 <= 0)

m.c242 = Constraint(expr=   3*m.b203 + m.x248 <= 0)

m.c243 = Constraint(expr=   m.b204 + m.x249 <= 0)

m.c244 = Constraint(expr=   9*m.b205 + m.x250 <= 0)

m.c245 = Constraint(expr=   2*m.b206 + m.x251 <= 0)

m.c246 = Constraint(expr=   6*m.b207 + m.x252 <= 0)

m.c247 = Constraint(expr=   3*m.b208 + m.x253 <= 0)

m.c248 = Constraint(expr=   4*m.b209 + m.x254 <= 0)

m.c249 = Constraint(expr=   8*m.b210 + m.x255 <= 0)

m.c250 = Constraint(expr=   m.b211 + m.x256 <= 0)

m.c251 = Constraint(expr=   5*m.b167 + m.x212 >= 0)

m.c252 = Constraint(expr=   4*m.b168 + m.x213 >= 0)

m.c253 = Constraint(expr=   6*m.b169 + m.x214 >= 0)

m.c254 = Constraint(expr=   8*m.b170 + m.x215 >= 0)

m.c255 = Constraint(expr=   7*m.b171 + m.x216 >= 0)

m.c256 = Constraint(expr=   6*m.b172 + m.x217 >= 0)

m.c257 = Constraint(expr=   6*m.b173 + m.x218 >= 0)

m.c258 = Constraint(expr=   9*m.b174 + m.x219 >= 0)

m.c259 = Constraint(expr=   4*m.b175 + m.x220 >= 0)

m.c260 = Constraint(expr=   10*m.b176 + m.x221 >= 0)

m.c261 = Constraint(expr=   9*m.b177 + m.x222 >= 0)

m.c262 = Constraint(expr=   5*m.b178 + m.x223 >= 0)

m.c263 = Constraint(expr=   6*m.b179 + m.x224 >= 0)

m.c264 = Constraint(expr=   10*m.b180 + m.x225 >= 0)

m.c265 = Constraint(expr=   6*m.b181 + m.x226 >= 0)

m.c266 = Constraint(expr=   7*m.b182 + m.x227 >= 0)

m.c267 = Constraint(expr=   7*m.b183 + m.x228 >= 0)

m.c268 = Constraint(expr=   4*m.b184 + m.x229 >= 0)

m.c269 = Constraint(expr=   4*m.b185 + m.x230 >= 0)

m.c270 = Constraint(expr=   3*m.b186 + m.x231 >= 0)

m.c271 = Constraint(expr=   2*m.b187 + m.x232 >= 0)

m.c272 = Constraint(expr=   5*m.b188 + m.x233 >= 0)

m.c273 = Constraint(expr=   6*m.b189 + m.x234 >= 0)

m.c274 = Constraint(expr=   7*m.b190 + m.x235 >= 0)

m.c275 = Constraint(expr=   2*m.b191 + m.x236 >= 0)

m.c276 = Constraint(expr=   5*m.b192 + m.x237 >= 0)

m.c277 = Constraint(expr=   2*m.b193 + m.x238 >= 0)

m.c278 = Constraint(expr=   4*m.b194 + m.x239 >= 0)

m.c279 = Constraint(expr=   7*m.b195 + m.x240 >= 0)

m.c280 = Constraint(expr=   4*m.b196 + m.x241 >= 0)

m.c281 = Constraint(expr=   3*m.b197 + m.x242 >= 0)

m.c282 = Constraint(expr=   9*m.b198 + m.x243 >= 0)

m.c283 = Constraint(expr=   3*m.b199 + m.x244 >= 0)

m.c284 = Constraint(expr=   7*m.b200 + m.x245 >= 0)

m.c285 = Constraint(expr=   2*m.b201 + m.x246 >= 0)

m.c286 = Constraint(expr=   9*m.b202 + m.x247 >= 0)

m.c287 = Constraint(expr=   3*m.b203 + m.x248 >= 0)

m.c288 = Constraint(expr=   m.b204 + m.x249 >= 0)

m.c289 = Constraint(expr=   9*m.b205 + m.x250 >= 0)

m.c290 = Constraint(expr=   2*m.b206 + m.x251 >= 0)

m.c291 = Constraint(expr=   6*m.b207 + m.x252 >= 0)

m.c292 = Constraint(expr=   3*m.b208 + m.x253 >= 0)

m.c293 = Constraint(expr=   4*m.b209 + m.x254 >= 0)

m.c294 = Constraint(expr=   8*m.b210 + m.x255 >= 0)

m.c295 = Constraint(expr=   m.b211 + m.x256 >= 0)

m.c296 = Constraint(expr=   m.b122 - m.b123 <= 0)

m.c297 = Constraint(expr=   m.b122 - m.b124 <= 0)

m.c298 = Constraint(expr=   m.b123 - m.b124 <= 0)

m.c299 = Constraint(expr=   m.b125 - m.b126 <= 0)

m.c300 = Constraint(expr=   m.b125 - m.b127 <= 0)

m.c301 = Constraint(expr=   m.b126 - m.b127 <= 0)

m.c302 = Constraint(expr=   m.b128 - m.b129 <= 0)

m.c303 = Constraint(expr=   m.b128 - m.b130 <= 0)

m.c304 = Constraint(expr=   m.b129 - m.b130 <= 0)

m.c305 = Constraint(expr=   m.b131 - m.b132 <= 0)

m.c306 = Constraint(expr=   m.b131 - m.b133 <= 0)

m.c307 = Constraint(expr=   m.b132 - m.b133 <= 0)

m.c308 = Constraint(expr=   m.b134 - m.b135 <= 0)

m.c309 = Constraint(expr=   m.b134 - m.b136 <= 0)

m.c310 = Constraint(expr=   m.b135 - m.b136 <= 0)

m.c311 = Constraint(expr=   m.b137 - m.b138 <= 0)

m.c312 = Constraint(expr=   m.b137 - m.b139 <= 0)

m.c313 = Constraint(expr=   m.b138 - m.b139 <= 0)

m.c314 = Constraint(expr=   m.b140 - m.b141 <= 0)

m.c315 = Constraint(expr=   m.b140 - m.b142 <= 0)

m.c316 = Constraint(expr=   m.b141 - m.b142 <= 0)

m.c317 = Constraint(expr=   m.b143 - m.b144 <= 0)

m.c318 = Constraint(expr=   m.b143 - m.b145 <= 0)

m.c319 = Constraint(expr=   m.b144 - m.b145 <= 0)

m.c320 = Constraint(expr=   m.b146 - m.b147 <= 0)

m.c321 = Constraint(expr=   m.b146 - m.b148 <= 0)

m.c322 = Constraint(expr=   m.b147 - m.b148 <= 0)

m.c323 = Constraint(expr=   m.b149 - m.b150 <= 0)

m.c324 = Constraint(expr=   m.b149 - m.b151 <= 0)

m.c325 = Constraint(expr=   m.b150 - m.b151 <= 0)

m.c326 = Constraint(expr=   m.b152 - m.b153 <= 0)

m.c327 = Constraint(expr=   m.b152 - m.b154 <= 0)

m.c328 = Constraint(expr=   m.b153 - m.b154 <= 0)

m.c329 = Constraint(expr=   m.b155 - m.b156 <= 0)

m.c330 = Constraint(expr=   m.b155 - m.b157 <= 0)

m.c331 = Constraint(expr=   m.b156 - m.b157 <= 0)

m.c332 = Constraint(expr=   m.b158 - m.b159 <= 0)

m.c333 = Constraint(expr=   m.b158 - m.b160 <= 0)

m.c334 = Constraint(expr=   m.b159 - m.b160 <= 0)

m.c335 = Constraint(expr=   m.b161 - m.b162 <= 0)

m.c336 = Constraint(expr=   m.b161 - m.b163 <= 0)

m.c337 = Constraint(expr=   m.b162 - m.b163 <= 0)

m.c338 = Constraint(expr=   m.b164 - m.b165 <= 0)

m.c339 = Constraint(expr=   m.b164 - m.b166 <= 0)

m.c340 = Constraint(expr=   m.b165 - m.b166 <= 0)

m.c341 = Constraint(expr=   m.b167 + m.b168 <= 1)

m.c342 = Constraint(expr=   m.b167 + m.b169 <= 1)

m.c343 = Constraint(expr=   m.b167 + m.b168 <= 1)

m.c344 = Constraint(expr=   m.b168 + m.b169 <= 1)

m.c345 = Constraint(expr=   m.b167 + m.b169 <= 1)

m.c346 = Constraint(expr=   m.b168 + m.b169 <= 1)

m.c347 = Constraint(expr=   m.b170 + m.b171 <= 1)

m.c348 = Constraint(expr=   m.b170 + m.b172 <= 1)

m.c349 = Constraint(expr=   m.b170 + m.b171 <= 1)

m.c350 = Constraint(expr=   m.b171 + m.b172 <= 1)

m.c351 = Constraint(expr=   m.b170 + m.b172 <= 1)

m.c352 = Constraint(expr=   m.b171 + m.b172 <= 1)

m.c353 = Constraint(expr=   m.b173 + m.b174 <= 1)

m.c354 = Constraint(expr=   m.b173 + m.b175 <= 1)

m.c355 = Constraint(expr=   m.b173 + m.b174 <= 1)

m.c356 = Constraint(expr=   m.b174 + m.b175 <= 1)

m.c357 = Constraint(expr=   m.b173 + m.b175 <= 1)

m.c358 = Constraint(expr=   m.b174 + m.b175 <= 1)

m.c359 = Constraint(expr=   m.b176 + m.b177 <= 1)

m.c360 = Constraint(expr=   m.b176 + m.b178 <= 1)

m.c361 = Constraint(expr=   m.b176 + m.b177 <= 1)

m.c362 = Constraint(expr=   m.b177 + m.b178 <= 1)

m.c363 = Constraint(expr=   m.b176 + m.b178 <= 1)

m.c364 = Constraint(expr=   m.b177 + m.b178 <= 1)

m.c365 = Constraint(expr=   m.b179 + m.b180 <= 1)

m.c366 = Constraint(expr=   m.b179 + m.b181 <= 1)

m.c367 = Constraint(expr=   m.b179 + m.b180 <= 1)

m.c368 = Constraint(expr=   m.b180 + m.b181 <= 1)

m.c369 = Constraint(expr=   m.b179 + m.b181 <= 1)

m.c370 = Constraint(expr=   m.b180 + m.b181 <= 1)

m.c371 = Constraint(expr=   m.b182 + m.b183 <= 1)

m.c372 = Constraint(expr=   m.b182 + m.b184 <= 1)

m.c373 = Constraint(expr=   m.b182 + m.b183 <= 1)

m.c374 = Constraint(expr=   m.b183 + m.b184 <= 1)

m.c375 = Constraint(expr=   m.b182 + m.b184 <= 1)

m.c376 = Constraint(expr=   m.b183 + m.b184 <= 1)

m.c377 = Constraint(expr=   m.b185 + m.b186 <= 1)

m.c378 = Constraint(expr=   m.b185 + m.b187 <= 1)

m.c379 = Constraint(expr=   m.b185 + m.b186 <= 1)

m.c380 = Constraint(expr=   m.b186 + m.b187 <= 1)

m.c381 = Constraint(expr=   m.b185 + m.b187 <= 1)

m.c382 = Constraint(expr=   m.b186 + m.b187 <= 1)

m.c383 = Constraint(expr=   m.b188 + m.b189 <= 1)

m.c384 = Constraint(expr=   m.b188 + m.b190 <= 1)

m.c385 = Constraint(expr=   m.b188 + m.b189 <= 1)

m.c386 = Constraint(expr=   m.b189 + m.b190 <= 1)

m.c387 = Constraint(expr=   m.b188 + m.b190 <= 1)

m.c388 = Constraint(expr=   m.b189 + m.b190 <= 1)

m.c389 = Constraint(expr=   m.b191 + m.b192 <= 1)

m.c390 = Constraint(expr=   m.b191 + m.b193 <= 1)

m.c391 = Constraint(expr=   m.b191 + m.b192 <= 1)

m.c392 = Constraint(expr=   m.b192 + m.b193 <= 1)

m.c393 = Constraint(expr=   m.b191 + m.b193 <= 1)

m.c394 = Constraint(expr=   m.b192 + m.b193 <= 1)

m.c395 = Constraint(expr=   m.b194 + m.b195 <= 1)

m.c396 = Constraint(expr=   m.b194 + m.b196 <= 1)

m.c397 = Constraint(expr=   m.b194 + m.b195 <= 1)

m.c398 = Constraint(expr=   m.b195 + m.b196 <= 1)

m.c399 = Constraint(expr=   m.b194 + m.b196 <= 1)

m.c400 = Constraint(expr=   m.b195 + m.b196 <= 1)

m.c401 = Constraint(expr=   m.b197 + m.b198 <= 1)

m.c402 = Constraint(expr=   m.b197 + m.b199 <= 1)

m.c403 = Constraint(expr=   m.b197 + m.b198 <= 1)

m.c404 = Constraint(expr=   m.b198 + m.b199 <= 1)

m.c405 = Constraint(expr=   m.b197 + m.b199 <= 1)

m.c406 = Constraint(expr=   m.b198 + m.b199 <= 1)

m.c407 = Constraint(expr=   m.b200 + m.b201 <= 1)

m.c408 = Constraint(expr=   m.b200 + m.b202 <= 1)

m.c409 = Constraint(expr=   m.b200 + m.b201 <= 1)

m.c410 = Constraint(expr=   m.b201 + m.b202 <= 1)

m.c411 = Constraint(expr=   m.b200 + m.b202 <= 1)

m.c412 = Constraint(expr=   m.b201 + m.b202 <= 1)

m.c413 = Constraint(expr=   m.b203 + m.b204 <= 1)

m.c414 = Constraint(expr=   m.b203 + m.b205 <= 1)

m.c415 = Constraint(expr=   m.b203 + m.b204 <= 1)

m.c416 = Constraint(expr=   m.b204 + m.b205 <= 1)

m.c417 = Constraint(expr=   m.b203 + m.b205 <= 1)

m.c418 = Constraint(expr=   m.b204 + m.b205 <= 1)

m.c419 = Constraint(expr=   m.b206 + m.b207 <= 1)

m.c420 = Constraint(expr=   m.b206 + m.b208 <= 1)

m.c421 = Constraint(expr=   m.b206 + m.b207 <= 1)

m.c422 = Constraint(expr=   m.b207 + m.b208 <= 1)

m.c423 = Constraint(expr=   m.b206 + m.b208 <= 1)

m.c424 = Constraint(expr=   m.b207 + m.b208 <= 1)

m.c425 = Constraint(expr=   m.b209 + m.b210 <= 1)

m.c426 = Constraint(expr=   m.b209 + m.b211 <= 1)

m.c427 = Constraint(expr=   m.b209 + m.b210 <= 1)

m.c428 = Constraint(expr=   m.b210 + m.b211 <= 1)

m.c429 = Constraint(expr=   m.b209 + m.b211 <= 1)

m.c430 = Constraint(expr=   m.b210 + m.b211 <= 1)

m.c431 = Constraint(expr=   m.b122 - m.b167 <= 0)

m.c432 = Constraint(expr= - m.b122 + m.b123 - m.b168 <= 0)

m.c433 = Constraint(expr= - m.b122 - m.b123 + m.b124 - m.b169 <= 0)

m.c434 = Constraint(expr=   m.b125 - m.b170 <= 0)

m.c435 = Constraint(expr= - m.b125 + m.b126 - m.b171 <= 0)

m.c436 = Constraint(expr= - m.b125 - m.b126 + m.b127 - m.b172 <= 0)

m.c437 = Constraint(expr=   m.b128 - m.b173 <= 0)

m.c438 = Constraint(expr= - m.b128 + m.b129 - m.b174 <= 0)

m.c439 = Constraint(expr= - m.b128 - m.b129 + m.b130 - m.b175 <= 0)

m.c440 = Constraint(expr=   m.b131 - m.b176 <= 0)

m.c441 = Constraint(expr= - m.b131 + m.b132 - m.b177 <= 0)

m.c442 = Constraint(expr= - m.b131 - m.b132 + m.b133 - m.b178 <= 0)

m.c443 = Constraint(expr=   m.b134 - m.b179 <= 0)

m.c444 = Constraint(expr= - m.b134 + m.b135 - m.b180 <= 0)

m.c445 = Constraint(expr= - m.b134 - m.b135 + m.b136 - m.b181 <= 0)

m.c446 = Constraint(expr=   m.b137 - m.b182 <= 0)

m.c447 = Constraint(expr= - m.b137 + m.b138 - m.b183 <= 0)

m.c448 = Constraint(expr= - m.b137 - m.b138 + m.b139 - m.b184 <= 0)

m.c449 = Constraint(expr=   m.b140 - m.b185 <= 0)

m.c450 = Constraint(expr= - m.b140 + m.b141 - m.b186 <= 0)

m.c451 = Constraint(expr= - m.b140 - m.b141 + m.b142 - m.b187 <= 0)

m.c452 = Constraint(expr=   m.b143 - m.b188 <= 0)

m.c453 = Constraint(expr= - m.b143 + m.b144 - m.b189 <= 0)

m.c454 = Constraint(expr= - m.b143 - m.b144 + m.b145 - m.b190 <= 0)

m.c455 = Constraint(expr=   m.b146 - m.b191 <= 0)

m.c456 = Constraint(expr= - m.b146 + m.b147 - m.b192 <= 0)

m.c457 = Constraint(expr= - m.b146 - m.b147 + m.b148 - m.b193 <= 0)

m.c458 = Constraint(expr=   m.b149 - m.b194 <= 0)

m.c459 = Constraint(expr= - m.b149 + m.b150 - m.b195 <= 0)

m.c460 = Constraint(expr= - m.b149 - m.b150 + m.b151 - m.b196 <= 0)

m.c461 = Constraint(expr=   m.b152 - m.b197 <= 0)

m.c462 = Constraint(expr= - m.b152 + m.b153 - m.b198 <= 0)

m.c463 = Constraint(expr= - m.b152 - m.b153 + m.b154 - m.b199 <= 0)

m.c464 = Constraint(expr=   m.b155 - m.b200 <= 0)

m.c465 = Constraint(expr= - m.b155 + m.b156 - m.b201 <= 0)

m.c466 = Constraint(expr= - m.b155 - m.b156 + m.b157 - m.b202 <= 0)

m.c467 = Constraint(expr=   m.b158 - m.b203 <= 0)

m.c468 = Constraint(expr= - m.b158 + m.b159 - m.b204 <= 0)

m.c469 = Constraint(expr= - m.b158 - m.b159 + m.b160 - m.b205 <= 0)

m.c470 = Constraint(expr=   m.b161 - m.b206 <= 0)

m.c471 = Constraint(expr= - m.b161 + m.b162 - m.b207 <= 0)

m.c472 = Constraint(expr= - m.b161 - m.b162 + m.b163 - m.b208 <= 0)

m.c473 = Constraint(expr=   m.b164 - m.b209 <= 0)

m.c474 = Constraint(expr= - m.b164 + m.b165 - m.b210 <= 0)

m.c475 = Constraint(expr= - m.b164 - m.b165 + m.b166 - m.b211 <= 0)

m.c476 = Constraint(expr=   m.b122 + m.b125 == 1)

m.c477 = Constraint(expr=   m.b123 + m.b126 == 1)

m.c478 = Constraint(expr=   m.b124 + m.b127 == 1)

m.c479 = Constraint(expr= - m.b128 + m.b137 + m.b140 >= 0)

m.c480 = Constraint(expr= - m.b129 + m.b138 + m.b141 >= 0)

m.c481 = Constraint(expr= - m.b130 + m.b139 + m.b142 >= 0)

m.c482 = Constraint(expr= - m.b137 + m.b155 >= 0)

m.c483 = Constraint(expr= - m.b138 + m.b156 >= 0)

m.c484 = Constraint(expr= - m.b139 + m.b157 >= 0)

m.c485 = Constraint(expr= - m.b140 + m.b158 >= 0)

m.c486 = Constraint(expr= - m.b141 + m.b159 >= 0)

m.c487 = Constraint(expr= - m.b142 + m.b160 >= 0)

m.c488 = Constraint(expr= - m.b131 + m.b143 >= 0)

m.c489 = Constraint(expr= - m.b132 + m.b144 >= 0)

m.c490 = Constraint(expr= - m.b133 + m.b145 >= 0)

m.c491 = Constraint(expr= - m.b143 + m.b161 + m.b164 >= 0)

m.c492 = Constraint(expr= - m.b144 + m.b162 + m.b165 >= 0)

m.c493 = Constraint(expr= - m.b145 + m.b163 + m.b166 >= 0)

m.c494 = Constraint(expr= - m.b134 + m.b146 + m.b149 + m.b152 >= 0)

m.c495 = Constraint(expr= - m.b135 + m.b147 + m.b150 + m.b153 >= 0)

m.c496 = Constraint(expr= - m.b136 + m.b148 + m.b151 + m.b154 >= 0)

m.c497 = Constraint(expr= - m.b146 + m.b164 >= 0)

m.c498 = Constraint(expr= - m.b147 + m.b165 >= 0)

m.c499 = Constraint(expr= - m.b148 + m.b166 >= 0)

m.c500 = Constraint(expr=   m.b122 + m.b125 - m.b128 >= 0)

m.c501 = Constraint(expr=   m.b123 + m.b126 - m.b129 >= 0)

m.c502 = Constraint(expr=   m.b124 + m.b127 - m.b130 >= 0)

m.c503 = Constraint(expr=   m.b122 + m.b125 - m.b131 >= 0)

m.c504 = Constraint(expr=   m.b123 + m.b126 - m.b132 >= 0)

m.c505 = Constraint(expr=   m.b124 + m.b127 - m.b133 >= 0)

m.c506 = Constraint(expr=   m.b122 + m.b125 - m.b134 >= 0)

m.c507 = Constraint(expr=   m.b123 + m.b126 - m.b135 >= 0)

m.c508 = Constraint(expr=   m.b124 + m.b127 - m.b136 >= 0)

m.c509 = Constraint(expr=   m.b128 - m.b137 >= 0)

m.c510 = Constraint(expr=   m.b129 - m.b138 >= 0)

m.c511 = Constraint(expr=   m.b130 - m.b139 >= 0)

m.c512 = Constraint(expr=   m.b128 - m.b140 >= 0)

m.c513 = Constraint(expr=   m.b129 - m.b141 >= 0)

m.c514 = Constraint(expr=   m.b130 - m.b142 >= 0)

m.c515 = Constraint(expr=   m.b131 - m.b143 >= 0)

m.c516 = Constraint(expr=   m.b132 - m.b144 >= 0)

m.c517 = Constraint(expr=   m.b133 - m.b145 >= 0)

m.c518 = Constraint(expr=   m.b134 - m.b146 >= 0)

m.c519 = Constraint(expr=   m.b135 - m.b147 >= 0)

m.c520 = Constraint(expr=   m.b136 - m.b148 >= 0)

m.c521 = Constraint(expr=   m.b134 - m.b149 >= 0)

m.c522 = Constraint(expr=   m.b135 - m.b150 >= 0)

m.c523 = Constraint(expr=   m.b136 - m.b151 >= 0)

m.c524 = Constraint(expr=   m.b134 - m.b152 >= 0)

m.c525 = Constraint(expr=   m.b135 - m.b153 >= 0)

m.c526 = Constraint(expr=   m.b136 - m.b154 >= 0)

m.c527 = Constraint(expr=   m.b137 - m.b155 >= 0)

m.c528 = Constraint(expr=   m.b138 - m.b156 >= 0)

m.c529 = Constraint(expr=   m.b139 - m.b157 >= 0)

m.c530 = Constraint(expr=   m.b140 - m.b158 >= 0)

m.c531 = Constraint(expr=   m.b141 - m.b159 >= 0)

m.c532 = Constraint(expr=   m.b142 - m.b160 >= 0)

m.c533 = Constraint(expr=   m.b143 - m.b161 >= 0)

m.c534 = Constraint(expr=   m.b144 - m.b162 >= 0)

m.c535 = Constraint(expr=   m.b145 - m.b163 >= 0)

m.c536 = Constraint(expr=   m.b143 - m.b164 >= 0)

m.c537 = Constraint(expr=   m.b144 - m.b165 >= 0)

m.c538 = Constraint(expr=   m.b145 - m.b166 >= 0)

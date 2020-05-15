#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        407       23      112      272        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        211      131       80        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1011      983       28        0
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
m.x58 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x172 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)
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

m.obj = Objective(expr= - m.x2 - m.x3 + 5*m.x14 + 10*m.x15 - 2*m.x24 - m.x25 - 10*m.x58 - 5*m.x59 - 5*m.x60 - 5*m.x61
                        + 80*m.x74 + 130*m.x75 + 110*m.x76 + 120*m.x77 + 110*m.x78 + 130*m.x79 + 80*m.x80 + 90*m.x81
                        + 285*m.x82 + 390*m.x83 + 290*m.x84 + 405*m.x85 + 280*m.x86 + 400*m.x87 + 290*m.x88 + 300*m.x89
                        + 350*m.x90 + 250*m.x91 - 5*m.b132 - 4*m.b133 - 8*m.b134 - 7*m.b135 - 6*m.b136 - 9*m.b137
                        - 10*m.b138 - 9*m.b139 - 6*m.b140 - 10*m.b141 - 7*m.b142 - 7*m.b143 - 4*m.b144 - 3*m.b145
                        - 5*m.b146 - 6*m.b147 - 2*m.b148 - 5*m.b149 - 4*m.b150 - 7*m.b151 - 3*m.b152 - 9*m.b153
                        - 7*m.b154 - 2*m.b155 - 3*m.b156 - m.b157 - 2*m.b158 - 6*m.b159 - 4*m.b160 - 8*m.b161 - 2*m.b162
                        - 5*m.b163 - 3*m.b164 - 4*m.b165 - 5*m.b166 - 7*m.b167 - 2*m.b168 - 8*m.b169 - m.b170 - 4*m.b171
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x4 - m.x6 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x5 - m.x7 == 0)

m.c4 = Constraint(expr= - m.x8 - m.x10 + m.x12 == 0)

m.c5 = Constraint(expr= - m.x9 - m.x11 + m.x13 == 0)

m.c6 = Constraint(expr=   m.x12 - m.x14 - m.x16 == 0)

m.c7 = Constraint(expr=   m.x13 - m.x15 - m.x17 == 0)

m.c8 = Constraint(expr=   m.x16 - m.x18 - m.x20 - m.x22 == 0)

m.c9 = Constraint(expr=   m.x17 - m.x19 - m.x21 - m.x23 == 0)

m.c10 = Constraint(expr=   m.x26 - m.x32 - m.x34 == 0)

m.c11 = Constraint(expr=   m.x27 - m.x33 - m.x35 == 0)

m.c12 = Constraint(expr=   m.x30 - m.x36 - m.x38 - m.x40 == 0)

m.c13 = Constraint(expr=   m.x31 - m.x37 - m.x39 - m.x41 == 0)

m.c14 = Constraint(expr=   m.x46 - m.x54 - m.x56 == 0)

m.c15 = Constraint(expr=   m.x47 - m.x55 - m.x57 == 0)

m.c16 = Constraint(expr= - m.x48 - m.x60 + m.x62 == 0)

m.c17 = Constraint(expr= - m.x49 - m.x61 + m.x63 == 0)

m.c18 = Constraint(expr=   m.x50 - m.x64 - m.x66 == 0)

m.c19 = Constraint(expr=   m.x51 - m.x65 - m.x67 == 0)

m.c20 = Constraint(expr=   m.x52 - m.x68 - m.x70 - m.x72 == 0)

m.c21 = Constraint(expr=   m.x53 - m.x69 - m.x71 - m.x73 == 0)

m.c22 = Constraint(expr=-log(1 + m.x4) + m.x8 + m.b92 <= 1)

m.c23 = Constraint(expr=-log(1 + m.x5) + m.x9 + m.b93 <= 1)

m.c24 = Constraint(expr=   m.x4 - 40*m.b92 <= 0)

m.c25 = Constraint(expr=   m.x5 - 40*m.b93 <= 0)

m.c26 = Constraint(expr=   m.x8 - 3.71357206670431*m.b92 <= 0)

m.c27 = Constraint(expr=   m.x9 - 3.71357206670431*m.b93 <= 0)

m.c28 = Constraint(expr=-1.2*log(1 + m.x6) + m.x10 + m.b94 <= 1)

m.c29 = Constraint(expr=-1.2*log(1 + m.x7) + m.x11 + m.b95 <= 1)

m.c30 = Constraint(expr=   m.x6 - 40*m.b94 <= 0)

m.c31 = Constraint(expr=   m.x7 - 40*m.b95 <= 0)

m.c32 = Constraint(expr=   m.x10 - 4.45628648004517*m.b94 <= 0)

m.c33 = Constraint(expr=   m.x11 - 4.45628648004517*m.b95 <= 0)

m.c34 = Constraint(expr= - 0.75*m.x18 + m.x26 + m.b96 <= 1)

m.c35 = Constraint(expr= - 0.75*m.x19 + m.x27 + m.b97 <= 1)

m.c36 = Constraint(expr= - 0.75*m.x18 + m.x26 - m.b96 >= -1)

m.c37 = Constraint(expr= - 0.75*m.x19 + m.x27 - m.b97 >= -1)

m.c38 = Constraint(expr=   m.x18 - 4.45628648004517*m.b96 <= 0)

m.c39 = Constraint(expr=   m.x19 - 4.45628648004517*m.b97 <= 0)

m.c40 = Constraint(expr=   m.x26 - 3.34221486003388*m.b96 <= 0)

m.c41 = Constraint(expr=   m.x27 - 3.34221486003388*m.b97 <= 0)

m.c42 = Constraint(expr=-1.5*log(1 + m.x20) + m.x28 + m.b98 <= 1)

m.c43 = Constraint(expr=-1.5*log(1 + m.x21) + m.x29 + m.b99 <= 1)

m.c44 = Constraint(expr=   m.x20 - 4.45628648004517*m.b98 <= 0)

m.c45 = Constraint(expr=   m.x21 - 4.45628648004517*m.b99 <= 0)

m.c46 = Constraint(expr=   m.x28 - 2.54515263975353*m.b98 <= 0)

m.c47 = Constraint(expr=   m.x29 - 2.54515263975353*m.b99 <= 0)

m.c48 = Constraint(expr= - m.x22 + m.x30 + m.b100 <= 1)

m.c49 = Constraint(expr= - m.x23 + m.x31 + m.b101 <= 1)

m.c50 = Constraint(expr= - m.x22 + m.x30 - m.b100 >= -1)

m.c51 = Constraint(expr= - m.x23 + m.x31 - m.b101 >= -1)

m.c52 = Constraint(expr= - 0.5*m.x24 + m.x30 + m.b100 <= 1)

m.c53 = Constraint(expr= - 0.5*m.x25 + m.x31 + m.b101 <= 1)

m.c54 = Constraint(expr= - 0.5*m.x24 + m.x30 - m.b100 >= -1)

m.c55 = Constraint(expr= - 0.5*m.x25 + m.x31 - m.b101 >= -1)

m.c56 = Constraint(expr=   m.x22 - 4.45628648004517*m.b100 <= 0)

m.c57 = Constraint(expr=   m.x23 - 4.45628648004517*m.b101 <= 0)

m.c58 = Constraint(expr=   m.x24 - 30*m.b100 <= 0)

m.c59 = Constraint(expr=   m.x25 - 30*m.b101 <= 0)

m.c60 = Constraint(expr=   m.x30 - 15*m.b100 <= 0)

m.c61 = Constraint(expr=   m.x31 - 15*m.b101 <= 0)

m.c62 = Constraint(expr=-1.25*log(1 + m.x32) + m.x42 + m.b102 <= 1)

m.c63 = Constraint(expr=-1.25*log(1 + m.x33) + m.x43 + m.b103 <= 1)

m.c64 = Constraint(expr=   m.x32 - 3.34221486003388*m.b102 <= 0)

m.c65 = Constraint(expr=   m.x33 - 3.34221486003388*m.b103 <= 0)

m.c66 = Constraint(expr=   m.x42 - 1.83548069293539*m.b102 <= 0)

m.c67 = Constraint(expr=   m.x43 - 1.83548069293539*m.b103 <= 0)

m.c68 = Constraint(expr=-0.9*log(1 + m.x34) + m.x44 + m.b104 <= 1)

m.c69 = Constraint(expr=-0.9*log(1 + m.x35) + m.x45 + m.b105 <= 1)

m.c70 = Constraint(expr=   m.x34 - 3.34221486003388*m.b104 <= 0)

m.c71 = Constraint(expr=   m.x35 - 3.34221486003388*m.b105 <= 0)

m.c72 = Constraint(expr=   m.x44 - 1.32154609891348*m.b104 <= 0)

m.c73 = Constraint(expr=   m.x45 - 1.32154609891348*m.b105 <= 0)

m.c74 = Constraint(expr=-log(1 + m.x28) + m.x46 + m.b106 <= 1)

m.c75 = Constraint(expr=-log(1 + m.x29) + m.x47 + m.b107 <= 1)

m.c76 = Constraint(expr=   m.x28 - 2.54515263975353*m.b106 <= 0)

m.c77 = Constraint(expr=   m.x29 - 2.54515263975353*m.b107 <= 0)

m.c78 = Constraint(expr=   m.x46 - 1.26558121681553*m.b106 <= 0)

m.c79 = Constraint(expr=   m.x47 - 1.26558121681553*m.b107 <= 0)

m.c80 = Constraint(expr= - 0.9*m.x36 + m.x48 + m.b108 <= 1)

m.c81 = Constraint(expr= - 0.9*m.x37 + m.x49 + m.b109 <= 1)

m.c82 = Constraint(expr= - 0.9*m.x36 + m.x48 - m.b108 >= -1)

m.c83 = Constraint(expr= - 0.9*m.x37 + m.x49 - m.b109 >= -1)

m.c84 = Constraint(expr=   m.x36 - 15*m.b108 <= 0)

m.c85 = Constraint(expr=   m.x37 - 15*m.b109 <= 0)

m.c86 = Constraint(expr=   m.x48 - 13.5*m.b108 <= 0)

m.c87 = Constraint(expr=   m.x49 - 13.5*m.b109 <= 0)

m.c88 = Constraint(expr= - 0.6*m.x38 + m.x50 + m.b110 <= 1)

m.c89 = Constraint(expr= - 0.6*m.x39 + m.x51 + m.b111 <= 1)

m.c90 = Constraint(expr= - 0.6*m.x38 + m.x50 - m.b110 >= -1)

m.c91 = Constraint(expr= - 0.6*m.x39 + m.x51 - m.b111 >= -1)

m.c92 = Constraint(expr=   m.x38 - 15*m.b110 <= 0)

m.c93 = Constraint(expr=   m.x39 - 15*m.b111 <= 0)

m.c94 = Constraint(expr=   m.x50 - 9*m.b110 <= 0)

m.c95 = Constraint(expr=   m.x51 - 9*m.b111 <= 0)

m.c96 = Constraint(expr=-1.1*log(1 + m.x40) + m.x52 + m.b112 <= 1)

m.c97 = Constraint(expr=-1.1*log(1 + m.x41) + m.x53 + m.b113 <= 1)

m.c98 = Constraint(expr=   m.x40 - 15*m.b112 <= 0)

m.c99 = Constraint(expr=   m.x41 - 15*m.b113 <= 0)

m.c100 = Constraint(expr=   m.x52 - 3.04984759446376*m.b112 <= 0)

m.c101 = Constraint(expr=   m.x53 - 3.04984759446376*m.b113 <= 0)

m.c102 = Constraint(expr= - 0.9*m.x42 + m.x74 + m.b114 <= 1)

m.c103 = Constraint(expr= - 0.9*m.x43 + m.x75 + m.b115 <= 1)

m.c104 = Constraint(expr= - 0.9*m.x42 + m.x74 - m.b114 >= -1)

m.c105 = Constraint(expr= - 0.9*m.x43 + m.x75 - m.b115 >= -1)

m.c106 = Constraint(expr= - m.x58 + m.x74 + m.b114 <= 1)

m.c107 = Constraint(expr= - m.x59 + m.x75 + m.b115 <= 1)

m.c108 = Constraint(expr= - m.x58 + m.x74 - m.b114 >= -1)

m.c109 = Constraint(expr= - m.x59 + m.x75 - m.b115 >= -1)

m.c110 = Constraint(expr=   m.x42 - 1.83548069293539*m.b114 <= 0)

m.c111 = Constraint(expr=   m.x43 - 1.83548069293539*m.b115 <= 0)

m.c112 = Constraint(expr=   m.x58 - 20*m.b114 <= 0)

m.c113 = Constraint(expr=   m.x59 - 20*m.b115 <= 0)

m.c114 = Constraint(expr=   m.x74 - 20*m.b114 <= 0)

m.c115 = Constraint(expr=   m.x75 - 20*m.b115 <= 0)

m.c116 = Constraint(expr=-log(1 + m.x44) + m.x76 + m.b116 <= 1)

m.c117 = Constraint(expr=-log(1 + m.x45) + m.x77 + m.b117 <= 1)

m.c118 = Constraint(expr=   m.x44 - 1.32154609891348*m.b116 <= 0)

m.c119 = Constraint(expr=   m.x45 - 1.32154609891348*m.b117 <= 0)

m.c120 = Constraint(expr=   m.x76 - 0.842233385663186*m.b116 <= 0)

m.c121 = Constraint(expr=   m.x77 - 0.842233385663186*m.b117 <= 0)

m.c122 = Constraint(expr=-0.7*log(1 + m.x54) + m.x78 + m.b118 <= 1)

m.c123 = Constraint(expr=-0.7*log(1 + m.x55) + m.x79 + m.b119 <= 1)

m.c124 = Constraint(expr=   m.x54 - 1.26558121681553*m.b118 <= 0)

m.c125 = Constraint(expr=   m.x55 - 1.26558121681553*m.b119 <= 0)

m.c126 = Constraint(expr=   m.x78 - 0.572481933717686*m.b118 <= 0)

m.c127 = Constraint(expr=   m.x79 - 0.572481933717686*m.b119 <= 0)

m.c128 = Constraint(expr=-0.65*log(1 + m.x56) + m.x80 + m.b120 <= 1)

m.c129 = Constraint(expr=-0.65*log(1 + m.x57) + m.x81 + m.b121 <= 1)

m.c130 = Constraint(expr=-0.65*log(1 + m.x62) + m.x80 + m.b120 <= 1)

m.c131 = Constraint(expr=-0.65*log(1 + m.x63) + m.x81 + m.b121 <= 1)

m.c132 = Constraint(expr=   m.x56 - 1.26558121681553*m.b120 <= 0)

m.c133 = Constraint(expr=   m.x57 - 1.26558121681553*m.b121 <= 0)

m.c134 = Constraint(expr=   m.x62 - 33.5*m.b120 <= 0)

m.c135 = Constraint(expr=   m.x63 - 33.5*m.b121 <= 0)

m.c136 = Constraint(expr=   m.x80 - 2.30162356062425*m.b120 <= 0)

m.c137 = Constraint(expr=   m.x81 - 2.30162356062425*m.b121 <= 0)

m.c138 = Constraint(expr= - m.x64 + m.x82 + m.b122 <= 1)

m.c139 = Constraint(expr= - m.x65 + m.x83 + m.b123 <= 1)

m.c140 = Constraint(expr= - m.x64 + m.x82 - m.b122 >= -1)

m.c141 = Constraint(expr= - m.x65 + m.x83 - m.b123 >= -1)

m.c142 = Constraint(expr=   m.x64 - 9*m.b122 <= 0)

m.c143 = Constraint(expr=   m.x65 - 9*m.b123 <= 0)

m.c144 = Constraint(expr=   m.x82 - 9*m.b122 <= 0)

m.c145 = Constraint(expr=   m.x83 - 9*m.b123 <= 0)

m.c146 = Constraint(expr= - m.x66 + m.x84 + m.b124 <= 1)

m.c147 = Constraint(expr= - m.x67 + m.x85 + m.b125 <= 1)

m.c148 = Constraint(expr= - m.x66 + m.x84 - m.b124 >= -1)

m.c149 = Constraint(expr= - m.x67 + m.x85 - m.b125 >= -1)

m.c150 = Constraint(expr=   m.x66 - 9*m.b124 <= 0)

m.c151 = Constraint(expr=   m.x67 - 9*m.b125 <= 0)

m.c152 = Constraint(expr=   m.x84 - 9*m.b124 <= 0)

m.c153 = Constraint(expr=   m.x85 - 9*m.b125 <= 0)

m.c154 = Constraint(expr=-0.75*log(1 + m.x68) + m.x86 + m.b126 <= 1)

m.c155 = Constraint(expr=-0.75*log(1 + m.x69) + m.x87 + m.b127 <= 1)

m.c156 = Constraint(expr=   m.x68 - 3.04984759446376*m.b126 <= 0)

m.c157 = Constraint(expr=   m.x69 - 3.04984759446376*m.b127 <= 0)

m.c158 = Constraint(expr=   m.x86 - 1.04900943706034*m.b126 <= 0)

m.c159 = Constraint(expr=   m.x87 - 1.04900943706034*m.b127 <= 0)

m.c160 = Constraint(expr=-0.8*log(1 + m.x70) + m.x88 + m.b128 <= 1)

m.c161 = Constraint(expr=-0.8*log(1 + m.x71) + m.x89 + m.b129 <= 1)

m.c162 = Constraint(expr=   m.x70 - 3.04984759446376*m.b128 <= 0)

m.c163 = Constraint(expr=   m.x71 - 3.04984759446376*m.b129 <= 0)

m.c164 = Constraint(expr=   m.x88 - 1.11894339953103*m.b128 <= 0)

m.c165 = Constraint(expr=   m.x89 - 1.11894339953103*m.b129 <= 0)

m.c166 = Constraint(expr=-0.85*log(1 + m.x72) + m.x90 + m.b130 <= 1)

m.c167 = Constraint(expr=-0.85*log(1 + m.x73) + m.x91 + m.b131 <= 1)

m.c168 = Constraint(expr=   m.x72 - 3.04984759446376*m.b130 <= 0)

m.c169 = Constraint(expr=   m.x73 - 3.04984759446376*m.b131 <= 0)

m.c170 = Constraint(expr=   m.x90 - 1.18887736200171*m.b130 <= 0)

m.c171 = Constraint(expr=   m.x91 - 1.18887736200171*m.b131 <= 0)

m.c172 = Constraint(expr=   5*m.b132 + m.x172 <= 0)

m.c173 = Constraint(expr=   4*m.b133 + m.x173 <= 0)

m.c174 = Constraint(expr=   8*m.b134 + m.x174 <= 0)

m.c175 = Constraint(expr=   7*m.b135 + m.x175 <= 0)

m.c176 = Constraint(expr=   6*m.b136 + m.x176 <= 0)

m.c177 = Constraint(expr=   9*m.b137 + m.x177 <= 0)

m.c178 = Constraint(expr=   10*m.b138 + m.x178 <= 0)

m.c179 = Constraint(expr=   9*m.b139 + m.x179 <= 0)

m.c180 = Constraint(expr=   6*m.b140 + m.x180 <= 0)

m.c181 = Constraint(expr=   10*m.b141 + m.x181 <= 0)

m.c182 = Constraint(expr=   7*m.b142 + m.x182 <= 0)

m.c183 = Constraint(expr=   7*m.b143 + m.x183 <= 0)

m.c184 = Constraint(expr=   4*m.b144 + m.x184 <= 0)

m.c185 = Constraint(expr=   3*m.b145 + m.x185 <= 0)

m.c186 = Constraint(expr=   5*m.b146 + m.x186 <= 0)

m.c187 = Constraint(expr=   6*m.b147 + m.x187 <= 0)

m.c188 = Constraint(expr=   2*m.b148 + m.x188 <= 0)

m.c189 = Constraint(expr=   5*m.b149 + m.x189 <= 0)

m.c190 = Constraint(expr=   4*m.b150 + m.x190 <= 0)

m.c191 = Constraint(expr=   7*m.b151 + m.x191 <= 0)

m.c192 = Constraint(expr=   3*m.b152 + m.x192 <= 0)

m.c193 = Constraint(expr=   9*m.b153 + m.x193 <= 0)

m.c194 = Constraint(expr=   7*m.b154 + m.x194 <= 0)

m.c195 = Constraint(expr=   2*m.b155 + m.x195 <= 0)

m.c196 = Constraint(expr=   3*m.b156 + m.x196 <= 0)

m.c197 = Constraint(expr=   m.b157 + m.x197 <= 0)

m.c198 = Constraint(expr=   2*m.b158 + m.x198 <= 0)

m.c199 = Constraint(expr=   6*m.b159 + m.x199 <= 0)

m.c200 = Constraint(expr=   4*m.b160 + m.x200 <= 0)

m.c201 = Constraint(expr=   8*m.b161 + m.x201 <= 0)

m.c202 = Constraint(expr=   2*m.b162 + m.x202 <= 0)

m.c203 = Constraint(expr=   5*m.b163 + m.x203 <= 0)

m.c204 = Constraint(expr=   3*m.b164 + m.x204 <= 0)

m.c205 = Constraint(expr=   4*m.b165 + m.x205 <= 0)

m.c206 = Constraint(expr=   5*m.b166 + m.x206 <= 0)

m.c207 = Constraint(expr=   7*m.b167 + m.x207 <= 0)

m.c208 = Constraint(expr=   2*m.b168 + m.x208 <= 0)

m.c209 = Constraint(expr=   8*m.b169 + m.x209 <= 0)

m.c210 = Constraint(expr=   m.b170 + m.x210 <= 0)

m.c211 = Constraint(expr=   4*m.b171 + m.x211 <= 0)

m.c212 = Constraint(expr=   5*m.b132 + m.x172 >= 0)

m.c213 = Constraint(expr=   4*m.b133 + m.x173 >= 0)

m.c214 = Constraint(expr=   8*m.b134 + m.x174 >= 0)

m.c215 = Constraint(expr=   7*m.b135 + m.x175 >= 0)

m.c216 = Constraint(expr=   6*m.b136 + m.x176 >= 0)

m.c217 = Constraint(expr=   9*m.b137 + m.x177 >= 0)

m.c218 = Constraint(expr=   10*m.b138 + m.x178 >= 0)

m.c219 = Constraint(expr=   9*m.b139 + m.x179 >= 0)

m.c220 = Constraint(expr=   6*m.b140 + m.x180 >= 0)

m.c221 = Constraint(expr=   10*m.b141 + m.x181 >= 0)

m.c222 = Constraint(expr=   7*m.b142 + m.x182 >= 0)

m.c223 = Constraint(expr=   7*m.b143 + m.x183 >= 0)

m.c224 = Constraint(expr=   4*m.b144 + m.x184 >= 0)

m.c225 = Constraint(expr=   3*m.b145 + m.x185 >= 0)

m.c226 = Constraint(expr=   5*m.b146 + m.x186 >= 0)

m.c227 = Constraint(expr=   6*m.b147 + m.x187 >= 0)

m.c228 = Constraint(expr=   2*m.b148 + m.x188 >= 0)

m.c229 = Constraint(expr=   5*m.b149 + m.x189 >= 0)

m.c230 = Constraint(expr=   4*m.b150 + m.x190 >= 0)

m.c231 = Constraint(expr=   7*m.b151 + m.x191 >= 0)

m.c232 = Constraint(expr=   3*m.b152 + m.x192 >= 0)

m.c233 = Constraint(expr=   9*m.b153 + m.x193 >= 0)

m.c234 = Constraint(expr=   7*m.b154 + m.x194 >= 0)

m.c235 = Constraint(expr=   2*m.b155 + m.x195 >= 0)

m.c236 = Constraint(expr=   3*m.b156 + m.x196 >= 0)

m.c237 = Constraint(expr=   m.b157 + m.x197 >= 0)

m.c238 = Constraint(expr=   2*m.b158 + m.x198 >= 0)

m.c239 = Constraint(expr=   6*m.b159 + m.x199 >= 0)

m.c240 = Constraint(expr=   4*m.b160 + m.x200 >= 0)

m.c241 = Constraint(expr=   8*m.b161 + m.x201 >= 0)

m.c242 = Constraint(expr=   2*m.b162 + m.x202 >= 0)

m.c243 = Constraint(expr=   5*m.b163 + m.x203 >= 0)

m.c244 = Constraint(expr=   3*m.b164 + m.x204 >= 0)

m.c245 = Constraint(expr=   4*m.b165 + m.x205 >= 0)

m.c246 = Constraint(expr=   5*m.b166 + m.x206 >= 0)

m.c247 = Constraint(expr=   7*m.b167 + m.x207 >= 0)

m.c248 = Constraint(expr=   2*m.b168 + m.x208 >= 0)

m.c249 = Constraint(expr=   8*m.b169 + m.x209 >= 0)

m.c250 = Constraint(expr=   m.b170 + m.x210 >= 0)

m.c251 = Constraint(expr=   4*m.b171 + m.x211 >= 0)

m.c252 = Constraint(expr=   m.b92 - m.b93 <= 0)

m.c253 = Constraint(expr=   m.b94 - m.b95 <= 0)

m.c254 = Constraint(expr=   m.b96 - m.b97 <= 0)

m.c255 = Constraint(expr=   m.b98 - m.b99 <= 0)

m.c256 = Constraint(expr=   m.b100 - m.b101 <= 0)

m.c257 = Constraint(expr=   m.b102 - m.b103 <= 0)

m.c258 = Constraint(expr=   m.b104 - m.b105 <= 0)

m.c259 = Constraint(expr=   m.b106 - m.b107 <= 0)

m.c260 = Constraint(expr=   m.b108 - m.b109 <= 0)

m.c261 = Constraint(expr=   m.b110 - m.b111 <= 0)

m.c262 = Constraint(expr=   m.b112 - m.b113 <= 0)

m.c263 = Constraint(expr=   m.b114 - m.b115 <= 0)

m.c264 = Constraint(expr=   m.b116 - m.b117 <= 0)

m.c265 = Constraint(expr=   m.b118 - m.b119 <= 0)

m.c266 = Constraint(expr=   m.b120 - m.b121 <= 0)

m.c267 = Constraint(expr=   m.b122 - m.b123 <= 0)

m.c268 = Constraint(expr=   m.b124 - m.b125 <= 0)

m.c269 = Constraint(expr=   m.b126 - m.b127 <= 0)

m.c270 = Constraint(expr=   m.b128 - m.b129 <= 0)

m.c271 = Constraint(expr=   m.b130 - m.b131 <= 0)

m.c272 = Constraint(expr=   m.b132 + m.b133 <= 1)

m.c273 = Constraint(expr=   m.b132 + m.b133 <= 1)

m.c274 = Constraint(expr=   m.b134 + m.b135 <= 1)

m.c275 = Constraint(expr=   m.b134 + m.b135 <= 1)

m.c276 = Constraint(expr=   m.b136 + m.b137 <= 1)

m.c277 = Constraint(expr=   m.b136 + m.b137 <= 1)

m.c278 = Constraint(expr=   m.b138 + m.b139 <= 1)

m.c279 = Constraint(expr=   m.b138 + m.b139 <= 1)

m.c280 = Constraint(expr=   m.b140 + m.b141 <= 1)

m.c281 = Constraint(expr=   m.b140 + m.b141 <= 1)

m.c282 = Constraint(expr=   m.b142 + m.b143 <= 1)

m.c283 = Constraint(expr=   m.b142 + m.b143 <= 1)

m.c284 = Constraint(expr=   m.b144 + m.b145 <= 1)

m.c285 = Constraint(expr=   m.b144 + m.b145 <= 1)

m.c286 = Constraint(expr=   m.b146 + m.b147 <= 1)

m.c287 = Constraint(expr=   m.b146 + m.b147 <= 1)

m.c288 = Constraint(expr=   m.b148 + m.b149 <= 1)

m.c289 = Constraint(expr=   m.b148 + m.b149 <= 1)

m.c290 = Constraint(expr=   m.b150 + m.b151 <= 1)

m.c291 = Constraint(expr=   m.b150 + m.b151 <= 1)

m.c292 = Constraint(expr=   m.b152 + m.b153 <= 1)

m.c293 = Constraint(expr=   m.b152 + m.b153 <= 1)

m.c294 = Constraint(expr=   m.b154 + m.b155 <= 1)

m.c295 = Constraint(expr=   m.b154 + m.b155 <= 1)

m.c296 = Constraint(expr=   m.b156 + m.b157 <= 1)

m.c297 = Constraint(expr=   m.b156 + m.b157 <= 1)

m.c298 = Constraint(expr=   m.b158 + m.b159 <= 1)

m.c299 = Constraint(expr=   m.b158 + m.b159 <= 1)

m.c300 = Constraint(expr=   m.b160 + m.b161 <= 1)

m.c301 = Constraint(expr=   m.b160 + m.b161 <= 1)

m.c302 = Constraint(expr=   m.b162 + m.b163 <= 1)

m.c303 = Constraint(expr=   m.b162 + m.b163 <= 1)

m.c304 = Constraint(expr=   m.b164 + m.b165 <= 1)

m.c305 = Constraint(expr=   m.b164 + m.b165 <= 1)

m.c306 = Constraint(expr=   m.b166 + m.b167 <= 1)

m.c307 = Constraint(expr=   m.b166 + m.b167 <= 1)

m.c308 = Constraint(expr=   m.b168 + m.b169 <= 1)

m.c309 = Constraint(expr=   m.b168 + m.b169 <= 1)

m.c310 = Constraint(expr=   m.b170 + m.b171 <= 1)

m.c311 = Constraint(expr=   m.b170 + m.b171 <= 1)

m.c312 = Constraint(expr=   m.b92 - m.b132 <= 0)

m.c313 = Constraint(expr= - m.b92 + m.b93 - m.b133 <= 0)

m.c314 = Constraint(expr=   m.b94 - m.b134 <= 0)

m.c315 = Constraint(expr= - m.b94 + m.b95 - m.b135 <= 0)

m.c316 = Constraint(expr=   m.b96 - m.b136 <= 0)

m.c317 = Constraint(expr= - m.b96 + m.b97 - m.b137 <= 0)

m.c318 = Constraint(expr=   m.b98 - m.b138 <= 0)

m.c319 = Constraint(expr= - m.b98 + m.b99 - m.b139 <= 0)

m.c320 = Constraint(expr=   m.b100 - m.b140 <= 0)

m.c321 = Constraint(expr= - m.b100 + m.b101 - m.b141 <= 0)

m.c322 = Constraint(expr=   m.b102 - m.b142 <= 0)

m.c323 = Constraint(expr= - m.b102 + m.b103 - m.b143 <= 0)

m.c324 = Constraint(expr=   m.b104 - m.b144 <= 0)

m.c325 = Constraint(expr= - m.b104 + m.b105 - m.b145 <= 0)

m.c326 = Constraint(expr=   m.b106 - m.b146 <= 0)

m.c327 = Constraint(expr= - m.b106 + m.b107 - m.b147 <= 0)

m.c328 = Constraint(expr=   m.b108 - m.b148 <= 0)

m.c329 = Constraint(expr= - m.b108 + m.b109 - m.b149 <= 0)

m.c330 = Constraint(expr=   m.b110 - m.b150 <= 0)

m.c331 = Constraint(expr= - m.b110 + m.b111 - m.b151 <= 0)

m.c332 = Constraint(expr=   m.b112 - m.b152 <= 0)

m.c333 = Constraint(expr= - m.b112 + m.b113 - m.b153 <= 0)

m.c334 = Constraint(expr=   m.b114 - m.b154 <= 0)

m.c335 = Constraint(expr= - m.b114 + m.b115 - m.b155 <= 0)

m.c336 = Constraint(expr=   m.b116 - m.b156 <= 0)

m.c337 = Constraint(expr= - m.b116 + m.b117 - m.b157 <= 0)

m.c338 = Constraint(expr=   m.b118 - m.b158 <= 0)

m.c339 = Constraint(expr= - m.b118 + m.b119 - m.b159 <= 0)

m.c340 = Constraint(expr=   m.b120 - m.b160 <= 0)

m.c341 = Constraint(expr= - m.b120 + m.b121 - m.b161 <= 0)

m.c342 = Constraint(expr=   m.b122 - m.b162 <= 0)

m.c343 = Constraint(expr= - m.b122 + m.b123 - m.b163 <= 0)

m.c344 = Constraint(expr=   m.b124 - m.b164 <= 0)

m.c345 = Constraint(expr= - m.b124 + m.b125 - m.b165 <= 0)

m.c346 = Constraint(expr=   m.b126 - m.b166 <= 0)

m.c347 = Constraint(expr= - m.b126 + m.b127 - m.b167 <= 0)

m.c348 = Constraint(expr=   m.b128 - m.b168 <= 0)

m.c349 = Constraint(expr= - m.b128 + m.b129 - m.b169 <= 0)

m.c350 = Constraint(expr=   m.b130 - m.b170 <= 0)

m.c351 = Constraint(expr= - m.b130 + m.b131 - m.b171 <= 0)

m.c352 = Constraint(expr=   m.b92 + m.b94 == 1)

m.c353 = Constraint(expr=   m.b93 + m.b95 == 1)

m.c354 = Constraint(expr= - m.b96 + m.b102 + m.b104 >= 0)

m.c355 = Constraint(expr= - m.b97 + m.b103 + m.b105 >= 0)

m.c356 = Constraint(expr= - m.b102 + m.b114 >= 0)

m.c357 = Constraint(expr= - m.b103 + m.b115 >= 0)

m.c358 = Constraint(expr= - m.b104 + m.b116 >= 0)

m.c359 = Constraint(expr= - m.b105 + m.b117 >= 0)

m.c360 = Constraint(expr= - m.b98 + m.b106 >= 0)

m.c361 = Constraint(expr= - m.b99 + m.b107 >= 0)

m.c362 = Constraint(expr= - m.b106 + m.b118 + m.b120 >= 0)

m.c363 = Constraint(expr= - m.b107 + m.b119 + m.b121 >= 0)

m.c364 = Constraint(expr= - m.b100 + m.b108 + m.b110 + m.b112 >= 0)

m.c365 = Constraint(expr= - m.b101 + m.b109 + m.b111 + m.b113 >= 0)

m.c366 = Constraint(expr= - m.b108 + m.b120 >= 0)

m.c367 = Constraint(expr= - m.b109 + m.b121 >= 0)

m.c368 = Constraint(expr= - m.b110 + m.b122 + m.b124 >= 0)

m.c369 = Constraint(expr= - m.b111 + m.b123 + m.b125 >= 0)

m.c370 = Constraint(expr= - m.b112 + m.b126 + m.b128 + m.b130 >= 0)

m.c371 = Constraint(expr= - m.b113 + m.b127 + m.b129 + m.b131 >= 0)

m.c372 = Constraint(expr=   m.b92 + m.b94 - m.b96 >= 0)

m.c373 = Constraint(expr=   m.b93 + m.b95 - m.b97 >= 0)

m.c374 = Constraint(expr=   m.b92 + m.b94 - m.b98 >= 0)

m.c375 = Constraint(expr=   m.b93 + m.b95 - m.b99 >= 0)

m.c376 = Constraint(expr=   m.b92 + m.b94 - m.b100 >= 0)

m.c377 = Constraint(expr=   m.b93 + m.b95 - m.b101 >= 0)

m.c378 = Constraint(expr=   m.b96 - m.b102 >= 0)

m.c379 = Constraint(expr=   m.b97 - m.b103 >= 0)

m.c380 = Constraint(expr=   m.b96 - m.b104 >= 0)

m.c381 = Constraint(expr=   m.b97 - m.b105 >= 0)

m.c382 = Constraint(expr=   m.b98 - m.b106 >= 0)

m.c383 = Constraint(expr=   m.b99 - m.b107 >= 0)

m.c384 = Constraint(expr=   m.b100 - m.b108 >= 0)

m.c385 = Constraint(expr=   m.b101 - m.b109 >= 0)

m.c386 = Constraint(expr=   m.b100 - m.b110 >= 0)

m.c387 = Constraint(expr=   m.b101 - m.b111 >= 0)

m.c388 = Constraint(expr=   m.b100 - m.b112 >= 0)

m.c389 = Constraint(expr=   m.b101 - m.b113 >= 0)

m.c390 = Constraint(expr=   m.b102 - m.b114 >= 0)

m.c391 = Constraint(expr=   m.b103 - m.b115 >= 0)

m.c392 = Constraint(expr=   m.b104 - m.b116 >= 0)

m.c393 = Constraint(expr=   m.b105 - m.b117 >= 0)

m.c394 = Constraint(expr=   m.b106 - m.b118 >= 0)

m.c395 = Constraint(expr=   m.b107 - m.b119 >= 0)

m.c396 = Constraint(expr=   m.b106 - m.b120 >= 0)

m.c397 = Constraint(expr=   m.b107 - m.b121 >= 0)

m.c398 = Constraint(expr=   m.b110 - m.b122 >= 0)

m.c399 = Constraint(expr=   m.b111 - m.b123 >= 0)

m.c400 = Constraint(expr=   m.b110 - m.b124 >= 0)

m.c401 = Constraint(expr=   m.b111 - m.b125 >= 0)

m.c402 = Constraint(expr=   m.b112 - m.b126 >= 0)

m.c403 = Constraint(expr=   m.b113 - m.b127 >= 0)

m.c404 = Constraint(expr=   m.b112 - m.b128 >= 0)

m.c405 = Constraint(expr=   m.b113 - m.b129 >= 0)

m.c406 = Constraint(expr=   m.b112 - m.b130 >= 0)

m.c407 = Constraint(expr=   m.b113 - m.b131 >= 0)

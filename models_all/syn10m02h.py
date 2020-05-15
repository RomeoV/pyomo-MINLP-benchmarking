#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        295      129       20      146        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        195      155       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        673      637       36        0
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
m.x44 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,30),initialize=0)
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

m.obj = Objective(expr= - m.x22 - m.x23 + 5*m.x34 + 10*m.x35 - 2*m.x44 - m.x45 + 80*m.x60 + 90*m.x61 + 285*m.x62
                        + 390*m.x63 + 290*m.x64 + 405*m.x65 + 280*m.x66 + 400*m.x67 + 290*m.x68 + 300*m.x69 + 350*m.x70
                        + 250*m.x71 - 5*m.b176 - 4*m.b177 - 8*m.b178 - 7*m.b179 - 6*m.b180 - 9*m.b181 - 10*m.b182
                        - 9*m.b183 - 6*m.b184 - 10*m.b185 - 7*m.b186 - 7*m.b187 - 4*m.b188 - 3*m.b189 - 5*m.b190
                        - 6*m.b191 - 2*m.b192 - 5*m.b193 - 4*m.b194 - 7*m.b195, sense=maximize)

m.c2 = Constraint(expr=   m.x22 - m.x24 - m.x26 == 0)

m.c3 = Constraint(expr=   m.x23 - m.x25 - m.x27 == 0)

m.c4 = Constraint(expr= - m.x28 - m.x30 + m.x32 == 0)

m.c5 = Constraint(expr= - m.x29 - m.x31 + m.x33 == 0)

m.c6 = Constraint(expr=   m.x32 - m.x34 - m.x36 == 0)

m.c7 = Constraint(expr=   m.x33 - m.x35 - m.x37 == 0)

m.c8 = Constraint(expr=   m.x36 - m.x38 - m.x40 - m.x42 == 0)

m.c9 = Constraint(expr=   m.x37 - m.x39 - m.x41 - m.x43 == 0)

m.c10 = Constraint(expr=   m.x46 - m.x52 - m.x54 == 0)

m.c11 = Constraint(expr=   m.x47 - m.x53 - m.x55 == 0)

m.c12 = Constraint(expr=   m.x50 - m.x56 - m.x58 - m.x60 == 0)

m.c13 = Constraint(expr=   m.x51 - m.x57 - m.x59 - m.x61 == 0)

m.c14 = Constraint(expr=(m.x80/(1e-6 + m.b156) - log(1 + m.x72/(1e-6 + m.b156)))*(1e-6 + m.b156) <= 0)

m.c15 = Constraint(expr=(m.x81/(1e-6 + m.b157) - log(1 + m.x73/(1e-6 + m.b157)))*(1e-6 + m.b157) <= 0)

m.c16 = Constraint(expr=   m.x74 == 0)

m.c17 = Constraint(expr=   m.x75 == 0)

m.c18 = Constraint(expr=   m.x82 == 0)

m.c19 = Constraint(expr=   m.x83 == 0)

m.c20 = Constraint(expr=   m.x24 - m.x72 - m.x74 == 0)

m.c21 = Constraint(expr=   m.x25 - m.x73 - m.x75 == 0)

m.c22 = Constraint(expr=   m.x28 - m.x80 - m.x82 == 0)

m.c23 = Constraint(expr=   m.x29 - m.x81 - m.x83 == 0)

m.c24 = Constraint(expr=   m.x72 - 40*m.b156 <= 0)

m.c25 = Constraint(expr=   m.x73 - 40*m.b157 <= 0)

m.c26 = Constraint(expr=   m.x74 + 40*m.b156 <= 40)

m.c27 = Constraint(expr=   m.x75 + 40*m.b157 <= 40)

m.c28 = Constraint(expr=   m.x80 - 3.71357206670431*m.b156 <= 0)

m.c29 = Constraint(expr=   m.x81 - 3.71357206670431*m.b157 <= 0)

m.c30 = Constraint(expr=   m.x82 + 3.71357206670431*m.b156 <= 3.71357206670431)

m.c31 = Constraint(expr=   m.x83 + 3.71357206670431*m.b157 <= 3.71357206670431)

m.c32 = Constraint(expr=(m.x84/(1e-6 + m.b158) - 1.2*log(1 + m.x76/(1e-6 + m.b158)))*(1e-6 + m.b158) <= 0)

m.c33 = Constraint(expr=(m.x85/(1e-6 + m.b159) - 1.2*log(1 + m.x77/(1e-6 + m.b159)))*(1e-6 + m.b159) <= 0)

m.c34 = Constraint(expr=   m.x78 == 0)

m.c35 = Constraint(expr=   m.x79 == 0)

m.c36 = Constraint(expr=   m.x86 == 0)

m.c37 = Constraint(expr=   m.x87 == 0)

m.c38 = Constraint(expr=   m.x26 - m.x76 - m.x78 == 0)

m.c39 = Constraint(expr=   m.x27 - m.x77 - m.x79 == 0)

m.c40 = Constraint(expr=   m.x30 - m.x84 - m.x86 == 0)

m.c41 = Constraint(expr=   m.x31 - m.x85 - m.x87 == 0)

m.c42 = Constraint(expr=   m.x76 - 40*m.b158 <= 0)

m.c43 = Constraint(expr=   m.x77 - 40*m.b159 <= 0)

m.c44 = Constraint(expr=   m.x78 + 40*m.b158 <= 40)

m.c45 = Constraint(expr=   m.x79 + 40*m.b159 <= 40)

m.c46 = Constraint(expr=   m.x84 - 4.45628648004517*m.b158 <= 0)

m.c47 = Constraint(expr=   m.x85 - 4.45628648004517*m.b159 <= 0)

m.c48 = Constraint(expr=   m.x86 + 4.45628648004517*m.b158 <= 4.45628648004517)

m.c49 = Constraint(expr=   m.x87 + 4.45628648004517*m.b159 <= 4.45628648004517)

m.c50 = Constraint(expr= - 0.75*m.x88 + m.x104 == 0)

m.c51 = Constraint(expr= - 0.75*m.x89 + m.x105 == 0)

m.c52 = Constraint(expr=   m.x90 == 0)

m.c53 = Constraint(expr=   m.x91 == 0)

m.c54 = Constraint(expr=   m.x106 == 0)

m.c55 = Constraint(expr=   m.x107 == 0)

m.c56 = Constraint(expr=   m.x38 - m.x88 - m.x90 == 0)

m.c57 = Constraint(expr=   m.x39 - m.x89 - m.x91 == 0)

m.c58 = Constraint(expr=   m.x46 - m.x104 - m.x106 == 0)

m.c59 = Constraint(expr=   m.x47 - m.x105 - m.x107 == 0)

m.c60 = Constraint(expr=   m.x88 - 4.45628648004517*m.b160 <= 0)

m.c61 = Constraint(expr=   m.x89 - 4.45628648004517*m.b161 <= 0)

m.c62 = Constraint(expr=   m.x90 + 4.45628648004517*m.b160 <= 4.45628648004517)

m.c63 = Constraint(expr=   m.x91 + 4.45628648004517*m.b161 <= 4.45628648004517)

m.c64 = Constraint(expr=   m.x104 - 3.34221486003388*m.b160 <= 0)

m.c65 = Constraint(expr=   m.x105 - 3.34221486003388*m.b161 <= 0)

m.c66 = Constraint(expr=   m.x106 + 3.34221486003388*m.b160 <= 3.34221486003388)

m.c67 = Constraint(expr=   m.x107 + 3.34221486003388*m.b161 <= 3.34221486003388)

m.c68 = Constraint(expr=(m.x108/(1e-6 + m.b162) - 1.5*log(1 + m.x92/(1e-6 + m.b162)))*(1e-6 + m.b162) <= 0)

m.c69 = Constraint(expr=(m.x109/(1e-6 + m.b163) - 1.5*log(1 + m.x93/(1e-6 + m.b163)))*(1e-6 + m.b163) <= 0)

m.c70 = Constraint(expr=   m.x94 == 0)

m.c71 = Constraint(expr=   m.x95 == 0)

m.c72 = Constraint(expr=   m.x112 == 0)

m.c73 = Constraint(expr=   m.x113 == 0)

m.c74 = Constraint(expr=   m.x40 - m.x92 - m.x94 == 0)

m.c75 = Constraint(expr=   m.x41 - m.x93 - m.x95 == 0)

m.c76 = Constraint(expr=   m.x48 - m.x108 - m.x112 == 0)

m.c77 = Constraint(expr=   m.x49 - m.x109 - m.x113 == 0)

m.c78 = Constraint(expr=   m.x92 - 4.45628648004517*m.b162 <= 0)

m.c79 = Constraint(expr=   m.x93 - 4.45628648004517*m.b163 <= 0)

m.c80 = Constraint(expr=   m.x94 + 4.45628648004517*m.b162 <= 4.45628648004517)

m.c81 = Constraint(expr=   m.x95 + 4.45628648004517*m.b163 <= 4.45628648004517)

m.c82 = Constraint(expr=   m.x108 - 2.54515263975353*m.b162 <= 0)

m.c83 = Constraint(expr=   m.x109 - 2.54515263975353*m.b163 <= 0)

m.c84 = Constraint(expr=   m.x112 + 2.54515263975353*m.b162 <= 2.54515263975353)

m.c85 = Constraint(expr=   m.x113 + 2.54515263975353*m.b163 <= 2.54515263975353)

m.c86 = Constraint(expr= - m.x96 + m.x116 == 0)

m.c87 = Constraint(expr= - m.x97 + m.x117 == 0)

m.c88 = Constraint(expr= - 0.5*m.x100 + m.x116 == 0)

m.c89 = Constraint(expr= - 0.5*m.x101 + m.x117 == 0)

m.c90 = Constraint(expr=   m.x98 == 0)

m.c91 = Constraint(expr=   m.x99 == 0)

m.c92 = Constraint(expr=   m.x102 == 0)

m.c93 = Constraint(expr=   m.x103 == 0)

m.c94 = Constraint(expr=   m.x118 == 0)

m.c95 = Constraint(expr=   m.x119 == 0)

m.c96 = Constraint(expr=   m.x42 - m.x96 - m.x98 == 0)

m.c97 = Constraint(expr=   m.x43 - m.x97 - m.x99 == 0)

m.c98 = Constraint(expr=   m.x44 - m.x100 - m.x102 == 0)

m.c99 = Constraint(expr=   m.x45 - m.x101 - m.x103 == 0)

m.c100 = Constraint(expr=   m.x50 - m.x116 - m.x118 == 0)

m.c101 = Constraint(expr=   m.x51 - m.x117 - m.x119 == 0)

m.c102 = Constraint(expr=   m.x96 - 4.45628648004517*m.b164 <= 0)

m.c103 = Constraint(expr=   m.x97 - 4.45628648004517*m.b165 <= 0)

m.c104 = Constraint(expr=   m.x98 + 4.45628648004517*m.b164 <= 4.45628648004517)

m.c105 = Constraint(expr=   m.x99 + 4.45628648004517*m.b165 <= 4.45628648004517)

m.c106 = Constraint(expr=   m.x100 - 30*m.b164 <= 0)

m.c107 = Constraint(expr=   m.x101 - 30*m.b165 <= 0)

m.c108 = Constraint(expr=   m.x102 + 30*m.b164 <= 30)

m.c109 = Constraint(expr=   m.x103 + 30*m.b165 <= 30)

m.c110 = Constraint(expr=   m.x116 - 15*m.b164 <= 0)

m.c111 = Constraint(expr=   m.x117 - 15*m.b165 <= 0)

m.c112 = Constraint(expr=   m.x118 + 15*m.b164 <= 15)

m.c113 = Constraint(expr=   m.x119 + 15*m.b165 <= 15)

m.c114 = Constraint(expr=(m.x136/(1e-6 + m.b166) - 1.25*log(1 + m.x120/(1e-6 + m.b166)))*(1e-6 + m.b166) <= 0)

m.c115 = Constraint(expr=(m.x137/(1e-6 + m.b167) - 1.25*log(1 + m.x121/(1e-6 + m.b167)))*(1e-6 + m.b167) <= 0)

m.c116 = Constraint(expr=   m.x122 == 0)

m.c117 = Constraint(expr=   m.x123 == 0)

m.c118 = Constraint(expr=   m.x138 == 0)

m.c119 = Constraint(expr=   m.x139 == 0)

m.c120 = Constraint(expr=   m.x52 - m.x120 - m.x122 == 0)

m.c121 = Constraint(expr=   m.x53 - m.x121 - m.x123 == 0)

m.c122 = Constraint(expr=   m.x62 - m.x136 - m.x138 == 0)

m.c123 = Constraint(expr=   m.x63 - m.x137 - m.x139 == 0)

m.c124 = Constraint(expr=   m.x120 - 3.34221486003388*m.b166 <= 0)

m.c125 = Constraint(expr=   m.x121 - 3.34221486003388*m.b167 <= 0)

m.c126 = Constraint(expr=   m.x122 + 3.34221486003388*m.b166 <= 3.34221486003388)

m.c127 = Constraint(expr=   m.x123 + 3.34221486003388*m.b167 <= 3.34221486003388)

m.c128 = Constraint(expr=   m.x136 - 1.83548069293539*m.b166 <= 0)

m.c129 = Constraint(expr=   m.x137 - 1.83548069293539*m.b167 <= 0)

m.c130 = Constraint(expr=   m.x138 + 1.83548069293539*m.b166 <= 1.83548069293539)

m.c131 = Constraint(expr=   m.x139 + 1.83548069293539*m.b167 <= 1.83548069293539)

m.c132 = Constraint(expr=(m.x140/(1e-6 + m.b168) - 0.9*log(1 + m.x124/(1e-6 + m.b168)))*(1e-6 + m.b168) <= 0)

m.c133 = Constraint(expr=(m.x141/(1e-6 + m.b169) - 0.9*log(1 + m.x125/(1e-6 + m.b169)))*(1e-6 + m.b169) <= 0)

m.c134 = Constraint(expr=   m.x126 == 0)

m.c135 = Constraint(expr=   m.x127 == 0)

m.c136 = Constraint(expr=   m.x142 == 0)

m.c137 = Constraint(expr=   m.x143 == 0)

m.c138 = Constraint(expr=   m.x54 - m.x124 - m.x126 == 0)

m.c139 = Constraint(expr=   m.x55 - m.x125 - m.x127 == 0)

m.c140 = Constraint(expr=   m.x64 - m.x140 - m.x142 == 0)

m.c141 = Constraint(expr=   m.x65 - m.x141 - m.x143 == 0)

m.c142 = Constraint(expr=   m.x124 - 3.34221486003388*m.b168 <= 0)

m.c143 = Constraint(expr=   m.x125 - 3.34221486003388*m.b169 <= 0)

m.c144 = Constraint(expr=   m.x126 + 3.34221486003388*m.b168 <= 3.34221486003388)

m.c145 = Constraint(expr=   m.x127 + 3.34221486003388*m.b169 <= 3.34221486003388)

m.c146 = Constraint(expr=   m.x140 - 1.32154609891348*m.b168 <= 0)

m.c147 = Constraint(expr=   m.x141 - 1.32154609891348*m.b169 <= 0)

m.c148 = Constraint(expr=   m.x142 + 1.32154609891348*m.b168 <= 1.32154609891348)

m.c149 = Constraint(expr=   m.x143 + 1.32154609891348*m.b169 <= 1.32154609891348)

m.c150 = Constraint(expr=(m.x144/(1e-6 + m.b170) - log(1 + m.x110/(1e-6 + m.b170)))*(1e-6 + m.b170) <= 0)

m.c151 = Constraint(expr=(m.x145/(1e-6 + m.b171) - log(1 + m.x111/(1e-6 + m.b171)))*(1e-6 + m.b171) <= 0)

m.c152 = Constraint(expr=   m.x114 == 0)

m.c153 = Constraint(expr=   m.x115 == 0)

m.c154 = Constraint(expr=   m.x146 == 0)

m.c155 = Constraint(expr=   m.x147 == 0)

m.c156 = Constraint(expr=   m.x48 - m.x110 - m.x114 == 0)

m.c157 = Constraint(expr=   m.x49 - m.x111 - m.x115 == 0)

m.c158 = Constraint(expr=   m.x66 - m.x144 - m.x146 == 0)

m.c159 = Constraint(expr=   m.x67 - m.x145 - m.x147 == 0)

m.c160 = Constraint(expr=   m.x110 - 2.54515263975353*m.b170 <= 0)

m.c161 = Constraint(expr=   m.x111 - 2.54515263975353*m.b171 <= 0)

m.c162 = Constraint(expr=   m.x114 + 2.54515263975353*m.b170 <= 2.54515263975353)

m.c163 = Constraint(expr=   m.x115 + 2.54515263975353*m.b171 <= 2.54515263975353)

m.c164 = Constraint(expr=   m.x144 - 1.26558121681553*m.b170 <= 0)

m.c165 = Constraint(expr=   m.x145 - 1.26558121681553*m.b171 <= 0)

m.c166 = Constraint(expr=   m.x146 + 1.26558121681553*m.b170 <= 1.26558121681553)

m.c167 = Constraint(expr=   m.x147 + 1.26558121681553*m.b171 <= 1.26558121681553)

m.c168 = Constraint(expr= - 0.9*m.x128 + m.x148 == 0)

m.c169 = Constraint(expr= - 0.9*m.x129 + m.x149 == 0)

m.c170 = Constraint(expr=   m.x130 == 0)

m.c171 = Constraint(expr=   m.x131 == 0)

m.c172 = Constraint(expr=   m.x150 == 0)

m.c173 = Constraint(expr=   m.x151 == 0)

m.c174 = Constraint(expr=   m.x56 - m.x128 - m.x130 == 0)

m.c175 = Constraint(expr=   m.x57 - m.x129 - m.x131 == 0)

m.c176 = Constraint(expr=   m.x68 - m.x148 - m.x150 == 0)

m.c177 = Constraint(expr=   m.x69 - m.x149 - m.x151 == 0)

m.c178 = Constraint(expr=   m.x128 - 15*m.b172 <= 0)

m.c179 = Constraint(expr=   m.x129 - 15*m.b173 <= 0)

m.c180 = Constraint(expr=   m.x130 + 15*m.b172 <= 15)

m.c181 = Constraint(expr=   m.x131 + 15*m.b173 <= 15)

m.c182 = Constraint(expr=   m.x148 - 13.5*m.b172 <= 0)

m.c183 = Constraint(expr=   m.x149 - 13.5*m.b173 <= 0)

m.c184 = Constraint(expr=   m.x150 + 13.5*m.b172 <= 13.5)

m.c185 = Constraint(expr=   m.x151 + 13.5*m.b173 <= 13.5)

m.c186 = Constraint(expr= - 0.6*m.x132 + m.x152 == 0)

m.c187 = Constraint(expr= - 0.6*m.x133 + m.x153 == 0)

m.c188 = Constraint(expr=   m.x134 == 0)

m.c189 = Constraint(expr=   m.x135 == 0)

m.c190 = Constraint(expr=   m.x154 == 0)

m.c191 = Constraint(expr=   m.x155 == 0)

m.c192 = Constraint(expr=   m.x58 - m.x132 - m.x134 == 0)

m.c193 = Constraint(expr=   m.x59 - m.x133 - m.x135 == 0)

m.c194 = Constraint(expr=   m.x70 - m.x152 - m.x154 == 0)

m.c195 = Constraint(expr=   m.x71 - m.x153 - m.x155 == 0)

m.c196 = Constraint(expr=   m.x132 - 15*m.b174 <= 0)

m.c197 = Constraint(expr=   m.x133 - 15*m.b175 <= 0)

m.c198 = Constraint(expr=   m.x134 + 15*m.b174 <= 15)

m.c199 = Constraint(expr=   m.x135 + 15*m.b175 <= 15)

m.c200 = Constraint(expr=   m.x152 - 9*m.b174 <= 0)

m.c201 = Constraint(expr=   m.x153 - 9*m.b175 <= 0)

m.c202 = Constraint(expr=   m.x154 + 9*m.b174 <= 9)

m.c203 = Constraint(expr=   m.x155 + 9*m.b175 <= 9)

m.c204 = Constraint(expr=   m.x2 + 5*m.b176 == 0)

m.c205 = Constraint(expr=   m.x3 + 4*m.b177 == 0)

m.c206 = Constraint(expr=   m.x4 + 8*m.b178 == 0)

m.c207 = Constraint(expr=   m.x5 + 7*m.b179 == 0)

m.c208 = Constraint(expr=   m.x6 + 6*m.b180 == 0)

m.c209 = Constraint(expr=   m.x7 + 9*m.b181 == 0)

m.c210 = Constraint(expr=   m.x8 + 10*m.b182 == 0)

m.c211 = Constraint(expr=   m.x9 + 9*m.b183 == 0)

m.c212 = Constraint(expr=   m.x10 + 6*m.b184 == 0)

m.c213 = Constraint(expr=   m.x11 + 10*m.b185 == 0)

m.c214 = Constraint(expr=   m.x12 + 7*m.b186 == 0)

m.c215 = Constraint(expr=   m.x13 + 7*m.b187 == 0)

m.c216 = Constraint(expr=   m.x14 + 4*m.b188 == 0)

m.c217 = Constraint(expr=   m.x15 + 3*m.b189 == 0)

m.c218 = Constraint(expr=   m.x16 + 5*m.b190 == 0)

m.c219 = Constraint(expr=   m.x17 + 6*m.b191 == 0)

m.c220 = Constraint(expr=   m.x18 + 2*m.b192 == 0)

m.c221 = Constraint(expr=   m.x19 + 5*m.b193 == 0)

m.c222 = Constraint(expr=   m.x20 + 4*m.b194 == 0)

m.c223 = Constraint(expr=   m.x21 + 7*m.b195 == 0)

m.c224 = Constraint(expr=   m.b156 - m.b157 <= 0)

m.c225 = Constraint(expr=   m.b158 - m.b159 <= 0)

m.c226 = Constraint(expr=   m.b160 - m.b161 <= 0)

m.c227 = Constraint(expr=   m.b162 - m.b163 <= 0)

m.c228 = Constraint(expr=   m.b164 - m.b165 <= 0)

m.c229 = Constraint(expr=   m.b166 - m.b167 <= 0)

m.c230 = Constraint(expr=   m.b168 - m.b169 <= 0)

m.c231 = Constraint(expr=   m.b170 - m.b171 <= 0)

m.c232 = Constraint(expr=   m.b172 - m.b173 <= 0)

m.c233 = Constraint(expr=   m.b174 - m.b175 <= 0)

m.c234 = Constraint(expr=   m.b176 + m.b177 <= 1)

m.c235 = Constraint(expr=   m.b176 + m.b177 <= 1)

m.c236 = Constraint(expr=   m.b178 + m.b179 <= 1)

m.c237 = Constraint(expr=   m.b178 + m.b179 <= 1)

m.c238 = Constraint(expr=   m.b180 + m.b181 <= 1)

m.c239 = Constraint(expr=   m.b180 + m.b181 <= 1)

m.c240 = Constraint(expr=   m.b182 + m.b183 <= 1)

m.c241 = Constraint(expr=   m.b182 + m.b183 <= 1)

m.c242 = Constraint(expr=   m.b184 + m.b185 <= 1)

m.c243 = Constraint(expr=   m.b184 + m.b185 <= 1)

m.c244 = Constraint(expr=   m.b186 + m.b187 <= 1)

m.c245 = Constraint(expr=   m.b186 + m.b187 <= 1)

m.c246 = Constraint(expr=   m.b188 + m.b189 <= 1)

m.c247 = Constraint(expr=   m.b188 + m.b189 <= 1)

m.c248 = Constraint(expr=   m.b190 + m.b191 <= 1)

m.c249 = Constraint(expr=   m.b190 + m.b191 <= 1)

m.c250 = Constraint(expr=   m.b192 + m.b193 <= 1)

m.c251 = Constraint(expr=   m.b192 + m.b193 <= 1)

m.c252 = Constraint(expr=   m.b194 + m.b195 <= 1)

m.c253 = Constraint(expr=   m.b194 + m.b195 <= 1)

m.c254 = Constraint(expr=   m.b156 - m.b176 <= 0)

m.c255 = Constraint(expr= - m.b156 + m.b157 - m.b177 <= 0)

m.c256 = Constraint(expr=   m.b158 - m.b178 <= 0)

m.c257 = Constraint(expr= - m.b158 + m.b159 - m.b179 <= 0)

m.c258 = Constraint(expr=   m.b160 - m.b180 <= 0)

m.c259 = Constraint(expr= - m.b160 + m.b161 - m.b181 <= 0)

m.c260 = Constraint(expr=   m.b162 - m.b182 <= 0)

m.c261 = Constraint(expr= - m.b162 + m.b163 - m.b183 <= 0)

m.c262 = Constraint(expr=   m.b164 - m.b184 <= 0)

m.c263 = Constraint(expr= - m.b164 + m.b165 - m.b185 <= 0)

m.c264 = Constraint(expr=   m.b166 - m.b186 <= 0)

m.c265 = Constraint(expr= - m.b166 + m.b167 - m.b187 <= 0)

m.c266 = Constraint(expr=   m.b168 - m.b188 <= 0)

m.c267 = Constraint(expr= - m.b168 + m.b169 - m.b189 <= 0)

m.c268 = Constraint(expr=   m.b170 - m.b190 <= 0)

m.c269 = Constraint(expr= - m.b170 + m.b171 - m.b191 <= 0)

m.c270 = Constraint(expr=   m.b172 - m.b192 <= 0)

m.c271 = Constraint(expr= - m.b172 + m.b173 - m.b193 <= 0)

m.c272 = Constraint(expr=   m.b174 - m.b194 <= 0)

m.c273 = Constraint(expr= - m.b174 + m.b175 - m.b195 <= 0)

m.c274 = Constraint(expr=   m.b156 + m.b158 == 1)

m.c275 = Constraint(expr=   m.b157 + m.b159 == 1)

m.c276 = Constraint(expr= - m.b160 + m.b166 + m.b168 >= 0)

m.c277 = Constraint(expr= - m.b161 + m.b167 + m.b169 >= 0)

m.c278 = Constraint(expr= - m.b162 + m.b170 >= 0)

m.c279 = Constraint(expr= - m.b163 + m.b171 >= 0)

m.c280 = Constraint(expr=   m.b156 + m.b158 - m.b160 >= 0)

m.c281 = Constraint(expr=   m.b157 + m.b159 - m.b161 >= 0)

m.c282 = Constraint(expr=   m.b156 + m.b158 - m.b162 >= 0)

m.c283 = Constraint(expr=   m.b157 + m.b159 - m.b163 >= 0)

m.c284 = Constraint(expr=   m.b156 + m.b158 - m.b164 >= 0)

m.c285 = Constraint(expr=   m.b157 + m.b159 - m.b165 >= 0)

m.c286 = Constraint(expr=   m.b160 - m.b166 >= 0)

m.c287 = Constraint(expr=   m.b161 - m.b167 >= 0)

m.c288 = Constraint(expr=   m.b160 - m.b168 >= 0)

m.c289 = Constraint(expr=   m.b161 - m.b169 >= 0)

m.c290 = Constraint(expr=   m.b162 - m.b170 >= 0)

m.c291 = Constraint(expr=   m.b163 - m.b171 >= 0)

m.c292 = Constraint(expr=   m.b164 - m.b172 >= 0)

m.c293 = Constraint(expr=   m.b165 - m.b173 >= 0)

m.c294 = Constraint(expr=   m.b164 - m.b174 >= 0)

m.c295 = Constraint(expr=   m.b165 - m.b175 >= 0)

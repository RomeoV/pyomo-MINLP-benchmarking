#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        182       85       20       77        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        122      107       15        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        416      383       33        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
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
m.x13 = Var(within=Reals,bounds=(0,7),initialize=0)
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
m.x30 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,5),initialize=0)
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

m.obj = Objective(expr=   5*m.x8 + 500*m.x26 + 350*m.x27 + 200*m.x38 + 250*m.x39 + 200*m.x40 + 200*m.x41 - 5*m.b108
                        - 8*m.b109 - 6*m.b110 - 10*m.b111 - 6*m.b112 - 7*m.b113 - 4*m.b114 - 5*m.b115 - 2*m.b116
                        - 4*m.b117 - 3*m.b118 - 7*m.b119 - 3*m.b120 - 2*m.b121 - 4*m.b122, sense=maximize)

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

m.c12 = Constraint(expr=(m.x46/(1e-6 + m.b108) - log(1 + m.x42/(1e-6 + m.b108)))*(1e-6 + m.b108) <= 0)

m.c13 = Constraint(expr=   m.x43 == 0)

m.c14 = Constraint(expr=   m.x47 == 0)

m.c15 = Constraint(expr=   m.x3 - m.x42 - m.x43 == 0)

m.c16 = Constraint(expr=   m.x5 - m.x46 - m.x47 == 0)

m.c17 = Constraint(expr=   m.x42 - 10*m.b108 <= 0)

m.c18 = Constraint(expr=   m.x43 + 10*m.b108 <= 10)

m.c19 = Constraint(expr=   m.x46 - 2.39789527279837*m.b108 <= 0)

m.c20 = Constraint(expr=   m.x47 + 2.39789527279837*m.b108 <= 2.39789527279837)

m.c21 = Constraint(expr=(m.x48/(1e-6 + m.b109) - 1.2*log(1 + m.x44/(1e-6 + m.b109)))*(1e-6 + m.b109) <= 0)

m.c22 = Constraint(expr=   m.x45 == 0)

m.c23 = Constraint(expr=   m.x49 == 0)

m.c24 = Constraint(expr=   m.x4 - m.x44 - m.x45 == 0)

m.c25 = Constraint(expr=   m.x6 - m.x48 - m.x49 == 0)

m.c26 = Constraint(expr=   m.x44 - 10*m.b109 <= 0)

m.c27 = Constraint(expr=   m.x45 + 10*m.b109 <= 10)

m.c28 = Constraint(expr=   m.x48 - 2.87747432735804*m.b109 <= 0)

m.c29 = Constraint(expr=   m.x49 + 2.87747432735804*m.b109 <= 2.87747432735804)

m.c30 = Constraint(expr= - 0.75*m.x50 + m.x58 == 0)

m.c31 = Constraint(expr=   m.x51 == 0)

m.c32 = Constraint(expr=   m.x59 == 0)

m.c33 = Constraint(expr=   m.x10 - m.x50 - m.x51 == 0)

m.c34 = Constraint(expr=   m.x14 - m.x58 - m.x59 == 0)

m.c35 = Constraint(expr=   m.x50 - 2.87747432735804*m.b110 <= 0)

m.c36 = Constraint(expr=   m.x51 + 2.87747432735804*m.b110 <= 2.87747432735804)

m.c37 = Constraint(expr=   m.x58 - 2.15810574551853*m.b110 <= 0)

m.c38 = Constraint(expr=   m.x59 + 2.15810574551853*m.b110 <= 2.15810574551853)

m.c39 = Constraint(expr=(m.x60/(1e-6 + m.b111) - 1.5*log(1 + m.x52/(1e-6 + m.b111)))*(1e-6 + m.b111) <= 0)

m.c40 = Constraint(expr=   m.x53 == 0)

m.c41 = Constraint(expr=   m.x62 == 0)

m.c42 = Constraint(expr=   m.x11 - m.x52 - m.x53 == 0)

m.c43 = Constraint(expr=   m.x15 - m.x60 - m.x62 == 0)

m.c44 = Constraint(expr=   m.x52 - 2.87747432735804*m.b111 <= 0)

m.c45 = Constraint(expr=   m.x53 + 2.87747432735804*m.b111 <= 2.87747432735804)

m.c46 = Constraint(expr=   m.x60 - 2.03277599268042*m.b111 <= 0)

m.c47 = Constraint(expr=   m.x62 + 2.03277599268042*m.b111 <= 2.03277599268042)

m.c48 = Constraint(expr= - m.x54 + m.x64 == 0)

m.c49 = Constraint(expr= - 0.5*m.x56 + m.x64 == 0)

m.c50 = Constraint(expr=   m.x55 == 0)

m.c51 = Constraint(expr=   m.x57 == 0)

m.c52 = Constraint(expr=   m.x65 == 0)

m.c53 = Constraint(expr=   m.x12 - m.x54 - m.x55 == 0)

m.c54 = Constraint(expr=   m.x13 - m.x56 - m.x57 == 0)

m.c55 = Constraint(expr=   m.x16 - m.x64 - m.x65 == 0)

m.c56 = Constraint(expr=   m.x54 - 2.87747432735804*m.b112 <= 0)

m.c57 = Constraint(expr=   m.x55 + 2.87747432735804*m.b112 <= 2.87747432735804)

m.c58 = Constraint(expr=   m.x56 - 7*m.b112 <= 0)

m.c59 = Constraint(expr=   m.x57 + 7*m.b112 <= 7)

m.c60 = Constraint(expr=   m.x64 - 3.5*m.b112 <= 0)

m.c61 = Constraint(expr=   m.x65 + 3.5*m.b112 <= 3.5)

m.c62 = Constraint(expr=(m.x76/(1e-6 + m.b113) - 1.25*log(1 + m.x66/(1e-6 + m.b113)))*(1e-6 + m.b113) <= 0)

m.c63 = Constraint(expr=   m.x67 == 0)

m.c64 = Constraint(expr=   m.x78 == 0)

m.c65 = Constraint(expr=   m.x17 - m.x66 - m.x67 == 0)

m.c66 = Constraint(expr=   m.x22 - m.x76 - m.x78 == 0)

m.c67 = Constraint(expr=   m.x66 - 2.15810574551853*m.b113 <= 0)

m.c68 = Constraint(expr=   m.x67 + 2.15810574551853*m.b113 <= 2.15810574551853)

m.c69 = Constraint(expr=   m.x76 - 1.43746550029693*m.b113 <= 0)

m.c70 = Constraint(expr=   m.x78 + 1.43746550029693*m.b113 <= 1.43746550029693)

m.c71 = Constraint(expr=(m.x80/(1e-6 + m.b114) - 0.9*log(1 + m.x68/(1e-6 + m.b114)))*(1e-6 + m.b114) <= 0)

m.c72 = Constraint(expr=   m.x69 == 0)

m.c73 = Constraint(expr=   m.x82 == 0)

m.c74 = Constraint(expr=   m.x18 - m.x68 - m.x69 == 0)

m.c75 = Constraint(expr=   m.x23 - m.x80 - m.x82 == 0)

m.c76 = Constraint(expr=   m.x68 - 2.15810574551853*m.b114 <= 0)

m.c77 = Constraint(expr=   m.x69 + 2.15810574551853*m.b114 <= 2.15810574551853)

m.c78 = Constraint(expr=   m.x80 - 1.03497516021379*m.b114 <= 0)

m.c79 = Constraint(expr=   m.x82 + 1.03497516021379*m.b114 <= 1.03497516021379)

m.c80 = Constraint(expr=(m.x84/(1e-6 + m.b115) - log(1 + m.x61/(1e-6 + m.b115)))*(1e-6 + m.b115) <= 0)

m.c81 = Constraint(expr=   m.x63 == 0)

m.c82 = Constraint(expr=   m.x85 == 0)

m.c83 = Constraint(expr=   m.x15 - m.x61 - m.x63 == 0)

m.c84 = Constraint(expr=   m.x24 - m.x84 - m.x85 == 0)

m.c85 = Constraint(expr=   m.x61 - 2.03277599268042*m.b115 <= 0)

m.c86 = Constraint(expr=   m.x63 + 2.03277599268042*m.b115 <= 2.03277599268042)

m.c87 = Constraint(expr=   m.x84 - 1.10947836929589*m.b115 <= 0)

m.c88 = Constraint(expr=   m.x85 + 1.10947836929589*m.b115 <= 1.10947836929589)

m.c89 = Constraint(expr= - 0.9*m.x70 + m.x86 == 0)

m.c90 = Constraint(expr=   m.x71 == 0)

m.c91 = Constraint(expr=   m.x87 == 0)

m.c92 = Constraint(expr=   m.x19 - m.x70 - m.x71 == 0)

m.c93 = Constraint(expr=   m.x25 - m.x86 - m.x87 == 0)

m.c94 = Constraint(expr=   m.x70 - 3.5*m.b116 <= 0)

m.c95 = Constraint(expr=   m.x71 + 3.5*m.b116 <= 3.5)

m.c96 = Constraint(expr=   m.x86 - 3.15*m.b116 <= 0)

m.c97 = Constraint(expr=   m.x87 + 3.15*m.b116 <= 3.15)

m.c98 = Constraint(expr= - 0.6*m.x72 + m.x88 == 0)

m.c99 = Constraint(expr=   m.x73 == 0)

m.c100 = Constraint(expr=   m.x89 == 0)

m.c101 = Constraint(expr=   m.x20 - m.x72 - m.x73 == 0)

m.c102 = Constraint(expr=   m.x26 - m.x88 - m.x89 == 0)

m.c103 = Constraint(expr=   m.x72 - 3.5*m.b117 <= 0)

m.c104 = Constraint(expr=   m.x73 + 3.5*m.b117 <= 3.5)

m.c105 = Constraint(expr=   m.x88 - 2.1*m.b117 <= 0)

m.c106 = Constraint(expr=   m.x89 + 2.1*m.b117 <= 2.1)

m.c107 = Constraint(expr=(m.x90/(1e-6 + m.b118) - 1.1*log(1 + m.x74/(1e-6 + m.b118)))*(1e-6 + m.b118) <= 0)

m.c108 = Constraint(expr=   m.x75 == 0)

m.c109 = Constraint(expr=   m.x91 == 0)

m.c110 = Constraint(expr=   m.x21 - m.x74 - m.x75 == 0)

m.c111 = Constraint(expr=   m.x27 - m.x90 - m.x91 == 0)

m.c112 = Constraint(expr=   m.x74 - 3.5*m.b118 <= 0)

m.c113 = Constraint(expr=   m.x75 + 3.5*m.b118 <= 3.5)

m.c114 = Constraint(expr=   m.x90 - 1.6544851364539*m.b118 <= 0)

m.c115 = Constraint(expr=   m.x91 + 1.6544851364539*m.b118 <= 1.6544851364539)

m.c116 = Constraint(expr= - 0.9*m.x77 + m.x100 == 0)

m.c117 = Constraint(expr= - m.x96 + m.x100 == 0)

m.c118 = Constraint(expr=   m.x79 == 0)

m.c119 = Constraint(expr=   m.x97 == 0)

m.c120 = Constraint(expr=   m.x101 == 0)

m.c121 = Constraint(expr=   m.x22 - m.x77 - m.x79 == 0)

m.c122 = Constraint(expr=   m.x30 - m.x96 - m.x97 == 0)

m.c123 = Constraint(expr=   m.x38 - m.x100 - m.x101 == 0)

m.c124 = Constraint(expr=   m.x77 - 1.43746550029693*m.b119 <= 0)

m.c125 = Constraint(expr=   m.x79 + 1.43746550029693*m.b119 <= 1.43746550029693)

m.c126 = Constraint(expr=   m.x96 - 5*m.b119 <= 0)

m.c127 = Constraint(expr=   m.x97 + 5*m.b119 <= 5)

m.c128 = Constraint(expr=   m.x100 - 5*m.b119 <= 0)

m.c129 = Constraint(expr=   m.x101 + 5*m.b119 <= 5)

m.c130 = Constraint(expr=(m.x102/(1e-6 + m.b120) - log(1 + m.x81/(1e-6 + m.b120)))*(1e-6 + m.b120) <= 0)

m.c131 = Constraint(expr=   m.x83 == 0)

m.c132 = Constraint(expr=   m.x103 == 0)

m.c133 = Constraint(expr=   m.x23 - m.x81 - m.x83 == 0)

m.c134 = Constraint(expr=   m.x39 - m.x102 - m.x103 == 0)

m.c135 = Constraint(expr=   m.x81 - 1.03497516021379*m.b120 <= 0)

m.c136 = Constraint(expr=   m.x83 + 1.03497516021379*m.b120 <= 1.03497516021379)

m.c137 = Constraint(expr=   m.x102 - 0.710483612536911*m.b120 <= 0)

m.c138 = Constraint(expr=   m.x103 + 0.710483612536911*m.b120 <= 0.710483612536911)

m.c139 = Constraint(expr=(m.x104/(1e-6 + m.b121) - 0.7*log(1 + m.x92/(1e-6 + m.b121)))*(1e-6 + m.b121) <= 0)

m.c140 = Constraint(expr=   m.x93 == 0)

m.c141 = Constraint(expr=   m.x105 == 0)

m.c142 = Constraint(expr=   m.x28 - m.x92 - m.x93 == 0)

m.c143 = Constraint(expr=   m.x40 - m.x104 - m.x105 == 0)

m.c144 = Constraint(expr=   m.x92 - 1.10947836929589*m.b121 <= 0)

m.c145 = Constraint(expr=   m.x93 + 1.10947836929589*m.b121 <= 1.10947836929589)

m.c146 = Constraint(expr=   m.x104 - 0.522508489006913*m.b121 <= 0)

m.c147 = Constraint(expr=   m.x105 + 0.522508489006913*m.b121 <= 0.522508489006913)

m.c148 = Constraint(expr=(m.x106/(1e-6 + m.b122) - 0.65*log(1 + m.x94/(1e-6 + m.b122)))*(1e-6 + m.b122) <= 0)

m.c149 = Constraint(expr=(m.x106/(1e-6 + m.b122) - 0.65*log(1 + m.x98/(1e-6 + m.b122)))*(1e-6 + m.b122) <= 0)

m.c150 = Constraint(expr=   m.x95 == 0)

m.c151 = Constraint(expr=   m.x99 == 0)

m.c152 = Constraint(expr=   m.x107 == 0)

m.c153 = Constraint(expr=   m.x29 - m.x94 - m.x95 == 0)

m.c154 = Constraint(expr=   m.x32 - m.x98 - m.x99 == 0)

m.c155 = Constraint(expr=   m.x41 - m.x106 - m.x107 == 0)

m.c156 = Constraint(expr=   m.x94 - 1.10947836929589*m.b122 <= 0)

m.c157 = Constraint(expr=   m.x95 + 1.10947836929589*m.b122 <= 1.10947836929589)

m.c158 = Constraint(expr=   m.x98 - 8.15*m.b122 <= 0)

m.c159 = Constraint(expr=   m.x99 + 8.15*m.b122 <= 8.15)

m.c160 = Constraint(expr=   m.x106 - 1.43894002153683*m.b122 <= 0)

m.c161 = Constraint(expr=   m.x107 + 1.43894002153683*m.b122 <= 1.43894002153683)

m.c162 = Constraint(expr=   m.b108 + m.b109 == 1)

m.c163 = Constraint(expr= - m.b110 + m.b113 + m.b114 >= 0)

m.c164 = Constraint(expr= - m.b113 + m.b119 >= 0)

m.c165 = Constraint(expr= - m.b114 + m.b120 >= 0)

m.c166 = Constraint(expr= - m.b111 + m.b115 >= 0)

m.c167 = Constraint(expr= - m.b115 + m.b121 + m.b122 >= 0)

m.c168 = Constraint(expr= - m.b112 + m.b116 + m.b117 + m.b118 >= 0)

m.c169 = Constraint(expr= - m.b116 + m.b122 >= 0)

m.c170 = Constraint(expr=   m.b108 + m.b109 - m.b110 >= 0)

m.c171 = Constraint(expr=   m.b108 + m.b109 - m.b111 >= 0)

m.c172 = Constraint(expr=   m.b108 + m.b109 - m.b112 >= 0)

m.c173 = Constraint(expr=   m.b110 - m.b113 >= 0)

m.c174 = Constraint(expr=   m.b110 - m.b114 >= 0)

m.c175 = Constraint(expr=   m.b111 - m.b115 >= 0)

m.c176 = Constraint(expr=   m.b112 - m.b116 >= 0)

m.c177 = Constraint(expr=   m.b112 - m.b117 >= 0)

m.c178 = Constraint(expr=   m.b112 - m.b118 >= 0)

m.c179 = Constraint(expr=   m.b113 - m.b119 >= 0)

m.c180 = Constraint(expr=   m.b114 - m.b120 >= 0)

m.c181 = Constraint(expr=   m.b115 - m.b121 >= 0)

m.c182 = Constraint(expr=   m.b115 - m.b122 >= 0)

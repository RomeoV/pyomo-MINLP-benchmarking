#  MINLP written by GAMS Convert at 08/13/20 17:38:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        284        7      114      163        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         88       52       36        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1627      685      942        0


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
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,5),initialize=0)

m.obj = Objective(expr=m.x88, sense=minimize)

m.c1 = Constraint(expr=m.x87*m.x61 + 1000*m.b1 <= 1000.024)

m.c2 = Constraint(expr=m.x87*m.x63 + 1000*m.b2 <= 1000.024)

m.c3 = Constraint(expr=m.x87*m.x65 + 1000*m.b3 <= 1000.024)

m.c4 = Constraint(expr=m.x87*m.x67 + 1000*m.b4 <= 1000.024)

m.c5 = Constraint(expr=m.x87*m.x69 + 1000*m.b5 <= 1000.024)

m.c6 = Constraint(expr=m.x87*m.x71 + 1000*m.b6 <= 1000.024)

m.c7 = Constraint(expr=m.x87*m.x73 + 1000*m.b7 <= 1000.024)

m.c8 = Constraint(expr=m.x87*m.x75 + 1000*m.b8 <= 1000.024)

m.c9 = Constraint(expr=m.x87*m.x77 + 1000*m.b9 <= 1000.024)

m.c10 = Constraint(expr=m.x87*m.x79 + 1000*m.b10 <= 1000.024)

m.c11 = Constraint(expr=m.x87*m.x81 + 1000*m.b11 <= 1000.024)

m.c12 = Constraint(expr=m.x87*m.x83 + 1000*m.b12 <= 1000.024)

m.c13 = Constraint(expr=(100*m.b14 + 100*m.b15 + 100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21
                         + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x39 + m.x86*m.x63 - (100*m.b15 + 100*m.b16 + 100
                        *m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + 
                        m.x85)*m.x41 - m.x86*m.x61 - 80*m.b14 - 1000*m.b2 + 1000*m.b26 <= 1000)

m.c14 = Constraint(expr=(100*m.b14 + 100*m.b15 + 100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21
                         + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x40 + m.x86*m.x64 - (100*m.b15 + 100*m.b16 + 100
                        *m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + 
                        m.x85)*m.x42 - m.x86*m.x62 - 20*m.b14 - 1000*m.b2 + 1000*m.b26 <= 1000)

m.c15 = Constraint(expr=(100*m.b15 + 100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22
                         + 100*m.b23 + 100*m.b24 + m.x85)*m.x41 + m.x86*m.x65 - (100*m.b16 + 100*m.b17 + 100*m.b18 + 100
                        *m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x43 - m.x86*m.x63
                         - 80*m.b15 - 1000*m.b3 + 1000*m.b27 <= 1000)

m.c16 = Constraint(expr=(100*m.b15 + 100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22
                         + 100*m.b23 + 100*m.b24 + m.x85)*m.x42 + m.x86*m.x66 - (100*m.b16 + 100*m.b17 + 100*m.b18 + 100
                        *m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x44 - m.x86*m.x64
                         - 20*m.b15 - 1000*m.b3 + 1000*m.b27 <= 1000)

m.c17 = Constraint(expr=(100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23
                         + 100*m.b24 + m.x85)*m.x43 + m.x86*m.x67 - (100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100
                        *m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x45 - m.x86*m.x65 - 80*m.b16 - 1000*m.b4
                         + 1000*m.b28 <= 1000)

m.c18 = Constraint(expr=(100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23
                         + 100*m.b24 + m.x85)*m.x44 + m.x86*m.x68 - (100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100
                        *m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x46 - m.x86*m.x66 - 20*m.b16 - 1000*m.b4
                         + 1000*m.b28 <= 1000)

m.c19 = Constraint(expr=(100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24
                         + m.x85)*m.x45 + m.x86*m.x69 - (100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100
                        *m.b23 + 100*m.b24 + m.x85)*m.x47 - m.x86*m.x67 - 80*m.b17 - 1000*m.b5 + 1000*m.b29 <= 1000)

m.c20 = Constraint(expr=(100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24
                         + m.x85)*m.x46 + m.x86*m.x70 - (100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100
                        *m.b23 + 100*m.b24 + m.x85)*m.x48 - m.x86*m.x68 - 20*m.b17 - 1000*m.b5 + 1000*m.b29 <= 1000)

m.c21 = Constraint(expr=(100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*
                        m.x47 + m.x86*m.x71 - (100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + 
                        m.x85)*m.x49 - m.x86*m.x69 - 80*m.b18 - 1000*m.b6 + 1000*m.b30 <= 1000)

m.c22 = Constraint(expr=(100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*
                        m.x48 + m.x86*m.x72 - (100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + 
                        m.x85)*m.x50 - m.x86*m.x70 - 20*m.b18 - 1000*m.b6 + 1000*m.b30 <= 1000)

m.c23 = Constraint(expr=(100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x49 + m.x86*
                        m.x73 - (100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x51 - m.x86*m.x71
                         - 80*m.b19 - 1000*m.b7 + 1000*m.b31 <= 1000)

m.c24 = Constraint(expr=(100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x50 + m.x86*
                        m.x74 - (100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x52 - m.x86*m.x72
                         - 20*m.b19 - 1000*m.b7 + 1000*m.b31 <= 1000)

m.c25 = Constraint(expr=(100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x51 + m.x86*m.x75 - (100*
                        m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x53 - m.x86*m.x73 - 80*m.b20 - 1000*m.b8
                         + 1000*m.b32 <= 1000)

m.c26 = Constraint(expr=(100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x52 + m.x86*m.x76 - (100*
                        m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x54 - m.x86*m.x74 - 20*m.b20 - 1000*m.b8
                         + 1000*m.b32 <= 1000)

m.c27 = Constraint(expr=(100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x53 + m.x86*m.x77 - (100*m.b22 + 100*
                        m.b23 + 100*m.b24 + m.x85)*m.x55 - m.x86*m.x75 - 80*m.b21 - 1000*m.b9 + 1000*m.b33 <= 1000)

m.c28 = Constraint(expr=(100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x54 + m.x86*m.x78 - (100*m.b22 + 100*
                        m.b23 + 100*m.b24 + m.x85)*m.x56 - m.x86*m.x76 - 20*m.b21 - 1000*m.b9 + 1000*m.b33 <= 1000)

m.c29 = Constraint(expr=(100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x55 + m.x86*m.x79 - (100*m.b23 + 100*m.b24 + m.x85
                        )*m.x57 - m.x86*m.x77 - 80*m.b22 - 1000*m.b10 + 1000*m.b34 <= 1000)

m.c30 = Constraint(expr=(100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x56 + m.x86*m.x80 - (100*m.b23 + 100*m.b24 + m.x85
                        )*m.x58 - m.x86*m.x78 - 20*m.b22 - 1000*m.b10 + 1000*m.b34 <= 1000)

m.c31 = Constraint(expr=(100*m.b23 + 100*m.b24 + m.x85)*m.x57 + m.x86*m.x81 - (100*m.b24 + m.x85)*m.x59 - m.x86*m.x79 - 
                        80*m.b23 - 1000*m.b11 + 1000*m.b35 <= 1000)

m.c32 = Constraint(expr=(100*m.b23 + 100*m.b24 + m.x85)*m.x58 + m.x86*m.x82 - (100*m.b24 + m.x85)*m.x60 - m.x86*m.x80 - 
                        20*m.b23 - 1000*m.b11 + 1000*m.b35 <= 1000)

m.c33 = Constraint(expr=m.x86*m.x61 - (100 + m.x85)*m.x39 + 80*m.x37 == 0)

m.c34 = Constraint(expr=m.x86*m.x62 - (100 + m.x85)*m.x40 + 80*m.x38 == 0)

m.c35 = Constraint(expr=(100*m.b14 + 100*m.b15 + 100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21
                         + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x39 + m.x86*m.x63 - (100*m.b15 + 100*m.b16 + 100
                        *m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + 
                        m.x85)*m.x41 - m.x86*m.x61 - 80*m.b14 - 1000*m.b2 + 1000*m.b26 >= 1000)

m.c36 = Constraint(expr=(100*m.b14 + 100*m.b15 + 100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21
                         + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x40 + m.x86*m.x64 - (100*m.b15 + 100*m.b16 + 100
                        *m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + 
                        m.x85)*m.x42 - m.x86*m.x62 - 20*m.b14 - 1000*m.b2 + 1000*m.b26 >= 1000)

m.c37 = Constraint(expr=(100*m.b15 + 100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22
                         + 100*m.b23 + 100*m.b24 + m.x85)*m.x41 + m.x86*m.x65 - (100*m.b16 + 100*m.b17 + 100*m.b18 + 100
                        *m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x43 - m.x86*m.x63
                         - 80*m.b15 - 1000*m.b3 + 1000*m.b27 >= 1000)

m.c38 = Constraint(expr=(100*m.b15 + 100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22
                         + 100*m.b23 + 100*m.b24 + m.x85)*m.x42 + m.x86*m.x66 - (100*m.b16 + 100*m.b17 + 100*m.b18 + 100
                        *m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x44 - m.x86*m.x64
                         - 20*m.b15 - 1000*m.b3 + 1000*m.b27 >= 1000)

m.c39 = Constraint(expr=(100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23
                         + 100*m.b24 + m.x85)*m.x43 + m.x86*m.x67 - (100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100
                        *m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x45 - m.x86*m.x65 - 80*m.b16 - 1000*m.b4
                         + 1000*m.b28 >= 1000)

m.c40 = Constraint(expr=(100*m.b16 + 100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23
                         + 100*m.b24 + m.x85)*m.x44 + m.x86*m.x68 - (100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100
                        *m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x46 - m.x86*m.x66 - 20*m.b16 - 1000*m.b4
                         + 1000*m.b28 >= 1000)

m.c41 = Constraint(expr=(100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24
                         + m.x85)*m.x45 + m.x86*m.x69 - (100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100
                        *m.b23 + 100*m.b24 + m.x85)*m.x47 - m.x86*m.x67 - 80*m.b17 - 1000*m.b5 + 1000*m.b29 >= 1000)

m.c42 = Constraint(expr=(100*m.b17 + 100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24
                         + m.x85)*m.x46 + m.x86*m.x70 - (100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100
                        *m.b23 + 100*m.b24 + m.x85)*m.x48 - m.x86*m.x68 - 20*m.b17 - 1000*m.b5 + 1000*m.b29 >= 1000)

m.c43 = Constraint(expr=(100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*
                        m.x47 + m.x86*m.x71 - (100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + 
                        m.x85)*m.x49 - m.x86*m.x69 - 80*m.b18 - 1000*m.b6 + 1000*m.b30 >= 1000)

m.c44 = Constraint(expr=(100*m.b18 + 100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*
                        m.x48 + m.x86*m.x72 - (100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + 
                        m.x85)*m.x50 - m.x86*m.x70 - 20*m.b18 - 1000*m.b6 + 1000*m.b30 >= 1000)

m.c45 = Constraint(expr=(100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x49 + m.x86*
                        m.x73 - (100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x51 - m.x86*m.x71
                         - 80*m.b19 - 1000*m.b7 + 1000*m.b31 >= 1000)

m.c46 = Constraint(expr=(100*m.b19 + 100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x50 + m.x86*
                        m.x74 - (100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x52 - m.x86*m.x72
                         - 20*m.b19 - 1000*m.b7 + 1000*m.b31 >= 1000)

m.c47 = Constraint(expr=(100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x51 + m.x86*m.x75 - (100*
                        m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x53 - m.x86*m.x73 - 80*m.b20 - 1000*m.b8
                         + 1000*m.b32 >= 1000)

m.c48 = Constraint(expr=(100*m.b20 + 100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x52 + m.x86*m.x76 - (100*
                        m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x54 - m.x86*m.x74 - 20*m.b20 - 1000*m.b8
                         + 1000*m.b32 >= 1000)

m.c49 = Constraint(expr=(100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x53 + m.x86*m.x77 - (100*m.b22 + 100*
                        m.b23 + 100*m.b24 + m.x85)*m.x55 - m.x86*m.x75 - 80*m.b21 - 1000*m.b9 + 1000*m.b33 >= 1000)

m.c50 = Constraint(expr=(100*m.b21 + 100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x54 + m.x86*m.x78 - (100*m.b22 + 100*
                        m.b23 + 100*m.b24 + m.x85)*m.x56 - m.x86*m.x76 - 20*m.b21 - 1000*m.b9 + 1000*m.b33 >= 1000)

m.c51 = Constraint(expr=(100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x55 + m.x86*m.x79 - (100*m.b23 + 100*m.b24 + m.x85
                        )*m.x57 - m.x86*m.x77 - 80*m.b22 - 1000*m.b10 + 1000*m.b34 >= 1000)

m.c52 = Constraint(expr=(100*m.b22 + 100*m.b23 + 100*m.b24 + m.x85)*m.x56 + m.x86*m.x80 - (100*m.b23 + 100*m.b24 + m.x85
                        )*m.x58 - m.x86*m.x78 - 20*m.b22 - 1000*m.b10 + 1000*m.b34 >= 1000)

m.c53 = Constraint(expr=(100*m.b23 + 100*m.b24 + m.x85)*m.x57 + m.x86*m.x81 - (100*m.b24 + m.x85)*m.x59 - m.x86*m.x79 - 
                        80*m.b23 - 1000*m.b11 + 1000*m.b35 >= 1000)

m.c54 = Constraint(expr=(100*m.b23 + 100*m.b24 + m.x85)*m.x58 + m.x86*m.x82 - (100*m.b24 + m.x85)*m.x60 - m.x86*m.x80 - 
                        20*m.b23 - 1000*m.b11 + 1000*m.b35 >= 1000)

m.c55 = Constraint(expr=m.x85*m.x39 + m.x87*m.x63 - m.x86*m.x61 + 1000*m.b2 <= 1000)

m.c56 = Constraint(expr=m.x85*m.x40 + m.x87*m.x64 - m.x86*m.x62 + 1000*m.b2 <= 1000)

m.c57 = Constraint(expr=m.x85*m.x41 + m.x87*m.x65 - m.x86*m.x63 + 1000*m.b3 <= 1000)

m.c58 = Constraint(expr=m.x85*m.x42 + m.x87*m.x66 - m.x86*m.x64 + 1000*m.b3 <= 1000)

m.c59 = Constraint(expr=m.x85*m.x43 + m.x87*m.x67 - m.x86*m.x65 + 1000*m.b4 <= 1000)

m.c60 = Constraint(expr=m.x85*m.x44 + m.x87*m.x68 - m.x86*m.x66 + 1000*m.b4 <= 1000)

m.c61 = Constraint(expr=m.x85*m.x45 + m.x87*m.x69 - m.x86*m.x67 + 1000*m.b5 <= 1000)

m.c62 = Constraint(expr=m.x85*m.x46 + m.x87*m.x70 - m.x86*m.x68 + 1000*m.b5 <= 1000)

m.c63 = Constraint(expr=m.x85*m.x47 + m.x87*m.x71 - m.x86*m.x69 + 1000*m.b6 <= 1000)

m.c64 = Constraint(expr=m.x85*m.x48 + m.x87*m.x72 - m.x86*m.x70 + 1000*m.b6 <= 1000)

m.c65 = Constraint(expr=m.x85*m.x49 + m.x87*m.x73 - m.x86*m.x71 + 1000*m.b7 <= 1000)

m.c66 = Constraint(expr=m.x85*m.x50 + m.x87*m.x74 - m.x86*m.x72 + 1000*m.b7 <= 1000)

m.c67 = Constraint(expr=m.x85*m.x51 + m.x87*m.x75 - m.x86*m.x73 + 1000*m.b8 <= 1000)

m.c68 = Constraint(expr=m.x85*m.x52 + m.x87*m.x76 - m.x86*m.x74 + 1000*m.b8 <= 1000)

m.c69 = Constraint(expr=m.x85*m.x53 + m.x87*m.x77 - m.x86*m.x75 + 1000*m.b9 <= 1000)

m.c70 = Constraint(expr=m.x85*m.x54 + m.x87*m.x78 - m.x86*m.x76 + 1000*m.b9 <= 1000)

m.c71 = Constraint(expr=m.x85*m.x55 + m.x87*m.x79 - m.x86*m.x77 + 1000*m.b10 <= 1000)

m.c72 = Constraint(expr=m.x85*m.x56 + m.x87*m.x80 - m.x86*m.x78 + 1000*m.b10 <= 1000)

m.c73 = Constraint(expr=m.x85*m.x57 + m.x87*m.x81 - m.x86*m.x79 + 1000*m.b11 <= 1000)

m.c74 = Constraint(expr=m.x85*m.x58 + m.x87*m.x82 - m.x86*m.x80 + 1000*m.b11 <= 1000)

m.c75 = Constraint(expr=m.x85*m.x59 + m.x87*m.x83 - m.x86*m.x81 + 1000*m.b12 <= 1000)

m.c76 = Constraint(expr=m.x85*m.x60 + m.x87*m.x84 - m.x86*m.x82 + 1000*m.b12 <= 1000)

m.c77 = Constraint(expr=m.x85*m.x39 + m.x87*m.x63 - m.x86*m.x61 - 1000*m.b2 >= -1000)

m.c78 = Constraint(expr=m.x85*m.x40 + m.x87*m.x64 - m.x86*m.x62 - 1000*m.b2 >= -1000)

m.c79 = Constraint(expr=m.x85*m.x41 + m.x87*m.x65 - m.x86*m.x63 - 1000*m.b3 >= -1000)

m.c80 = Constraint(expr=m.x85*m.x42 + m.x87*m.x66 - m.x86*m.x64 - 1000*m.b3 >= -1000)

m.c81 = Constraint(expr=m.x85*m.x43 + m.x87*m.x67 - m.x86*m.x65 - 1000*m.b4 >= -1000)

m.c82 = Constraint(expr=m.x85*m.x44 + m.x87*m.x68 - m.x86*m.x66 - 1000*m.b4 >= -1000)

m.c83 = Constraint(expr=m.x85*m.x45 + m.x87*m.x69 - m.x86*m.x67 - 1000*m.b5 >= -1000)

m.c84 = Constraint(expr=m.x85*m.x46 + m.x87*m.x70 - m.x86*m.x68 - 1000*m.b5 >= -1000)

m.c85 = Constraint(expr=m.x85*m.x47 + m.x87*m.x71 - m.x86*m.x69 - 1000*m.b6 >= -1000)

m.c86 = Constraint(expr=m.x85*m.x48 + m.x87*m.x72 - m.x86*m.x70 - 1000*m.b6 >= -1000)

m.c87 = Constraint(expr=m.x85*m.x49 + m.x87*m.x73 - m.x86*m.x71 - 1000*m.b7 >= -1000)

m.c88 = Constraint(expr=m.x85*m.x50 + m.x87*m.x74 - m.x86*m.x72 - 1000*m.b7 >= -1000)

m.c89 = Constraint(expr=m.x85*m.x51 + m.x87*m.x75 - m.x86*m.x73 - 1000*m.b8 >= -1000)

m.c90 = Constraint(expr=m.x85*m.x52 + m.x87*m.x76 - m.x86*m.x74 - 1000*m.b8 >= -1000)

m.c91 = Constraint(expr=m.x85*m.x53 + m.x87*m.x77 - m.x86*m.x75 - 1000*m.b9 >= -1000)

m.c92 = Constraint(expr=m.x85*m.x54 + m.x87*m.x78 - m.x86*m.x76 - 1000*m.b9 >= -1000)

m.c93 = Constraint(expr=m.x85*m.x55 + m.x87*m.x79 - m.x86*m.x77 - 1000*m.b10 >= -1000)

m.c94 = Constraint(expr=m.x85*m.x56 + m.x87*m.x80 - m.x86*m.x78 - 1000*m.b10 >= -1000)

m.c95 = Constraint(expr=m.x85*m.x57 + m.x87*m.x81 - m.x86*m.x79 - 1000*m.b11 >= -1000)

m.c96 = Constraint(expr=m.x85*m.x58 + m.x87*m.x82 - m.x86*m.x80 - 1000*m.b11 >= -1000)

m.c97 = Constraint(expr=m.x85*m.x59 + m.x87*m.x83 - m.x86*m.x81 - 1000*m.b12 >= -1000)

m.c98 = Constraint(expr=m.x85*m.x60 + m.x87*m.x84 - m.x86*m.x82 - 1000*m.b12 >= -1000)

m.c99 = Constraint(expr=-m.x88*m.x87 + m.x85 == 0)

m.c100 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23
                          + m.b24 == 1)

m.c101 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c102 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35
                          + m.b36 == 12)

m.c103 = Constraint(expr=   m.b1 + 2*m.b2 + 3*m.b3 + 4*m.b4 + 5*m.b5 + 6*m.b6 + 7*m.b7 + 8*m.b8 + 9*m.b9 + 10*m.b10
                          + 11*m.b11 + 12*m.b12 == 12)

m.c104 = Constraint(expr= - m.b1 - 2*m.b2 - 3*m.b3 - 4*m.b4 - 5*m.b5 - 6*m.b6 - 7*m.b7 - 8*m.b8 - 9*m.b9 - 10*m.b10
                          - 11*m.b11 - 12*m.b12 + m.b13 + 2*m.b14 + 3*m.b15 + 4*m.b16 + 5*m.b17 + 6*m.b18 + 7*m.b19
                          + 8*m.b20 + 9*m.b21 + 10*m.b22 + 11*m.b23 + 12*m.b24 <= 0)

m.c105 = Constraint(expr=   m.b1 - m.b25 <= 0)

m.c106 = Constraint(expr=   m.b2 - m.b26 <= 0)

m.c107 = Constraint(expr=   m.b3 - m.b27 <= 0)

m.c108 = Constraint(expr=   m.b4 - m.b28 <= 0)

m.c109 = Constraint(expr=   m.b5 - m.b29 <= 0)

m.c110 = Constraint(expr=   m.b6 - m.b30 <= 0)

m.c111 = Constraint(expr=   m.b7 - m.b31 <= 0)

m.c112 = Constraint(expr=   m.b8 - m.b32 <= 0)

m.c113 = Constraint(expr=   m.b9 - m.b33 <= 0)

m.c114 = Constraint(expr=   m.b10 - m.b34 <= 0)

m.c115 = Constraint(expr=   m.b11 - m.b35 <= 0)

m.c116 = Constraint(expr=   m.b12 - m.b36 <= 0)

m.c117 = Constraint(expr=   m.b13 - m.b25 <= 0)

m.c118 = Constraint(expr=   m.b14 - m.b26 <= 0)

m.c119 = Constraint(expr=   m.b15 - m.b27 <= 0)

m.c120 = Constraint(expr=   m.b16 - m.b28 <= 0)

m.c121 = Constraint(expr=   m.b17 - m.b29 <= 0)

m.c122 = Constraint(expr=   m.b18 - m.b30 <= 0)

m.c123 = Constraint(expr=   m.b19 - m.b31 <= 0)

m.c124 = Constraint(expr=   m.b20 - m.b32 <= 0)

m.c125 = Constraint(expr=   m.b21 - m.b33 <= 0)

m.c126 = Constraint(expr=   m.b22 - m.b34 <= 0)

m.c127 = Constraint(expr=   m.b23 - m.b35 <= 0)

m.c128 = Constraint(expr=   m.b24 - m.b36 <= 0)

m.c129 = Constraint(expr= - m.b1 - m.b2 - m.b3 - m.b4 - m.b5 - m.b6 - m.b7 - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 + m.b25
                          <= 0)

m.c130 = Constraint(expr= - m.b2 - m.b3 - m.b4 - m.b5 - m.b6 - m.b7 - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 + m.b26 <= 0)

m.c131 = Constraint(expr= - m.b3 - m.b4 - m.b5 - m.b6 - m.b7 - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 + m.b27 <= 0)

m.c132 = Constraint(expr= - m.b4 - m.b5 - m.b6 - m.b7 - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 + m.b28 <= 0)

m.c133 = Constraint(expr= - m.b5 - m.b6 - m.b7 - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 + m.b29 <= 0)

m.c134 = Constraint(expr= - m.b6 - m.b7 - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 + m.b30 <= 0)

m.c135 = Constraint(expr= - m.b7 - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 + m.b31 <= 0)

m.c136 = Constraint(expr= - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 + m.b32 <= 0)

m.c137 = Constraint(expr= - m.b9 - m.b10 - m.b11 - m.b12 + m.b33 <= 0)

m.c138 = Constraint(expr= - m.b10 - m.b11 - m.b12 + m.b34 <= 0)

m.c139 = Constraint(expr= - m.b11 - m.b12 + m.b35 <= 0)

m.c140 = Constraint(expr= - m.b12 + m.b36 <= 0)

m.c141 = Constraint(expr= - m.b25 - m.x61 - m.x62 <= 0)

m.c142 = Constraint(expr= - m.b26 - m.x63 - m.x64 <= 0)

m.c143 = Constraint(expr= - m.b27 - m.x65 - m.x66 <= 0)

m.c144 = Constraint(expr= - m.b28 - m.x67 - m.x68 <= 0)

m.c145 = Constraint(expr= - m.b29 - m.x69 - m.x70 <= 0)

m.c146 = Constraint(expr= - m.b30 - m.x71 - m.x72 <= 0)

m.c147 = Constraint(expr= - m.b31 - m.x73 - m.x74 <= 0)

m.c148 = Constraint(expr= - m.b32 - m.x75 - m.x76 <= 0)

m.c149 = Constraint(expr= - m.b33 - m.x77 - m.x78 <= 0)

m.c150 = Constraint(expr= - m.b34 - m.x79 - m.x80 <= 0)

m.c151 = Constraint(expr= - m.b35 - m.x81 - m.x82 <= 0)

m.c152 = Constraint(expr= - m.b36 - m.x83 - m.x84 <= 0)

m.c153 = Constraint(expr=   m.b25 - m.x61 - m.x62 <= 0)

m.c154 = Constraint(expr=   m.b26 - m.x63 - m.x64 <= 0)

m.c155 = Constraint(expr=   m.b27 - m.x65 - m.x66 <= 0)

m.c156 = Constraint(expr=   m.b28 - m.x67 - m.x68 <= 0)

m.c157 = Constraint(expr=   m.b29 - m.x69 - m.x70 <= 0)

m.c158 = Constraint(expr=   m.b30 - m.x71 - m.x72 <= 0)

m.c159 = Constraint(expr=   m.b31 - m.x73 - m.x74 <= 0)

m.c160 = Constraint(expr=   m.b32 - m.x75 - m.x76 <= 0)

m.c161 = Constraint(expr=   m.b33 - m.x77 - m.x78 <= 0)

m.c162 = Constraint(expr=   m.b34 - m.x79 - m.x80 <= 0)

m.c163 = Constraint(expr=   m.b35 - m.x81 - m.x82 <= 0)

m.c164 = Constraint(expr=   m.b36 - m.x83 - m.x84 <= 0)

m.c165 = Constraint(expr= - m.b25 - m.x37 - m.x38 <= 0)

m.c166 = Constraint(expr= - m.b26 - m.x39 - m.x40 <= 0)

m.c167 = Constraint(expr= - m.b27 - m.x41 - m.x42 <= 0)

m.c168 = Constraint(expr= - m.b28 - m.x43 - m.x44 <= 0)

m.c169 = Constraint(expr= - m.b29 - m.x45 - m.x46 <= 0)

m.c170 = Constraint(expr= - m.b30 - m.x47 - m.x48 <= 0)

m.c171 = Constraint(expr= - m.b31 - m.x49 - m.x50 <= 0)

m.c172 = Constraint(expr= - m.b32 - m.x51 - m.x52 <= 0)

m.c173 = Constraint(expr= - m.b33 - m.x53 - m.x54 <= 0)

m.c174 = Constraint(expr= - m.b34 - m.x55 - m.x56 <= 0)

m.c175 = Constraint(expr= - m.b35 - m.x57 - m.x58 <= 0)

m.c176 = Constraint(expr= - m.b36 - m.x59 - m.x60 <= 0)

m.c177 = Constraint(expr=   m.b25 - m.x37 - m.x38 <= 0)

m.c178 = Constraint(expr=   m.b26 - m.x39 - m.x40 <= 0)

m.c179 = Constraint(expr=   m.b27 - m.x41 - m.x42 <= 0)

m.c180 = Constraint(expr=   m.b28 - m.x43 - m.x44 <= 0)

m.c181 = Constraint(expr=   m.b29 - m.x45 - m.x46 <= 0)

m.c182 = Constraint(expr=   m.b30 - m.x47 - m.x48 <= 0)

m.c183 = Constraint(expr=   m.b31 - m.x49 - m.x50 <= 0)

m.c184 = Constraint(expr=   m.b32 - m.x51 - m.x52 <= 0)

m.c185 = Constraint(expr=   m.b33 - m.x53 - m.x54 <= 0)

m.c186 = Constraint(expr=   m.b34 - m.x55 - m.x56 <= 0)

m.c187 = Constraint(expr=   m.b35 - m.x57 - m.x58 <= 0)

m.c188 = Constraint(expr=   m.b36 - m.x59 - m.x60 <= 0)

m.c189 = Constraint(expr= - m.b25 - m.x61 - m.x62 >= -2)

m.c190 = Constraint(expr= - m.b26 - m.x63 - m.x64 >= -2)

m.c191 = Constraint(expr= - m.b27 - m.x65 - m.x66 >= -2)

m.c192 = Constraint(expr= - m.b28 - m.x67 - m.x68 >= -2)

m.c193 = Constraint(expr= - m.b29 - m.x69 - m.x70 >= -2)

m.c194 = Constraint(expr= - m.b30 - m.x71 - m.x72 >= -2)

m.c195 = Constraint(expr= - m.b31 - m.x73 - m.x74 >= -2)

m.c196 = Constraint(expr= - m.b32 - m.x75 - m.x76 >= -2)

m.c197 = Constraint(expr= - m.b33 - m.x77 - m.x78 >= -2)

m.c198 = Constraint(expr= - m.b34 - m.x79 - m.x80 >= -2)

m.c199 = Constraint(expr= - m.b35 - m.x81 - m.x82 >= -2)

m.c200 = Constraint(expr= - m.b36 - m.x83 - m.x84 >= -2)

m.c201 = Constraint(expr=   m.b25 - m.x61 - m.x62 >= -2)

m.c202 = Constraint(expr=   m.b26 - m.x63 - m.x64 >= -2)

m.c203 = Constraint(expr=   m.b27 - m.x65 - m.x66 >= -2)

m.c204 = Constraint(expr=   m.b28 - m.x67 - m.x68 >= -2)

m.c205 = Constraint(expr=   m.b29 - m.x69 - m.x70 >= -2)

m.c206 = Constraint(expr=   m.b30 - m.x71 - m.x72 >= -2)

m.c207 = Constraint(expr=   m.b31 - m.x73 - m.x74 >= -2)

m.c208 = Constraint(expr=   m.b32 - m.x75 - m.x76 >= -2)

m.c209 = Constraint(expr=   m.b33 - m.x77 - m.x78 >= -2)

m.c210 = Constraint(expr=   m.b34 - m.x79 - m.x80 >= -2)

m.c211 = Constraint(expr=   m.b35 - m.x81 - m.x82 >= -2)

m.c212 = Constraint(expr=   m.b36 - m.x83 - m.x84 >= -2)

m.c213 = Constraint(expr= - m.b25 - m.x37 - m.x38 >= -2)

m.c214 = Constraint(expr= - m.b26 - m.x39 - m.x40 >= -2)

m.c215 = Constraint(expr= - m.b27 - m.x41 - m.x42 >= -2)

m.c216 = Constraint(expr= - m.b28 - m.x43 - m.x44 >= -2)

m.c217 = Constraint(expr= - m.b29 - m.x45 - m.x46 >= -2)

m.c218 = Constraint(expr= - m.b30 - m.x47 - m.x48 >= -2)

m.c219 = Constraint(expr= - m.b31 - m.x49 - m.x50 >= -2)

m.c220 = Constraint(expr= - m.b32 - m.x51 - m.x52 >= -2)

m.c221 = Constraint(expr= - m.b33 - m.x53 - m.x54 >= -2)

m.c222 = Constraint(expr= - m.b34 - m.x55 - m.x56 >= -2)

m.c223 = Constraint(expr= - m.b35 - m.x57 - m.x58 >= -2)

m.c224 = Constraint(expr= - m.b36 - m.x59 - m.x60 >= -2)

m.c225 = Constraint(expr=   m.b25 - m.x37 - m.x38 >= -2)

m.c226 = Constraint(expr=   m.b26 - m.x39 - m.x40 >= -2)

m.c227 = Constraint(expr=   m.b27 - m.x41 - m.x42 >= -2)

m.c228 = Constraint(expr=   m.b28 - m.x43 - m.x44 >= -2)

m.c229 = Constraint(expr=   m.b29 - m.x45 - m.x46 >= -2)

m.c230 = Constraint(expr=   m.b30 - m.x47 - m.x48 >= -2)

m.c231 = Constraint(expr=   m.b31 - m.x49 - m.x50 >= -2)

m.c232 = Constraint(expr=   m.b32 - m.x51 - m.x52 >= -2)

m.c233 = Constraint(expr=   m.b33 - m.x53 - m.x54 >= -2)

m.c234 = Constraint(expr=   m.b34 - m.x55 - m.x56 >= -2)

m.c235 = Constraint(expr=   m.b35 - m.x57 - m.x58 >= -2)

m.c236 = Constraint(expr=   m.b36 - m.x59 - m.x60 >= -2)

m.c237 = Constraint(expr=(m.x37 + 5.13435*m.x38)*m.x61 - m.x37 + 1000*m.b25 <= 1000)

m.c238 = Constraint(expr=(m.x37 + 5.13435*m.x38)*m.x62 - 5.13435*m.x38 + 1000*m.b25 <= 1000)

m.c239 = Constraint(expr=(m.x39 + 5.13435*m.x40)*m.x63 - m.x39 + 1000*m.b26 <= 1000)

m.c240 = Constraint(expr=(m.x39 + 5.13435*m.x40)*m.x64 - 5.13435*m.x40 + 1000*m.b26 <= 1000)

m.c241 = Constraint(expr=(m.x41 + 5.13435*m.x42)*m.x65 - m.x41 + 1000*m.b27 <= 1000)

m.c242 = Constraint(expr=(m.x41 + 5.13435*m.x42)*m.x66 - 5.13435*m.x42 + 1000*m.b27 <= 1000)

m.c243 = Constraint(expr=(m.x43 + 5.13435*m.x44)*m.x67 - m.x43 + 1000*m.b28 <= 1000)

m.c244 = Constraint(expr=(m.x43 + 5.13435*m.x44)*m.x68 - 5.13435*m.x44 + 1000*m.b28 <= 1000)

m.c245 = Constraint(expr=(m.x45 + 5.13435*m.x46)*m.x69 - m.x45 + 1000*m.b29 <= 1000)

m.c246 = Constraint(expr=(m.x45 + 5.13435*m.x46)*m.x70 - 5.13435*m.x46 + 1000*m.b29 <= 1000)

m.c247 = Constraint(expr=(m.x47 + 5.13435*m.x48)*m.x71 - m.x47 + 1000*m.b30 <= 1000)

m.c248 = Constraint(expr=(m.x47 + 5.13435*m.x48)*m.x72 - 5.13435*m.x48 + 1000*m.b30 <= 1000)

m.c249 = Constraint(expr=(m.x49 + 5.13435*m.x50)*m.x73 - m.x49 + 1000*m.b31 <= 1000)

m.c250 = Constraint(expr=(m.x49 + 5.13435*m.x50)*m.x74 - 5.13435*m.x50 + 1000*m.b31 <= 1000)

m.c251 = Constraint(expr=(m.x51 + 5.13435*m.x52)*m.x75 - m.x51 + 1000*m.b32 <= 1000)

m.c252 = Constraint(expr=(m.x51 + 5.13435*m.x52)*m.x76 - 5.13435*m.x52 + 1000*m.b32 <= 1000)

m.c253 = Constraint(expr=(m.x53 + 5.13435*m.x54)*m.x77 - m.x53 + 1000*m.b33 <= 1000)

m.c254 = Constraint(expr=(m.x53 + 5.13435*m.x54)*m.x78 - 5.13435*m.x54 + 1000*m.b33 <= 1000)

m.c255 = Constraint(expr=(m.x55 + 5.13435*m.x56)*m.x79 - m.x55 + 1000*m.b34 <= 1000)

m.c256 = Constraint(expr=(m.x55 + 5.13435*m.x56)*m.x80 - 5.13435*m.x56 + 1000*m.b34 <= 1000)

m.c257 = Constraint(expr=(m.x57 + 5.13435*m.x58)*m.x81 - m.x57 + 1000*m.b35 <= 1000)

m.c258 = Constraint(expr=(m.x57 + 5.13435*m.x58)*m.x82 - 5.13435*m.x58 + 1000*m.b35 <= 1000)

m.c259 = Constraint(expr=(m.x59 + 5.13435*m.x60)*m.x83 - m.x59 + 1000*m.b36 <= 1000)

m.c260 = Constraint(expr=(m.x59 + 5.13435*m.x60)*m.x84 - 5.13435*m.x60 + 1000*m.b36 <= 1000)

m.c261 = Constraint(expr=(m.x37 + 5.13435*m.x38)*m.x61 - m.x37 - 1000*m.b25 >= -1000)

m.c262 = Constraint(expr=(m.x37 + 5.13435*m.x38)*m.x62 - 5.13435*m.x38 - 1000*m.b25 >= -1000)

m.c263 = Constraint(expr=(m.x39 + 5.13435*m.x40)*m.x63 - m.x39 - 1000*m.b26 >= -1000)

m.c264 = Constraint(expr=(m.x39 + 5.13435*m.x40)*m.x64 - 5.13435*m.x40 - 1000*m.b26 >= -1000)

m.c265 = Constraint(expr=(m.x41 + 5.13435*m.x42)*m.x65 - m.x41 - 1000*m.b27 >= -1000)

m.c266 = Constraint(expr=(m.x41 + 5.13435*m.x42)*m.x66 - 5.13435*m.x42 - 1000*m.b27 >= -1000)

m.c267 = Constraint(expr=(m.x43 + 5.13435*m.x44)*m.x67 - m.x43 - 1000*m.b28 >= -1000)

m.c268 = Constraint(expr=(m.x43 + 5.13435*m.x44)*m.x68 - 5.13435*m.x44 - 1000*m.b28 >= -1000)

m.c269 = Constraint(expr=(m.x45 + 5.13435*m.x46)*m.x69 - m.x45 - 1000*m.b29 >= -1000)

m.c270 = Constraint(expr=(m.x45 + 5.13435*m.x46)*m.x70 - 5.13435*m.x46 - 1000*m.b29 >= -1000)

m.c271 = Constraint(expr=(m.x47 + 5.13435*m.x48)*m.x71 - m.x47 - 1000*m.b30 >= -1000)

m.c272 = Constraint(expr=(m.x47 + 5.13435*m.x48)*m.x72 - 5.13435*m.x48 - 1000*m.b30 >= -1000)

m.c273 = Constraint(expr=(m.x49 + 5.13435*m.x50)*m.x73 - m.x49 - 1000*m.b31 >= -1000)

m.c274 = Constraint(expr=(m.x49 + 5.13435*m.x50)*m.x74 - 5.13435*m.x50 - 1000*m.b31 >= -1000)

m.c275 = Constraint(expr=(m.x51 + 5.13435*m.x52)*m.x75 - m.x51 - 1000*m.b32 >= -1000)

m.c276 = Constraint(expr=(m.x51 + 5.13435*m.x52)*m.x76 - 5.13435*m.x52 - 1000*m.b32 >= -1000)

m.c277 = Constraint(expr=(m.x53 + 5.13435*m.x54)*m.x77 - m.x53 - 1000*m.b33 >= -1000)

m.c278 = Constraint(expr=(m.x53 + 5.13435*m.x54)*m.x78 - 5.13435*m.x54 - 1000*m.b33 >= -1000)

m.c279 = Constraint(expr=(m.x55 + 5.13435*m.x56)*m.x79 - m.x55 - 1000*m.b34 >= -1000)

m.c280 = Constraint(expr=(m.x55 + 5.13435*m.x56)*m.x80 - 5.13435*m.x56 - 1000*m.b34 >= -1000)

m.c281 = Constraint(expr=(m.x57 + 5.13435*m.x58)*m.x81 - m.x57 - 1000*m.b35 >= -1000)

m.c282 = Constraint(expr=(m.x57 + 5.13435*m.x58)*m.x82 - 5.13435*m.x58 - 1000*m.b35 >= -1000)

m.c283 = Constraint(expr=(m.x59 + 5.13435*m.x60)*m.x83 - m.x59 - 1000*m.b36 >= -1000)

m.c284 = Constraint(expr=(m.x59 + 5.13435*m.x60)*m.x84 - 5.13435*m.x60 - 1000*m.b36 >= -1000)

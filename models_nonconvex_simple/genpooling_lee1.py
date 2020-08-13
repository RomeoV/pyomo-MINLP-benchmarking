#  MINLP written by GAMS Convert at 08/13/20 17:37:51
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         83       13        0       70        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         50       41        9        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        370      242      128        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,686),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,229),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,173),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,284),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,229),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,173),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,284),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,229),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,173),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,284),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,229),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,173),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,284),initialize=0)
m.x33 = Var(within=Reals,bounds=(0.13,0.89),initialize=0.13)
m.x34 = Var(within=Reals,bounds=(0.11,0.87),initialize=0.11)
m.x35 = Var(within=Reals,bounds=(0.13,0.89),initialize=0.13)
m.x36 = Var(within=Reals,bounds=(0.11,0.87),initialize=0.11)
m.x37 = Var(within=Reals,bounds=(0.13,0.89),initialize=0.13)
m.x38 = Var(within=Reals,bounds=(0.11,0.87),initialize=0.11)
m.x39 = Var(within=Reals,bounds=(0.13,0.89),initialize=0.13)
m.x40 = Var(within=Reals,bounds=(0.11,0.87),initialize=0.11)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   6.2*m.x1 + 9.4*m.x2 + 7.6*m.x3 + 10.2*m.x4 + 1.67*m.x5 + 2.53*m.x6 + 2.05*m.x7 + 2.75*m.x8
                        + 3.58*m.x9 + 5.42*m.x10 + 4.39*m.x11 + 5.89*m.x12 + 4.53*m.x13 + 6.87*m.x14 + 5.55*m.x15
                        + 7.45*m.x16 + 2.62*m.x17 + 3.98*m.x18 + 3.22*m.x19 + 4.32*m.x20 - 10.5*m.x21 - 11.2*m.x22
                        - 12.5*m.x23 - 10.5*m.x24 - 11.2*m.x25 - 12.5*m.x26 - 10.5*m.x27 - 11.2*m.x28 - 12.5*m.x29
                        - 10.5*m.x30 - 11.2*m.x31 - 12.5*m.x32 + 260*m.b41 + 70*m.b42 + 150*m.b43 + 190*m.b44
                        + 110*m.b45 + 310*m.b46 + 470*m.b47 + 380*m.b48 + 510*m.b49, sense=minimize)

m.c2 = Constraint(expr= - m.x21 - m.x24 - m.x27 - m.x30 <= -229)

m.c3 = Constraint(expr= - m.x22 - m.x25 - m.x28 - m.x31 <= -173)

m.c4 = Constraint(expr= - m.x23 - m.x26 - m.x29 - m.x32 <= -284)

m.c5 = Constraint(expr=   m.x21 + m.x24 + m.x27 + m.x30 <= 229)

m.c6 = Constraint(expr=   m.x22 + m.x25 + m.x28 + m.x31 <= 173)

m.c7 = Constraint(expr=   m.x23 + m.x26 + m.x29 + m.x32 <= 284)

m.c8 = Constraint(expr=   m.x1 + m.x5 + m.x9 + m.x13 + m.x17 - m.x21 - m.x22 - m.x23 == 0)

m.c9 = Constraint(expr=   m.x2 + m.x6 + m.x10 + m.x14 + m.x18 - m.x24 - m.x25 - m.x26 == 0)

m.c10 = Constraint(expr=   m.x3 + m.x7 + m.x11 + m.x15 + m.x19 - m.x27 - m.x28 - m.x29 == 0)

m.c11 = Constraint(expr=   m.x4 + m.x8 + m.x12 + m.x16 + m.x20 - m.x30 - m.x31 - m.x32 == 0)

m.c12 = Constraint(expr=-(m.x33*m.x21 + m.x33*m.x22 + m.x33*m.x23) + 0.13*m.x1 + 0.89*m.x5 + 0.69*m.x9 + 0.28*m.x13
                         + 0.35*m.x17 == 0)

m.c13 = Constraint(expr=-(m.x34*m.x21 + m.x34*m.x22 + m.x34*m.x23) + 0.87*m.x1 + 0.11*m.x5 + 0.31*m.x9 + 0.72*m.x13
                         + 0.65*m.x17 == 0)

m.c14 = Constraint(expr=-(m.x35*m.x24 + m.x35*m.x25 + m.x35*m.x26) + 0.13*m.x2 + 0.89*m.x6 + 0.69*m.x10 + 0.28*m.x14
                         + 0.35*m.x18 == 0)

m.c15 = Constraint(expr=-(m.x36*m.x24 + m.x36*m.x25 + m.x36*m.x26) + 0.87*m.x2 + 0.11*m.x6 + 0.31*m.x10 + 0.72*m.x14
                         + 0.65*m.x18 == 0)

m.c16 = Constraint(expr=-(m.x37*m.x27 + m.x37*m.x28 + m.x37*m.x29) + 0.13*m.x3 + 0.89*m.x7 + 0.69*m.x11 + 0.28*m.x15
                         + 0.35*m.x19 == 0)

m.c17 = Constraint(expr=-(m.x38*m.x27 + m.x38*m.x28 + m.x38*m.x29) + 0.87*m.x3 + 0.11*m.x7 + 0.31*m.x11 + 0.72*m.x15
                         + 0.65*m.x19 == 0)

m.c18 = Constraint(expr=-(m.x39*m.x30 + m.x39*m.x31 + m.x39*m.x32) + 0.13*m.x4 + 0.89*m.x8 + 0.69*m.x12 + 0.28*m.x16
                         + 0.35*m.x20 == 0)

m.c19 = Constraint(expr=-(m.x40*m.x30 + m.x40*m.x31 + m.x40*m.x32) + 0.87*m.x4 + 0.11*m.x8 + 0.31*m.x12 + 0.72*m.x16
                         + 0.65*m.x20 == 0)

m.c20 = Constraint(expr=0.56*m.x21 - (m.x33*m.x21 + m.x35*m.x24 + m.x37*m.x27 + m.x39*m.x30) + 0.56*m.x24 + 0.56*m.x27
                         + 0.56*m.x30 <= 0)

m.c21 = Constraint(expr=0.44*m.x21 - (m.x34*m.x21 + m.x36*m.x24 + m.x38*m.x27 + m.x40*m.x30) + 0.44*m.x24 + 0.44*m.x27
                         + 0.44*m.x30 <= 0)

m.c22 = Constraint(expr=0.3*m.x22 - (m.x33*m.x22 + m.x35*m.x25 + m.x37*m.x28 + m.x39*m.x31) + 0.3*m.x25 + 0.3*m.x28 + 
                        0.3*m.x31 <= 0)

m.c23 = Constraint(expr=0.7*m.x22 - (m.x34*m.x22 + m.x36*m.x25 + m.x38*m.x28 + m.x40*m.x31) + 0.7*m.x25 + 0.7*m.x28 + 
                        0.7*m.x31 <= 0)

m.c24 = Constraint(expr=0.41*m.x23 - (m.x33*m.x23 + m.x35*m.x26 + m.x37*m.x29 + m.x39*m.x32) + 0.41*m.x26 + 0.41*m.x29
                         + 0.41*m.x32 <= 0)

m.c25 = Constraint(expr=0.59*m.x23 - (m.x34*m.x23 + m.x36*m.x26 + m.x38*m.x29 + m.x40*m.x32) + 0.59*m.x26 + 0.59*m.x29
                         + 0.59*m.x32 <= 0)

m.c26 = Constraint(expr=m.x33*m.x21 + m.x35*m.x24 + m.x37*m.x27 + m.x39*m.x30 - 0.56*m.x21 - 0.56*m.x24 - 0.56*m.x27 - 
                        0.56*m.x30 <= 0)

m.c27 = Constraint(expr=m.x34*m.x21 + m.x36*m.x24 + m.x38*m.x27 + m.x40*m.x30 - 0.44*m.x21 - 0.44*m.x24 - 0.44*m.x27 - 
                        0.44*m.x30 <= 0)

m.c28 = Constraint(expr=m.x33*m.x22 + m.x35*m.x25 + m.x37*m.x28 + m.x39*m.x31 - 0.3*m.x22 - 0.3*m.x25 - 0.3*m.x28 - 0.3*
                        m.x31 <= 0)

m.c29 = Constraint(expr=m.x34*m.x22 + m.x36*m.x25 + m.x38*m.x28 + m.x40*m.x31 - 0.7*m.x22 - 0.7*m.x25 - 0.7*m.x28 - 0.7*
                        m.x31 <= 0)

m.c30 = Constraint(expr=m.x33*m.x23 + m.x35*m.x26 + m.x37*m.x29 + m.x39*m.x32 - 0.41*m.x23 - 0.41*m.x26 - 0.41*m.x29 - 
                        0.41*m.x32 <= 0)

m.c31 = Constraint(expr=m.x34*m.x23 + m.x36*m.x26 + m.x38*m.x29 + m.x40*m.x32 - 0.59*m.x23 - 0.59*m.x26 - 0.59*m.x29 - 
                        0.59*m.x32 <= 0)

m.c32 = Constraint(expr=   m.x1 - 686*m.b46 <= 0)

m.c33 = Constraint(expr=   m.x2 - 686*m.b47 <= 0)

m.c34 = Constraint(expr=   m.x3 - 686*m.b48 <= 0)

m.c35 = Constraint(expr=   m.x4 - 686*m.b49 <= 0)

m.c36 = Constraint(expr=   m.x5 - 686*m.b46 <= 0)

m.c37 = Constraint(expr=   m.x6 - 686*m.b47 <= 0)

m.c38 = Constraint(expr=   m.x7 - 686*m.b48 <= 0)

m.c39 = Constraint(expr=   m.x8 - 686*m.b49 <= 0)

m.c40 = Constraint(expr=   m.x9 - 686*m.b46 <= 0)

m.c41 = Constraint(expr=   m.x10 - 686*m.b47 <= 0)

m.c42 = Constraint(expr=   m.x11 - 686*m.b48 <= 0)

m.c43 = Constraint(expr=   m.x12 - 686*m.b49 <= 0)

m.c44 = Constraint(expr=   m.x13 - 686*m.b46 <= 0)

m.c45 = Constraint(expr=   m.x14 - 686*m.b47 <= 0)

m.c46 = Constraint(expr=   m.x15 - 686*m.b48 <= 0)

m.c47 = Constraint(expr=   m.x16 - 686*m.b49 <= 0)

m.c48 = Constraint(expr=   m.x17 - 686*m.b46 <= 0)

m.c49 = Constraint(expr=   m.x18 - 686*m.b47 <= 0)

m.c50 = Constraint(expr=   m.x19 - 686*m.b48 <= 0)

m.c51 = Constraint(expr=   m.x20 - 686*m.b49 <= 0)

m.c52 = Constraint(expr=   m.x1 - 686*m.b41 <= 0)

m.c53 = Constraint(expr=   m.x2 - 686*m.b41 <= 0)

m.c54 = Constraint(expr=   m.x3 - 686*m.b41 <= 0)

m.c55 = Constraint(expr=   m.x4 - 686*m.b41 <= 0)

m.c56 = Constraint(expr=   m.x5 - 686*m.b42 <= 0)

m.c57 = Constraint(expr=   m.x6 - 686*m.b42 <= 0)

m.c58 = Constraint(expr=   m.x7 - 686*m.b42 <= 0)

m.c59 = Constraint(expr=   m.x8 - 686*m.b42 <= 0)

m.c60 = Constraint(expr=   m.x9 - 686*m.b43 <= 0)

m.c61 = Constraint(expr=   m.x10 - 686*m.b43 <= 0)

m.c62 = Constraint(expr=   m.x11 - 686*m.b43 <= 0)

m.c63 = Constraint(expr=   m.x12 - 686*m.b43 <= 0)

m.c64 = Constraint(expr=   m.x13 - 686*m.b44 <= 0)

m.c65 = Constraint(expr=   m.x14 - 686*m.b44 <= 0)

m.c66 = Constraint(expr=   m.x15 - 686*m.b44 <= 0)

m.c67 = Constraint(expr=   m.x16 - 686*m.b44 <= 0)

m.c68 = Constraint(expr=   m.x17 - 686*m.b45 <= 0)

m.c69 = Constraint(expr=   m.x18 - 686*m.b45 <= 0)

m.c70 = Constraint(expr=   m.x19 - 686*m.b45 <= 0)

m.c71 = Constraint(expr=   m.x20 - 686*m.b45 <= 0)

m.c72 = Constraint(expr=   m.x21 - 229*m.b46 <= 0)

m.c73 = Constraint(expr=   m.x22 - 173*m.b46 <= 0)

m.c74 = Constraint(expr=   m.x23 - 284*m.b46 <= 0)

m.c75 = Constraint(expr=   m.x24 - 229*m.b47 <= 0)

m.c76 = Constraint(expr=   m.x25 - 173*m.b47 <= 0)

m.c77 = Constraint(expr=   m.x26 - 284*m.b47 <= 0)

m.c78 = Constraint(expr=   m.x27 - 229*m.b48 <= 0)

m.c79 = Constraint(expr=   m.x28 - 173*m.b48 <= 0)

m.c80 = Constraint(expr=   m.x29 - 284*m.b48 <= 0)

m.c81 = Constraint(expr=   m.x30 - 229*m.b49 <= 0)

m.c82 = Constraint(expr=   m.x31 - 173*m.b49 <= 0)

m.c83 = Constraint(expr=   m.x32 - 284*m.b49 <= 0)

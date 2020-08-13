#  MINLP written by GAMS Convert at 08/13/20 17:37:57
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         81       22       29       30        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         62       38       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        226      179       47        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0.0345)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=1.011)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=9.144)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.0095)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=1.1278)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
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

m.obj = Objective(expr=-325.08*m.x1**0*m.x2**0*m.x3**0.05*m.x4**0.533*m.x5**(-0.0822)*m.x12, sense=minimize)

m.c2 = Constraint(expr=-(16.00034*m.x1**0*m.x2**(-0.2344)*m.x3**0*m.x4**0*m.x5**0*m.x6 - 196.1292*m.x1**0.7464*m.x2**0*
                       m.x3**0*m.x4**0*m.x5**0.0243*m.x7) == 0)

m.c3 = Constraint(expr=-(196.1292*m.x1**0.7464*m.x2**0*m.x3**0*m.x4**0*m.x5**0.0243*m.x7 - 16.58544*m.x1**0*m.x2**0.7318
                       *m.x3**0*m.x4**0*m.x5**(-0.3941)*m.x8 - 0.012879*m.x1**0*m.x2**8.6107*m.x3**0*m.x4**0*m.x5**0*
                       m.x9) == 0)

m.c4 = Constraint(expr=-(16.58544*m.x1**0*m.x2**0.7318*m.x3**0*m.x4**0*m.x5**(-0.3941)*m.x8 - 3.78145609890476*m.x1**0*
                       m.x2**0*m.x3**0.6159*m.x4**0*m.x5**0.1308*m.x10 - 9.59175*m.x1**0*m.x2**0*m.x3**0.05*m.x4**0.533*
                       m.x5**(-0.0822)*m.x11) == 0)

m.c5 = Constraint(expr=-(7.56291219780952*m.x1**0*m.x2**0*m.x3**0.6159*m.x4**0*m.x5**0.1308*m.x10 - 325.08*m.x1**0*m.x2
                       **0*m.x3**0.05*m.x4**0.533*m.x5**(-0.0822)*m.x12) == 0)

m.c6 = Constraint(expr=-(-196.1292*m.x1**0.7464*m.x2**0*m.x3**0*m.x4**0*m.x5**0.0243*m.x7 - 16.58544*m.x1**0*m.x2**
                       0.7318*m.x3**0*m.x4**0*m.x5**(-0.3941)*m.x8 - 0.012879*m.x1**0*m.x2**8.6107*m.x3**0*m.x4**0*m.x5
                       **0*m.x9 + 7.56291219780952*m.x1**0*m.x2**0*m.x3**0.6159*m.x4**0*m.x5**0.1308*m.x10 + 325.08*m.x1
                       **0*m.x2**0*m.x3**0.05*m.x4**0.533*m.x5**(-0.0822)*m.x12 - 25.1*m.x1**0*m.x2**0*m.x3**0*m.x4**0*
                       m.x5**1*m.x13) == 0)

m.c7 = Constraint(expr=   m.x1 >= 0.00345)

m.c8 = Constraint(expr=   m.x2 >= 0.1011)

m.c9 = Constraint(expr=   m.x3 >= 0.9144)

m.c10 = Constraint(expr=   m.x4 >= 0.00095)

m.c11 = Constraint(expr=   m.x5 >= 0.11278)

m.c12 = Constraint(expr=   m.x1 <= 0.345)

m.c13 = Constraint(expr=   m.x2 <= 10.11)

m.c14 = Constraint(expr=   m.x3 <= 91.44)

m.c15 = Constraint(expr=   m.x4 <= 0.095)

m.c16 = Constraint(expr=   m.x5 <= 11.278)

m.c17 = Constraint(expr=   m.x6 - m.x14 - m.x22 - m.x30 == 0)

m.c18 = Constraint(expr=   m.x7 - m.x15 - m.x23 - m.x31 == 0)

m.c19 = Constraint(expr=   m.x8 - m.x16 - m.x24 - m.x32 == 0)

m.c20 = Constraint(expr=   m.x9 - m.x17 - m.x25 - m.x33 == 0)

m.c21 = Constraint(expr=   m.x10 - m.x18 - m.x26 - m.x34 == 0)

m.c22 = Constraint(expr=   m.x11 - m.x19 - m.x27 - m.x35 == 0)

m.c23 = Constraint(expr=   m.x12 - m.x20 - m.x28 - m.x36 == 0)

m.c24 = Constraint(expr=   m.x13 - m.x21 - m.x29 - m.x37 == 0)

m.c25 = Constraint(expr=   m.x14 - 0.2*m.b39 >= 0)

m.c26 = Constraint(expr=   m.x15 - 0.2*m.b40 >= 0)

m.c27 = Constraint(expr=   m.x16 - 0.2*m.b41 >= 0)

m.c28 = Constraint(expr=   m.x17 - 0.2*m.b42 >= 0)

m.c29 = Constraint(expr=   m.x18 - 0.2*m.b43 >= 0)

m.c30 = Constraint(expr=   m.x19 - 0.2*m.b44 >= 0)

m.c31 = Constraint(expr=   m.x20 - 0.2*m.b45 >= 0)

m.c32 = Constraint(expr=   m.x21 - 0.2*m.b46 >= 0)

m.c33 = Constraint(expr=   m.x14 - 0.999999995*m.b39 <= 0)

m.c34 = Constraint(expr=   m.x15 - 0.999999995*m.b40 <= 0)

m.c35 = Constraint(expr=   m.x16 - 0.999999995*m.b41 <= 0)

m.c36 = Constraint(expr=   m.x17 - 0.999999995*m.b42 <= 0)

m.c37 = Constraint(expr=   m.x18 - 0.999999995*m.b43 <= 0)

m.c38 = Constraint(expr=   m.x19 - 0.999999995*m.b44 <= 0)

m.c39 = Constraint(expr=   m.x20 - 0.999999995*m.b45 <= 0)

m.c40 = Constraint(expr=   m.x21 - 0.999999995*m.b46 <= 0)

m.c41 = Constraint(expr=   m.x22 - 0.999999995*m.b47 >= 0)

m.c42 = Constraint(expr=   m.x23 - 0.999999995*m.b48 >= 0)

m.c43 = Constraint(expr=   m.x24 - 0.999999995*m.b49 >= 0)

m.c44 = Constraint(expr=   m.x25 - 0.999999995*m.b50 >= 0)

m.c45 = Constraint(expr=   m.x26 - 0.999999995*m.b51 >= 0)

m.c46 = Constraint(expr=   m.x27 - 0.999999995*m.b52 >= 0)

m.c47 = Constraint(expr=   m.x28 - 0.999999995*m.b53 >= 0)

m.c48 = Constraint(expr=   m.x29 - 0.999999995*m.b54 >= 0)

m.c49 = Constraint(expr=   m.x22 - 1.000000005*m.b47 <= 0)

m.c50 = Constraint(expr=   m.x23 - 1.000000005*m.b48 <= 0)

m.c51 = Constraint(expr=   m.x24 - 1.000000005*m.b49 <= 0)

m.c52 = Constraint(expr=   m.x25 - 1.000000005*m.b50 <= 0)

m.c53 = Constraint(expr=   m.x26 - 1.000000005*m.b51 <= 0)

m.c54 = Constraint(expr=   m.x27 - 1.000000005*m.b52 <= 0)

m.c55 = Constraint(expr=   m.x28 - 1.000000005*m.b53 <= 0)

m.c56 = Constraint(expr=   m.x29 - 1.000000005*m.b54 <= 0)

m.c57 = Constraint(expr=   m.x30 - 1.000000005*m.b55 >= 0)

m.c58 = Constraint(expr=   m.x31 - 1.000000005*m.b56 >= 0)

m.c59 = Constraint(expr=   m.x32 - 1.000000005*m.b57 >= 0)

m.c60 = Constraint(expr=   m.x33 - 1.000000005*m.b58 >= 0)

m.c61 = Constraint(expr=   m.x34 - 1.000000005*m.b59 >= 0)

m.c62 = Constraint(expr=   m.x35 - 1.000000005*m.b60 >= 0)

m.c63 = Constraint(expr=   m.x36 - 1.000000005*m.b61 >= 0)

m.c64 = Constraint(expr=   m.x37 - 1.000000005*m.b62 >= 0)

m.c65 = Constraint(expr=   m.x30 - 5*m.b55 <= 0)

m.c66 = Constraint(expr=   m.x31 - 5*m.b56 <= 0)

m.c67 = Constraint(expr=   m.x32 - 5*m.b57 <= 0)

m.c68 = Constraint(expr=   m.x33 - 5*m.b58 <= 0)

m.c69 = Constraint(expr=   m.x34 - 5*m.b59 <= 0)

m.c70 = Constraint(expr=   m.x35 - 5*m.b60 <= 0)

m.c71 = Constraint(expr=   m.x36 - 5*m.b61 <= 0)

m.c72 = Constraint(expr=   m.x37 - 5*m.b62 <= 0)

m.c73 = Constraint(expr=   m.b39 + m.b47 + m.b55 == 1)

m.c74 = Constraint(expr=   m.b40 + m.b48 + m.b56 == 1)

m.c75 = Constraint(expr=   m.b41 + m.b49 + m.b57 == 1)

m.c76 = Constraint(expr=   m.b42 + m.b50 + m.b58 == 1)

m.c77 = Constraint(expr=   m.b43 + m.b51 + m.b59 == 1)

m.c78 = Constraint(expr=   m.b44 + m.b52 + m.b60 == 1)

m.c79 = Constraint(expr=   m.b45 + m.b53 + m.b61 == 1)

m.c80 = Constraint(expr=   m.b46 + m.b54 + m.b62 == 1)

m.c81 = Constraint(expr=   m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b55 + m.b56 + m.b57 + m.b58
                         + m.b59 + m.b60 + m.b61 + m.b62 <= 8)

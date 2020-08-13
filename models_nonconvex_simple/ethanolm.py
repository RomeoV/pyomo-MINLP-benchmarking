#  MINLP written by GAMS Convert at 08/13/20 17:37:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         73       14       13       46        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         38       14       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        178      131       47        0
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
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)

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

m.c17 = Constraint(expr=   m.x6 + 100000*m.b15 <= 100000.999999995)

m.c18 = Constraint(expr=   m.x7 + 100000*m.b16 <= 100000.999999995)

m.c19 = Constraint(expr=   m.x8 + 100000*m.b17 <= 100000.999999995)

m.c20 = Constraint(expr=   m.x9 + 100000*m.b18 <= 100000.999999995)

m.c21 = Constraint(expr=   m.x10 + 100000*m.b19 <= 100000.999999995)

m.c22 = Constraint(expr=   m.x11 + 100000*m.b20 <= 100000.999999995)

m.c23 = Constraint(expr=   m.x12 + 100000*m.b21 <= 100000.999999995)

m.c24 = Constraint(expr=   m.x13 + 100000*m.b22 <= 100000.999999995)

m.c25 = Constraint(expr= - m.x6 + 100000*m.b23 <= 99999.000000005)

m.c26 = Constraint(expr= - m.x7 + 100000*m.b24 <= 99999.000000005)

m.c27 = Constraint(expr= - m.x8 + 100000*m.b25 <= 99999.000000005)

m.c28 = Constraint(expr= - m.x9 + 100000*m.b26 <= 99999.000000005)

m.c29 = Constraint(expr= - m.x10 + 100000*m.b27 <= 99999.000000005)

m.c30 = Constraint(expr= - m.x11 + 100000*m.b28 <= 99999.000000005)

m.c31 = Constraint(expr= - m.x12 + 100000*m.b29 <= 99999.000000005)

m.c32 = Constraint(expr= - m.x13 + 100000*m.b30 <= 99999.000000005)

m.c33 = Constraint(expr=   m.x6 + 100000*m.b23 <= 100001.000000005)

m.c34 = Constraint(expr=   m.x7 + 100000*m.b24 <= 100001.000000005)

m.c35 = Constraint(expr=   m.x8 + 100000*m.b25 <= 100001.000000005)

m.c36 = Constraint(expr=   m.x9 + 100000*m.b26 <= 100001.000000005)

m.c37 = Constraint(expr=   m.x10 + 100000*m.b27 <= 100001.000000005)

m.c38 = Constraint(expr=   m.x11 + 100000*m.b28 <= 100001.000000005)

m.c39 = Constraint(expr=   m.x12 + 100000*m.b29 <= 100001.000000005)

m.c40 = Constraint(expr=   m.x13 + 100000*m.b30 <= 100001.000000005)

m.c41 = Constraint(expr= - m.x6 + 100000*m.b31 <= 99998.999999995)

m.c42 = Constraint(expr= - m.x7 + 100000*m.b32 <= 99998.999999995)

m.c43 = Constraint(expr= - m.x8 + 100000*m.b33 <= 99998.999999995)

m.c44 = Constraint(expr= - m.x9 + 100000*m.b34 <= 99998.999999995)

m.c45 = Constraint(expr= - m.x10 + 100000*m.b35 <= 99998.999999995)

m.c46 = Constraint(expr= - m.x11 + 100000*m.b36 <= 99998.999999995)

m.c47 = Constraint(expr= - m.x12 + 100000*m.b37 <= 99998.999999995)

m.c48 = Constraint(expr= - m.x13 + 100000*m.b38 <= 99998.999999995)

m.c49 = Constraint(expr=   m.x6 >= 0.2)

m.c50 = Constraint(expr=   m.x7 >= 0.2)

m.c51 = Constraint(expr=   m.x8 >= 0.2)

m.c52 = Constraint(expr=   m.x9 >= 0.2)

m.c53 = Constraint(expr=   m.x10 >= 0.2)

m.c54 = Constraint(expr=   m.x11 >= 0.2)

m.c55 = Constraint(expr=   m.x12 >= 0.2)

m.c56 = Constraint(expr=   m.x13 >= 0.2)

m.c57 = Constraint(expr=   m.x6 <= 5)

m.c58 = Constraint(expr=   m.x7 <= 5)

m.c59 = Constraint(expr=   m.x8 <= 5)

m.c60 = Constraint(expr=   m.x9 <= 5)

m.c61 = Constraint(expr=   m.x10 <= 5)

m.c62 = Constraint(expr=   m.x11 <= 5)

m.c63 = Constraint(expr=   m.x12 <= 5)

m.c64 = Constraint(expr=   m.x13 <= 5)

m.c65 = Constraint(expr=   m.b15 + m.b23 + m.b31 == 1)

m.c66 = Constraint(expr=   m.b16 + m.b24 + m.b32 == 1)

m.c67 = Constraint(expr=   m.b17 + m.b25 + m.b33 == 1)

m.c68 = Constraint(expr=   m.b18 + m.b26 + m.b34 == 1)

m.c69 = Constraint(expr=   m.b19 + m.b27 + m.b35 == 1)

m.c70 = Constraint(expr=   m.b20 + m.b28 + m.b36 == 1)

m.c71 = Constraint(expr=   m.b21 + m.b29 + m.b37 == 1)

m.c72 = Constraint(expr=   m.b22 + m.b30 + m.b38 == 1)

m.c73 = Constraint(expr=   m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b31 + m.b32 + m.b33 + m.b34
                         + m.b35 + m.b36 + m.b37 + m.b38 <= 8)

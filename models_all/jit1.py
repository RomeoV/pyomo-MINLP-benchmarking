#  MINLP written by GAMS Convert at 05/15/20 00:50:51
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         33       13       18        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         26       22        0        4        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        112      100       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i2 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i3 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i4 = Var(within=Integers,bounds=(1,None),initialize=1)
m.x5 = Var(within=Reals,bounds=(0.000252525252525253,None),initialize=0.000252525252525253)
m.x6 = Var(within=Reals,bounds=(0.000508388408744281,None),initialize=0.000508388408744281)
m.x7 = Var(within=Reals,bounds=(0.000635162601626016,None),initialize=0.000635162601626016)
m.x8 = Var(within=Reals,bounds=(0.000636456211812627,None),initialize=0.000636456211812627)
m.x9 = Var(within=Reals,bounds=(0.000861450107681263,None),initialize=0.000861450107681263)
m.x10 = Var(within=Reals,bounds=(0.000438212094653812,None),initialize=0.000438212094653812)
m.x11 = Var(within=Reals,bounds=(0.000433776749566223,None),initialize=0.000433776749566223)
m.x12 = Var(within=Reals,bounds=(0.000289184499710815,None),initialize=0.000289184499710815)
m.x13 = Var(within=Reals,bounds=(0.000224466891133558,None),initialize=0.000224466891133558)
m.x14 = Var(within=Reals,bounds=(0.00033892560582952,None),initialize=0.00033892560582952)
m.x15 = Var(within=Reals,bounds=(0.000224014336917563,None),initialize=0.000224014336917563)
m.x16 = Var(within=Reals,bounds=(0.000337381916329285,None),initialize=0.000337381916329285)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=7.5/m.x5 + 5.625/m.x6 + 11.25/m.x7 + 7.5/m.x8 + 8.57142857142857/m.x9 + 7.14285714285714/m.x10 + 
                       2.85714285714286/m.x11 + 5.71428571428571/m.x12 + 8.88888888888889/m.x13 + 8.88888888888889/m.x14
                        + 8.88888888888889/m.x15 + 4.44444444444444/m.x16 + 5000*m.i1 + 5500*m.i2 + 4000*m.i3
                        + 6000*m.i4 + 6000000*m.x17 + 9000000*m.x18 + 6000000*m.x19 + 9000000*m.x20 + 8000000*m.x21
                        + 8000000*m.x22 + 8000000*m.x23 + 10000000*m.x24 + 8000000*m.x25, sense=minimize)

m.c2 = Constraint(expr= - 0.000252525252525253*m.i1 + m.x5 == 0)

m.c3 = Constraint(expr= - 0.000508388408744281*m.i2 + m.x6 == 0)

m.c4 = Constraint(expr= - 0.000635162601626016*m.i3 + m.x7 == 0)

m.c5 = Constraint(expr= - 0.000636456211812627*m.i4 + m.x8 == 0)

m.c6 = Constraint(expr= - 0.000861450107681263*m.i1 + m.x9 == 0)

m.c7 = Constraint(expr= - 0.000438212094653812*m.i2 + m.x10 == 0)

m.c8 = Constraint(expr= - 0.000433776749566223*m.i3 + m.x11 == 0)

m.c9 = Constraint(expr= - 0.000289184499710815*m.i4 + m.x12 == 0)

m.c10 = Constraint(expr= - 0.000224466891133558*m.i1 + m.x13 == 0)

m.c11 = Constraint(expr= - 0.00033892560582952*m.i2 + m.x14 == 0)

m.c12 = Constraint(expr= - 0.000224014336917563*m.i3 + m.x15 == 0)

m.c13 = Constraint(expr= - 0.000337381916329285*m.i4 + m.x16 == 0)

m.c14 = Constraint(expr=   5000*m.i1 + 5500*m.i2 + 4000*m.i3 + 6000*m.i4 <= 6000000)

m.c15 = Constraint(expr=   60*m.i1 + 50*m.i2 + 80*m.i3 + 40*m.i4 <= 3000)

m.c16 = Constraint(expr= - m.x5 + m.x6 + m.x17 >= 0)

m.c17 = Constraint(expr= - m.x6 + m.x7 + m.x18 >= 0)

m.c18 = Constraint(expr= - m.x7 + m.x8 + m.x19 >= 0)

m.c19 = Constraint(expr= - m.x9 + m.x10 + m.x20 >= 0)

m.c20 = Constraint(expr= - m.x10 + m.x11 + m.x21 >= 0)

m.c21 = Constraint(expr= - m.x11 + m.x12 + m.x22 >= 0)

m.c22 = Constraint(expr= - m.x13 + m.x14 + m.x23 >= 0)

m.c23 = Constraint(expr= - m.x14 + m.x15 + m.x24 >= 0)

m.c24 = Constraint(expr= - m.x15 + m.x16 + m.x25 >= 0)

m.c25 = Constraint(expr=   m.x5 - m.x6 + m.x17 >= 0)

m.c26 = Constraint(expr=   m.x6 - m.x7 + m.x18 >= 0)

m.c27 = Constraint(expr=   m.x7 - m.x8 + m.x19 >= 0)

m.c28 = Constraint(expr=   m.x9 - m.x10 + m.x20 >= 0)

m.c29 = Constraint(expr=   m.x10 - m.x11 + m.x21 >= 0)

m.c30 = Constraint(expr=   m.x11 - m.x12 + m.x22 >= 0)

m.c31 = Constraint(expr=   m.x13 - m.x14 + m.x23 >= 0)

m.c32 = Constraint(expr=   m.x14 - m.x15 + m.x24 >= 0)

m.c33 = Constraint(expr=   m.x15 - m.x16 + m.x25 >= 0)

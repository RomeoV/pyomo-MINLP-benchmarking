#  MINLP written by GAMS Convert at 08/13/20 17:37:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         40       16        6       18        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         33       26        7        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        131      115       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x9 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x10 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x11 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x12 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x13 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x14 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x15 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x16 = Var(within=Reals,bounds=(0.01,1000),initialize=0.01)
m.x17 = Var(within=Reals,bounds=(0,1620),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1620),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,360),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,360),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1980),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1620),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,360),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x26 = Var(within=Reals,bounds=(350,600),initialize=350)
m.x27 = Var(within=Reals,bounds=(0,430),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,368),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,600),initialize=0)

m.obj = Objective(expr=670*(m.x17/(0.5*(m.x8**2*m.x9 + m.x9**2*m.x8))**0.333333333333333)**0.83 + 670*(m.x18/(0.5*(m.x9
                       **2*m.x10 + m.x10**2*m.x9))**0.333333333333333)**0.83 + 670*(0.5*m.x19/(0.5*(m.x11**2*m.x12 + 
                       m.x12**2*m.x11))**0.333333333333333)**0.83 + 670*(0.5*m.x20/(0.5*(m.x12**2*m.x13 + m.x13**2*m.x12
                       ))**0.333333333333333)**0.83 + 670*(0.666666666666667*m.x21/(1250*m.x14**2)**0.333333333333333)**
                       0.83 + 20*m.x21 + 670*(0.666666666666667*m.x22/(2450*m.x15**2)**0.333333333333333)**0.83 + 120*
                       m.x22 + 670*(0.4*m.x23/(8712*m.x16**2)**0.333333333333333)**0.83 + 120*m.x23 + 6600*m.b1
                        + 6600*m.b2 + 6600*m.b3 + 6600*m.b4 + 6600*m.b5 + 6600*m.b6 + 6600*m.b7, sense=minimize)

m.c1 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 + m.x21 == 1980)

m.c2 = Constraint(expr=   m.x17 + m.x18 + m.x22 == 1620)

m.c3 = Constraint(expr=   m.x19 + m.x20 + m.x23 == 360)

m.c4 = Constraint(expr= - m.x17 - m.x19 + 22*m.x24 - 22*m.x25 == 0)

m.c5 = Constraint(expr= - m.x18 - m.x20 + 22*m.x25 - 22*m.x26 == 0)

m.c6 = Constraint(expr= - m.x17 + 20*m.x27 - 20*m.x28 == 0)

m.c7 = Constraint(expr= - m.x18 + 20*m.x28 - 20*m.x29 == 0)

m.c8 = Constraint(expr= - m.x19 + 7.5*m.x30 - 7.5*m.x31 == 0)

m.c9 = Constraint(expr= - m.x20 + 7.5*m.x31 - 7.5*m.x32 == 0)

m.c10 = Constraint(expr=   m.x24 == 440)

m.c11 = Constraint(expr=   m.x29 == 349)

m.c12 = Constraint(expr=   m.x32 == 320)

m.c13 = Constraint(expr=   m.x24 - m.x25 >= 0)

m.c14 = Constraint(expr=   m.x25 - m.x26 >= 0)

m.c15 = Constraint(expr=   m.x27 - m.x28 >= 0)

m.c16 = Constraint(expr=   m.x28 - m.x29 >= 0)

m.c17 = Constraint(expr=   m.x30 - m.x31 >= 0)

m.c18 = Constraint(expr=   m.x31 - m.x32 >= 0)

m.c19 = Constraint(expr= - m.x21 + 22*m.x26 == 7700)

m.c20 = Constraint(expr= - m.x22 - 20*m.x27 == -8600)

m.c21 = Constraint(expr= - m.x23 - 7.5*m.x30 == -2760)

m.c22 = Constraint(expr= - 1620*m.b1 + m.x17 <= 0)

m.c23 = Constraint(expr= - 1620*m.b2 + m.x18 <= 0)

m.c24 = Constraint(expr= - 360*m.b3 + m.x19 <= 0)

m.c25 = Constraint(expr= - 360*m.b4 + m.x20 <= 0)

m.c26 = Constraint(expr= - 1980*m.b5 + m.x21 <= 0)

m.c27 = Constraint(expr= - 1620*m.b6 + m.x22 <= 0)

m.c28 = Constraint(expr= - 360*m.b7 + m.x23 <= 0)

m.c29 = Constraint(expr=   200*m.b1 + m.x8 - m.x24 + m.x27 <= 200)

m.c30 = Constraint(expr=   200*m.b2 + m.x9 - m.x25 + m.x28 <= 200)

m.c31 = Constraint(expr=   200*m.b3 + m.x11 - m.x24 + m.x30 <= 200)

m.c32 = Constraint(expr=   200*m.b4 + m.x12 - m.x25 + m.x31 <= 200)

m.c33 = Constraint(expr=   200*m.b1 + m.x9 - m.x25 + m.x28 <= 200)

m.c34 = Constraint(expr=   200*m.b2 + m.x10 - m.x26 + m.x29 <= 200)

m.c35 = Constraint(expr=   200*m.b3 + m.x12 - m.x25 + m.x31 <= 200)

m.c36 = Constraint(expr=   200*m.b4 + m.x13 - m.x26 + m.x32 <= 200)

m.c37 = Constraint(expr=   200*m.b5 + m.x14 - m.x26 <= -120)

m.c38 = Constraint(expr=   200*m.b6 + m.x15 + m.x27 <= 700)

m.c39 = Constraint(expr=   200*m.b7 + m.x16 + m.x30 <= 700)

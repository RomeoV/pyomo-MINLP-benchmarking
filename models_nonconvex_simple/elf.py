#  MINLP written by GAMS Convert at 08/13/20 17:37:53
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         39        7       32        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         55       31       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        178      148       30        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0.33)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=   m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36
                        + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48
                       , sense=minimize)

m.c1 = Constraint(expr=-(8 - m.x49)**2 - 100*m.b1 + m.x25 >= -100)

m.c2 = Constraint(expr=-(8 - m.x50)**2 - 100*m.b2 + m.x26 >= -100)

m.c3 = Constraint(expr=-(8 - m.x51)**2 - 100*m.b3 + m.x27 >= -100)

m.c4 = Constraint(expr=-(8.5 - m.x49)**2 - 100*m.b4 + m.x28 >= -100)

m.c5 = Constraint(expr=-(8.5 - m.x50)**2 - 100*m.b5 + m.x29 >= -100)

m.c6 = Constraint(expr=-(8.5 - m.x51)**2 - 100*m.b6 + m.x30 >= -100)

m.c7 = Constraint(expr=-(8.3 - m.x49)**2 - 100*m.b7 + m.x31 >= -100)

m.c8 = Constraint(expr=-(8.3 - m.x50)**2 - 100*m.b8 + m.x32 >= -100)

m.c9 = Constraint(expr=-(8.3 - m.x51)**2 - 100*m.b9 + m.x33 >= -100)

m.c10 = Constraint(expr=-(8.7 - m.x49)**2 - 100*m.b10 + m.x34 >= -100)

m.c11 = Constraint(expr=-(8.7 - m.x50)**2 - 100*m.b11 + m.x35 >= -100)

m.c12 = Constraint(expr=-(8.7 - m.x51)**2 - 100*m.b12 + m.x36 >= -100)

m.c13 = Constraint(expr=-(8.6 - m.x49)**2 - 100*m.b13 + m.x37 >= -100)

m.c14 = Constraint(expr=-(8.6 - m.x50)**2 - 100*m.b14 + m.x38 >= -100)

m.c15 = Constraint(expr=-(8.6 - m.x51)**2 - 100*m.b15 + m.x39 >= -100)

m.c16 = Constraint(expr=-(9 - m.x49)**2 - 100*m.b16 + m.x40 >= -100)

m.c17 = Constraint(expr=-(9 - m.x50)**2 - 100*m.b17 + m.x41 >= -100)

m.c18 = Constraint(expr=-(9 - m.x51)**2 - 100*m.b18 + m.x42 >= -100)

m.c19 = Constraint(expr=-(9.2 - m.x49)**2 - 100*m.b19 + m.x43 >= -100)

m.c20 = Constraint(expr=-(9.2 - m.x50)**2 - 100*m.b20 + m.x44 >= -100)

m.c21 = Constraint(expr=-(9.2 - m.x51)**2 - 100*m.b21 + m.x45 >= -100)

m.c22 = Constraint(expr=-(9.5 - m.x49)**2 - 100*m.b22 + m.x46 >= -100)

m.c23 = Constraint(expr=-(9.5 - m.x50)**2 - 100*m.b23 + m.x47 >= -100)

m.c24 = Constraint(expr=-(9.5 - m.x51)**2 - 100*m.b24 + m.x48 >= -100)

m.c25 = Constraint(expr=   m.b1 + m.b2 + m.b3 >= 1)

m.c26 = Constraint(expr=   m.b4 + m.b5 + m.b6 >= 1)

m.c27 = Constraint(expr=   m.b7 + m.b8 + m.b9 >= 1)

m.c28 = Constraint(expr=   m.b10 + m.b11 + m.b12 >= 1)

m.c29 = Constraint(expr=   m.b13 + m.b14 + m.b15 >= 1)

m.c30 = Constraint(expr=   m.b16 + m.b17 + m.b18 >= 1)

m.c31 = Constraint(expr=   m.b19 + m.b20 + m.b21 >= 1)

m.c32 = Constraint(expr=   m.b22 + m.b23 + m.b24 >= 1)

m.c33 = Constraint(expr= - m.b1 - m.b4 - m.b7 - m.b10 - m.b13 - m.b16 - m.b19 - m.b22 + m.x52 == 0)

m.c34 = Constraint(expr= - m.b2 - m.b5 - m.b8 - m.b11 - m.b14 - m.b17 - m.b20 - m.b23 + m.x53 == 0)

m.c35 = Constraint(expr= - m.b3 - m.b6 - m.b9 - m.b12 - m.b15 - m.b18 - m.b21 - m.b24 + m.x54 == 0)

m.c36 = Constraint(expr=m.x52*m.x49 - 8*m.b1 - 8.5*m.b4 - 8.3*m.b7 - 8.7*m.b10 - 8.6*m.b13 - 9*m.b16 - 9.2*m.b19
                         - 9.5*m.b22 == 0)

m.c37 = Constraint(expr=m.x53*m.x50 - 8*m.b2 - 8.5*m.b5 - 8.3*m.b8 - 8.7*m.b11 - 8.6*m.b14 - 9*m.b17 - 9.2*m.b20
                         - 9.5*m.b23 == 0)

m.c38 = Constraint(expr=m.x54*m.x51 - 8*m.b3 - 8.5*m.b6 - 8.3*m.b9 - 8.7*m.b12 - 8.6*m.b15 - 9*m.b18 - 9.2*m.b21
                         - 9.5*m.b24 == 0)

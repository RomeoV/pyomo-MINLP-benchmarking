#  MINLP written by GAMS Convert at 08/13/20 17:37:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        1        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         17        1       16        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17        1       16        0


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
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x17, sense=maximize)

m.c1 = Constraint(expr=m.b1*m.b6*m.b11*m.b16 - m.b1*m.b6*m.b12*m.b15 + m.b1*m.b8*m.b10*m.b15 - m.b4*m.b5*m.b10*m.b15 + 
                       m.b4*m.b5*m.b11*m.b14 - m.b1*m.b8*m.b11*m.b14 + m.b1*m.b7*m.b12*m.b14 - m.b1*m.b7*m.b10*m.b16 + 
                       m.b3*m.b5*m.b10*m.b16 - m.b3*m.b5*m.b12*m.b14 + m.b3*m.b8*m.b9*m.b14 - m.b4*m.b7*m.b9*m.b14 + 
                       m.b4*m.b7*m.b10*m.b13 - m.b3*m.b8*m.b10*m.b13 + m.b3*m.b6*m.b12*m.b13 - m.b3*m.b6*m.b9*m.b16 + 
                       m.b2*m.b7*m.b9*m.b16 - m.b2*m.b7*m.b12*m.b13 + m.b2*m.b8*m.b11*m.b13 - m.b4*m.b6*m.b11*m.b13 + 
                       m.b4*m.b6*m.b9*m.b15 - m.b2*m.b8*m.b9*m.b15 + m.b2*m.b5*m.b12*m.b15 - m.b2*m.b5*m.b11*m.b16
                        - m.x17 >= 0)

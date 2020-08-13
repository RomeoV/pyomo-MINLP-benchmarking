#  MINLP written by GAMS Convert at 08/13/20 17:37:50
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         46        1       45        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         46        1       45        0


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
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x46, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b14 - 2*m.b1 - 4*m.b14 + 2*m.b1*m.b34 + 2*m.b1*m.b35 - 2*m.b1*m.b39 + 2*m.b2*m.b3 - 2*
                       m.b2 - 2*m.b3 + 2*m.b2*m.b31 - 4*m.b31 + 2*m.b3*m.b4 - 2*m.b4 + 2*m.b3*m.b8 - 4*m.b8 - 2*m.b3*
                       m.b43 + 2*m.b4*m.b9 - 4*m.b9 + 2*m.b5*m.b7 - 2*m.b5 - 4*m.b7 + 2*m.b5*m.b11 - 2*m.b11 + 2*m.b6*
                       m.b7 - 2*m.b6 + 2*m.b6*m.b11 + 2*m.b7*m.b13 - 2*m.b13 + 2*m.b7*m.b42 + 2*m.b8*m.b19 - 4*m.b19 + 2
                       *m.b8*m.b28 - 2*m.b28 + 2*m.b8*m.b44 + 2*m.b9*m.b10 - 2*m.b10 + 2*m.b9*m.b18 - 2*m.b18 + 2*m.b9*
                       m.b43 + 2*m.b10*m.b19 + 2*m.b11*m.b36 - 2*m.b11*m.b40 - 2*m.b12*m.b13 + 2*m.b12 - 2*m.b12*m.b38
                        + 2*m.b12*m.b40 - 2*m.b12*m.b45 + 2*m.b13*m.b14 + 2*m.b13*m.b25 - 2*m.b25 + 2*m.b14*m.b16 - 2*
                       m.b16 + 2*m.b14*m.b40 - 2*m.b15*m.b17 - 2*m.b15 - 2*m.b17 + 2*m.b15*m.b25 + 2*m.b15*m.b35 + 2*
                       m.b15*m.b41 + 2*m.b16*m.b17 + 2*m.b16*m.b26 - 2*m.b26 - 2*m.b16*m.b44 + 2*m.b17*m.b18 + 2*m.b17*
                       m.b43 + 2*m.b18*m.b30 - 2*m.b30 - 2*m.b18*m.b35 + 2*m.b19*m.b20 - 2*m.b20 + 2*m.b19*m.b29 - 2*
                       m.b29 + 2*m.b20*m.b30 - 2*m.b21*m.b22 + 2*m.b21 + 2*m.b22 - 2*m.b21*m.b23 - 2*m.b23 - 2*m.b22*
                       m.b24 - 2*m.b24 - 2*m.b22*m.b36 + 2*m.b22*m.b38 + 2*m.b23*m.b24 + 2*m.b23*m.b42 + 2*m.b23*m.b45
                        + 2*m.b24*m.b26 + 2*m.b24*m.b39 - 2*m.b25*m.b27 - 2*m.b27 + 2*m.b25*m.b36 + 2*m.b26*m.b27 - 2*
                       m.b26*m.b42 + 2*m.b27*m.b28 + 2*m.b27*m.b44 + 2*m.b28*m.b29 - 2*m.b28*m.b37 + 2*m.b29*m.b31 - 2*
                       m.b29*m.b34 + 2*m.b30*m.b32 - 2*m.b32 - 2*m.b30*m.b33 + 2*m.b31*m.b32 + 2*m.b31*m.b33 + 2*m.b33*
                       m.b34 - 2*m.b33*m.b35 - 2*m.b34*m.b37 - 2*m.b36*m.b41 + 2*m.b37*m.b39 + 2*m.b37*m.b41 - 2*m.b39*
                       m.b40 - 2*m.b41*m.b42 - 2*m.b43*m.b44 + m.x46 <= 0)

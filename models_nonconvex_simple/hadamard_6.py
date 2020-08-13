#  MINLP written by GAMS Convert at 08/13/20 17:37:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        1        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         37        1       36        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         37        1       36        0


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
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x37, sense=maximize)

m.c1 = Constraint(expr=m.b1*m.b8*m.b15*m.b22*m.b29*m.b36 - m.b1*m.b8*m.b15*m.b22*m.b30*m.b35 + m.b1*m.b8*m.b15*m.b24*
                       m.b28*m.b35 - m.b1*m.b8*m.b18*m.b21*m.b28*m.b35 + m.b1*m.b12*m.b14*m.b21*m.b28*m.b35 - m.b6*m.b7*
                       m.b14*m.b21*m.b28*m.b35 + m.b6*m.b7*m.b14*m.b21*m.b29*m.b34 - m.b1*m.b12*m.b14*m.b21*m.b29*m.b34
                        + m.b1*m.b8*m.b18*m.b21*m.b29*m.b34 - m.b1*m.b8*m.b15*m.b24*m.b29*m.b34 + m.b1*m.b8*m.b15*m.b23*
                       m.b30*m.b34 - m.b1*m.b8*m.b15*m.b23*m.b28*m.b36 + m.b1*m.b8*m.b17*m.b21*m.b28*m.b36 - m.b1*m.b8*
                       m.b17*m.b21*m.b30*m.b34 + m.b1*m.b8*m.b17*m.b24*m.b27*m.b34 - m.b1*m.b8*m.b18*m.b23*m.b27*m.b34
                        + m.b1*m.b12*m.b14*m.b23*m.b27*m.b34 - m.b6*m.b7*m.b14*m.b23*m.b27*m.b34 + m.b6*m.b7*m.b17*m.b20
                       *m.b27*m.b34 - m.b1*m.b12*m.b17*m.b20*m.b27*m.b34 + m.b1*m.b11*m.b18*m.b20*m.b27*m.b34 - m.b1*
                       m.b11*m.b14*m.b24*m.b27*m.b34 + m.b1*m.b11*m.b14*m.b21*m.b30*m.b34 - m.b1*m.b11*m.b14*m.b21*m.b28
                       *m.b36 + m.b5*m.b7*m.b14*m.b21*m.b28*m.b36 - m.b5*m.b7*m.b14*m.b21*m.b30*m.b34 + m.b5*m.b7*m.b14*
                       m.b24*m.b27*m.b34 - m.b5*m.b7*m.b18*m.b20*m.b27*m.b34 + m.b5*m.b12*m.b13*m.b20*m.b27*m.b34 - m.b6
                       *m.b11*m.b13*m.b20*m.b27*m.b34 + m.b6*m.b11*m.b13*m.b20*m.b28*m.b33 - m.b5*m.b12*m.b13*m.b20*
                       m.b28*m.b33 + m.b5*m.b7*m.b18*m.b20*m.b28*m.b33 - m.b5*m.b7*m.b14*m.b24*m.b28*m.b33 + m.b5*m.b7*
                       m.b14*m.b22*m.b30*m.b33 - m.b5*m.b7*m.b14*m.b22*m.b27*m.b36 + m.b1*m.b11*m.b14*m.b22*m.b27*m.b36
                        - m.b1*m.b11*m.b14*m.b22*m.b30*m.b33 + m.b1*m.b11*m.b14*m.b24*m.b28*m.b33 - m.b1*m.b11*m.b18*
                       m.b20*m.b28*m.b33 + m.b1*m.b12*m.b17*m.b20*m.b28*m.b33 - m.b6*m.b7*m.b17*m.b20*m.b28*m.b33 + m.b6
                       *m.b7*m.b14*m.b23*m.b28*m.b33 - m.b1*m.b12*m.b14*m.b23*m.b28*m.b33 + m.b1*m.b8*m.b18*m.b23*m.b28*
                       m.b33 - m.b1*m.b8*m.b17*m.b24*m.b28*m.b33 + m.b1*m.b8*m.b17*m.b22*m.b30*m.b33 - m.b1*m.b8*m.b17*
                       m.b22*m.b27*m.b36 + m.b1*m.b8*m.b16*m.b23*m.b27*m.b36 - m.b1*m.b8*m.b16*m.b23*m.b30*m.b33 + m.b1*
                       m.b8*m.b16*m.b24*m.b29*m.b33 - m.b1*m.b8*m.b18*m.b22*m.b29*m.b33 + m.b1*m.b12*m.b14*m.b22*m.b29*
                       m.b33 - m.b6*m.b7*m.b14*m.b22*m.b29*m.b33 + m.b6*m.b7*m.b14*m.b22*m.b27*m.b35 - m.b1*m.b12*m.b14*
                       m.b22*m.b27*m.b35 + m.b1*m.b8*m.b18*m.b22*m.b27*m.b35 - m.b1*m.b8*m.b16*m.b24*m.b27*m.b35 + m.b1*
                       m.b8*m.b16*m.b21*m.b30*m.b35 - m.b1*m.b8*m.b16*m.b21*m.b29*m.b36 + m.b1*m.b10*m.b14*m.b21*m.b29*
                       m.b36 - m.b1*m.b10*m.b14*m.b21*m.b30*m.b35 + m.b1*m.b10*m.b14*m.b24*m.b27*m.b35 - m.b1*m.b10*
                       m.b18*m.b20*m.b27*m.b35 + m.b1*m.b12*m.b16*m.b20*m.b27*m.b35 - m.b6*m.b7*m.b16*m.b20*m.b27*m.b35
                        + m.b6*m.b7*m.b16*m.b20*m.b29*m.b33 - m.b1*m.b12*m.b16*m.b20*m.b29*m.b33 + m.b1*m.b10*m.b18*
                       m.b20*m.b29*m.b33 - m.b1*m.b10*m.b14*m.b24*m.b29*m.b33 + m.b1*m.b10*m.b14*m.b23*m.b30*m.b33 - 
                       m.b1*m.b10*m.b14*m.b23*m.b27*m.b36 + m.b1*m.b10*m.b17*m.b20*m.b27*m.b36 - m.b1*m.b10*m.b17*m.b20*
                       m.b30*m.b33 + m.b1*m.b10*m.b17*m.b24*m.b26*m.b33 - m.b1*m.b10*m.b18*m.b23*m.b26*m.b33 + m.b1*
                       m.b12*m.b16*m.b23*m.b26*m.b33 - m.b6*m.b7*m.b16*m.b23*m.b26*m.b33 + m.b6*m.b7*m.b17*m.b22*m.b26*
                       m.b33 - m.b1*m.b12*m.b17*m.b22*m.b26*m.b33 + m.b1*m.b11*m.b18*m.b22*m.b26*m.b33 - m.b1*m.b11*
                       m.b16*m.b24*m.b26*m.b33 + m.b1*m.b11*m.b16*m.b20*m.b30*m.b33 - m.b1*m.b11*m.b16*m.b20*m.b27*m.b36
                        + m.b5*m.b7*m.b16*m.b20*m.b27*m.b36 - m.b5*m.b7*m.b16*m.b20*m.b30*m.b33 + m.b5*m.b7*m.b16*m.b24*
                       m.b26*m.b33 - m.b5*m.b7*m.b18*m.b22*m.b26*m.b33 + m.b5*m.b12*m.b13*m.b22*m.b26*m.b33 - m.b6*m.b11
                       *m.b13*m.b22*m.b26*m.b33 + m.b6*m.b11*m.b16*m.b19*m.b26*m.b33 - m.b5*m.b12*m.b16*m.b19*m.b26*
                       m.b33 + m.b5*m.b10*m.b18*m.b19*m.b26*m.b33 - m.b5*m.b10*m.b13*m.b24*m.b26*m.b33 + m.b5*m.b10*
                       m.b13*m.b20*m.b30*m.b33 - m.b5*m.b10*m.b13*m.b20*m.b27*m.b36 + m.b4*m.b11*m.b13*m.b20*m.b27*m.b36
                        - m.b4*m.b11*m.b13*m.b20*m.b30*m.b33 + m.b4*m.b11*m.b13*m.b24*m.b26*m.b33 - m.b4*m.b11*m.b18*
                       m.b19*m.b26*m.b33 + m.b4*m.b12*m.b17*m.b19*m.b26*m.b33 - m.b6*m.b10*m.b17*m.b19*m.b26*m.b33 + 
                       m.b6*m.b10*m.b13*m.b23*m.b26*m.b33 - m.b4*m.b12*m.b13*m.b23*m.b26*m.b33 + m.b4*m.b7*m.b18*m.b23*
                       m.b26*m.b33 - m.b4*m.b7*m.b17*m.b24*m.b26*m.b33 + m.b4*m.b7*m.b17*m.b20*m.b30*m.b33 - m.b4*m.b7*
                       m.b17*m.b20*m.b27*m.b36 + m.b4*m.b7*m.b14*m.b23*m.b27*m.b36 - m.b4*m.b7*m.b14*m.b23*m.b30*m.b33
                        + m.b4*m.b7*m.b14*m.b24*m.b29*m.b33 - m.b4*m.b7*m.b18*m.b20*m.b29*m.b33 + m.b4*m.b12*m.b13*m.b20
                       *m.b29*m.b33 - m.b6*m.b10*m.b13*m.b20*m.b29*m.b33 + m.b6*m.b10*m.b13*m.b20*m.b27*m.b35 - m.b4*
                       m.b12*m.b13*m.b20*m.b27*m.b35 + m.b4*m.b7*m.b18*m.b20*m.b27*m.b35 - m.b4*m.b7*m.b14*m.b24*m.b27*
                       m.b35 + m.b4*m.b7*m.b14*m.b21*m.b30*m.b35 - m.b4*m.b7*m.b14*m.b21*m.b29*m.b36 + m.b4*m.b7*m.b15*
                       m.b20*m.b29*m.b36 - m.b4*m.b7*m.b15*m.b20*m.b30*m.b35 + m.b4*m.b7*m.b15*m.b24*m.b26*m.b35 - m.b4*
                       m.b7*m.b18*m.b21*m.b26*m.b35 + m.b4*m.b12*m.b13*m.b21*m.b26*m.b35 - m.b6*m.b10*m.b13*m.b21*m.b26*
                       m.b35 + m.b6*m.b10*m.b13*m.b21*m.b29*m.b32 - m.b4*m.b12*m.b13*m.b21*m.b29*m.b32 + m.b4*m.b7*m.b18
                       *m.b21*m.b29*m.b32 - m.b4*m.b7*m.b15*m.b24*m.b29*m.b32 + m.b4*m.b7*m.b15*m.b23*m.b30*m.b32 - m.b4
                       *m.b7*m.b15*m.b23*m.b26*m.b36 + m.b4*m.b7*m.b17*m.b21*m.b26*m.b36 - m.b4*m.b7*m.b17*m.b21*m.b30*
                       m.b32 + m.b4*m.b7*m.b17*m.b24*m.b27*m.b32 - m.b4*m.b7*m.b18*m.b23*m.b27*m.b32 + m.b4*m.b12*m.b13*
                       m.b23*m.b27*m.b32 - m.b6*m.b10*m.b13*m.b23*m.b27*m.b32 + m.b6*m.b10*m.b17*m.b19*m.b27*m.b32 - 
                       m.b4*m.b12*m.b17*m.b19*m.b27*m.b32 + m.b4*m.b11*m.b18*m.b19*m.b27*m.b32 - m.b4*m.b11*m.b13*m.b24*
                       m.b27*m.b32 + m.b4*m.b11*m.b13*m.b21*m.b30*m.b32 - m.b4*m.b11*m.b13*m.b21*m.b26*m.b36 + m.b5*
                       m.b10*m.b13*m.b21*m.b26*m.b36 - m.b5*m.b10*m.b13*m.b21*m.b30*m.b32 + m.b5*m.b10*m.b13*m.b24*m.b27
                       *m.b32 - m.b5*m.b10*m.b18*m.b19*m.b27*m.b32 + m.b5*m.b12*m.b16*m.b19*m.b27*m.b32 - m.b6*m.b11*
                       m.b16*m.b19*m.b27*m.b32 + m.b6*m.b11*m.b13*m.b22*m.b27*m.b32 - m.b5*m.b12*m.b13*m.b22*m.b27*m.b32
                        + m.b5*m.b7*m.b18*m.b22*m.b27*m.b32 - m.b5*m.b7*m.b16*m.b24*m.b27*m.b32 + m.b5*m.b7*m.b16*m.b21*
                       m.b30*m.b32 - m.b5*m.b7*m.b16*m.b21*m.b26*m.b36 + m.b1*m.b11*m.b16*m.b21*m.b26*m.b36 - m.b1*m.b11
                       *m.b16*m.b21*m.b30*m.b32 + m.b1*m.b11*m.b16*m.b24*m.b27*m.b32 - m.b1*m.b11*m.b18*m.b22*m.b27*
                       m.b32 + m.b1*m.b12*m.b17*m.b22*m.b27*m.b32 - m.b6*m.b7*m.b17*m.b22*m.b27*m.b32 + m.b6*m.b7*m.b16*
                       m.b23*m.b27*m.b32 - m.b1*m.b12*m.b16*m.b23*m.b27*m.b32 + m.b1*m.b10*m.b18*m.b23*m.b27*m.b32 - 
                       m.b1*m.b10*m.b17*m.b24*m.b27*m.b32 + m.b1*m.b10*m.b17*m.b21*m.b30*m.b32 - m.b1*m.b10*m.b17*m.b21*
                       m.b26*m.b36 + m.b1*m.b10*m.b15*m.b23*m.b26*m.b36 - m.b1*m.b10*m.b15*m.b23*m.b30*m.b32 + m.b1*
                       m.b10*m.b15*m.b24*m.b29*m.b32 - m.b1*m.b10*m.b18*m.b21*m.b29*m.b32 + m.b1*m.b12*m.b16*m.b21*m.b29
                       *m.b32 - m.b6*m.b7*m.b16*m.b21*m.b29*m.b32 + m.b6*m.b7*m.b16*m.b21*m.b26*m.b35 - m.b1*m.b12*m.b16
                       *m.b21*m.b26*m.b35 + m.b1*m.b10*m.b18*m.b21*m.b26*m.b35 - m.b1*m.b10*m.b15*m.b24*m.b26*m.b35 + 
                       m.b1*m.b10*m.b15*m.b20*m.b30*m.b35 - m.b1*m.b10*m.b15*m.b20*m.b29*m.b36 + m.b1*m.b9*m.b16*m.b20*
                       m.b29*m.b36 - m.b1*m.b9*m.b16*m.b20*m.b30*m.b35 + m.b1*m.b9*m.b16*m.b24*m.b26*m.b35 - m.b1*m.b9*
                       m.b18*m.b22*m.b26*m.b35 + m.b1*m.b12*m.b15*m.b22*m.b26*m.b35 - m.b6*m.b7*m.b15*m.b22*m.b26*m.b35
                        + m.b6*m.b7*m.b15*m.b22*m.b29*m.b32 - m.b1*m.b12*m.b15*m.b22*m.b29*m.b32 + m.b1*m.b9*m.b18*m.b22
                       *m.b29*m.b32 - m.b1*m.b9*m.b16*m.b24*m.b29*m.b32 + m.b1*m.b9*m.b16*m.b23*m.b30*m.b32 - m.b1*m.b9*
                       m.b16*m.b23*m.b26*m.b36 + m.b1*m.b9*m.b17*m.b22*m.b26*m.b36 - m.b1*m.b9*m.b17*m.b22*m.b30*m.b32
                        + m.b1*m.b9*m.b17*m.b24*m.b28*m.b32 - m.b1*m.b9*m.b18*m.b23*m.b28*m.b32 + m.b1*m.b12*m.b15*m.b23
                       *m.b28*m.b32 - m.b6*m.b7*m.b15*m.b23*m.b28*m.b32 + m.b6*m.b7*m.b17*m.b21*m.b28*m.b32 - m.b1*m.b12
                       *m.b17*m.b21*m.b28*m.b32 + m.b1*m.b11*m.b18*m.b21*m.b28*m.b32 - m.b1*m.b11*m.b15*m.b24*m.b28*
                       m.b32 + m.b1*m.b11*m.b15*m.b22*m.b30*m.b32 - m.b1*m.b11*m.b15*m.b22*m.b26*m.b36 + m.b5*m.b7*m.b15
                       *m.b22*m.b26*m.b36 - m.b5*m.b7*m.b15*m.b22*m.b30*m.b32 + m.b5*m.b7*m.b15*m.b24*m.b28*m.b32 - m.b5
                       *m.b7*m.b18*m.b21*m.b28*m.b32 + m.b5*m.b12*m.b13*m.b21*m.b28*m.b32 - m.b6*m.b11*m.b13*m.b21*m.b28
                       *m.b32 + m.b6*m.b11*m.b13*m.b21*m.b26*m.b34 - m.b5*m.b12*m.b13*m.b21*m.b26*m.b34 + m.b5*m.b7*
                       m.b18*m.b21*m.b26*m.b34 - m.b5*m.b7*m.b15*m.b24*m.b26*m.b34 + m.b5*m.b7*m.b15*m.b20*m.b30*m.b34
                        - m.b5*m.b7*m.b15*m.b20*m.b28*m.b36 + m.b1*m.b11*m.b15*m.b20*m.b28*m.b36 - m.b1*m.b11*m.b15*
                       m.b20*m.b30*m.b34 + m.b1*m.b11*m.b15*m.b24*m.b26*m.b34 - m.b1*m.b11*m.b18*m.b21*m.b26*m.b34 + 
                       m.b1*m.b12*m.b17*m.b21*m.b26*m.b34 - m.b6*m.b7*m.b17*m.b21*m.b26*m.b34 + m.b6*m.b7*m.b15*m.b23*
                       m.b26*m.b34 - m.b1*m.b12*m.b15*m.b23*m.b26*m.b34 + m.b1*m.b9*m.b18*m.b23*m.b26*m.b34 - m.b1*m.b9*
                       m.b17*m.b24*m.b26*m.b34 + m.b1*m.b9*m.b17*m.b20*m.b30*m.b34 - m.b1*m.b9*m.b17*m.b20*m.b28*m.b36
                        + m.b1*m.b9*m.b14*m.b23*m.b28*m.b36 - m.b1*m.b9*m.b14*m.b23*m.b30*m.b34 + m.b1*m.b9*m.b14*m.b24*
                       m.b29*m.b34 - m.b1*m.b9*m.b18*m.b20*m.b29*m.b34 + m.b1*m.b12*m.b15*m.b20*m.b29*m.b34 - m.b6*m.b7*
                       m.b15*m.b20*m.b29*m.b34 + m.b6*m.b7*m.b15*m.b20*m.b28*m.b35 - m.b1*m.b12*m.b15*m.b20*m.b28*m.b35
                        + m.b1*m.b9*m.b18*m.b20*m.b28*m.b35 - m.b1*m.b9*m.b14*m.b24*m.b28*m.b35 + m.b1*m.b9*m.b14*m.b22*
                       m.b30*m.b35 - m.b1*m.b9*m.b14*m.b22*m.b29*m.b36 + m.b3*m.b7*m.b14*m.b22*m.b29*m.b36 - m.b3*m.b7*
                       m.b14*m.b22*m.b30*m.b35 + m.b3*m.b7*m.b14*m.b24*m.b28*m.b35 - m.b3*m.b7*m.b18*m.b20*m.b28*m.b35
                        + m.b3*m.b12*m.b13*m.b20*m.b28*m.b35 - m.b6*m.b9*m.b13*m.b20*m.b28*m.b35 + m.b6*m.b9*m.b13*m.b20
                       *m.b29*m.b34 - m.b3*m.b12*m.b13*m.b20*m.b29*m.b34 + m.b3*m.b7*m.b18*m.b20*m.b29*m.b34 - m.b3*m.b7
                       *m.b14*m.b24*m.b29*m.b34 + m.b3*m.b7*m.b14*m.b23*m.b30*m.b34 - m.b3*m.b7*m.b14*m.b23*m.b28*m.b36
                        + m.b3*m.b7*m.b17*m.b20*m.b28*m.b36 - m.b3*m.b7*m.b17*m.b20*m.b30*m.b34 + m.b3*m.b7*m.b17*m.b24*
                       m.b26*m.b34 - m.b3*m.b7*m.b18*m.b23*m.b26*m.b34 + m.b3*m.b12*m.b13*m.b23*m.b26*m.b34 - m.b6*m.b9*
                       m.b13*m.b23*m.b26*m.b34 + m.b6*m.b9*m.b17*m.b19*m.b26*m.b34 - m.b3*m.b12*m.b17*m.b19*m.b26*m.b34
                        + m.b3*m.b11*m.b18*m.b19*m.b26*m.b34 - m.b3*m.b11*m.b13*m.b24*m.b26*m.b34 + m.b3*m.b11*m.b13*
                       m.b20*m.b30*m.b34 - m.b3*m.b11*m.b13*m.b20*m.b28*m.b36 + m.b5*m.b9*m.b13*m.b20*m.b28*m.b36 - m.b5
                       *m.b9*m.b13*m.b20*m.b30*m.b34 + m.b5*m.b9*m.b13*m.b24*m.b26*m.b34 - m.b5*m.b9*m.b18*m.b19*m.b26*
                       m.b34 + m.b5*m.b12*m.b15*m.b19*m.b26*m.b34 - m.b6*m.b11*m.b15*m.b19*m.b26*m.b34 + m.b6*m.b11*
                       m.b15*m.b19*m.b28*m.b32 - m.b5*m.b12*m.b15*m.b19*m.b28*m.b32 + m.b5*m.b9*m.b18*m.b19*m.b28*m.b32
                        - m.b5*m.b9*m.b13*m.b24*m.b28*m.b32 + m.b5*m.b9*m.b13*m.b22*m.b30*m.b32 - m.b5*m.b9*m.b13*m.b22*
                       m.b26*m.b36 + m.b3*m.b11*m.b13*m.b22*m.b26*m.b36 - m.b3*m.b11*m.b13*m.b22*m.b30*m.b32 + m.b3*
                       m.b11*m.b13*m.b24*m.b28*m.b32 - m.b3*m.b11*m.b18*m.b19*m.b28*m.b32 + m.b3*m.b12*m.b17*m.b19*m.b28
                       *m.b32 - m.b6*m.b9*m.b17*m.b19*m.b28*m.b32 + m.b6*m.b9*m.b13*m.b23*m.b28*m.b32 - m.b3*m.b12*m.b13
                       *m.b23*m.b28*m.b32 + m.b3*m.b7*m.b18*m.b23*m.b28*m.b32 - m.b3*m.b7*m.b17*m.b24*m.b28*m.b32 + m.b3
                       *m.b7*m.b17*m.b22*m.b30*m.b32 - m.b3*m.b7*m.b17*m.b22*m.b26*m.b36 + m.b3*m.b7*m.b16*m.b23*m.b26*
                       m.b36 - m.b3*m.b7*m.b16*m.b23*m.b30*m.b32 + m.b3*m.b7*m.b16*m.b24*m.b29*m.b32 - m.b3*m.b7*m.b18*
                       m.b22*m.b29*m.b32 + m.b3*m.b12*m.b13*m.b22*m.b29*m.b32 - m.b6*m.b9*m.b13*m.b22*m.b29*m.b32 + m.b6
                       *m.b9*m.b13*m.b22*m.b26*m.b35 - m.b3*m.b12*m.b13*m.b22*m.b26*m.b35 + m.b3*m.b7*m.b18*m.b22*m.b26*
                       m.b35 - m.b3*m.b7*m.b16*m.b24*m.b26*m.b35 + m.b3*m.b7*m.b16*m.b20*m.b30*m.b35 - m.b3*m.b7*m.b16*
                       m.b20*m.b29*m.b36 + m.b3*m.b10*m.b13*m.b20*m.b29*m.b36 - m.b3*m.b10*m.b13*m.b20*m.b30*m.b35 + 
                       m.b3*m.b10*m.b13*m.b24*m.b26*m.b35 - m.b3*m.b10*m.b18*m.b19*m.b26*m.b35 + m.b3*m.b12*m.b16*m.b19*
                       m.b26*m.b35 - m.b6*m.b9*m.b16*m.b19*m.b26*m.b35 + m.b6*m.b9*m.b16*m.b19*m.b29*m.b32 - m.b3*m.b12*
                       m.b16*m.b19*m.b29*m.b32 + m.b3*m.b10*m.b18*m.b19*m.b29*m.b32 - m.b3*m.b10*m.b13*m.b24*m.b29*m.b32
                        + m.b3*m.b10*m.b13*m.b23*m.b30*m.b32 - m.b3*m.b10*m.b13*m.b23*m.b26*m.b36 + m.b3*m.b10*m.b17*
                       m.b19*m.b26*m.b36 - m.b3*m.b10*m.b17*m.b19*m.b30*m.b32 + m.b3*m.b10*m.b17*m.b24*m.b25*m.b32 - 
                       m.b3*m.b10*m.b18*m.b23*m.b25*m.b32 + m.b3*m.b12*m.b16*m.b23*m.b25*m.b32 - m.b6*m.b9*m.b16*m.b23*
                       m.b25*m.b32 + m.b6*m.b9*m.b17*m.b22*m.b25*m.b32 - m.b3*m.b12*m.b17*m.b22*m.b25*m.b32 + m.b3*m.b11
                       *m.b18*m.b22*m.b25*m.b32 - m.b3*m.b11*m.b16*m.b24*m.b25*m.b32 + m.b3*m.b11*m.b16*m.b19*m.b30*
                       m.b32 - m.b3*m.b11*m.b16*m.b19*m.b26*m.b36 + m.b5*m.b9*m.b16*m.b19*m.b26*m.b36 - m.b5*m.b9*m.b16*
                       m.b19*m.b30*m.b32 + m.b5*m.b9*m.b16*m.b24*m.b25*m.b32 - m.b5*m.b9*m.b18*m.b22*m.b25*m.b32 + m.b5*
                       m.b12*m.b15*m.b22*m.b25*m.b32 - m.b6*m.b11*m.b15*m.b22*m.b25*m.b32 + m.b6*m.b11*m.b16*m.b21*m.b25
                       *m.b32 - m.b5*m.b12*m.b16*m.b21*m.b25*m.b32 + m.b5*m.b10*m.b18*m.b21*m.b25*m.b32 - m.b5*m.b10*
                       m.b15*m.b24*m.b25*m.b32 + m.b5*m.b10*m.b15*m.b19*m.b30*m.b32 - m.b5*m.b10*m.b15*m.b19*m.b26*m.b36
                        + m.b4*m.b11*m.b15*m.b19*m.b26*m.b36 - m.b4*m.b11*m.b15*m.b19*m.b30*m.b32 + m.b4*m.b11*m.b15*
                       m.b24*m.b25*m.b32 - m.b4*m.b11*m.b18*m.b21*m.b25*m.b32 + m.b4*m.b12*m.b17*m.b21*m.b25*m.b32 - 
                       m.b6*m.b10*m.b17*m.b21*m.b25*m.b32 + m.b6*m.b10*m.b15*m.b23*m.b25*m.b32 - m.b4*m.b12*m.b15*m.b23*
                       m.b25*m.b32 + m.b4*m.b9*m.b18*m.b23*m.b25*m.b32 - m.b4*m.b9*m.b17*m.b24*m.b25*m.b32 + m.b4*m.b9*
                       m.b17*m.b19*m.b30*m.b32 - m.b4*m.b9*m.b17*m.b19*m.b26*m.b36 + m.b4*m.b9*m.b13*m.b23*m.b26*m.b36
                        - m.b4*m.b9*m.b13*m.b23*m.b30*m.b32 + m.b4*m.b9*m.b13*m.b24*m.b29*m.b32 - m.b4*m.b9*m.b18*m.b19*
                       m.b29*m.b32 + m.b4*m.b12*m.b15*m.b19*m.b29*m.b32 - m.b6*m.b10*m.b15*m.b19*m.b29*m.b32 + m.b6*
                       m.b10*m.b15*m.b19*m.b26*m.b35 - m.b4*m.b12*m.b15*m.b19*m.b26*m.b35 + m.b4*m.b9*m.b18*m.b19*m.b26*
                       m.b35 - m.b4*m.b9*m.b13*m.b24*m.b26*m.b35 + m.b4*m.b9*m.b13*m.b20*m.b30*m.b35 - m.b4*m.b9*m.b13*
                       m.b20*m.b29*m.b36 + m.b4*m.b9*m.b14*m.b19*m.b29*m.b36 - m.b4*m.b9*m.b14*m.b19*m.b30*m.b35 + m.b4*
                       m.b9*m.b14*m.b24*m.b25*m.b35 - m.b4*m.b9*m.b18*m.b20*m.b25*m.b35 + m.b4*m.b12*m.b15*m.b20*m.b25*
                       m.b35 - m.b6*m.b10*m.b15*m.b20*m.b25*m.b35 + m.b6*m.b10*m.b15*m.b20*m.b29*m.b31 - m.b4*m.b12*
                       m.b15*m.b20*m.b29*m.b31 + m.b4*m.b9*m.b18*m.b20*m.b29*m.b31 - m.b4*m.b9*m.b14*m.b24*m.b29*m.b31
                        + m.b4*m.b9*m.b14*m.b23*m.b30*m.b31 - m.b4*m.b9*m.b14*m.b23*m.b25*m.b36 + m.b4*m.b9*m.b17*m.b20*
                       m.b25*m.b36 - m.b4*m.b9*m.b17*m.b20*m.b30*m.b31 + m.b4*m.b9*m.b17*m.b24*m.b26*m.b31 - m.b4*m.b9*
                       m.b18*m.b23*m.b26*m.b31 + m.b4*m.b12*m.b15*m.b23*m.b26*m.b31 - m.b6*m.b10*m.b15*m.b23*m.b26*m.b31
                        + m.b6*m.b10*m.b17*m.b21*m.b26*m.b31 - m.b4*m.b12*m.b17*m.b21*m.b26*m.b31 + m.b4*m.b11*m.b18*
                       m.b21*m.b26*m.b31 - m.b4*m.b11*m.b15*m.b24*m.b26*m.b31 + m.b4*m.b11*m.b15*m.b20*m.b30*m.b31 - 
                       m.b4*m.b11*m.b15*m.b20*m.b25*m.b36 + m.b5*m.b10*m.b15*m.b20*m.b25*m.b36 - m.b5*m.b10*m.b15*m.b20*
                       m.b30*m.b31 + m.b5*m.b10*m.b15*m.b24*m.b26*m.b31 - m.b5*m.b10*m.b18*m.b21*m.b26*m.b31 + m.b5*
                       m.b12*m.b16*m.b21*m.b26*m.b31 - m.b6*m.b11*m.b16*m.b21*m.b26*m.b31 + m.b6*m.b11*m.b15*m.b22*m.b26
                       *m.b31 - m.b5*m.b12*m.b15*m.b22*m.b26*m.b31 + m.b5*m.b9*m.b18*m.b22*m.b26*m.b31 - m.b5*m.b9*m.b16
                       *m.b24*m.b26*m.b31 + m.b5*m.b9*m.b16*m.b20*m.b30*m.b31 - m.b5*m.b9*m.b16*m.b20*m.b25*m.b36 + m.b3
                       *m.b11*m.b16*m.b20*m.b25*m.b36 - m.b3*m.b11*m.b16*m.b20*m.b30*m.b31 + m.b3*m.b11*m.b16*m.b24*
                       m.b26*m.b31 - m.b3*m.b11*m.b18*m.b22*m.b26*m.b31 + m.b3*m.b12*m.b17*m.b22*m.b26*m.b31 - m.b6*m.b9
                       *m.b17*m.b22*m.b26*m.b31 + m.b6*m.b9*m.b16*m.b23*m.b26*m.b31 - m.b3*m.b12*m.b16*m.b23*m.b26*m.b31
                        + m.b3*m.b10*m.b18*m.b23*m.b26*m.b31 - m.b3*m.b10*m.b17*m.b24*m.b26*m.b31 + m.b3*m.b10*m.b17*
                       m.b20*m.b30*m.b31 - m.b3*m.b10*m.b17*m.b20*m.b25*m.b36 + m.b3*m.b10*m.b14*m.b23*m.b25*m.b36 - 
                       m.b3*m.b10*m.b14*m.b23*m.b30*m.b31 + m.b3*m.b10*m.b14*m.b24*m.b29*m.b31 - m.b3*m.b10*m.b18*m.b20*
                       m.b29*m.b31 + m.b3*m.b12*m.b16*m.b20*m.b29*m.b31 - m.b6*m.b9*m.b16*m.b20*m.b29*m.b31 + m.b6*m.b9*
                       m.b16*m.b20*m.b25*m.b35 - m.b3*m.b12*m.b16*m.b20*m.b25*m.b35 + m.b3*m.b10*m.b18*m.b20*m.b25*m.b35
                        - m.b3*m.b10*m.b14*m.b24*m.b25*m.b35 + m.b3*m.b10*m.b14*m.b19*m.b30*m.b35 - m.b3*m.b10*m.b14*
                       m.b19*m.b29*m.b36 + m.b3*m.b8*m.b16*m.b19*m.b29*m.b36 - m.b3*m.b8*m.b16*m.b19*m.b30*m.b35 + m.b3*
                       m.b8*m.b16*m.b24*m.b25*m.b35 - m.b3*m.b8*m.b18*m.b22*m.b25*m.b35 + m.b3*m.b12*m.b14*m.b22*m.b25*
                       m.b35 - m.b6*m.b9*m.b14*m.b22*m.b25*m.b35 + m.b6*m.b9*m.b14*m.b22*m.b29*m.b31 - m.b3*m.b12*m.b14*
                       m.b22*m.b29*m.b31 + m.b3*m.b8*m.b18*m.b22*m.b29*m.b31 - m.b3*m.b8*m.b16*m.b24*m.b29*m.b31 + m.b3*
                       m.b8*m.b16*m.b23*m.b30*m.b31 - m.b3*m.b8*m.b16*m.b23*m.b25*m.b36 + m.b3*m.b8*m.b17*m.b22*m.b25*
                       m.b36 - m.b3*m.b8*m.b17*m.b22*m.b30*m.b31 + m.b3*m.b8*m.b17*m.b24*m.b28*m.b31 - m.b3*m.b8*m.b18*
                       m.b23*m.b28*m.b31 + m.b3*m.b12*m.b14*m.b23*m.b28*m.b31 - m.b6*m.b9*m.b14*m.b23*m.b28*m.b31 + m.b6
                       *m.b9*m.b17*m.b20*m.b28*m.b31 - m.b3*m.b12*m.b17*m.b20*m.b28*m.b31 + m.b3*m.b11*m.b18*m.b20*m.b28
                       *m.b31 - m.b3*m.b11*m.b14*m.b24*m.b28*m.b31 + m.b3*m.b11*m.b14*m.b22*m.b30*m.b31 - m.b3*m.b11*
                       m.b14*m.b22*m.b25*m.b36 + m.b5*m.b9*m.b14*m.b22*m.b25*m.b36 - m.b5*m.b9*m.b14*m.b22*m.b30*m.b31
                        + m.b5*m.b9*m.b14*m.b24*m.b28*m.b31 - m.b5*m.b9*m.b18*m.b20*m.b28*m.b31 + m.b5*m.b12*m.b15*m.b20
                       *m.b28*m.b31 - m.b6*m.b11*m.b15*m.b20*m.b28*m.b31 + m.b6*m.b11*m.b15*m.b20*m.b25*m.b34 - m.b5*
                       m.b12*m.b15*m.b20*m.b25*m.b34 + m.b5*m.b9*m.b18*m.b20*m.b25*m.b34 - m.b5*m.b9*m.b14*m.b24*m.b25*
                       m.b34 + m.b5*m.b9*m.b14*m.b19*m.b30*m.b34 - m.b5*m.b9*m.b14*m.b19*m.b28*m.b36 + m.b3*m.b11*m.b14*
                       m.b19*m.b28*m.b36 - m.b3*m.b11*m.b14*m.b19*m.b30*m.b34 + m.b3*m.b11*m.b14*m.b24*m.b25*m.b34 - 
                       m.b3*m.b11*m.b18*m.b20*m.b25*m.b34 + m.b3*m.b12*m.b17*m.b20*m.b25*m.b34 - m.b6*m.b9*m.b17*m.b20*
                       m.b25*m.b34 + m.b6*m.b9*m.b14*m.b23*m.b25*m.b34 - m.b3*m.b12*m.b14*m.b23*m.b25*m.b34 + m.b3*m.b8*
                       m.b18*m.b23*m.b25*m.b34 - m.b3*m.b8*m.b17*m.b24*m.b25*m.b34 + m.b3*m.b8*m.b17*m.b19*m.b30*m.b34
                        - m.b3*m.b8*m.b17*m.b19*m.b28*m.b36 + m.b3*m.b8*m.b13*m.b23*m.b28*m.b36 - m.b3*m.b8*m.b13*m.b23*
                       m.b30*m.b34 + m.b3*m.b8*m.b13*m.b24*m.b29*m.b34 - m.b3*m.b8*m.b18*m.b19*m.b29*m.b34 + m.b3*m.b12*
                       m.b14*m.b19*m.b29*m.b34 - m.b6*m.b9*m.b14*m.b19*m.b29*m.b34 + m.b6*m.b9*m.b14*m.b19*m.b28*m.b35
                        - m.b3*m.b12*m.b14*m.b19*m.b28*m.b35 + m.b3*m.b8*m.b18*m.b19*m.b28*m.b35 - m.b3*m.b8*m.b13*m.b24
                       *m.b28*m.b35 + m.b3*m.b8*m.b13*m.b22*m.b30*m.b35 - m.b3*m.b8*m.b13*m.b22*m.b29*m.b36 + m.b2*m.b9*
                       m.b13*m.b22*m.b29*m.b36 - m.b2*m.b9*m.b13*m.b22*m.b30*m.b35 + m.b2*m.b9*m.b13*m.b24*m.b28*m.b35
                        - m.b2*m.b9*m.b18*m.b19*m.b28*m.b35 + m.b2*m.b12*m.b15*m.b19*m.b28*m.b35 - m.b6*m.b8*m.b15*m.b19
                       *m.b28*m.b35 + m.b6*m.b8*m.b15*m.b19*m.b29*m.b34 - m.b2*m.b12*m.b15*m.b19*m.b29*m.b34 + m.b2*m.b9
                       *m.b18*m.b19*m.b29*m.b34 - m.b2*m.b9*m.b13*m.b24*m.b29*m.b34 + m.b2*m.b9*m.b13*m.b23*m.b30*m.b34
                        - m.b2*m.b9*m.b13*m.b23*m.b28*m.b36 + m.b2*m.b9*m.b17*m.b19*m.b28*m.b36 - m.b2*m.b9*m.b17*m.b19*
                       m.b30*m.b34 + m.b2*m.b9*m.b17*m.b24*m.b25*m.b34 - m.b2*m.b9*m.b18*m.b23*m.b25*m.b34 + m.b2*m.b12*
                       m.b15*m.b23*m.b25*m.b34 - m.b6*m.b8*m.b15*m.b23*m.b25*m.b34 + m.b6*m.b8*m.b17*m.b21*m.b25*m.b34
                        - m.b2*m.b12*m.b17*m.b21*m.b25*m.b34 + m.b2*m.b11*m.b18*m.b21*m.b25*m.b34 - m.b2*m.b11*m.b15*
                       m.b24*m.b25*m.b34 + m.b2*m.b11*m.b15*m.b19*m.b30*m.b34 - m.b2*m.b11*m.b15*m.b19*m.b28*m.b36 + 
                       m.b5*m.b8*m.b15*m.b19*m.b28*m.b36 - m.b5*m.b8*m.b15*m.b19*m.b30*m.b34 + m.b5*m.b8*m.b15*m.b24*
                       m.b25*m.b34 - m.b5*m.b8*m.b18*m.b21*m.b25*m.b34 + m.b5*m.b12*m.b14*m.b21*m.b25*m.b34 - m.b6*m.b11
                       *m.b14*m.b21*m.b25*m.b34 + m.b6*m.b11*m.b14*m.b21*m.b28*m.b31 - m.b5*m.b12*m.b14*m.b21*m.b28*
                       m.b31 + m.b5*m.b8*m.b18*m.b21*m.b28*m.b31 - m.b5*m.b8*m.b15*m.b24*m.b28*m.b31 + m.b5*m.b8*m.b15*
                       m.b22*m.b30*m.b31 - m.b5*m.b8*m.b15*m.b22*m.b25*m.b36 + m.b2*m.b11*m.b15*m.b22*m.b25*m.b36 - m.b2
                       *m.b11*m.b15*m.b22*m.b30*m.b31 + m.b2*m.b11*m.b15*m.b24*m.b28*m.b31 - m.b2*m.b11*m.b18*m.b21*
                       m.b28*m.b31 + m.b2*m.b12*m.b17*m.b21*m.b28*m.b31 - m.b6*m.b8*m.b17*m.b21*m.b28*m.b31 + m.b6*m.b8*
                       m.b15*m.b23*m.b28*m.b31 - m.b2*m.b12*m.b15*m.b23*m.b28*m.b31 + m.b2*m.b9*m.b18*m.b23*m.b28*m.b31
                        - m.b2*m.b9*m.b17*m.b24*m.b28*m.b31 + m.b2*m.b9*m.b17*m.b22*m.b30*m.b31 - m.b2*m.b9*m.b17*m.b22*
                       m.b25*m.b36 + m.b2*m.b9*m.b16*m.b23*m.b25*m.b36 - m.b2*m.b9*m.b16*m.b23*m.b30*m.b31 + m.b2*m.b9*
                       m.b16*m.b24*m.b29*m.b31 - m.b2*m.b9*m.b18*m.b22*m.b29*m.b31 + m.b2*m.b12*m.b15*m.b22*m.b29*m.b31
                        - m.b6*m.b8*m.b15*m.b22*m.b29*m.b31 + m.b6*m.b8*m.b15*m.b22*m.b25*m.b35 - m.b2*m.b12*m.b15*m.b22
                       *m.b25*m.b35 + m.b2*m.b9*m.b18*m.b22*m.b25*m.b35 - m.b2*m.b9*m.b16*m.b24*m.b25*m.b35 + m.b2*m.b9*
                       m.b16*m.b19*m.b30*m.b35 - m.b2*m.b9*m.b16*m.b19*m.b29*m.b36 + m.b2*m.b10*m.b15*m.b19*m.b29*m.b36
                        - m.b2*m.b10*m.b15*m.b19*m.b30*m.b35 + m.b2*m.b10*m.b15*m.b24*m.b25*m.b35 - m.b2*m.b10*m.b18*
                       m.b21*m.b25*m.b35 + m.b2*m.b12*m.b16*m.b21*m.b25*m.b35 - m.b6*m.b8*m.b16*m.b21*m.b25*m.b35 + m.b6
                       *m.b8*m.b16*m.b21*m.b29*m.b31 - m.b2*m.b12*m.b16*m.b21*m.b29*m.b31 + m.b2*m.b10*m.b18*m.b21*m.b29
                       *m.b31 - m.b2*m.b10*m.b15*m.b24*m.b29*m.b31 + m.b2*m.b10*m.b15*m.b23*m.b30*m.b31 - m.b2*m.b10*
                       m.b15*m.b23*m.b25*m.b36 + m.b2*m.b10*m.b17*m.b21*m.b25*m.b36 - m.b2*m.b10*m.b17*m.b21*m.b30*m.b31
                        + m.b2*m.b10*m.b17*m.b24*m.b27*m.b31 - m.b2*m.b10*m.b18*m.b23*m.b27*m.b31 + m.b2*m.b12*m.b16*
                       m.b23*m.b27*m.b31 - m.b6*m.b8*m.b16*m.b23*m.b27*m.b31 + m.b6*m.b8*m.b17*m.b22*m.b27*m.b31 - m.b2*
                       m.b12*m.b17*m.b22*m.b27*m.b31 + m.b2*m.b11*m.b18*m.b22*m.b27*m.b31 - m.b2*m.b11*m.b16*m.b24*m.b27
                       *m.b31 + m.b2*m.b11*m.b16*m.b21*m.b30*m.b31 - m.b2*m.b11*m.b16*m.b21*m.b25*m.b36 + m.b5*m.b8*
                       m.b16*m.b21*m.b25*m.b36 - m.b5*m.b8*m.b16*m.b21*m.b30*m.b31 + m.b5*m.b8*m.b16*m.b24*m.b27*m.b31
                        - m.b5*m.b8*m.b18*m.b22*m.b27*m.b31 + m.b5*m.b12*m.b14*m.b22*m.b27*m.b31 - m.b6*m.b11*m.b14*
                       m.b22*m.b27*m.b31 + m.b6*m.b11*m.b16*m.b20*m.b27*m.b31 - m.b5*m.b12*m.b16*m.b20*m.b27*m.b31 + 
                       m.b5*m.b10*m.b18*m.b20*m.b27*m.b31 - m.b5*m.b10*m.b14*m.b24*m.b27*m.b31 + m.b5*m.b10*m.b14*m.b21*
                       m.b30*m.b31 - m.b5*m.b10*m.b14*m.b21*m.b25*m.b36 + m.b4*m.b11*m.b14*m.b21*m.b25*m.b36 - m.b4*
                       m.b11*m.b14*m.b21*m.b30*m.b31 + m.b4*m.b11*m.b14*m.b24*m.b27*m.b31 - m.b4*m.b11*m.b18*m.b20*m.b27
                       *m.b31 + m.b4*m.b12*m.b17*m.b20*m.b27*m.b31 - m.b6*m.b10*m.b17*m.b20*m.b27*m.b31 + m.b6*m.b10*
                       m.b14*m.b23*m.b27*m.b31 - m.b4*m.b12*m.b14*m.b23*m.b27*m.b31 + m.b4*m.b8*m.b18*m.b23*m.b27*m.b31
                        - m.b4*m.b8*m.b17*m.b24*m.b27*m.b31 + m.b4*m.b8*m.b17*m.b21*m.b30*m.b31 - m.b4*m.b8*m.b17*m.b21*
                       m.b25*m.b36 + m.b4*m.b8*m.b15*m.b23*m.b25*m.b36 - m.b4*m.b8*m.b15*m.b23*m.b30*m.b31 + m.b4*m.b8*
                       m.b15*m.b24*m.b29*m.b31 - m.b4*m.b8*m.b18*m.b21*m.b29*m.b31 + m.b4*m.b12*m.b14*m.b21*m.b29*m.b31
                        - m.b6*m.b10*m.b14*m.b21*m.b29*m.b31 + m.b6*m.b10*m.b14*m.b21*m.b25*m.b35 - m.b4*m.b12*m.b14*
                       m.b21*m.b25*m.b35 + m.b4*m.b8*m.b18*m.b21*m.b25*m.b35 - m.b4*m.b8*m.b15*m.b24*m.b25*m.b35 + m.b4*
                       m.b8*m.b15*m.b19*m.b30*m.b35 - m.b4*m.b8*m.b15*m.b19*m.b29*m.b36 + m.b4*m.b8*m.b13*m.b21*m.b29*
                       m.b36 - m.b4*m.b8*m.b13*m.b21*m.b30*m.b35 + m.b4*m.b8*m.b13*m.b24*m.b27*m.b35 - m.b4*m.b8*m.b18*
                       m.b19*m.b27*m.b35 + m.b4*m.b12*m.b14*m.b19*m.b27*m.b35 - m.b6*m.b10*m.b14*m.b19*m.b27*m.b35 + 
                       m.b6*m.b10*m.b14*m.b19*m.b29*m.b33 - m.b4*m.b12*m.b14*m.b19*m.b29*m.b33 + m.b4*m.b8*m.b18*m.b19*
                       m.b29*m.b33 - m.b4*m.b8*m.b13*m.b24*m.b29*m.b33 + m.b4*m.b8*m.b13*m.b23*m.b30*m.b33 - m.b4*m.b8*
                       m.b13*m.b23*m.b27*m.b36 + m.b4*m.b8*m.b17*m.b19*m.b27*m.b36 - m.b4*m.b8*m.b17*m.b19*m.b30*m.b33
                        + m.b4*m.b8*m.b17*m.b24*m.b25*m.b33 - m.b4*m.b8*m.b18*m.b23*m.b25*m.b33 + m.b4*m.b12*m.b14*m.b23
                       *m.b25*m.b33 - m.b6*m.b10*m.b14*m.b23*m.b25*m.b33 + m.b6*m.b10*m.b17*m.b20*m.b25*m.b33 - m.b4*
                       m.b12*m.b17*m.b20*m.b25*m.b33 + m.b4*m.b11*m.b18*m.b20*m.b25*m.b33 - m.b4*m.b11*m.b14*m.b24*m.b25
                       *m.b33 + m.b4*m.b11*m.b14*m.b19*m.b30*m.b33 - m.b4*m.b11*m.b14*m.b19*m.b27*m.b36 + m.b5*m.b10*
                       m.b14*m.b19*m.b27*m.b36 - m.b5*m.b10*m.b14*m.b19*m.b30*m.b33 + m.b5*m.b10*m.b14*m.b24*m.b25*m.b33
                        - m.b5*m.b10*m.b18*m.b20*m.b25*m.b33 + m.b5*m.b12*m.b16*m.b20*m.b25*m.b33 - m.b6*m.b11*m.b16*
                       m.b20*m.b25*m.b33 + m.b6*m.b11*m.b14*m.b22*m.b25*m.b33 - m.b5*m.b12*m.b14*m.b22*m.b25*m.b33 + 
                       m.b5*m.b8*m.b18*m.b22*m.b25*m.b33 - m.b5*m.b8*m.b16*m.b24*m.b25*m.b33 + m.b5*m.b8*m.b16*m.b19*
                       m.b30*m.b33 - m.b5*m.b8*m.b16*m.b19*m.b27*m.b36 + m.b2*m.b11*m.b16*m.b19*m.b27*m.b36 - m.b2*m.b11
                       *m.b16*m.b19*m.b30*m.b33 + m.b2*m.b11*m.b16*m.b24*m.b25*m.b33 - m.b2*m.b11*m.b18*m.b22*m.b25*
                       m.b33 + m.b2*m.b12*m.b17*m.b22*m.b25*m.b33 - m.b6*m.b8*m.b17*m.b22*m.b25*m.b33 + m.b6*m.b8*m.b16*
                       m.b23*m.b25*m.b33 - m.b2*m.b12*m.b16*m.b23*m.b25*m.b33 + m.b2*m.b10*m.b18*m.b23*m.b25*m.b33 - 
                       m.b2*m.b10*m.b17*m.b24*m.b25*m.b33 + m.b2*m.b10*m.b17*m.b19*m.b30*m.b33 - m.b2*m.b10*m.b17*m.b19*
                       m.b27*m.b36 + m.b2*m.b10*m.b13*m.b23*m.b27*m.b36 - m.b2*m.b10*m.b13*m.b23*m.b30*m.b33 + m.b2*
                       m.b10*m.b13*m.b24*m.b29*m.b33 - m.b2*m.b10*m.b18*m.b19*m.b29*m.b33 + m.b2*m.b12*m.b16*m.b19*m.b29
                       *m.b33 - m.b6*m.b8*m.b16*m.b19*m.b29*m.b33 + m.b6*m.b8*m.b16*m.b19*m.b27*m.b35 - m.b2*m.b12*m.b16
                       *m.b19*m.b27*m.b35 + m.b2*m.b10*m.b18*m.b19*m.b27*m.b35 - m.b2*m.b10*m.b13*m.b24*m.b27*m.b35 + 
                       m.b2*m.b10*m.b13*m.b21*m.b30*m.b35 - m.b2*m.b10*m.b13*m.b21*m.b29*m.b36 + m.b2*m.b7*m.b16*m.b21*
                       m.b29*m.b36 - m.b2*m.b7*m.b16*m.b21*m.b30*m.b35 + m.b2*m.b7*m.b16*m.b24*m.b27*m.b35 - m.b2*m.b7*
                       m.b18*m.b22*m.b27*m.b35 + m.b2*m.b12*m.b13*m.b22*m.b27*m.b35 - m.b6*m.b8*m.b13*m.b22*m.b27*m.b35
                        + m.b6*m.b8*m.b13*m.b22*m.b29*m.b33 - m.b2*m.b12*m.b13*m.b22*m.b29*m.b33 + m.b2*m.b7*m.b18*m.b22
                       *m.b29*m.b33 - m.b2*m.b7*m.b16*m.b24*m.b29*m.b33 + m.b2*m.b7*m.b16*m.b23*m.b30*m.b33 - m.b2*m.b7*
                       m.b16*m.b23*m.b27*m.b36 + m.b2*m.b7*m.b17*m.b22*m.b27*m.b36 - m.b2*m.b7*m.b17*m.b22*m.b30*m.b33
                        + m.b2*m.b7*m.b17*m.b24*m.b28*m.b33 - m.b2*m.b7*m.b18*m.b23*m.b28*m.b33 + m.b2*m.b12*m.b13*m.b23
                       *m.b28*m.b33 - m.b6*m.b8*m.b13*m.b23*m.b28*m.b33 + m.b6*m.b8*m.b17*m.b19*m.b28*m.b33 - m.b2*m.b12
                       *m.b17*m.b19*m.b28*m.b33 + m.b2*m.b11*m.b18*m.b19*m.b28*m.b33 - m.b2*m.b11*m.b13*m.b24*m.b28*
                       m.b33 + m.b2*m.b11*m.b13*m.b22*m.b30*m.b33 - m.b2*m.b11*m.b13*m.b22*m.b27*m.b36 + m.b5*m.b8*m.b13
                       *m.b22*m.b27*m.b36 - m.b5*m.b8*m.b13*m.b22*m.b30*m.b33 + m.b5*m.b8*m.b13*m.b24*m.b28*m.b33 - m.b5
                       *m.b8*m.b18*m.b19*m.b28*m.b33 + m.b5*m.b12*m.b14*m.b19*m.b28*m.b33 - m.b6*m.b11*m.b14*m.b19*m.b28
                       *m.b33 + m.b6*m.b11*m.b14*m.b19*m.b27*m.b34 - m.b5*m.b12*m.b14*m.b19*m.b27*m.b34 + m.b5*m.b8*
                       m.b18*m.b19*m.b27*m.b34 - m.b5*m.b8*m.b13*m.b24*m.b27*m.b34 + m.b5*m.b8*m.b13*m.b21*m.b30*m.b34
                        - m.b5*m.b8*m.b13*m.b21*m.b28*m.b36 + m.b2*m.b11*m.b13*m.b21*m.b28*m.b36 - m.b2*m.b11*m.b13*
                       m.b21*m.b30*m.b34 + m.b2*m.b11*m.b13*m.b24*m.b27*m.b34 - m.b2*m.b11*m.b18*m.b19*m.b27*m.b34 + 
                       m.b2*m.b12*m.b17*m.b19*m.b27*m.b34 - m.b6*m.b8*m.b17*m.b19*m.b27*m.b34 + m.b6*m.b8*m.b13*m.b23*
                       m.b27*m.b34 - m.b2*m.b12*m.b13*m.b23*m.b27*m.b34 + m.b2*m.b7*m.b18*m.b23*m.b27*m.b34 - m.b2*m.b7*
                       m.b17*m.b24*m.b27*m.b34 + m.b2*m.b7*m.b17*m.b21*m.b30*m.b34 - m.b2*m.b7*m.b17*m.b21*m.b28*m.b36
                        + m.b2*m.b7*m.b15*m.b23*m.b28*m.b36 - m.b2*m.b7*m.b15*m.b23*m.b30*m.b34 + m.b2*m.b7*m.b15*m.b24*
                       m.b29*m.b34 - m.b2*m.b7*m.b18*m.b21*m.b29*m.b34 + m.b2*m.b12*m.b13*m.b21*m.b29*m.b34 - m.b6*m.b8*
                       m.b13*m.b21*m.b29*m.b34 + m.b6*m.b8*m.b13*m.b21*m.b28*m.b35 - m.b2*m.b12*m.b13*m.b21*m.b28*m.b35
                        + m.b2*m.b7*m.b18*m.b21*m.b28*m.b35 - m.b2*m.b7*m.b15*m.b24*m.b28*m.b35 + m.b2*m.b7*m.b15*m.b22*
                       m.b30*m.b35 - m.b2*m.b7*m.b15*m.b22*m.b29*m.b36 - m.x37 >= 0)

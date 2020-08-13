#  MINLP written by GAMS Convert at 08/13/20 17:37:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31        1       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         31        1       30        0


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
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x31, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*
                       m.b8 + 64*m.b1*m.b4*m.b5*m.b8 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3
                       *m.b6*m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 64*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b4*m.b5*m.b7 + 128*
                       m.b2*m.b4*m.b6*m.b8 + 64*m.b2*m.b4*m.b7*m.b9 + 64*m.b2*m.b5*m.b6*m.b9 + 192*m.b3*m.b4*m.b5*m.b6
                        + 192*m.b3*m.b4*m.b6*m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 128*m.b3*m.b4*m.b8*m.b9 + 64*m.b3*m.b4*
                       m.b9*m.b10 + 192*m.b3*m.b5*m.b6*m.b8 + 128*m.b3*m.b5*m.b7*m.b9 + 64*m.b3*m.b5*m.b8*m.b10 + 64*
                       m.b3*m.b6*m.b7*m.b10 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 192*m.b4*m.b5*m.b8*
                       m.b9 + 128*m.b4*m.b5*m.b9*m.b10 + 64*m.b4*m.b5*m.b10*m.b11 + 192*m.b4*m.b6*m.b7*m.b9 + 128*m.b4*
                       m.b6*m.b8*m.b10 + 64*m.b4*m.b6*m.b9*m.b11 + 64*m.b4*m.b7*m.b8*m.b11 + 320*m.b5*m.b6*m.b7*m.b8 + 
                       256*m.b5*m.b6*m.b8*m.b9 + 192*m.b5*m.b6*m.b9*m.b10 + 128*m.b5*m.b6*m.b10*m.b11 + 64*m.b5*m.b6*
                       m.b11*m.b12 + 192*m.b5*m.b7*m.b8*m.b10 + 128*m.b5*m.b7*m.b9*m.b11 + 64*m.b5*m.b7*m.b10*m.b12 + 64
                       *m.b5*m.b8*m.b9*m.b12 + 320*m.b6*m.b7*m.b8*m.b9 + 256*m.b6*m.b7*m.b9*m.b10 + 192*m.b6*m.b7*m.b10*
                       m.b11 + 128*m.b6*m.b7*m.b11*m.b12 + 64*m.b6*m.b7*m.b12*m.b13 + 192*m.b6*m.b8*m.b9*m.b11 + 128*
                       m.b6*m.b8*m.b10*m.b12 + 64*m.b6*m.b8*m.b11*m.b13 + 64*m.b6*m.b9*m.b10*m.b13 + 320*m.b7*m.b8*m.b9*
                       m.b10 + 256*m.b7*m.b8*m.b10*m.b11 + 192*m.b7*m.b8*m.b11*m.b12 + 128*m.b7*m.b8*m.b12*m.b13 + 64*
                       m.b7*m.b8*m.b13*m.b14 + 192*m.b7*m.b9*m.b10*m.b12 + 128*m.b7*m.b9*m.b11*m.b13 + 64*m.b7*m.b9*
                       m.b12*m.b14 + 64*m.b7*m.b10*m.b11*m.b14 + 320*m.b8*m.b9*m.b10*m.b11 + 256*m.b8*m.b9*m.b11*m.b12
                        + 192*m.b8*m.b9*m.b12*m.b13 + 128*m.b8*m.b9*m.b13*m.b14 + 64*m.b8*m.b9*m.b14*m.b15 + 192*m.b8*
                       m.b10*m.b11*m.b13 + 128*m.b8*m.b10*m.b12*m.b14 + 64*m.b8*m.b10*m.b13*m.b15 + 64*m.b8*m.b11*m.b12*
                       m.b15 + 320*m.b9*m.b10*m.b11*m.b12 + 256*m.b9*m.b10*m.b12*m.b13 + 192*m.b9*m.b10*m.b13*m.b14 + 
                       128*m.b9*m.b10*m.b14*m.b15 + 64*m.b9*m.b10*m.b15*m.b16 + 192*m.b9*m.b11*m.b12*m.b14 + 128*m.b9*
                       m.b11*m.b13*m.b15 + 64*m.b9*m.b11*m.b14*m.b16 + 64*m.b9*m.b12*m.b13*m.b16 + 320*m.b10*m.b11*m.b12
                       *m.b13 + 256*m.b10*m.b11*m.b13*m.b14 + 192*m.b10*m.b11*m.b14*m.b15 + 128*m.b10*m.b11*m.b15*m.b16
                        + 64*m.b10*m.b11*m.b16*m.b17 + 192*m.b10*m.b12*m.b13*m.b15 + 128*m.b10*m.b12*m.b14*m.b16 + 64*
                       m.b10*m.b12*m.b15*m.b17 + 64*m.b10*m.b13*m.b14*m.b17 + 320*m.b11*m.b12*m.b13*m.b14 + 256*m.b11*
                       m.b12*m.b14*m.b15 + 192*m.b11*m.b12*m.b15*m.b16 + 128*m.b11*m.b12*m.b16*m.b17 + 64*m.b11*m.b12*
                       m.b17*m.b18 + 192*m.b11*m.b13*m.b14*m.b16 + 128*m.b11*m.b13*m.b15*m.b17 + 64*m.b11*m.b13*m.b16*
                       m.b18 + 64*m.b11*m.b14*m.b15*m.b18 + 320*m.b12*m.b13*m.b14*m.b15 + 256*m.b12*m.b13*m.b15*m.b16 + 
                       192*m.b12*m.b13*m.b16*m.b17 + 128*m.b12*m.b13*m.b17*m.b18 + 64*m.b12*m.b13*m.b18*m.b19 + 192*
                       m.b12*m.b14*m.b15*m.b17 + 128*m.b12*m.b14*m.b16*m.b18 + 64*m.b12*m.b14*m.b17*m.b19 + 64*m.b12*
                       m.b15*m.b16*m.b19 + 320*m.b13*m.b14*m.b15*m.b16 + 256*m.b13*m.b14*m.b16*m.b17 + 192*m.b13*m.b14*
                       m.b17*m.b18 + 128*m.b13*m.b14*m.b18*m.b19 + 64*m.b13*m.b14*m.b19*m.b20 + 192*m.b13*m.b15*m.b16*
                       m.b18 + 128*m.b13*m.b15*m.b17*m.b19 + 64*m.b13*m.b15*m.b18*m.b20 + 64*m.b13*m.b16*m.b17*m.b20 + 
                       320*m.b14*m.b15*m.b16*m.b17 + 256*m.b14*m.b15*m.b17*m.b18 + 192*m.b14*m.b15*m.b18*m.b19 + 128*
                       m.b14*m.b15*m.b19*m.b20 + 64*m.b14*m.b15*m.b20*m.b21 + 192*m.b14*m.b16*m.b17*m.b19 + 128*m.b14*
                       m.b16*m.b18*m.b20 + 64*m.b14*m.b16*m.b19*m.b21 + 64*m.b14*m.b17*m.b18*m.b21 + 320*m.b15*m.b16*
                       m.b17*m.b18 + 256*m.b15*m.b16*m.b18*m.b19 + 192*m.b15*m.b16*m.b19*m.b20 + 128*m.b15*m.b16*m.b20*
                       m.b21 + 64*m.b15*m.b16*m.b21*m.b22 + 192*m.b15*m.b17*m.b18*m.b20 + 128*m.b15*m.b17*m.b19*m.b21 + 
                       64*m.b15*m.b17*m.b20*m.b22 + 64*m.b15*m.b18*m.b19*m.b22 + 320*m.b16*m.b17*m.b18*m.b19 + 256*m.b16
                       *m.b17*m.b19*m.b20 + 192*m.b16*m.b17*m.b20*m.b21 + 128*m.b16*m.b17*m.b21*m.b22 + 64*m.b16*m.b17*
                       m.b22*m.b23 + 192*m.b16*m.b18*m.b19*m.b21 + 128*m.b16*m.b18*m.b20*m.b22 + 64*m.b16*m.b18*m.b21*
                       m.b23 + 64*m.b16*m.b19*m.b20*m.b23 + 320*m.b17*m.b18*m.b19*m.b20 + 256*m.b17*m.b18*m.b20*m.b21 + 
                       192*m.b17*m.b18*m.b21*m.b22 + 128*m.b17*m.b18*m.b22*m.b23 + 64*m.b17*m.b18*m.b23*m.b24 + 192*
                       m.b17*m.b19*m.b20*m.b22 + 128*m.b17*m.b19*m.b21*m.b23 + 64*m.b17*m.b19*m.b22*m.b24 + 64*m.b17*
                       m.b20*m.b21*m.b24 + 320*m.b18*m.b19*m.b20*m.b21 + 256*m.b18*m.b19*m.b21*m.b22 + 192*m.b18*m.b19*
                       m.b22*m.b23 + 128*m.b18*m.b19*m.b23*m.b24 + 64*m.b18*m.b19*m.b24*m.b25 + 192*m.b18*m.b20*m.b21*
                       m.b23 + 128*m.b18*m.b20*m.b22*m.b24 + 64*m.b18*m.b20*m.b23*m.b25 + 64*m.b18*m.b21*m.b22*m.b25 + 
                       320*m.b19*m.b20*m.b21*m.b22 + 256*m.b19*m.b20*m.b22*m.b23 + 192*m.b19*m.b20*m.b23*m.b24 + 128*
                       m.b19*m.b20*m.b24*m.b25 + 64*m.b19*m.b20*m.b25*m.b26 + 192*m.b19*m.b21*m.b22*m.b24 + 128*m.b19*
                       m.b21*m.b23*m.b25 + 64*m.b19*m.b21*m.b24*m.b26 + 64*m.b19*m.b22*m.b23*m.b26 + 320*m.b20*m.b21*
                       m.b22*m.b23 + 256*m.b20*m.b21*m.b23*m.b24 + 192*m.b20*m.b21*m.b24*m.b25 + 128*m.b20*m.b21*m.b25*
                       m.b26 + 64*m.b20*m.b21*m.b26*m.b27 + 192*m.b20*m.b22*m.b23*m.b25 + 128*m.b20*m.b22*m.b24*m.b26 + 
                       64*m.b20*m.b22*m.b25*m.b27 + 64*m.b20*m.b23*m.b24*m.b27 + 320*m.b21*m.b22*m.b23*m.b24 + 256*m.b21
                       *m.b22*m.b24*m.b25 + 192*m.b21*m.b22*m.b25*m.b26 + 128*m.b21*m.b22*m.b26*m.b27 + 64*m.b21*m.b22*
                       m.b27*m.b28 + 192*m.b21*m.b23*m.b24*m.b26 + 128*m.b21*m.b23*m.b25*m.b27 + 64*m.b21*m.b23*m.b26*
                       m.b28 + 64*m.b21*m.b24*m.b25*m.b28 + 320*m.b22*m.b23*m.b24*m.b25 + 256*m.b22*m.b23*m.b25*m.b26 + 
                       192*m.b22*m.b23*m.b26*m.b27 + 128*m.b22*m.b23*m.b27*m.b28 + 64*m.b22*m.b23*m.b28*m.b29 + 192*
                       m.b22*m.b24*m.b25*m.b27 + 128*m.b22*m.b24*m.b26*m.b28 + 64*m.b22*m.b24*m.b27*m.b29 + 64*m.b22*
                       m.b25*m.b26*m.b29 + 320*m.b23*m.b24*m.b25*m.b26 + 256*m.b23*m.b24*m.b26*m.b27 + 192*m.b23*m.b24*
                       m.b27*m.b28 + 128*m.b23*m.b24*m.b28*m.b29 + 64*m.b23*m.b24*m.b29*m.b30 + 192*m.b23*m.b25*m.b26*
                       m.b28 + 128*m.b23*m.b25*m.b27*m.b29 + 64*m.b23*m.b25*m.b28*m.b30 + 64*m.b23*m.b26*m.b27*m.b30 + 
                       256*m.b24*m.b25*m.b26*m.b27 + 192*m.b24*m.b25*m.b27*m.b28 + 128*m.b24*m.b25*m.b28*m.b29 + 64*
                       m.b24*m.b25*m.b29*m.b30 + 128*m.b24*m.b26*m.b27*m.b29 + 64*m.b24*m.b26*m.b28*m.b30 + 192*m.b25*
                       m.b26*m.b27*m.b28 + 128*m.b25*m.b26*m.b28*m.b29 + 64*m.b25*m.b26*m.b29*m.b30 + 64*m.b25*m.b27*
                       m.b28*m.b30 + 128*m.b26*m.b27*m.b28*m.b29 + 64*m.b26*m.b27*m.b29*m.b30 + 64*m.b27*m.b28*m.b29*
                       m.b30 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*
                       m.b2*m.b7 - 32*m.b1*m.b2*m.b8 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 32*
                       m.b1*m.b3*m.b7 - 32*m.b1*m.b3*m.b8 - 64*m.b1*m.b4*m.b5 - 32*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b8 - 
                       32*m.b1*m.b5*m.b6 - 32*m.b1*m.b5*m.b7 - 32*m.b1*m.b5*m.b8 - 32*m.b1*m.b6*m.b7 - 32*m.b1*m.b6*m.b8
                        - 32*m.b1*m.b7*m.b8 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*
                       m.b3*m.b7 - 96*m.b2*m.b3*m.b8 - 32*m.b2*m.b3*m.b9 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 96*
                       m.b2*m.b4*m.b7 - 64*m.b2*m.b4*m.b8 - 32*m.b2*m.b4*m.b9 - 128*m.b2*m.b5*m.b6 - 64*m.b2*m.b5*m.b7
                        - 32*m.b2*m.b5*m.b9 - 96*m.b2*m.b6*m.b7 - 64*m.b2*m.b6*m.b8 - 32*m.b2*m.b6*m.b9 - 96*m.b2*m.b7*
                       m.b8 - 32*m.b2*m.b7*m.b9 - 32*m.b2*m.b8*m.b9 - 160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3
                       *m.b4*m.b7 - 160*m.b3*m.b4*m.b8 - 96*m.b3*m.b4*m.b9 - 32*m.b3*m.b4*m.b10 - 256*m.b3*m.b5*m.b6 - 
                       96*m.b3*m.b5*m.b7 - 128*m.b3*m.b5*m.b8 - 64*m.b3*m.b5*m.b9 - 32*m.b3*m.b5*m.b10 - 192*m.b3*m.b6*
                       m.b7 - 128*m.b3*m.b6*m.b8 - 32*m.b3*m.b6*m.b10 - 160*m.b3*m.b7*m.b8 - 64*m.b3*m.b7*m.b9 - 32*m.b3
                       *m.b7*m.b10 - 96*m.b3*m.b8*m.b9 - 32*m.b3*m.b8*m.b10 - 32*m.b3*m.b9*m.b10 - 224*m.b4*m.b5*m.b6 - 
                       320*m.b4*m.b5*m.b7 - 256*m.b4*m.b5*m.b8 - 160*m.b4*m.b5*m.b9 - 96*m.b4*m.b5*m.b10 - 32*m.b4*m.b5*
                       m.b11 - 320*m.b4*m.b6*m.b7 - 128*m.b4*m.b6*m.b8 - 128*m.b4*m.b6*m.b9 - 64*m.b4*m.b6*m.b10 - 32*
                       m.b4*m.b6*m.b11 - 256*m.b4*m.b7*m.b8 - 128*m.b4*m.b7*m.b9 - 32*m.b4*m.b7*m.b11 - 160*m.b4*m.b8*
                       m.b9 - 64*m.b4*m.b8*m.b10 - 32*m.b4*m.b8*m.b11 - 96*m.b4*m.b9*m.b10 - 32*m.b4*m.b9*m.b11 - 32*
                       m.b4*m.b10*m.b11 - 288*m.b5*m.b6*m.b7 - 384*m.b5*m.b6*m.b8 - 256*m.b5*m.b6*m.b9 - 160*m.b5*m.b6*
                       m.b10 - 96*m.b5*m.b6*m.b11 - 32*m.b5*m.b6*m.b12 - 384*m.b5*m.b7*m.b8 - 128*m.b5*m.b7*m.b9 - 128*
                       m.b5*m.b7*m.b10 - 64*m.b5*m.b7*m.b11 - 32*m.b5*m.b7*m.b12 - 256*m.b5*m.b8*m.b9 - 128*m.b5*m.b8*
                       m.b10 - 32*m.b5*m.b8*m.b12 - 160*m.b5*m.b9*m.b10 - 64*m.b5*m.b9*m.b11 - 32*m.b5*m.b9*m.b12 - 96*
                       m.b5*m.b10*m.b11 - 32*m.b5*m.b10*m.b12 - 32*m.b5*m.b11*m.b12 - 320*m.b6*m.b7*m.b8 - 384*m.b6*m.b7
                       *m.b9 - 256*m.b6*m.b7*m.b10 - 160*m.b6*m.b7*m.b11 - 96*m.b6*m.b7*m.b12 - 32*m.b6*m.b7*m.b13 - 384
                       *m.b6*m.b8*m.b9 - 128*m.b6*m.b8*m.b10 - 128*m.b6*m.b8*m.b11 - 64*m.b6*m.b8*m.b12 - 32*m.b6*m.b8*
                       m.b13 - 256*m.b6*m.b9*m.b10 - 128*m.b6*m.b9*m.b11 - 32*m.b6*m.b9*m.b13 - 160*m.b6*m.b10*m.b11 - 
                       64*m.b6*m.b10*m.b12 - 32*m.b6*m.b10*m.b13 - 96*m.b6*m.b11*m.b12 - 32*m.b6*m.b11*m.b13 - 32*m.b6*
                       m.b12*m.b13 - 320*m.b7*m.b8*m.b9 - 384*m.b7*m.b8*m.b10 - 256*m.b7*m.b8*m.b11 - 160*m.b7*m.b8*
                       m.b12 - 96*m.b7*m.b8*m.b13 - 32*m.b7*m.b8*m.b14 - 384*m.b7*m.b9*m.b10 - 128*m.b7*m.b9*m.b11 - 128
                       *m.b7*m.b9*m.b12 - 64*m.b7*m.b9*m.b13 - 32*m.b7*m.b9*m.b14 - 256*m.b7*m.b10*m.b11 - 128*m.b7*
                       m.b10*m.b12 - 32*m.b7*m.b10*m.b14 - 160*m.b7*m.b11*m.b12 - 64*m.b7*m.b11*m.b13 - 32*m.b7*m.b11*
                       m.b14 - 96*m.b7*m.b12*m.b13 - 32*m.b7*m.b12*m.b14 - 32*m.b7*m.b13*m.b14 - 320*m.b8*m.b9*m.b10 - 
                       384*m.b8*m.b9*m.b11 - 256*m.b8*m.b9*m.b12 - 160*m.b8*m.b9*m.b13 - 96*m.b8*m.b9*m.b14 - 32*m.b8*
                       m.b9*m.b15 - 384*m.b8*m.b10*m.b11 - 128*m.b8*m.b10*m.b12 - 128*m.b8*m.b10*m.b13 - 64*m.b8*m.b10*
                       m.b14 - 32*m.b8*m.b10*m.b15 - 256*m.b8*m.b11*m.b12 - 128*m.b8*m.b11*m.b13 - 32*m.b8*m.b11*m.b15
                        - 160*m.b8*m.b12*m.b13 - 64*m.b8*m.b12*m.b14 - 32*m.b8*m.b12*m.b15 - 96*m.b8*m.b13*m.b14 - 32*
                       m.b8*m.b13*m.b15 - 32*m.b8*m.b14*m.b15 - 320*m.b9*m.b10*m.b11 - 384*m.b9*m.b10*m.b12 - 256*m.b9*
                       m.b10*m.b13 - 160*m.b9*m.b10*m.b14 - 96*m.b9*m.b10*m.b15 - 32*m.b9*m.b10*m.b16 - 384*m.b9*m.b11*
                       m.b12 - 128*m.b9*m.b11*m.b13 - 128*m.b9*m.b11*m.b14 - 64*m.b9*m.b11*m.b15 - 32*m.b9*m.b11*m.b16
                        - 256*m.b9*m.b12*m.b13 - 128*m.b9*m.b12*m.b14 - 32*m.b9*m.b12*m.b16 - 160*m.b9*m.b13*m.b14 - 64*
                       m.b9*m.b13*m.b15 - 32*m.b9*m.b13*m.b16 - 96*m.b9*m.b14*m.b15 - 32*m.b9*m.b14*m.b16 - 32*m.b9*
                       m.b15*m.b16 - 320*m.b10*m.b11*m.b12 - 384*m.b10*m.b11*m.b13 - 256*m.b10*m.b11*m.b14 - 160*m.b10*
                       m.b11*m.b15 - 96*m.b10*m.b11*m.b16 - 32*m.b10*m.b11*m.b17 - 384*m.b10*m.b12*m.b13 - 128*m.b10*
                       m.b12*m.b14 - 128*m.b10*m.b12*m.b15 - 64*m.b10*m.b12*m.b16 - 32*m.b10*m.b12*m.b17 - 256*m.b10*
                       m.b13*m.b14 - 128*m.b10*m.b13*m.b15 - 32*m.b10*m.b13*m.b17 - 160*m.b10*m.b14*m.b15 - 64*m.b10*
                       m.b14*m.b16 - 32*m.b10*m.b14*m.b17 - 96*m.b10*m.b15*m.b16 - 32*m.b10*m.b15*m.b17 - 32*m.b10*m.b16
                       *m.b17 - 320*m.b11*m.b12*m.b13 - 384*m.b11*m.b12*m.b14 - 256*m.b11*m.b12*m.b15 - 160*m.b11*m.b12*
                       m.b16 - 96*m.b11*m.b12*m.b17 - 32*m.b11*m.b12*m.b18 - 384*m.b11*m.b13*m.b14 - 128*m.b11*m.b13*
                       m.b15 - 128*m.b11*m.b13*m.b16 - 64*m.b11*m.b13*m.b17 - 32*m.b11*m.b13*m.b18 - 256*m.b11*m.b14*
                       m.b15 - 128*m.b11*m.b14*m.b16 - 32*m.b11*m.b14*m.b18 - 160*m.b11*m.b15*m.b16 - 64*m.b11*m.b15*
                       m.b17 - 32*m.b11*m.b15*m.b18 - 96*m.b11*m.b16*m.b17 - 32*m.b11*m.b16*m.b18 - 32*m.b11*m.b17*m.b18
                        - 320*m.b12*m.b13*m.b14 - 384*m.b12*m.b13*m.b15 - 256*m.b12*m.b13*m.b16 - 160*m.b12*m.b13*m.b17
                        - 96*m.b12*m.b13*m.b18 - 32*m.b12*m.b13*m.b19 - 384*m.b12*m.b14*m.b15 - 128*m.b12*m.b14*m.b16 - 
                       128*m.b12*m.b14*m.b17 - 64*m.b12*m.b14*m.b18 - 32*m.b12*m.b14*m.b19 - 256*m.b12*m.b15*m.b16 - 128
                       *m.b12*m.b15*m.b17 - 32*m.b12*m.b15*m.b19 - 160*m.b12*m.b16*m.b17 - 64*m.b12*m.b16*m.b18 - 32*
                       m.b12*m.b16*m.b19 - 96*m.b12*m.b17*m.b18 - 32*m.b12*m.b17*m.b19 - 32*m.b12*m.b18*m.b19 - 320*
                       m.b13*m.b14*m.b15 - 384*m.b13*m.b14*m.b16 - 256*m.b13*m.b14*m.b17 - 160*m.b13*m.b14*m.b18 - 96*
                       m.b13*m.b14*m.b19 - 32*m.b13*m.b14*m.b20 - 384*m.b13*m.b15*m.b16 - 128*m.b13*m.b15*m.b17 - 128*
                       m.b13*m.b15*m.b18 - 64*m.b13*m.b15*m.b19 - 32*m.b13*m.b15*m.b20 - 256*m.b13*m.b16*m.b17 - 128*
                       m.b13*m.b16*m.b18 - 32*m.b13*m.b16*m.b20 - 160*m.b13*m.b17*m.b18 - 64*m.b13*m.b17*m.b19 - 32*
                       m.b13*m.b17*m.b20 - 96*m.b13*m.b18*m.b19 - 32*m.b13*m.b18*m.b20 - 32*m.b13*m.b19*m.b20 - 320*
                       m.b14*m.b15*m.b16 - 384*m.b14*m.b15*m.b17 - 256*m.b14*m.b15*m.b18 - 160*m.b14*m.b15*m.b19 - 96*
                       m.b14*m.b15*m.b20 - 32*m.b14*m.b15*m.b21 - 384*m.b14*m.b16*m.b17 - 128*m.b14*m.b16*m.b18 - 128*
                       m.b14*m.b16*m.b19 - 64*m.b14*m.b16*m.b20 - 32*m.b14*m.b16*m.b21 - 256*m.b14*m.b17*m.b18 - 128*
                       m.b14*m.b17*m.b19 - 32*m.b14*m.b17*m.b21 - 160*m.b14*m.b18*m.b19 - 64*m.b14*m.b18*m.b20 - 32*
                       m.b14*m.b18*m.b21 - 96*m.b14*m.b19*m.b20 - 32*m.b14*m.b19*m.b21 - 32*m.b14*m.b20*m.b21 - 320*
                       m.b15*m.b16*m.b17 - 384*m.b15*m.b16*m.b18 - 256*m.b15*m.b16*m.b19 - 160*m.b15*m.b16*m.b20 - 96*
                       m.b15*m.b16*m.b21 - 32*m.b15*m.b16*m.b22 - 384*m.b15*m.b17*m.b18 - 128*m.b15*m.b17*m.b19 - 128*
                       m.b15*m.b17*m.b20 - 64*m.b15*m.b17*m.b21 - 32*m.b15*m.b17*m.b22 - 256*m.b15*m.b18*m.b19 - 128*
                       m.b15*m.b18*m.b20 - 32*m.b15*m.b18*m.b22 - 160*m.b15*m.b19*m.b20 - 64*m.b15*m.b19*m.b21 - 32*
                       m.b15*m.b19*m.b22 - 96*m.b15*m.b20*m.b21 - 32*m.b15*m.b20*m.b22 - 32*m.b15*m.b21*m.b22 - 320*
                       m.b16*m.b17*m.b18 - 384*m.b16*m.b17*m.b19 - 256*m.b16*m.b17*m.b20 - 160*m.b16*m.b17*m.b21 - 96*
                       m.b16*m.b17*m.b22 - 32*m.b16*m.b17*m.b23 - 384*m.b16*m.b18*m.b19 - 128*m.b16*m.b18*m.b20 - 128*
                       m.b16*m.b18*m.b21 - 64*m.b16*m.b18*m.b22 - 32*m.b16*m.b18*m.b23 - 256*m.b16*m.b19*m.b20 - 128*
                       m.b16*m.b19*m.b21 - 32*m.b16*m.b19*m.b23 - 160*m.b16*m.b20*m.b21 - 64*m.b16*m.b20*m.b22 - 32*
                       m.b16*m.b20*m.b23 - 96*m.b16*m.b21*m.b22 - 32*m.b16*m.b21*m.b23 - 32*m.b16*m.b22*m.b23 - 320*
                       m.b17*m.b18*m.b19 - 384*m.b17*m.b18*m.b20 - 256*m.b17*m.b18*m.b21 - 160*m.b17*m.b18*m.b22 - 96*
                       m.b17*m.b18*m.b23 - 32*m.b17*m.b18*m.b24 - 384*m.b17*m.b19*m.b20 - 128*m.b17*m.b19*m.b21 - 128*
                       m.b17*m.b19*m.b22 - 64*m.b17*m.b19*m.b23 - 32*m.b17*m.b19*m.b24 - 256*m.b17*m.b20*m.b21 - 128*
                       m.b17*m.b20*m.b22 - 32*m.b17*m.b20*m.b24 - 160*m.b17*m.b21*m.b22 - 64*m.b17*m.b21*m.b23 - 32*
                       m.b17*m.b21*m.b24 - 96*m.b17*m.b22*m.b23 - 32*m.b17*m.b22*m.b24 - 32*m.b17*m.b23*m.b24 - 320*
                       m.b18*m.b19*m.b20 - 384*m.b18*m.b19*m.b21 - 256*m.b18*m.b19*m.b22 - 160*m.b18*m.b19*m.b23 - 96*
                       m.b18*m.b19*m.b24 - 32*m.b18*m.b19*m.b25 - 384*m.b18*m.b20*m.b21 - 128*m.b18*m.b20*m.b22 - 128*
                       m.b18*m.b20*m.b23 - 64*m.b18*m.b20*m.b24 - 32*m.b18*m.b20*m.b25 - 256*m.b18*m.b21*m.b22 - 128*
                       m.b18*m.b21*m.b23 - 32*m.b18*m.b21*m.b25 - 160*m.b18*m.b22*m.b23 - 64*m.b18*m.b22*m.b24 - 32*
                       m.b18*m.b22*m.b25 - 96*m.b18*m.b23*m.b24 - 32*m.b18*m.b23*m.b25 - 32*m.b18*m.b24*m.b25 - 320*
                       m.b19*m.b20*m.b21 - 384*m.b19*m.b20*m.b22 - 256*m.b19*m.b20*m.b23 - 160*m.b19*m.b20*m.b24 - 96*
                       m.b19*m.b20*m.b25 - 32*m.b19*m.b20*m.b26 - 384*m.b19*m.b21*m.b22 - 128*m.b19*m.b21*m.b23 - 128*
                       m.b19*m.b21*m.b24 - 64*m.b19*m.b21*m.b25 - 32*m.b19*m.b21*m.b26 - 256*m.b19*m.b22*m.b23 - 128*
                       m.b19*m.b22*m.b24 - 32*m.b19*m.b22*m.b26 - 160*m.b19*m.b23*m.b24 - 64*m.b19*m.b23*m.b25 - 32*
                       m.b19*m.b23*m.b26 - 96*m.b19*m.b24*m.b25 - 32*m.b19*m.b24*m.b26 - 32*m.b19*m.b25*m.b26 - 320*
                       m.b20*m.b21*m.b22 - 384*m.b20*m.b21*m.b23 - 256*m.b20*m.b21*m.b24 - 160*m.b20*m.b21*m.b25 - 96*
                       m.b20*m.b21*m.b26 - 32*m.b20*m.b21*m.b27 - 384*m.b20*m.b22*m.b23 - 128*m.b20*m.b22*m.b24 - 128*
                       m.b20*m.b22*m.b25 - 64*m.b20*m.b22*m.b26 - 32*m.b20*m.b22*m.b27 - 256*m.b20*m.b23*m.b24 - 128*
                       m.b20*m.b23*m.b25 - 32*m.b20*m.b23*m.b27 - 160*m.b20*m.b24*m.b25 - 64*m.b20*m.b24*m.b26 - 32*
                       m.b20*m.b24*m.b27 - 96*m.b20*m.b25*m.b26 - 32*m.b20*m.b25*m.b27 - 32*m.b20*m.b26*m.b27 - 320*
                       m.b21*m.b22*m.b23 - 384*m.b21*m.b22*m.b24 - 256*m.b21*m.b22*m.b25 - 160*m.b21*m.b22*m.b26 - 96*
                       m.b21*m.b22*m.b27 - 32*m.b21*m.b22*m.b28 - 384*m.b21*m.b23*m.b24 - 128*m.b21*m.b23*m.b25 - 128*
                       m.b21*m.b23*m.b26 - 64*m.b21*m.b23*m.b27 - 32*m.b21*m.b23*m.b28 - 256*m.b21*m.b24*m.b25 - 128*
                       m.b21*m.b24*m.b26 - 32*m.b21*m.b24*m.b28 - 160*m.b21*m.b25*m.b26 - 64*m.b21*m.b25*m.b27 - 32*
                       m.b21*m.b25*m.b28 - 96*m.b21*m.b26*m.b27 - 32*m.b21*m.b26*m.b28 - 32*m.b21*m.b27*m.b28 - 320*
                       m.b22*m.b23*m.b24 - 384*m.b22*m.b23*m.b25 - 256*m.b22*m.b23*m.b26 - 160*m.b22*m.b23*m.b27 - 96*
                       m.b22*m.b23*m.b28 - 32*m.b22*m.b23*m.b29 - 384*m.b22*m.b24*m.b25 - 128*m.b22*m.b24*m.b26 - 128*
                       m.b22*m.b24*m.b27 - 64*m.b22*m.b24*m.b28 - 32*m.b22*m.b24*m.b29 - 256*m.b22*m.b25*m.b26 - 128*
                       m.b22*m.b25*m.b27 - 32*m.b22*m.b25*m.b29 - 160*m.b22*m.b26*m.b27 - 64*m.b22*m.b26*m.b28 - 32*
                       m.b22*m.b26*m.b29 - 96*m.b22*m.b27*m.b28 - 32*m.b22*m.b27*m.b29 - 32*m.b22*m.b28*m.b29 - 320*
                       m.b23*m.b24*m.b25 - 384*m.b23*m.b24*m.b26 - 256*m.b23*m.b24*m.b27 - 160*m.b23*m.b24*m.b28 - 96*
                       m.b23*m.b24*m.b29 - 32*m.b23*m.b24*m.b30 - 384*m.b23*m.b25*m.b26 - 128*m.b23*m.b25*m.b27 - 128*
                       m.b23*m.b25*m.b28 - 64*m.b23*m.b25*m.b29 - 32*m.b23*m.b25*m.b30 - 256*m.b23*m.b26*m.b27 - 128*
                       m.b23*m.b26*m.b28 - 32*m.b23*m.b26*m.b30 - 160*m.b23*m.b27*m.b28 - 64*m.b23*m.b27*m.b29 - 32*
                       m.b23*m.b27*m.b30 - 96*m.b23*m.b28*m.b29 - 32*m.b23*m.b28*m.b30 - 32*m.b23*m.b29*m.b30 - 288*
                       m.b24*m.b25*m.b26 - 320*m.b24*m.b25*m.b27 - 192*m.b24*m.b25*m.b28 - 96*m.b24*m.b25*m.b29 - 32*
                       m.b24*m.b25*m.b30 - 320*m.b24*m.b26*m.b27 - 96*m.b24*m.b26*m.b28 - 64*m.b24*m.b26*m.b29 - 32*
                       m.b24*m.b26*m.b30 - 192*m.b24*m.b27*m.b28 - 96*m.b24*m.b27*m.b29 - 128*m.b24*m.b28*m.b29 - 32*
                       m.b24*m.b28*m.b30 - 64*m.b24*m.b29*m.b30 - 224*m.b25*m.b26*m.b27 - 256*m.b25*m.b26*m.b28 - 128*
                       m.b25*m.b26*m.b29 - 32*m.b25*m.b26*m.b30 - 224*m.b25*m.b27*m.b28 - 64*m.b25*m.b27*m.b29 - 32*
                       m.b25*m.b27*m.b30 - 128*m.b25*m.b28*m.b29 - 64*m.b25*m.b28*m.b30 - 64*m.b25*m.b29*m.b30 - 160*
                       m.b26*m.b27*m.b28 - 160*m.b26*m.b27*m.b29 - 64*m.b26*m.b27*m.b30 - 128*m.b26*m.b28*m.b29 - 32*
                       m.b26*m.b28*m.b30 - 64*m.b26*m.b29*m.b30 - 96*m.b27*m.b28*m.b29 - 64*m.b27*m.b28*m.b30 - 64*m.b27
                       *m.b29*m.b30 - 32*m.b28*m.b29*m.b30 + 80*m.b1*m.b2 + 72*m.b1*m.b3 + 64*m.b1*m.b4 + 72*m.b1*m.b5
                        + 64*m.b1*m.b6 + 56*m.b1*m.b7 + 48*m.b1*m.b8 + 160*m.b2*m.b3 + 160*m.b2*m.b4 + 144*m.b2*m.b5 + 
                       160*m.b2*m.b6 + 144*m.b2*m.b7 + 112*m.b2*m.b8 + 48*m.b2*m.b9 + 256*m.b3*m.b4 + 248*m.b3*m.b5 + 
                       256*m.b3*m.b6 + 248*m.b3*m.b7 + 208*m.b3*m.b8 + 112*m.b3*m.b9 + 48*m.b3*m.b10 + 368*m.b4*m.b5 + 
                       336*m.b4*m.b6 + 336*m.b4*m.b7 + 320*m.b4*m.b8 + 208*m.b4*m.b9 + 112*m.b4*m.b10 + 48*m.b4*m.b11 + 
                       464*m.b5*m.b6 + 424*m.b5*m.b7 + 400*m.b5*m.b8 + 320*m.b5*m.b9 + 208*m.b5*m.b10 + 112*m.b5*m.b11
                        + 48*m.b5*m.b12 + 544*m.b6*m.b7 + 496*m.b6*m.b8 + 400*m.b6*m.b9 + 320*m.b6*m.b10 + 208*m.b6*
                       m.b11 + 112*m.b6*m.b12 + 48*m.b6*m.b13 + 624*m.b7*m.b8 + 496*m.b7*m.b9 + 400*m.b7*m.b10 + 320*
                       m.b7*m.b11 + 208*m.b7*m.b12 + 112*m.b7*m.b13 + 48*m.b7*m.b14 + 624*m.b8*m.b9 + 496*m.b8*m.b10 + 
                       400*m.b8*m.b11 + 320*m.b8*m.b12 + 208*m.b8*m.b13 + 112*m.b8*m.b14 + 48*m.b8*m.b15 + 624*m.b9*
                       m.b10 + 496*m.b9*m.b11 + 400*m.b9*m.b12 + 320*m.b9*m.b13 + 208*m.b9*m.b14 + 112*m.b9*m.b15 + 48*
                       m.b9*m.b16 + 624*m.b10*m.b11 + 496*m.b10*m.b12 + 400*m.b10*m.b13 + 320*m.b10*m.b14 + 208*m.b10*
                       m.b15 + 112*m.b10*m.b16 + 48*m.b10*m.b17 + 624*m.b11*m.b12 + 496*m.b11*m.b13 + 400*m.b11*m.b14 + 
                       320*m.b11*m.b15 + 208*m.b11*m.b16 + 112*m.b11*m.b17 + 48*m.b11*m.b18 + 624*m.b12*m.b13 + 496*
                       m.b12*m.b14 + 400*m.b12*m.b15 + 320*m.b12*m.b16 + 208*m.b12*m.b17 + 112*m.b12*m.b18 + 48*m.b12*
                       m.b19 + 624*m.b13*m.b14 + 496*m.b13*m.b15 + 400*m.b13*m.b16 + 320*m.b13*m.b17 + 208*m.b13*m.b18
                        + 112*m.b13*m.b19 + 48*m.b13*m.b20 + 624*m.b14*m.b15 + 496*m.b14*m.b16 + 400*m.b14*m.b17 + 320*
                       m.b14*m.b18 + 208*m.b14*m.b19 + 112*m.b14*m.b20 + 48*m.b14*m.b21 + 624*m.b15*m.b16 + 496*m.b15*
                       m.b17 + 400*m.b15*m.b18 + 320*m.b15*m.b19 + 208*m.b15*m.b20 + 112*m.b15*m.b21 + 48*m.b15*m.b22 + 
                       624*m.b16*m.b17 + 496*m.b16*m.b18 + 400*m.b16*m.b19 + 320*m.b16*m.b20 + 208*m.b16*m.b21 + 112*
                       m.b16*m.b22 + 48*m.b16*m.b23 + 624*m.b17*m.b18 + 496*m.b17*m.b19 + 400*m.b17*m.b20 + 320*m.b17*
                       m.b21 + 208*m.b17*m.b22 + 112*m.b17*m.b23 + 48*m.b17*m.b24 + 624*m.b18*m.b19 + 496*m.b18*m.b20 + 
                       400*m.b18*m.b21 + 320*m.b18*m.b22 + 208*m.b18*m.b23 + 112*m.b18*m.b24 + 48*m.b18*m.b25 + 624*
                       m.b19*m.b20 + 496*m.b19*m.b21 + 400*m.b19*m.b22 + 320*m.b19*m.b23 + 208*m.b19*m.b24 + 112*m.b19*
                       m.b25 + 48*m.b19*m.b26 + 624*m.b20*m.b21 + 496*m.b20*m.b22 + 400*m.b20*m.b23 + 320*m.b20*m.b24 + 
                       208*m.b20*m.b25 + 112*m.b20*m.b26 + 48*m.b20*m.b27 + 624*m.b21*m.b22 + 496*m.b21*m.b23 + 400*
                       m.b21*m.b24 + 320*m.b21*m.b25 + 208*m.b21*m.b26 + 112*m.b21*m.b27 + 48*m.b21*m.b28 + 624*m.b22*
                       m.b23 + 496*m.b22*m.b24 + 400*m.b22*m.b25 + 320*m.b22*m.b26 + 208*m.b22*m.b27 + 112*m.b22*m.b28
                        + 48*m.b22*m.b29 + 624*m.b23*m.b24 + 496*m.b23*m.b25 + 400*m.b23*m.b26 + 320*m.b23*m.b27 + 208*
                       m.b23*m.b28 + 112*m.b23*m.b29 + 48*m.b23*m.b30 + 544*m.b24*m.b25 + 424*m.b24*m.b26 + 336*m.b24*
                       m.b27 + 248*m.b24*m.b28 + 144*m.b24*m.b29 + 56*m.b24*m.b30 + 464*m.b25*m.b26 + 336*m.b25*m.b27 + 
                       256*m.b25*m.b28 + 160*m.b25*m.b29 + 64*m.b25*m.b30 + 368*m.b26*m.b27 + 248*m.b26*m.b28 + 144*
                       m.b26*m.b29 + 72*m.b26*m.b30 + 256*m.b27*m.b28 + 160*m.b27*m.b29 + 64*m.b27*m.b30 + 160*m.b28*
                       m.b29 + 72*m.b28*m.b30 + 80*m.b29*m.b30 - 84*m.b1 - 184*m.b2 - 292*m.b3 - 400*m.b4 - 508*m.b5 - 
                       616*m.b6 - 716*m.b7 - 800*m.b8 - 800*m.b9 - 800*m.b10 - 800*m.b11 - 800*m.b12 - 800*m.b13 - 800*
                       m.b14 - 800*m.b15 - 800*m.b16 - 800*m.b17 - 800*m.b18 - 800*m.b19 - 800*m.b20 - 800*m.b21 - 800*
                       m.b22 - 800*m.b23 - 716*m.b24 - 616*m.b25 - 508*m.b26 - 400*m.b27 - 292*m.b28 - 184*m.b29 - 84*
                       m.b30 - m.x31 <= 0)

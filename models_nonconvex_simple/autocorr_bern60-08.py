#  MINLP written by GAMS Convert at 08/13/20 17:37:55
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         61        1       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         61        1       60        0


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
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x61, sense=minimize)

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
                       320*m.b24*m.b25*m.b26*m.b27 + 256*m.b24*m.b25*m.b27*m.b28 + 192*m.b24*m.b25*m.b28*m.b29 + 128*
                       m.b24*m.b25*m.b29*m.b30 + 64*m.b24*m.b25*m.b30*m.b31 + 192*m.b24*m.b26*m.b27*m.b29 + 128*m.b24*
                       m.b26*m.b28*m.b30 + 64*m.b24*m.b26*m.b29*m.b31 + 64*m.b24*m.b27*m.b28*m.b31 + 320*m.b25*m.b26*
                       m.b27*m.b28 + 256*m.b25*m.b26*m.b28*m.b29 + 192*m.b25*m.b26*m.b29*m.b30 + 128*m.b25*m.b26*m.b30*
                       m.b31 + 64*m.b25*m.b26*m.b31*m.b32 + 192*m.b25*m.b27*m.b28*m.b30 + 128*m.b25*m.b27*m.b29*m.b31 + 
                       64*m.b25*m.b27*m.b30*m.b32 + 64*m.b25*m.b28*m.b29*m.b32 + 320*m.b26*m.b27*m.b28*m.b29 + 256*m.b26
                       *m.b27*m.b29*m.b30 + 192*m.b26*m.b27*m.b30*m.b31 + 128*m.b26*m.b27*m.b31*m.b32 + 64*m.b26*m.b27*
                       m.b32*m.b33 + 192*m.b26*m.b28*m.b29*m.b31 + 128*m.b26*m.b28*m.b30*m.b32 + 64*m.b26*m.b28*m.b31*
                       m.b33 + 64*m.b26*m.b29*m.b30*m.b33 + 320*m.b27*m.b28*m.b29*m.b30 + 256*m.b27*m.b28*m.b30*m.b31 + 
                       192*m.b27*m.b28*m.b31*m.b32 + 128*m.b27*m.b28*m.b32*m.b33 + 64*m.b27*m.b28*m.b33*m.b34 + 192*
                       m.b27*m.b29*m.b30*m.b32 + 128*m.b27*m.b29*m.b31*m.b33 + 64*m.b27*m.b29*m.b32*m.b34 + 64*m.b27*
                       m.b30*m.b31*m.b34 + 320*m.b28*m.b29*m.b30*m.b31 + 256*m.b28*m.b29*m.b31*m.b32 + 192*m.b28*m.b29*
                       m.b32*m.b33 + 128*m.b28*m.b29*m.b33*m.b34 + 64*m.b28*m.b29*m.b34*m.b35 + 192*m.b28*m.b30*m.b31*
                       m.b33 + 128*m.b28*m.b30*m.b32*m.b34 + 64*m.b28*m.b30*m.b33*m.b35 + 64*m.b28*m.b31*m.b32*m.b35 + 
                       320*m.b29*m.b30*m.b31*m.b32 + 256*m.b29*m.b30*m.b32*m.b33 + 192*m.b29*m.b30*m.b33*m.b34 + 128*
                       m.b29*m.b30*m.b34*m.b35 + 64*m.b29*m.b30*m.b35*m.b36 + 192*m.b29*m.b31*m.b32*m.b34 + 128*m.b29*
                       m.b31*m.b33*m.b35 + 64*m.b29*m.b31*m.b34*m.b36 + 64*m.b29*m.b32*m.b33*m.b36 + 320*m.b30*m.b31*
                       m.b32*m.b33 + 256*m.b30*m.b31*m.b33*m.b34 + 192*m.b30*m.b31*m.b34*m.b35 + 128*m.b30*m.b31*m.b35*
                       m.b36 + 64*m.b30*m.b31*m.b36*m.b37 + 192*m.b30*m.b32*m.b33*m.b35 + 128*m.b30*m.b32*m.b34*m.b36 + 
                       64*m.b30*m.b32*m.b35*m.b37 + 64*m.b30*m.b33*m.b34*m.b37 + 320*m.b31*m.b32*m.b33*m.b34 + 256*m.b31
                       *m.b32*m.b34*m.b35 + 192*m.b31*m.b32*m.b35*m.b36 + 128*m.b31*m.b32*m.b36*m.b37 + 64*m.b31*m.b32*
                       m.b37*m.b38 + 192*m.b31*m.b33*m.b34*m.b36 + 128*m.b31*m.b33*m.b35*m.b37 + 64*m.b31*m.b33*m.b36*
                       m.b38 + 64*m.b31*m.b34*m.b35*m.b38 + 320*m.b32*m.b33*m.b34*m.b35 + 256*m.b32*m.b33*m.b35*m.b36 + 
                       192*m.b32*m.b33*m.b36*m.b37 + 128*m.b32*m.b33*m.b37*m.b38 + 64*m.b32*m.b33*m.b38*m.b39 + 192*
                       m.b32*m.b34*m.b35*m.b37 + 128*m.b32*m.b34*m.b36*m.b38 + 64*m.b32*m.b34*m.b37*m.b39 + 64*m.b32*
                       m.b35*m.b36*m.b39 + 320*m.b33*m.b34*m.b35*m.b36 + 256*m.b33*m.b34*m.b36*m.b37 + 192*m.b33*m.b34*
                       m.b37*m.b38 + 128*m.b33*m.b34*m.b38*m.b39 + 64*m.b33*m.b34*m.b39*m.b40 + 192*m.b33*m.b35*m.b36*
                       m.b38 + 128*m.b33*m.b35*m.b37*m.b39 + 64*m.b33*m.b35*m.b38*m.b40 + 64*m.b33*m.b36*m.b37*m.b40 + 
                       320*m.b34*m.b35*m.b36*m.b37 + 256*m.b34*m.b35*m.b37*m.b38 + 192*m.b34*m.b35*m.b38*m.b39 + 128*
                       m.b34*m.b35*m.b39*m.b40 + 64*m.b34*m.b35*m.b40*m.b41 + 192*m.b34*m.b36*m.b37*m.b39 + 128*m.b34*
                       m.b36*m.b38*m.b40 + 64*m.b34*m.b36*m.b39*m.b41 + 64*m.b34*m.b37*m.b38*m.b41 + 320*m.b35*m.b36*
                       m.b37*m.b38 + 256*m.b35*m.b36*m.b38*m.b39 + 192*m.b35*m.b36*m.b39*m.b40 + 128*m.b35*m.b36*m.b40*
                       m.b41 + 64*m.b35*m.b36*m.b41*m.b42 + 192*m.b35*m.b37*m.b38*m.b40 + 128*m.b35*m.b37*m.b39*m.b41 + 
                       64*m.b35*m.b37*m.b40*m.b42 + 64*m.b35*m.b38*m.b39*m.b42 + 320*m.b36*m.b37*m.b38*m.b39 + 256*m.b36
                       *m.b37*m.b39*m.b40 + 192*m.b36*m.b37*m.b40*m.b41 + 128*m.b36*m.b37*m.b41*m.b42 + 64*m.b36*m.b37*
                       m.b42*m.b43 + 192*m.b36*m.b38*m.b39*m.b41 + 128*m.b36*m.b38*m.b40*m.b42 + 64*m.b36*m.b38*m.b41*
                       m.b43 + 64*m.b36*m.b39*m.b40*m.b43 + 320*m.b37*m.b38*m.b39*m.b40 + 256*m.b37*m.b38*m.b40*m.b41 + 
                       192*m.b37*m.b38*m.b41*m.b42 + 128*m.b37*m.b38*m.b42*m.b43 + 64*m.b37*m.b38*m.b43*m.b44 + 192*
                       m.b37*m.b39*m.b40*m.b42 + 128*m.b37*m.b39*m.b41*m.b43 + 64*m.b37*m.b39*m.b42*m.b44 + 64*m.b37*
                       m.b40*m.b41*m.b44 + 320*m.b38*m.b39*m.b40*m.b41 + 256*m.b38*m.b39*m.b41*m.b42 + 192*m.b38*m.b39*
                       m.b42*m.b43 + 128*m.b38*m.b39*m.b43*m.b44 + 64*m.b38*m.b39*m.b44*m.b45 + 192*m.b38*m.b40*m.b41*
                       m.b43 + 128*m.b38*m.b40*m.b42*m.b44 + 64*m.b38*m.b40*m.b43*m.b45 + 64*m.b38*m.b41*m.b42*m.b45 + 
                       320*m.b39*m.b40*m.b41*m.b42 + 256*m.b39*m.b40*m.b42*m.b43 + 192*m.b39*m.b40*m.b43*m.b44 + 128*
                       m.b39*m.b40*m.b44*m.b45 + 64*m.b39*m.b40*m.b45*m.b46 + 192*m.b39*m.b41*m.b42*m.b44 + 128*m.b39*
                       m.b41*m.b43*m.b45 + 64*m.b39*m.b41*m.b44*m.b46 + 64*m.b39*m.b42*m.b43*m.b46 + 320*m.b40*m.b41*
                       m.b42*m.b43 + 256*m.b40*m.b41*m.b43*m.b44 + 192*m.b40*m.b41*m.b44*m.b45 + 128*m.b40*m.b41*m.b45*
                       m.b46 + 64*m.b40*m.b41*m.b46*m.b47 + 192*m.b40*m.b42*m.b43*m.b45 + 128*m.b40*m.b42*m.b44*m.b46 + 
                       64*m.b40*m.b42*m.b45*m.b47 + 64*m.b40*m.b43*m.b44*m.b47 + 320*m.b41*m.b42*m.b43*m.b44 + 256*m.b41
                       *m.b42*m.b44*m.b45 + 192*m.b41*m.b42*m.b45*m.b46 + 128*m.b41*m.b42*m.b46*m.b47 + 64*m.b41*m.b42*
                       m.b47*m.b48 + 192*m.b41*m.b43*m.b44*m.b46 + 128*m.b41*m.b43*m.b45*m.b47 + 64*m.b41*m.b43*m.b46*
                       m.b48 + 64*m.b41*m.b44*m.b45*m.b48 + 320*m.b42*m.b43*m.b44*m.b45 + 256*m.b42*m.b43*m.b45*m.b46 + 
                       192*m.b42*m.b43*m.b46*m.b47 + 128*m.b42*m.b43*m.b47*m.b48 + 64*m.b42*m.b43*m.b48*m.b49 + 192*
                       m.b42*m.b44*m.b45*m.b47 + 128*m.b42*m.b44*m.b46*m.b48 + 64*m.b42*m.b44*m.b47*m.b49 + 64*m.b42*
                       m.b45*m.b46*m.b49 + 320*m.b43*m.b44*m.b45*m.b46 + 256*m.b43*m.b44*m.b46*m.b47 + 192*m.b43*m.b44*
                       m.b47*m.b48 + 128*m.b43*m.b44*m.b48*m.b49 + 64*m.b43*m.b44*m.b49*m.b50 + 192*m.b43*m.b45*m.b46*
                       m.b48 + 128*m.b43*m.b45*m.b47*m.b49 + 64*m.b43*m.b45*m.b48*m.b50 + 64*m.b43*m.b46*m.b47*m.b50 + 
                       320*m.b44*m.b45*m.b46*m.b47 + 256*m.b44*m.b45*m.b47*m.b48 + 192*m.b44*m.b45*m.b48*m.b49 + 128*
                       m.b44*m.b45*m.b49*m.b50 + 64*m.b44*m.b45*m.b50*m.b51 + 192*m.b44*m.b46*m.b47*m.b49 + 128*m.b44*
                       m.b46*m.b48*m.b50 + 64*m.b44*m.b46*m.b49*m.b51 + 64*m.b44*m.b47*m.b48*m.b51 + 320*m.b45*m.b46*
                       m.b47*m.b48 + 256*m.b45*m.b46*m.b48*m.b49 + 192*m.b45*m.b46*m.b49*m.b50 + 128*m.b45*m.b46*m.b50*
                       m.b51 + 64*m.b45*m.b46*m.b51*m.b52 + 192*m.b45*m.b47*m.b48*m.b50 + 128*m.b45*m.b47*m.b49*m.b51 + 
                       64*m.b45*m.b47*m.b50*m.b52 + 64*m.b45*m.b48*m.b49*m.b52 + 320*m.b46*m.b47*m.b48*m.b49 + 256*m.b46
                       *m.b47*m.b49*m.b50 + 192*m.b46*m.b47*m.b50*m.b51 + 128*m.b46*m.b47*m.b51*m.b52 + 64*m.b46*m.b47*
                       m.b52*m.b53 + 192*m.b46*m.b48*m.b49*m.b51 + 128*m.b46*m.b48*m.b50*m.b52 + 64*m.b46*m.b48*m.b51*
                       m.b53 + 64*m.b46*m.b49*m.b50*m.b53 + 320*m.b47*m.b48*m.b49*m.b50 + 256*m.b47*m.b48*m.b50*m.b51 + 
                       192*m.b47*m.b48*m.b51*m.b52 + 128*m.b47*m.b48*m.b52*m.b53 + 64*m.b47*m.b48*m.b53*m.b54 + 192*
                       m.b47*m.b49*m.b50*m.b52 + 128*m.b47*m.b49*m.b51*m.b53 + 64*m.b47*m.b49*m.b52*m.b54 + 64*m.b47*
                       m.b50*m.b51*m.b54 + 320*m.b48*m.b49*m.b50*m.b51 + 256*m.b48*m.b49*m.b51*m.b52 + 192*m.b48*m.b49*
                       m.b52*m.b53 + 128*m.b48*m.b49*m.b53*m.b54 + 64*m.b48*m.b49*m.b54*m.b55 + 192*m.b48*m.b50*m.b51*
                       m.b53 + 128*m.b48*m.b50*m.b52*m.b54 + 64*m.b48*m.b50*m.b53*m.b55 + 64*m.b48*m.b51*m.b52*m.b55 + 
                       320*m.b49*m.b50*m.b51*m.b52 + 256*m.b49*m.b50*m.b52*m.b53 + 192*m.b49*m.b50*m.b53*m.b54 + 128*
                       m.b49*m.b50*m.b54*m.b55 + 64*m.b49*m.b50*m.b55*m.b56 + 192*m.b49*m.b51*m.b52*m.b54 + 128*m.b49*
                       m.b51*m.b53*m.b55 + 64*m.b49*m.b51*m.b54*m.b56 + 64*m.b49*m.b52*m.b53*m.b56 + 320*m.b50*m.b51*
                       m.b52*m.b53 + 256*m.b50*m.b51*m.b53*m.b54 + 192*m.b50*m.b51*m.b54*m.b55 + 128*m.b50*m.b51*m.b55*
                       m.b56 + 64*m.b50*m.b51*m.b56*m.b57 + 192*m.b50*m.b52*m.b53*m.b55 + 128*m.b50*m.b52*m.b54*m.b56 + 
                       64*m.b50*m.b52*m.b55*m.b57 + 64*m.b50*m.b53*m.b54*m.b57 + 320*m.b51*m.b52*m.b53*m.b54 + 256*m.b51
                       *m.b52*m.b54*m.b55 + 192*m.b51*m.b52*m.b55*m.b56 + 128*m.b51*m.b52*m.b56*m.b57 + 64*m.b51*m.b52*
                       m.b57*m.b58 + 192*m.b51*m.b53*m.b54*m.b56 + 128*m.b51*m.b53*m.b55*m.b57 + 64*m.b51*m.b53*m.b56*
                       m.b58 + 64*m.b51*m.b54*m.b55*m.b58 + 320*m.b52*m.b53*m.b54*m.b55 + 256*m.b52*m.b53*m.b55*m.b56 + 
                       192*m.b52*m.b53*m.b56*m.b57 + 128*m.b52*m.b53*m.b57*m.b58 + 64*m.b52*m.b53*m.b58*m.b59 + 192*
                       m.b52*m.b54*m.b55*m.b57 + 128*m.b52*m.b54*m.b56*m.b58 + 64*m.b52*m.b54*m.b57*m.b59 + 64*m.b52*
                       m.b55*m.b56*m.b59 + 320*m.b53*m.b54*m.b55*m.b56 + 256*m.b53*m.b54*m.b56*m.b57 + 192*m.b53*m.b54*
                       m.b57*m.b58 + 128*m.b53*m.b54*m.b58*m.b59 + 64*m.b53*m.b54*m.b59*m.b60 + 192*m.b53*m.b55*m.b56*
                       m.b58 + 128*m.b53*m.b55*m.b57*m.b59 + 64*m.b53*m.b55*m.b58*m.b60 + 64*m.b53*m.b56*m.b57*m.b60 + 
                       256*m.b54*m.b55*m.b56*m.b57 + 192*m.b54*m.b55*m.b57*m.b58 + 128*m.b54*m.b55*m.b58*m.b59 + 64*
                       m.b54*m.b55*m.b59*m.b60 + 128*m.b54*m.b56*m.b57*m.b59 + 64*m.b54*m.b56*m.b58*m.b60 + 192*m.b55*
                       m.b56*m.b57*m.b58 + 128*m.b55*m.b56*m.b58*m.b59 + 64*m.b55*m.b56*m.b59*m.b60 + 64*m.b55*m.b57*
                       m.b58*m.b60 + 128*m.b56*m.b57*m.b58*m.b59 + 64*m.b56*m.b57*m.b59*m.b60 + 64*m.b57*m.b58*m.b59*
                       m.b60 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*
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
                       m.b23*m.b27*m.b30 - 96*m.b23*m.b28*m.b29 - 32*m.b23*m.b28*m.b30 - 32*m.b23*m.b29*m.b30 - 320*
                       m.b24*m.b25*m.b26 - 384*m.b24*m.b25*m.b27 - 256*m.b24*m.b25*m.b28 - 160*m.b24*m.b25*m.b29 - 96*
                       m.b24*m.b25*m.b30 - 32*m.b24*m.b25*m.b31 - 384*m.b24*m.b26*m.b27 - 128*m.b24*m.b26*m.b28 - 128*
                       m.b24*m.b26*m.b29 - 64*m.b24*m.b26*m.b30 - 32*m.b24*m.b26*m.b31 - 256*m.b24*m.b27*m.b28 - 128*
                       m.b24*m.b27*m.b29 - 32*m.b24*m.b27*m.b31 - 160*m.b24*m.b28*m.b29 - 64*m.b24*m.b28*m.b30 - 32*
                       m.b24*m.b28*m.b31 - 96*m.b24*m.b29*m.b30 - 32*m.b24*m.b29*m.b31 - 32*m.b24*m.b30*m.b31 - 320*
                       m.b25*m.b26*m.b27 - 384*m.b25*m.b26*m.b28 - 256*m.b25*m.b26*m.b29 - 160*m.b25*m.b26*m.b30 - 96*
                       m.b25*m.b26*m.b31 - 32*m.b25*m.b26*m.b32 - 384*m.b25*m.b27*m.b28 - 128*m.b25*m.b27*m.b29 - 128*
                       m.b25*m.b27*m.b30 - 64*m.b25*m.b27*m.b31 - 32*m.b25*m.b27*m.b32 - 256*m.b25*m.b28*m.b29 - 128*
                       m.b25*m.b28*m.b30 - 32*m.b25*m.b28*m.b32 - 160*m.b25*m.b29*m.b30 - 64*m.b25*m.b29*m.b31 - 32*
                       m.b25*m.b29*m.b32 - 96*m.b25*m.b30*m.b31 - 32*m.b25*m.b30*m.b32 - 32*m.b25*m.b31*m.b32 - 320*
                       m.b26*m.b27*m.b28 - 384*m.b26*m.b27*m.b29 - 256*m.b26*m.b27*m.b30 - 160*m.b26*m.b27*m.b31 - 96*
                       m.b26*m.b27*m.b32 - 32*m.b26*m.b27*m.b33 - 384*m.b26*m.b28*m.b29 - 128*m.b26*m.b28*m.b30 - 128*
                       m.b26*m.b28*m.b31 - 64*m.b26*m.b28*m.b32 - 32*m.b26*m.b28*m.b33 - 256*m.b26*m.b29*m.b30 - 128*
                       m.b26*m.b29*m.b31 - 32*m.b26*m.b29*m.b33 - 160*m.b26*m.b30*m.b31 - 64*m.b26*m.b30*m.b32 - 32*
                       m.b26*m.b30*m.b33 - 96*m.b26*m.b31*m.b32 - 32*m.b26*m.b31*m.b33 - 32*m.b26*m.b32*m.b33 - 320*
                       m.b27*m.b28*m.b29 - 384*m.b27*m.b28*m.b30 - 256*m.b27*m.b28*m.b31 - 160*m.b27*m.b28*m.b32 - 96*
                       m.b27*m.b28*m.b33 - 32*m.b27*m.b28*m.b34 - 384*m.b27*m.b29*m.b30 - 128*m.b27*m.b29*m.b31 - 128*
                       m.b27*m.b29*m.b32 - 64*m.b27*m.b29*m.b33 - 32*m.b27*m.b29*m.b34 - 256*m.b27*m.b30*m.b31 - 128*
                       m.b27*m.b30*m.b32 - 32*m.b27*m.b30*m.b34 - 160*m.b27*m.b31*m.b32 - 64*m.b27*m.b31*m.b33 - 32*
                       m.b27*m.b31*m.b34 - 96*m.b27*m.b32*m.b33 - 32*m.b27*m.b32*m.b34 - 32*m.b27*m.b33*m.b34 - 320*
                       m.b28*m.b29*m.b30 - 384*m.b28*m.b29*m.b31 - 256*m.b28*m.b29*m.b32 - 160*m.b28*m.b29*m.b33 - 96*
                       m.b28*m.b29*m.b34 - 32*m.b28*m.b29*m.b35 - 384*m.b28*m.b30*m.b31 - 128*m.b28*m.b30*m.b32 - 128*
                       m.b28*m.b30*m.b33 - 64*m.b28*m.b30*m.b34 - 32*m.b28*m.b30*m.b35 - 256*m.b28*m.b31*m.b32 - 128*
                       m.b28*m.b31*m.b33 - 32*m.b28*m.b31*m.b35 - 160*m.b28*m.b32*m.b33 - 64*m.b28*m.b32*m.b34 - 32*
                       m.b28*m.b32*m.b35 - 96*m.b28*m.b33*m.b34 - 32*m.b28*m.b33*m.b35 - 32*m.b28*m.b34*m.b35 - 320*
                       m.b29*m.b30*m.b31 - 384*m.b29*m.b30*m.b32 - 256*m.b29*m.b30*m.b33 - 160*m.b29*m.b30*m.b34 - 96*
                       m.b29*m.b30*m.b35 - 32*m.b29*m.b30*m.b36 - 384*m.b29*m.b31*m.b32 - 128*m.b29*m.b31*m.b33 - 128*
                       m.b29*m.b31*m.b34 - 64*m.b29*m.b31*m.b35 - 32*m.b29*m.b31*m.b36 - 256*m.b29*m.b32*m.b33 - 128*
                       m.b29*m.b32*m.b34 - 32*m.b29*m.b32*m.b36 - 160*m.b29*m.b33*m.b34 - 64*m.b29*m.b33*m.b35 - 32*
                       m.b29*m.b33*m.b36 - 96*m.b29*m.b34*m.b35 - 32*m.b29*m.b34*m.b36 - 32*m.b29*m.b35*m.b36 - 320*
                       m.b30*m.b31*m.b32 - 384*m.b30*m.b31*m.b33 - 256*m.b30*m.b31*m.b34 - 160*m.b30*m.b31*m.b35 - 96*
                       m.b30*m.b31*m.b36 - 32*m.b30*m.b31*m.b37 - 384*m.b30*m.b32*m.b33 - 128*m.b30*m.b32*m.b34 - 128*
                       m.b30*m.b32*m.b35 - 64*m.b30*m.b32*m.b36 - 32*m.b30*m.b32*m.b37 - 256*m.b30*m.b33*m.b34 - 128*
                       m.b30*m.b33*m.b35 - 32*m.b30*m.b33*m.b37 - 160*m.b30*m.b34*m.b35 - 64*m.b30*m.b34*m.b36 - 32*
                       m.b30*m.b34*m.b37 - 96*m.b30*m.b35*m.b36 - 32*m.b30*m.b35*m.b37 - 32*m.b30*m.b36*m.b37 - 320*
                       m.b31*m.b32*m.b33 - 384*m.b31*m.b32*m.b34 - 256*m.b31*m.b32*m.b35 - 160*m.b31*m.b32*m.b36 - 96*
                       m.b31*m.b32*m.b37 - 32*m.b31*m.b32*m.b38 - 384*m.b31*m.b33*m.b34 - 128*m.b31*m.b33*m.b35 - 128*
                       m.b31*m.b33*m.b36 - 64*m.b31*m.b33*m.b37 - 32*m.b31*m.b33*m.b38 - 256*m.b31*m.b34*m.b35 - 128*
                       m.b31*m.b34*m.b36 - 32*m.b31*m.b34*m.b38 - 160*m.b31*m.b35*m.b36 - 64*m.b31*m.b35*m.b37 - 32*
                       m.b31*m.b35*m.b38 - 96*m.b31*m.b36*m.b37 - 32*m.b31*m.b36*m.b38 - 32*m.b31*m.b37*m.b38 - 320*
                       m.b32*m.b33*m.b34 - 384*m.b32*m.b33*m.b35 - 256*m.b32*m.b33*m.b36 - 160*m.b32*m.b33*m.b37 - 96*
                       m.b32*m.b33*m.b38 - 32*m.b32*m.b33*m.b39 - 384*m.b32*m.b34*m.b35 - 128*m.b32*m.b34*m.b36 - 128*
                       m.b32*m.b34*m.b37 - 64*m.b32*m.b34*m.b38 - 32*m.b32*m.b34*m.b39 - 256*m.b32*m.b35*m.b36 - 128*
                       m.b32*m.b35*m.b37 - 32*m.b32*m.b35*m.b39 - 160*m.b32*m.b36*m.b37 - 64*m.b32*m.b36*m.b38 - 32*
                       m.b32*m.b36*m.b39 - 96*m.b32*m.b37*m.b38 - 32*m.b32*m.b37*m.b39 - 32*m.b32*m.b38*m.b39 - 320*
                       m.b33*m.b34*m.b35 - 384*m.b33*m.b34*m.b36 - 256*m.b33*m.b34*m.b37 - 160*m.b33*m.b34*m.b38 - 96*
                       m.b33*m.b34*m.b39 - 32*m.b33*m.b34*m.b40 - 384*m.b33*m.b35*m.b36 - 128*m.b33*m.b35*m.b37 - 128*
                       m.b33*m.b35*m.b38 - 64*m.b33*m.b35*m.b39 - 32*m.b33*m.b35*m.b40 - 256*m.b33*m.b36*m.b37 - 128*
                       m.b33*m.b36*m.b38 - 32*m.b33*m.b36*m.b40 - 160*m.b33*m.b37*m.b38 - 64*m.b33*m.b37*m.b39 - 32*
                       m.b33*m.b37*m.b40 - 96*m.b33*m.b38*m.b39 - 32*m.b33*m.b38*m.b40 - 32*m.b33*m.b39*m.b40 - 320*
                       m.b34*m.b35*m.b36 - 384*m.b34*m.b35*m.b37 - 256*m.b34*m.b35*m.b38 - 160*m.b34*m.b35*m.b39 - 96*
                       m.b34*m.b35*m.b40 - 32*m.b34*m.b35*m.b41 - 384*m.b34*m.b36*m.b37 - 128*m.b34*m.b36*m.b38 - 128*
                       m.b34*m.b36*m.b39 - 64*m.b34*m.b36*m.b40 - 32*m.b34*m.b36*m.b41 - 256*m.b34*m.b37*m.b38 - 128*
                       m.b34*m.b37*m.b39 - 32*m.b34*m.b37*m.b41 - 160*m.b34*m.b38*m.b39 - 64*m.b34*m.b38*m.b40 - 32*
                       m.b34*m.b38*m.b41 - 96*m.b34*m.b39*m.b40 - 32*m.b34*m.b39*m.b41 - 32*m.b34*m.b40*m.b41 - 320*
                       m.b35*m.b36*m.b37 - 384*m.b35*m.b36*m.b38 - 256*m.b35*m.b36*m.b39 - 160*m.b35*m.b36*m.b40 - 96*
                       m.b35*m.b36*m.b41 - 32*m.b35*m.b36*m.b42 - 384*m.b35*m.b37*m.b38 - 128*m.b35*m.b37*m.b39 - 128*
                       m.b35*m.b37*m.b40 - 64*m.b35*m.b37*m.b41 - 32*m.b35*m.b37*m.b42 - 256*m.b35*m.b38*m.b39 - 128*
                       m.b35*m.b38*m.b40 - 32*m.b35*m.b38*m.b42 - 160*m.b35*m.b39*m.b40 - 64*m.b35*m.b39*m.b41 - 32*
                       m.b35*m.b39*m.b42 - 96*m.b35*m.b40*m.b41 - 32*m.b35*m.b40*m.b42 - 32*m.b35*m.b41*m.b42 - 320*
                       m.b36*m.b37*m.b38 - 384*m.b36*m.b37*m.b39 - 256*m.b36*m.b37*m.b40 - 160*m.b36*m.b37*m.b41 - 96*
                       m.b36*m.b37*m.b42 - 32*m.b36*m.b37*m.b43 - 384*m.b36*m.b38*m.b39 - 128*m.b36*m.b38*m.b40 - 128*
                       m.b36*m.b38*m.b41 - 64*m.b36*m.b38*m.b42 - 32*m.b36*m.b38*m.b43 - 256*m.b36*m.b39*m.b40 - 128*
                       m.b36*m.b39*m.b41 - 32*m.b36*m.b39*m.b43 - 160*m.b36*m.b40*m.b41 - 64*m.b36*m.b40*m.b42 - 32*
                       m.b36*m.b40*m.b43 - 96*m.b36*m.b41*m.b42 - 32*m.b36*m.b41*m.b43 - 32*m.b36*m.b42*m.b43 - 320*
                       m.b37*m.b38*m.b39 - 384*m.b37*m.b38*m.b40 - 256*m.b37*m.b38*m.b41 - 160*m.b37*m.b38*m.b42 - 96*
                       m.b37*m.b38*m.b43 - 32*m.b37*m.b38*m.b44 - 384*m.b37*m.b39*m.b40 - 128*m.b37*m.b39*m.b41 - 128*
                       m.b37*m.b39*m.b42 - 64*m.b37*m.b39*m.b43 - 32*m.b37*m.b39*m.b44 - 256*m.b37*m.b40*m.b41 - 128*
                       m.b37*m.b40*m.b42 - 32*m.b37*m.b40*m.b44 - 160*m.b37*m.b41*m.b42 - 64*m.b37*m.b41*m.b43 - 32*
                       m.b37*m.b41*m.b44 - 96*m.b37*m.b42*m.b43 - 32*m.b37*m.b42*m.b44 - 32*m.b37*m.b43*m.b44 - 320*
                       m.b38*m.b39*m.b40 - 384*m.b38*m.b39*m.b41 - 256*m.b38*m.b39*m.b42 - 160*m.b38*m.b39*m.b43 - 96*
                       m.b38*m.b39*m.b44 - 32*m.b38*m.b39*m.b45 - 384*m.b38*m.b40*m.b41 - 128*m.b38*m.b40*m.b42 - 128*
                       m.b38*m.b40*m.b43 - 64*m.b38*m.b40*m.b44 - 32*m.b38*m.b40*m.b45 - 256*m.b38*m.b41*m.b42 - 128*
                       m.b38*m.b41*m.b43 - 32*m.b38*m.b41*m.b45 - 160*m.b38*m.b42*m.b43 - 64*m.b38*m.b42*m.b44 - 32*
                       m.b38*m.b42*m.b45 - 96*m.b38*m.b43*m.b44 - 32*m.b38*m.b43*m.b45 - 32*m.b38*m.b44*m.b45 - 320*
                       m.b39*m.b40*m.b41 - 384*m.b39*m.b40*m.b42 - 256*m.b39*m.b40*m.b43 - 160*m.b39*m.b40*m.b44 - 96*
                       m.b39*m.b40*m.b45 - 32*m.b39*m.b40*m.b46 - 384*m.b39*m.b41*m.b42 - 128*m.b39*m.b41*m.b43 - 128*
                       m.b39*m.b41*m.b44 - 64*m.b39*m.b41*m.b45 - 32*m.b39*m.b41*m.b46 - 256*m.b39*m.b42*m.b43 - 128*
                       m.b39*m.b42*m.b44 - 32*m.b39*m.b42*m.b46 - 160*m.b39*m.b43*m.b44 - 64*m.b39*m.b43*m.b45 - 32*
                       m.b39*m.b43*m.b46 - 96*m.b39*m.b44*m.b45 - 32*m.b39*m.b44*m.b46 - 32*m.b39*m.b45*m.b46 - 320*
                       m.b40*m.b41*m.b42 - 384*m.b40*m.b41*m.b43 - 256*m.b40*m.b41*m.b44 - 160*m.b40*m.b41*m.b45 - 96*
                       m.b40*m.b41*m.b46 - 32*m.b40*m.b41*m.b47 - 384*m.b40*m.b42*m.b43 - 128*m.b40*m.b42*m.b44 - 128*
                       m.b40*m.b42*m.b45 - 64*m.b40*m.b42*m.b46 - 32*m.b40*m.b42*m.b47 - 256*m.b40*m.b43*m.b44 - 128*
                       m.b40*m.b43*m.b45 - 32*m.b40*m.b43*m.b47 - 160*m.b40*m.b44*m.b45 - 64*m.b40*m.b44*m.b46 - 32*
                       m.b40*m.b44*m.b47 - 96*m.b40*m.b45*m.b46 - 32*m.b40*m.b45*m.b47 - 32*m.b40*m.b46*m.b47 - 320*
                       m.b41*m.b42*m.b43 - 384*m.b41*m.b42*m.b44 - 256*m.b41*m.b42*m.b45 - 160*m.b41*m.b42*m.b46 - 96*
                       m.b41*m.b42*m.b47 - 32*m.b41*m.b42*m.b48 - 384*m.b41*m.b43*m.b44 - 128*m.b41*m.b43*m.b45 - 128*
                       m.b41*m.b43*m.b46 - 64*m.b41*m.b43*m.b47 - 32*m.b41*m.b43*m.b48 - 256*m.b41*m.b44*m.b45 - 128*
                       m.b41*m.b44*m.b46 - 32*m.b41*m.b44*m.b48 - 160*m.b41*m.b45*m.b46 - 64*m.b41*m.b45*m.b47 - 32*
                       m.b41*m.b45*m.b48 - 96*m.b41*m.b46*m.b47 - 32*m.b41*m.b46*m.b48 - 32*m.b41*m.b47*m.b48 - 320*
                       m.b42*m.b43*m.b44 - 384*m.b42*m.b43*m.b45 - 256*m.b42*m.b43*m.b46 - 160*m.b42*m.b43*m.b47 - 96*
                       m.b42*m.b43*m.b48 - 32*m.b42*m.b43*m.b49 - 384*m.b42*m.b44*m.b45 - 128*m.b42*m.b44*m.b46 - 128*
                       m.b42*m.b44*m.b47 - 64*m.b42*m.b44*m.b48 - 32*m.b42*m.b44*m.b49 - 256*m.b42*m.b45*m.b46 - 128*
                       m.b42*m.b45*m.b47 - 32*m.b42*m.b45*m.b49 - 160*m.b42*m.b46*m.b47 - 64*m.b42*m.b46*m.b48 - 32*
                       m.b42*m.b46*m.b49 - 96*m.b42*m.b47*m.b48 - 32*m.b42*m.b47*m.b49 - 32*m.b42*m.b48*m.b49 - 320*
                       m.b43*m.b44*m.b45 - 384*m.b43*m.b44*m.b46 - 256*m.b43*m.b44*m.b47 - 160*m.b43*m.b44*m.b48 - 96*
                       m.b43*m.b44*m.b49 - 32*m.b43*m.b44*m.b50 - 384*m.b43*m.b45*m.b46 - 128*m.b43*m.b45*m.b47 - 128*
                       m.b43*m.b45*m.b48 - 64*m.b43*m.b45*m.b49 - 32*m.b43*m.b45*m.b50 - 256*m.b43*m.b46*m.b47 - 128*
                       m.b43*m.b46*m.b48 - 32*m.b43*m.b46*m.b50 - 160*m.b43*m.b47*m.b48 - 64*m.b43*m.b47*m.b49 - 32*
                       m.b43*m.b47*m.b50 - 96*m.b43*m.b48*m.b49 - 32*m.b43*m.b48*m.b50 - 32*m.b43*m.b49*m.b50 - 320*
                       m.b44*m.b45*m.b46 - 384*m.b44*m.b45*m.b47 - 256*m.b44*m.b45*m.b48 - 160*m.b44*m.b45*m.b49 - 96*
                       m.b44*m.b45*m.b50 - 32*m.b44*m.b45*m.b51 - 384*m.b44*m.b46*m.b47 - 128*m.b44*m.b46*m.b48 - 128*
                       m.b44*m.b46*m.b49 - 64*m.b44*m.b46*m.b50 - 32*m.b44*m.b46*m.b51 - 256*m.b44*m.b47*m.b48 - 128*
                       m.b44*m.b47*m.b49 - 32*m.b44*m.b47*m.b51 - 160*m.b44*m.b48*m.b49 - 64*m.b44*m.b48*m.b50 - 32*
                       m.b44*m.b48*m.b51 - 96*m.b44*m.b49*m.b50 - 32*m.b44*m.b49*m.b51 - 32*m.b44*m.b50*m.b51 - 320*
                       m.b45*m.b46*m.b47 - 384*m.b45*m.b46*m.b48 - 256*m.b45*m.b46*m.b49 - 160*m.b45*m.b46*m.b50 - 96*
                       m.b45*m.b46*m.b51 - 32*m.b45*m.b46*m.b52 - 384*m.b45*m.b47*m.b48 - 128*m.b45*m.b47*m.b49 - 128*
                       m.b45*m.b47*m.b50 - 64*m.b45*m.b47*m.b51 - 32*m.b45*m.b47*m.b52 - 256*m.b45*m.b48*m.b49 - 128*
                       m.b45*m.b48*m.b50 - 32*m.b45*m.b48*m.b52 - 160*m.b45*m.b49*m.b50 - 64*m.b45*m.b49*m.b51 - 32*
                       m.b45*m.b49*m.b52 - 96*m.b45*m.b50*m.b51 - 32*m.b45*m.b50*m.b52 - 32*m.b45*m.b51*m.b52 - 320*
                       m.b46*m.b47*m.b48 - 384*m.b46*m.b47*m.b49 - 256*m.b46*m.b47*m.b50 - 160*m.b46*m.b47*m.b51 - 96*
                       m.b46*m.b47*m.b52 - 32*m.b46*m.b47*m.b53 - 384*m.b46*m.b48*m.b49 - 128*m.b46*m.b48*m.b50 - 128*
                       m.b46*m.b48*m.b51 - 64*m.b46*m.b48*m.b52 - 32*m.b46*m.b48*m.b53 - 256*m.b46*m.b49*m.b50 - 128*
                       m.b46*m.b49*m.b51 - 32*m.b46*m.b49*m.b53 - 160*m.b46*m.b50*m.b51 - 64*m.b46*m.b50*m.b52 - 32*
                       m.b46*m.b50*m.b53 - 96*m.b46*m.b51*m.b52 - 32*m.b46*m.b51*m.b53 - 32*m.b46*m.b52*m.b53 - 320*
                       m.b47*m.b48*m.b49 - 384*m.b47*m.b48*m.b50 - 256*m.b47*m.b48*m.b51 - 160*m.b47*m.b48*m.b52 - 96*
                       m.b47*m.b48*m.b53 - 32*m.b47*m.b48*m.b54 - 384*m.b47*m.b49*m.b50 - 128*m.b47*m.b49*m.b51 - 128*
                       m.b47*m.b49*m.b52 - 64*m.b47*m.b49*m.b53 - 32*m.b47*m.b49*m.b54 - 256*m.b47*m.b50*m.b51 - 128*
                       m.b47*m.b50*m.b52 - 32*m.b47*m.b50*m.b54 - 160*m.b47*m.b51*m.b52 - 64*m.b47*m.b51*m.b53 - 32*
                       m.b47*m.b51*m.b54 - 96*m.b47*m.b52*m.b53 - 32*m.b47*m.b52*m.b54 - 32*m.b47*m.b53*m.b54 - 320*
                       m.b48*m.b49*m.b50 - 384*m.b48*m.b49*m.b51 - 256*m.b48*m.b49*m.b52 - 160*m.b48*m.b49*m.b53 - 96*
                       m.b48*m.b49*m.b54 - 32*m.b48*m.b49*m.b55 - 384*m.b48*m.b50*m.b51 - 128*m.b48*m.b50*m.b52 - 128*
                       m.b48*m.b50*m.b53 - 64*m.b48*m.b50*m.b54 - 32*m.b48*m.b50*m.b55 - 256*m.b48*m.b51*m.b52 - 128*
                       m.b48*m.b51*m.b53 - 32*m.b48*m.b51*m.b55 - 160*m.b48*m.b52*m.b53 - 64*m.b48*m.b52*m.b54 - 32*
                       m.b48*m.b52*m.b55 - 96*m.b48*m.b53*m.b54 - 32*m.b48*m.b53*m.b55 - 32*m.b48*m.b54*m.b55 - 320*
                       m.b49*m.b50*m.b51 - 384*m.b49*m.b50*m.b52 - 256*m.b49*m.b50*m.b53 - 160*m.b49*m.b50*m.b54 - 96*
                       m.b49*m.b50*m.b55 - 32*m.b49*m.b50*m.b56 - 384*m.b49*m.b51*m.b52 - 128*m.b49*m.b51*m.b53 - 128*
                       m.b49*m.b51*m.b54 - 64*m.b49*m.b51*m.b55 - 32*m.b49*m.b51*m.b56 - 256*m.b49*m.b52*m.b53 - 128*
                       m.b49*m.b52*m.b54 - 32*m.b49*m.b52*m.b56 - 160*m.b49*m.b53*m.b54 - 64*m.b49*m.b53*m.b55 - 32*
                       m.b49*m.b53*m.b56 - 96*m.b49*m.b54*m.b55 - 32*m.b49*m.b54*m.b56 - 32*m.b49*m.b55*m.b56 - 320*
                       m.b50*m.b51*m.b52 - 384*m.b50*m.b51*m.b53 - 256*m.b50*m.b51*m.b54 - 160*m.b50*m.b51*m.b55 - 96*
                       m.b50*m.b51*m.b56 - 32*m.b50*m.b51*m.b57 - 384*m.b50*m.b52*m.b53 - 128*m.b50*m.b52*m.b54 - 128*
                       m.b50*m.b52*m.b55 - 64*m.b50*m.b52*m.b56 - 32*m.b50*m.b52*m.b57 - 256*m.b50*m.b53*m.b54 - 128*
                       m.b50*m.b53*m.b55 - 32*m.b50*m.b53*m.b57 - 160*m.b50*m.b54*m.b55 - 64*m.b50*m.b54*m.b56 - 32*
                       m.b50*m.b54*m.b57 - 96*m.b50*m.b55*m.b56 - 32*m.b50*m.b55*m.b57 - 32*m.b50*m.b56*m.b57 - 320*
                       m.b51*m.b52*m.b53 - 384*m.b51*m.b52*m.b54 - 256*m.b51*m.b52*m.b55 - 160*m.b51*m.b52*m.b56 - 96*
                       m.b51*m.b52*m.b57 - 32*m.b51*m.b52*m.b58 - 384*m.b51*m.b53*m.b54 - 128*m.b51*m.b53*m.b55 - 128*
                       m.b51*m.b53*m.b56 - 64*m.b51*m.b53*m.b57 - 32*m.b51*m.b53*m.b58 - 256*m.b51*m.b54*m.b55 - 128*
                       m.b51*m.b54*m.b56 - 32*m.b51*m.b54*m.b58 - 160*m.b51*m.b55*m.b56 - 64*m.b51*m.b55*m.b57 - 32*
                       m.b51*m.b55*m.b58 - 96*m.b51*m.b56*m.b57 - 32*m.b51*m.b56*m.b58 - 32*m.b51*m.b57*m.b58 - 320*
                       m.b52*m.b53*m.b54 - 384*m.b52*m.b53*m.b55 - 256*m.b52*m.b53*m.b56 - 160*m.b52*m.b53*m.b57 - 96*
                       m.b52*m.b53*m.b58 - 32*m.b52*m.b53*m.b59 - 384*m.b52*m.b54*m.b55 - 128*m.b52*m.b54*m.b56 - 128*
                       m.b52*m.b54*m.b57 - 64*m.b52*m.b54*m.b58 - 32*m.b52*m.b54*m.b59 - 256*m.b52*m.b55*m.b56 - 128*
                       m.b52*m.b55*m.b57 - 32*m.b52*m.b55*m.b59 - 160*m.b52*m.b56*m.b57 - 64*m.b52*m.b56*m.b58 - 32*
                       m.b52*m.b56*m.b59 - 96*m.b52*m.b57*m.b58 - 32*m.b52*m.b57*m.b59 - 32*m.b52*m.b58*m.b59 - 320*
                       m.b53*m.b54*m.b55 - 384*m.b53*m.b54*m.b56 - 256*m.b53*m.b54*m.b57 - 160*m.b53*m.b54*m.b58 - 96*
                       m.b53*m.b54*m.b59 - 32*m.b53*m.b54*m.b60 - 384*m.b53*m.b55*m.b56 - 128*m.b53*m.b55*m.b57 - 128*
                       m.b53*m.b55*m.b58 - 64*m.b53*m.b55*m.b59 - 32*m.b53*m.b55*m.b60 - 256*m.b53*m.b56*m.b57 - 128*
                       m.b53*m.b56*m.b58 - 32*m.b53*m.b56*m.b60 - 160*m.b53*m.b57*m.b58 - 64*m.b53*m.b57*m.b59 - 32*
                       m.b53*m.b57*m.b60 - 96*m.b53*m.b58*m.b59 - 32*m.b53*m.b58*m.b60 - 32*m.b53*m.b59*m.b60 - 288*
                       m.b54*m.b55*m.b56 - 320*m.b54*m.b55*m.b57 - 192*m.b54*m.b55*m.b58 - 96*m.b54*m.b55*m.b59 - 32*
                       m.b54*m.b55*m.b60 - 320*m.b54*m.b56*m.b57 - 96*m.b54*m.b56*m.b58 - 64*m.b54*m.b56*m.b59 - 32*
                       m.b54*m.b56*m.b60 - 192*m.b54*m.b57*m.b58 - 96*m.b54*m.b57*m.b59 - 128*m.b54*m.b58*m.b59 - 32*
                       m.b54*m.b58*m.b60 - 64*m.b54*m.b59*m.b60 - 224*m.b55*m.b56*m.b57 - 256*m.b55*m.b56*m.b58 - 128*
                       m.b55*m.b56*m.b59 - 32*m.b55*m.b56*m.b60 - 224*m.b55*m.b57*m.b58 - 64*m.b55*m.b57*m.b59 - 32*
                       m.b55*m.b57*m.b60 - 128*m.b55*m.b58*m.b59 - 64*m.b55*m.b58*m.b60 - 64*m.b55*m.b59*m.b60 - 160*
                       m.b56*m.b57*m.b58 - 160*m.b56*m.b57*m.b59 - 64*m.b56*m.b57*m.b60 - 128*m.b56*m.b58*m.b59 - 32*
                       m.b56*m.b58*m.b60 - 64*m.b56*m.b59*m.b60 - 96*m.b57*m.b58*m.b59 - 64*m.b57*m.b58*m.b60 - 64*m.b57
                       *m.b59*m.b60 - 32*m.b58*m.b59*m.b60 + 80*m.b1*m.b2 + 72*m.b1*m.b3 + 64*m.b1*m.b4 + 72*m.b1*m.b5
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
                       m.b23*m.b28 + 112*m.b23*m.b29 + 48*m.b23*m.b30 + 624*m.b24*m.b25 + 496*m.b24*m.b26 + 400*m.b24*
                       m.b27 + 320*m.b24*m.b28 + 208*m.b24*m.b29 + 112*m.b24*m.b30 + 48*m.b24*m.b31 + 624*m.b25*m.b26 + 
                       496*m.b25*m.b27 + 400*m.b25*m.b28 + 320*m.b25*m.b29 + 208*m.b25*m.b30 + 112*m.b25*m.b31 + 48*
                       m.b25*m.b32 + 624*m.b26*m.b27 + 496*m.b26*m.b28 + 400*m.b26*m.b29 + 320*m.b26*m.b30 + 208*m.b26*
                       m.b31 + 112*m.b26*m.b32 + 48*m.b26*m.b33 + 624*m.b27*m.b28 + 496*m.b27*m.b29 + 400*m.b27*m.b30 + 
                       320*m.b27*m.b31 + 208*m.b27*m.b32 + 112*m.b27*m.b33 + 48*m.b27*m.b34 + 624*m.b28*m.b29 + 496*
                       m.b28*m.b30 + 400*m.b28*m.b31 + 320*m.b28*m.b32 + 208*m.b28*m.b33 + 112*m.b28*m.b34 + 48*m.b28*
                       m.b35 + 624*m.b29*m.b30 + 496*m.b29*m.b31 + 400*m.b29*m.b32 + 320*m.b29*m.b33 + 208*m.b29*m.b34
                        + 112*m.b29*m.b35 + 48*m.b29*m.b36 + 624*m.b30*m.b31 + 496*m.b30*m.b32 + 400*m.b30*m.b33 + 320*
                       m.b30*m.b34 + 208*m.b30*m.b35 + 112*m.b30*m.b36 + 48*m.b30*m.b37 + 624*m.b31*m.b32 + 496*m.b31*
                       m.b33 + 400*m.b31*m.b34 + 320*m.b31*m.b35 + 208*m.b31*m.b36 + 112*m.b31*m.b37 + 48*m.b31*m.b38 + 
                       624*m.b32*m.b33 + 496*m.b32*m.b34 + 400*m.b32*m.b35 + 320*m.b32*m.b36 + 208*m.b32*m.b37 + 112*
                       m.b32*m.b38 + 48*m.b32*m.b39 + 624*m.b33*m.b34 + 496*m.b33*m.b35 + 400*m.b33*m.b36 + 320*m.b33*
                       m.b37 + 208*m.b33*m.b38 + 112*m.b33*m.b39 + 48*m.b33*m.b40 + 624*m.b34*m.b35 + 496*m.b34*m.b36 + 
                       400*m.b34*m.b37 + 320*m.b34*m.b38 + 208*m.b34*m.b39 + 112*m.b34*m.b40 + 48*m.b34*m.b41 + 624*
                       m.b35*m.b36 + 496*m.b35*m.b37 + 400*m.b35*m.b38 + 320*m.b35*m.b39 + 208*m.b35*m.b40 + 112*m.b35*
                       m.b41 + 48*m.b35*m.b42 + 624*m.b36*m.b37 + 496*m.b36*m.b38 + 400*m.b36*m.b39 + 320*m.b36*m.b40 + 
                       208*m.b36*m.b41 + 112*m.b36*m.b42 + 48*m.b36*m.b43 + 624*m.b37*m.b38 + 496*m.b37*m.b39 + 400*
                       m.b37*m.b40 + 320*m.b37*m.b41 + 208*m.b37*m.b42 + 112*m.b37*m.b43 + 48*m.b37*m.b44 + 624*m.b38*
                       m.b39 + 496*m.b38*m.b40 + 400*m.b38*m.b41 + 320*m.b38*m.b42 + 208*m.b38*m.b43 + 112*m.b38*m.b44
                        + 48*m.b38*m.b45 + 624*m.b39*m.b40 + 496*m.b39*m.b41 + 400*m.b39*m.b42 + 320*m.b39*m.b43 + 208*
                       m.b39*m.b44 + 112*m.b39*m.b45 + 48*m.b39*m.b46 + 624*m.b40*m.b41 + 496*m.b40*m.b42 + 400*m.b40*
                       m.b43 + 320*m.b40*m.b44 + 208*m.b40*m.b45 + 112*m.b40*m.b46 + 48*m.b40*m.b47 + 624*m.b41*m.b42 + 
                       496*m.b41*m.b43 + 400*m.b41*m.b44 + 320*m.b41*m.b45 + 208*m.b41*m.b46 + 112*m.b41*m.b47 + 48*
                       m.b41*m.b48 + 624*m.b42*m.b43 + 496*m.b42*m.b44 + 400*m.b42*m.b45 + 320*m.b42*m.b46 + 208*m.b42*
                       m.b47 + 112*m.b42*m.b48 + 48*m.b42*m.b49 + 624*m.b43*m.b44 + 496*m.b43*m.b45 + 400*m.b43*m.b46 + 
                       320*m.b43*m.b47 + 208*m.b43*m.b48 + 112*m.b43*m.b49 + 48*m.b43*m.b50 + 624*m.b44*m.b45 + 496*
                       m.b44*m.b46 + 400*m.b44*m.b47 + 320*m.b44*m.b48 + 208*m.b44*m.b49 + 112*m.b44*m.b50 + 48*m.b44*
                       m.b51 + 624*m.b45*m.b46 + 496*m.b45*m.b47 + 400*m.b45*m.b48 + 320*m.b45*m.b49 + 208*m.b45*m.b50
                        + 112*m.b45*m.b51 + 48*m.b45*m.b52 + 624*m.b46*m.b47 + 496*m.b46*m.b48 + 400*m.b46*m.b49 + 320*
                       m.b46*m.b50 + 208*m.b46*m.b51 + 112*m.b46*m.b52 + 48*m.b46*m.b53 + 624*m.b47*m.b48 + 496*m.b47*
                       m.b49 + 400*m.b47*m.b50 + 320*m.b47*m.b51 + 208*m.b47*m.b52 + 112*m.b47*m.b53 + 48*m.b47*m.b54 + 
                       624*m.b48*m.b49 + 496*m.b48*m.b50 + 400*m.b48*m.b51 + 320*m.b48*m.b52 + 208*m.b48*m.b53 + 112*
                       m.b48*m.b54 + 48*m.b48*m.b55 + 624*m.b49*m.b50 + 496*m.b49*m.b51 + 400*m.b49*m.b52 + 320*m.b49*
                       m.b53 + 208*m.b49*m.b54 + 112*m.b49*m.b55 + 48*m.b49*m.b56 + 624*m.b50*m.b51 + 496*m.b50*m.b52 + 
                       400*m.b50*m.b53 + 320*m.b50*m.b54 + 208*m.b50*m.b55 + 112*m.b50*m.b56 + 48*m.b50*m.b57 + 624*
                       m.b51*m.b52 + 496*m.b51*m.b53 + 400*m.b51*m.b54 + 320*m.b51*m.b55 + 208*m.b51*m.b56 + 112*m.b51*
                       m.b57 + 48*m.b51*m.b58 + 624*m.b52*m.b53 + 496*m.b52*m.b54 + 400*m.b52*m.b55 + 320*m.b52*m.b56 + 
                       208*m.b52*m.b57 + 112*m.b52*m.b58 + 48*m.b52*m.b59 + 624*m.b53*m.b54 + 496*m.b53*m.b55 + 400*
                       m.b53*m.b56 + 320*m.b53*m.b57 + 208*m.b53*m.b58 + 112*m.b53*m.b59 + 48*m.b53*m.b60 + 544*m.b54*
                       m.b55 + 424*m.b54*m.b56 + 336*m.b54*m.b57 + 248*m.b54*m.b58 + 144*m.b54*m.b59 + 56*m.b54*m.b60 + 
                       464*m.b55*m.b56 + 336*m.b55*m.b57 + 256*m.b55*m.b58 + 160*m.b55*m.b59 + 64*m.b55*m.b60 + 368*
                       m.b56*m.b57 + 248*m.b56*m.b58 + 144*m.b56*m.b59 + 72*m.b56*m.b60 + 256*m.b57*m.b58 + 160*m.b57*
                       m.b59 + 64*m.b57*m.b60 + 160*m.b58*m.b59 + 72*m.b58*m.b60 + 80*m.b59*m.b60 - 84*m.b1 - 184*m.b2
                        - 292*m.b3 - 400*m.b4 - 508*m.b5 - 616*m.b6 - 716*m.b7 - 800*m.b8 - 800*m.b9 - 800*m.b10 - 800*
                       m.b11 - 800*m.b12 - 800*m.b13 - 800*m.b14 - 800*m.b15 - 800*m.b16 - 800*m.b17 - 800*m.b18 - 800*
                       m.b19 - 800*m.b20 - 800*m.b21 - 800*m.b22 - 800*m.b23 - 800*m.b24 - 800*m.b25 - 800*m.b26 - 800*
                       m.b27 - 800*m.b28 - 800*m.b29 - 800*m.b30 - 800*m.b31 - 800*m.b32 - 800*m.b33 - 800*m.b34 - 800*
                       m.b35 - 800*m.b36 - 800*m.b37 - 800*m.b38 - 800*m.b39 - 800*m.b40 - 800*m.b41 - 800*m.b42 - 800*
                       m.b43 - 800*m.b44 - 800*m.b45 - 800*m.b46 - 800*m.b47 - 800*m.b48 - 800*m.b49 - 800*m.b50 - 800*
                       m.b51 - 800*m.b52 - 800*m.b53 - 716*m.b54 - 616*m.b55 - 508*m.b56 - 400*m.b57 - 292*m.b58 - 184*
                       m.b59 - 84*m.b60 - m.x61 <= 0)

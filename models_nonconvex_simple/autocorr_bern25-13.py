#  MINLP written by GAMS Convert at 08/13/20 17:37:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         26        1       25        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         26        1       25        0


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
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x26, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*
                       m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*
                       m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3*m.b10*m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b4*m.b5*
                       m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*
                       m.b9*m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11 + 64*
                       m.b1*m.b5*m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b6*m.b7*m.b12 + 64*m.b1*m.b6*m.b8*
                       m.b13 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 128*m.b2*
                       m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*m.b10 + 128*m.b2*m.b3*m.b10*m.b11
                        + 128*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*m.b12*m.b13 + 64*m.b2*m.b3*m.b13*m.b14 + 128*m.b2*
                       m.b4*m.b5*m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 
                       128*m.b2*m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*m.b11*m.b13 + 64*m.b2*m.b4*
                       m.b12*m.b14 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5*m.b7*m.b10 + 128*m.b2*m.b5*m.b8*m.b11 + 128
                       *m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*m.b13 + 64*m.b2*m.b5*m.b11*m.b14 + 128*m.b2*m.b6*m.b7
                       *m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*m.b13 + 64*m.b2*m.b6*m.b10*m.b14 + 128*
                       m.b2*m.b7*m.b8*m.b13 + 64*m.b2*m.b7*m.b9*m.b14 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*
                       m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*m.b10 + 192*m.b3*
                       m.b4*m.b10*m.b11 + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b4*m.b12*m.b13 + 128*m.b3*m.b4*m.b13*
                       m.b14 + 64*m.b3*m.b4*m.b14*m.b15 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*
                       m.b5*m.b8*m.b10 + 192*m.b3*m.b5*m.b9*m.b11 + 192*m.b3*m.b5*m.b10*m.b12 + 192*m.b3*m.b5*m.b11*
                       m.b13 + 128*m.b3*m.b5*m.b12*m.b14 + 64*m.b3*m.b5*m.b13*m.b15 + 192*m.b3*m.b6*m.b7*m.b10 + 192*
                       m.b3*m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*m.b10*m.b13 + 128*m.b3*m.b6*m.b11
                       *m.b14 + 64*m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b7*m.b8*m.b12 + 192*m.b3*m.b7*m.b9*m.b13 + 128*
                       m.b3*m.b7*m.b10*m.b14 + 64*m.b3*m.b7*m.b11*m.b15 + 128*m.b3*m.b8*m.b9*m.b14 + 64*m.b3*m.b8*m.b10*
                       m.b15 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*m.b4*m.b5*m.b8*m.b9 + 256*m.b4*
                       m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5*m.b11*m.b12 + 256*m.b4*m.b5*m.b12*
                       m.b13 + 192*m.b4*m.b5*m.b13*m.b14 + 128*m.b4*m.b5*m.b14*m.b15 + 64*m.b4*m.b5*m.b15*m.b16 + 256*
                       m.b4*m.b6*m.b7*m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11 + 256*m.b4*m.b6*m.b10*
                       m.b12 + 256*m.b4*m.b6*m.b11*m.b13 + 192*m.b4*m.b6*m.b12*m.b14 + 128*m.b4*m.b6*m.b13*m.b15 + 64*
                       m.b4*m.b6*m.b14*m.b16 + 256*m.b4*m.b7*m.b8*m.b11 + 256*m.b4*m.b7*m.b9*m.b12 + 256*m.b4*m.b7*m.b10
                       *m.b13 + 192*m.b4*m.b7*m.b11*m.b14 + 128*m.b4*m.b7*m.b12*m.b15 + 64*m.b4*m.b7*m.b13*m.b16 + 256*
                       m.b4*m.b8*m.b9*m.b13 + 192*m.b4*m.b8*m.b10*m.b14 + 128*m.b4*m.b8*m.b11*m.b15 + 64*m.b4*m.b8*m.b12
                       *m.b16 + 128*m.b4*m.b9*m.b10*m.b15 + 64*m.b4*m.b9*m.b11*m.b16 + 320*m.b5*m.b6*m.b7*m.b8 + 320*
                       m.b5*m.b6*m.b8*m.b9 + 320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*m.b10*m.b11 + 320*m.b5*m.b6*m.b11*
                       m.b12 + 320*m.b5*m.b6*m.b12*m.b13 + 256*m.b5*m.b6*m.b13*m.b14 + 192*m.b5*m.b6*m.b14*m.b15 + 128*
                       m.b5*m.b6*m.b15*m.b16 + 64*m.b5*m.b6*m.b16*m.b17 + 320*m.b5*m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*
                       m.b11 + 320*m.b5*m.b7*m.b10*m.b12 + 320*m.b5*m.b7*m.b11*m.b13 + 256*m.b5*m.b7*m.b12*m.b14 + 192*
                       m.b5*m.b7*m.b13*m.b15 + 128*m.b5*m.b7*m.b14*m.b16 + 64*m.b5*m.b7*m.b15*m.b17 + 320*m.b5*m.b8*m.b9
                       *m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 256*m.b5*m.b8*m.b11*m.b14 + 192*m.b5*m.b8*m.b12*m.b15 + 128*
                       m.b5*m.b8*m.b13*m.b16 + 64*m.b5*m.b8*m.b14*m.b17 + 256*m.b5*m.b9*m.b10*m.b14 + 192*m.b5*m.b9*
                       m.b11*m.b15 + 128*m.b5*m.b9*m.b12*m.b16 + 64*m.b5*m.b9*m.b13*m.b17 + 128*m.b5*m.b10*m.b11*m.b16
                        + 64*m.b5*m.b10*m.b12*m.b17 + 384*m.b6*m.b7*m.b8*m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7
                       *m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12 + 384*m.b6*m.b7*m.b12*m.b13 + 320*m.b6*m.b7*m.b13*m.b14
                        + 256*m.b6*m.b7*m.b14*m.b15 + 192*m.b6*m.b7*m.b15*m.b16 + 128*m.b6*m.b7*m.b16*m.b17 + 64*m.b6*
                       m.b7*m.b17*m.b18 + 384*m.b6*m.b8*m.b9*m.b11 + 384*m.b6*m.b8*m.b10*m.b12 + 384*m.b6*m.b8*m.b11*
                       m.b13 + 320*m.b6*m.b8*m.b12*m.b14 + 256*m.b6*m.b8*m.b13*m.b15 + 192*m.b6*m.b8*m.b14*m.b16 + 128*
                       m.b6*m.b8*m.b15*m.b17 + 64*m.b6*m.b8*m.b16*m.b18 + 384*m.b6*m.b9*m.b10*m.b13 + 320*m.b6*m.b9*
                       m.b11*m.b14 + 256*m.b6*m.b9*m.b12*m.b15 + 192*m.b6*m.b9*m.b13*m.b16 + 128*m.b6*m.b9*m.b14*m.b17
                        + 64*m.b6*m.b9*m.b15*m.b18 + 256*m.b6*m.b10*m.b11*m.b15 + 192*m.b6*m.b10*m.b12*m.b16 + 128*m.b6*
                       m.b10*m.b13*m.b17 + 64*m.b6*m.b10*m.b14*m.b18 + 128*m.b6*m.b11*m.b12*m.b17 + 64*m.b6*m.b11*m.b13*
                       m.b18 + 448*m.b7*m.b8*m.b9*m.b10 + 448*m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*m.b11*m.b12 + 448*
                       m.b7*m.b8*m.b12*m.b13 + 384*m.b7*m.b8*m.b13*m.b14 + 320*m.b7*m.b8*m.b14*m.b15 + 256*m.b7*m.b8*
                       m.b15*m.b16 + 192*m.b7*m.b8*m.b16*m.b17 + 128*m.b7*m.b8*m.b17*m.b18 + 64*m.b7*m.b8*m.b18*m.b19 + 
                       448*m.b7*m.b9*m.b10*m.b12 + 448*m.b7*m.b9*m.b11*m.b13 + 384*m.b7*m.b9*m.b12*m.b14 + 320*m.b7*m.b9
                       *m.b13*m.b15 + 256*m.b7*m.b9*m.b14*m.b16 + 192*m.b7*m.b9*m.b15*m.b17 + 128*m.b7*m.b9*m.b16*m.b18
                        + 64*m.b7*m.b9*m.b17*m.b19 + 384*m.b7*m.b10*m.b11*m.b14 + 320*m.b7*m.b10*m.b12*m.b15 + 256*m.b7*
                       m.b10*m.b13*m.b16 + 192*m.b7*m.b10*m.b14*m.b17 + 128*m.b7*m.b10*m.b15*m.b18 + 64*m.b7*m.b10*m.b16
                       *m.b19 + 256*m.b7*m.b11*m.b12*m.b16 + 192*m.b7*m.b11*m.b13*m.b17 + 128*m.b7*m.b11*m.b14*m.b18 + 
                       64*m.b7*m.b11*m.b15*m.b19 + 128*m.b7*m.b12*m.b13*m.b18 + 64*m.b7*m.b12*m.b14*m.b19 + 512*m.b8*
                       m.b9*m.b10*m.b11 + 512*m.b8*m.b9*m.b11*m.b12 + 512*m.b8*m.b9*m.b12*m.b13 + 448*m.b8*m.b9*m.b13*
                       m.b14 + 384*m.b8*m.b9*m.b14*m.b15 + 320*m.b8*m.b9*m.b15*m.b16 + 256*m.b8*m.b9*m.b16*m.b17 + 192*
                       m.b8*m.b9*m.b17*m.b18 + 128*m.b8*m.b9*m.b18*m.b19 + 64*m.b8*m.b9*m.b19*m.b20 + 512*m.b8*m.b10*
                       m.b11*m.b13 + 448*m.b8*m.b10*m.b12*m.b14 + 384*m.b8*m.b10*m.b13*m.b15 + 320*m.b8*m.b10*m.b14*
                       m.b16 + 256*m.b8*m.b10*m.b15*m.b17 + 192*m.b8*m.b10*m.b16*m.b18 + 128*m.b8*m.b10*m.b17*m.b19 + 64
                       *m.b8*m.b10*m.b18*m.b20 + 384*m.b8*m.b11*m.b12*m.b15 + 320*m.b8*m.b11*m.b13*m.b16 + 256*m.b8*
                       m.b11*m.b14*m.b17 + 192*m.b8*m.b11*m.b15*m.b18 + 128*m.b8*m.b11*m.b16*m.b19 + 64*m.b8*m.b11*m.b17
                       *m.b20 + 256*m.b8*m.b12*m.b13*m.b17 + 192*m.b8*m.b12*m.b14*m.b18 + 128*m.b8*m.b12*m.b15*m.b19 + 
                       64*m.b8*m.b12*m.b16*m.b20 + 128*m.b8*m.b13*m.b14*m.b19 + 64*m.b8*m.b13*m.b15*m.b20 + 576*m.b9*
                       m.b10*m.b11*m.b12 + 576*m.b9*m.b10*m.b12*m.b13 + 512*m.b9*m.b10*m.b13*m.b14 + 448*m.b9*m.b10*
                       m.b14*m.b15 + 384*m.b9*m.b10*m.b15*m.b16 + 320*m.b9*m.b10*m.b16*m.b17 + 256*m.b9*m.b10*m.b17*
                       m.b18 + 192*m.b9*m.b10*m.b18*m.b19 + 128*m.b9*m.b10*m.b19*m.b20 + 64*m.b9*m.b10*m.b20*m.b21 + 512
                       *m.b9*m.b11*m.b12*m.b14 + 448*m.b9*m.b11*m.b13*m.b15 + 384*m.b9*m.b11*m.b14*m.b16 + 320*m.b9*
                       m.b11*m.b15*m.b17 + 256*m.b9*m.b11*m.b16*m.b18 + 192*m.b9*m.b11*m.b17*m.b19 + 128*m.b9*m.b11*
                       m.b18*m.b20 + 64*m.b9*m.b11*m.b19*m.b21 + 384*m.b9*m.b12*m.b13*m.b16 + 320*m.b9*m.b12*m.b14*m.b17
                        + 256*m.b9*m.b12*m.b15*m.b18 + 192*m.b9*m.b12*m.b16*m.b19 + 128*m.b9*m.b12*m.b17*m.b20 + 64*m.b9
                       *m.b12*m.b18*m.b21 + 256*m.b9*m.b13*m.b14*m.b18 + 192*m.b9*m.b13*m.b15*m.b19 + 128*m.b9*m.b13*
                       m.b16*m.b20 + 64*m.b9*m.b13*m.b17*m.b21 + 128*m.b9*m.b14*m.b15*m.b20 + 64*m.b9*m.b14*m.b16*m.b21
                        + 640*m.b10*m.b11*m.b12*m.b13 + 576*m.b10*m.b11*m.b13*m.b14 + 512*m.b10*m.b11*m.b14*m.b15 + 448*
                       m.b10*m.b11*m.b15*m.b16 + 384*m.b10*m.b11*m.b16*m.b17 + 320*m.b10*m.b11*m.b17*m.b18 + 256*m.b10*
                       m.b11*m.b18*m.b19 + 192*m.b10*m.b11*m.b19*m.b20 + 128*m.b10*m.b11*m.b20*m.b21 + 64*m.b10*m.b11*
                       m.b21*m.b22 + 512*m.b10*m.b12*m.b13*m.b15 + 448*m.b10*m.b12*m.b14*m.b16 + 384*m.b10*m.b12*m.b15*
                       m.b17 + 320*m.b10*m.b12*m.b16*m.b18 + 256*m.b10*m.b12*m.b17*m.b19 + 192*m.b10*m.b12*m.b18*m.b20
                        + 128*m.b10*m.b12*m.b19*m.b21 + 64*m.b10*m.b12*m.b20*m.b22 + 384*m.b10*m.b13*m.b14*m.b17 + 320*
                       m.b10*m.b13*m.b15*m.b18 + 256*m.b10*m.b13*m.b16*m.b19 + 192*m.b10*m.b13*m.b17*m.b20 + 128*m.b10*
                       m.b13*m.b18*m.b21 + 64*m.b10*m.b13*m.b19*m.b22 + 256*m.b10*m.b14*m.b15*m.b19 + 192*m.b10*m.b14*
                       m.b16*m.b20 + 128*m.b10*m.b14*m.b17*m.b21 + 64*m.b10*m.b14*m.b18*m.b22 + 128*m.b10*m.b15*m.b16*
                       m.b21 + 64*m.b10*m.b15*m.b17*m.b22 + 640*m.b11*m.b12*m.b13*m.b14 + 576*m.b11*m.b12*m.b14*m.b15 + 
                       512*m.b11*m.b12*m.b15*m.b16 + 448*m.b11*m.b12*m.b16*m.b17 + 384*m.b11*m.b12*m.b17*m.b18 + 320*
                       m.b11*m.b12*m.b18*m.b19 + 256*m.b11*m.b12*m.b19*m.b20 + 192*m.b11*m.b12*m.b20*m.b21 + 128*m.b11*
                       m.b12*m.b21*m.b22 + 64*m.b11*m.b12*m.b22*m.b23 + 512*m.b11*m.b13*m.b14*m.b16 + 448*m.b11*m.b13*
                       m.b15*m.b17 + 384*m.b11*m.b13*m.b16*m.b18 + 320*m.b11*m.b13*m.b17*m.b19 + 256*m.b11*m.b13*m.b18*
                       m.b20 + 192*m.b11*m.b13*m.b19*m.b21 + 128*m.b11*m.b13*m.b20*m.b22 + 64*m.b11*m.b13*m.b21*m.b23 + 
                       384*m.b11*m.b14*m.b15*m.b18 + 320*m.b11*m.b14*m.b16*m.b19 + 256*m.b11*m.b14*m.b17*m.b20 + 192*
                       m.b11*m.b14*m.b18*m.b21 + 128*m.b11*m.b14*m.b19*m.b22 + 64*m.b11*m.b14*m.b20*m.b23 + 256*m.b11*
                       m.b15*m.b16*m.b20 + 192*m.b11*m.b15*m.b17*m.b21 + 128*m.b11*m.b15*m.b18*m.b22 + 64*m.b11*m.b15*
                       m.b19*m.b23 + 128*m.b11*m.b16*m.b17*m.b22 + 64*m.b11*m.b16*m.b18*m.b23 + 640*m.b12*m.b13*m.b14*
                       m.b15 + 576*m.b12*m.b13*m.b15*m.b16 + 512*m.b12*m.b13*m.b16*m.b17 + 448*m.b12*m.b13*m.b17*m.b18
                        + 384*m.b12*m.b13*m.b18*m.b19 + 320*m.b12*m.b13*m.b19*m.b20 + 256*m.b12*m.b13*m.b20*m.b21 + 192*
                       m.b12*m.b13*m.b21*m.b22 + 128*m.b12*m.b13*m.b22*m.b23 + 64*m.b12*m.b13*m.b23*m.b24 + 512*m.b12*
                       m.b14*m.b15*m.b17 + 448*m.b12*m.b14*m.b16*m.b18 + 384*m.b12*m.b14*m.b17*m.b19 + 320*m.b12*m.b14*
                       m.b18*m.b20 + 256*m.b12*m.b14*m.b19*m.b21 + 192*m.b12*m.b14*m.b20*m.b22 + 128*m.b12*m.b14*m.b21*
                       m.b23 + 64*m.b12*m.b14*m.b22*m.b24 + 384*m.b12*m.b15*m.b16*m.b19 + 320*m.b12*m.b15*m.b17*m.b20 + 
                       256*m.b12*m.b15*m.b18*m.b21 + 192*m.b12*m.b15*m.b19*m.b22 + 128*m.b12*m.b15*m.b20*m.b23 + 64*
                       m.b12*m.b15*m.b21*m.b24 + 256*m.b12*m.b16*m.b17*m.b21 + 192*m.b12*m.b16*m.b18*m.b22 + 128*m.b12*
                       m.b16*m.b19*m.b23 + 64*m.b12*m.b16*m.b20*m.b24 + 128*m.b12*m.b17*m.b18*m.b23 + 64*m.b12*m.b17*
                       m.b19*m.b24 + 640*m.b13*m.b14*m.b15*m.b16 + 576*m.b13*m.b14*m.b16*m.b17 + 512*m.b13*m.b14*m.b17*
                       m.b18 + 448*m.b13*m.b14*m.b18*m.b19 + 384*m.b13*m.b14*m.b19*m.b20 + 320*m.b13*m.b14*m.b20*m.b21
                        + 256*m.b13*m.b14*m.b21*m.b22 + 192*m.b13*m.b14*m.b22*m.b23 + 128*m.b13*m.b14*m.b23*m.b24 + 64*
                       m.b13*m.b14*m.b24*m.b25 + 512*m.b13*m.b15*m.b16*m.b18 + 448*m.b13*m.b15*m.b17*m.b19 + 384*m.b13*
                       m.b15*m.b18*m.b20 + 320*m.b13*m.b15*m.b19*m.b21 + 256*m.b13*m.b15*m.b20*m.b22 + 192*m.b13*m.b15*
                       m.b21*m.b23 + 128*m.b13*m.b15*m.b22*m.b24 + 64*m.b13*m.b15*m.b23*m.b25 + 384*m.b13*m.b16*m.b17*
                       m.b20 + 320*m.b13*m.b16*m.b18*m.b21 + 256*m.b13*m.b16*m.b19*m.b22 + 192*m.b13*m.b16*m.b20*m.b23
                        + 128*m.b13*m.b16*m.b21*m.b24 + 64*m.b13*m.b16*m.b22*m.b25 + 256*m.b13*m.b17*m.b18*m.b22 + 192*
                       m.b13*m.b17*m.b19*m.b23 + 128*m.b13*m.b17*m.b20*m.b24 + 64*m.b13*m.b17*m.b21*m.b25 + 128*m.b13*
                       m.b18*m.b19*m.b24 + 64*m.b13*m.b18*m.b20*m.b25 + 576*m.b14*m.b15*m.b16*m.b17 + 512*m.b14*m.b15*
                       m.b17*m.b18 + 448*m.b14*m.b15*m.b18*m.b19 + 384*m.b14*m.b15*m.b19*m.b20 + 320*m.b14*m.b15*m.b20*
                       m.b21 + 256*m.b14*m.b15*m.b21*m.b22 + 192*m.b14*m.b15*m.b22*m.b23 + 128*m.b14*m.b15*m.b23*m.b24
                        + 64*m.b14*m.b15*m.b24*m.b25 + 448*m.b14*m.b16*m.b17*m.b19 + 384*m.b14*m.b16*m.b18*m.b20 + 320*
                       m.b14*m.b16*m.b19*m.b21 + 256*m.b14*m.b16*m.b20*m.b22 + 192*m.b14*m.b16*m.b21*m.b23 + 128*m.b14*
                       m.b16*m.b22*m.b24 + 64*m.b14*m.b16*m.b23*m.b25 + 320*m.b14*m.b17*m.b18*m.b21 + 256*m.b14*m.b17*
                       m.b19*m.b22 + 192*m.b14*m.b17*m.b20*m.b23 + 128*m.b14*m.b17*m.b21*m.b24 + 64*m.b14*m.b17*m.b22*
                       m.b25 + 192*m.b14*m.b18*m.b19*m.b23 + 128*m.b14*m.b18*m.b20*m.b24 + 64*m.b14*m.b18*m.b21*m.b25 + 
                       64*m.b14*m.b19*m.b20*m.b25 + 512*m.b15*m.b16*m.b17*m.b18 + 448*m.b15*m.b16*m.b18*m.b19 + 384*
                       m.b15*m.b16*m.b19*m.b20 + 320*m.b15*m.b16*m.b20*m.b21 + 256*m.b15*m.b16*m.b21*m.b22 + 192*m.b15*
                       m.b16*m.b22*m.b23 + 128*m.b15*m.b16*m.b23*m.b24 + 64*m.b15*m.b16*m.b24*m.b25 + 384*m.b15*m.b17*
                       m.b18*m.b20 + 320*m.b15*m.b17*m.b19*m.b21 + 256*m.b15*m.b17*m.b20*m.b22 + 192*m.b15*m.b17*m.b21*
                       m.b23 + 128*m.b15*m.b17*m.b22*m.b24 + 64*m.b15*m.b17*m.b23*m.b25 + 256*m.b15*m.b18*m.b19*m.b22 + 
                       192*m.b15*m.b18*m.b20*m.b23 + 128*m.b15*m.b18*m.b21*m.b24 + 64*m.b15*m.b18*m.b22*m.b25 + 128*
                       m.b15*m.b19*m.b20*m.b24 + 64*m.b15*m.b19*m.b21*m.b25 + 448*m.b16*m.b17*m.b18*m.b19 + 384*m.b16*
                       m.b17*m.b19*m.b20 + 320*m.b16*m.b17*m.b20*m.b21 + 256*m.b16*m.b17*m.b21*m.b22 + 192*m.b16*m.b17*
                       m.b22*m.b23 + 128*m.b16*m.b17*m.b23*m.b24 + 64*m.b16*m.b17*m.b24*m.b25 + 320*m.b16*m.b18*m.b19*
                       m.b21 + 256*m.b16*m.b18*m.b20*m.b22 + 192*m.b16*m.b18*m.b21*m.b23 + 128*m.b16*m.b18*m.b22*m.b24
                        + 64*m.b16*m.b18*m.b23*m.b25 + 192*m.b16*m.b19*m.b20*m.b23 + 128*m.b16*m.b19*m.b21*m.b24 + 64*
                       m.b16*m.b19*m.b22*m.b25 + 64*m.b16*m.b20*m.b21*m.b25 + 384*m.b17*m.b18*m.b19*m.b20 + 320*m.b17*
                       m.b18*m.b20*m.b21 + 256*m.b17*m.b18*m.b21*m.b22 + 192*m.b17*m.b18*m.b22*m.b23 + 128*m.b17*m.b18*
                       m.b23*m.b24 + 64*m.b17*m.b18*m.b24*m.b25 + 256*m.b17*m.b19*m.b20*m.b22 + 192*m.b17*m.b19*m.b21*
                       m.b23 + 128*m.b17*m.b19*m.b22*m.b24 + 64*m.b17*m.b19*m.b23*m.b25 + 128*m.b17*m.b20*m.b21*m.b24 + 
                       64*m.b17*m.b20*m.b22*m.b25 + 320*m.b18*m.b19*m.b20*m.b21 + 256*m.b18*m.b19*m.b21*m.b22 + 192*
                       m.b18*m.b19*m.b22*m.b23 + 128*m.b18*m.b19*m.b23*m.b24 + 64*m.b18*m.b19*m.b24*m.b25 + 192*m.b18*
                       m.b20*m.b21*m.b23 + 128*m.b18*m.b20*m.b22*m.b24 + 64*m.b18*m.b20*m.b23*m.b25 + 64*m.b18*m.b21*
                       m.b22*m.b25 + 256*m.b19*m.b20*m.b21*m.b22 + 192*m.b19*m.b20*m.b22*m.b23 + 128*m.b19*m.b20*m.b23*
                       m.b24 + 64*m.b19*m.b20*m.b24*m.b25 + 128*m.b19*m.b21*m.b22*m.b24 + 64*m.b19*m.b21*m.b23*m.b25 + 
                       192*m.b20*m.b21*m.b22*m.b23 + 128*m.b20*m.b21*m.b23*m.b24 + 64*m.b20*m.b21*m.b24*m.b25 + 64*m.b20
                       *m.b22*m.b23*m.b25 + 128*m.b21*m.b22*m.b23*m.b24 + 64*m.b21*m.b22*m.b24*m.b25 + 64*m.b22*m.b23*
                       m.b24*m.b25 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*
                       m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11
                        - 64*m.b1*m.b2*m.b12 - 32*m.b1*m.b2*m.b13 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3
                       *m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*
                       m.b3*m.b11 - 32*m.b1*m.b3*m.b12 - 32*m.b1*m.b3*m.b13 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32
                       *m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 32*m.b1*m.b4*m.b11
                        - 32*m.b1*m.b4*m.b12 - 32*m.b1*m.b4*m.b13 - 64*m.b1*m.b5*m.b6 - 64*m.b1*m.b5*m.b7 - 64*m.b1*m.b5
                       *m.b8 - 32*m.b1*m.b5*m.b9 - 32*m.b1*m.b5*m.b10 - 32*m.b1*m.b5*m.b11 - 32*m.b1*m.b5*m.b12 - 32*
                       m.b1*m.b5*m.b13 - 64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 32*m.b1*m.b6*m.b9 - 32*m.b1*m.b6*m.b10
                        - 32*m.b1*m.b6*m.b12 - 32*m.b1*m.b6*m.b13 - 32*m.b1*m.b7*m.b8 - 32*m.b1*m.b7*m.b9 - 32*m.b1*m.b7
                       *m.b10 - 32*m.b1*m.b7*m.b11 - 32*m.b1*m.b7*m.b12 - 32*m.b1*m.b8*m.b9 - 32*m.b1*m.b8*m.b10 - 32*
                       m.b1*m.b8*m.b11 - 32*m.b1*m.b8*m.b12 - 32*m.b1*m.b8*m.b13 - 32*m.b1*m.b9*m.b10 - 32*m.b1*m.b9*
                       m.b11 - 32*m.b1*m.b9*m.b12 - 32*m.b1*m.b9*m.b13 - 32*m.b1*m.b10*m.b11 - 32*m.b1*m.b10*m.b12 - 32*
                       m.b1*m.b10*m.b13 - 32*m.b1*m.b11*m.b12 - 32*m.b1*m.b11*m.b13 - 32*m.b1*m.b12*m.b13 - 96*m.b2*m.b3
                       *m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*
                       m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*m.b11 - 128*m.b2*m.b3*m.b12 - 96*m.b2*m.b3*
                       m.b13 - 32*m.b2*m.b3*m.b14 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 128*
                       m.b2*m.b4*m.b8 - 128*m.b2*m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*m.b4*m.b11 - 96*m.b2*m.b4*
                       m.b12 - 64*m.b2*m.b4*m.b13 - 32*m.b2*m.b4*m.b14 - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5*m.b7 - 64*
                       m.b2*m.b5*m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*m.b10 - 96*m.b2*m.b5*m.b11 - 64*m.b2*m.b5*
                       m.b12 - 64*m.b2*m.b5*m.b13 - 32*m.b2*m.b5*m.b14 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*m.b8 - 128*
                       m.b2*m.b6*m.b9 - 32*m.b2*m.b6*m.b10 - 64*m.b2*m.b6*m.b11 - 64*m.b2*m.b6*m.b12 - 64*m.b2*m.b6*
                       m.b13 - 32*m.b2*m.b6*m.b14 - 160*m.b2*m.b7*m.b8 - 96*m.b2*m.b7*m.b9 - 64*m.b2*m.b7*m.b10 - 64*
                       m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b13 - 32*m.b2*m.b7*m.b14 - 96*m.b2*m.b8*m.b9 - 64*m.b2*m.b8*
                       m.b10 - 64*m.b2*m.b8*m.b11 - 64*m.b2*m.b8*m.b12 - 64*m.b2*m.b8*m.b13 - 96*m.b2*m.b9*m.b10 - 64*
                       m.b2*m.b9*m.b11 - 64*m.b2*m.b9*m.b12 - 64*m.b2*m.b9*m.b13 - 32*m.b2*m.b9*m.b14 - 96*m.b2*m.b10*
                       m.b11 - 64*m.b2*m.b10*m.b12 - 64*m.b2*m.b10*m.b13 - 32*m.b2*m.b10*m.b14 - 96*m.b2*m.b11*m.b12 - 
                       64*m.b2*m.b11*m.b13 - 32*m.b2*m.b11*m.b14 - 96*m.b2*m.b12*m.b13 - 32*m.b2*m.b12*m.b14 - 32*m.b2*
                       m.b13*m.b14 - 160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8
                        - 192*m.b3*m.b4*m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*m.b12 - 160*
                       m.b3*m.b4*m.b13 - 96*m.b3*m.b4*m.b14 - 32*m.b3*m.b4*m.b15 - 256*m.b3*m.b5*m.b6 - 128*m.b3*m.b5*
                       m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*m.b10 - 192*m.b3*m.b5*m.b11 - 160*
                       m.b3*m.b5*m.b12 - 128*m.b3*m.b5*m.b13 - 64*m.b3*m.b5*m.b14 - 32*m.b3*m.b5*m.b15 - 256*m.b3*m.b6*
                       m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*m.b9 - 192*m.b3*m.b6*m.b10 - 160*m.b3*m.b6*m.b11 - 128*
                       m.b3*m.b6*m.b12 - 96*m.b3*m.b6*m.b13 - 64*m.b3*m.b6*m.b14 - 32*m.b3*m.b6*m.b15 - 256*m.b3*m.b7*
                       m.b8 - 224*m.b3*m.b7*m.b9 - 160*m.b3*m.b7*m.b10 - 32*m.b3*m.b7*m.b11 - 96*m.b3*m.b7*m.b12 - 96*
                       m.b3*m.b7*m.b13 - 64*m.b3*m.b7*m.b14 - 32*m.b3*m.b7*m.b15 - 224*m.b3*m.b8*m.b9 - 160*m.b3*m.b8*
                       m.b10 - 96*m.b3*m.b8*m.b11 - 96*m.b3*m.b8*m.b12 - 64*m.b3*m.b8*m.b14 - 32*m.b3*m.b8*m.b15 - 160*
                       m.b3*m.b9*m.b10 - 128*m.b3*m.b9*m.b11 - 96*m.b3*m.b9*m.b12 - 96*m.b3*m.b9*m.b13 - 64*m.b3*m.b9*
                       m.b14 - 160*m.b3*m.b10*m.b11 - 128*m.b3*m.b10*m.b12 - 96*m.b3*m.b10*m.b13 - 64*m.b3*m.b10*m.b14
                        - 32*m.b3*m.b10*m.b15 - 160*m.b3*m.b11*m.b12 - 128*m.b3*m.b11*m.b13 - 64*m.b3*m.b11*m.b14 - 32*
                       m.b3*m.b11*m.b15 - 160*m.b3*m.b12*m.b13 - 64*m.b3*m.b12*m.b14 - 32*m.b3*m.b12*m.b15 - 96*m.b3*
                       m.b13*m.b14 - 32*m.b3*m.b13*m.b15 - 32*m.b3*m.b14*m.b15 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7
                        - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 256*m.b4*m.b5*m.b11 - 256*m.b4
                       *m.b5*m.b12 - 224*m.b4*m.b5*m.b13 - 160*m.b4*m.b5*m.b14 - 96*m.b4*m.b5*m.b15 - 32*m.b4*m.b5*m.b16
                        - 352*m.b4*m.b6*m.b7 - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10 - 256*m.b4*
                       m.b6*m.b11 - 224*m.b4*m.b6*m.b12 - 192*m.b4*m.b6*m.b13 - 128*m.b4*m.b6*m.b14 - 64*m.b4*m.b6*m.b15
                        - 32*m.b4*m.b6*m.b16 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*m.b4*m.b7*m.b10 - 224*m.b4*
                       m.b7*m.b11 - 192*m.b4*m.b7*m.b12 - 160*m.b4*m.b7*m.b13 - 96*m.b4*m.b7*m.b14 - 64*m.b4*m.b7*m.b15
                        - 32*m.b4*m.b7*m.b16 - 352*m.b4*m.b8*m.b9 - 288*m.b4*m.b8*m.b10 - 224*m.b4*m.b8*m.b11 - 32*m.b4*
                       m.b8*m.b12 - 128*m.b4*m.b8*m.b13 - 96*m.b4*m.b8*m.b14 - 64*m.b4*m.b8*m.b15 - 32*m.b4*m.b8*m.b16
                        - 288*m.b4*m.b9*m.b10 - 224*m.b4*m.b9*m.b11 - 160*m.b4*m.b9*m.b12 - 128*m.b4*m.b9*m.b13 - 64*
                       m.b4*m.b9*m.b15 - 32*m.b4*m.b9*m.b16 - 224*m.b4*m.b10*m.b11 - 192*m.b4*m.b10*m.b12 - 160*m.b4*
                       m.b10*m.b13 - 96*m.b4*m.b10*m.b14 - 64*m.b4*m.b10*m.b15 - 224*m.b4*m.b11*m.b12 - 192*m.b4*m.b11*
                       m.b13 - 96*m.b4*m.b11*m.b14 - 64*m.b4*m.b11*m.b15 - 32*m.b4*m.b11*m.b16 - 224*m.b4*m.b12*m.b13 - 
                       128*m.b4*m.b12*m.b14 - 64*m.b4*m.b12*m.b15 - 32*m.b4*m.b12*m.b16 - 160*m.b4*m.b13*m.b14 - 64*m.b4
                       *m.b13*m.b15 - 32*m.b4*m.b13*m.b16 - 96*m.b4*m.b14*m.b15 - 32*m.b4*m.b14*m.b16 - 32*m.b4*m.b15*
                       m.b16 - 288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*
                       m.b5*m.b6*m.b11 - 320*m.b5*m.b6*m.b12 - 288*m.b5*m.b6*m.b13 - 224*m.b5*m.b6*m.b14 - 160*m.b5*m.b6
                       *m.b15 - 96*m.b5*m.b6*m.b16 - 32*m.b5*m.b6*m.b17 - 448*m.b5*m.b7*m.b8 - 256*m.b5*m.b7*m.b9 - 384*
                       m.b5*m.b7*m.b10 - 352*m.b5*m.b7*m.b11 - 288*m.b5*m.b7*m.b12 - 256*m.b5*m.b7*m.b13 - 192*m.b5*m.b7
                       *m.b14 - 128*m.b5*m.b7*m.b15 - 64*m.b5*m.b7*m.b16 - 32*m.b5*m.b7*m.b17 - 448*m.b5*m.b8*m.b9 - 416
                       *m.b5*m.b8*m.b10 - 192*m.b5*m.b8*m.b11 - 288*m.b5*m.b8*m.b12 - 224*m.b5*m.b8*m.b13 - 160*m.b5*
                       m.b8*m.b14 - 96*m.b5*m.b8*m.b15 - 64*m.b5*m.b8*m.b16 - 32*m.b5*m.b8*m.b17 - 416*m.b5*m.b9*m.b10
                        - 352*m.b5*m.b9*m.b11 - 288*m.b5*m.b9*m.b12 - 64*m.b5*m.b9*m.b13 - 128*m.b5*m.b9*m.b14 - 96*m.b5
                       *m.b9*m.b15 - 64*m.b5*m.b9*m.b16 - 32*m.b5*m.b9*m.b17 - 352*m.b5*m.b10*m.b11 - 288*m.b5*m.b10*
                       m.b12 - 224*m.b5*m.b10*m.b13 - 128*m.b5*m.b10*m.b14 - 64*m.b5*m.b10*m.b16 - 32*m.b5*m.b10*m.b17
                        - 288*m.b5*m.b11*m.b12 - 256*m.b5*m.b11*m.b13 - 160*m.b5*m.b11*m.b14 - 96*m.b5*m.b11*m.b15 - 64*
                       m.b5*m.b11*m.b16 - 288*m.b5*m.b12*m.b13 - 192*m.b5*m.b12*m.b14 - 96*m.b5*m.b12*m.b15 - 64*m.b5*
                       m.b12*m.b16 - 32*m.b5*m.b12*m.b17 - 224*m.b5*m.b13*m.b14 - 128*m.b5*m.b13*m.b15 - 64*m.b5*m.b13*
                       m.b16 - 32*m.b5*m.b13*m.b17 - 160*m.b5*m.b14*m.b15 - 64*m.b5*m.b14*m.b16 - 32*m.b5*m.b14*m.b17 - 
                       96*m.b5*m.b15*m.b16 - 32*m.b5*m.b15*m.b17 - 32*m.b5*m.b16*m.b17 - 352*m.b6*m.b7*m.b8 - 512*m.b6*
                       m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*m.b7*m.b11 - 416*m.b6*m.b7*m.b12 - 352*m.b6*m.b7*m.b13
                        - 288*m.b6*m.b7*m.b14 - 224*m.b6*m.b7*m.b15 - 160*m.b6*m.b7*m.b16 - 96*m.b6*m.b7*m.b17 - 32*m.b6
                       *m.b7*m.b18 - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10 - 480*m.b6*m.b8*m.b11 - 416*m.b6*m.b8*
                       m.b12 - 352*m.b6*m.b8*m.b13 - 256*m.b6*m.b8*m.b14 - 192*m.b6*m.b8*m.b15 - 128*m.b6*m.b8*m.b16 - 
                       64*m.b6*m.b8*m.b17 - 32*m.b6*m.b8*m.b18 - 544*m.b6*m.b9*m.b10 - 480*m.b6*m.b9*m.b11 - 224*m.b6*
                       m.b9*m.b12 - 352*m.b6*m.b9*m.b13 - 224*m.b6*m.b9*m.b14 - 160*m.b6*m.b9*m.b15 - 96*m.b6*m.b9*m.b16
                        - 64*m.b6*m.b9*m.b17 - 32*m.b6*m.b9*m.b18 - 480*m.b6*m.b10*m.b11 - 416*m.b6*m.b10*m.b12 - 352*
                       m.b6*m.b10*m.b13 - 64*m.b6*m.b10*m.b14 - 128*m.b6*m.b10*m.b15 - 96*m.b6*m.b10*m.b16 - 64*m.b6*
                       m.b10*m.b17 - 32*m.b6*m.b10*m.b18 - 416*m.b6*m.b11*m.b12 - 352*m.b6*m.b11*m.b13 - 224*m.b6*m.b11*
                       m.b14 - 128*m.b6*m.b11*m.b15 - 64*m.b6*m.b11*m.b17 - 32*m.b6*m.b11*m.b18 - 352*m.b6*m.b12*m.b13
                        - 256*m.b6*m.b12*m.b14 - 160*m.b6*m.b12*m.b15 - 96*m.b6*m.b12*m.b16 - 64*m.b6*m.b12*m.b17 - 288*
                       m.b6*m.b13*m.b14 - 192*m.b6*m.b13*m.b15 - 96*m.b6*m.b13*m.b16 - 64*m.b6*m.b13*m.b17 - 32*m.b6*
                       m.b13*m.b18 - 224*m.b6*m.b14*m.b15 - 128*m.b6*m.b14*m.b16 - 64*m.b6*m.b14*m.b17 - 32*m.b6*m.b14*
                       m.b18 - 160*m.b6*m.b15*m.b16 - 64*m.b6*m.b15*m.b17 - 32*m.b6*m.b15*m.b18 - 96*m.b6*m.b16*m.b17 - 
                       32*m.b6*m.b16*m.b18 - 32*m.b6*m.b17*m.b18 - 416*m.b7*m.b8*m.b9 - 608*m.b7*m.b8*m.b10 - 576*m.b7*
                       m.b8*m.b11 - 544*m.b7*m.b8*m.b12 - 480*m.b7*m.b8*m.b13 - 352*m.b7*m.b8*m.b14 - 288*m.b7*m.b8*
                       m.b15 - 224*m.b7*m.b8*m.b16 - 160*m.b7*m.b8*m.b17 - 96*m.b7*m.b8*m.b18 - 32*m.b7*m.b8*m.b19 - 640
                       *m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 544*m.b7*m.b9*m.b12 - 480*m.b7*m.b9*m.b13 - 352*m.b7*
                       m.b9*m.b14 - 256*m.b7*m.b9*m.b15 - 192*m.b7*m.b9*m.b16 - 128*m.b7*m.b9*m.b17 - 64*m.b7*m.b9*m.b18
                        - 32*m.b7*m.b9*m.b19 - 608*m.b7*m.b10*m.b11 - 544*m.b7*m.b10*m.b12 - 256*m.b7*m.b10*m.b13 - 352*
                       m.b7*m.b10*m.b14 - 224*m.b7*m.b10*m.b15 - 160*m.b7*m.b10*m.b16 - 96*m.b7*m.b10*m.b17 - 64*m.b7*
                       m.b10*m.b18 - 32*m.b7*m.b10*m.b19 - 544*m.b7*m.b11*m.b12 - 480*m.b7*m.b11*m.b13 - 352*m.b7*m.b11*
                       m.b14 - 64*m.b7*m.b11*m.b15 - 128*m.b7*m.b11*m.b16 - 96*m.b7*m.b11*m.b17 - 64*m.b7*m.b11*m.b18 - 
                       32*m.b7*m.b11*m.b19 - 480*m.b7*m.b12*m.b13 - 352*m.b7*m.b12*m.b14 - 224*m.b7*m.b12*m.b15 - 128*
                       m.b7*m.b12*m.b16 - 64*m.b7*m.b12*m.b18 - 32*m.b7*m.b12*m.b19 - 352*m.b7*m.b13*m.b14 - 256*m.b7*
                       m.b13*m.b15 - 160*m.b7*m.b13*m.b16 - 96*m.b7*m.b13*m.b17 - 64*m.b7*m.b13*m.b18 - 288*m.b7*m.b14*
                       m.b15 - 192*m.b7*m.b14*m.b16 - 96*m.b7*m.b14*m.b17 - 64*m.b7*m.b14*m.b18 - 32*m.b7*m.b14*m.b19 - 
                       224*m.b7*m.b15*m.b16 - 128*m.b7*m.b15*m.b17 - 64*m.b7*m.b15*m.b18 - 32*m.b7*m.b15*m.b19 - 160*
                       m.b7*m.b16*m.b17 - 64*m.b7*m.b16*m.b18 - 32*m.b7*m.b16*m.b19 - 96*m.b7*m.b17*m.b18 - 32*m.b7*
                       m.b17*m.b19 - 32*m.b7*m.b18*m.b19 - 480*m.b8*m.b9*m.b10 - 704*m.b8*m.b9*m.b11 - 672*m.b8*m.b9*
                       m.b12 - 608*m.b8*m.b9*m.b13 - 480*m.b8*m.b9*m.b14 - 352*m.b8*m.b9*m.b15 - 288*m.b8*m.b9*m.b16 - 
                       224*m.b8*m.b9*m.b17 - 160*m.b8*m.b9*m.b18 - 96*m.b8*m.b9*m.b19 - 32*m.b8*m.b9*m.b20 - 736*m.b8*
                       m.b10*m.b11 - 416*m.b8*m.b10*m.b12 - 608*m.b8*m.b10*m.b13 - 480*m.b8*m.b10*m.b14 - 352*m.b8*m.b10
                       *m.b15 - 256*m.b8*m.b10*m.b16 - 192*m.b8*m.b10*m.b17 - 128*m.b8*m.b10*m.b18 - 64*m.b8*m.b10*m.b19
                        - 32*m.b8*m.b10*m.b20 - 672*m.b8*m.b11*m.b12 - 608*m.b8*m.b11*m.b13 - 256*m.b8*m.b11*m.b14 - 352
                       *m.b8*m.b11*m.b15 - 224*m.b8*m.b11*m.b16 - 160*m.b8*m.b11*m.b17 - 96*m.b8*m.b11*m.b18 - 64*m.b8*
                       m.b11*m.b19 - 32*m.b8*m.b11*m.b20 - 608*m.b8*m.b12*m.b13 - 480*m.b8*m.b12*m.b14 - 352*m.b8*m.b12*
                       m.b15 - 64*m.b8*m.b12*m.b16 - 128*m.b8*m.b12*m.b17 - 96*m.b8*m.b12*m.b18 - 64*m.b8*m.b12*m.b19 - 
                       32*m.b8*m.b12*m.b20 - 480*m.b8*m.b13*m.b14 - 352*m.b8*m.b13*m.b15 - 224*m.b8*m.b13*m.b16 - 128*
                       m.b8*m.b13*m.b17 - 64*m.b8*m.b13*m.b19 - 32*m.b8*m.b13*m.b20 - 352*m.b8*m.b14*m.b15 - 256*m.b8*
                       m.b14*m.b16 - 160*m.b8*m.b14*m.b17 - 96*m.b8*m.b14*m.b18 - 64*m.b8*m.b14*m.b19 - 288*m.b8*m.b15*
                       m.b16 - 192*m.b8*m.b15*m.b17 - 96*m.b8*m.b15*m.b18 - 64*m.b8*m.b15*m.b19 - 32*m.b8*m.b15*m.b20 - 
                       224*m.b8*m.b16*m.b17 - 128*m.b8*m.b16*m.b18 - 64*m.b8*m.b16*m.b19 - 32*m.b8*m.b16*m.b20 - 160*
                       m.b8*m.b17*m.b18 - 64*m.b8*m.b17*m.b19 - 32*m.b8*m.b17*m.b20 - 96*m.b8*m.b18*m.b19 - 32*m.b8*
                       m.b18*m.b20 - 32*m.b8*m.b19*m.b20 - 544*m.b9*m.b10*m.b11 - 800*m.b9*m.b10*m.b12 - 736*m.b9*m.b10*
                       m.b13 - 608*m.b9*m.b10*m.b14 - 480*m.b9*m.b10*m.b15 - 352*m.b9*m.b10*m.b16 - 288*m.b9*m.b10*m.b17
                        - 224*m.b9*m.b10*m.b18 - 160*m.b9*m.b10*m.b19 - 96*m.b9*m.b10*m.b20 - 32*m.b9*m.b10*m.b21 - 800*
                       m.b9*m.b11*m.b12 - 448*m.b9*m.b11*m.b13 - 608*m.b9*m.b11*m.b14 - 480*m.b9*m.b11*m.b15 - 352*m.b9*
                       m.b11*m.b16 - 256*m.b9*m.b11*m.b17 - 192*m.b9*m.b11*m.b18 - 128*m.b9*m.b11*m.b19 - 64*m.b9*m.b11*
                       m.b20 - 32*m.b9*m.b11*m.b21 - 736*m.b9*m.b12*m.b13 - 608*m.b9*m.b12*m.b14 - 256*m.b9*m.b12*m.b15
                        - 352*m.b9*m.b12*m.b16 - 224*m.b9*m.b12*m.b17 - 160*m.b9*m.b12*m.b18 - 96*m.b9*m.b12*m.b19 - 64*
                       m.b9*m.b12*m.b20 - 32*m.b9*m.b12*m.b21 - 608*m.b9*m.b13*m.b14 - 480*m.b9*m.b13*m.b15 - 352*m.b9*
                       m.b13*m.b16 - 64*m.b9*m.b13*m.b17 - 128*m.b9*m.b13*m.b18 - 96*m.b9*m.b13*m.b19 - 64*m.b9*m.b13*
                       m.b20 - 32*m.b9*m.b13*m.b21 - 480*m.b9*m.b14*m.b15 - 352*m.b9*m.b14*m.b16 - 224*m.b9*m.b14*m.b17
                        - 128*m.b9*m.b14*m.b18 - 64*m.b9*m.b14*m.b20 - 32*m.b9*m.b14*m.b21 - 352*m.b9*m.b15*m.b16 - 256*
                       m.b9*m.b15*m.b17 - 160*m.b9*m.b15*m.b18 - 96*m.b9*m.b15*m.b19 - 64*m.b9*m.b15*m.b20 - 288*m.b9*
                       m.b16*m.b17 - 192*m.b9*m.b16*m.b18 - 96*m.b9*m.b16*m.b19 - 64*m.b9*m.b16*m.b20 - 32*m.b9*m.b16*
                       m.b21 - 224*m.b9*m.b17*m.b18 - 128*m.b9*m.b17*m.b19 - 64*m.b9*m.b17*m.b20 - 32*m.b9*m.b17*m.b21
                        - 160*m.b9*m.b18*m.b19 - 64*m.b9*m.b18*m.b20 - 32*m.b9*m.b18*m.b21 - 96*m.b9*m.b19*m.b20 - 32*
                       m.b9*m.b19*m.b21 - 32*m.b9*m.b20*m.b21 - 608*m.b10*m.b11*m.b12 - 864*m.b10*m.b11*m.b13 - 736*
                       m.b10*m.b11*m.b14 - 608*m.b10*m.b11*m.b15 - 480*m.b10*m.b11*m.b16 - 352*m.b10*m.b11*m.b17 - 288*
                       m.b10*m.b11*m.b18 - 224*m.b10*m.b11*m.b19 - 160*m.b10*m.b11*m.b20 - 96*m.b10*m.b11*m.b21 - 32*
                       m.b10*m.b11*m.b22 - 864*m.b10*m.b12*m.b13 - 448*m.b10*m.b12*m.b14 - 608*m.b10*m.b12*m.b15 - 480*
                       m.b10*m.b12*m.b16 - 352*m.b10*m.b12*m.b17 - 256*m.b10*m.b12*m.b18 - 192*m.b10*m.b12*m.b19 - 128*
                       m.b10*m.b12*m.b20 - 64*m.b10*m.b12*m.b21 - 32*m.b10*m.b12*m.b22 - 736*m.b10*m.b13*m.b14 - 608*
                       m.b10*m.b13*m.b15 - 256*m.b10*m.b13*m.b16 - 352*m.b10*m.b13*m.b17 - 224*m.b10*m.b13*m.b18 - 160*
                       m.b10*m.b13*m.b19 - 96*m.b10*m.b13*m.b20 - 64*m.b10*m.b13*m.b21 - 32*m.b10*m.b13*m.b22 - 608*
                       m.b10*m.b14*m.b15 - 480*m.b10*m.b14*m.b16 - 352*m.b10*m.b14*m.b17 - 64*m.b10*m.b14*m.b18 - 128*
                       m.b10*m.b14*m.b19 - 96*m.b10*m.b14*m.b20 - 64*m.b10*m.b14*m.b21 - 32*m.b10*m.b14*m.b22 - 480*
                       m.b10*m.b15*m.b16 - 352*m.b10*m.b15*m.b17 - 224*m.b10*m.b15*m.b18 - 128*m.b10*m.b15*m.b19 - 64*
                       m.b10*m.b15*m.b21 - 32*m.b10*m.b15*m.b22 - 352*m.b10*m.b16*m.b17 - 256*m.b10*m.b16*m.b18 - 160*
                       m.b10*m.b16*m.b19 - 96*m.b10*m.b16*m.b20 - 64*m.b10*m.b16*m.b21 - 288*m.b10*m.b17*m.b18 - 192*
                       m.b10*m.b17*m.b19 - 96*m.b10*m.b17*m.b20 - 64*m.b10*m.b17*m.b21 - 32*m.b10*m.b17*m.b22 - 224*
                       m.b10*m.b18*m.b19 - 128*m.b10*m.b18*m.b20 - 64*m.b10*m.b18*m.b21 - 32*m.b10*m.b18*m.b22 - 160*
                       m.b10*m.b19*m.b20 - 64*m.b10*m.b19*m.b21 - 32*m.b10*m.b19*m.b22 - 96*m.b10*m.b20*m.b21 - 32*m.b10
                       *m.b20*m.b22 - 32*m.b10*m.b21*m.b22 - 640*m.b11*m.b12*m.b13 - 864*m.b11*m.b12*m.b14 - 736*m.b11*
                       m.b12*m.b15 - 608*m.b11*m.b12*m.b16 - 480*m.b11*m.b12*m.b17 - 352*m.b11*m.b12*m.b18 - 288*m.b11*
                       m.b12*m.b19 - 224*m.b11*m.b12*m.b20 - 160*m.b11*m.b12*m.b21 - 96*m.b11*m.b12*m.b22 - 32*m.b11*
                       m.b12*m.b23 - 864*m.b11*m.b13*m.b14 - 448*m.b11*m.b13*m.b15 - 608*m.b11*m.b13*m.b16 - 480*m.b11*
                       m.b13*m.b17 - 352*m.b11*m.b13*m.b18 - 256*m.b11*m.b13*m.b19 - 192*m.b11*m.b13*m.b20 - 128*m.b11*
                       m.b13*m.b21 - 64*m.b11*m.b13*m.b22 - 32*m.b11*m.b13*m.b23 - 736*m.b11*m.b14*m.b15 - 608*m.b11*
                       m.b14*m.b16 - 256*m.b11*m.b14*m.b17 - 352*m.b11*m.b14*m.b18 - 224*m.b11*m.b14*m.b19 - 160*m.b11*
                       m.b14*m.b20 - 96*m.b11*m.b14*m.b21 - 64*m.b11*m.b14*m.b22 - 32*m.b11*m.b14*m.b23 - 608*m.b11*
                       m.b15*m.b16 - 480*m.b11*m.b15*m.b17 - 352*m.b11*m.b15*m.b18 - 64*m.b11*m.b15*m.b19 - 128*m.b11*
                       m.b15*m.b20 - 96*m.b11*m.b15*m.b21 - 64*m.b11*m.b15*m.b22 - 32*m.b11*m.b15*m.b23 - 480*m.b11*
                       m.b16*m.b17 - 352*m.b11*m.b16*m.b18 - 224*m.b11*m.b16*m.b19 - 128*m.b11*m.b16*m.b20 - 64*m.b11*
                       m.b16*m.b22 - 32*m.b11*m.b16*m.b23 - 352*m.b11*m.b17*m.b18 - 256*m.b11*m.b17*m.b19 - 160*m.b11*
                       m.b17*m.b20 - 96*m.b11*m.b17*m.b21 - 64*m.b11*m.b17*m.b22 - 288*m.b11*m.b18*m.b19 - 192*m.b11*
                       m.b18*m.b20 - 96*m.b11*m.b18*m.b21 - 64*m.b11*m.b18*m.b22 - 32*m.b11*m.b18*m.b23 - 224*m.b11*
                       m.b19*m.b20 - 128*m.b11*m.b19*m.b21 - 64*m.b11*m.b19*m.b22 - 32*m.b11*m.b19*m.b23 - 160*m.b11*
                       m.b20*m.b21 - 64*m.b11*m.b20*m.b22 - 32*m.b11*m.b20*m.b23 - 96*m.b11*m.b21*m.b22 - 32*m.b11*m.b21
                       *m.b23 - 32*m.b11*m.b22*m.b23 - 640*m.b12*m.b13*m.b14 - 864*m.b12*m.b13*m.b15 - 736*m.b12*m.b13*
                       m.b16 - 608*m.b12*m.b13*m.b17 - 480*m.b12*m.b13*m.b18 - 352*m.b12*m.b13*m.b19 - 288*m.b12*m.b13*
                       m.b20 - 224*m.b12*m.b13*m.b21 - 160*m.b12*m.b13*m.b22 - 96*m.b12*m.b13*m.b23 - 32*m.b12*m.b13*
                       m.b24 - 864*m.b12*m.b14*m.b15 - 448*m.b12*m.b14*m.b16 - 608*m.b12*m.b14*m.b17 - 480*m.b12*m.b14*
                       m.b18 - 352*m.b12*m.b14*m.b19 - 256*m.b12*m.b14*m.b20 - 192*m.b12*m.b14*m.b21 - 128*m.b12*m.b14*
                       m.b22 - 64*m.b12*m.b14*m.b23 - 32*m.b12*m.b14*m.b24 - 736*m.b12*m.b15*m.b16 - 608*m.b12*m.b15*
                       m.b17 - 256*m.b12*m.b15*m.b18 - 352*m.b12*m.b15*m.b19 - 224*m.b12*m.b15*m.b20 - 160*m.b12*m.b15*
                       m.b21 - 96*m.b12*m.b15*m.b22 - 64*m.b12*m.b15*m.b23 - 32*m.b12*m.b15*m.b24 - 608*m.b12*m.b16*
                       m.b17 - 480*m.b12*m.b16*m.b18 - 352*m.b12*m.b16*m.b19 - 64*m.b12*m.b16*m.b20 - 128*m.b12*m.b16*
                       m.b21 - 96*m.b12*m.b16*m.b22 - 64*m.b12*m.b16*m.b23 - 32*m.b12*m.b16*m.b24 - 480*m.b12*m.b17*
                       m.b18 - 352*m.b12*m.b17*m.b19 - 224*m.b12*m.b17*m.b20 - 128*m.b12*m.b17*m.b21 - 64*m.b12*m.b17*
                       m.b23 - 32*m.b12*m.b17*m.b24 - 352*m.b12*m.b18*m.b19 - 256*m.b12*m.b18*m.b20 - 160*m.b12*m.b18*
                       m.b21 - 96*m.b12*m.b18*m.b22 - 64*m.b12*m.b18*m.b23 - 288*m.b12*m.b19*m.b20 - 192*m.b12*m.b19*
                       m.b21 - 96*m.b12*m.b19*m.b22 - 64*m.b12*m.b19*m.b23 - 32*m.b12*m.b19*m.b24 - 224*m.b12*m.b20*
                       m.b21 - 128*m.b12*m.b20*m.b22 - 64*m.b12*m.b20*m.b23 - 32*m.b12*m.b20*m.b24 - 160*m.b12*m.b21*
                       m.b22 - 64*m.b12*m.b21*m.b23 - 32*m.b12*m.b21*m.b24 - 96*m.b12*m.b22*m.b23 - 32*m.b12*m.b22*m.b24
                        - 32*m.b12*m.b23*m.b24 - 640*m.b13*m.b14*m.b15 - 864*m.b13*m.b14*m.b16 - 736*m.b13*m.b14*m.b17
                        - 608*m.b13*m.b14*m.b18 - 480*m.b13*m.b14*m.b19 - 352*m.b13*m.b14*m.b20 - 288*m.b13*m.b14*m.b21
                        - 224*m.b13*m.b14*m.b22 - 160*m.b13*m.b14*m.b23 - 96*m.b13*m.b14*m.b24 - 32*m.b13*m.b14*m.b25 - 
                       864*m.b13*m.b15*m.b16 - 448*m.b13*m.b15*m.b17 - 608*m.b13*m.b15*m.b18 - 480*m.b13*m.b15*m.b19 - 
                       352*m.b13*m.b15*m.b20 - 256*m.b13*m.b15*m.b21 - 192*m.b13*m.b15*m.b22 - 128*m.b13*m.b15*m.b23 - 
                       64*m.b13*m.b15*m.b24 - 32*m.b13*m.b15*m.b25 - 736*m.b13*m.b16*m.b17 - 608*m.b13*m.b16*m.b18 - 256
                       *m.b13*m.b16*m.b19 - 352*m.b13*m.b16*m.b20 - 224*m.b13*m.b16*m.b21 - 160*m.b13*m.b16*m.b22 - 96*
                       m.b13*m.b16*m.b23 - 64*m.b13*m.b16*m.b24 - 32*m.b13*m.b16*m.b25 - 608*m.b13*m.b17*m.b18 - 480*
                       m.b13*m.b17*m.b19 - 352*m.b13*m.b17*m.b20 - 64*m.b13*m.b17*m.b21 - 128*m.b13*m.b17*m.b22 - 96*
                       m.b13*m.b17*m.b23 - 64*m.b13*m.b17*m.b24 - 32*m.b13*m.b17*m.b25 - 480*m.b13*m.b18*m.b19 - 352*
                       m.b13*m.b18*m.b20 - 224*m.b13*m.b18*m.b21 - 128*m.b13*m.b18*m.b22 - 64*m.b13*m.b18*m.b24 - 32*
                       m.b13*m.b18*m.b25 - 352*m.b13*m.b19*m.b20 - 256*m.b13*m.b19*m.b21 - 160*m.b13*m.b19*m.b22 - 96*
                       m.b13*m.b19*m.b23 - 64*m.b13*m.b19*m.b24 - 288*m.b13*m.b20*m.b21 - 192*m.b13*m.b20*m.b22 - 96*
                       m.b13*m.b20*m.b23 - 64*m.b13*m.b20*m.b24 - 32*m.b13*m.b20*m.b25 - 224*m.b13*m.b21*m.b22 - 128*
                       m.b13*m.b21*m.b23 - 64*m.b13*m.b21*m.b24 - 32*m.b13*m.b21*m.b25 - 160*m.b13*m.b22*m.b23 - 64*
                       m.b13*m.b22*m.b24 - 32*m.b13*m.b22*m.b25 - 96*m.b13*m.b23*m.b24 - 32*m.b13*m.b23*m.b25 - 32*m.b13
                       *m.b24*m.b25 - 608*m.b14*m.b15*m.b16 - 800*m.b14*m.b15*m.b17 - 672*m.b14*m.b15*m.b18 - 544*m.b14*
                       m.b15*m.b19 - 416*m.b14*m.b15*m.b20 - 288*m.b14*m.b15*m.b21 - 224*m.b14*m.b15*m.b22 - 160*m.b14*
                       m.b15*m.b23 - 96*m.b14*m.b15*m.b24 - 32*m.b14*m.b15*m.b25 - 800*m.b14*m.b16*m.b17 - 416*m.b14*
                       m.b16*m.b18 - 544*m.b14*m.b16*m.b19 - 416*m.b14*m.b16*m.b20 - 288*m.b14*m.b16*m.b21 - 192*m.b14*
                       m.b16*m.b22 - 128*m.b14*m.b16*m.b23 - 64*m.b14*m.b16*m.b24 - 32*m.b14*m.b16*m.b25 - 672*m.b14*
                       m.b17*m.b18 - 544*m.b14*m.b17*m.b19 - 224*m.b14*m.b17*m.b20 - 288*m.b14*m.b17*m.b21 - 160*m.b14*
                       m.b17*m.b22 - 96*m.b14*m.b17*m.b23 - 64*m.b14*m.b17*m.b24 - 32*m.b14*m.b17*m.b25 - 544*m.b14*
                       m.b18*m.b19 - 416*m.b14*m.b18*m.b20 - 288*m.b14*m.b18*m.b21 - 32*m.b14*m.b18*m.b22 - 96*m.b14*
                       m.b18*m.b23 - 64*m.b14*m.b18*m.b24 - 32*m.b14*m.b18*m.b25 - 416*m.b14*m.b19*m.b20 - 288*m.b14*
                       m.b19*m.b21 - 192*m.b14*m.b19*m.b22 - 96*m.b14*m.b19*m.b23 - 32*m.b14*m.b19*m.b25 - 320*m.b14*
                       m.b20*m.b21 - 224*m.b14*m.b20*m.b22 - 128*m.b14*m.b20*m.b23 - 64*m.b14*m.b20*m.b24 - 32*m.b14*
                       m.b20*m.b25 - 256*m.b14*m.b21*m.b22 - 160*m.b14*m.b21*m.b23 - 64*m.b14*m.b21*m.b24 - 32*m.b14*
                       m.b21*m.b25 - 192*m.b14*m.b22*m.b23 - 96*m.b14*m.b22*m.b24 - 32*m.b14*m.b22*m.b25 - 128*m.b14*
                       m.b23*m.b24 - 32*m.b14*m.b23*m.b25 - 64*m.b14*m.b24*m.b25 - 544*m.b15*m.b16*m.b17 - 736*m.b15*
                       m.b16*m.b18 - 608*m.b15*m.b16*m.b19 - 480*m.b15*m.b16*m.b20 - 352*m.b15*m.b16*m.b21 - 224*m.b15*
                       m.b16*m.b22 - 160*m.b15*m.b16*m.b23 - 96*m.b15*m.b16*m.b24 - 32*m.b15*m.b16*m.b25 - 704*m.b15*
                       m.b17*m.b18 - 384*m.b15*m.b17*m.b19 - 480*m.b15*m.b17*m.b20 - 352*m.b15*m.b17*m.b21 - 224*m.b15*
                       m.b17*m.b22 - 128*m.b15*m.b17*m.b23 - 64*m.b15*m.b17*m.b24 - 32*m.b15*m.b17*m.b25 - 576*m.b15*
                       m.b18*m.b19 - 480*m.b15*m.b18*m.b20 - 192*m.b15*m.b18*m.b21 - 224*m.b15*m.b18*m.b22 - 96*m.b15*
                       m.b18*m.b23 - 64*m.b15*m.b18*m.b24 - 32*m.b15*m.b18*m.b25 - 448*m.b15*m.b19*m.b20 - 352*m.b15*
                       m.b19*m.b21 - 224*m.b15*m.b19*m.b22 - 32*m.b15*m.b19*m.b23 - 64*m.b15*m.b19*m.b24 - 32*m.b15*
                       m.b19*m.b25 - 320*m.b15*m.b20*m.b21 - 256*m.b15*m.b20*m.b22 - 160*m.b15*m.b20*m.b23 - 64*m.b15*
                       m.b20*m.b24 - 256*m.b15*m.b21*m.b22 - 192*m.b15*m.b21*m.b23 - 96*m.b15*m.b21*m.b24 - 32*m.b15*
                       m.b21*m.b25 - 192*m.b15*m.b22*m.b23 - 128*m.b15*m.b22*m.b24 - 32*m.b15*m.b22*m.b25 - 128*m.b15*
                       m.b23*m.b24 - 64*m.b15*m.b23*m.b25 - 64*m.b15*m.b24*m.b25 - 480*m.b16*m.b17*m.b18 - 640*m.b16*
                       m.b17*m.b19 - 544*m.b16*m.b17*m.b20 - 416*m.b16*m.b17*m.b21 - 288*m.b16*m.b17*m.b22 - 160*m.b16*
                       m.b17*m.b23 - 96*m.b16*m.b17*m.b24 - 32*m.b16*m.b17*m.b25 - 608*m.b16*m.b18*m.b19 - 320*m.b16*
                       m.b18*m.b20 - 416*m.b16*m.b18*m.b21 - 288*m.b16*m.b18*m.b22 - 160*m.b16*m.b18*m.b23 - 64*m.b16*
                       m.b18*m.b24 - 32*m.b16*m.b18*m.b25 - 480*m.b16*m.b19*m.b20 - 384*m.b16*m.b19*m.b21 - 160*m.b16*
                       m.b19*m.b22 - 160*m.b16*m.b19*m.b23 - 64*m.b16*m.b19*m.b24 - 32*m.b16*m.b19*m.b25 - 352*m.b16*
                       m.b20*m.b21 - 256*m.b16*m.b20*m.b22 - 192*m.b16*m.b20*m.b23 - 32*m.b16*m.b20*m.b24 - 32*m.b16*
                       m.b20*m.b25 - 256*m.b16*m.b21*m.b22 - 192*m.b16*m.b21*m.b23 - 128*m.b16*m.b21*m.b24 - 32*m.b16*
                       m.b21*m.b25 - 192*m.b16*m.b22*m.b23 - 128*m.b16*m.b22*m.b24 - 64*m.b16*m.b22*m.b25 - 128*m.b16*
                       m.b23*m.b24 - 64*m.b16*m.b23*m.b25 - 64*m.b16*m.b24*m.b25 - 416*m.b17*m.b18*m.b19 - 544*m.b17*
                       m.b18*m.b20 - 448*m.b17*m.b18*m.b21 - 352*m.b17*m.b18*m.b22 - 224*m.b17*m.b18*m.b23 - 96*m.b17*
                       m.b18*m.b24 - 32*m.b17*m.b18*m.b25 - 512*m.b17*m.b19*m.b20 - 256*m.b17*m.b19*m.b21 - 320*m.b17*
                       m.b19*m.b22 - 224*m.b17*m.b19*m.b23 - 96*m.b17*m.b19*m.b24 - 32*m.b17*m.b19*m.b25 - 384*m.b17*
                       m.b20*m.b21 - 288*m.b17*m.b20*m.b22 - 96*m.b17*m.b20*m.b23 - 128*m.b17*m.b20*m.b24 - 32*m.b17*
                       m.b20*m.b25 - 256*m.b17*m.b21*m.b22 - 192*m.b17*m.b21*m.b23 - 128*m.b17*m.b21*m.b24 - 32*m.b17*
                       m.b21*m.b25 - 192*m.b17*m.b22*m.b23 - 128*m.b17*m.b22*m.b24 - 64*m.b17*m.b22*m.b25 - 128*m.b17*
                       m.b23*m.b24 - 64*m.b17*m.b23*m.b25 - 64*m.b17*m.b24*m.b25 - 352*m.b18*m.b19*m.b20 - 448*m.b18*
                       m.b19*m.b21 - 352*m.b18*m.b19*m.b22 - 256*m.b18*m.b19*m.b23 - 160*m.b18*m.b19*m.b24 - 32*m.b18*
                       m.b19*m.b25 - 416*m.b18*m.b20*m.b21 - 192*m.b18*m.b20*m.b22 - 224*m.b18*m.b20*m.b23 - 128*m.b18*
                       m.b20*m.b24 - 64*m.b18*m.b20*m.b25 - 288*m.b18*m.b21*m.b22 - 192*m.b18*m.b21*m.b23 - 64*m.b18*
                       m.b21*m.b24 - 64*m.b18*m.b21*m.b25 - 192*m.b18*m.b22*m.b23 - 128*m.b18*m.b22*m.b24 - 64*m.b18*
                       m.b22*m.b25 - 128*m.b18*m.b23*m.b24 - 64*m.b18*m.b23*m.b25 - 64*m.b18*m.b24*m.b25 - 288*m.b19*
                       m.b20*m.b21 - 352*m.b19*m.b20*m.b22 - 256*m.b19*m.b20*m.b23 - 160*m.b19*m.b20*m.b24 - 64*m.b19*
                       m.b20*m.b25 - 320*m.b19*m.b21*m.b22 - 128*m.b19*m.b21*m.b23 - 128*m.b19*m.b21*m.b24 - 64*m.b19*
                       m.b21*m.b25 - 192*m.b19*m.b22*m.b23 - 128*m.b19*m.b22*m.b24 - 32*m.b19*m.b22*m.b25 - 128*m.b19*
                       m.b23*m.b24 - 64*m.b19*m.b23*m.b25 - 64*m.b19*m.b24*m.b25 - 224*m.b20*m.b21*m.b22 - 256*m.b20*
                       m.b21*m.b23 - 160*m.b20*m.b21*m.b24 - 64*m.b20*m.b21*m.b25 - 224*m.b20*m.b22*m.b23 - 64*m.b20*
                       m.b22*m.b24 - 64*m.b20*m.b22*m.b25 - 128*m.b20*m.b23*m.b24 - 64*m.b20*m.b23*m.b25 - 64*m.b20*
                       m.b24*m.b25 - 160*m.b21*m.b22*m.b23 - 160*m.b21*m.b22*m.b24 - 64*m.b21*m.b22*m.b25 - 128*m.b21*
                       m.b23*m.b24 - 32*m.b21*m.b23*m.b25 - 64*m.b21*m.b24*m.b25 - 96*m.b22*m.b23*m.b24 - 64*m.b22*m.b23
                       *m.b25 - 64*m.b22*m.b24*m.b25 - 32*m.b23*m.b24*m.b25 + 160*m.b1*m.b2 + 152*m.b1*m.b3 + 144*m.b1*
                       m.b4 + 136*m.b1*m.b5 + 128*m.b1*m.b6 + 120*m.b1*m.b7 + 128*m.b1*m.b8 + 120*m.b1*m.b9 + 112*m.b1*
                       m.b10 + 104*m.b1*m.b11 + 96*m.b1*m.b12 + 88*m.b1*m.b13 + 320*m.b2*m.b3 + 320*m.b2*m.b4 + 304*m.b2
                       *m.b5 + 288*m.b2*m.b6 + 272*m.b2*m.b7 + 272*m.b2*m.b8 + 272*m.b2*m.b9 + 256*m.b2*m.b10 + 240*m.b2
                       *m.b11 + 224*m.b2*m.b12 + 192*m.b2*m.b13 + 88*m.b2*m.b14 + 496*m.b3*m.b4 + 488*m.b3*m.b5 + 480*
                       m.b3*m.b6 + 456*m.b3*m.b7 + 432*m.b3*m.b8 + 440*m.b3*m.b9 + 432*m.b3*m.b10 + 408*m.b3*m.b11 + 368
                       *m.b3*m.b12 + 328*m.b3*m.b13 + 192*m.b3*m.b14 + 88*m.b3*m.b15 + 688*m.b4*m.b5 + 672*m.b4*m.b6 + 
                       656*m.b4*m.b7 + 640*m.b4*m.b8 + 624*m.b4*m.b9 + 624*m.b4*m.b10 + 592*m.b4*m.b11 + 544*m.b4*m.b12
                        + 480*m.b4*m.b13 + 328*m.b4*m.b14 + 192*m.b4*m.b15 + 88*m.b4*m.b16 + 896*m.b5*m.b6 + 872*m.b5*
                       m.b7 + 848*m.b5*m.b8 + 824*m.b5*m.b9 + 816*m.b5*m.b10 + 792*m.b5*m.b11 + 736*m.b5*m.b12 + 664*
                       m.b5*m.b13 + 480*m.b5*m.b14 + 328*m.b5*m.b15 + 192*m.b5*m.b16 + 88*m.b5*m.b17 + 1120*m.b6*m.b7 + 
                       1088*m.b6*m.b8 + 1040*m.b6*m.b9 + 1008*m.b6*m.b10 + 976*m.b6*m.b11 + 944*m.b6*m.b12 + 864*m.b6*
                       m.b13 + 664*m.b6*m.b14 + 480*m.b6*m.b15 + 328*m.b6*m.b16 + 192*m.b6*m.b17 + 88*m.b6*m.b18 + 1344*
                       m.b7*m.b8 + 1288*m.b7*m.b9 + 1216*m.b7*m.b10 + 1176*m.b7*m.b11 + 1120*m.b7*m.b12 + 1064*m.b7*
                       m.b13 + 864*m.b7*m.b14 + 664*m.b7*m.b15 + 480*m.b7*m.b16 + 328*m.b7*m.b17 + 192*m.b7*m.b18 + 88*
                       m.b7*m.b19 + 1552*m.b8*m.b9 + 1472*m.b8*m.b10 + 1392*m.b8*m.b11 + 1328*m.b8*m.b12 + 1248*m.b8*
                       m.b13 + 1064*m.b8*m.b14 + 864*m.b8*m.b15 + 664*m.b8*m.b16 + 480*m.b8*m.b17 + 328*m.b8*m.b18 + 192
                       *m.b8*m.b19 + 88*m.b8*m.b20 + 1744*m.b9*m.b10 + 1640*m.b9*m.b11 + 1552*m.b9*m.b12 + 1464*m.b9*
                       m.b13 + 1248*m.b9*m.b14 + 1064*m.b9*m.b15 + 864*m.b9*m.b16 + 664*m.b9*m.b17 + 480*m.b9*m.b18 + 
                       328*m.b9*m.b19 + 192*m.b9*m.b20 + 88*m.b9*m.b21 + 1920*m.b10*m.b11 + 1808*m.b10*m.b12 + 1696*
                       m.b10*m.b13 + 1464*m.b10*m.b14 + 1248*m.b10*m.b15 + 1064*m.b10*m.b16 + 864*m.b10*m.b17 + 664*
                       m.b10*m.b18 + 480*m.b10*m.b19 + 328*m.b10*m.b20 + 192*m.b10*m.b21 + 88*m.b10*m.b22 + 2080*m.b11*
                       m.b12 + 1960*m.b11*m.b13 + 1696*m.b11*m.b14 + 1464*m.b11*m.b15 + 1248*m.b11*m.b16 + 1064*m.b11*
                       m.b17 + 864*m.b11*m.b18 + 664*m.b11*m.b19 + 480*m.b11*m.b20 + 328*m.b11*m.b21 + 192*m.b11*m.b22
                        + 88*m.b11*m.b23 + 2240*m.b12*m.b13 + 1960*m.b12*m.b14 + 1696*m.b12*m.b15 + 1464*m.b12*m.b16 + 
                       1248*m.b12*m.b17 + 1064*m.b12*m.b18 + 864*m.b12*m.b19 + 664*m.b12*m.b20 + 480*m.b12*m.b21 + 328*
                       m.b12*m.b22 + 192*m.b12*m.b23 + 88*m.b12*m.b24 + 2240*m.b13*m.b14 + 1960*m.b13*m.b15 + 1696*m.b13
                       *m.b16 + 1464*m.b13*m.b17 + 1248*m.b13*m.b18 + 1064*m.b13*m.b19 + 864*m.b13*m.b20 + 664*m.b13*
                       m.b21 + 480*m.b13*m.b22 + 328*m.b13*m.b23 + 192*m.b13*m.b24 + 88*m.b13*m.b25 + 2080*m.b14*m.b15
                        + 1808*m.b14*m.b16 + 1552*m.b14*m.b17 + 1328*m.b14*m.b18 + 1120*m.b14*m.b19 + 944*m.b14*m.b20 + 
                       736*m.b14*m.b21 + 544*m.b14*m.b22 + 368*m.b14*m.b23 + 224*m.b14*m.b24 + 96*m.b14*m.b25 + 1920*
                       m.b15*m.b16 + 1640*m.b15*m.b17 + 1392*m.b15*m.b18 + 1176*m.b15*m.b19 + 976*m.b15*m.b20 + 792*
                       m.b15*m.b21 + 592*m.b15*m.b22 + 408*m.b15*m.b23 + 240*m.b15*m.b24 + 104*m.b15*m.b25 + 1744*m.b16*
                       m.b17 + 1472*m.b16*m.b18 + 1216*m.b16*m.b19 + 1008*m.b16*m.b20 + 816*m.b16*m.b21 + 624*m.b16*
                       m.b22 + 432*m.b16*m.b23 + 256*m.b16*m.b24 + 112*m.b16*m.b25 + 1552*m.b17*m.b18 + 1288*m.b17*m.b19
                        + 1040*m.b17*m.b20 + 824*m.b17*m.b21 + 624*m.b17*m.b22 + 440*m.b17*m.b23 + 272*m.b17*m.b24 + 120
                       *m.b17*m.b25 + 1344*m.b18*m.b19 + 1088*m.b18*m.b20 + 848*m.b18*m.b21 + 640*m.b18*m.b22 + 432*
                       m.b18*m.b23 + 272*m.b18*m.b24 + 128*m.b18*m.b25 + 1120*m.b19*m.b20 + 872*m.b19*m.b21 + 656*m.b19*
                       m.b22 + 456*m.b19*m.b23 + 272*m.b19*m.b24 + 120*m.b19*m.b25 + 896*m.b20*m.b21 + 672*m.b20*m.b22
                        + 480*m.b20*m.b23 + 288*m.b20*m.b24 + 128*m.b20*m.b25 + 688*m.b21*m.b22 + 488*m.b21*m.b23 + 304*
                       m.b21*m.b24 + 136*m.b21*m.b25 + 496*m.b22*m.b23 + 320*m.b22*m.b24 + 144*m.b22*m.b25 + 320*m.b23*
                       m.b24 + 152*m.b23*m.b25 + 160*m.b24*m.b25 - 264*m.b1 - 564*m.b2 - 892*m.b3 - 1240*m.b4 - 1600*
                       m.b5 - 1964*m.b6 - 2324*m.b7 - 2688*m.b8 - 3048*m.b9 - 3396*m.b10 - 3724*m.b11 - 4024*m.b12 - 
                       4288*m.b13 - 4024*m.b14 - 3724*m.b15 - 3396*m.b16 - 3048*m.b17 - 2688*m.b18 - 2324*m.b19 - 1964*
                       m.b20 - 1600*m.b21 - 1240*m.b22 - 892*m.b23 - 564*m.b24 - 264*m.b25 - m.x26 <= 0)

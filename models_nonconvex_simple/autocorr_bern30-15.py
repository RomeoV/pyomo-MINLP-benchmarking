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
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b2*m.b14*m.b15 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64
                       *m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3*m.b10*
                       m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*m.b3*m.b13*m.b15 + 64*m.b1*
                       m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*
                       m.b1*m.b4*m.b9*m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*m.b1*m.b4*m.b11*m.b14 + 64*m.b1*m.b4*m.b12*
                       m.b15 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11 + 64*m.b1*m.b5*m.b8*m.b12 + 64*m.b1*
                       m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*m.b14 + 64*m.b1*m.b5*m.b11*m.b15 + 64*m.b1*m.b6*m.b7*m.b12
                        + 64*m.b1*m.b6*m.b8*m.b13 + 64*m.b1*m.b6*m.b9*m.b14 + 64*m.b1*m.b6*m.b10*m.b15 + 64*m.b1*m.b7*
                       m.b8*m.b14 + 64*m.b1*m.b7*m.b9*m.b15 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*
                       m.b2*m.b3*m.b6*m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*
                       m.b10 + 128*m.b2*m.b3*m.b10*m.b11 + 128*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*m.b12*m.b13 + 128*
                       m.b2*m.b3*m.b13*m.b14 + 128*m.b2*m.b3*m.b14*m.b15 + 64*m.b2*m.b3*m.b15*m.b16 + 128*m.b2*m.b4*m.b5
                       *m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*
                       m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*m.b12*
                       m.b14 + 128*m.b2*m.b4*m.b13*m.b15 + 64*m.b2*m.b4*m.b14*m.b16 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2
                       *m.b5*m.b7*m.b10 + 128*m.b2*m.b5*m.b8*m.b11 + 128*m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*
                       m.b13 + 128*m.b2*m.b5*m.b11*m.b14 + 128*m.b2*m.b5*m.b12*m.b15 + 64*m.b2*m.b5*m.b13*m.b16 + 128*
                       m.b2*m.b6*m.b7*m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*m.b13 + 128*m.b2*m.b6*m.b10*
                       m.b14 + 128*m.b2*m.b6*m.b11*m.b15 + 64*m.b2*m.b6*m.b12*m.b16 + 128*m.b2*m.b7*m.b8*m.b13 + 128*
                       m.b2*m.b7*m.b9*m.b14 + 128*m.b2*m.b7*m.b10*m.b15 + 64*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b8*m.b9*
                       m.b15 + 64*m.b2*m.b8*m.b10*m.b16 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*m.b7 + 192*m.b3*
                       m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*m.b10 + 192*m.b3*m.b4*m.b10*m.b11
                        + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b4*m.b12*m.b13 + 192*m.b3*m.b4*m.b13*m.b14 + 192*m.b3*
                       m.b4*m.b14*m.b15 + 128*m.b3*m.b4*m.b15*m.b16 + 64*m.b3*m.b4*m.b16*m.b17 + 192*m.b3*m.b5*m.b6*m.b8
                        + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*m.b5*m.b8*m.b10 + 192*m.b3*m.b5*m.b9*m.b11 + 192*m.b3*m.b5*
                       m.b10*m.b12 + 192*m.b3*m.b5*m.b11*m.b13 + 192*m.b3*m.b5*m.b12*m.b14 + 192*m.b3*m.b5*m.b13*m.b15
                        + 128*m.b3*m.b5*m.b14*m.b16 + 64*m.b3*m.b5*m.b15*m.b17 + 192*m.b3*m.b6*m.b7*m.b10 + 192*m.b3*
                       m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*m.b10*m.b13 + 192*m.b3*m.b6*m.b11*
                       m.b14 + 192*m.b3*m.b6*m.b12*m.b15 + 128*m.b3*m.b6*m.b13*m.b16 + 64*m.b3*m.b6*m.b14*m.b17 + 192*
                       m.b3*m.b7*m.b8*m.b12 + 192*m.b3*m.b7*m.b9*m.b13 + 192*m.b3*m.b7*m.b10*m.b14 + 192*m.b3*m.b7*m.b11
                       *m.b15 + 128*m.b3*m.b7*m.b12*m.b16 + 64*m.b3*m.b7*m.b13*m.b17 + 192*m.b3*m.b8*m.b9*m.b14 + 192*
                       m.b3*m.b8*m.b10*m.b15 + 128*m.b3*m.b8*m.b11*m.b16 + 64*m.b3*m.b8*m.b12*m.b17 + 128*m.b3*m.b9*
                       m.b10*m.b16 + 64*m.b3*m.b9*m.b11*m.b17 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*
                       m.b4*m.b5*m.b8*m.b9 + 256*m.b4*m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5*m.b11*
                       m.b12 + 256*m.b4*m.b5*m.b12*m.b13 + 256*m.b4*m.b5*m.b13*m.b14 + 256*m.b4*m.b5*m.b14*m.b15 + 192*
                       m.b4*m.b5*m.b15*m.b16 + 128*m.b4*m.b5*m.b16*m.b17 + 64*m.b4*m.b5*m.b17*m.b18 + 256*m.b4*m.b6*m.b7
                       *m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11 + 256*m.b4*m.b6*m.b10*m.b12 + 256*
                       m.b4*m.b6*m.b11*m.b13 + 256*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*m.b6*m.b13*m.b15 + 192*m.b4*m.b6*
                       m.b14*m.b16 + 128*m.b4*m.b6*m.b15*m.b17 + 64*m.b4*m.b6*m.b16*m.b18 + 256*m.b4*m.b7*m.b8*m.b11 + 
                       256*m.b4*m.b7*m.b9*m.b12 + 256*m.b4*m.b7*m.b10*m.b13 + 256*m.b4*m.b7*m.b11*m.b14 + 256*m.b4*m.b7*
                       m.b12*m.b15 + 192*m.b4*m.b7*m.b13*m.b16 + 128*m.b4*m.b7*m.b14*m.b17 + 64*m.b4*m.b7*m.b15*m.b18 + 
                       256*m.b4*m.b8*m.b9*m.b13 + 256*m.b4*m.b8*m.b10*m.b14 + 256*m.b4*m.b8*m.b11*m.b15 + 192*m.b4*m.b8*
                       m.b12*m.b16 + 128*m.b4*m.b8*m.b13*m.b17 + 64*m.b4*m.b8*m.b14*m.b18 + 256*m.b4*m.b9*m.b10*m.b15 + 
                       192*m.b4*m.b9*m.b11*m.b16 + 128*m.b4*m.b9*m.b12*m.b17 + 64*m.b4*m.b9*m.b13*m.b18 + 128*m.b4*m.b10
                       *m.b11*m.b17 + 64*m.b4*m.b10*m.b12*m.b18 + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 
                       320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*m.b10*m.b11 + 320*m.b5*m.b6*m.b11*m.b12 + 320*m.b5*m.b6*
                       m.b12*m.b13 + 320*m.b5*m.b6*m.b13*m.b14 + 320*m.b5*m.b6*m.b14*m.b15 + 256*m.b5*m.b6*m.b15*m.b16
                        + 192*m.b5*m.b6*m.b16*m.b17 + 128*m.b5*m.b6*m.b17*m.b18 + 64*m.b5*m.b6*m.b18*m.b19 + 320*m.b5*
                       m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*m.b11 + 320*m.b5*m.b7*m.b10*m.b12 + 320*m.b5*m.b7*m.b11*
                       m.b13 + 320*m.b5*m.b7*m.b12*m.b14 + 320*m.b5*m.b7*m.b13*m.b15 + 256*m.b5*m.b7*m.b14*m.b16 + 192*
                       m.b5*m.b7*m.b15*m.b17 + 128*m.b5*m.b7*m.b16*m.b18 + 64*m.b5*m.b7*m.b17*m.b19 + 320*m.b5*m.b8*m.b9
                       *m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 320*m.b5*m.b8*m.b11*m.b14 + 320*m.b5*m.b8*m.b12*m.b15 + 256*
                       m.b5*m.b8*m.b13*m.b16 + 192*m.b5*m.b8*m.b14*m.b17 + 128*m.b5*m.b8*m.b15*m.b18 + 64*m.b5*m.b8*
                       m.b16*m.b19 + 320*m.b5*m.b9*m.b10*m.b14 + 320*m.b5*m.b9*m.b11*m.b15 + 256*m.b5*m.b9*m.b12*m.b16
                        + 192*m.b5*m.b9*m.b13*m.b17 + 128*m.b5*m.b9*m.b14*m.b18 + 64*m.b5*m.b9*m.b15*m.b19 + 256*m.b5*
                       m.b10*m.b11*m.b16 + 192*m.b5*m.b10*m.b12*m.b17 + 128*m.b5*m.b10*m.b13*m.b18 + 64*m.b5*m.b10*m.b14
                       *m.b19 + 128*m.b5*m.b11*m.b12*m.b18 + 64*m.b5*m.b11*m.b13*m.b19 + 384*m.b6*m.b7*m.b8*m.b9 + 384*
                       m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12 + 384*m.b6*m.b7*
                       m.b12*m.b13 + 384*m.b6*m.b7*m.b13*m.b14 + 384*m.b6*m.b7*m.b14*m.b15 + 320*m.b6*m.b7*m.b15*m.b16
                        + 256*m.b6*m.b7*m.b16*m.b17 + 192*m.b6*m.b7*m.b17*m.b18 + 128*m.b6*m.b7*m.b18*m.b19 + 64*m.b6*
                       m.b7*m.b19*m.b20 + 384*m.b6*m.b8*m.b9*m.b11 + 384*m.b6*m.b8*m.b10*m.b12 + 384*m.b6*m.b8*m.b11*
                       m.b13 + 384*m.b6*m.b8*m.b12*m.b14 + 384*m.b6*m.b8*m.b13*m.b15 + 320*m.b6*m.b8*m.b14*m.b16 + 256*
                       m.b6*m.b8*m.b15*m.b17 + 192*m.b6*m.b8*m.b16*m.b18 + 128*m.b6*m.b8*m.b17*m.b19 + 64*m.b6*m.b8*
                       m.b18*m.b20 + 384*m.b6*m.b9*m.b10*m.b13 + 384*m.b6*m.b9*m.b11*m.b14 + 384*m.b6*m.b9*m.b12*m.b15
                        + 320*m.b6*m.b9*m.b13*m.b16 + 256*m.b6*m.b9*m.b14*m.b17 + 192*m.b6*m.b9*m.b15*m.b18 + 128*m.b6*
                       m.b9*m.b16*m.b19 + 64*m.b6*m.b9*m.b17*m.b20 + 384*m.b6*m.b10*m.b11*m.b15 + 320*m.b6*m.b10*m.b12*
                       m.b16 + 256*m.b6*m.b10*m.b13*m.b17 + 192*m.b6*m.b10*m.b14*m.b18 + 128*m.b6*m.b10*m.b15*m.b19 + 64
                       *m.b6*m.b10*m.b16*m.b20 + 256*m.b6*m.b11*m.b12*m.b17 + 192*m.b6*m.b11*m.b13*m.b18 + 128*m.b6*
                       m.b11*m.b14*m.b19 + 64*m.b6*m.b11*m.b15*m.b20 + 128*m.b6*m.b12*m.b13*m.b19 + 64*m.b6*m.b12*m.b14*
                       m.b20 + 448*m.b7*m.b8*m.b9*m.b10 + 448*m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*m.b11*m.b12 + 448*
                       m.b7*m.b8*m.b12*m.b13 + 448*m.b7*m.b8*m.b13*m.b14 + 448*m.b7*m.b8*m.b14*m.b15 + 384*m.b7*m.b8*
                       m.b15*m.b16 + 320*m.b7*m.b8*m.b16*m.b17 + 256*m.b7*m.b8*m.b17*m.b18 + 192*m.b7*m.b8*m.b18*m.b19
                        + 128*m.b7*m.b8*m.b19*m.b20 + 64*m.b7*m.b8*m.b20*m.b21 + 448*m.b7*m.b9*m.b10*m.b12 + 448*m.b7*
                       m.b9*m.b11*m.b13 + 448*m.b7*m.b9*m.b12*m.b14 + 448*m.b7*m.b9*m.b13*m.b15 + 384*m.b7*m.b9*m.b14*
                       m.b16 + 320*m.b7*m.b9*m.b15*m.b17 + 256*m.b7*m.b9*m.b16*m.b18 + 192*m.b7*m.b9*m.b17*m.b19 + 128*
                       m.b7*m.b9*m.b18*m.b20 + 64*m.b7*m.b9*m.b19*m.b21 + 448*m.b7*m.b10*m.b11*m.b14 + 448*m.b7*m.b10*
                       m.b12*m.b15 + 384*m.b7*m.b10*m.b13*m.b16 + 320*m.b7*m.b10*m.b14*m.b17 + 256*m.b7*m.b10*m.b15*
                       m.b18 + 192*m.b7*m.b10*m.b16*m.b19 + 128*m.b7*m.b10*m.b17*m.b20 + 64*m.b7*m.b10*m.b18*m.b21 + 384
                       *m.b7*m.b11*m.b12*m.b16 + 320*m.b7*m.b11*m.b13*m.b17 + 256*m.b7*m.b11*m.b14*m.b18 + 192*m.b7*
                       m.b11*m.b15*m.b19 + 128*m.b7*m.b11*m.b16*m.b20 + 64*m.b7*m.b11*m.b17*m.b21 + 256*m.b7*m.b12*m.b13
                       *m.b18 + 192*m.b7*m.b12*m.b14*m.b19 + 128*m.b7*m.b12*m.b15*m.b20 + 64*m.b7*m.b12*m.b16*m.b21 + 
                       128*m.b7*m.b13*m.b14*m.b20 + 64*m.b7*m.b13*m.b15*m.b21 + 512*m.b8*m.b9*m.b10*m.b11 + 512*m.b8*
                       m.b9*m.b11*m.b12 + 512*m.b8*m.b9*m.b12*m.b13 + 512*m.b8*m.b9*m.b13*m.b14 + 512*m.b8*m.b9*m.b14*
                       m.b15 + 448*m.b8*m.b9*m.b15*m.b16 + 384*m.b8*m.b9*m.b16*m.b17 + 320*m.b8*m.b9*m.b17*m.b18 + 256*
                       m.b8*m.b9*m.b18*m.b19 + 192*m.b8*m.b9*m.b19*m.b20 + 128*m.b8*m.b9*m.b20*m.b21 + 64*m.b8*m.b9*
                       m.b21*m.b22 + 512*m.b8*m.b10*m.b11*m.b13 + 512*m.b8*m.b10*m.b12*m.b14 + 512*m.b8*m.b10*m.b13*
                       m.b15 + 448*m.b8*m.b10*m.b14*m.b16 + 384*m.b8*m.b10*m.b15*m.b17 + 320*m.b8*m.b10*m.b16*m.b18 + 
                       256*m.b8*m.b10*m.b17*m.b19 + 192*m.b8*m.b10*m.b18*m.b20 + 128*m.b8*m.b10*m.b19*m.b21 + 64*m.b8*
                       m.b10*m.b20*m.b22 + 512*m.b8*m.b11*m.b12*m.b15 + 448*m.b8*m.b11*m.b13*m.b16 + 384*m.b8*m.b11*
                       m.b14*m.b17 + 320*m.b8*m.b11*m.b15*m.b18 + 256*m.b8*m.b11*m.b16*m.b19 + 192*m.b8*m.b11*m.b17*
                       m.b20 + 128*m.b8*m.b11*m.b18*m.b21 + 64*m.b8*m.b11*m.b19*m.b22 + 384*m.b8*m.b12*m.b13*m.b17 + 320
                       *m.b8*m.b12*m.b14*m.b18 + 256*m.b8*m.b12*m.b15*m.b19 + 192*m.b8*m.b12*m.b16*m.b20 + 128*m.b8*
                       m.b12*m.b17*m.b21 + 64*m.b8*m.b12*m.b18*m.b22 + 256*m.b8*m.b13*m.b14*m.b19 + 192*m.b8*m.b13*m.b15
                       *m.b20 + 128*m.b8*m.b13*m.b16*m.b21 + 64*m.b8*m.b13*m.b17*m.b22 + 128*m.b8*m.b14*m.b15*m.b21 + 64
                       *m.b8*m.b14*m.b16*m.b22 + 576*m.b9*m.b10*m.b11*m.b12 + 576*m.b9*m.b10*m.b12*m.b13 + 576*m.b9*
                       m.b10*m.b13*m.b14 + 576*m.b9*m.b10*m.b14*m.b15 + 512*m.b9*m.b10*m.b15*m.b16 + 448*m.b9*m.b10*
                       m.b16*m.b17 + 384*m.b9*m.b10*m.b17*m.b18 + 320*m.b9*m.b10*m.b18*m.b19 + 256*m.b9*m.b10*m.b19*
                       m.b20 + 192*m.b9*m.b10*m.b20*m.b21 + 128*m.b9*m.b10*m.b21*m.b22 + 64*m.b9*m.b10*m.b22*m.b23 + 576
                       *m.b9*m.b11*m.b12*m.b14 + 576*m.b9*m.b11*m.b13*m.b15 + 512*m.b9*m.b11*m.b14*m.b16 + 448*m.b9*
                       m.b11*m.b15*m.b17 + 384*m.b9*m.b11*m.b16*m.b18 + 320*m.b9*m.b11*m.b17*m.b19 + 256*m.b9*m.b11*
                       m.b18*m.b20 + 192*m.b9*m.b11*m.b19*m.b21 + 128*m.b9*m.b11*m.b20*m.b22 + 64*m.b9*m.b11*m.b21*m.b23
                        + 512*m.b9*m.b12*m.b13*m.b16 + 448*m.b9*m.b12*m.b14*m.b17 + 384*m.b9*m.b12*m.b15*m.b18 + 320*
                       m.b9*m.b12*m.b16*m.b19 + 256*m.b9*m.b12*m.b17*m.b20 + 192*m.b9*m.b12*m.b18*m.b21 + 128*m.b9*m.b12
                       *m.b19*m.b22 + 64*m.b9*m.b12*m.b20*m.b23 + 384*m.b9*m.b13*m.b14*m.b18 + 320*m.b9*m.b13*m.b15*
                       m.b19 + 256*m.b9*m.b13*m.b16*m.b20 + 192*m.b9*m.b13*m.b17*m.b21 + 128*m.b9*m.b13*m.b18*m.b22 + 64
                       *m.b9*m.b13*m.b19*m.b23 + 256*m.b9*m.b14*m.b15*m.b20 + 192*m.b9*m.b14*m.b16*m.b21 + 128*m.b9*
                       m.b14*m.b17*m.b22 + 64*m.b9*m.b14*m.b18*m.b23 + 128*m.b9*m.b15*m.b16*m.b22 + 64*m.b9*m.b15*m.b17*
                       m.b23 + 640*m.b10*m.b11*m.b12*m.b13 + 640*m.b10*m.b11*m.b13*m.b14 + 640*m.b10*m.b11*m.b14*m.b15
                        + 576*m.b10*m.b11*m.b15*m.b16 + 512*m.b10*m.b11*m.b16*m.b17 + 448*m.b10*m.b11*m.b17*m.b18 + 384*
                       m.b10*m.b11*m.b18*m.b19 + 320*m.b10*m.b11*m.b19*m.b20 + 256*m.b10*m.b11*m.b20*m.b21 + 192*m.b10*
                       m.b11*m.b21*m.b22 + 128*m.b10*m.b11*m.b22*m.b23 + 64*m.b10*m.b11*m.b23*m.b24 + 640*m.b10*m.b12*
                       m.b13*m.b15 + 576*m.b10*m.b12*m.b14*m.b16 + 512*m.b10*m.b12*m.b15*m.b17 + 448*m.b10*m.b12*m.b16*
                       m.b18 + 384*m.b10*m.b12*m.b17*m.b19 + 320*m.b10*m.b12*m.b18*m.b20 + 256*m.b10*m.b12*m.b19*m.b21
                        + 192*m.b10*m.b12*m.b20*m.b22 + 128*m.b10*m.b12*m.b21*m.b23 + 64*m.b10*m.b12*m.b22*m.b24 + 512*
                       m.b10*m.b13*m.b14*m.b17 + 448*m.b10*m.b13*m.b15*m.b18 + 384*m.b10*m.b13*m.b16*m.b19 + 320*m.b10*
                       m.b13*m.b17*m.b20 + 256*m.b10*m.b13*m.b18*m.b21 + 192*m.b10*m.b13*m.b19*m.b22 + 128*m.b10*m.b13*
                       m.b20*m.b23 + 64*m.b10*m.b13*m.b21*m.b24 + 384*m.b10*m.b14*m.b15*m.b19 + 320*m.b10*m.b14*m.b16*
                       m.b20 + 256*m.b10*m.b14*m.b17*m.b21 + 192*m.b10*m.b14*m.b18*m.b22 + 128*m.b10*m.b14*m.b19*m.b23
                        + 64*m.b10*m.b14*m.b20*m.b24 + 256*m.b10*m.b15*m.b16*m.b21 + 192*m.b10*m.b15*m.b17*m.b22 + 128*
                       m.b10*m.b15*m.b18*m.b23 + 64*m.b10*m.b15*m.b19*m.b24 + 128*m.b10*m.b16*m.b17*m.b23 + 64*m.b10*
                       m.b16*m.b18*m.b24 + 704*m.b11*m.b12*m.b13*m.b14 + 704*m.b11*m.b12*m.b14*m.b15 + 640*m.b11*m.b12*
                       m.b15*m.b16 + 576*m.b11*m.b12*m.b16*m.b17 + 512*m.b11*m.b12*m.b17*m.b18 + 448*m.b11*m.b12*m.b18*
                       m.b19 + 384*m.b11*m.b12*m.b19*m.b20 + 320*m.b11*m.b12*m.b20*m.b21 + 256*m.b11*m.b12*m.b21*m.b22
                        + 192*m.b11*m.b12*m.b22*m.b23 + 128*m.b11*m.b12*m.b23*m.b24 + 64*m.b11*m.b12*m.b24*m.b25 + 640*
                       m.b11*m.b13*m.b14*m.b16 + 576*m.b11*m.b13*m.b15*m.b17 + 512*m.b11*m.b13*m.b16*m.b18 + 448*m.b11*
                       m.b13*m.b17*m.b19 + 384*m.b11*m.b13*m.b18*m.b20 + 320*m.b11*m.b13*m.b19*m.b21 + 256*m.b11*m.b13*
                       m.b20*m.b22 + 192*m.b11*m.b13*m.b21*m.b23 + 128*m.b11*m.b13*m.b22*m.b24 + 64*m.b11*m.b13*m.b23*
                       m.b25 + 512*m.b11*m.b14*m.b15*m.b18 + 448*m.b11*m.b14*m.b16*m.b19 + 384*m.b11*m.b14*m.b17*m.b20
                        + 320*m.b11*m.b14*m.b18*m.b21 + 256*m.b11*m.b14*m.b19*m.b22 + 192*m.b11*m.b14*m.b20*m.b23 + 128*
                       m.b11*m.b14*m.b21*m.b24 + 64*m.b11*m.b14*m.b22*m.b25 + 384*m.b11*m.b15*m.b16*m.b20 + 320*m.b11*
                       m.b15*m.b17*m.b21 + 256*m.b11*m.b15*m.b18*m.b22 + 192*m.b11*m.b15*m.b19*m.b23 + 128*m.b11*m.b15*
                       m.b20*m.b24 + 64*m.b11*m.b15*m.b21*m.b25 + 256*m.b11*m.b16*m.b17*m.b22 + 192*m.b11*m.b16*m.b18*
                       m.b23 + 128*m.b11*m.b16*m.b19*m.b24 + 64*m.b11*m.b16*m.b20*m.b25 + 128*m.b11*m.b17*m.b18*m.b24 + 
                       64*m.b11*m.b17*m.b19*m.b25 + 768*m.b12*m.b13*m.b14*m.b15 + 704*m.b12*m.b13*m.b15*m.b16 + 640*
                       m.b12*m.b13*m.b16*m.b17 + 576*m.b12*m.b13*m.b17*m.b18 + 512*m.b12*m.b13*m.b18*m.b19 + 448*m.b12*
                       m.b13*m.b19*m.b20 + 384*m.b12*m.b13*m.b20*m.b21 + 320*m.b12*m.b13*m.b21*m.b22 + 256*m.b12*m.b13*
                       m.b22*m.b23 + 192*m.b12*m.b13*m.b23*m.b24 + 128*m.b12*m.b13*m.b24*m.b25 + 64*m.b12*m.b13*m.b25*
                       m.b26 + 640*m.b12*m.b14*m.b15*m.b17 + 576*m.b12*m.b14*m.b16*m.b18 + 512*m.b12*m.b14*m.b17*m.b19
                        + 448*m.b12*m.b14*m.b18*m.b20 + 384*m.b12*m.b14*m.b19*m.b21 + 320*m.b12*m.b14*m.b20*m.b22 + 256*
                       m.b12*m.b14*m.b21*m.b23 + 192*m.b12*m.b14*m.b22*m.b24 + 128*m.b12*m.b14*m.b23*m.b25 + 64*m.b12*
                       m.b14*m.b24*m.b26 + 512*m.b12*m.b15*m.b16*m.b19 + 448*m.b12*m.b15*m.b17*m.b20 + 384*m.b12*m.b15*
                       m.b18*m.b21 + 320*m.b12*m.b15*m.b19*m.b22 + 256*m.b12*m.b15*m.b20*m.b23 + 192*m.b12*m.b15*m.b21*
                       m.b24 + 128*m.b12*m.b15*m.b22*m.b25 + 64*m.b12*m.b15*m.b23*m.b26 + 384*m.b12*m.b16*m.b17*m.b21 + 
                       320*m.b12*m.b16*m.b18*m.b22 + 256*m.b12*m.b16*m.b19*m.b23 + 192*m.b12*m.b16*m.b20*m.b24 + 128*
                       m.b12*m.b16*m.b21*m.b25 + 64*m.b12*m.b16*m.b22*m.b26 + 256*m.b12*m.b17*m.b18*m.b23 + 192*m.b12*
                       m.b17*m.b19*m.b24 + 128*m.b12*m.b17*m.b20*m.b25 + 64*m.b12*m.b17*m.b21*m.b26 + 128*m.b12*m.b18*
                       m.b19*m.b25 + 64*m.b12*m.b18*m.b20*m.b26 + 768*m.b13*m.b14*m.b15*m.b16 + 704*m.b13*m.b14*m.b16*
                       m.b17 + 640*m.b13*m.b14*m.b17*m.b18 + 576*m.b13*m.b14*m.b18*m.b19 + 512*m.b13*m.b14*m.b19*m.b20
                        + 448*m.b13*m.b14*m.b20*m.b21 + 384*m.b13*m.b14*m.b21*m.b22 + 320*m.b13*m.b14*m.b22*m.b23 + 256*
                       m.b13*m.b14*m.b23*m.b24 + 192*m.b13*m.b14*m.b24*m.b25 + 128*m.b13*m.b14*m.b25*m.b26 + 64*m.b13*
                       m.b14*m.b26*m.b27 + 640*m.b13*m.b15*m.b16*m.b18 + 576*m.b13*m.b15*m.b17*m.b19 + 512*m.b13*m.b15*
                       m.b18*m.b20 + 448*m.b13*m.b15*m.b19*m.b21 + 384*m.b13*m.b15*m.b20*m.b22 + 320*m.b13*m.b15*m.b21*
                       m.b23 + 256*m.b13*m.b15*m.b22*m.b24 + 192*m.b13*m.b15*m.b23*m.b25 + 128*m.b13*m.b15*m.b24*m.b26
                        + 64*m.b13*m.b15*m.b25*m.b27 + 512*m.b13*m.b16*m.b17*m.b20 + 448*m.b13*m.b16*m.b18*m.b21 + 384*
                       m.b13*m.b16*m.b19*m.b22 + 320*m.b13*m.b16*m.b20*m.b23 + 256*m.b13*m.b16*m.b21*m.b24 + 192*m.b13*
                       m.b16*m.b22*m.b25 + 128*m.b13*m.b16*m.b23*m.b26 + 64*m.b13*m.b16*m.b24*m.b27 + 384*m.b13*m.b17*
                       m.b18*m.b22 + 320*m.b13*m.b17*m.b19*m.b23 + 256*m.b13*m.b17*m.b20*m.b24 + 192*m.b13*m.b17*m.b21*
                       m.b25 + 128*m.b13*m.b17*m.b22*m.b26 + 64*m.b13*m.b17*m.b23*m.b27 + 256*m.b13*m.b18*m.b19*m.b24 + 
                       192*m.b13*m.b18*m.b20*m.b25 + 128*m.b13*m.b18*m.b21*m.b26 + 64*m.b13*m.b18*m.b22*m.b27 + 128*
                       m.b13*m.b19*m.b20*m.b26 + 64*m.b13*m.b19*m.b21*m.b27 + 768*m.b14*m.b15*m.b16*m.b17 + 704*m.b14*
                       m.b15*m.b17*m.b18 + 640*m.b14*m.b15*m.b18*m.b19 + 576*m.b14*m.b15*m.b19*m.b20 + 512*m.b14*m.b15*
                       m.b20*m.b21 + 448*m.b14*m.b15*m.b21*m.b22 + 384*m.b14*m.b15*m.b22*m.b23 + 320*m.b14*m.b15*m.b23*
                       m.b24 + 256*m.b14*m.b15*m.b24*m.b25 + 192*m.b14*m.b15*m.b25*m.b26 + 128*m.b14*m.b15*m.b26*m.b27
                        + 64*m.b14*m.b15*m.b27*m.b28 + 640*m.b14*m.b16*m.b17*m.b19 + 576*m.b14*m.b16*m.b18*m.b20 + 512*
                       m.b14*m.b16*m.b19*m.b21 + 448*m.b14*m.b16*m.b20*m.b22 + 384*m.b14*m.b16*m.b21*m.b23 + 320*m.b14*
                       m.b16*m.b22*m.b24 + 256*m.b14*m.b16*m.b23*m.b25 + 192*m.b14*m.b16*m.b24*m.b26 + 128*m.b14*m.b16*
                       m.b25*m.b27 + 64*m.b14*m.b16*m.b26*m.b28 + 512*m.b14*m.b17*m.b18*m.b21 + 448*m.b14*m.b17*m.b19*
                       m.b22 + 384*m.b14*m.b17*m.b20*m.b23 + 320*m.b14*m.b17*m.b21*m.b24 + 256*m.b14*m.b17*m.b22*m.b25
                        + 192*m.b14*m.b17*m.b23*m.b26 + 128*m.b14*m.b17*m.b24*m.b27 + 64*m.b14*m.b17*m.b25*m.b28 + 384*
                       m.b14*m.b18*m.b19*m.b23 + 320*m.b14*m.b18*m.b20*m.b24 + 256*m.b14*m.b18*m.b21*m.b25 + 192*m.b14*
                       m.b18*m.b22*m.b26 + 128*m.b14*m.b18*m.b23*m.b27 + 64*m.b14*m.b18*m.b24*m.b28 + 256*m.b14*m.b19*
                       m.b20*m.b25 + 192*m.b14*m.b19*m.b21*m.b26 + 128*m.b14*m.b19*m.b22*m.b27 + 64*m.b14*m.b19*m.b23*
                       m.b28 + 128*m.b14*m.b20*m.b21*m.b27 + 64*m.b14*m.b20*m.b22*m.b28 + 768*m.b15*m.b16*m.b17*m.b18 + 
                       704*m.b15*m.b16*m.b18*m.b19 + 640*m.b15*m.b16*m.b19*m.b20 + 576*m.b15*m.b16*m.b20*m.b21 + 512*
                       m.b15*m.b16*m.b21*m.b22 + 448*m.b15*m.b16*m.b22*m.b23 + 384*m.b15*m.b16*m.b23*m.b24 + 320*m.b15*
                       m.b16*m.b24*m.b25 + 256*m.b15*m.b16*m.b25*m.b26 + 192*m.b15*m.b16*m.b26*m.b27 + 128*m.b15*m.b16*
                       m.b27*m.b28 + 64*m.b15*m.b16*m.b28*m.b29 + 640*m.b15*m.b17*m.b18*m.b20 + 576*m.b15*m.b17*m.b19*
                       m.b21 + 512*m.b15*m.b17*m.b20*m.b22 + 448*m.b15*m.b17*m.b21*m.b23 + 384*m.b15*m.b17*m.b22*m.b24
                        + 320*m.b15*m.b17*m.b23*m.b25 + 256*m.b15*m.b17*m.b24*m.b26 + 192*m.b15*m.b17*m.b25*m.b27 + 128*
                       m.b15*m.b17*m.b26*m.b28 + 64*m.b15*m.b17*m.b27*m.b29 + 512*m.b15*m.b18*m.b19*m.b22 + 448*m.b15*
                       m.b18*m.b20*m.b23 + 384*m.b15*m.b18*m.b21*m.b24 + 320*m.b15*m.b18*m.b22*m.b25 + 256*m.b15*m.b18*
                       m.b23*m.b26 + 192*m.b15*m.b18*m.b24*m.b27 + 128*m.b15*m.b18*m.b25*m.b28 + 64*m.b15*m.b18*m.b26*
                       m.b29 + 384*m.b15*m.b19*m.b20*m.b24 + 320*m.b15*m.b19*m.b21*m.b25 + 256*m.b15*m.b19*m.b22*m.b26
                        + 192*m.b15*m.b19*m.b23*m.b27 + 128*m.b15*m.b19*m.b24*m.b28 + 64*m.b15*m.b19*m.b25*m.b29 + 256*
                       m.b15*m.b20*m.b21*m.b26 + 192*m.b15*m.b20*m.b22*m.b27 + 128*m.b15*m.b20*m.b23*m.b28 + 64*m.b15*
                       m.b20*m.b24*m.b29 + 128*m.b15*m.b21*m.b22*m.b28 + 64*m.b15*m.b21*m.b23*m.b29 + 768*m.b16*m.b17*
                       m.b18*m.b19 + 704*m.b16*m.b17*m.b19*m.b20 + 640*m.b16*m.b17*m.b20*m.b21 + 576*m.b16*m.b17*m.b21*
                       m.b22 + 512*m.b16*m.b17*m.b22*m.b23 + 448*m.b16*m.b17*m.b23*m.b24 + 384*m.b16*m.b17*m.b24*m.b25
                        + 320*m.b16*m.b17*m.b25*m.b26 + 256*m.b16*m.b17*m.b26*m.b27 + 192*m.b16*m.b17*m.b27*m.b28 + 128*
                       m.b16*m.b17*m.b28*m.b29 + 64*m.b16*m.b17*m.b29*m.b30 + 640*m.b16*m.b18*m.b19*m.b21 + 576*m.b16*
                       m.b18*m.b20*m.b22 + 512*m.b16*m.b18*m.b21*m.b23 + 448*m.b16*m.b18*m.b22*m.b24 + 384*m.b16*m.b18*
                       m.b23*m.b25 + 320*m.b16*m.b18*m.b24*m.b26 + 256*m.b16*m.b18*m.b25*m.b27 + 192*m.b16*m.b18*m.b26*
                       m.b28 + 128*m.b16*m.b18*m.b27*m.b29 + 64*m.b16*m.b18*m.b28*m.b30 + 512*m.b16*m.b19*m.b20*m.b23 + 
                       448*m.b16*m.b19*m.b21*m.b24 + 384*m.b16*m.b19*m.b22*m.b25 + 320*m.b16*m.b19*m.b23*m.b26 + 256*
                       m.b16*m.b19*m.b24*m.b27 + 192*m.b16*m.b19*m.b25*m.b28 + 128*m.b16*m.b19*m.b26*m.b29 + 64*m.b16*
                       m.b19*m.b27*m.b30 + 384*m.b16*m.b20*m.b21*m.b25 + 320*m.b16*m.b20*m.b22*m.b26 + 256*m.b16*m.b20*
                       m.b23*m.b27 + 192*m.b16*m.b20*m.b24*m.b28 + 128*m.b16*m.b20*m.b25*m.b29 + 64*m.b16*m.b20*m.b26*
                       m.b30 + 256*m.b16*m.b21*m.b22*m.b27 + 192*m.b16*m.b21*m.b23*m.b28 + 128*m.b16*m.b21*m.b24*m.b29
                        + 64*m.b16*m.b21*m.b25*m.b30 + 128*m.b16*m.b22*m.b23*m.b29 + 64*m.b16*m.b22*m.b24*m.b30 + 704*
                       m.b17*m.b18*m.b19*m.b20 + 640*m.b17*m.b18*m.b20*m.b21 + 576*m.b17*m.b18*m.b21*m.b22 + 512*m.b17*
                       m.b18*m.b22*m.b23 + 448*m.b17*m.b18*m.b23*m.b24 + 384*m.b17*m.b18*m.b24*m.b25 + 320*m.b17*m.b18*
                       m.b25*m.b26 + 256*m.b17*m.b18*m.b26*m.b27 + 192*m.b17*m.b18*m.b27*m.b28 + 128*m.b17*m.b18*m.b28*
                       m.b29 + 64*m.b17*m.b18*m.b29*m.b30 + 576*m.b17*m.b19*m.b20*m.b22 + 512*m.b17*m.b19*m.b21*m.b23 + 
                       448*m.b17*m.b19*m.b22*m.b24 + 384*m.b17*m.b19*m.b23*m.b25 + 320*m.b17*m.b19*m.b24*m.b26 + 256*
                       m.b17*m.b19*m.b25*m.b27 + 192*m.b17*m.b19*m.b26*m.b28 + 128*m.b17*m.b19*m.b27*m.b29 + 64*m.b17*
                       m.b19*m.b28*m.b30 + 448*m.b17*m.b20*m.b21*m.b24 + 384*m.b17*m.b20*m.b22*m.b25 + 320*m.b17*m.b20*
                       m.b23*m.b26 + 256*m.b17*m.b20*m.b24*m.b27 + 192*m.b17*m.b20*m.b25*m.b28 + 128*m.b17*m.b20*m.b26*
                       m.b29 + 64*m.b17*m.b20*m.b27*m.b30 + 320*m.b17*m.b21*m.b22*m.b26 + 256*m.b17*m.b21*m.b23*m.b27 + 
                       192*m.b17*m.b21*m.b24*m.b28 + 128*m.b17*m.b21*m.b25*m.b29 + 64*m.b17*m.b21*m.b26*m.b30 + 192*
                       m.b17*m.b22*m.b23*m.b28 + 128*m.b17*m.b22*m.b24*m.b29 + 64*m.b17*m.b22*m.b25*m.b30 + 64*m.b17*
                       m.b23*m.b24*m.b30 + 640*m.b18*m.b19*m.b20*m.b21 + 576*m.b18*m.b19*m.b21*m.b22 + 512*m.b18*m.b19*
                       m.b22*m.b23 + 448*m.b18*m.b19*m.b23*m.b24 + 384*m.b18*m.b19*m.b24*m.b25 + 320*m.b18*m.b19*m.b25*
                       m.b26 + 256*m.b18*m.b19*m.b26*m.b27 + 192*m.b18*m.b19*m.b27*m.b28 + 128*m.b18*m.b19*m.b28*m.b29
                        + 64*m.b18*m.b19*m.b29*m.b30 + 512*m.b18*m.b20*m.b21*m.b23 + 448*m.b18*m.b20*m.b22*m.b24 + 384*
                       m.b18*m.b20*m.b23*m.b25 + 320*m.b18*m.b20*m.b24*m.b26 + 256*m.b18*m.b20*m.b25*m.b27 + 192*m.b18*
                       m.b20*m.b26*m.b28 + 128*m.b18*m.b20*m.b27*m.b29 + 64*m.b18*m.b20*m.b28*m.b30 + 384*m.b18*m.b21*
                       m.b22*m.b25 + 320*m.b18*m.b21*m.b23*m.b26 + 256*m.b18*m.b21*m.b24*m.b27 + 192*m.b18*m.b21*m.b25*
                       m.b28 + 128*m.b18*m.b21*m.b26*m.b29 + 64*m.b18*m.b21*m.b27*m.b30 + 256*m.b18*m.b22*m.b23*m.b27 + 
                       192*m.b18*m.b22*m.b24*m.b28 + 128*m.b18*m.b22*m.b25*m.b29 + 64*m.b18*m.b22*m.b26*m.b30 + 128*
                       m.b18*m.b23*m.b24*m.b29 + 64*m.b18*m.b23*m.b25*m.b30 + 576*m.b19*m.b20*m.b21*m.b22 + 512*m.b19*
                       m.b20*m.b22*m.b23 + 448*m.b19*m.b20*m.b23*m.b24 + 384*m.b19*m.b20*m.b24*m.b25 + 320*m.b19*m.b20*
                       m.b25*m.b26 + 256*m.b19*m.b20*m.b26*m.b27 + 192*m.b19*m.b20*m.b27*m.b28 + 128*m.b19*m.b20*m.b28*
                       m.b29 + 64*m.b19*m.b20*m.b29*m.b30 + 448*m.b19*m.b21*m.b22*m.b24 + 384*m.b19*m.b21*m.b23*m.b25 + 
                       320*m.b19*m.b21*m.b24*m.b26 + 256*m.b19*m.b21*m.b25*m.b27 + 192*m.b19*m.b21*m.b26*m.b28 + 128*
                       m.b19*m.b21*m.b27*m.b29 + 64*m.b19*m.b21*m.b28*m.b30 + 320*m.b19*m.b22*m.b23*m.b26 + 256*m.b19*
                       m.b22*m.b24*m.b27 + 192*m.b19*m.b22*m.b25*m.b28 + 128*m.b19*m.b22*m.b26*m.b29 + 64*m.b19*m.b22*
                       m.b27*m.b30 + 192*m.b19*m.b23*m.b24*m.b28 + 128*m.b19*m.b23*m.b25*m.b29 + 64*m.b19*m.b23*m.b26*
                       m.b30 + 64*m.b19*m.b24*m.b25*m.b30 + 512*m.b20*m.b21*m.b22*m.b23 + 448*m.b20*m.b21*m.b23*m.b24 + 
                       384*m.b20*m.b21*m.b24*m.b25 + 320*m.b20*m.b21*m.b25*m.b26 + 256*m.b20*m.b21*m.b26*m.b27 + 192*
                       m.b20*m.b21*m.b27*m.b28 + 128*m.b20*m.b21*m.b28*m.b29 + 64*m.b20*m.b21*m.b29*m.b30 + 384*m.b20*
                       m.b22*m.b23*m.b25 + 320*m.b20*m.b22*m.b24*m.b26 + 256*m.b20*m.b22*m.b25*m.b27 + 192*m.b20*m.b22*
                       m.b26*m.b28 + 128*m.b20*m.b22*m.b27*m.b29 + 64*m.b20*m.b22*m.b28*m.b30 + 256*m.b20*m.b23*m.b24*
                       m.b27 + 192*m.b20*m.b23*m.b25*m.b28 + 128*m.b20*m.b23*m.b26*m.b29 + 64*m.b20*m.b23*m.b27*m.b30 + 
                       128*m.b20*m.b24*m.b25*m.b29 + 64*m.b20*m.b24*m.b26*m.b30 + 448*m.b21*m.b22*m.b23*m.b24 + 384*
                       m.b21*m.b22*m.b24*m.b25 + 320*m.b21*m.b22*m.b25*m.b26 + 256*m.b21*m.b22*m.b26*m.b27 + 192*m.b21*
                       m.b22*m.b27*m.b28 + 128*m.b21*m.b22*m.b28*m.b29 + 64*m.b21*m.b22*m.b29*m.b30 + 320*m.b21*m.b23*
                       m.b24*m.b26 + 256*m.b21*m.b23*m.b25*m.b27 + 192*m.b21*m.b23*m.b26*m.b28 + 128*m.b21*m.b23*m.b27*
                       m.b29 + 64*m.b21*m.b23*m.b28*m.b30 + 192*m.b21*m.b24*m.b25*m.b28 + 128*m.b21*m.b24*m.b26*m.b29 + 
                       64*m.b21*m.b24*m.b27*m.b30 + 64*m.b21*m.b25*m.b26*m.b30 + 384*m.b22*m.b23*m.b24*m.b25 + 320*m.b22
                       *m.b23*m.b25*m.b26 + 256*m.b22*m.b23*m.b26*m.b27 + 192*m.b22*m.b23*m.b27*m.b28 + 128*m.b22*m.b23*
                       m.b28*m.b29 + 64*m.b22*m.b23*m.b29*m.b30 + 256*m.b22*m.b24*m.b25*m.b27 + 192*m.b22*m.b24*m.b26*
                       m.b28 + 128*m.b22*m.b24*m.b27*m.b29 + 64*m.b22*m.b24*m.b28*m.b30 + 128*m.b22*m.b25*m.b26*m.b29 + 
                       64*m.b22*m.b25*m.b27*m.b30 + 320*m.b23*m.b24*m.b25*m.b26 + 256*m.b23*m.b24*m.b26*m.b27 + 192*
                       m.b23*m.b24*m.b27*m.b28 + 128*m.b23*m.b24*m.b28*m.b29 + 64*m.b23*m.b24*m.b29*m.b30 + 192*m.b23*
                       m.b25*m.b26*m.b28 + 128*m.b23*m.b25*m.b27*m.b29 + 64*m.b23*m.b25*m.b28*m.b30 + 64*m.b23*m.b26*
                       m.b27*m.b30 + 256*m.b24*m.b25*m.b26*m.b27 + 192*m.b24*m.b25*m.b27*m.b28 + 128*m.b24*m.b25*m.b28*
                       m.b29 + 64*m.b24*m.b25*m.b29*m.b30 + 128*m.b24*m.b26*m.b27*m.b29 + 64*m.b24*m.b26*m.b28*m.b30 + 
                       192*m.b25*m.b26*m.b27*m.b28 + 128*m.b25*m.b26*m.b28*m.b29 + 64*m.b25*m.b26*m.b29*m.b30 + 64*m.b25
                       *m.b27*m.b28*m.b30 + 128*m.b26*m.b27*m.b28*m.b29 + 64*m.b26*m.b27*m.b29*m.b30 + 64*m.b27*m.b28*
                       m.b29*m.b30 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*
                       m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11
                        - 64*m.b1*m.b2*m.b12 - 64*m.b1*m.b2*m.b13 - 64*m.b1*m.b2*m.b14 - 32*m.b1*m.b2*m.b15 - 64*m.b1*
                       m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*
                       m.b1*m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*m.b11 - 64*m.b1*m.b3*m.b12 - 64*m.b1*m.b3*
                       m.b13 - 32*m.b1*m.b3*m.b14 - 32*m.b1*m.b3*m.b15 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1
                       *m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64
                       *m.b1*m.b4*m.b12 - 32*m.b1*m.b4*m.b13 - 32*m.b1*m.b4*m.b14 - 32*m.b1*m.b4*m.b15 - 64*m.b1*m.b5*
                       m.b6 - 64*m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 64*m.b1*
                       m.b5*m.b11 - 32*m.b1*m.b5*m.b12 - 32*m.b1*m.b5*m.b13 - 32*m.b1*m.b5*m.b14 - 32*m.b1*m.b5*m.b15 - 
                       64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10 - 32*m.b1*m.b6*
                       m.b12 - 32*m.b1*m.b6*m.b13 - 32*m.b1*m.b6*m.b14 - 32*m.b1*m.b6*m.b15 - 64*m.b1*m.b7*m.b8 - 64*
                       m.b1*m.b7*m.b9 - 32*m.b1*m.b7*m.b10 - 32*m.b1*m.b7*m.b11 - 32*m.b1*m.b7*m.b12 - 32*m.b1*m.b7*
                       m.b14 - 32*m.b1*m.b7*m.b15 - 32*m.b1*m.b8*m.b9 - 32*m.b1*m.b8*m.b10 - 32*m.b1*m.b8*m.b11 - 32*
                       m.b1*m.b8*m.b12 - 32*m.b1*m.b8*m.b13 - 32*m.b1*m.b8*m.b14 - 32*m.b1*m.b9*m.b10 - 32*m.b1*m.b9*
                       m.b11 - 32*m.b1*m.b9*m.b12 - 32*m.b1*m.b9*m.b13 - 32*m.b1*m.b9*m.b14 - 32*m.b1*m.b9*m.b15 - 32*
                       m.b1*m.b10*m.b11 - 32*m.b1*m.b10*m.b12 - 32*m.b1*m.b10*m.b13 - 32*m.b1*m.b10*m.b14 - 32*m.b1*
                       m.b10*m.b15 - 32*m.b1*m.b11*m.b12 - 32*m.b1*m.b11*m.b13 - 32*m.b1*m.b11*m.b14 - 32*m.b1*m.b11*
                       m.b15 - 32*m.b1*m.b12*m.b13 - 32*m.b1*m.b12*m.b14 - 32*m.b1*m.b12*m.b15 - 32*m.b1*m.b13*m.b14 - 
                       32*m.b1*m.b13*m.b15 - 32*m.b1*m.b14*m.b15 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*
                       m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 
                       128*m.b2*m.b3*m.b11 - 128*m.b2*m.b3*m.b12 - 128*m.b2*m.b3*m.b13 - 128*m.b2*m.b3*m.b14 - 96*m.b2*
                       m.b3*m.b15 - 32*m.b2*m.b3*m.b16 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 
                       128*m.b2*m.b4*m.b8 - 128*m.b2*m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*m.b4*m.b11 - 128*m.b2*
                       m.b4*m.b12 - 128*m.b2*m.b4*m.b13 - 96*m.b2*m.b4*m.b14 - 64*m.b2*m.b4*m.b15 - 32*m.b2*m.b4*m.b16
                        - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*
                       m.b5*m.b10 - 128*m.b2*m.b5*m.b11 - 128*m.b2*m.b5*m.b12 - 96*m.b2*m.b5*m.b13 - 64*m.b2*m.b5*m.b14
                        - 64*m.b2*m.b5*m.b15 - 32*m.b2*m.b5*m.b16 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*m.b8 - 128*m.b2*
                       m.b6*m.b9 - 64*m.b2*m.b6*m.b10 - 128*m.b2*m.b6*m.b11 - 96*m.b2*m.b6*m.b12 - 64*m.b2*m.b6*m.b13 - 
                       64*m.b2*m.b6*m.b14 - 64*m.b2*m.b6*m.b15 - 32*m.b2*m.b6*m.b16 - 160*m.b2*m.b7*m.b8 - 128*m.b2*m.b7
                       *m.b9 - 128*m.b2*m.b7*m.b10 - 96*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b13 - 64*m.b2*m.b7*m.b14 - 64*
                       m.b2*m.b7*m.b15 - 32*m.b2*m.b7*m.b16 - 160*m.b2*m.b8*m.b9 - 96*m.b2*m.b8*m.b10 - 64*m.b2*m.b8*
                       m.b11 - 64*m.b2*m.b8*m.b12 - 64*m.b2*m.b8*m.b13 - 64*m.b2*m.b8*m.b15 - 32*m.b2*m.b8*m.b16 - 96*
                       m.b2*m.b9*m.b10 - 64*m.b2*m.b9*m.b11 - 64*m.b2*m.b9*m.b12 - 64*m.b2*m.b9*m.b13 - 64*m.b2*m.b9*
                       m.b14 - 64*m.b2*m.b9*m.b15 - 96*m.b2*m.b10*m.b11 - 64*m.b2*m.b10*m.b12 - 64*m.b2*m.b10*m.b13 - 64
                       *m.b2*m.b10*m.b14 - 64*m.b2*m.b10*m.b15 - 32*m.b2*m.b10*m.b16 - 96*m.b2*m.b11*m.b12 - 64*m.b2*
                       m.b11*m.b13 - 64*m.b2*m.b11*m.b14 - 64*m.b2*m.b11*m.b15 - 32*m.b2*m.b11*m.b16 - 96*m.b2*m.b12*
                       m.b13 - 64*m.b2*m.b12*m.b14 - 64*m.b2*m.b12*m.b15 - 32*m.b2*m.b12*m.b16 - 96*m.b2*m.b13*m.b14 - 
                       64*m.b2*m.b13*m.b15 - 32*m.b2*m.b13*m.b16 - 96*m.b2*m.b14*m.b15 - 32*m.b2*m.b14*m.b16 - 32*m.b2*
                       m.b15*m.b16 - 160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8
                        - 192*m.b3*m.b4*m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*m.b12 - 192*
                       m.b3*m.b4*m.b13 - 192*m.b3*m.b4*m.b14 - 160*m.b3*m.b4*m.b15 - 96*m.b3*m.b4*m.b16 - 32*m.b3*m.b4*
                       m.b17 - 256*m.b3*m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*
                       m.b3*m.b5*m.b10 - 192*m.b3*m.b5*m.b11 - 192*m.b3*m.b5*m.b12 - 192*m.b3*m.b5*m.b13 - 160*m.b3*m.b5
                       *m.b14 - 128*m.b3*m.b5*m.b15 - 64*m.b3*m.b5*m.b16 - 32*m.b3*m.b5*m.b17 - 256*m.b3*m.b6*m.b7 - 224
                       *m.b3*m.b6*m.b8 - 96*m.b3*m.b6*m.b9 - 192*m.b3*m.b6*m.b10 - 192*m.b3*m.b6*m.b11 - 192*m.b3*m.b6*
                       m.b12 - 160*m.b3*m.b6*m.b13 - 128*m.b3*m.b6*m.b14 - 96*m.b3*m.b6*m.b15 - 64*m.b3*m.b6*m.b16 - 32*
                       m.b3*m.b6*m.b17 - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 192*m.b3*m.b7*m.b10 - 96*m.b3*m.b7*
                       m.b11 - 160*m.b3*m.b7*m.b12 - 128*m.b3*m.b7*m.b13 - 96*m.b3*m.b7*m.b14 - 96*m.b3*m.b7*m.b15 - 64*
                       m.b3*m.b7*m.b16 - 32*m.b3*m.b7*m.b17 - 256*m.b3*m.b8*m.b9 - 224*m.b3*m.b8*m.b10 - 160*m.b3*m.b8*
                       m.b11 - 128*m.b3*m.b8*m.b12 - 96*m.b3*m.b8*m.b14 - 96*m.b3*m.b8*m.b15 - 64*m.b3*m.b8*m.b16 - 32*
                       m.b3*m.b8*m.b17 - 224*m.b3*m.b9*m.b10 - 160*m.b3*m.b9*m.b11 - 96*m.b3*m.b9*m.b12 - 96*m.b3*m.b9*
                       m.b13 - 96*m.b3*m.b9*m.b14 - 64*m.b3*m.b9*m.b16 - 32*m.b3*m.b9*m.b17 - 160*m.b3*m.b10*m.b11 - 128
                       *m.b3*m.b10*m.b12 - 96*m.b3*m.b10*m.b13 - 96*m.b3*m.b10*m.b14 - 96*m.b3*m.b10*m.b15 - 64*m.b3*
                       m.b10*m.b16 - 160*m.b3*m.b11*m.b12 - 128*m.b3*m.b11*m.b13 - 96*m.b3*m.b11*m.b14 - 96*m.b3*m.b11*
                       m.b15 - 64*m.b3*m.b11*m.b16 - 32*m.b3*m.b11*m.b17 - 160*m.b3*m.b12*m.b13 - 128*m.b3*m.b12*m.b14
                        - 96*m.b3*m.b12*m.b15 - 64*m.b3*m.b12*m.b16 - 32*m.b3*m.b12*m.b17 - 160*m.b3*m.b13*m.b14 - 128*
                       m.b3*m.b13*m.b15 - 64*m.b3*m.b13*m.b16 - 32*m.b3*m.b13*m.b17 - 160*m.b3*m.b14*m.b15 - 64*m.b3*
                       m.b14*m.b16 - 32*m.b3*m.b14*m.b17 - 96*m.b3*m.b15*m.b16 - 32*m.b3*m.b15*m.b17 - 32*m.b3*m.b16*
                       m.b17 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*
                       m.b4*m.b5*m.b10 - 256*m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 256*m.b4*m.b5*m.b13 - 256*m.b4*m.b5
                       *m.b14 - 224*m.b4*m.b5*m.b15 - 160*m.b4*m.b5*m.b16 - 96*m.b4*m.b5*m.b17 - 32*m.b4*m.b5*m.b18 - 
                       352*m.b4*m.b6*m.b7 - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10 - 256*m.b4*
                       m.b6*m.b11 - 256*m.b4*m.b6*m.b12 - 256*m.b4*m.b6*m.b13 - 224*m.b4*m.b6*m.b14 - 192*m.b4*m.b6*
                       m.b15 - 128*m.b4*m.b6*m.b16 - 64*m.b4*m.b6*m.b17 - 32*m.b4*m.b6*m.b18 - 352*m.b4*m.b7*m.b8 - 320*
                       m.b4*m.b7*m.b9 - 160*m.b4*m.b7*m.b10 - 256*m.b4*m.b7*m.b11 - 256*m.b4*m.b7*m.b12 - 224*m.b4*m.b7*
                       m.b13 - 192*m.b4*m.b7*m.b14 - 160*m.b4*m.b7*m.b15 - 96*m.b4*m.b7*m.b16 - 64*m.b4*m.b7*m.b17 - 32*
                       m.b4*m.b7*m.b18 - 352*m.b4*m.b8*m.b9 - 320*m.b4*m.b8*m.b10 - 288*m.b4*m.b8*m.b11 - 96*m.b4*m.b8*
                       m.b12 - 192*m.b4*m.b8*m.b13 - 160*m.b4*m.b8*m.b14 - 128*m.b4*m.b8*m.b15 - 96*m.b4*m.b8*m.b16 - 64
                       *m.b4*m.b8*m.b17 - 32*m.b4*m.b8*m.b18 - 352*m.b4*m.b9*m.b10 - 288*m.b4*m.b9*m.b11 - 224*m.b4*m.b9
                       *m.b12 - 160*m.b4*m.b9*m.b13 - 128*m.b4*m.b9*m.b15 - 96*m.b4*m.b9*m.b16 - 64*m.b4*m.b9*m.b17 - 32
                       *m.b4*m.b9*m.b18 - 288*m.b4*m.b10*m.b11 - 224*m.b4*m.b10*m.b12 - 160*m.b4*m.b10*m.b13 - 128*m.b4*
                       m.b10*m.b14 - 128*m.b4*m.b10*m.b15 - 64*m.b4*m.b10*m.b17 - 32*m.b4*m.b10*m.b18 - 224*m.b4*m.b11*
                       m.b12 - 192*m.b4*m.b11*m.b13 - 160*m.b4*m.b11*m.b14 - 128*m.b4*m.b11*m.b15 - 96*m.b4*m.b11*m.b16
                        - 64*m.b4*m.b11*m.b17 - 224*m.b4*m.b12*m.b13 - 192*m.b4*m.b12*m.b14 - 160*m.b4*m.b12*m.b15 - 96*
                       m.b4*m.b12*m.b16 - 64*m.b4*m.b12*m.b17 - 32*m.b4*m.b12*m.b18 - 224*m.b4*m.b13*m.b14 - 192*m.b4*
                       m.b13*m.b15 - 96*m.b4*m.b13*m.b16 - 64*m.b4*m.b13*m.b17 - 32*m.b4*m.b13*m.b18 - 224*m.b4*m.b14*
                       m.b15 - 128*m.b4*m.b14*m.b16 - 64*m.b4*m.b14*m.b17 - 32*m.b4*m.b14*m.b18 - 160*m.b4*m.b15*m.b16
                        - 64*m.b4*m.b15*m.b17 - 32*m.b4*m.b15*m.b18 - 96*m.b4*m.b16*m.b17 - 32*m.b4*m.b16*m.b18 - 32*
                       m.b4*m.b17*m.b18 - 288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*
                       m.b10 - 320*m.b5*m.b6*m.b11 - 320*m.b5*m.b6*m.b12 - 320*m.b5*m.b6*m.b13 - 320*m.b5*m.b6*m.b14 - 
                       288*m.b5*m.b6*m.b15 - 224*m.b5*m.b6*m.b16 - 160*m.b5*m.b6*m.b17 - 96*m.b5*m.b6*m.b18 - 32*m.b5*
                       m.b6*m.b19 - 448*m.b5*m.b7*m.b8 - 256*m.b5*m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*m.b5*m.b7*m.b11
                        - 320*m.b5*m.b7*m.b12 - 320*m.b5*m.b7*m.b13 - 288*m.b5*m.b7*m.b14 - 256*m.b5*m.b7*m.b15 - 192*
                       m.b5*m.b7*m.b16 - 128*m.b5*m.b7*m.b17 - 64*m.b5*m.b7*m.b18 - 32*m.b5*m.b7*m.b19 - 448*m.b5*m.b8*
                       m.b9 - 416*m.b5*m.b8*m.b10 - 224*m.b5*m.b8*m.b11 - 352*m.b5*m.b8*m.b12 - 288*m.b5*m.b8*m.b13 - 
                       256*m.b5*m.b8*m.b14 - 224*m.b5*m.b8*m.b15 - 160*m.b5*m.b8*m.b16 - 96*m.b5*m.b8*m.b17 - 64*m.b5*
                       m.b8*m.b18 - 32*m.b5*m.b8*m.b19 - 448*m.b5*m.b9*m.b10 - 416*m.b5*m.b9*m.b11 - 352*m.b5*m.b9*m.b12
                        - 128*m.b5*m.b9*m.b13 - 224*m.b5*m.b9*m.b14 - 192*m.b5*m.b9*m.b15 - 128*m.b5*m.b9*m.b16 - 96*
                       m.b5*m.b9*m.b17 - 64*m.b5*m.b9*m.b18 - 32*m.b5*m.b9*m.b19 - 416*m.b5*m.b10*m.b11 - 352*m.b5*m.b10
                       *m.b12 - 288*m.b5*m.b10*m.b13 - 224*m.b5*m.b10*m.b14 - 128*m.b5*m.b10*m.b16 - 96*m.b5*m.b10*m.b17
                        - 64*m.b5*m.b10*m.b18 - 32*m.b5*m.b10*m.b19 - 352*m.b5*m.b11*m.b12 - 288*m.b5*m.b11*m.b13 - 224*
                       m.b5*m.b11*m.b14 - 192*m.b5*m.b11*m.b15 - 128*m.b5*m.b11*m.b16 - 64*m.b5*m.b11*m.b18 - 32*m.b5*
                       m.b11*m.b19 - 288*m.b5*m.b12*m.b13 - 256*m.b5*m.b12*m.b14 - 224*m.b5*m.b12*m.b15 - 128*m.b5*m.b12
                       *m.b16 - 96*m.b5*m.b12*m.b17 - 64*m.b5*m.b12*m.b18 - 288*m.b5*m.b13*m.b14 - 256*m.b5*m.b13*m.b15
                        - 160*m.b5*m.b13*m.b16 - 96*m.b5*m.b13*m.b17 - 64*m.b5*m.b13*m.b18 - 32*m.b5*m.b13*m.b19 - 288*
                       m.b5*m.b14*m.b15 - 192*m.b5*m.b14*m.b16 - 96*m.b5*m.b14*m.b17 - 64*m.b5*m.b14*m.b18 - 32*m.b5*
                       m.b14*m.b19 - 224*m.b5*m.b15*m.b16 - 128*m.b5*m.b15*m.b17 - 64*m.b5*m.b15*m.b18 - 32*m.b5*m.b15*
                       m.b19 - 160*m.b5*m.b16*m.b17 - 64*m.b5*m.b16*m.b18 - 32*m.b5*m.b16*m.b19 - 96*m.b5*m.b17*m.b18 - 
                       32*m.b5*m.b17*m.b19 - 32*m.b5*m.b18*m.b19 - 352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*
                       m.b7*m.b10 - 448*m.b6*m.b7*m.b11 - 416*m.b6*m.b7*m.b12 - 384*m.b6*m.b7*m.b13 - 384*m.b6*m.b7*
                       m.b14 - 352*m.b6*m.b7*m.b15 - 288*m.b6*m.b7*m.b16 - 224*m.b6*m.b7*m.b17 - 160*m.b6*m.b7*m.b18 - 
                       96*m.b6*m.b7*m.b19 - 32*m.b6*m.b7*m.b20 - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10 - 480*m.b6*
                       m.b8*m.b11 - 448*m.b6*m.b8*m.b12 - 416*m.b6*m.b8*m.b13 - 352*m.b6*m.b8*m.b14 - 320*m.b6*m.b8*
                       m.b15 - 256*m.b6*m.b8*m.b16 - 192*m.b6*m.b8*m.b17 - 128*m.b6*m.b8*m.b18 - 64*m.b6*m.b8*m.b19 - 32
                       *m.b6*m.b8*m.b20 - 544*m.b6*m.b9*m.b10 - 512*m.b6*m.b9*m.b11 - 288*m.b6*m.b9*m.b12 - 416*m.b6*
                       m.b9*m.b13 - 352*m.b6*m.b9*m.b14 - 288*m.b6*m.b9*m.b15 - 224*m.b6*m.b9*m.b16 - 160*m.b6*m.b9*
                       m.b17 - 96*m.b6*m.b9*m.b18 - 64*m.b6*m.b9*m.b19 - 32*m.b6*m.b9*m.b20 - 544*m.b6*m.b10*m.b11 - 480
                       *m.b6*m.b10*m.b12 - 416*m.b6*m.b10*m.b13 - 160*m.b6*m.b10*m.b14 - 288*m.b6*m.b10*m.b15 - 192*m.b6
                       *m.b10*m.b16 - 128*m.b6*m.b10*m.b17 - 96*m.b6*m.b10*m.b18 - 64*m.b6*m.b10*m.b19 - 32*m.b6*m.b10*
                       m.b20 - 480*m.b6*m.b11*m.b12 - 416*m.b6*m.b11*m.b13 - 352*m.b6*m.b11*m.b14 - 288*m.b6*m.b11*m.b15
                        - 128*m.b6*m.b11*m.b17 - 96*m.b6*m.b11*m.b18 - 64*m.b6*m.b11*m.b19 - 32*m.b6*m.b11*m.b20 - 416*
                       m.b6*m.b12*m.b13 - 352*m.b6*m.b12*m.b14 - 288*m.b6*m.b12*m.b15 - 192*m.b6*m.b12*m.b16 - 128*m.b6*
                       m.b12*m.b17 - 64*m.b6*m.b12*m.b19 - 32*m.b6*m.b12*m.b20 - 352*m.b6*m.b13*m.b14 - 320*m.b6*m.b13*
                       m.b15 - 224*m.b6*m.b13*m.b16 - 128*m.b6*m.b13*m.b17 - 96*m.b6*m.b13*m.b18 - 64*m.b6*m.b13*m.b19
                        - 352*m.b6*m.b14*m.b15 - 256*m.b6*m.b14*m.b16 - 160*m.b6*m.b14*m.b17 - 96*m.b6*m.b14*m.b18 - 64*
                       m.b6*m.b14*m.b19 - 32*m.b6*m.b14*m.b20 - 288*m.b6*m.b15*m.b16 - 192*m.b6*m.b15*m.b17 - 96*m.b6*
                       m.b15*m.b18 - 64*m.b6*m.b15*m.b19 - 32*m.b6*m.b15*m.b20 - 224*m.b6*m.b16*m.b17 - 128*m.b6*m.b16*
                       m.b18 - 64*m.b6*m.b16*m.b19 - 32*m.b6*m.b16*m.b20 - 160*m.b6*m.b17*m.b18 - 64*m.b6*m.b17*m.b19 - 
                       32*m.b6*m.b17*m.b20 - 96*m.b6*m.b18*m.b19 - 32*m.b6*m.b18*m.b20 - 32*m.b6*m.b19*m.b20 - 416*m.b7*
                       m.b8*m.b9 - 608*m.b7*m.b8*m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*m.b8*m.b12 - 512*m.b7*m.b8*m.b13
                        - 480*m.b7*m.b8*m.b14 - 416*m.b7*m.b8*m.b15 - 352*m.b7*m.b8*m.b16 - 288*m.b7*m.b8*m.b17 - 224*
                       m.b7*m.b8*m.b18 - 160*m.b7*m.b8*m.b19 - 96*m.b7*m.b8*m.b20 - 32*m.b7*m.b8*m.b21 - 640*m.b7*m.b9*
                       m.b10 - 384*m.b7*m.b9*m.b11 - 576*m.b7*m.b9*m.b12 - 544*m.b7*m.b9*m.b13 - 480*m.b7*m.b9*m.b14 - 
                       416*m.b7*m.b9*m.b15 - 320*m.b7*m.b9*m.b16 - 256*m.b7*m.b9*m.b17 - 192*m.b7*m.b9*m.b18 - 128*m.b7*
                       m.b9*m.b19 - 64*m.b7*m.b9*m.b20 - 32*m.b7*m.b9*m.b21 - 640*m.b7*m.b10*m.b11 - 608*m.b7*m.b10*
                       m.b12 - 320*m.b7*m.b10*m.b13 - 480*m.b7*m.b10*m.b14 - 416*m.b7*m.b10*m.b15 - 288*m.b7*m.b10*m.b16
                        - 224*m.b7*m.b10*m.b17 - 160*m.b7*m.b10*m.b18 - 96*m.b7*m.b10*m.b19 - 64*m.b7*m.b10*m.b20 - 32*
                       m.b7*m.b10*m.b21 - 608*m.b7*m.b11*m.b12 - 544*m.b7*m.b11*m.b13 - 480*m.b7*m.b11*m.b14 - 192*m.b7*
                       m.b11*m.b15 - 288*m.b7*m.b11*m.b16 - 192*m.b7*m.b11*m.b17 - 128*m.b7*m.b11*m.b18 - 96*m.b7*m.b11*
                       m.b19 - 64*m.b7*m.b11*m.b20 - 32*m.b7*m.b11*m.b21 - 544*m.b7*m.b12*m.b13 - 480*m.b7*m.b12*m.b14
                        - 416*m.b7*m.b12*m.b15 - 288*m.b7*m.b12*m.b16 - 128*m.b7*m.b12*m.b18 - 96*m.b7*m.b12*m.b19 - 64*
                       m.b7*m.b12*m.b20 - 32*m.b7*m.b12*m.b21 - 480*m.b7*m.b13*m.b14 - 416*m.b7*m.b13*m.b15 - 288*m.b7*
                       m.b13*m.b16 - 192*m.b7*m.b13*m.b17 - 128*m.b7*m.b13*m.b18 - 64*m.b7*m.b13*m.b20 - 32*m.b7*m.b13*
                       m.b21 - 416*m.b7*m.b14*m.b15 - 320*m.b7*m.b14*m.b16 - 224*m.b7*m.b14*m.b17 - 128*m.b7*m.b14*m.b18
                        - 96*m.b7*m.b14*m.b19 - 64*m.b7*m.b14*m.b20 - 352*m.b7*m.b15*m.b16 - 256*m.b7*m.b15*m.b17 - 160*
                       m.b7*m.b15*m.b18 - 96*m.b7*m.b15*m.b19 - 64*m.b7*m.b15*m.b20 - 32*m.b7*m.b15*m.b21 - 288*m.b7*
                       m.b16*m.b17 - 192*m.b7*m.b16*m.b18 - 96*m.b7*m.b16*m.b19 - 64*m.b7*m.b16*m.b20 - 32*m.b7*m.b16*
                       m.b21 - 224*m.b7*m.b17*m.b18 - 128*m.b7*m.b17*m.b19 - 64*m.b7*m.b17*m.b20 - 32*m.b7*m.b17*m.b21
                        - 160*m.b7*m.b18*m.b19 - 64*m.b7*m.b18*m.b20 - 32*m.b7*m.b18*m.b21 - 96*m.b7*m.b19*m.b20 - 32*
                       m.b7*m.b19*m.b21 - 32*m.b7*m.b20*m.b21 - 480*m.b8*m.b9*m.b10 - 704*m.b8*m.b9*m.b11 - 672*m.b8*
                       m.b9*m.b12 - 640*m.b8*m.b9*m.b13 - 608*m.b8*m.b9*m.b14 - 544*m.b8*m.b9*m.b15 - 416*m.b8*m.b9*
                       m.b16 - 352*m.b8*m.b9*m.b17 - 288*m.b8*m.b9*m.b18 - 224*m.b8*m.b9*m.b19 - 160*m.b8*m.b9*m.b20 - 
                       96*m.b8*m.b9*m.b21 - 32*m.b8*m.b9*m.b22 - 736*m.b8*m.b10*m.b11 - 448*m.b8*m.b10*m.b12 - 672*m.b8*
                       m.b10*m.b13 - 608*m.b8*m.b10*m.b14 - 544*m.b8*m.b10*m.b15 - 416*m.b8*m.b10*m.b16 - 320*m.b8*m.b10
                       *m.b17 - 256*m.b8*m.b10*m.b18 - 192*m.b8*m.b10*m.b19 - 128*m.b8*m.b10*m.b20 - 64*m.b8*m.b10*m.b21
                        - 32*m.b8*m.b10*m.b22 - 736*m.b8*m.b11*m.b12 - 672*m.b8*m.b11*m.b13 - 352*m.b8*m.b11*m.b14 - 544
                       *m.b8*m.b11*m.b15 - 416*m.b8*m.b11*m.b16 - 288*m.b8*m.b11*m.b17 - 224*m.b8*m.b11*m.b18 - 160*m.b8
                       *m.b11*m.b19 - 96*m.b8*m.b11*m.b20 - 64*m.b8*m.b11*m.b21 - 32*m.b8*m.b11*m.b22 - 672*m.b8*m.b12*
                       m.b13 - 608*m.b8*m.b12*m.b14 - 544*m.b8*m.b12*m.b15 - 192*m.b8*m.b12*m.b16 - 288*m.b8*m.b12*m.b17
                        - 192*m.b8*m.b12*m.b18 - 128*m.b8*m.b12*m.b19 - 96*m.b8*m.b12*m.b20 - 64*m.b8*m.b12*m.b21 - 32*
                       m.b8*m.b12*m.b22 - 608*m.b8*m.b13*m.b14 - 544*m.b8*m.b13*m.b15 - 416*m.b8*m.b13*m.b16 - 288*m.b8*
                       m.b13*m.b17 - 128*m.b8*m.b13*m.b19 - 96*m.b8*m.b13*m.b20 - 64*m.b8*m.b13*m.b21 - 32*m.b8*m.b13*
                       m.b22 - 544*m.b8*m.b14*m.b15 - 416*m.b8*m.b14*m.b16 - 288*m.b8*m.b14*m.b17 - 192*m.b8*m.b14*m.b18
                        - 128*m.b8*m.b14*m.b19 - 64*m.b8*m.b14*m.b21 - 32*m.b8*m.b14*m.b22 - 416*m.b8*m.b15*m.b16 - 320*
                       m.b8*m.b15*m.b17 - 224*m.b8*m.b15*m.b18 - 128*m.b8*m.b15*m.b19 - 96*m.b8*m.b15*m.b20 - 64*m.b8*
                       m.b15*m.b21 - 352*m.b8*m.b16*m.b17 - 256*m.b8*m.b16*m.b18 - 160*m.b8*m.b16*m.b19 - 96*m.b8*m.b16*
                       m.b20 - 64*m.b8*m.b16*m.b21 - 32*m.b8*m.b16*m.b22 - 288*m.b8*m.b17*m.b18 - 192*m.b8*m.b17*m.b19
                        - 96*m.b8*m.b17*m.b20 - 64*m.b8*m.b17*m.b21 - 32*m.b8*m.b17*m.b22 - 224*m.b8*m.b18*m.b19 - 128*
                       m.b8*m.b18*m.b20 - 64*m.b8*m.b18*m.b21 - 32*m.b8*m.b18*m.b22 - 160*m.b8*m.b19*m.b20 - 64*m.b8*
                       m.b19*m.b21 - 32*m.b8*m.b19*m.b22 - 96*m.b8*m.b20*m.b21 - 32*m.b8*m.b20*m.b22 - 32*m.b8*m.b21*
                       m.b22 - 544*m.b9*m.b10*m.b11 - 800*m.b9*m.b10*m.b12 - 768*m.b9*m.b10*m.b13 - 736*m.b9*m.b10*m.b14
                        - 672*m.b9*m.b10*m.b15 - 544*m.b9*m.b10*m.b16 - 416*m.b9*m.b10*m.b17 - 352*m.b9*m.b10*m.b18 - 
                       288*m.b9*m.b10*m.b19 - 224*m.b9*m.b10*m.b20 - 160*m.b9*m.b10*m.b21 - 96*m.b9*m.b10*m.b22 - 32*
                       m.b9*m.b10*m.b23 - 832*m.b9*m.b11*m.b12 - 512*m.b9*m.b11*m.b13 - 736*m.b9*m.b11*m.b14 - 672*m.b9*
                       m.b11*m.b15 - 544*m.b9*m.b11*m.b16 - 416*m.b9*m.b11*m.b17 - 320*m.b9*m.b11*m.b18 - 256*m.b9*m.b11
                       *m.b19 - 192*m.b9*m.b11*m.b20 - 128*m.b9*m.b11*m.b21 - 64*m.b9*m.b11*m.b22 - 32*m.b9*m.b11*m.b23
                        - 800*m.b9*m.b12*m.b13 - 736*m.b9*m.b12*m.b14 - 384*m.b9*m.b12*m.b15 - 544*m.b9*m.b12*m.b16 - 
                       416*m.b9*m.b12*m.b17 - 288*m.b9*m.b12*m.b18 - 224*m.b9*m.b12*m.b19 - 160*m.b9*m.b12*m.b20 - 96*
                       m.b9*m.b12*m.b21 - 64*m.b9*m.b12*m.b22 - 32*m.b9*m.b12*m.b23 - 736*m.b9*m.b13*m.b14 - 672*m.b9*
                       m.b13*m.b15 - 544*m.b9*m.b13*m.b16 - 192*m.b9*m.b13*m.b17 - 288*m.b9*m.b13*m.b18 - 192*m.b9*m.b13
                       *m.b19 - 128*m.b9*m.b13*m.b20 - 96*m.b9*m.b13*m.b21 - 64*m.b9*m.b13*m.b22 - 32*m.b9*m.b13*m.b23
                        - 672*m.b9*m.b14*m.b15 - 544*m.b9*m.b14*m.b16 - 416*m.b9*m.b14*m.b17 - 288*m.b9*m.b14*m.b18 - 
                       128*m.b9*m.b14*m.b20 - 96*m.b9*m.b14*m.b21 - 64*m.b9*m.b14*m.b22 - 32*m.b9*m.b14*m.b23 - 544*m.b9
                       *m.b15*m.b16 - 416*m.b9*m.b15*m.b17 - 288*m.b9*m.b15*m.b18 - 192*m.b9*m.b15*m.b19 - 128*m.b9*
                       m.b15*m.b20 - 64*m.b9*m.b15*m.b22 - 32*m.b9*m.b15*m.b23 - 416*m.b9*m.b16*m.b17 - 320*m.b9*m.b16*
                       m.b18 - 224*m.b9*m.b16*m.b19 - 128*m.b9*m.b16*m.b20 - 96*m.b9*m.b16*m.b21 - 64*m.b9*m.b16*m.b22
                        - 352*m.b9*m.b17*m.b18 - 256*m.b9*m.b17*m.b19 - 160*m.b9*m.b17*m.b20 - 96*m.b9*m.b17*m.b21 - 64*
                       m.b9*m.b17*m.b22 - 32*m.b9*m.b17*m.b23 - 288*m.b9*m.b18*m.b19 - 192*m.b9*m.b18*m.b20 - 96*m.b9*
                       m.b18*m.b21 - 64*m.b9*m.b18*m.b22 - 32*m.b9*m.b18*m.b23 - 224*m.b9*m.b19*m.b20 - 128*m.b9*m.b19*
                       m.b21 - 64*m.b9*m.b19*m.b22 - 32*m.b9*m.b19*m.b23 - 160*m.b9*m.b20*m.b21 - 64*m.b9*m.b20*m.b22 - 
                       32*m.b9*m.b20*m.b23 - 96*m.b9*m.b21*m.b22 - 32*m.b9*m.b21*m.b23 - 32*m.b9*m.b22*m.b23 - 608*m.b10
                       *m.b11*m.b12 - 896*m.b10*m.b11*m.b13 - 864*m.b10*m.b11*m.b14 - 800*m.b10*m.b11*m.b15 - 672*m.b10*
                       m.b11*m.b16 - 544*m.b10*m.b11*m.b17 - 416*m.b10*m.b11*m.b18 - 352*m.b10*m.b11*m.b19 - 288*m.b10*
                       m.b11*m.b20 - 224*m.b10*m.b11*m.b21 - 160*m.b10*m.b11*m.b22 - 96*m.b10*m.b11*m.b23 - 32*m.b10*
                       m.b11*m.b24 - 928*m.b10*m.b12*m.b13 - 544*m.b10*m.b12*m.b14 - 800*m.b10*m.b12*m.b15 - 672*m.b10*
                       m.b12*m.b16 - 544*m.b10*m.b12*m.b17 - 416*m.b10*m.b12*m.b18 - 320*m.b10*m.b12*m.b19 - 256*m.b10*
                       m.b12*m.b20 - 192*m.b10*m.b12*m.b21 - 128*m.b10*m.b12*m.b22 - 64*m.b10*m.b12*m.b23 - 32*m.b10*
                       m.b12*m.b24 - 864*m.b10*m.b13*m.b14 - 800*m.b10*m.b13*m.b15 - 384*m.b10*m.b13*m.b16 - 544*m.b10*
                       m.b13*m.b17 - 416*m.b10*m.b13*m.b18 - 288*m.b10*m.b13*m.b19 - 224*m.b10*m.b13*m.b20 - 160*m.b10*
                       m.b13*m.b21 - 96*m.b10*m.b13*m.b22 - 64*m.b10*m.b13*m.b23 - 32*m.b10*m.b13*m.b24 - 800*m.b10*
                       m.b14*m.b15 - 672*m.b10*m.b14*m.b16 - 544*m.b10*m.b14*m.b17 - 192*m.b10*m.b14*m.b18 - 288*m.b10*
                       m.b14*m.b19 - 192*m.b10*m.b14*m.b20 - 128*m.b10*m.b14*m.b21 - 96*m.b10*m.b14*m.b22 - 64*m.b10*
                       m.b14*m.b23 - 32*m.b10*m.b14*m.b24 - 672*m.b10*m.b15*m.b16 - 544*m.b10*m.b15*m.b17 - 416*m.b10*
                       m.b15*m.b18 - 288*m.b10*m.b15*m.b19 - 128*m.b10*m.b15*m.b21 - 96*m.b10*m.b15*m.b22 - 64*m.b10*
                       m.b15*m.b23 - 32*m.b10*m.b15*m.b24 - 544*m.b10*m.b16*m.b17 - 416*m.b10*m.b16*m.b18 - 288*m.b10*
                       m.b16*m.b19 - 192*m.b10*m.b16*m.b20 - 128*m.b10*m.b16*m.b21 - 64*m.b10*m.b16*m.b23 - 32*m.b10*
                       m.b16*m.b24 - 416*m.b10*m.b17*m.b18 - 320*m.b10*m.b17*m.b19 - 224*m.b10*m.b17*m.b20 - 128*m.b10*
                       m.b17*m.b21 - 96*m.b10*m.b17*m.b22 - 64*m.b10*m.b17*m.b23 - 352*m.b10*m.b18*m.b19 - 256*m.b10*
                       m.b18*m.b20 - 160*m.b10*m.b18*m.b21 - 96*m.b10*m.b18*m.b22 - 64*m.b10*m.b18*m.b23 - 32*m.b10*
                       m.b18*m.b24 - 288*m.b10*m.b19*m.b20 - 192*m.b10*m.b19*m.b21 - 96*m.b10*m.b19*m.b22 - 64*m.b10*
                       m.b19*m.b23 - 32*m.b10*m.b19*m.b24 - 224*m.b10*m.b20*m.b21 - 128*m.b10*m.b20*m.b22 - 64*m.b10*
                       m.b20*m.b23 - 32*m.b10*m.b20*m.b24 - 160*m.b10*m.b21*m.b22 - 64*m.b10*m.b21*m.b23 - 32*m.b10*
                       m.b21*m.b24 - 96*m.b10*m.b22*m.b23 - 32*m.b10*m.b22*m.b24 - 32*m.b10*m.b23*m.b24 - 672*m.b11*
                       m.b12*m.b13 - 992*m.b11*m.b12*m.b14 - 928*m.b11*m.b12*m.b15 - 800*m.b11*m.b12*m.b16 - 672*m.b11*
                       m.b12*m.b17 - 544*m.b11*m.b12*m.b18 - 416*m.b11*m.b12*m.b19 - 352*m.b11*m.b12*m.b20 - 288*m.b11*
                       m.b12*m.b21 - 224*m.b11*m.b12*m.b22 - 160*m.b11*m.b12*m.b23 - 96*m.b11*m.b12*m.b24 - 32*m.b11*
                       m.b12*m.b25 - 992*m.b11*m.b13*m.b14 - 576*m.b11*m.b13*m.b15 - 800*m.b11*m.b13*m.b16 - 672*m.b11*
                       m.b13*m.b17 - 544*m.b11*m.b13*m.b18 - 416*m.b11*m.b13*m.b19 - 320*m.b11*m.b13*m.b20 - 256*m.b11*
                       m.b13*m.b21 - 192*m.b11*m.b13*m.b22 - 128*m.b11*m.b13*m.b23 - 64*m.b11*m.b13*m.b24 - 32*m.b11*
                       m.b13*m.b25 - 928*m.b11*m.b14*m.b15 - 800*m.b11*m.b14*m.b16 - 384*m.b11*m.b14*m.b17 - 544*m.b11*
                       m.b14*m.b18 - 416*m.b11*m.b14*m.b19 - 288*m.b11*m.b14*m.b20 - 224*m.b11*m.b14*m.b21 - 160*m.b11*
                       m.b14*m.b22 - 96*m.b11*m.b14*m.b23 - 64*m.b11*m.b14*m.b24 - 32*m.b11*m.b14*m.b25 - 800*m.b11*
                       m.b15*m.b16 - 672*m.b11*m.b15*m.b17 - 544*m.b11*m.b15*m.b18 - 192*m.b11*m.b15*m.b19 - 288*m.b11*
                       m.b15*m.b20 - 192*m.b11*m.b15*m.b21 - 128*m.b11*m.b15*m.b22 - 96*m.b11*m.b15*m.b23 - 64*m.b11*
                       m.b15*m.b24 - 32*m.b11*m.b15*m.b25 - 672*m.b11*m.b16*m.b17 - 544*m.b11*m.b16*m.b18 - 416*m.b11*
                       m.b16*m.b19 - 288*m.b11*m.b16*m.b20 - 128*m.b11*m.b16*m.b22 - 96*m.b11*m.b16*m.b23 - 64*m.b11*
                       m.b16*m.b24 - 32*m.b11*m.b16*m.b25 - 544*m.b11*m.b17*m.b18 - 416*m.b11*m.b17*m.b19 - 288*m.b11*
                       m.b17*m.b20 - 192*m.b11*m.b17*m.b21 - 128*m.b11*m.b17*m.b22 - 64*m.b11*m.b17*m.b24 - 32*m.b11*
                       m.b17*m.b25 - 416*m.b11*m.b18*m.b19 - 320*m.b11*m.b18*m.b20 - 224*m.b11*m.b18*m.b21 - 128*m.b11*
                       m.b18*m.b22 - 96*m.b11*m.b18*m.b23 - 64*m.b11*m.b18*m.b24 - 352*m.b11*m.b19*m.b20 - 256*m.b11*
                       m.b19*m.b21 - 160*m.b11*m.b19*m.b22 - 96*m.b11*m.b19*m.b23 - 64*m.b11*m.b19*m.b24 - 32*m.b11*
                       m.b19*m.b25 - 288*m.b11*m.b20*m.b21 - 192*m.b11*m.b20*m.b22 - 96*m.b11*m.b20*m.b23 - 64*m.b11*
                       m.b20*m.b24 - 32*m.b11*m.b20*m.b25 - 224*m.b11*m.b21*m.b22 - 128*m.b11*m.b21*m.b23 - 64*m.b11*
                       m.b21*m.b24 - 32*m.b11*m.b21*m.b25 - 160*m.b11*m.b22*m.b23 - 64*m.b11*m.b22*m.b24 - 32*m.b11*
                       m.b22*m.b25 - 96*m.b11*m.b23*m.b24 - 32*m.b11*m.b23*m.b25 - 32*m.b11*m.b24*m.b25 - 736*m.b12*
                       m.b13*m.b14 - 1056*m.b12*m.b13*m.b15 - 928*m.b12*m.b13*m.b16 - 800*m.b12*m.b13*m.b17 - 672*m.b12*
                       m.b13*m.b18 - 544*m.b12*m.b13*m.b19 - 416*m.b12*m.b13*m.b20 - 352*m.b12*m.b13*m.b21 - 288*m.b12*
                       m.b13*m.b22 - 224*m.b12*m.b13*m.b23 - 160*m.b12*m.b13*m.b24 - 96*m.b12*m.b13*m.b25 - 32*m.b12*
                       m.b13*m.b26 - 1056*m.b12*m.b14*m.b15 - 576*m.b12*m.b14*m.b16 - 800*m.b12*m.b14*m.b17 - 672*m.b12*
                       m.b14*m.b18 - 544*m.b12*m.b14*m.b19 - 416*m.b12*m.b14*m.b20 - 320*m.b12*m.b14*m.b21 - 256*m.b12*
                       m.b14*m.b22 - 192*m.b12*m.b14*m.b23 - 128*m.b12*m.b14*m.b24 - 64*m.b12*m.b14*m.b25 - 32*m.b12*
                       m.b14*m.b26 - 928*m.b12*m.b15*m.b16 - 800*m.b12*m.b15*m.b17 - 384*m.b12*m.b15*m.b18 - 544*m.b12*
                       m.b15*m.b19 - 416*m.b12*m.b15*m.b20 - 288*m.b12*m.b15*m.b21 - 224*m.b12*m.b15*m.b22 - 160*m.b12*
                       m.b15*m.b23 - 96*m.b12*m.b15*m.b24 - 64*m.b12*m.b15*m.b25 - 32*m.b12*m.b15*m.b26 - 800*m.b12*
                       m.b16*m.b17 - 672*m.b12*m.b16*m.b18 - 544*m.b12*m.b16*m.b19 - 192*m.b12*m.b16*m.b20 - 288*m.b12*
                       m.b16*m.b21 - 192*m.b12*m.b16*m.b22 - 128*m.b12*m.b16*m.b23 - 96*m.b12*m.b16*m.b24 - 64*m.b12*
                       m.b16*m.b25 - 32*m.b12*m.b16*m.b26 - 672*m.b12*m.b17*m.b18 - 544*m.b12*m.b17*m.b19 - 416*m.b12*
                       m.b17*m.b20 - 288*m.b12*m.b17*m.b21 - 128*m.b12*m.b17*m.b23 - 96*m.b12*m.b17*m.b24 - 64*m.b12*
                       m.b17*m.b25 - 32*m.b12*m.b17*m.b26 - 544*m.b12*m.b18*m.b19 - 416*m.b12*m.b18*m.b20 - 288*m.b12*
                       m.b18*m.b21 - 192*m.b12*m.b18*m.b22 - 128*m.b12*m.b18*m.b23 - 64*m.b12*m.b18*m.b25 - 32*m.b12*
                       m.b18*m.b26 - 416*m.b12*m.b19*m.b20 - 320*m.b12*m.b19*m.b21 - 224*m.b12*m.b19*m.b22 - 128*m.b12*
                       m.b19*m.b23 - 96*m.b12*m.b19*m.b24 - 64*m.b12*m.b19*m.b25 - 352*m.b12*m.b20*m.b21 - 256*m.b12*
                       m.b20*m.b22 - 160*m.b12*m.b20*m.b23 - 96*m.b12*m.b20*m.b24 - 64*m.b12*m.b20*m.b25 - 32*m.b12*
                       m.b20*m.b26 - 288*m.b12*m.b21*m.b22 - 192*m.b12*m.b21*m.b23 - 96*m.b12*m.b21*m.b24 - 64*m.b12*
                       m.b21*m.b25 - 32*m.b12*m.b21*m.b26 - 224*m.b12*m.b22*m.b23 - 128*m.b12*m.b22*m.b24 - 64*m.b12*
                       m.b22*m.b25 - 32*m.b12*m.b22*m.b26 - 160*m.b12*m.b23*m.b24 - 64*m.b12*m.b23*m.b25 - 32*m.b12*
                       m.b23*m.b26 - 96*m.b12*m.b24*m.b25 - 32*m.b12*m.b24*m.b26 - 32*m.b12*m.b25*m.b26 - 768*m.b13*
                       m.b14*m.b15 - 1056*m.b13*m.b14*m.b16 - 928*m.b13*m.b14*m.b17 - 800*m.b13*m.b14*m.b18 - 672*m.b13*
                       m.b14*m.b19 - 544*m.b13*m.b14*m.b20 - 416*m.b13*m.b14*m.b21 - 352*m.b13*m.b14*m.b22 - 288*m.b13*
                       m.b14*m.b23 - 224*m.b13*m.b14*m.b24 - 160*m.b13*m.b14*m.b25 - 96*m.b13*m.b14*m.b26 - 32*m.b13*
                       m.b14*m.b27 - 1056*m.b13*m.b15*m.b16 - 576*m.b13*m.b15*m.b17 - 800*m.b13*m.b15*m.b18 - 672*m.b13*
                       m.b15*m.b19 - 544*m.b13*m.b15*m.b20 - 416*m.b13*m.b15*m.b21 - 320*m.b13*m.b15*m.b22 - 256*m.b13*
                       m.b15*m.b23 - 192*m.b13*m.b15*m.b24 - 128*m.b13*m.b15*m.b25 - 64*m.b13*m.b15*m.b26 - 32*m.b13*
                       m.b15*m.b27 - 928*m.b13*m.b16*m.b17 - 800*m.b13*m.b16*m.b18 - 384*m.b13*m.b16*m.b19 - 544*m.b13*
                       m.b16*m.b20 - 416*m.b13*m.b16*m.b21 - 288*m.b13*m.b16*m.b22 - 224*m.b13*m.b16*m.b23 - 160*m.b13*
                       m.b16*m.b24 - 96*m.b13*m.b16*m.b25 - 64*m.b13*m.b16*m.b26 - 32*m.b13*m.b16*m.b27 - 800*m.b13*
                       m.b17*m.b18 - 672*m.b13*m.b17*m.b19 - 544*m.b13*m.b17*m.b20 - 192*m.b13*m.b17*m.b21 - 288*m.b13*
                       m.b17*m.b22 - 192*m.b13*m.b17*m.b23 - 128*m.b13*m.b17*m.b24 - 96*m.b13*m.b17*m.b25 - 64*m.b13*
                       m.b17*m.b26 - 32*m.b13*m.b17*m.b27 - 672*m.b13*m.b18*m.b19 - 544*m.b13*m.b18*m.b20 - 416*m.b13*
                       m.b18*m.b21 - 288*m.b13*m.b18*m.b22 - 128*m.b13*m.b18*m.b24 - 96*m.b13*m.b18*m.b25 - 64*m.b13*
                       m.b18*m.b26 - 32*m.b13*m.b18*m.b27 - 544*m.b13*m.b19*m.b20 - 416*m.b13*m.b19*m.b21 - 288*m.b13*
                       m.b19*m.b22 - 192*m.b13*m.b19*m.b23 - 128*m.b13*m.b19*m.b24 - 64*m.b13*m.b19*m.b26 - 32*m.b13*
                       m.b19*m.b27 - 416*m.b13*m.b20*m.b21 - 320*m.b13*m.b20*m.b22 - 224*m.b13*m.b20*m.b23 - 128*m.b13*
                       m.b20*m.b24 - 96*m.b13*m.b20*m.b25 - 64*m.b13*m.b20*m.b26 - 352*m.b13*m.b21*m.b22 - 256*m.b13*
                       m.b21*m.b23 - 160*m.b13*m.b21*m.b24 - 96*m.b13*m.b21*m.b25 - 64*m.b13*m.b21*m.b26 - 32*m.b13*
                       m.b21*m.b27 - 288*m.b13*m.b22*m.b23 - 192*m.b13*m.b22*m.b24 - 96*m.b13*m.b22*m.b25 - 64*m.b13*
                       m.b22*m.b26 - 32*m.b13*m.b22*m.b27 - 224*m.b13*m.b23*m.b24 - 128*m.b13*m.b23*m.b25 - 64*m.b13*
                       m.b23*m.b26 - 32*m.b13*m.b23*m.b27 - 160*m.b13*m.b24*m.b25 - 64*m.b13*m.b24*m.b26 - 32*m.b13*
                       m.b24*m.b27 - 96*m.b13*m.b25*m.b26 - 32*m.b13*m.b25*m.b27 - 32*m.b13*m.b26*m.b27 - 768*m.b14*
                       m.b15*m.b16 - 1056*m.b14*m.b15*m.b17 - 928*m.b14*m.b15*m.b18 - 800*m.b14*m.b15*m.b19 - 672*m.b14*
                       m.b15*m.b20 - 544*m.b14*m.b15*m.b21 - 416*m.b14*m.b15*m.b22 - 352*m.b14*m.b15*m.b23 - 288*m.b14*
                       m.b15*m.b24 - 224*m.b14*m.b15*m.b25 - 160*m.b14*m.b15*m.b26 - 96*m.b14*m.b15*m.b27 - 32*m.b14*
                       m.b15*m.b28 - 1056*m.b14*m.b16*m.b17 - 576*m.b14*m.b16*m.b18 - 800*m.b14*m.b16*m.b19 - 672*m.b14*
                       m.b16*m.b20 - 544*m.b14*m.b16*m.b21 - 416*m.b14*m.b16*m.b22 - 320*m.b14*m.b16*m.b23 - 256*m.b14*
                       m.b16*m.b24 - 192*m.b14*m.b16*m.b25 - 128*m.b14*m.b16*m.b26 - 64*m.b14*m.b16*m.b27 - 32*m.b14*
                       m.b16*m.b28 - 928*m.b14*m.b17*m.b18 - 800*m.b14*m.b17*m.b19 - 384*m.b14*m.b17*m.b20 - 544*m.b14*
                       m.b17*m.b21 - 416*m.b14*m.b17*m.b22 - 288*m.b14*m.b17*m.b23 - 224*m.b14*m.b17*m.b24 - 160*m.b14*
                       m.b17*m.b25 - 96*m.b14*m.b17*m.b26 - 64*m.b14*m.b17*m.b27 - 32*m.b14*m.b17*m.b28 - 800*m.b14*
                       m.b18*m.b19 - 672*m.b14*m.b18*m.b20 - 544*m.b14*m.b18*m.b21 - 192*m.b14*m.b18*m.b22 - 288*m.b14*
                       m.b18*m.b23 - 192*m.b14*m.b18*m.b24 - 128*m.b14*m.b18*m.b25 - 96*m.b14*m.b18*m.b26 - 64*m.b14*
                       m.b18*m.b27 - 32*m.b14*m.b18*m.b28 - 672*m.b14*m.b19*m.b20 - 544*m.b14*m.b19*m.b21 - 416*m.b14*
                       m.b19*m.b22 - 288*m.b14*m.b19*m.b23 - 128*m.b14*m.b19*m.b25 - 96*m.b14*m.b19*m.b26 - 64*m.b14*
                       m.b19*m.b27 - 32*m.b14*m.b19*m.b28 - 544*m.b14*m.b20*m.b21 - 416*m.b14*m.b20*m.b22 - 288*m.b14*
                       m.b20*m.b23 - 192*m.b14*m.b20*m.b24 - 128*m.b14*m.b20*m.b25 - 64*m.b14*m.b20*m.b27 - 32*m.b14*
                       m.b20*m.b28 - 416*m.b14*m.b21*m.b22 - 320*m.b14*m.b21*m.b23 - 224*m.b14*m.b21*m.b24 - 128*m.b14*
                       m.b21*m.b25 - 96*m.b14*m.b21*m.b26 - 64*m.b14*m.b21*m.b27 - 352*m.b14*m.b22*m.b23 - 256*m.b14*
                       m.b22*m.b24 - 160*m.b14*m.b22*m.b25 - 96*m.b14*m.b22*m.b26 - 64*m.b14*m.b22*m.b27 - 32*m.b14*
                       m.b22*m.b28 - 288*m.b14*m.b23*m.b24 - 192*m.b14*m.b23*m.b25 - 96*m.b14*m.b23*m.b26 - 64*m.b14*
                       m.b23*m.b27 - 32*m.b14*m.b23*m.b28 - 224*m.b14*m.b24*m.b25 - 128*m.b14*m.b24*m.b26 - 64*m.b14*
                       m.b24*m.b27 - 32*m.b14*m.b24*m.b28 - 160*m.b14*m.b25*m.b26 - 64*m.b14*m.b25*m.b27 - 32*m.b14*
                       m.b25*m.b28 - 96*m.b14*m.b26*m.b27 - 32*m.b14*m.b26*m.b28 - 32*m.b14*m.b27*m.b28 - 768*m.b15*
                       m.b16*m.b17 - 1056*m.b15*m.b16*m.b18 - 928*m.b15*m.b16*m.b19 - 800*m.b15*m.b16*m.b20 - 672*m.b15*
                       m.b16*m.b21 - 544*m.b15*m.b16*m.b22 - 416*m.b15*m.b16*m.b23 - 352*m.b15*m.b16*m.b24 - 288*m.b15*
                       m.b16*m.b25 - 224*m.b15*m.b16*m.b26 - 160*m.b15*m.b16*m.b27 - 96*m.b15*m.b16*m.b28 - 32*m.b15*
                       m.b16*m.b29 - 1056*m.b15*m.b17*m.b18 - 576*m.b15*m.b17*m.b19 - 800*m.b15*m.b17*m.b20 - 672*m.b15*
                       m.b17*m.b21 - 544*m.b15*m.b17*m.b22 - 416*m.b15*m.b17*m.b23 - 320*m.b15*m.b17*m.b24 - 256*m.b15*
                       m.b17*m.b25 - 192*m.b15*m.b17*m.b26 - 128*m.b15*m.b17*m.b27 - 64*m.b15*m.b17*m.b28 - 32*m.b15*
                       m.b17*m.b29 - 928*m.b15*m.b18*m.b19 - 800*m.b15*m.b18*m.b20 - 384*m.b15*m.b18*m.b21 - 544*m.b15*
                       m.b18*m.b22 - 416*m.b15*m.b18*m.b23 - 288*m.b15*m.b18*m.b24 - 224*m.b15*m.b18*m.b25 - 160*m.b15*
                       m.b18*m.b26 - 96*m.b15*m.b18*m.b27 - 64*m.b15*m.b18*m.b28 - 32*m.b15*m.b18*m.b29 - 800*m.b15*
                       m.b19*m.b20 - 672*m.b15*m.b19*m.b21 - 544*m.b15*m.b19*m.b22 - 192*m.b15*m.b19*m.b23 - 288*m.b15*
                       m.b19*m.b24 - 192*m.b15*m.b19*m.b25 - 128*m.b15*m.b19*m.b26 - 96*m.b15*m.b19*m.b27 - 64*m.b15*
                       m.b19*m.b28 - 32*m.b15*m.b19*m.b29 - 672*m.b15*m.b20*m.b21 - 544*m.b15*m.b20*m.b22 - 416*m.b15*
                       m.b20*m.b23 - 288*m.b15*m.b20*m.b24 - 128*m.b15*m.b20*m.b26 - 96*m.b15*m.b20*m.b27 - 64*m.b15*
                       m.b20*m.b28 - 32*m.b15*m.b20*m.b29 - 544*m.b15*m.b21*m.b22 - 416*m.b15*m.b21*m.b23 - 288*m.b15*
                       m.b21*m.b24 - 192*m.b15*m.b21*m.b25 - 128*m.b15*m.b21*m.b26 - 64*m.b15*m.b21*m.b28 - 32*m.b15*
                       m.b21*m.b29 - 416*m.b15*m.b22*m.b23 - 320*m.b15*m.b22*m.b24 - 224*m.b15*m.b22*m.b25 - 128*m.b15*
                       m.b22*m.b26 - 96*m.b15*m.b22*m.b27 - 64*m.b15*m.b22*m.b28 - 352*m.b15*m.b23*m.b24 - 256*m.b15*
                       m.b23*m.b25 - 160*m.b15*m.b23*m.b26 - 96*m.b15*m.b23*m.b27 - 64*m.b15*m.b23*m.b28 - 32*m.b15*
                       m.b23*m.b29 - 288*m.b15*m.b24*m.b25 - 192*m.b15*m.b24*m.b26 - 96*m.b15*m.b24*m.b27 - 64*m.b15*
                       m.b24*m.b28 - 32*m.b15*m.b24*m.b29 - 224*m.b15*m.b25*m.b26 - 128*m.b15*m.b25*m.b27 - 64*m.b15*
                       m.b25*m.b28 - 32*m.b15*m.b25*m.b29 - 160*m.b15*m.b26*m.b27 - 64*m.b15*m.b26*m.b28 - 32*m.b15*
                       m.b26*m.b29 - 96*m.b15*m.b27*m.b28 - 32*m.b15*m.b27*m.b29 - 32*m.b15*m.b28*m.b29 - 768*m.b16*
                       m.b17*m.b18 - 1056*m.b16*m.b17*m.b19 - 928*m.b16*m.b17*m.b20 - 800*m.b16*m.b17*m.b21 - 672*m.b16*
                       m.b17*m.b22 - 544*m.b16*m.b17*m.b23 - 416*m.b16*m.b17*m.b24 - 352*m.b16*m.b17*m.b25 - 288*m.b16*
                       m.b17*m.b26 - 224*m.b16*m.b17*m.b27 - 160*m.b16*m.b17*m.b28 - 96*m.b16*m.b17*m.b29 - 32*m.b16*
                       m.b17*m.b30 - 1056*m.b16*m.b18*m.b19 - 576*m.b16*m.b18*m.b20 - 800*m.b16*m.b18*m.b21 - 672*m.b16*
                       m.b18*m.b22 - 544*m.b16*m.b18*m.b23 - 416*m.b16*m.b18*m.b24 - 320*m.b16*m.b18*m.b25 - 256*m.b16*
                       m.b18*m.b26 - 192*m.b16*m.b18*m.b27 - 128*m.b16*m.b18*m.b28 - 64*m.b16*m.b18*m.b29 - 32*m.b16*
                       m.b18*m.b30 - 928*m.b16*m.b19*m.b20 - 800*m.b16*m.b19*m.b21 - 384*m.b16*m.b19*m.b22 - 544*m.b16*
                       m.b19*m.b23 - 416*m.b16*m.b19*m.b24 - 288*m.b16*m.b19*m.b25 - 224*m.b16*m.b19*m.b26 - 160*m.b16*
                       m.b19*m.b27 - 96*m.b16*m.b19*m.b28 - 64*m.b16*m.b19*m.b29 - 32*m.b16*m.b19*m.b30 - 800*m.b16*
                       m.b20*m.b21 - 672*m.b16*m.b20*m.b22 - 544*m.b16*m.b20*m.b23 - 192*m.b16*m.b20*m.b24 - 288*m.b16*
                       m.b20*m.b25 - 192*m.b16*m.b20*m.b26 - 128*m.b16*m.b20*m.b27 - 96*m.b16*m.b20*m.b28 - 64*m.b16*
                       m.b20*m.b29 - 32*m.b16*m.b20*m.b30 - 672*m.b16*m.b21*m.b22 - 544*m.b16*m.b21*m.b23 - 416*m.b16*
                       m.b21*m.b24 - 288*m.b16*m.b21*m.b25 - 128*m.b16*m.b21*m.b27 - 96*m.b16*m.b21*m.b28 - 64*m.b16*
                       m.b21*m.b29 - 32*m.b16*m.b21*m.b30 - 544*m.b16*m.b22*m.b23 - 416*m.b16*m.b22*m.b24 - 288*m.b16*
                       m.b22*m.b25 - 192*m.b16*m.b22*m.b26 - 128*m.b16*m.b22*m.b27 - 64*m.b16*m.b22*m.b29 - 32*m.b16*
                       m.b22*m.b30 - 416*m.b16*m.b23*m.b24 - 320*m.b16*m.b23*m.b25 - 224*m.b16*m.b23*m.b26 - 128*m.b16*
                       m.b23*m.b27 - 96*m.b16*m.b23*m.b28 - 64*m.b16*m.b23*m.b29 - 352*m.b16*m.b24*m.b25 - 256*m.b16*
                       m.b24*m.b26 - 160*m.b16*m.b24*m.b27 - 96*m.b16*m.b24*m.b28 - 64*m.b16*m.b24*m.b29 - 32*m.b16*
                       m.b24*m.b30 - 288*m.b16*m.b25*m.b26 - 192*m.b16*m.b25*m.b27 - 96*m.b16*m.b25*m.b28 - 64*m.b16*
                       m.b25*m.b29 - 32*m.b16*m.b25*m.b30 - 224*m.b16*m.b26*m.b27 - 128*m.b16*m.b26*m.b28 - 64*m.b16*
                       m.b26*m.b29 - 32*m.b16*m.b26*m.b30 - 160*m.b16*m.b27*m.b28 - 64*m.b16*m.b27*m.b29 - 32*m.b16*
                       m.b27*m.b30 - 96*m.b16*m.b28*m.b29 - 32*m.b16*m.b28*m.b30 - 32*m.b16*m.b29*m.b30 - 736*m.b17*
                       m.b18*m.b19 - 992*m.b17*m.b18*m.b20 - 864*m.b17*m.b18*m.b21 - 736*m.b17*m.b18*m.b22 - 608*m.b17*
                       m.b18*m.b23 - 480*m.b17*m.b18*m.b24 - 352*m.b17*m.b18*m.b25 - 288*m.b17*m.b18*m.b26 - 224*m.b17*
                       m.b18*m.b27 - 160*m.b17*m.b18*m.b28 - 96*m.b17*m.b18*m.b29 - 32*m.b17*m.b18*m.b30 - 992*m.b17*
                       m.b19*m.b20 - 544*m.b17*m.b19*m.b21 - 736*m.b17*m.b19*m.b22 - 608*m.b17*m.b19*m.b23 - 480*m.b17*
                       m.b19*m.b24 - 352*m.b17*m.b19*m.b25 - 256*m.b17*m.b19*m.b26 - 192*m.b17*m.b19*m.b27 - 128*m.b17*
                       m.b19*m.b28 - 64*m.b17*m.b19*m.b29 - 32*m.b17*m.b19*m.b30 - 864*m.b17*m.b20*m.b21 - 736*m.b17*
                       m.b20*m.b22 - 352*m.b17*m.b20*m.b23 - 480*m.b17*m.b20*m.b24 - 352*m.b17*m.b20*m.b25 - 224*m.b17*
                       m.b20*m.b26 - 160*m.b17*m.b20*m.b27 - 96*m.b17*m.b20*m.b28 - 64*m.b17*m.b20*m.b29 - 32*m.b17*
                       m.b20*m.b30 - 736*m.b17*m.b21*m.b22 - 608*m.b17*m.b21*m.b23 - 480*m.b17*m.b21*m.b24 - 160*m.b17*
                       m.b21*m.b25 - 224*m.b17*m.b21*m.b26 - 128*m.b17*m.b21*m.b27 - 96*m.b17*m.b21*m.b28 - 64*m.b17*
                       m.b21*m.b29 - 32*m.b17*m.b21*m.b30 - 608*m.b17*m.b22*m.b23 - 480*m.b17*m.b22*m.b24 - 352*m.b17*
                       m.b22*m.b25 - 224*m.b17*m.b22*m.b26 - 96*m.b17*m.b22*m.b28 - 64*m.b17*m.b22*m.b29 - 32*m.b17*
                       m.b22*m.b30 - 480*m.b17*m.b23*m.b24 - 352*m.b17*m.b23*m.b25 - 256*m.b17*m.b23*m.b26 - 160*m.b17*
                       m.b23*m.b27 - 96*m.b17*m.b23*m.b28 - 32*m.b17*m.b23*m.b30 - 384*m.b17*m.b24*m.b25 - 288*m.b17*
                       m.b24*m.b26 - 192*m.b17*m.b24*m.b27 - 96*m.b17*m.b24*m.b28 - 64*m.b17*m.b24*m.b29 - 32*m.b17*
                       m.b24*m.b30 - 320*m.b17*m.b25*m.b26 - 224*m.b17*m.b25*m.b27 - 128*m.b17*m.b25*m.b28 - 64*m.b17*
                       m.b25*m.b29 - 32*m.b17*m.b25*m.b30 - 256*m.b17*m.b26*m.b27 - 160*m.b17*m.b26*m.b28 - 64*m.b17*
                       m.b26*m.b29 - 32*m.b17*m.b26*m.b30 - 192*m.b17*m.b27*m.b28 - 96*m.b17*m.b27*m.b29 - 32*m.b17*
                       m.b27*m.b30 - 128*m.b17*m.b28*m.b29 - 32*m.b17*m.b28*m.b30 - 64*m.b17*m.b29*m.b30 - 672*m.b18*
                       m.b19*m.b20 - 928*m.b18*m.b19*m.b21 - 800*m.b18*m.b19*m.b22 - 672*m.b18*m.b19*m.b23 - 544*m.b18*
                       m.b19*m.b24 - 416*m.b18*m.b19*m.b25 - 288*m.b18*m.b19*m.b26 - 224*m.b18*m.b19*m.b27 - 160*m.b18*
                       m.b19*m.b28 - 96*m.b18*m.b19*m.b29 - 32*m.b18*m.b19*m.b30 - 896*m.b18*m.b20*m.b21 - 512*m.b18*
                       m.b20*m.b22 - 672*m.b18*m.b20*m.b23 - 544*m.b18*m.b20*m.b24 - 416*m.b18*m.b20*m.b25 - 288*m.b18*
                       m.b20*m.b26 - 192*m.b18*m.b20*m.b27 - 128*m.b18*m.b20*m.b28 - 64*m.b18*m.b20*m.b29 - 32*m.b18*
                       m.b20*m.b30 - 768*m.b18*m.b21*m.b22 - 672*m.b18*m.b21*m.b23 - 320*m.b18*m.b21*m.b24 - 416*m.b18*
                       m.b21*m.b25 - 288*m.b18*m.b21*m.b26 - 160*m.b18*m.b21*m.b27 - 96*m.b18*m.b21*m.b28 - 64*m.b18*
                       m.b21*m.b29 - 32*m.b18*m.b21*m.b30 - 640*m.b18*m.b22*m.b23 - 544*m.b18*m.b22*m.b24 - 416*m.b18*
                       m.b22*m.b25 - 128*m.b18*m.b22*m.b26 - 160*m.b18*m.b22*m.b27 - 96*m.b18*m.b22*m.b28 - 64*m.b18*
                       m.b22*m.b29 - 32*m.b18*m.b22*m.b30 - 512*m.b18*m.b23*m.b24 - 416*m.b18*m.b23*m.b25 - 288*m.b18*
                       m.b23*m.b26 - 192*m.b18*m.b23*m.b27 - 64*m.b18*m.b23*m.b29 - 32*m.b18*m.b23*m.b30 - 384*m.b18*
                       m.b24*m.b25 - 320*m.b18*m.b24*m.b26 - 224*m.b18*m.b24*m.b27 - 128*m.b18*m.b24*m.b28 - 64*m.b18*
                       m.b24*m.b29 - 320*m.b18*m.b25*m.b26 - 256*m.b18*m.b25*m.b27 - 160*m.b18*m.b25*m.b28 - 64*m.b18*
                       m.b25*m.b29 - 32*m.b18*m.b25*m.b30 - 256*m.b18*m.b26*m.b27 - 192*m.b18*m.b26*m.b28 - 96*m.b18*
                       m.b26*m.b29 - 32*m.b18*m.b26*m.b30 - 192*m.b18*m.b27*m.b28 - 128*m.b18*m.b27*m.b29 - 32*m.b18*
                       m.b27*m.b30 - 128*m.b18*m.b28*m.b29 - 64*m.b18*m.b28*m.b30 - 64*m.b18*m.b29*m.b30 - 608*m.b19*
                       m.b20*m.b21 - 832*m.b19*m.b20*m.b22 - 736*m.b19*m.b20*m.b23 - 608*m.b19*m.b20*m.b24 - 480*m.b19*
                       m.b20*m.b25 - 352*m.b19*m.b20*m.b26 - 224*m.b19*m.b20*m.b27 - 160*m.b19*m.b20*m.b28 - 96*m.b19*
                       m.b20*m.b29 - 32*m.b19*m.b20*m.b30 - 800*m.b19*m.b21*m.b22 - 448*m.b19*m.b21*m.b23 - 608*m.b19*
                       m.b21*m.b24 - 480*m.b19*m.b21*m.b25 - 352*m.b19*m.b21*m.b26 - 224*m.b19*m.b21*m.b27 - 128*m.b19*
                       m.b21*m.b28 - 64*m.b19*m.b21*m.b29 - 32*m.b19*m.b21*m.b30 - 672*m.b19*m.b22*m.b23 - 576*m.b19*
                       m.b22*m.b24 - 288*m.b19*m.b22*m.b25 - 352*m.b19*m.b22*m.b26 - 224*m.b19*m.b22*m.b27 - 96*m.b19*
                       m.b22*m.b28 - 64*m.b19*m.b22*m.b29 - 32*m.b19*m.b22*m.b30 - 544*m.b19*m.b23*m.b24 - 448*m.b19*
                       m.b23*m.b25 - 352*m.b19*m.b23*m.b26 - 96*m.b19*m.b23*m.b27 - 128*m.b19*m.b23*m.b28 - 64*m.b19*
                       m.b23*m.b29 - 32*m.b19*m.b23*m.b30 - 416*m.b19*m.b24*m.b25 - 320*m.b19*m.b24*m.b26 - 256*m.b19*
                       m.b24*m.b27 - 160*m.b19*m.b24*m.b28 - 32*m.b19*m.b24*m.b30 - 320*m.b19*m.b25*m.b26 - 256*m.b19*
                       m.b25*m.b27 - 192*m.b19*m.b25*m.b28 - 96*m.b19*m.b25*m.b29 - 32*m.b19*m.b25*m.b30 - 256*m.b19*
                       m.b26*m.b27 - 192*m.b19*m.b26*m.b28 - 128*m.b19*m.b26*m.b29 - 32*m.b19*m.b26*m.b30 - 192*m.b19*
                       m.b27*m.b28 - 128*m.b19*m.b27*m.b29 - 64*m.b19*m.b27*m.b30 - 128*m.b19*m.b28*m.b29 - 64*m.b19*
                       m.b28*m.b30 - 64*m.b19*m.b29*m.b30 - 544*m.b20*m.b21*m.b22 - 736*m.b20*m.b21*m.b23 - 640*m.b20*
                       m.b21*m.b24 - 544*m.b20*m.b21*m.b25 - 416*m.b20*m.b21*m.b26 - 288*m.b20*m.b21*m.b27 - 160*m.b20*
                       m.b21*m.b28 - 96*m.b20*m.b21*m.b29 - 32*m.b20*m.b21*m.b30 - 704*m.b20*m.b22*m.b23 - 384*m.b20*
                       m.b22*m.b24 - 512*m.b20*m.b22*m.b25 - 416*m.b20*m.b22*m.b26 - 288*m.b20*m.b22*m.b27 - 160*m.b20*
                       m.b22*m.b28 - 64*m.b20*m.b22*m.b29 - 32*m.b20*m.b22*m.b30 - 576*m.b20*m.b23*m.b24 - 480*m.b20*
                       m.b23*m.b25 - 224*m.b20*m.b23*m.b26 - 288*m.b20*m.b23*m.b27 - 160*m.b20*m.b23*m.b28 - 64*m.b20*
                       m.b23*m.b29 - 32*m.b20*m.b23*m.b30 - 448*m.b20*m.b24*m.b25 - 352*m.b20*m.b24*m.b26 - 256*m.b20*
                       m.b24*m.b27 - 96*m.b20*m.b24*m.b28 - 96*m.b20*m.b24*m.b29 - 32*m.b20*m.b24*m.b30 - 320*m.b20*
                       m.b25*m.b26 - 256*m.b20*m.b25*m.b27 - 192*m.b20*m.b25*m.b28 - 128*m.b20*m.b25*m.b29 - 256*m.b20*
                       m.b26*m.b27 - 192*m.b20*m.b26*m.b28 - 128*m.b20*m.b26*m.b29 - 64*m.b20*m.b26*m.b30 - 192*m.b20*
                       m.b27*m.b28 - 128*m.b20*m.b27*m.b29 - 64*m.b20*m.b27*m.b30 - 128*m.b20*m.b28*m.b29 - 64*m.b20*
                       m.b28*m.b30 - 64*m.b20*m.b29*m.b30 - 480*m.b21*m.b22*m.b23 - 640*m.b21*m.b22*m.b24 - 544*m.b21*
                       m.b22*m.b25 - 448*m.b21*m.b22*m.b26 - 352*m.b21*m.b22*m.b27 - 224*m.b21*m.b22*m.b28 - 96*m.b21*
                       m.b22*m.b29 - 32*m.b21*m.b22*m.b30 - 608*m.b21*m.b23*m.b24 - 320*m.b21*m.b23*m.b25 - 416*m.b21*
                       m.b23*m.b26 - 320*m.b21*m.b23*m.b27 - 224*m.b21*m.b23*m.b28 - 96*m.b21*m.b23*m.b29 - 32*m.b21*
                       m.b23*m.b30 - 480*m.b21*m.b24*m.b25 - 384*m.b21*m.b24*m.b26 - 160*m.b21*m.b24*m.b27 - 192*m.b21*
                       m.b24*m.b28 - 128*m.b21*m.b24*m.b29 - 32*m.b21*m.b24*m.b30 - 352*m.b21*m.b25*m.b26 - 256*m.b21*
                       m.b25*m.b27 - 192*m.b21*m.b25*m.b28 - 64*m.b21*m.b25*m.b29 - 64*m.b21*m.b25*m.b30 - 256*m.b21*
                       m.b26*m.b27 - 192*m.b21*m.b26*m.b28 - 128*m.b21*m.b26*m.b29 - 64*m.b21*m.b26*m.b30 - 192*m.b21*
                       m.b27*m.b28 - 128*m.b21*m.b27*m.b29 - 64*m.b21*m.b27*m.b30 - 128*m.b21*m.b28*m.b29 - 64*m.b21*
                       m.b28*m.b30 - 64*m.b21*m.b29*m.b30 - 416*m.b22*m.b23*m.b24 - 544*m.b22*m.b23*m.b25 - 448*m.b22*
                       m.b23*m.b26 - 352*m.b22*m.b23*m.b27 - 256*m.b22*m.b23*m.b28 - 160*m.b22*m.b23*m.b29 - 32*m.b22*
                       m.b23*m.b30 - 512*m.b22*m.b24*m.b25 - 256*m.b22*m.b24*m.b26 - 320*m.b22*m.b24*m.b27 - 224*m.b22*
                       m.b24*m.b28 - 128*m.b22*m.b24*m.b29 - 64*m.b22*m.b24*m.b30 - 384*m.b22*m.b25*m.b26 - 288*m.b22*
                       m.b25*m.b27 - 96*m.b22*m.b25*m.b28 - 128*m.b22*m.b25*m.b29 - 64*m.b22*m.b25*m.b30 - 256*m.b22*
                       m.b26*m.b27 - 192*m.b22*m.b26*m.b28 - 128*m.b22*m.b26*m.b29 - 32*m.b22*m.b26*m.b30 - 192*m.b22*
                       m.b27*m.b28 - 128*m.b22*m.b27*m.b29 - 64*m.b22*m.b27*m.b30 - 128*m.b22*m.b28*m.b29 - 64*m.b22*
                       m.b28*m.b30 - 64*m.b22*m.b29*m.b30 - 352*m.b23*m.b24*m.b25 - 448*m.b23*m.b24*m.b26 - 352*m.b23*
                       m.b24*m.b27 - 256*m.b23*m.b24*m.b28 - 160*m.b23*m.b24*m.b29 - 64*m.b23*m.b24*m.b30 - 416*m.b23*
                       m.b25*m.b26 - 192*m.b23*m.b25*m.b27 - 224*m.b23*m.b25*m.b28 - 128*m.b23*m.b25*m.b29 - 64*m.b23*
                       m.b25*m.b30 - 288*m.b23*m.b26*m.b27 - 192*m.b23*m.b26*m.b28 - 64*m.b23*m.b26*m.b29 - 64*m.b23*
                       m.b26*m.b30 - 192*m.b23*m.b27*m.b28 - 128*m.b23*m.b27*m.b29 - 64*m.b23*m.b27*m.b30 - 128*m.b23*
                       m.b28*m.b29 - 64*m.b23*m.b28*m.b30 - 64*m.b23*m.b29*m.b30 - 288*m.b24*m.b25*m.b26 - 352*m.b24*
                       m.b25*m.b27 - 256*m.b24*m.b25*m.b28 - 160*m.b24*m.b25*m.b29 - 64*m.b24*m.b25*m.b30 - 320*m.b24*
                       m.b26*m.b27 - 128*m.b24*m.b26*m.b28 - 128*m.b24*m.b26*m.b29 - 64*m.b24*m.b26*m.b30 - 192*m.b24*
                       m.b27*m.b28 - 128*m.b24*m.b27*m.b29 - 32*m.b24*m.b27*m.b30 - 128*m.b24*m.b28*m.b29 - 64*m.b24*
                       m.b28*m.b30 - 64*m.b24*m.b29*m.b30 - 224*m.b25*m.b26*m.b27 - 256*m.b25*m.b26*m.b28 - 160*m.b25*
                       m.b26*m.b29 - 64*m.b25*m.b26*m.b30 - 224*m.b25*m.b27*m.b28 - 64*m.b25*m.b27*m.b29 - 64*m.b25*
                       m.b27*m.b30 - 128*m.b25*m.b28*m.b29 - 64*m.b25*m.b28*m.b30 - 64*m.b25*m.b29*m.b30 - 160*m.b26*
                       m.b27*m.b28 - 160*m.b26*m.b27*m.b29 - 64*m.b26*m.b27*m.b30 - 128*m.b26*m.b28*m.b29 - 32*m.b26*
                       m.b28*m.b30 - 64*m.b26*m.b29*m.b30 - 96*m.b27*m.b28*m.b29 - 64*m.b27*m.b28*m.b30 - 64*m.b27*m.b29
                       *m.b30 - 32*m.b28*m.b29*m.b30 + 192*m.b1*m.b2 + 184*m.b1*m.b3 + 176*m.b1*m.b4 + 168*m.b1*m.b5 + 
                       160*m.b1*m.b6 + 152*m.b1*m.b7 + 144*m.b1*m.b8 + 152*m.b1*m.b9 + 144*m.b1*m.b10 + 136*m.b1*m.b11
                        + 128*m.b1*m.b12 + 120*m.b1*m.b13 + 112*m.b1*m.b14 + 104*m.b1*m.b15 + 384*m.b2*m.b3 + 384*m.b2*
                       m.b4 + 368*m.b2*m.b5 + 352*m.b2*m.b6 + 336*m.b2*m.b7 + 320*m.b2*m.b8 + 320*m.b2*m.b9 + 320*m.b2*
                       m.b10 + 304*m.b2*m.b11 + 288*m.b2*m.b12 + 272*m.b2*m.b13 + 256*m.b2*m.b14 + 224*m.b2*m.b15 + 104*
                       m.b2*m.b16 + 592*m.b3*m.b4 + 584*m.b3*m.b5 + 576*m.b3*m.b6 + 552*m.b3*m.b7 + 528*m.b3*m.b8 + 504*
                       m.b3*m.b9 + 512*m.b3*m.b10 + 504*m.b3*m.b11 + 480*m.b3*m.b12 + 456*m.b3*m.b13 + 416*m.b3*m.b14 + 
                       376*m.b3*m.b15 + 224*m.b3*m.b16 + 104*m.b3*m.b17 + 816*m.b4*m.b5 + 800*m.b4*m.b6 + 784*m.b4*m.b7
                        + 768*m.b4*m.b8 + 736*m.b4*m.b9 + 720*m.b4*m.b10 + 720*m.b4*m.b11 + 704*m.b4*m.b12 + 656*m.b4*
                       m.b13 + 608*m.b4*m.b14 + 544*m.b4*m.b15 + 376*m.b4*m.b16 + 224*m.b4*m.b17 + 104*m.b4*m.b18 + 1056
                       *m.b5*m.b6 + 1032*m.b5*m.b7 + 1008*m.b5*m.b8 + 984*m.b5*m.b9 + 960*m.b5*m.b10 + 952*m.b5*m.b11 + 
                       928*m.b5*m.b12 + 888*m.b5*m.b13 + 816*m.b5*m.b14 + 744*m.b5*m.b15 + 544*m.b5*m.b16 + 376*m.b5*
                       m.b17 + 224*m.b5*m.b18 + 104*m.b5*m.b19 + 1312*m.b6*m.b7 + 1280*m.b6*m.b8 + 1248*m.b6*m.b9 + 1216
                       *m.b6*m.b10 + 1184*m.b6*m.b11 + 1168*m.b6*m.b12 + 1120*m.b6*m.b13 + 1056*m.b6*m.b14 + 960*m.b6*
                       m.b15 + 744*m.b6*m.b16 + 544*m.b6*m.b17 + 376*m.b6*m.b18 + 224*m.b6*m.b19 + 104*m.b6*m.b20 + 1584
                       *m.b7*m.b8 + 1544*m.b7*m.b9 + 1488*m.b7*m.b10 + 1432*m.b7*m.b11 + 1392*m.b7*m.b12 + 1352*m.b7*
                       m.b13 + 1296*m.b7*m.b14 + 1208*m.b7*m.b15 + 960*m.b7*m.b16 + 744*m.b7*m.b17 + 544*m.b7*m.b18 + 
                       376*m.b7*m.b19 + 224*m.b7*m.b20 + 104*m.b7*m.b21 + 1856*m.b8*m.b9 + 1792*m.b8*m.b10 + 1712*m.b8*
                       m.b11 + 1648*m.b8*m.b12 + 1584*m.b8*m.b13 + 1520*m.b8*m.b14 + 1440*m.b8*m.b15 + 1208*m.b8*m.b16
                        + 960*m.b8*m.b17 + 744*m.b8*m.b18 + 544*m.b8*m.b19 + 376*m.b8*m.b20 + 224*m.b8*m.b21 + 104*m.b8*
                       m.b22 + 2112*m.b9*m.b10 + 2024*m.b9*m.b11 + 1920*m.b9*m.b12 + 1848*m.b9*m.b13 + 1760*m.b9*m.b14
                        + 1672*m.b9*m.b15 + 1440*m.b9*m.b16 + 1208*m.b9*m.b17 + 960*m.b9*m.b18 + 744*m.b9*m.b19 + 544*
                       m.b9*m.b20 + 376*m.b9*m.b21 + 224*m.b9*m.b22 + 104*m.b9*m.b23 + 2352*m.b10*m.b11 + 2240*m.b10*
                       m.b12 + 2128*m.b10*m.b13 + 2032*m.b10*m.b14 + 1920*m.b10*m.b15 + 1672*m.b10*m.b16 + 1440*m.b10*
                       m.b17 + 1208*m.b10*m.b18 + 960*m.b10*m.b19 + 744*m.b10*m.b20 + 544*m.b10*m.b21 + 376*m.b10*m.b22
                        + 224*m.b10*m.b23 + 104*m.b10*m.b24 + 2576*m.b11*m.b12 + 2440*m.b11*m.b13 + 2320*m.b11*m.b14 + 
                       2200*m.b11*m.b15 + 1920*m.b11*m.b16 + 1672*m.b11*m.b17 + 1440*m.b11*m.b18 + 1208*m.b11*m.b19 + 
                       960*m.b11*m.b20 + 744*m.b11*m.b21 + 544*m.b11*m.b22 + 376*m.b11*m.b23 + 224*m.b11*m.b24 + 104*
                       m.b11*m.b25 + 2784*m.b12*m.b13 + 2640*m.b12*m.b14 + 2496*m.b12*m.b15 + 2200*m.b12*m.b16 + 1920*
                       m.b12*m.b17 + 1672*m.b12*m.b18 + 1440*m.b12*m.b19 + 1208*m.b12*m.b20 + 960*m.b12*m.b21 + 744*
                       m.b12*m.b22 + 544*m.b12*m.b23 + 376*m.b12*m.b24 + 224*m.b12*m.b25 + 104*m.b12*m.b26 + 2976*m.b13*
                       m.b14 + 2824*m.b13*m.b15 + 2496*m.b13*m.b16 + 2200*m.b13*m.b17 + 1920*m.b13*m.b18 + 1672*m.b13*
                       m.b19 + 1440*m.b13*m.b20 + 1208*m.b13*m.b21 + 960*m.b13*m.b22 + 744*m.b13*m.b23 + 544*m.b13*m.b24
                        + 376*m.b13*m.b25 + 224*m.b13*m.b26 + 104*m.b13*m.b27 + 3168*m.b14*m.b15 + 2824*m.b14*m.b16 + 
                       2496*m.b14*m.b17 + 2200*m.b14*m.b18 + 1920*m.b14*m.b19 + 1672*m.b14*m.b20 + 1440*m.b14*m.b21 + 
                       1208*m.b14*m.b22 + 960*m.b14*m.b23 + 744*m.b14*m.b24 + 544*m.b14*m.b25 + 376*m.b14*m.b26 + 224*
                       m.b14*m.b27 + 104*m.b14*m.b28 + 3168*m.b15*m.b16 + 2824*m.b15*m.b17 + 2496*m.b15*m.b18 + 2200*
                       m.b15*m.b19 + 1920*m.b15*m.b20 + 1672*m.b15*m.b21 + 1440*m.b15*m.b22 + 1208*m.b15*m.b23 + 960*
                       m.b15*m.b24 + 744*m.b15*m.b25 + 544*m.b15*m.b26 + 376*m.b15*m.b27 + 224*m.b15*m.b28 + 104*m.b15*
                       m.b29 + 3168*m.b16*m.b17 + 2824*m.b16*m.b18 + 2496*m.b16*m.b19 + 2200*m.b16*m.b20 + 1920*m.b16*
                       m.b21 + 1672*m.b16*m.b22 + 1440*m.b16*m.b23 + 1208*m.b16*m.b24 + 960*m.b16*m.b25 + 744*m.b16*
                       m.b26 + 544*m.b16*m.b27 + 376*m.b16*m.b28 + 224*m.b16*m.b29 + 104*m.b16*m.b30 + 2976*m.b17*m.b18
                        + 2640*m.b17*m.b19 + 2320*m.b17*m.b20 + 2032*m.b17*m.b21 + 1760*m.b17*m.b22 + 1520*m.b17*m.b23
                        + 1296*m.b17*m.b24 + 1056*m.b17*m.b25 + 816*m.b17*m.b26 + 608*m.b17*m.b27 + 416*m.b17*m.b28 + 
                       256*m.b17*m.b29 + 112*m.b17*m.b30 + 2784*m.b18*m.b19 + 2440*m.b18*m.b20 + 2128*m.b18*m.b21 + 1848
                       *m.b18*m.b22 + 1584*m.b18*m.b23 + 1352*m.b18*m.b24 + 1120*m.b18*m.b25 + 888*m.b18*m.b26 + 656*
                       m.b18*m.b27 + 456*m.b18*m.b28 + 272*m.b18*m.b29 + 120*m.b18*m.b30 + 2576*m.b19*m.b20 + 2240*m.b19
                       *m.b21 + 1920*m.b19*m.b22 + 1648*m.b19*m.b23 + 1392*m.b19*m.b24 + 1168*m.b19*m.b25 + 928*m.b19*
                       m.b26 + 704*m.b19*m.b27 + 480*m.b19*m.b28 + 288*m.b19*m.b29 + 128*m.b19*m.b30 + 2352*m.b20*m.b21
                        + 2024*m.b20*m.b22 + 1712*m.b20*m.b23 + 1432*m.b20*m.b24 + 1184*m.b20*m.b25 + 952*m.b20*m.b26 + 
                       720*m.b20*m.b27 + 504*m.b20*m.b28 + 304*m.b20*m.b29 + 136*m.b20*m.b30 + 2112*m.b21*m.b22 + 1792*
                       m.b21*m.b23 + 1488*m.b21*m.b24 + 1216*m.b21*m.b25 + 960*m.b21*m.b26 + 720*m.b21*m.b27 + 512*m.b21
                       *m.b28 + 320*m.b21*m.b29 + 144*m.b21*m.b30 + 1856*m.b22*m.b23 + 1544*m.b22*m.b24 + 1248*m.b22*
                       m.b25 + 984*m.b22*m.b26 + 736*m.b22*m.b27 + 504*m.b22*m.b28 + 320*m.b22*m.b29 + 152*m.b22*m.b30
                        + 1584*m.b23*m.b24 + 1280*m.b23*m.b25 + 1008*m.b23*m.b26 + 768*m.b23*m.b27 + 528*m.b23*m.b28 + 
                       320*m.b23*m.b29 + 144*m.b23*m.b30 + 1312*m.b24*m.b25 + 1032*m.b24*m.b26 + 784*m.b24*m.b27 + 552*
                       m.b24*m.b28 + 336*m.b24*m.b29 + 152*m.b24*m.b30 + 1056*m.b25*m.b26 + 800*m.b25*m.b27 + 576*m.b25*
                       m.b28 + 352*m.b25*m.b29 + 160*m.b25*m.b30 + 816*m.b26*m.b27 + 584*m.b26*m.b28 + 368*m.b26*m.b29
                        + 168*m.b26*m.b30 + 592*m.b27*m.b28 + 384*m.b27*m.b29 + 176*m.b27*m.b30 + 384*m.b28*m.b29 + 184*
                       m.b28*m.b30 + 192*m.b29*m.b30 - 364*m.b1 - 772*m.b2 - 1216*m.b3 - 1688*m.b4 - 2180*m.b5 - 2684*
                       m.b6 - 3192*m.b7 - 3696*m.b8 - 4204*m.b9 - 4708*m.b10 - 5200*m.b11 - 5672*m.b12 - 6116*m.b13 - 
                       6524*m.b14 - 6888*m.b15 - 6888*m.b16 - 6524*m.b17 - 6116*m.b18 - 5672*m.b19 - 5200*m.b20 - 4708*
                       m.b21 - 4204*m.b22 - 3696*m.b23 - 3192*m.b24 - 2684*m.b25 - 2180*m.b26 - 1688*m.b27 - 1216*m.b28
                        - 772*m.b29 - 364*m.b30 - m.x31 <= 0)

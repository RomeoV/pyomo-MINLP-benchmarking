#  MINLP written by GAMS Convert at 08/13/20 17:37:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21        1       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21        1       20        0


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
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x21, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b3*m.b4*
                       m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*
                       m.b8*m.b10 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*
                       m.b5*m.b6*m.b10 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 
                       128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*m.b10 + 64*m.b2*m.b3*m.b10
                       *m.b11 + 128*m.b2*m.b4*m.b5*m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*
                       m.b4*m.b8*m.b10 + 64*m.b2*m.b4*m.b9*m.b11 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5*m.b7*m.b10 + 
                       64*m.b2*m.b5*m.b8*m.b11 + 64*m.b2*m.b6*m.b7*m.b11 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*
                       m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*m.b10 + 128*m.b3*
                       m.b4*m.b10*m.b11 + 64*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9
                        + 192*m.b3*m.b5*m.b8*m.b10 + 128*m.b3*m.b5*m.b9*m.b11 + 64*m.b3*m.b5*m.b10*m.b12 + 192*m.b3*m.b6
                       *m.b7*m.b10 + 128*m.b3*m.b6*m.b8*m.b11 + 64*m.b3*m.b6*m.b9*m.b12 + 64*m.b3*m.b7*m.b8*m.b12 + 256*
                       m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*m.b4*m.b5*m.b8*m.b9 + 256*m.b4*m.b5*m.b9*
                       m.b10 + 192*m.b4*m.b5*m.b10*m.b11 + 128*m.b4*m.b5*m.b11*m.b12 + 64*m.b4*m.b5*m.b12*m.b13 + 256*
                       m.b4*m.b6*m.b7*m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 192*m.b4*m.b6*m.b9*m.b11 + 128*m.b4*m.b6*m.b10*
                       m.b12 + 64*m.b4*m.b6*m.b11*m.b13 + 192*m.b4*m.b7*m.b8*m.b11 + 128*m.b4*m.b7*m.b9*m.b12 + 64*m.b4*
                       m.b7*m.b10*m.b13 + 64*m.b4*m.b8*m.b9*m.b13 + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 
                       320*m.b5*m.b6*m.b9*m.b10 + 256*m.b5*m.b6*m.b10*m.b11 + 192*m.b5*m.b6*m.b11*m.b12 + 128*m.b5*m.b6*
                       m.b12*m.b13 + 64*m.b5*m.b6*m.b13*m.b14 + 320*m.b5*m.b7*m.b8*m.b10 + 256*m.b5*m.b7*m.b9*m.b11 + 
                       192*m.b5*m.b7*m.b10*m.b12 + 128*m.b5*m.b7*m.b11*m.b13 + 64*m.b5*m.b7*m.b12*m.b14 + 192*m.b5*m.b8*
                       m.b9*m.b12 + 128*m.b5*m.b8*m.b10*m.b13 + 64*m.b5*m.b8*m.b11*m.b14 + 64*m.b5*m.b9*m.b10*m.b14 + 
                       384*m.b6*m.b7*m.b8*m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 320*m.b6*m.b7*m.b10*m.b11 + 256*m.b6*m.b7*
                       m.b11*m.b12 + 192*m.b6*m.b7*m.b12*m.b13 + 128*m.b6*m.b7*m.b13*m.b14 + 64*m.b6*m.b7*m.b14*m.b15 + 
                       320*m.b6*m.b8*m.b9*m.b11 + 256*m.b6*m.b8*m.b10*m.b12 + 192*m.b6*m.b8*m.b11*m.b13 + 128*m.b6*m.b8*
                       m.b12*m.b14 + 64*m.b6*m.b8*m.b13*m.b15 + 192*m.b6*m.b9*m.b10*m.b13 + 128*m.b6*m.b9*m.b11*m.b14 + 
                       64*m.b6*m.b9*m.b12*m.b15 + 64*m.b6*m.b10*m.b11*m.b15 + 448*m.b7*m.b8*m.b9*m.b10 + 384*m.b7*m.b8*
                       m.b10*m.b11 + 320*m.b7*m.b8*m.b11*m.b12 + 256*m.b7*m.b8*m.b12*m.b13 + 192*m.b7*m.b8*m.b13*m.b14
                        + 128*m.b7*m.b8*m.b14*m.b15 + 64*m.b7*m.b8*m.b15*m.b16 + 320*m.b7*m.b9*m.b10*m.b12 + 256*m.b7*
                       m.b9*m.b11*m.b13 + 192*m.b7*m.b9*m.b12*m.b14 + 128*m.b7*m.b9*m.b13*m.b15 + 64*m.b7*m.b9*m.b14*
                       m.b16 + 192*m.b7*m.b10*m.b11*m.b14 + 128*m.b7*m.b10*m.b12*m.b15 + 64*m.b7*m.b10*m.b13*m.b16 + 64*
                       m.b7*m.b11*m.b12*m.b16 + 448*m.b8*m.b9*m.b10*m.b11 + 384*m.b8*m.b9*m.b11*m.b12 + 320*m.b8*m.b9*
                       m.b12*m.b13 + 256*m.b8*m.b9*m.b13*m.b14 + 192*m.b8*m.b9*m.b14*m.b15 + 128*m.b8*m.b9*m.b15*m.b16
                        + 64*m.b8*m.b9*m.b16*m.b17 + 320*m.b8*m.b10*m.b11*m.b13 + 256*m.b8*m.b10*m.b12*m.b14 + 192*m.b8*
                       m.b10*m.b13*m.b15 + 128*m.b8*m.b10*m.b14*m.b16 + 64*m.b8*m.b10*m.b15*m.b17 + 192*m.b8*m.b11*m.b12
                       *m.b15 + 128*m.b8*m.b11*m.b13*m.b16 + 64*m.b8*m.b11*m.b14*m.b17 + 64*m.b8*m.b12*m.b13*m.b17 + 448
                       *m.b9*m.b10*m.b11*m.b12 + 384*m.b9*m.b10*m.b12*m.b13 + 320*m.b9*m.b10*m.b13*m.b14 + 256*m.b9*
                       m.b10*m.b14*m.b15 + 192*m.b9*m.b10*m.b15*m.b16 + 128*m.b9*m.b10*m.b16*m.b17 + 64*m.b9*m.b10*m.b17
                       *m.b18 + 320*m.b9*m.b11*m.b12*m.b14 + 256*m.b9*m.b11*m.b13*m.b15 + 192*m.b9*m.b11*m.b14*m.b16 + 
                       128*m.b9*m.b11*m.b15*m.b17 + 64*m.b9*m.b11*m.b16*m.b18 + 192*m.b9*m.b12*m.b13*m.b16 + 128*m.b9*
                       m.b12*m.b14*m.b17 + 64*m.b9*m.b12*m.b15*m.b18 + 64*m.b9*m.b13*m.b14*m.b18 + 448*m.b10*m.b11*m.b12
                       *m.b13 + 384*m.b10*m.b11*m.b13*m.b14 + 320*m.b10*m.b11*m.b14*m.b15 + 256*m.b10*m.b11*m.b15*m.b16
                        + 192*m.b10*m.b11*m.b16*m.b17 + 128*m.b10*m.b11*m.b17*m.b18 + 64*m.b10*m.b11*m.b18*m.b19 + 320*
                       m.b10*m.b12*m.b13*m.b15 + 256*m.b10*m.b12*m.b14*m.b16 + 192*m.b10*m.b12*m.b15*m.b17 + 128*m.b10*
                       m.b12*m.b16*m.b18 + 64*m.b10*m.b12*m.b17*m.b19 + 192*m.b10*m.b13*m.b14*m.b17 + 128*m.b10*m.b13*
                       m.b15*m.b18 + 64*m.b10*m.b13*m.b16*m.b19 + 64*m.b10*m.b14*m.b15*m.b19 + 448*m.b11*m.b12*m.b13*
                       m.b14 + 384*m.b11*m.b12*m.b14*m.b15 + 320*m.b11*m.b12*m.b15*m.b16 + 256*m.b11*m.b12*m.b16*m.b17
                        + 192*m.b11*m.b12*m.b17*m.b18 + 128*m.b11*m.b12*m.b18*m.b19 + 64*m.b11*m.b12*m.b19*m.b20 + 320*
                       m.b11*m.b13*m.b14*m.b16 + 256*m.b11*m.b13*m.b15*m.b17 + 192*m.b11*m.b13*m.b16*m.b18 + 128*m.b11*
                       m.b13*m.b17*m.b19 + 64*m.b11*m.b13*m.b18*m.b20 + 192*m.b11*m.b14*m.b15*m.b18 + 128*m.b11*m.b14*
                       m.b16*m.b19 + 64*m.b11*m.b14*m.b17*m.b20 + 64*m.b11*m.b15*m.b16*m.b20 + 384*m.b12*m.b13*m.b14*
                       m.b15 + 320*m.b12*m.b13*m.b15*m.b16 + 256*m.b12*m.b13*m.b16*m.b17 + 192*m.b12*m.b13*m.b17*m.b18
                        + 128*m.b12*m.b13*m.b18*m.b19 + 64*m.b12*m.b13*m.b19*m.b20 + 256*m.b12*m.b14*m.b15*m.b17 + 192*
                       m.b12*m.b14*m.b16*m.b18 + 128*m.b12*m.b14*m.b17*m.b19 + 64*m.b12*m.b14*m.b18*m.b20 + 128*m.b12*
                       m.b15*m.b16*m.b19 + 64*m.b12*m.b15*m.b17*m.b20 + 320*m.b13*m.b14*m.b15*m.b16 + 256*m.b13*m.b14*
                       m.b16*m.b17 + 192*m.b13*m.b14*m.b17*m.b18 + 128*m.b13*m.b14*m.b18*m.b19 + 64*m.b13*m.b14*m.b19*
                       m.b20 + 192*m.b13*m.b15*m.b16*m.b18 + 128*m.b13*m.b15*m.b17*m.b19 + 64*m.b13*m.b15*m.b18*m.b20 + 
                       64*m.b13*m.b16*m.b17*m.b20 + 256*m.b14*m.b15*m.b16*m.b17 + 192*m.b14*m.b15*m.b17*m.b18 + 128*
                       m.b14*m.b15*m.b18*m.b19 + 64*m.b14*m.b15*m.b19*m.b20 + 128*m.b14*m.b16*m.b17*m.b19 + 64*m.b14*
                       m.b16*m.b18*m.b20 + 192*m.b15*m.b16*m.b17*m.b18 + 128*m.b15*m.b16*m.b18*m.b19 + 64*m.b15*m.b16*
                       m.b19*m.b20 + 64*m.b15*m.b17*m.b18*m.b20 + 128*m.b16*m.b17*m.b18*m.b19 + 64*m.b16*m.b17*m.b19*
                       m.b20 + 64*m.b17*m.b18*m.b19*m.b20 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 
                       64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*m.b9 - 32*m.b1*m.b2*
                       m.b10 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*
                       m.b3*m.b8 - 32*m.b1*m.b3*m.b9 - 32*m.b1*m.b3*m.b10 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*
                       m.b1*m.b4*m.b7 - 32*m.b1*m.b4*m.b8 - 32*m.b1*m.b4*m.b9 - 32*m.b1*m.b4*m.b10 - 64*m.b1*m.b5*m.b6
                        - 32*m.b1*m.b5*m.b7 - 32*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b10 - 32*m.b1*m.b6*m.b7 - 32*m.b1*m.b6*
                       m.b8 - 32*m.b1*m.b6*m.b9 - 32*m.b1*m.b6*m.b10 - 32*m.b1*m.b7*m.b8 - 32*m.b1*m.b7*m.b9 - 32*m.b1*
                       m.b7*m.b10 - 32*m.b1*m.b8*m.b9 - 32*m.b1*m.b8*m.b10 - 32*m.b1*m.b9*m.b10 - 96*m.b2*m.b3*m.b4 - 
                       128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*m.b3
                       *m.b9 - 96*m.b2*m.b3*m.b10 - 32*m.b2*m.b3*m.b11 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*
                       m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 96*m.b2*m.b4*m.b9 - 64*m.b2*m.b4*m.b10 - 32*m.b2*m.b4*m.b11
                        - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5*m.b7 - 32*m.b2*m.b5*m.b8 - 64*m.b2*m.b5*m.b9 - 64*m.b2*m.b5
                       *m.b10 - 32*m.b2*m.b5*m.b11 - 128*m.b2*m.b6*m.b7 - 64*m.b2*m.b6*m.b8 - 64*m.b2*m.b6*m.b9 - 32*
                       m.b2*m.b6*m.b11 - 96*m.b2*m.b7*m.b8 - 64*m.b2*m.b7*m.b9 - 64*m.b2*m.b7*m.b10 - 32*m.b2*m.b7*m.b11
                        - 96*m.b2*m.b8*m.b9 - 64*m.b2*m.b8*m.b10 - 32*m.b2*m.b8*m.b11 - 96*m.b2*m.b9*m.b10 - 32*m.b2*
                       m.b9*m.b11 - 32*m.b2*m.b10*m.b11 - 160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7
                        - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4*m.b9 - 160*m.b3*m.b4*m.b10 - 96*m.b3*m.b4*m.b11 - 32*m.b3*
                       m.b4*m.b12 - 256*m.b3*m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 160*m.b3*m.b5*m.b9 - 
                       128*m.b3*m.b5*m.b10 - 64*m.b3*m.b5*m.b11 - 32*m.b3*m.b5*m.b12 - 256*m.b3*m.b6*m.b7 - 192*m.b3*
                       m.b6*m.b8 - 32*m.b3*m.b6*m.b9 - 96*m.b3*m.b6*m.b10 - 64*m.b3*m.b6*m.b11 - 32*m.b3*m.b6*m.b12 - 
                       192*m.b3*m.b7*m.b8 - 128*m.b3*m.b7*m.b9 - 96*m.b3*m.b7*m.b10 - 32*m.b3*m.b7*m.b12 - 160*m.b3*m.b8
                       *m.b9 - 128*m.b3*m.b8*m.b10 - 64*m.b3*m.b8*m.b11 - 32*m.b3*m.b8*m.b12 - 160*m.b3*m.b9*m.b10 - 64*
                       m.b3*m.b9*m.b11 - 32*m.b3*m.b9*m.b12 - 96*m.b3*m.b10*m.b11 - 32*m.b3*m.b10*m.b12 - 32*m.b3*m.b11*
                       m.b12 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 224*
                       m.b4*m.b5*m.b10 - 160*m.b4*m.b5*m.b11 - 96*m.b4*m.b5*m.b12 - 32*m.b4*m.b5*m.b13 - 352*m.b4*m.b6*
                       m.b7 - 192*m.b4*m.b6*m.b8 - 256*m.b4*m.b6*m.b9 - 192*m.b4*m.b6*m.b10 - 128*m.b4*m.b6*m.b11 - 64*
                       m.b4*m.b6*m.b12 - 32*m.b4*m.b6*m.b13 - 320*m.b4*m.b7*m.b8 - 256*m.b4*m.b7*m.b9 - 64*m.b4*m.b7*
                       m.b10 - 96*m.b4*m.b7*m.b11 - 64*m.b4*m.b7*m.b12 - 32*m.b4*m.b7*m.b13 - 256*m.b4*m.b8*m.b9 - 192*
                       m.b4*m.b8*m.b10 - 96*m.b4*m.b8*m.b11 - 32*m.b4*m.b8*m.b13 - 224*m.b4*m.b9*m.b10 - 128*m.b4*m.b9*
                       m.b11 - 64*m.b4*m.b9*m.b12 - 32*m.b4*m.b9*m.b13 - 160*m.b4*m.b10*m.b11 - 64*m.b4*m.b10*m.b12 - 32
                       *m.b4*m.b10*m.b13 - 96*m.b4*m.b11*m.b12 - 32*m.b4*m.b11*m.b13 - 32*m.b4*m.b12*m.b13 - 288*m.b5*
                       m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 320*m.b5*m.b6*m.b10 - 224*m.b5*m.b6*m.b11
                        - 160*m.b5*m.b6*m.b12 - 96*m.b5*m.b6*m.b13 - 32*m.b5*m.b6*m.b14 - 448*m.b5*m.b7*m.b8 - 224*m.b5*
                       m.b7*m.b9 - 320*m.b5*m.b7*m.b10 - 192*m.b5*m.b7*m.b11 - 128*m.b5*m.b7*m.b12 - 64*m.b5*m.b7*m.b13
                        - 32*m.b5*m.b7*m.b14 - 384*m.b5*m.b8*m.b9 - 320*m.b5*m.b8*m.b10 - 64*m.b5*m.b8*m.b11 - 96*m.b5*
                       m.b8*m.b12 - 64*m.b5*m.b8*m.b13 - 32*m.b5*m.b8*m.b14 - 320*m.b5*m.b9*m.b10 - 192*m.b5*m.b9*m.b11
                        - 96*m.b5*m.b9*m.b12 - 32*m.b5*m.b9*m.b14 - 224*m.b5*m.b10*m.b11 - 128*m.b5*m.b10*m.b12 - 64*
                       m.b5*m.b10*m.b13 - 32*m.b5*m.b10*m.b14 - 160*m.b5*m.b11*m.b12 - 64*m.b5*m.b11*m.b13 - 32*m.b5*
                       m.b11*m.b14 - 96*m.b5*m.b12*m.b13 - 32*m.b5*m.b12*m.b14 - 32*m.b5*m.b13*m.b14 - 352*m.b6*m.b7*
                       m.b8 - 512*m.b6*m.b7*m.b9 - 448*m.b6*m.b7*m.b10 - 320*m.b6*m.b7*m.b11 - 224*m.b6*m.b7*m.b12 - 160
                       *m.b6*m.b7*m.b13 - 96*m.b6*m.b7*m.b14 - 32*m.b6*m.b7*m.b15 - 512*m.b6*m.b8*m.b9 - 256*m.b6*m.b8*
                       m.b10 - 320*m.b6*m.b8*m.b11 - 192*m.b6*m.b8*m.b12 - 128*m.b6*m.b8*m.b13 - 64*m.b6*m.b8*m.b14 - 32
                       *m.b6*m.b8*m.b15 - 448*m.b6*m.b9*m.b10 - 320*m.b6*m.b9*m.b11 - 64*m.b6*m.b9*m.b12 - 96*m.b6*m.b9*
                       m.b13 - 64*m.b6*m.b9*m.b14 - 32*m.b6*m.b9*m.b15 - 320*m.b6*m.b10*m.b11 - 192*m.b6*m.b10*m.b12 - 
                       96*m.b6*m.b10*m.b13 - 32*m.b6*m.b10*m.b15 - 224*m.b6*m.b11*m.b12 - 128*m.b6*m.b11*m.b13 - 64*m.b6
                       *m.b11*m.b14 - 32*m.b6*m.b11*m.b15 - 160*m.b6*m.b12*m.b13 - 64*m.b6*m.b12*m.b14 - 32*m.b6*m.b12*
                       m.b15 - 96*m.b6*m.b13*m.b14 - 32*m.b6*m.b13*m.b15 - 32*m.b6*m.b14*m.b15 - 416*m.b7*m.b8*m.b9 - 
                       576*m.b7*m.b8*m.b10 - 448*m.b7*m.b8*m.b11 - 320*m.b7*m.b8*m.b12 - 224*m.b7*m.b8*m.b13 - 160*m.b7*
                       m.b8*m.b14 - 96*m.b7*m.b8*m.b15 - 32*m.b7*m.b8*m.b16 - 576*m.b7*m.b9*m.b10 - 256*m.b7*m.b9*m.b11
                        - 320*m.b7*m.b9*m.b12 - 192*m.b7*m.b9*m.b13 - 128*m.b7*m.b9*m.b14 - 64*m.b7*m.b9*m.b15 - 32*m.b7
                       *m.b9*m.b16 - 448*m.b7*m.b10*m.b11 - 320*m.b7*m.b10*m.b12 - 64*m.b7*m.b10*m.b13 - 96*m.b7*m.b10*
                       m.b14 - 64*m.b7*m.b10*m.b15 - 32*m.b7*m.b10*m.b16 - 320*m.b7*m.b11*m.b12 - 192*m.b7*m.b11*m.b13
                        - 96*m.b7*m.b11*m.b14 - 32*m.b7*m.b11*m.b16 - 224*m.b7*m.b12*m.b13 - 128*m.b7*m.b12*m.b14 - 64*
                       m.b7*m.b12*m.b15 - 32*m.b7*m.b12*m.b16 - 160*m.b7*m.b13*m.b14 - 64*m.b7*m.b13*m.b15 - 32*m.b7*
                       m.b13*m.b16 - 96*m.b7*m.b14*m.b15 - 32*m.b7*m.b14*m.b16 - 32*m.b7*m.b15*m.b16 - 448*m.b8*m.b9*
                       m.b10 - 576*m.b8*m.b9*m.b11 - 448*m.b8*m.b9*m.b12 - 320*m.b8*m.b9*m.b13 - 224*m.b8*m.b9*m.b14 - 
                       160*m.b8*m.b9*m.b15 - 96*m.b8*m.b9*m.b16 - 32*m.b8*m.b9*m.b17 - 576*m.b8*m.b10*m.b11 - 256*m.b8*
                       m.b10*m.b12 - 320*m.b8*m.b10*m.b13 - 192*m.b8*m.b10*m.b14 - 128*m.b8*m.b10*m.b15 - 64*m.b8*m.b10*
                       m.b16 - 32*m.b8*m.b10*m.b17 - 448*m.b8*m.b11*m.b12 - 320*m.b8*m.b11*m.b13 - 64*m.b8*m.b11*m.b14
                        - 96*m.b8*m.b11*m.b15 - 64*m.b8*m.b11*m.b16 - 32*m.b8*m.b11*m.b17 - 320*m.b8*m.b12*m.b13 - 192*
                       m.b8*m.b12*m.b14 - 96*m.b8*m.b12*m.b15 - 32*m.b8*m.b12*m.b17 - 224*m.b8*m.b13*m.b14 - 128*m.b8*
                       m.b13*m.b15 - 64*m.b8*m.b13*m.b16 - 32*m.b8*m.b13*m.b17 - 160*m.b8*m.b14*m.b15 - 64*m.b8*m.b14*
                       m.b16 - 32*m.b8*m.b14*m.b17 - 96*m.b8*m.b15*m.b16 - 32*m.b8*m.b15*m.b17 - 32*m.b8*m.b16*m.b17 - 
                       448*m.b9*m.b10*m.b11 - 576*m.b9*m.b10*m.b12 - 448*m.b9*m.b10*m.b13 - 320*m.b9*m.b10*m.b14 - 224*
                       m.b9*m.b10*m.b15 - 160*m.b9*m.b10*m.b16 - 96*m.b9*m.b10*m.b17 - 32*m.b9*m.b10*m.b18 - 576*m.b9*
                       m.b11*m.b12 - 256*m.b9*m.b11*m.b13 - 320*m.b9*m.b11*m.b14 - 192*m.b9*m.b11*m.b15 - 128*m.b9*m.b11
                       *m.b16 - 64*m.b9*m.b11*m.b17 - 32*m.b9*m.b11*m.b18 - 448*m.b9*m.b12*m.b13 - 320*m.b9*m.b12*m.b14
                        - 64*m.b9*m.b12*m.b15 - 96*m.b9*m.b12*m.b16 - 64*m.b9*m.b12*m.b17 - 32*m.b9*m.b12*m.b18 - 320*
                       m.b9*m.b13*m.b14 - 192*m.b9*m.b13*m.b15 - 96*m.b9*m.b13*m.b16 - 32*m.b9*m.b13*m.b18 - 224*m.b9*
                       m.b14*m.b15 - 128*m.b9*m.b14*m.b16 - 64*m.b9*m.b14*m.b17 - 32*m.b9*m.b14*m.b18 - 160*m.b9*m.b15*
                       m.b16 - 64*m.b9*m.b15*m.b17 - 32*m.b9*m.b15*m.b18 - 96*m.b9*m.b16*m.b17 - 32*m.b9*m.b16*m.b18 - 
                       32*m.b9*m.b17*m.b18 - 448*m.b10*m.b11*m.b12 - 576*m.b10*m.b11*m.b13 - 448*m.b10*m.b11*m.b14 - 320
                       *m.b10*m.b11*m.b15 - 224*m.b10*m.b11*m.b16 - 160*m.b10*m.b11*m.b17 - 96*m.b10*m.b11*m.b18 - 32*
                       m.b10*m.b11*m.b19 - 576*m.b10*m.b12*m.b13 - 256*m.b10*m.b12*m.b14 - 320*m.b10*m.b12*m.b15 - 192*
                       m.b10*m.b12*m.b16 - 128*m.b10*m.b12*m.b17 - 64*m.b10*m.b12*m.b18 - 32*m.b10*m.b12*m.b19 - 448*
                       m.b10*m.b13*m.b14 - 320*m.b10*m.b13*m.b15 - 64*m.b10*m.b13*m.b16 - 96*m.b10*m.b13*m.b17 - 64*
                       m.b10*m.b13*m.b18 - 32*m.b10*m.b13*m.b19 - 320*m.b10*m.b14*m.b15 - 192*m.b10*m.b14*m.b16 - 96*
                       m.b10*m.b14*m.b17 - 32*m.b10*m.b14*m.b19 - 224*m.b10*m.b15*m.b16 - 128*m.b10*m.b15*m.b17 - 64*
                       m.b10*m.b15*m.b18 - 32*m.b10*m.b15*m.b19 - 160*m.b10*m.b16*m.b17 - 64*m.b10*m.b16*m.b18 - 32*
                       m.b10*m.b16*m.b19 - 96*m.b10*m.b17*m.b18 - 32*m.b10*m.b17*m.b19 - 32*m.b10*m.b18*m.b19 - 448*
                       m.b11*m.b12*m.b13 - 576*m.b11*m.b12*m.b14 - 448*m.b11*m.b12*m.b15 - 320*m.b11*m.b12*m.b16 - 224*
                       m.b11*m.b12*m.b17 - 160*m.b11*m.b12*m.b18 - 96*m.b11*m.b12*m.b19 - 32*m.b11*m.b12*m.b20 - 576*
                       m.b11*m.b13*m.b14 - 256*m.b11*m.b13*m.b15 - 320*m.b11*m.b13*m.b16 - 192*m.b11*m.b13*m.b17 - 128*
                       m.b11*m.b13*m.b18 - 64*m.b11*m.b13*m.b19 - 32*m.b11*m.b13*m.b20 - 448*m.b11*m.b14*m.b15 - 320*
                       m.b11*m.b14*m.b16 - 64*m.b11*m.b14*m.b17 - 96*m.b11*m.b14*m.b18 - 64*m.b11*m.b14*m.b19 - 32*m.b11
                       *m.b14*m.b20 - 320*m.b11*m.b15*m.b16 - 192*m.b11*m.b15*m.b17 - 96*m.b11*m.b15*m.b18 - 32*m.b11*
                       m.b15*m.b20 - 224*m.b11*m.b16*m.b17 - 128*m.b11*m.b16*m.b18 - 64*m.b11*m.b16*m.b19 - 32*m.b11*
                       m.b16*m.b20 - 160*m.b11*m.b17*m.b18 - 64*m.b11*m.b17*m.b19 - 32*m.b11*m.b17*m.b20 - 96*m.b11*
                       m.b18*m.b19 - 32*m.b11*m.b18*m.b20 - 32*m.b11*m.b19*m.b20 - 416*m.b12*m.b13*m.b14 - 512*m.b12*
                       m.b13*m.b15 - 384*m.b12*m.b13*m.b16 - 256*m.b12*m.b13*m.b17 - 160*m.b12*m.b13*m.b18 - 96*m.b12*
                       m.b13*m.b19 - 32*m.b12*m.b13*m.b20 - 512*m.b12*m.b14*m.b15 - 224*m.b12*m.b14*m.b16 - 256*m.b12*
                       m.b14*m.b17 - 128*m.b12*m.b14*m.b18 - 64*m.b12*m.b14*m.b19 - 32*m.b12*m.b14*m.b20 - 384*m.b12*
                       m.b15*m.b16 - 256*m.b12*m.b15*m.b17 - 32*m.b12*m.b15*m.b18 - 64*m.b12*m.b15*m.b19 - 32*m.b12*
                       m.b15*m.b20 - 256*m.b12*m.b16*m.b17 - 160*m.b12*m.b16*m.b18 - 64*m.b12*m.b16*m.b19 - 192*m.b12*
                       m.b17*m.b18 - 96*m.b12*m.b17*m.b19 - 32*m.b12*m.b17*m.b20 - 128*m.b12*m.b18*m.b19 - 32*m.b12*
                       m.b18*m.b20 - 64*m.b12*m.b19*m.b20 - 352*m.b13*m.b14*m.b15 - 448*m.b13*m.b14*m.b16 - 320*m.b13*
                       m.b14*m.b17 - 192*m.b13*m.b14*m.b18 - 96*m.b13*m.b14*m.b19 - 32*m.b13*m.b14*m.b20 - 416*m.b13*
                       m.b15*m.b16 - 192*m.b13*m.b15*m.b17 - 192*m.b13*m.b15*m.b18 - 64*m.b13*m.b15*m.b19 - 32*m.b13*
                       m.b15*m.b20 - 288*m.b13*m.b16*m.b17 - 192*m.b13*m.b16*m.b18 - 32*m.b13*m.b16*m.b19 - 32*m.b13*
                       m.b16*m.b20 - 192*m.b13*m.b17*m.b18 - 128*m.b13*m.b17*m.b19 - 32*m.b13*m.b17*m.b20 - 128*m.b13*
                       m.b18*m.b19 - 64*m.b13*m.b18*m.b20 - 64*m.b13*m.b19*m.b20 - 288*m.b14*m.b15*m.b16 - 352*m.b14*
                       m.b15*m.b17 - 256*m.b14*m.b15*m.b18 - 128*m.b14*m.b15*m.b19 - 32*m.b14*m.b15*m.b20 - 320*m.b14*
                       m.b16*m.b17 - 128*m.b14*m.b16*m.b18 - 128*m.b14*m.b16*m.b19 - 32*m.b14*m.b16*m.b20 - 192*m.b14*
                       m.b17*m.b18 - 128*m.b14*m.b17*m.b19 - 32*m.b14*m.b17*m.b20 - 128*m.b14*m.b18*m.b19 - 64*m.b14*
                       m.b18*m.b20 - 64*m.b14*m.b19*m.b20 - 224*m.b15*m.b16*m.b17 - 256*m.b15*m.b16*m.b18 - 160*m.b15*
                       m.b16*m.b19 - 64*m.b15*m.b16*m.b20 - 224*m.b15*m.b17*m.b18 - 64*m.b15*m.b17*m.b19 - 64*m.b15*
                       m.b17*m.b20 - 128*m.b15*m.b18*m.b19 - 64*m.b15*m.b18*m.b20 - 64*m.b15*m.b19*m.b20 - 160*m.b16*
                       m.b17*m.b18 - 160*m.b16*m.b17*m.b19 - 64*m.b16*m.b17*m.b20 - 128*m.b16*m.b18*m.b19 - 32*m.b16*
                       m.b18*m.b20 - 64*m.b16*m.b19*m.b20 - 96*m.b17*m.b18*m.b19 - 64*m.b17*m.b18*m.b20 - 64*m.b17*m.b19
                       *m.b20 - 32*m.b18*m.b19*m.b20 + 112*m.b1*m.b2 + 104*m.b1*m.b3 + 96*m.b1*m.b4 + 88*m.b1*m.b5 + 96*
                       m.b1*m.b6 + 88*m.b1*m.b7 + 80*m.b1*m.b8 + 72*m.b1*m.b9 + 64*m.b1*m.b10 + 224*m.b2*m.b3 + 224*m.b2
                       *m.b4 + 208*m.b2*m.b5 + 192*m.b2*m.b6 + 208*m.b2*m.b7 + 192*m.b2*m.b8 + 176*m.b2*m.b9 + 144*m.b2*
                       m.b10 + 64*m.b2*m.b11 + 352*m.b3*m.b4 + 344*m.b3*m.b5 + 336*m.b3*m.b6 + 328*m.b3*m.b7 + 336*m.b3*
                       m.b8 + 296*m.b3*m.b9 + 256*m.b3*m.b10 + 144*m.b3*m.b11 + 64*m.b3*m.b12 + 496*m.b4*m.b5 + 480*m.b4
                       *m.b6 + 464*m.b4*m.b7 + 464*m.b4*m.b8 + 448*m.b4*m.b9 + 384*m.b4*m.b10 + 256*m.b4*m.b11 + 144*
                       m.b4*m.b12 + 64*m.b4*m.b13 + 656*m.b5*m.b6 + 616*m.b5*m.b7 + 592*m.b5*m.b8 + 568*m.b5*m.b9 + 544*
                       m.b5*m.b10 + 384*m.b5*m.b11 + 256*m.b5*m.b12 + 144*m.b5*m.b13 + 64*m.b5*m.b14 + 800*m.b6*m.b7 + 
                       736*m.b6*m.b8 + 704*m.b6*m.b9 + 656*m.b6*m.b10 + 544*m.b6*m.b11 + 384*m.b6*m.b12 + 256*m.b6*m.b13
                        + 144*m.b6*m.b14 + 64*m.b6*m.b15 + 928*m.b7*m.b8 + 856*m.b7*m.b9 + 800*m.b7*m.b10 + 656*m.b7*
                       m.b11 + 544*m.b7*m.b12 + 384*m.b7*m.b13 + 256*m.b7*m.b14 + 144*m.b7*m.b15 + 64*m.b7*m.b16 + 1040*
                       m.b8*m.b9 + 960*m.b8*m.b10 + 800*m.b8*m.b11 + 656*m.b8*m.b12 + 544*m.b8*m.b13 + 384*m.b8*m.b14 + 
                       256*m.b8*m.b15 + 144*m.b8*m.b16 + 64*m.b8*m.b17 + 1152*m.b9*m.b10 + 960*m.b9*m.b11 + 800*m.b9*
                       m.b12 + 656*m.b9*m.b13 + 544*m.b9*m.b14 + 384*m.b9*m.b15 + 256*m.b9*m.b16 + 144*m.b9*m.b17 + 64*
                       m.b9*m.b18 + 1152*m.b10*m.b11 + 960*m.b10*m.b12 + 800*m.b10*m.b13 + 656*m.b10*m.b14 + 544*m.b10*
                       m.b15 + 384*m.b10*m.b16 + 256*m.b10*m.b17 + 144*m.b10*m.b18 + 64*m.b10*m.b19 + 1152*m.b11*m.b12
                        + 960*m.b11*m.b13 + 800*m.b11*m.b14 + 656*m.b11*m.b15 + 544*m.b11*m.b16 + 384*m.b11*m.b17 + 256*
                       m.b11*m.b18 + 144*m.b11*m.b19 + 64*m.b11*m.b20 + 1040*m.b12*m.b13 + 856*m.b12*m.b14 + 704*m.b12*
                       m.b15 + 568*m.b12*m.b16 + 448*m.b12*m.b17 + 296*m.b12*m.b18 + 176*m.b12*m.b19 + 72*m.b12*m.b20 + 
                       928*m.b13*m.b14 + 736*m.b13*m.b15 + 592*m.b13*m.b16 + 464*m.b13*m.b17 + 336*m.b13*m.b18 + 192*
                       m.b13*m.b19 + 80*m.b13*m.b20 + 800*m.b14*m.b15 + 616*m.b14*m.b16 + 464*m.b14*m.b17 + 328*m.b14*
                       m.b18 + 208*m.b14*m.b19 + 88*m.b14*m.b20 + 656*m.b15*m.b16 + 480*m.b15*m.b17 + 336*m.b15*m.b18 + 
                       192*m.b15*m.b19 + 96*m.b15*m.b20 + 496*m.b16*m.b17 + 344*m.b16*m.b18 + 208*m.b16*m.b19 + 88*m.b16
                       *m.b20 + 352*m.b17*m.b18 + 224*m.b17*m.b19 + 96*m.b17*m.b20 + 224*m.b18*m.b19 + 104*m.b18*m.b20
                        + 112*m.b19*m.b20 - 144*m.b1 - 312*m.b2 - 496*m.b3 - 688*m.b4 - 880*m.b5 - 1072*m.b6 - 1264*m.b7
                        - 1448*m.b8 - 1616*m.b9 - 1760*m.b10 - 1760*m.b11 - 1616*m.b12 - 1448*m.b13 - 1264*m.b14 - 1072*
                       m.b15 - 880*m.b16 - 688*m.b17 - 496*m.b18 - 312*m.b19 - 144*m.b20 - m.x21 <= 0)

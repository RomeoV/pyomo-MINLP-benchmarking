#  MINLP written by GAMS Convert at 08/13/20 17:37:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         41        1       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         41        1       40        0


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
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x41, sense=minimize)

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
                       m.b16*m.b19 + 64*m.b11*m.b14*m.b17*m.b20 + 64*m.b11*m.b15*m.b16*m.b20 + 448*m.b12*m.b13*m.b14*
                       m.b15 + 384*m.b12*m.b13*m.b15*m.b16 + 320*m.b12*m.b13*m.b16*m.b17 + 256*m.b12*m.b13*m.b17*m.b18
                        + 192*m.b12*m.b13*m.b18*m.b19 + 128*m.b12*m.b13*m.b19*m.b20 + 64*m.b12*m.b13*m.b20*m.b21 + 320*
                       m.b12*m.b14*m.b15*m.b17 + 256*m.b12*m.b14*m.b16*m.b18 + 192*m.b12*m.b14*m.b17*m.b19 + 128*m.b12*
                       m.b14*m.b18*m.b20 + 64*m.b12*m.b14*m.b19*m.b21 + 192*m.b12*m.b15*m.b16*m.b19 + 128*m.b12*m.b15*
                       m.b17*m.b20 + 64*m.b12*m.b15*m.b18*m.b21 + 64*m.b12*m.b16*m.b17*m.b21 + 448*m.b13*m.b14*m.b15*
                       m.b16 + 384*m.b13*m.b14*m.b16*m.b17 + 320*m.b13*m.b14*m.b17*m.b18 + 256*m.b13*m.b14*m.b18*m.b19
                        + 192*m.b13*m.b14*m.b19*m.b20 + 128*m.b13*m.b14*m.b20*m.b21 + 64*m.b13*m.b14*m.b21*m.b22 + 320*
                       m.b13*m.b15*m.b16*m.b18 + 256*m.b13*m.b15*m.b17*m.b19 + 192*m.b13*m.b15*m.b18*m.b20 + 128*m.b13*
                       m.b15*m.b19*m.b21 + 64*m.b13*m.b15*m.b20*m.b22 + 192*m.b13*m.b16*m.b17*m.b20 + 128*m.b13*m.b16*
                       m.b18*m.b21 + 64*m.b13*m.b16*m.b19*m.b22 + 64*m.b13*m.b17*m.b18*m.b22 + 448*m.b14*m.b15*m.b16*
                       m.b17 + 384*m.b14*m.b15*m.b17*m.b18 + 320*m.b14*m.b15*m.b18*m.b19 + 256*m.b14*m.b15*m.b19*m.b20
                        + 192*m.b14*m.b15*m.b20*m.b21 + 128*m.b14*m.b15*m.b21*m.b22 + 64*m.b14*m.b15*m.b22*m.b23 + 320*
                       m.b14*m.b16*m.b17*m.b19 + 256*m.b14*m.b16*m.b18*m.b20 + 192*m.b14*m.b16*m.b19*m.b21 + 128*m.b14*
                       m.b16*m.b20*m.b22 + 64*m.b14*m.b16*m.b21*m.b23 + 192*m.b14*m.b17*m.b18*m.b21 + 128*m.b14*m.b17*
                       m.b19*m.b22 + 64*m.b14*m.b17*m.b20*m.b23 + 64*m.b14*m.b18*m.b19*m.b23 + 448*m.b15*m.b16*m.b17*
                       m.b18 + 384*m.b15*m.b16*m.b18*m.b19 + 320*m.b15*m.b16*m.b19*m.b20 + 256*m.b15*m.b16*m.b20*m.b21
                        + 192*m.b15*m.b16*m.b21*m.b22 + 128*m.b15*m.b16*m.b22*m.b23 + 64*m.b15*m.b16*m.b23*m.b24 + 320*
                       m.b15*m.b17*m.b18*m.b20 + 256*m.b15*m.b17*m.b19*m.b21 + 192*m.b15*m.b17*m.b20*m.b22 + 128*m.b15*
                       m.b17*m.b21*m.b23 + 64*m.b15*m.b17*m.b22*m.b24 + 192*m.b15*m.b18*m.b19*m.b22 + 128*m.b15*m.b18*
                       m.b20*m.b23 + 64*m.b15*m.b18*m.b21*m.b24 + 64*m.b15*m.b19*m.b20*m.b24 + 448*m.b16*m.b17*m.b18*
                       m.b19 + 384*m.b16*m.b17*m.b19*m.b20 + 320*m.b16*m.b17*m.b20*m.b21 + 256*m.b16*m.b17*m.b21*m.b22
                        + 192*m.b16*m.b17*m.b22*m.b23 + 128*m.b16*m.b17*m.b23*m.b24 + 64*m.b16*m.b17*m.b24*m.b25 + 320*
                       m.b16*m.b18*m.b19*m.b21 + 256*m.b16*m.b18*m.b20*m.b22 + 192*m.b16*m.b18*m.b21*m.b23 + 128*m.b16*
                       m.b18*m.b22*m.b24 + 64*m.b16*m.b18*m.b23*m.b25 + 192*m.b16*m.b19*m.b20*m.b23 + 128*m.b16*m.b19*
                       m.b21*m.b24 + 64*m.b16*m.b19*m.b22*m.b25 + 64*m.b16*m.b20*m.b21*m.b25 + 448*m.b17*m.b18*m.b19*
                       m.b20 + 384*m.b17*m.b18*m.b20*m.b21 + 320*m.b17*m.b18*m.b21*m.b22 + 256*m.b17*m.b18*m.b22*m.b23
                        + 192*m.b17*m.b18*m.b23*m.b24 + 128*m.b17*m.b18*m.b24*m.b25 + 64*m.b17*m.b18*m.b25*m.b26 + 320*
                       m.b17*m.b19*m.b20*m.b22 + 256*m.b17*m.b19*m.b21*m.b23 + 192*m.b17*m.b19*m.b22*m.b24 + 128*m.b17*
                       m.b19*m.b23*m.b25 + 64*m.b17*m.b19*m.b24*m.b26 + 192*m.b17*m.b20*m.b21*m.b24 + 128*m.b17*m.b20*
                       m.b22*m.b25 + 64*m.b17*m.b20*m.b23*m.b26 + 64*m.b17*m.b21*m.b22*m.b26 + 448*m.b18*m.b19*m.b20*
                       m.b21 + 384*m.b18*m.b19*m.b21*m.b22 + 320*m.b18*m.b19*m.b22*m.b23 + 256*m.b18*m.b19*m.b23*m.b24
                        + 192*m.b18*m.b19*m.b24*m.b25 + 128*m.b18*m.b19*m.b25*m.b26 + 64*m.b18*m.b19*m.b26*m.b27 + 320*
                       m.b18*m.b20*m.b21*m.b23 + 256*m.b18*m.b20*m.b22*m.b24 + 192*m.b18*m.b20*m.b23*m.b25 + 128*m.b18*
                       m.b20*m.b24*m.b26 + 64*m.b18*m.b20*m.b25*m.b27 + 192*m.b18*m.b21*m.b22*m.b25 + 128*m.b18*m.b21*
                       m.b23*m.b26 + 64*m.b18*m.b21*m.b24*m.b27 + 64*m.b18*m.b22*m.b23*m.b27 + 448*m.b19*m.b20*m.b21*
                       m.b22 + 384*m.b19*m.b20*m.b22*m.b23 + 320*m.b19*m.b20*m.b23*m.b24 + 256*m.b19*m.b20*m.b24*m.b25
                        + 192*m.b19*m.b20*m.b25*m.b26 + 128*m.b19*m.b20*m.b26*m.b27 + 64*m.b19*m.b20*m.b27*m.b28 + 320*
                       m.b19*m.b21*m.b22*m.b24 + 256*m.b19*m.b21*m.b23*m.b25 + 192*m.b19*m.b21*m.b24*m.b26 + 128*m.b19*
                       m.b21*m.b25*m.b27 + 64*m.b19*m.b21*m.b26*m.b28 + 192*m.b19*m.b22*m.b23*m.b26 + 128*m.b19*m.b22*
                       m.b24*m.b27 + 64*m.b19*m.b22*m.b25*m.b28 + 64*m.b19*m.b23*m.b24*m.b28 + 448*m.b20*m.b21*m.b22*
                       m.b23 + 384*m.b20*m.b21*m.b23*m.b24 + 320*m.b20*m.b21*m.b24*m.b25 + 256*m.b20*m.b21*m.b25*m.b26
                        + 192*m.b20*m.b21*m.b26*m.b27 + 128*m.b20*m.b21*m.b27*m.b28 + 64*m.b20*m.b21*m.b28*m.b29 + 320*
                       m.b20*m.b22*m.b23*m.b25 + 256*m.b20*m.b22*m.b24*m.b26 + 192*m.b20*m.b22*m.b25*m.b27 + 128*m.b20*
                       m.b22*m.b26*m.b28 + 64*m.b20*m.b22*m.b27*m.b29 + 192*m.b20*m.b23*m.b24*m.b27 + 128*m.b20*m.b23*
                       m.b25*m.b28 + 64*m.b20*m.b23*m.b26*m.b29 + 64*m.b20*m.b24*m.b25*m.b29 + 448*m.b21*m.b22*m.b23*
                       m.b24 + 384*m.b21*m.b22*m.b24*m.b25 + 320*m.b21*m.b22*m.b25*m.b26 + 256*m.b21*m.b22*m.b26*m.b27
                        + 192*m.b21*m.b22*m.b27*m.b28 + 128*m.b21*m.b22*m.b28*m.b29 + 64*m.b21*m.b22*m.b29*m.b30 + 320*
                       m.b21*m.b23*m.b24*m.b26 + 256*m.b21*m.b23*m.b25*m.b27 + 192*m.b21*m.b23*m.b26*m.b28 + 128*m.b21*
                       m.b23*m.b27*m.b29 + 64*m.b21*m.b23*m.b28*m.b30 + 192*m.b21*m.b24*m.b25*m.b28 + 128*m.b21*m.b24*
                       m.b26*m.b29 + 64*m.b21*m.b24*m.b27*m.b30 + 64*m.b21*m.b25*m.b26*m.b30 + 448*m.b22*m.b23*m.b24*
                       m.b25 + 384*m.b22*m.b23*m.b25*m.b26 + 320*m.b22*m.b23*m.b26*m.b27 + 256*m.b22*m.b23*m.b27*m.b28
                        + 192*m.b22*m.b23*m.b28*m.b29 + 128*m.b22*m.b23*m.b29*m.b30 + 64*m.b22*m.b23*m.b30*m.b31 + 320*
                       m.b22*m.b24*m.b25*m.b27 + 256*m.b22*m.b24*m.b26*m.b28 + 192*m.b22*m.b24*m.b27*m.b29 + 128*m.b22*
                       m.b24*m.b28*m.b30 + 64*m.b22*m.b24*m.b29*m.b31 + 192*m.b22*m.b25*m.b26*m.b29 + 128*m.b22*m.b25*
                       m.b27*m.b30 + 64*m.b22*m.b25*m.b28*m.b31 + 64*m.b22*m.b26*m.b27*m.b31 + 448*m.b23*m.b24*m.b25*
                       m.b26 + 384*m.b23*m.b24*m.b26*m.b27 + 320*m.b23*m.b24*m.b27*m.b28 + 256*m.b23*m.b24*m.b28*m.b29
                        + 192*m.b23*m.b24*m.b29*m.b30 + 128*m.b23*m.b24*m.b30*m.b31 + 64*m.b23*m.b24*m.b31*m.b32 + 320*
                       m.b23*m.b25*m.b26*m.b28 + 256*m.b23*m.b25*m.b27*m.b29 + 192*m.b23*m.b25*m.b28*m.b30 + 128*m.b23*
                       m.b25*m.b29*m.b31 + 64*m.b23*m.b25*m.b30*m.b32 + 192*m.b23*m.b26*m.b27*m.b30 + 128*m.b23*m.b26*
                       m.b28*m.b31 + 64*m.b23*m.b26*m.b29*m.b32 + 64*m.b23*m.b27*m.b28*m.b32 + 448*m.b24*m.b25*m.b26*
                       m.b27 + 384*m.b24*m.b25*m.b27*m.b28 + 320*m.b24*m.b25*m.b28*m.b29 + 256*m.b24*m.b25*m.b29*m.b30
                        + 192*m.b24*m.b25*m.b30*m.b31 + 128*m.b24*m.b25*m.b31*m.b32 + 64*m.b24*m.b25*m.b32*m.b33 + 320*
                       m.b24*m.b26*m.b27*m.b29 + 256*m.b24*m.b26*m.b28*m.b30 + 192*m.b24*m.b26*m.b29*m.b31 + 128*m.b24*
                       m.b26*m.b30*m.b32 + 64*m.b24*m.b26*m.b31*m.b33 + 192*m.b24*m.b27*m.b28*m.b31 + 128*m.b24*m.b27*
                       m.b29*m.b32 + 64*m.b24*m.b27*m.b30*m.b33 + 64*m.b24*m.b28*m.b29*m.b33 + 448*m.b25*m.b26*m.b27*
                       m.b28 + 384*m.b25*m.b26*m.b28*m.b29 + 320*m.b25*m.b26*m.b29*m.b30 + 256*m.b25*m.b26*m.b30*m.b31
                        + 192*m.b25*m.b26*m.b31*m.b32 + 128*m.b25*m.b26*m.b32*m.b33 + 64*m.b25*m.b26*m.b33*m.b34 + 320*
                       m.b25*m.b27*m.b28*m.b30 + 256*m.b25*m.b27*m.b29*m.b31 + 192*m.b25*m.b27*m.b30*m.b32 + 128*m.b25*
                       m.b27*m.b31*m.b33 + 64*m.b25*m.b27*m.b32*m.b34 + 192*m.b25*m.b28*m.b29*m.b32 + 128*m.b25*m.b28*
                       m.b30*m.b33 + 64*m.b25*m.b28*m.b31*m.b34 + 64*m.b25*m.b29*m.b30*m.b34 + 448*m.b26*m.b27*m.b28*
                       m.b29 + 384*m.b26*m.b27*m.b29*m.b30 + 320*m.b26*m.b27*m.b30*m.b31 + 256*m.b26*m.b27*m.b31*m.b32
                        + 192*m.b26*m.b27*m.b32*m.b33 + 128*m.b26*m.b27*m.b33*m.b34 + 64*m.b26*m.b27*m.b34*m.b35 + 320*
                       m.b26*m.b28*m.b29*m.b31 + 256*m.b26*m.b28*m.b30*m.b32 + 192*m.b26*m.b28*m.b31*m.b33 + 128*m.b26*
                       m.b28*m.b32*m.b34 + 64*m.b26*m.b28*m.b33*m.b35 + 192*m.b26*m.b29*m.b30*m.b33 + 128*m.b26*m.b29*
                       m.b31*m.b34 + 64*m.b26*m.b29*m.b32*m.b35 + 64*m.b26*m.b30*m.b31*m.b35 + 448*m.b27*m.b28*m.b29*
                       m.b30 + 384*m.b27*m.b28*m.b30*m.b31 + 320*m.b27*m.b28*m.b31*m.b32 + 256*m.b27*m.b28*m.b32*m.b33
                        + 192*m.b27*m.b28*m.b33*m.b34 + 128*m.b27*m.b28*m.b34*m.b35 + 64*m.b27*m.b28*m.b35*m.b36 + 320*
                       m.b27*m.b29*m.b30*m.b32 + 256*m.b27*m.b29*m.b31*m.b33 + 192*m.b27*m.b29*m.b32*m.b34 + 128*m.b27*
                       m.b29*m.b33*m.b35 + 64*m.b27*m.b29*m.b34*m.b36 + 192*m.b27*m.b30*m.b31*m.b34 + 128*m.b27*m.b30*
                       m.b32*m.b35 + 64*m.b27*m.b30*m.b33*m.b36 + 64*m.b27*m.b31*m.b32*m.b36 + 448*m.b28*m.b29*m.b30*
                       m.b31 + 384*m.b28*m.b29*m.b31*m.b32 + 320*m.b28*m.b29*m.b32*m.b33 + 256*m.b28*m.b29*m.b33*m.b34
                        + 192*m.b28*m.b29*m.b34*m.b35 + 128*m.b28*m.b29*m.b35*m.b36 + 64*m.b28*m.b29*m.b36*m.b37 + 320*
                       m.b28*m.b30*m.b31*m.b33 + 256*m.b28*m.b30*m.b32*m.b34 + 192*m.b28*m.b30*m.b33*m.b35 + 128*m.b28*
                       m.b30*m.b34*m.b36 + 64*m.b28*m.b30*m.b35*m.b37 + 192*m.b28*m.b31*m.b32*m.b35 + 128*m.b28*m.b31*
                       m.b33*m.b36 + 64*m.b28*m.b31*m.b34*m.b37 + 64*m.b28*m.b32*m.b33*m.b37 + 448*m.b29*m.b30*m.b31*
                       m.b32 + 384*m.b29*m.b30*m.b32*m.b33 + 320*m.b29*m.b30*m.b33*m.b34 + 256*m.b29*m.b30*m.b34*m.b35
                        + 192*m.b29*m.b30*m.b35*m.b36 + 128*m.b29*m.b30*m.b36*m.b37 + 64*m.b29*m.b30*m.b37*m.b38 + 320*
                       m.b29*m.b31*m.b32*m.b34 + 256*m.b29*m.b31*m.b33*m.b35 + 192*m.b29*m.b31*m.b34*m.b36 + 128*m.b29*
                       m.b31*m.b35*m.b37 + 64*m.b29*m.b31*m.b36*m.b38 + 192*m.b29*m.b32*m.b33*m.b36 + 128*m.b29*m.b32*
                       m.b34*m.b37 + 64*m.b29*m.b32*m.b35*m.b38 + 64*m.b29*m.b33*m.b34*m.b38 + 448*m.b30*m.b31*m.b32*
                       m.b33 + 384*m.b30*m.b31*m.b33*m.b34 + 320*m.b30*m.b31*m.b34*m.b35 + 256*m.b30*m.b31*m.b35*m.b36
                        + 192*m.b30*m.b31*m.b36*m.b37 + 128*m.b30*m.b31*m.b37*m.b38 + 64*m.b30*m.b31*m.b38*m.b39 + 320*
                       m.b30*m.b32*m.b33*m.b35 + 256*m.b30*m.b32*m.b34*m.b36 + 192*m.b30*m.b32*m.b35*m.b37 + 128*m.b30*
                       m.b32*m.b36*m.b38 + 64*m.b30*m.b32*m.b37*m.b39 + 192*m.b30*m.b33*m.b34*m.b37 + 128*m.b30*m.b33*
                       m.b35*m.b38 + 64*m.b30*m.b33*m.b36*m.b39 + 64*m.b30*m.b34*m.b35*m.b39 + 448*m.b31*m.b32*m.b33*
                       m.b34 + 384*m.b31*m.b32*m.b34*m.b35 + 320*m.b31*m.b32*m.b35*m.b36 + 256*m.b31*m.b32*m.b36*m.b37
                        + 192*m.b31*m.b32*m.b37*m.b38 + 128*m.b31*m.b32*m.b38*m.b39 + 64*m.b31*m.b32*m.b39*m.b40 + 320*
                       m.b31*m.b33*m.b34*m.b36 + 256*m.b31*m.b33*m.b35*m.b37 + 192*m.b31*m.b33*m.b36*m.b38 + 128*m.b31*
                       m.b33*m.b37*m.b39 + 64*m.b31*m.b33*m.b38*m.b40 + 192*m.b31*m.b34*m.b35*m.b38 + 128*m.b31*m.b34*
                       m.b36*m.b39 + 64*m.b31*m.b34*m.b37*m.b40 + 64*m.b31*m.b35*m.b36*m.b40 + 384*m.b32*m.b33*m.b34*
                       m.b35 + 320*m.b32*m.b33*m.b35*m.b36 + 256*m.b32*m.b33*m.b36*m.b37 + 192*m.b32*m.b33*m.b37*m.b38
                        + 128*m.b32*m.b33*m.b38*m.b39 + 64*m.b32*m.b33*m.b39*m.b40 + 256*m.b32*m.b34*m.b35*m.b37 + 192*
                       m.b32*m.b34*m.b36*m.b38 + 128*m.b32*m.b34*m.b37*m.b39 + 64*m.b32*m.b34*m.b38*m.b40 + 128*m.b32*
                       m.b35*m.b36*m.b39 + 64*m.b32*m.b35*m.b37*m.b40 + 320*m.b33*m.b34*m.b35*m.b36 + 256*m.b33*m.b34*
                       m.b36*m.b37 + 192*m.b33*m.b34*m.b37*m.b38 + 128*m.b33*m.b34*m.b38*m.b39 + 64*m.b33*m.b34*m.b39*
                       m.b40 + 192*m.b33*m.b35*m.b36*m.b38 + 128*m.b33*m.b35*m.b37*m.b39 + 64*m.b33*m.b35*m.b38*m.b40 + 
                       64*m.b33*m.b36*m.b37*m.b40 + 256*m.b34*m.b35*m.b36*m.b37 + 192*m.b34*m.b35*m.b37*m.b38 + 128*
                       m.b34*m.b35*m.b38*m.b39 + 64*m.b34*m.b35*m.b39*m.b40 + 128*m.b34*m.b36*m.b37*m.b39 + 64*m.b34*
                       m.b36*m.b38*m.b40 + 192*m.b35*m.b36*m.b37*m.b38 + 128*m.b35*m.b36*m.b38*m.b39 + 64*m.b35*m.b36*
                       m.b39*m.b40 + 64*m.b35*m.b37*m.b38*m.b40 + 128*m.b36*m.b37*m.b38*m.b39 + 64*m.b36*m.b37*m.b39*
                       m.b40 + 64*m.b37*m.b38*m.b39*m.b40 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 
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
                       m.b18*m.b19 - 32*m.b11*m.b18*m.b20 - 32*m.b11*m.b19*m.b20 - 448*m.b12*m.b13*m.b14 - 576*m.b12*
                       m.b13*m.b15 - 448*m.b12*m.b13*m.b16 - 320*m.b12*m.b13*m.b17 - 224*m.b12*m.b13*m.b18 - 160*m.b12*
                       m.b13*m.b19 - 96*m.b12*m.b13*m.b20 - 32*m.b12*m.b13*m.b21 - 576*m.b12*m.b14*m.b15 - 256*m.b12*
                       m.b14*m.b16 - 320*m.b12*m.b14*m.b17 - 192*m.b12*m.b14*m.b18 - 128*m.b12*m.b14*m.b19 - 64*m.b12*
                       m.b14*m.b20 - 32*m.b12*m.b14*m.b21 - 448*m.b12*m.b15*m.b16 - 320*m.b12*m.b15*m.b17 - 64*m.b12*
                       m.b15*m.b18 - 96*m.b12*m.b15*m.b19 - 64*m.b12*m.b15*m.b20 - 32*m.b12*m.b15*m.b21 - 320*m.b12*
                       m.b16*m.b17 - 192*m.b12*m.b16*m.b18 - 96*m.b12*m.b16*m.b19 - 32*m.b12*m.b16*m.b21 - 224*m.b12*
                       m.b17*m.b18 - 128*m.b12*m.b17*m.b19 - 64*m.b12*m.b17*m.b20 - 32*m.b12*m.b17*m.b21 - 160*m.b12*
                       m.b18*m.b19 - 64*m.b12*m.b18*m.b20 - 32*m.b12*m.b18*m.b21 - 96*m.b12*m.b19*m.b20 - 32*m.b12*m.b19
                       *m.b21 - 32*m.b12*m.b20*m.b21 - 448*m.b13*m.b14*m.b15 - 576*m.b13*m.b14*m.b16 - 448*m.b13*m.b14*
                       m.b17 - 320*m.b13*m.b14*m.b18 - 224*m.b13*m.b14*m.b19 - 160*m.b13*m.b14*m.b20 - 96*m.b13*m.b14*
                       m.b21 - 32*m.b13*m.b14*m.b22 - 576*m.b13*m.b15*m.b16 - 256*m.b13*m.b15*m.b17 - 320*m.b13*m.b15*
                       m.b18 - 192*m.b13*m.b15*m.b19 - 128*m.b13*m.b15*m.b20 - 64*m.b13*m.b15*m.b21 - 32*m.b13*m.b15*
                       m.b22 - 448*m.b13*m.b16*m.b17 - 320*m.b13*m.b16*m.b18 - 64*m.b13*m.b16*m.b19 - 96*m.b13*m.b16*
                       m.b20 - 64*m.b13*m.b16*m.b21 - 32*m.b13*m.b16*m.b22 - 320*m.b13*m.b17*m.b18 - 192*m.b13*m.b17*
                       m.b19 - 96*m.b13*m.b17*m.b20 - 32*m.b13*m.b17*m.b22 - 224*m.b13*m.b18*m.b19 - 128*m.b13*m.b18*
                       m.b20 - 64*m.b13*m.b18*m.b21 - 32*m.b13*m.b18*m.b22 - 160*m.b13*m.b19*m.b20 - 64*m.b13*m.b19*
                       m.b21 - 32*m.b13*m.b19*m.b22 - 96*m.b13*m.b20*m.b21 - 32*m.b13*m.b20*m.b22 - 32*m.b13*m.b21*m.b22
                        - 448*m.b14*m.b15*m.b16 - 576*m.b14*m.b15*m.b17 - 448*m.b14*m.b15*m.b18 - 320*m.b14*m.b15*m.b19
                        - 224*m.b14*m.b15*m.b20 - 160*m.b14*m.b15*m.b21 - 96*m.b14*m.b15*m.b22 - 32*m.b14*m.b15*m.b23 - 
                       576*m.b14*m.b16*m.b17 - 256*m.b14*m.b16*m.b18 - 320*m.b14*m.b16*m.b19 - 192*m.b14*m.b16*m.b20 - 
                       128*m.b14*m.b16*m.b21 - 64*m.b14*m.b16*m.b22 - 32*m.b14*m.b16*m.b23 - 448*m.b14*m.b17*m.b18 - 320
                       *m.b14*m.b17*m.b19 - 64*m.b14*m.b17*m.b20 - 96*m.b14*m.b17*m.b21 - 64*m.b14*m.b17*m.b22 - 32*
                       m.b14*m.b17*m.b23 - 320*m.b14*m.b18*m.b19 - 192*m.b14*m.b18*m.b20 - 96*m.b14*m.b18*m.b21 - 32*
                       m.b14*m.b18*m.b23 - 224*m.b14*m.b19*m.b20 - 128*m.b14*m.b19*m.b21 - 64*m.b14*m.b19*m.b22 - 32*
                       m.b14*m.b19*m.b23 - 160*m.b14*m.b20*m.b21 - 64*m.b14*m.b20*m.b22 - 32*m.b14*m.b20*m.b23 - 96*
                       m.b14*m.b21*m.b22 - 32*m.b14*m.b21*m.b23 - 32*m.b14*m.b22*m.b23 - 448*m.b15*m.b16*m.b17 - 576*
                       m.b15*m.b16*m.b18 - 448*m.b15*m.b16*m.b19 - 320*m.b15*m.b16*m.b20 - 224*m.b15*m.b16*m.b21 - 160*
                       m.b15*m.b16*m.b22 - 96*m.b15*m.b16*m.b23 - 32*m.b15*m.b16*m.b24 - 576*m.b15*m.b17*m.b18 - 256*
                       m.b15*m.b17*m.b19 - 320*m.b15*m.b17*m.b20 - 192*m.b15*m.b17*m.b21 - 128*m.b15*m.b17*m.b22 - 64*
                       m.b15*m.b17*m.b23 - 32*m.b15*m.b17*m.b24 - 448*m.b15*m.b18*m.b19 - 320*m.b15*m.b18*m.b20 - 64*
                       m.b15*m.b18*m.b21 - 96*m.b15*m.b18*m.b22 - 64*m.b15*m.b18*m.b23 - 32*m.b15*m.b18*m.b24 - 320*
                       m.b15*m.b19*m.b20 - 192*m.b15*m.b19*m.b21 - 96*m.b15*m.b19*m.b22 - 32*m.b15*m.b19*m.b24 - 224*
                       m.b15*m.b20*m.b21 - 128*m.b15*m.b20*m.b22 - 64*m.b15*m.b20*m.b23 - 32*m.b15*m.b20*m.b24 - 160*
                       m.b15*m.b21*m.b22 - 64*m.b15*m.b21*m.b23 - 32*m.b15*m.b21*m.b24 - 96*m.b15*m.b22*m.b23 - 32*m.b15
                       *m.b22*m.b24 - 32*m.b15*m.b23*m.b24 - 448*m.b16*m.b17*m.b18 - 576*m.b16*m.b17*m.b19 - 448*m.b16*
                       m.b17*m.b20 - 320*m.b16*m.b17*m.b21 - 224*m.b16*m.b17*m.b22 - 160*m.b16*m.b17*m.b23 - 96*m.b16*
                       m.b17*m.b24 - 32*m.b16*m.b17*m.b25 - 576*m.b16*m.b18*m.b19 - 256*m.b16*m.b18*m.b20 - 320*m.b16*
                       m.b18*m.b21 - 192*m.b16*m.b18*m.b22 - 128*m.b16*m.b18*m.b23 - 64*m.b16*m.b18*m.b24 - 32*m.b16*
                       m.b18*m.b25 - 448*m.b16*m.b19*m.b20 - 320*m.b16*m.b19*m.b21 - 64*m.b16*m.b19*m.b22 - 96*m.b16*
                       m.b19*m.b23 - 64*m.b16*m.b19*m.b24 - 32*m.b16*m.b19*m.b25 - 320*m.b16*m.b20*m.b21 - 192*m.b16*
                       m.b20*m.b22 - 96*m.b16*m.b20*m.b23 - 32*m.b16*m.b20*m.b25 - 224*m.b16*m.b21*m.b22 - 128*m.b16*
                       m.b21*m.b23 - 64*m.b16*m.b21*m.b24 - 32*m.b16*m.b21*m.b25 - 160*m.b16*m.b22*m.b23 - 64*m.b16*
                       m.b22*m.b24 - 32*m.b16*m.b22*m.b25 - 96*m.b16*m.b23*m.b24 - 32*m.b16*m.b23*m.b25 - 32*m.b16*m.b24
                       *m.b25 - 448*m.b17*m.b18*m.b19 - 576*m.b17*m.b18*m.b20 - 448*m.b17*m.b18*m.b21 - 320*m.b17*m.b18*
                       m.b22 - 224*m.b17*m.b18*m.b23 - 160*m.b17*m.b18*m.b24 - 96*m.b17*m.b18*m.b25 - 32*m.b17*m.b18*
                       m.b26 - 576*m.b17*m.b19*m.b20 - 256*m.b17*m.b19*m.b21 - 320*m.b17*m.b19*m.b22 - 192*m.b17*m.b19*
                       m.b23 - 128*m.b17*m.b19*m.b24 - 64*m.b17*m.b19*m.b25 - 32*m.b17*m.b19*m.b26 - 448*m.b17*m.b20*
                       m.b21 - 320*m.b17*m.b20*m.b22 - 64*m.b17*m.b20*m.b23 - 96*m.b17*m.b20*m.b24 - 64*m.b17*m.b20*
                       m.b25 - 32*m.b17*m.b20*m.b26 - 320*m.b17*m.b21*m.b22 - 192*m.b17*m.b21*m.b23 - 96*m.b17*m.b21*
                       m.b24 - 32*m.b17*m.b21*m.b26 - 224*m.b17*m.b22*m.b23 - 128*m.b17*m.b22*m.b24 - 64*m.b17*m.b22*
                       m.b25 - 32*m.b17*m.b22*m.b26 - 160*m.b17*m.b23*m.b24 - 64*m.b17*m.b23*m.b25 - 32*m.b17*m.b23*
                       m.b26 - 96*m.b17*m.b24*m.b25 - 32*m.b17*m.b24*m.b26 - 32*m.b17*m.b25*m.b26 - 448*m.b18*m.b19*
                       m.b20 - 576*m.b18*m.b19*m.b21 - 448*m.b18*m.b19*m.b22 - 320*m.b18*m.b19*m.b23 - 224*m.b18*m.b19*
                       m.b24 - 160*m.b18*m.b19*m.b25 - 96*m.b18*m.b19*m.b26 - 32*m.b18*m.b19*m.b27 - 576*m.b18*m.b20*
                       m.b21 - 256*m.b18*m.b20*m.b22 - 320*m.b18*m.b20*m.b23 - 192*m.b18*m.b20*m.b24 - 128*m.b18*m.b20*
                       m.b25 - 64*m.b18*m.b20*m.b26 - 32*m.b18*m.b20*m.b27 - 448*m.b18*m.b21*m.b22 - 320*m.b18*m.b21*
                       m.b23 - 64*m.b18*m.b21*m.b24 - 96*m.b18*m.b21*m.b25 - 64*m.b18*m.b21*m.b26 - 32*m.b18*m.b21*m.b27
                        - 320*m.b18*m.b22*m.b23 - 192*m.b18*m.b22*m.b24 - 96*m.b18*m.b22*m.b25 - 32*m.b18*m.b22*m.b27 - 
                       224*m.b18*m.b23*m.b24 - 128*m.b18*m.b23*m.b25 - 64*m.b18*m.b23*m.b26 - 32*m.b18*m.b23*m.b27 - 160
                       *m.b18*m.b24*m.b25 - 64*m.b18*m.b24*m.b26 - 32*m.b18*m.b24*m.b27 - 96*m.b18*m.b25*m.b26 - 32*
                       m.b18*m.b25*m.b27 - 32*m.b18*m.b26*m.b27 - 448*m.b19*m.b20*m.b21 - 576*m.b19*m.b20*m.b22 - 448*
                       m.b19*m.b20*m.b23 - 320*m.b19*m.b20*m.b24 - 224*m.b19*m.b20*m.b25 - 160*m.b19*m.b20*m.b26 - 96*
                       m.b19*m.b20*m.b27 - 32*m.b19*m.b20*m.b28 - 576*m.b19*m.b21*m.b22 - 256*m.b19*m.b21*m.b23 - 320*
                       m.b19*m.b21*m.b24 - 192*m.b19*m.b21*m.b25 - 128*m.b19*m.b21*m.b26 - 64*m.b19*m.b21*m.b27 - 32*
                       m.b19*m.b21*m.b28 - 448*m.b19*m.b22*m.b23 - 320*m.b19*m.b22*m.b24 - 64*m.b19*m.b22*m.b25 - 96*
                       m.b19*m.b22*m.b26 - 64*m.b19*m.b22*m.b27 - 32*m.b19*m.b22*m.b28 - 320*m.b19*m.b23*m.b24 - 192*
                       m.b19*m.b23*m.b25 - 96*m.b19*m.b23*m.b26 - 32*m.b19*m.b23*m.b28 - 224*m.b19*m.b24*m.b25 - 128*
                       m.b19*m.b24*m.b26 - 64*m.b19*m.b24*m.b27 - 32*m.b19*m.b24*m.b28 - 160*m.b19*m.b25*m.b26 - 64*
                       m.b19*m.b25*m.b27 - 32*m.b19*m.b25*m.b28 - 96*m.b19*m.b26*m.b27 - 32*m.b19*m.b26*m.b28 - 32*m.b19
                       *m.b27*m.b28 - 448*m.b20*m.b21*m.b22 - 576*m.b20*m.b21*m.b23 - 448*m.b20*m.b21*m.b24 - 320*m.b20*
                       m.b21*m.b25 - 224*m.b20*m.b21*m.b26 - 160*m.b20*m.b21*m.b27 - 96*m.b20*m.b21*m.b28 - 32*m.b20*
                       m.b21*m.b29 - 576*m.b20*m.b22*m.b23 - 256*m.b20*m.b22*m.b24 - 320*m.b20*m.b22*m.b25 - 192*m.b20*
                       m.b22*m.b26 - 128*m.b20*m.b22*m.b27 - 64*m.b20*m.b22*m.b28 - 32*m.b20*m.b22*m.b29 - 448*m.b20*
                       m.b23*m.b24 - 320*m.b20*m.b23*m.b25 - 64*m.b20*m.b23*m.b26 - 96*m.b20*m.b23*m.b27 - 64*m.b20*
                       m.b23*m.b28 - 32*m.b20*m.b23*m.b29 - 320*m.b20*m.b24*m.b25 - 192*m.b20*m.b24*m.b26 - 96*m.b20*
                       m.b24*m.b27 - 32*m.b20*m.b24*m.b29 - 224*m.b20*m.b25*m.b26 - 128*m.b20*m.b25*m.b27 - 64*m.b20*
                       m.b25*m.b28 - 32*m.b20*m.b25*m.b29 - 160*m.b20*m.b26*m.b27 - 64*m.b20*m.b26*m.b28 - 32*m.b20*
                       m.b26*m.b29 - 96*m.b20*m.b27*m.b28 - 32*m.b20*m.b27*m.b29 - 32*m.b20*m.b28*m.b29 - 448*m.b21*
                       m.b22*m.b23 - 576*m.b21*m.b22*m.b24 - 448*m.b21*m.b22*m.b25 - 320*m.b21*m.b22*m.b26 - 224*m.b21*
                       m.b22*m.b27 - 160*m.b21*m.b22*m.b28 - 96*m.b21*m.b22*m.b29 - 32*m.b21*m.b22*m.b30 - 576*m.b21*
                       m.b23*m.b24 - 256*m.b21*m.b23*m.b25 - 320*m.b21*m.b23*m.b26 - 192*m.b21*m.b23*m.b27 - 128*m.b21*
                       m.b23*m.b28 - 64*m.b21*m.b23*m.b29 - 32*m.b21*m.b23*m.b30 - 448*m.b21*m.b24*m.b25 - 320*m.b21*
                       m.b24*m.b26 - 64*m.b21*m.b24*m.b27 - 96*m.b21*m.b24*m.b28 - 64*m.b21*m.b24*m.b29 - 32*m.b21*m.b24
                       *m.b30 - 320*m.b21*m.b25*m.b26 - 192*m.b21*m.b25*m.b27 - 96*m.b21*m.b25*m.b28 - 32*m.b21*m.b25*
                       m.b30 - 224*m.b21*m.b26*m.b27 - 128*m.b21*m.b26*m.b28 - 64*m.b21*m.b26*m.b29 - 32*m.b21*m.b26*
                       m.b30 - 160*m.b21*m.b27*m.b28 - 64*m.b21*m.b27*m.b29 - 32*m.b21*m.b27*m.b30 - 96*m.b21*m.b28*
                       m.b29 - 32*m.b21*m.b28*m.b30 - 32*m.b21*m.b29*m.b30 - 448*m.b22*m.b23*m.b24 - 576*m.b22*m.b23*
                       m.b25 - 448*m.b22*m.b23*m.b26 - 320*m.b22*m.b23*m.b27 - 224*m.b22*m.b23*m.b28 - 160*m.b22*m.b23*
                       m.b29 - 96*m.b22*m.b23*m.b30 - 32*m.b22*m.b23*m.b31 - 576*m.b22*m.b24*m.b25 - 256*m.b22*m.b24*
                       m.b26 - 320*m.b22*m.b24*m.b27 - 192*m.b22*m.b24*m.b28 - 128*m.b22*m.b24*m.b29 - 64*m.b22*m.b24*
                       m.b30 - 32*m.b22*m.b24*m.b31 - 448*m.b22*m.b25*m.b26 - 320*m.b22*m.b25*m.b27 - 64*m.b22*m.b25*
                       m.b28 - 96*m.b22*m.b25*m.b29 - 64*m.b22*m.b25*m.b30 - 32*m.b22*m.b25*m.b31 - 320*m.b22*m.b26*
                       m.b27 - 192*m.b22*m.b26*m.b28 - 96*m.b22*m.b26*m.b29 - 32*m.b22*m.b26*m.b31 - 224*m.b22*m.b27*
                       m.b28 - 128*m.b22*m.b27*m.b29 - 64*m.b22*m.b27*m.b30 - 32*m.b22*m.b27*m.b31 - 160*m.b22*m.b28*
                       m.b29 - 64*m.b22*m.b28*m.b30 - 32*m.b22*m.b28*m.b31 - 96*m.b22*m.b29*m.b30 - 32*m.b22*m.b29*m.b31
                        - 32*m.b22*m.b30*m.b31 - 448*m.b23*m.b24*m.b25 - 576*m.b23*m.b24*m.b26 - 448*m.b23*m.b24*m.b27
                        - 320*m.b23*m.b24*m.b28 - 224*m.b23*m.b24*m.b29 - 160*m.b23*m.b24*m.b30 - 96*m.b23*m.b24*m.b31
                        - 32*m.b23*m.b24*m.b32 - 576*m.b23*m.b25*m.b26 - 256*m.b23*m.b25*m.b27 - 320*m.b23*m.b25*m.b28
                        - 192*m.b23*m.b25*m.b29 - 128*m.b23*m.b25*m.b30 - 64*m.b23*m.b25*m.b31 - 32*m.b23*m.b25*m.b32 - 
                       448*m.b23*m.b26*m.b27 - 320*m.b23*m.b26*m.b28 - 64*m.b23*m.b26*m.b29 - 96*m.b23*m.b26*m.b30 - 64*
                       m.b23*m.b26*m.b31 - 32*m.b23*m.b26*m.b32 - 320*m.b23*m.b27*m.b28 - 192*m.b23*m.b27*m.b29 - 96*
                       m.b23*m.b27*m.b30 - 32*m.b23*m.b27*m.b32 - 224*m.b23*m.b28*m.b29 - 128*m.b23*m.b28*m.b30 - 64*
                       m.b23*m.b28*m.b31 - 32*m.b23*m.b28*m.b32 - 160*m.b23*m.b29*m.b30 - 64*m.b23*m.b29*m.b31 - 32*
                       m.b23*m.b29*m.b32 - 96*m.b23*m.b30*m.b31 - 32*m.b23*m.b30*m.b32 - 32*m.b23*m.b31*m.b32 - 448*
                       m.b24*m.b25*m.b26 - 576*m.b24*m.b25*m.b27 - 448*m.b24*m.b25*m.b28 - 320*m.b24*m.b25*m.b29 - 224*
                       m.b24*m.b25*m.b30 - 160*m.b24*m.b25*m.b31 - 96*m.b24*m.b25*m.b32 - 32*m.b24*m.b25*m.b33 - 576*
                       m.b24*m.b26*m.b27 - 256*m.b24*m.b26*m.b28 - 320*m.b24*m.b26*m.b29 - 192*m.b24*m.b26*m.b30 - 128*
                       m.b24*m.b26*m.b31 - 64*m.b24*m.b26*m.b32 - 32*m.b24*m.b26*m.b33 - 448*m.b24*m.b27*m.b28 - 320*
                       m.b24*m.b27*m.b29 - 64*m.b24*m.b27*m.b30 - 96*m.b24*m.b27*m.b31 - 64*m.b24*m.b27*m.b32 - 32*m.b24
                       *m.b27*m.b33 - 320*m.b24*m.b28*m.b29 - 192*m.b24*m.b28*m.b30 - 96*m.b24*m.b28*m.b31 - 32*m.b24*
                       m.b28*m.b33 - 224*m.b24*m.b29*m.b30 - 128*m.b24*m.b29*m.b31 - 64*m.b24*m.b29*m.b32 - 32*m.b24*
                       m.b29*m.b33 - 160*m.b24*m.b30*m.b31 - 64*m.b24*m.b30*m.b32 - 32*m.b24*m.b30*m.b33 - 96*m.b24*
                       m.b31*m.b32 - 32*m.b24*m.b31*m.b33 - 32*m.b24*m.b32*m.b33 - 448*m.b25*m.b26*m.b27 - 576*m.b25*
                       m.b26*m.b28 - 448*m.b25*m.b26*m.b29 - 320*m.b25*m.b26*m.b30 - 224*m.b25*m.b26*m.b31 - 160*m.b25*
                       m.b26*m.b32 - 96*m.b25*m.b26*m.b33 - 32*m.b25*m.b26*m.b34 - 576*m.b25*m.b27*m.b28 - 256*m.b25*
                       m.b27*m.b29 - 320*m.b25*m.b27*m.b30 - 192*m.b25*m.b27*m.b31 - 128*m.b25*m.b27*m.b32 - 64*m.b25*
                       m.b27*m.b33 - 32*m.b25*m.b27*m.b34 - 448*m.b25*m.b28*m.b29 - 320*m.b25*m.b28*m.b30 - 64*m.b25*
                       m.b28*m.b31 - 96*m.b25*m.b28*m.b32 - 64*m.b25*m.b28*m.b33 - 32*m.b25*m.b28*m.b34 - 320*m.b25*
                       m.b29*m.b30 - 192*m.b25*m.b29*m.b31 - 96*m.b25*m.b29*m.b32 - 32*m.b25*m.b29*m.b34 - 224*m.b25*
                       m.b30*m.b31 - 128*m.b25*m.b30*m.b32 - 64*m.b25*m.b30*m.b33 - 32*m.b25*m.b30*m.b34 - 160*m.b25*
                       m.b31*m.b32 - 64*m.b25*m.b31*m.b33 - 32*m.b25*m.b31*m.b34 - 96*m.b25*m.b32*m.b33 - 32*m.b25*m.b32
                       *m.b34 - 32*m.b25*m.b33*m.b34 - 448*m.b26*m.b27*m.b28 - 576*m.b26*m.b27*m.b29 - 448*m.b26*m.b27*
                       m.b30 - 320*m.b26*m.b27*m.b31 - 224*m.b26*m.b27*m.b32 - 160*m.b26*m.b27*m.b33 - 96*m.b26*m.b27*
                       m.b34 - 32*m.b26*m.b27*m.b35 - 576*m.b26*m.b28*m.b29 - 256*m.b26*m.b28*m.b30 - 320*m.b26*m.b28*
                       m.b31 - 192*m.b26*m.b28*m.b32 - 128*m.b26*m.b28*m.b33 - 64*m.b26*m.b28*m.b34 - 32*m.b26*m.b28*
                       m.b35 - 448*m.b26*m.b29*m.b30 - 320*m.b26*m.b29*m.b31 - 64*m.b26*m.b29*m.b32 - 96*m.b26*m.b29*
                       m.b33 - 64*m.b26*m.b29*m.b34 - 32*m.b26*m.b29*m.b35 - 320*m.b26*m.b30*m.b31 - 192*m.b26*m.b30*
                       m.b32 - 96*m.b26*m.b30*m.b33 - 32*m.b26*m.b30*m.b35 - 224*m.b26*m.b31*m.b32 - 128*m.b26*m.b31*
                       m.b33 - 64*m.b26*m.b31*m.b34 - 32*m.b26*m.b31*m.b35 - 160*m.b26*m.b32*m.b33 - 64*m.b26*m.b32*
                       m.b34 - 32*m.b26*m.b32*m.b35 - 96*m.b26*m.b33*m.b34 - 32*m.b26*m.b33*m.b35 - 32*m.b26*m.b34*m.b35
                        - 448*m.b27*m.b28*m.b29 - 576*m.b27*m.b28*m.b30 - 448*m.b27*m.b28*m.b31 - 320*m.b27*m.b28*m.b32
                        - 224*m.b27*m.b28*m.b33 - 160*m.b27*m.b28*m.b34 - 96*m.b27*m.b28*m.b35 - 32*m.b27*m.b28*m.b36 - 
                       576*m.b27*m.b29*m.b30 - 256*m.b27*m.b29*m.b31 - 320*m.b27*m.b29*m.b32 - 192*m.b27*m.b29*m.b33 - 
                       128*m.b27*m.b29*m.b34 - 64*m.b27*m.b29*m.b35 - 32*m.b27*m.b29*m.b36 - 448*m.b27*m.b30*m.b31 - 320
                       *m.b27*m.b30*m.b32 - 64*m.b27*m.b30*m.b33 - 96*m.b27*m.b30*m.b34 - 64*m.b27*m.b30*m.b35 - 32*
                       m.b27*m.b30*m.b36 - 320*m.b27*m.b31*m.b32 - 192*m.b27*m.b31*m.b33 - 96*m.b27*m.b31*m.b34 - 32*
                       m.b27*m.b31*m.b36 - 224*m.b27*m.b32*m.b33 - 128*m.b27*m.b32*m.b34 - 64*m.b27*m.b32*m.b35 - 32*
                       m.b27*m.b32*m.b36 - 160*m.b27*m.b33*m.b34 - 64*m.b27*m.b33*m.b35 - 32*m.b27*m.b33*m.b36 - 96*
                       m.b27*m.b34*m.b35 - 32*m.b27*m.b34*m.b36 - 32*m.b27*m.b35*m.b36 - 448*m.b28*m.b29*m.b30 - 576*
                       m.b28*m.b29*m.b31 - 448*m.b28*m.b29*m.b32 - 320*m.b28*m.b29*m.b33 - 224*m.b28*m.b29*m.b34 - 160*
                       m.b28*m.b29*m.b35 - 96*m.b28*m.b29*m.b36 - 32*m.b28*m.b29*m.b37 - 576*m.b28*m.b30*m.b31 - 256*
                       m.b28*m.b30*m.b32 - 320*m.b28*m.b30*m.b33 - 192*m.b28*m.b30*m.b34 - 128*m.b28*m.b30*m.b35 - 64*
                       m.b28*m.b30*m.b36 - 32*m.b28*m.b30*m.b37 - 448*m.b28*m.b31*m.b32 - 320*m.b28*m.b31*m.b33 - 64*
                       m.b28*m.b31*m.b34 - 96*m.b28*m.b31*m.b35 - 64*m.b28*m.b31*m.b36 - 32*m.b28*m.b31*m.b37 - 320*
                       m.b28*m.b32*m.b33 - 192*m.b28*m.b32*m.b34 - 96*m.b28*m.b32*m.b35 - 32*m.b28*m.b32*m.b37 - 224*
                       m.b28*m.b33*m.b34 - 128*m.b28*m.b33*m.b35 - 64*m.b28*m.b33*m.b36 - 32*m.b28*m.b33*m.b37 - 160*
                       m.b28*m.b34*m.b35 - 64*m.b28*m.b34*m.b36 - 32*m.b28*m.b34*m.b37 - 96*m.b28*m.b35*m.b36 - 32*m.b28
                       *m.b35*m.b37 - 32*m.b28*m.b36*m.b37 - 448*m.b29*m.b30*m.b31 - 576*m.b29*m.b30*m.b32 - 448*m.b29*
                       m.b30*m.b33 - 320*m.b29*m.b30*m.b34 - 224*m.b29*m.b30*m.b35 - 160*m.b29*m.b30*m.b36 - 96*m.b29*
                       m.b30*m.b37 - 32*m.b29*m.b30*m.b38 - 576*m.b29*m.b31*m.b32 - 256*m.b29*m.b31*m.b33 - 320*m.b29*
                       m.b31*m.b34 - 192*m.b29*m.b31*m.b35 - 128*m.b29*m.b31*m.b36 - 64*m.b29*m.b31*m.b37 - 32*m.b29*
                       m.b31*m.b38 - 448*m.b29*m.b32*m.b33 - 320*m.b29*m.b32*m.b34 - 64*m.b29*m.b32*m.b35 - 96*m.b29*
                       m.b32*m.b36 - 64*m.b29*m.b32*m.b37 - 32*m.b29*m.b32*m.b38 - 320*m.b29*m.b33*m.b34 - 192*m.b29*
                       m.b33*m.b35 - 96*m.b29*m.b33*m.b36 - 32*m.b29*m.b33*m.b38 - 224*m.b29*m.b34*m.b35 - 128*m.b29*
                       m.b34*m.b36 - 64*m.b29*m.b34*m.b37 - 32*m.b29*m.b34*m.b38 - 160*m.b29*m.b35*m.b36 - 64*m.b29*
                       m.b35*m.b37 - 32*m.b29*m.b35*m.b38 - 96*m.b29*m.b36*m.b37 - 32*m.b29*m.b36*m.b38 - 32*m.b29*m.b37
                       *m.b38 - 448*m.b30*m.b31*m.b32 - 576*m.b30*m.b31*m.b33 - 448*m.b30*m.b31*m.b34 - 320*m.b30*m.b31*
                       m.b35 - 224*m.b30*m.b31*m.b36 - 160*m.b30*m.b31*m.b37 - 96*m.b30*m.b31*m.b38 - 32*m.b30*m.b31*
                       m.b39 - 576*m.b30*m.b32*m.b33 - 256*m.b30*m.b32*m.b34 - 320*m.b30*m.b32*m.b35 - 192*m.b30*m.b32*
                       m.b36 - 128*m.b30*m.b32*m.b37 - 64*m.b30*m.b32*m.b38 - 32*m.b30*m.b32*m.b39 - 448*m.b30*m.b33*
                       m.b34 - 320*m.b30*m.b33*m.b35 - 64*m.b30*m.b33*m.b36 - 96*m.b30*m.b33*m.b37 - 64*m.b30*m.b33*
                       m.b38 - 32*m.b30*m.b33*m.b39 - 320*m.b30*m.b34*m.b35 - 192*m.b30*m.b34*m.b36 - 96*m.b30*m.b34*
                       m.b37 - 32*m.b30*m.b34*m.b39 - 224*m.b30*m.b35*m.b36 - 128*m.b30*m.b35*m.b37 - 64*m.b30*m.b35*
                       m.b38 - 32*m.b30*m.b35*m.b39 - 160*m.b30*m.b36*m.b37 - 64*m.b30*m.b36*m.b38 - 32*m.b30*m.b36*
                       m.b39 - 96*m.b30*m.b37*m.b38 - 32*m.b30*m.b37*m.b39 - 32*m.b30*m.b38*m.b39 - 448*m.b31*m.b32*
                       m.b33 - 576*m.b31*m.b32*m.b34 - 448*m.b31*m.b32*m.b35 - 320*m.b31*m.b32*m.b36 - 224*m.b31*m.b32*
                       m.b37 - 160*m.b31*m.b32*m.b38 - 96*m.b31*m.b32*m.b39 - 32*m.b31*m.b32*m.b40 - 576*m.b31*m.b33*
                       m.b34 - 256*m.b31*m.b33*m.b35 - 320*m.b31*m.b33*m.b36 - 192*m.b31*m.b33*m.b37 - 128*m.b31*m.b33*
                       m.b38 - 64*m.b31*m.b33*m.b39 - 32*m.b31*m.b33*m.b40 - 448*m.b31*m.b34*m.b35 - 320*m.b31*m.b34*
                       m.b36 - 64*m.b31*m.b34*m.b37 - 96*m.b31*m.b34*m.b38 - 64*m.b31*m.b34*m.b39 - 32*m.b31*m.b34*m.b40
                        - 320*m.b31*m.b35*m.b36 - 192*m.b31*m.b35*m.b37 - 96*m.b31*m.b35*m.b38 - 32*m.b31*m.b35*m.b40 - 
                       224*m.b31*m.b36*m.b37 - 128*m.b31*m.b36*m.b38 - 64*m.b31*m.b36*m.b39 - 32*m.b31*m.b36*m.b40 - 160
                       *m.b31*m.b37*m.b38 - 64*m.b31*m.b37*m.b39 - 32*m.b31*m.b37*m.b40 - 96*m.b31*m.b38*m.b39 - 32*
                       m.b31*m.b38*m.b40 - 32*m.b31*m.b39*m.b40 - 416*m.b32*m.b33*m.b34 - 512*m.b32*m.b33*m.b35 - 384*
                       m.b32*m.b33*m.b36 - 256*m.b32*m.b33*m.b37 - 160*m.b32*m.b33*m.b38 - 96*m.b32*m.b33*m.b39 - 32*
                       m.b32*m.b33*m.b40 - 512*m.b32*m.b34*m.b35 - 224*m.b32*m.b34*m.b36 - 256*m.b32*m.b34*m.b37 - 128*
                       m.b32*m.b34*m.b38 - 64*m.b32*m.b34*m.b39 - 32*m.b32*m.b34*m.b40 - 384*m.b32*m.b35*m.b36 - 256*
                       m.b32*m.b35*m.b37 - 32*m.b32*m.b35*m.b38 - 64*m.b32*m.b35*m.b39 - 32*m.b32*m.b35*m.b40 - 256*
                       m.b32*m.b36*m.b37 - 160*m.b32*m.b36*m.b38 - 64*m.b32*m.b36*m.b39 - 192*m.b32*m.b37*m.b38 - 96*
                       m.b32*m.b37*m.b39 - 32*m.b32*m.b37*m.b40 - 128*m.b32*m.b38*m.b39 - 32*m.b32*m.b38*m.b40 - 64*
                       m.b32*m.b39*m.b40 - 352*m.b33*m.b34*m.b35 - 448*m.b33*m.b34*m.b36 - 320*m.b33*m.b34*m.b37 - 192*
                       m.b33*m.b34*m.b38 - 96*m.b33*m.b34*m.b39 - 32*m.b33*m.b34*m.b40 - 416*m.b33*m.b35*m.b36 - 192*
                       m.b33*m.b35*m.b37 - 192*m.b33*m.b35*m.b38 - 64*m.b33*m.b35*m.b39 - 32*m.b33*m.b35*m.b40 - 288*
                       m.b33*m.b36*m.b37 - 192*m.b33*m.b36*m.b38 - 32*m.b33*m.b36*m.b39 - 32*m.b33*m.b36*m.b40 - 192*
                       m.b33*m.b37*m.b38 - 128*m.b33*m.b37*m.b39 - 32*m.b33*m.b37*m.b40 - 128*m.b33*m.b38*m.b39 - 64*
                       m.b33*m.b38*m.b40 - 64*m.b33*m.b39*m.b40 - 288*m.b34*m.b35*m.b36 - 352*m.b34*m.b35*m.b37 - 256*
                       m.b34*m.b35*m.b38 - 128*m.b34*m.b35*m.b39 - 32*m.b34*m.b35*m.b40 - 320*m.b34*m.b36*m.b37 - 128*
                       m.b34*m.b36*m.b38 - 128*m.b34*m.b36*m.b39 - 32*m.b34*m.b36*m.b40 - 192*m.b34*m.b37*m.b38 - 128*
                       m.b34*m.b37*m.b39 - 32*m.b34*m.b37*m.b40 - 128*m.b34*m.b38*m.b39 - 64*m.b34*m.b38*m.b40 - 64*
                       m.b34*m.b39*m.b40 - 224*m.b35*m.b36*m.b37 - 256*m.b35*m.b36*m.b38 - 160*m.b35*m.b36*m.b39 - 64*
                       m.b35*m.b36*m.b40 - 224*m.b35*m.b37*m.b38 - 64*m.b35*m.b37*m.b39 - 64*m.b35*m.b37*m.b40 - 128*
                       m.b35*m.b38*m.b39 - 64*m.b35*m.b38*m.b40 - 64*m.b35*m.b39*m.b40 - 160*m.b36*m.b37*m.b38 - 160*
                       m.b36*m.b37*m.b39 - 64*m.b36*m.b37*m.b40 - 128*m.b36*m.b38*m.b39 - 32*m.b36*m.b38*m.b40 - 64*
                       m.b36*m.b39*m.b40 - 96*m.b37*m.b38*m.b39 - 64*m.b37*m.b38*m.b40 - 64*m.b37*m.b39*m.b40 - 32*m.b38
                       *m.b39*m.b40 + 112*m.b1*m.b2 + 104*m.b1*m.b3 + 96*m.b1*m.b4 + 88*m.b1*m.b5 + 96*m.b1*m.b6 + 88*
                       m.b1*m.b7 + 80*m.b1*m.b8 + 72*m.b1*m.b9 + 64*m.b1*m.b10 + 224*m.b2*m.b3 + 224*m.b2*m.b4 + 208*
                       m.b2*m.b5 + 192*m.b2*m.b6 + 208*m.b2*m.b7 + 192*m.b2*m.b8 + 176*m.b2*m.b9 + 144*m.b2*m.b10 + 64*
                       m.b2*m.b11 + 352*m.b3*m.b4 + 344*m.b3*m.b5 + 336*m.b3*m.b6 + 328*m.b3*m.b7 + 336*m.b3*m.b8 + 296*
                       m.b3*m.b9 + 256*m.b3*m.b10 + 144*m.b3*m.b11 + 64*m.b3*m.b12 + 496*m.b4*m.b5 + 480*m.b4*m.b6 + 464
                       *m.b4*m.b7 + 464*m.b4*m.b8 + 448*m.b4*m.b9 + 384*m.b4*m.b10 + 256*m.b4*m.b11 + 144*m.b4*m.b12 + 
                       64*m.b4*m.b13 + 656*m.b5*m.b6 + 616*m.b5*m.b7 + 592*m.b5*m.b8 + 568*m.b5*m.b9 + 544*m.b5*m.b10 + 
                       384*m.b5*m.b11 + 256*m.b5*m.b12 + 144*m.b5*m.b13 + 64*m.b5*m.b14 + 800*m.b6*m.b7 + 736*m.b6*m.b8
                        + 704*m.b6*m.b9 + 656*m.b6*m.b10 + 544*m.b6*m.b11 + 384*m.b6*m.b12 + 256*m.b6*m.b13 + 144*m.b6*
                       m.b14 + 64*m.b6*m.b15 + 928*m.b7*m.b8 + 856*m.b7*m.b9 + 800*m.b7*m.b10 + 656*m.b7*m.b11 + 544*
                       m.b7*m.b12 + 384*m.b7*m.b13 + 256*m.b7*m.b14 + 144*m.b7*m.b15 + 64*m.b7*m.b16 + 1040*m.b8*m.b9 + 
                       960*m.b8*m.b10 + 800*m.b8*m.b11 + 656*m.b8*m.b12 + 544*m.b8*m.b13 + 384*m.b8*m.b14 + 256*m.b8*
                       m.b15 + 144*m.b8*m.b16 + 64*m.b8*m.b17 + 1152*m.b9*m.b10 + 960*m.b9*m.b11 + 800*m.b9*m.b12 + 656*
                       m.b9*m.b13 + 544*m.b9*m.b14 + 384*m.b9*m.b15 + 256*m.b9*m.b16 + 144*m.b9*m.b17 + 64*m.b9*m.b18 + 
                       1152*m.b10*m.b11 + 960*m.b10*m.b12 + 800*m.b10*m.b13 + 656*m.b10*m.b14 + 544*m.b10*m.b15 + 384*
                       m.b10*m.b16 + 256*m.b10*m.b17 + 144*m.b10*m.b18 + 64*m.b10*m.b19 + 1152*m.b11*m.b12 + 960*m.b11*
                       m.b13 + 800*m.b11*m.b14 + 656*m.b11*m.b15 + 544*m.b11*m.b16 + 384*m.b11*m.b17 + 256*m.b11*m.b18
                        + 144*m.b11*m.b19 + 64*m.b11*m.b20 + 1152*m.b12*m.b13 + 960*m.b12*m.b14 + 800*m.b12*m.b15 + 656*
                       m.b12*m.b16 + 544*m.b12*m.b17 + 384*m.b12*m.b18 + 256*m.b12*m.b19 + 144*m.b12*m.b20 + 64*m.b12*
                       m.b21 + 1152*m.b13*m.b14 + 960*m.b13*m.b15 + 800*m.b13*m.b16 + 656*m.b13*m.b17 + 544*m.b13*m.b18
                        + 384*m.b13*m.b19 + 256*m.b13*m.b20 + 144*m.b13*m.b21 + 64*m.b13*m.b22 + 1152*m.b14*m.b15 + 960*
                       m.b14*m.b16 + 800*m.b14*m.b17 + 656*m.b14*m.b18 + 544*m.b14*m.b19 + 384*m.b14*m.b20 + 256*m.b14*
                       m.b21 + 144*m.b14*m.b22 + 64*m.b14*m.b23 + 1152*m.b15*m.b16 + 960*m.b15*m.b17 + 800*m.b15*m.b18
                        + 656*m.b15*m.b19 + 544*m.b15*m.b20 + 384*m.b15*m.b21 + 256*m.b15*m.b22 + 144*m.b15*m.b23 + 64*
                       m.b15*m.b24 + 1152*m.b16*m.b17 + 960*m.b16*m.b18 + 800*m.b16*m.b19 + 656*m.b16*m.b20 + 544*m.b16*
                       m.b21 + 384*m.b16*m.b22 + 256*m.b16*m.b23 + 144*m.b16*m.b24 + 64*m.b16*m.b25 + 1152*m.b17*m.b18
                        + 960*m.b17*m.b19 + 800*m.b17*m.b20 + 656*m.b17*m.b21 + 544*m.b17*m.b22 + 384*m.b17*m.b23 + 256*
                       m.b17*m.b24 + 144*m.b17*m.b25 + 64*m.b17*m.b26 + 1152*m.b18*m.b19 + 960*m.b18*m.b20 + 800*m.b18*
                       m.b21 + 656*m.b18*m.b22 + 544*m.b18*m.b23 + 384*m.b18*m.b24 + 256*m.b18*m.b25 + 144*m.b18*m.b26
                        + 64*m.b18*m.b27 + 1152*m.b19*m.b20 + 960*m.b19*m.b21 + 800*m.b19*m.b22 + 656*m.b19*m.b23 + 544*
                       m.b19*m.b24 + 384*m.b19*m.b25 + 256*m.b19*m.b26 + 144*m.b19*m.b27 + 64*m.b19*m.b28 + 1152*m.b20*
                       m.b21 + 960*m.b20*m.b22 + 800*m.b20*m.b23 + 656*m.b20*m.b24 + 544*m.b20*m.b25 + 384*m.b20*m.b26
                        + 256*m.b20*m.b27 + 144*m.b20*m.b28 + 64*m.b20*m.b29 + 1152*m.b21*m.b22 + 960*m.b21*m.b23 + 800*
                       m.b21*m.b24 + 656*m.b21*m.b25 + 544*m.b21*m.b26 + 384*m.b21*m.b27 + 256*m.b21*m.b28 + 144*m.b21*
                       m.b29 + 64*m.b21*m.b30 + 1152*m.b22*m.b23 + 960*m.b22*m.b24 + 800*m.b22*m.b25 + 656*m.b22*m.b26
                        + 544*m.b22*m.b27 + 384*m.b22*m.b28 + 256*m.b22*m.b29 + 144*m.b22*m.b30 + 64*m.b22*m.b31 + 1152*
                       m.b23*m.b24 + 960*m.b23*m.b25 + 800*m.b23*m.b26 + 656*m.b23*m.b27 + 544*m.b23*m.b28 + 384*m.b23*
                       m.b29 + 256*m.b23*m.b30 + 144*m.b23*m.b31 + 64*m.b23*m.b32 + 1152*m.b24*m.b25 + 960*m.b24*m.b26
                        + 800*m.b24*m.b27 + 656*m.b24*m.b28 + 544*m.b24*m.b29 + 384*m.b24*m.b30 + 256*m.b24*m.b31 + 144*
                       m.b24*m.b32 + 64*m.b24*m.b33 + 1152*m.b25*m.b26 + 960*m.b25*m.b27 + 800*m.b25*m.b28 + 656*m.b25*
                       m.b29 + 544*m.b25*m.b30 + 384*m.b25*m.b31 + 256*m.b25*m.b32 + 144*m.b25*m.b33 + 64*m.b25*m.b34 + 
                       1152*m.b26*m.b27 + 960*m.b26*m.b28 + 800*m.b26*m.b29 + 656*m.b26*m.b30 + 544*m.b26*m.b31 + 384*
                       m.b26*m.b32 + 256*m.b26*m.b33 + 144*m.b26*m.b34 + 64*m.b26*m.b35 + 1152*m.b27*m.b28 + 960*m.b27*
                       m.b29 + 800*m.b27*m.b30 + 656*m.b27*m.b31 + 544*m.b27*m.b32 + 384*m.b27*m.b33 + 256*m.b27*m.b34
                        + 144*m.b27*m.b35 + 64*m.b27*m.b36 + 1152*m.b28*m.b29 + 960*m.b28*m.b30 + 800*m.b28*m.b31 + 656*
                       m.b28*m.b32 + 544*m.b28*m.b33 + 384*m.b28*m.b34 + 256*m.b28*m.b35 + 144*m.b28*m.b36 + 64*m.b28*
                       m.b37 + 1152*m.b29*m.b30 + 960*m.b29*m.b31 + 800*m.b29*m.b32 + 656*m.b29*m.b33 + 544*m.b29*m.b34
                        + 384*m.b29*m.b35 + 256*m.b29*m.b36 + 144*m.b29*m.b37 + 64*m.b29*m.b38 + 1152*m.b30*m.b31 + 960*
                       m.b30*m.b32 + 800*m.b30*m.b33 + 656*m.b30*m.b34 + 544*m.b30*m.b35 + 384*m.b30*m.b36 + 256*m.b30*
                       m.b37 + 144*m.b30*m.b38 + 64*m.b30*m.b39 + 1152*m.b31*m.b32 + 960*m.b31*m.b33 + 800*m.b31*m.b34
                        + 656*m.b31*m.b35 + 544*m.b31*m.b36 + 384*m.b31*m.b37 + 256*m.b31*m.b38 + 144*m.b31*m.b39 + 64*
                       m.b31*m.b40 + 1040*m.b32*m.b33 + 856*m.b32*m.b34 + 704*m.b32*m.b35 + 568*m.b32*m.b36 + 448*m.b32*
                       m.b37 + 296*m.b32*m.b38 + 176*m.b32*m.b39 + 72*m.b32*m.b40 + 928*m.b33*m.b34 + 736*m.b33*m.b35 + 
                       592*m.b33*m.b36 + 464*m.b33*m.b37 + 336*m.b33*m.b38 + 192*m.b33*m.b39 + 80*m.b33*m.b40 + 800*
                       m.b34*m.b35 + 616*m.b34*m.b36 + 464*m.b34*m.b37 + 328*m.b34*m.b38 + 208*m.b34*m.b39 + 88*m.b34*
                       m.b40 + 656*m.b35*m.b36 + 480*m.b35*m.b37 + 336*m.b35*m.b38 + 192*m.b35*m.b39 + 96*m.b35*m.b40 + 
                       496*m.b36*m.b37 + 344*m.b36*m.b38 + 208*m.b36*m.b39 + 88*m.b36*m.b40 + 352*m.b37*m.b38 + 224*
                       m.b37*m.b39 + 96*m.b37*m.b40 + 224*m.b38*m.b39 + 104*m.b38*m.b40 + 112*m.b39*m.b40 - 144*m.b1 - 
                       312*m.b2 - 496*m.b3 - 688*m.b4 - 880*m.b5 - 1072*m.b6 - 1264*m.b7 - 1448*m.b8 - 1616*m.b9 - 1760*
                       m.b10 - 1760*m.b11 - 1760*m.b12 - 1760*m.b13 - 1760*m.b14 - 1760*m.b15 - 1760*m.b16 - 1760*m.b17
                        - 1760*m.b18 - 1760*m.b19 - 1760*m.b20 - 1760*m.b21 - 1760*m.b22 - 1760*m.b23 - 1760*m.b24 - 
                       1760*m.b25 - 1760*m.b26 - 1760*m.b27 - 1760*m.b28 - 1760*m.b29 - 1760*m.b30 - 1760*m.b31 - 1616*
                       m.b32 - 1448*m.b33 - 1264*m.b34 - 1072*m.b35 - 880*m.b36 - 688*m.b37 - 496*m.b38 - 312*m.b39 - 
                       144*m.b40 - m.x41 <= 0)

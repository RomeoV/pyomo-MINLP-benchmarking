#  MINLP written by GAMS Convert at 08/13/20 17:37:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         36        1       35        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         36        1       35        0


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
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x36, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b2*m.b14*m.b15 + 64*m.b1*m.b2*m.b15*m.b16 + 64*m.b1*m.b2*m.b16*m.b17 + 64*m.b1*m.b2*m.b17*
                       m.b18 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*
                       m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3*m.b10*m.b12 + 64*
                       m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*m.b3*m.b13*m.b15 + 64*m.b1*m.b3*m.b14*
                       m.b16 + 64*m.b1*m.b3*m.b15*m.b17 + 64*m.b1*m.b3*m.b16*m.b18 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*
                       m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*m.b9*m.b12 + 64
                       *m.b1*m.b4*m.b10*m.b13 + 64*m.b1*m.b4*m.b11*m.b14 + 64*m.b1*m.b4*m.b12*m.b15 + 64*m.b1*m.b4*m.b13
                       *m.b16 + 64*m.b1*m.b4*m.b14*m.b17 + 64*m.b1*m.b4*m.b15*m.b18 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*
                       m.b5*m.b7*m.b11 + 64*m.b1*m.b5*m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*m.b14 + 
                       64*m.b1*m.b5*m.b11*m.b15 + 64*m.b1*m.b5*m.b12*m.b16 + 64*m.b1*m.b5*m.b13*m.b17 + 64*m.b1*m.b5*
                       m.b14*m.b18 + 64*m.b1*m.b6*m.b7*m.b12 + 64*m.b1*m.b6*m.b8*m.b13 + 64*m.b1*m.b6*m.b9*m.b14 + 64*
                       m.b1*m.b6*m.b10*m.b15 + 64*m.b1*m.b6*m.b11*m.b16 + 64*m.b1*m.b6*m.b12*m.b17 + 64*m.b1*m.b6*m.b13*
                       m.b18 + 64*m.b1*m.b7*m.b8*m.b14 + 64*m.b1*m.b7*m.b9*m.b15 + 64*m.b1*m.b7*m.b10*m.b16 + 64*m.b1*
                       m.b7*m.b11*m.b17 + 64*m.b1*m.b7*m.b12*m.b18 + 64*m.b1*m.b8*m.b9*m.b16 + 64*m.b1*m.b8*m.b10*m.b17
                        + 64*m.b1*m.b8*m.b11*m.b18 + 64*m.b1*m.b9*m.b10*m.b18 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*
                       m.b5*m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*
                       m.b2*m.b3*m.b9*m.b10 + 128*m.b2*m.b3*m.b10*m.b11 + 128*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*
                       m.b12*m.b13 + 128*m.b2*m.b3*m.b13*m.b14 + 128*m.b2*m.b3*m.b14*m.b15 + 128*m.b2*m.b3*m.b15*m.b16
                        + 128*m.b2*m.b3*m.b16*m.b17 + 128*m.b2*m.b3*m.b17*m.b18 + 64*m.b2*m.b3*m.b18*m.b19 + 128*m.b2*
                       m.b4*m.b5*m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 
                       128*m.b2*m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*
                       m.b12*m.b14 + 128*m.b2*m.b4*m.b13*m.b15 + 128*m.b2*m.b4*m.b14*m.b16 + 128*m.b2*m.b4*m.b15*m.b17
                        + 128*m.b2*m.b4*m.b16*m.b18 + 64*m.b2*m.b4*m.b17*m.b19 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5
                       *m.b7*m.b10 + 128*m.b2*m.b5*m.b8*m.b11 + 128*m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*m.b13 + 
                       128*m.b2*m.b5*m.b11*m.b14 + 128*m.b2*m.b5*m.b12*m.b15 + 128*m.b2*m.b5*m.b13*m.b16 + 128*m.b2*m.b5
                       *m.b14*m.b17 + 128*m.b2*m.b5*m.b15*m.b18 + 64*m.b2*m.b5*m.b16*m.b19 + 128*m.b2*m.b6*m.b7*m.b11 + 
                       128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*m.b13 + 128*m.b2*m.b6*m.b10*m.b14 + 128*m.b2*m.b6*
                       m.b11*m.b15 + 128*m.b2*m.b6*m.b12*m.b16 + 128*m.b2*m.b6*m.b13*m.b17 + 128*m.b2*m.b6*m.b14*m.b18
                        + 64*m.b2*m.b6*m.b15*m.b19 + 128*m.b2*m.b7*m.b8*m.b13 + 128*m.b2*m.b7*m.b9*m.b14 + 128*m.b2*m.b7
                       *m.b10*m.b15 + 128*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b7*m.b12*m.b17 + 128*m.b2*m.b7*m.b13*m.b18
                        + 64*m.b2*m.b7*m.b14*m.b19 + 128*m.b2*m.b8*m.b9*m.b15 + 128*m.b2*m.b8*m.b10*m.b16 + 128*m.b2*
                       m.b8*m.b11*m.b17 + 128*m.b2*m.b8*m.b12*m.b18 + 64*m.b2*m.b8*m.b13*m.b19 + 128*m.b2*m.b9*m.b10*
                       m.b17 + 128*m.b2*m.b9*m.b11*m.b18 + 64*m.b2*m.b9*m.b12*m.b19 + 64*m.b2*m.b10*m.b11*m.b19 + 192*
                       m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9
                        + 192*m.b3*m.b4*m.b9*m.b10 + 192*m.b3*m.b4*m.b10*m.b11 + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*
                       m.b4*m.b12*m.b13 + 192*m.b3*m.b4*m.b13*m.b14 + 192*m.b3*m.b4*m.b14*m.b15 + 192*m.b3*m.b4*m.b15*
                       m.b16 + 192*m.b3*m.b4*m.b16*m.b17 + 192*m.b3*m.b4*m.b17*m.b18 + 128*m.b3*m.b4*m.b18*m.b19 + 64*
                       m.b3*m.b4*m.b19*m.b20 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*m.b5*m.b8*
                       m.b10 + 192*m.b3*m.b5*m.b9*m.b11 + 192*m.b3*m.b5*m.b10*m.b12 + 192*m.b3*m.b5*m.b11*m.b13 + 192*
                       m.b3*m.b5*m.b12*m.b14 + 192*m.b3*m.b5*m.b13*m.b15 + 192*m.b3*m.b5*m.b14*m.b16 + 192*m.b3*m.b5*
                       m.b15*m.b17 + 192*m.b3*m.b5*m.b16*m.b18 + 128*m.b3*m.b5*m.b17*m.b19 + 64*m.b3*m.b5*m.b18*m.b20 + 
                       192*m.b3*m.b6*m.b7*m.b10 + 192*m.b3*m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*
                       m.b10*m.b13 + 192*m.b3*m.b6*m.b11*m.b14 + 192*m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b6*m.b13*m.b16
                        + 192*m.b3*m.b6*m.b14*m.b17 + 192*m.b3*m.b6*m.b15*m.b18 + 128*m.b3*m.b6*m.b16*m.b19 + 64*m.b3*
                       m.b6*m.b17*m.b20 + 192*m.b3*m.b7*m.b8*m.b12 + 192*m.b3*m.b7*m.b9*m.b13 + 192*m.b3*m.b7*m.b10*
                       m.b14 + 192*m.b3*m.b7*m.b11*m.b15 + 192*m.b3*m.b7*m.b12*m.b16 + 192*m.b3*m.b7*m.b13*m.b17 + 192*
                       m.b3*m.b7*m.b14*m.b18 + 128*m.b3*m.b7*m.b15*m.b19 + 64*m.b3*m.b7*m.b16*m.b20 + 192*m.b3*m.b8*m.b9
                       *m.b14 + 192*m.b3*m.b8*m.b10*m.b15 + 192*m.b3*m.b8*m.b11*m.b16 + 192*m.b3*m.b8*m.b12*m.b17 + 192*
                       m.b3*m.b8*m.b13*m.b18 + 128*m.b3*m.b8*m.b14*m.b19 + 64*m.b3*m.b8*m.b15*m.b20 + 192*m.b3*m.b9*
                       m.b10*m.b16 + 192*m.b3*m.b9*m.b11*m.b17 + 192*m.b3*m.b9*m.b12*m.b18 + 128*m.b3*m.b9*m.b13*m.b19
                        + 64*m.b3*m.b9*m.b14*m.b20 + 192*m.b3*m.b10*m.b11*m.b18 + 128*m.b3*m.b10*m.b12*m.b19 + 64*m.b3*
                       m.b10*m.b13*m.b20 + 64*m.b3*m.b11*m.b12*m.b20 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8
                        + 256*m.b4*m.b5*m.b8*m.b9 + 256*m.b4*m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5
                       *m.b11*m.b12 + 256*m.b4*m.b5*m.b12*m.b13 + 256*m.b4*m.b5*m.b13*m.b14 + 256*m.b4*m.b5*m.b14*m.b15
                        + 256*m.b4*m.b5*m.b15*m.b16 + 256*m.b4*m.b5*m.b16*m.b17 + 256*m.b4*m.b5*m.b17*m.b18 + 192*m.b4*
                       m.b5*m.b18*m.b19 + 128*m.b4*m.b5*m.b19*m.b20 + 64*m.b4*m.b5*m.b20*m.b21 + 256*m.b4*m.b6*m.b7*m.b9
                        + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11 + 256*m.b4*m.b6*m.b10*m.b12 + 256*m.b4*
                       m.b6*m.b11*m.b13 + 256*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*m.b6*m.b13*m.b15 + 256*m.b4*m.b6*m.b14*
                       m.b16 + 256*m.b4*m.b6*m.b15*m.b17 + 256*m.b4*m.b6*m.b16*m.b18 + 192*m.b4*m.b6*m.b17*m.b19 + 128*
                       m.b4*m.b6*m.b18*m.b20 + 64*m.b4*m.b6*m.b19*m.b21 + 256*m.b4*m.b7*m.b8*m.b11 + 256*m.b4*m.b7*m.b9*
                       m.b12 + 256*m.b4*m.b7*m.b10*m.b13 + 256*m.b4*m.b7*m.b11*m.b14 + 256*m.b4*m.b7*m.b12*m.b15 + 256*
                       m.b4*m.b7*m.b13*m.b16 + 256*m.b4*m.b7*m.b14*m.b17 + 256*m.b4*m.b7*m.b15*m.b18 + 192*m.b4*m.b7*
                       m.b16*m.b19 + 128*m.b4*m.b7*m.b17*m.b20 + 64*m.b4*m.b7*m.b18*m.b21 + 256*m.b4*m.b8*m.b9*m.b13 + 
                       256*m.b4*m.b8*m.b10*m.b14 + 256*m.b4*m.b8*m.b11*m.b15 + 256*m.b4*m.b8*m.b12*m.b16 + 256*m.b4*m.b8
                       *m.b13*m.b17 + 256*m.b4*m.b8*m.b14*m.b18 + 192*m.b4*m.b8*m.b15*m.b19 + 128*m.b4*m.b8*m.b16*m.b20
                        + 64*m.b4*m.b8*m.b17*m.b21 + 256*m.b4*m.b9*m.b10*m.b15 + 256*m.b4*m.b9*m.b11*m.b16 + 256*m.b4*
                       m.b9*m.b12*m.b17 + 256*m.b4*m.b9*m.b13*m.b18 + 192*m.b4*m.b9*m.b14*m.b19 + 128*m.b4*m.b9*m.b15*
                       m.b20 + 64*m.b4*m.b9*m.b16*m.b21 + 256*m.b4*m.b10*m.b11*m.b17 + 256*m.b4*m.b10*m.b12*m.b18 + 192*
                       m.b4*m.b10*m.b13*m.b19 + 128*m.b4*m.b10*m.b14*m.b20 + 64*m.b4*m.b10*m.b15*m.b21 + 192*m.b4*m.b11*
                       m.b12*m.b19 + 128*m.b4*m.b11*m.b13*m.b20 + 64*m.b4*m.b11*m.b14*m.b21 + 64*m.b4*m.b12*m.b13*m.b21
                        + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*
                       m.b10*m.b11 + 320*m.b5*m.b6*m.b11*m.b12 + 320*m.b5*m.b6*m.b12*m.b13 + 320*m.b5*m.b6*m.b13*m.b14
                        + 320*m.b5*m.b6*m.b14*m.b15 + 320*m.b5*m.b6*m.b15*m.b16 + 320*m.b5*m.b6*m.b16*m.b17 + 320*m.b5*
                       m.b6*m.b17*m.b18 + 256*m.b5*m.b6*m.b18*m.b19 + 192*m.b5*m.b6*m.b19*m.b20 + 128*m.b5*m.b6*m.b20*
                       m.b21 + 64*m.b5*m.b6*m.b21*m.b22 + 320*m.b5*m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*m.b11 + 320*m.b5
                       *m.b7*m.b10*m.b12 + 320*m.b5*m.b7*m.b11*m.b13 + 320*m.b5*m.b7*m.b12*m.b14 + 320*m.b5*m.b7*m.b13*
                       m.b15 + 320*m.b5*m.b7*m.b14*m.b16 + 320*m.b5*m.b7*m.b15*m.b17 + 320*m.b5*m.b7*m.b16*m.b18 + 256*
                       m.b5*m.b7*m.b17*m.b19 + 192*m.b5*m.b7*m.b18*m.b20 + 128*m.b5*m.b7*m.b19*m.b21 + 64*m.b5*m.b7*
                       m.b20*m.b22 + 320*m.b5*m.b8*m.b9*m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 320*m.b5*m.b8*m.b11*m.b14 + 
                       320*m.b5*m.b8*m.b12*m.b15 + 320*m.b5*m.b8*m.b13*m.b16 + 320*m.b5*m.b8*m.b14*m.b17 + 320*m.b5*m.b8
                       *m.b15*m.b18 + 256*m.b5*m.b8*m.b16*m.b19 + 192*m.b5*m.b8*m.b17*m.b20 + 128*m.b5*m.b8*m.b18*m.b21
                        + 64*m.b5*m.b8*m.b19*m.b22 + 320*m.b5*m.b9*m.b10*m.b14 + 320*m.b5*m.b9*m.b11*m.b15 + 320*m.b5*
                       m.b9*m.b12*m.b16 + 320*m.b5*m.b9*m.b13*m.b17 + 320*m.b5*m.b9*m.b14*m.b18 + 256*m.b5*m.b9*m.b15*
                       m.b19 + 192*m.b5*m.b9*m.b16*m.b20 + 128*m.b5*m.b9*m.b17*m.b21 + 64*m.b5*m.b9*m.b18*m.b22 + 320*
                       m.b5*m.b10*m.b11*m.b16 + 320*m.b5*m.b10*m.b12*m.b17 + 320*m.b5*m.b10*m.b13*m.b18 + 256*m.b5*m.b10
                       *m.b14*m.b19 + 192*m.b5*m.b10*m.b15*m.b20 + 128*m.b5*m.b10*m.b16*m.b21 + 64*m.b5*m.b10*m.b17*
                       m.b22 + 320*m.b5*m.b11*m.b12*m.b18 + 256*m.b5*m.b11*m.b13*m.b19 + 192*m.b5*m.b11*m.b14*m.b20 + 
                       128*m.b5*m.b11*m.b15*m.b21 + 64*m.b5*m.b11*m.b16*m.b22 + 192*m.b5*m.b12*m.b13*m.b20 + 128*m.b5*
                       m.b12*m.b14*m.b21 + 64*m.b5*m.b12*m.b15*m.b22 + 64*m.b5*m.b13*m.b14*m.b22 + 384*m.b6*m.b7*m.b8*
                       m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12 + 384*
                       m.b6*m.b7*m.b12*m.b13 + 384*m.b6*m.b7*m.b13*m.b14 + 384*m.b6*m.b7*m.b14*m.b15 + 384*m.b6*m.b7*
                       m.b15*m.b16 + 384*m.b6*m.b7*m.b16*m.b17 + 384*m.b6*m.b7*m.b17*m.b18 + 320*m.b6*m.b7*m.b18*m.b19
                        + 256*m.b6*m.b7*m.b19*m.b20 + 192*m.b6*m.b7*m.b20*m.b21 + 128*m.b6*m.b7*m.b21*m.b22 + 64*m.b6*
                       m.b7*m.b22*m.b23 + 384*m.b6*m.b8*m.b9*m.b11 + 384*m.b6*m.b8*m.b10*m.b12 + 384*m.b6*m.b8*m.b11*
                       m.b13 + 384*m.b6*m.b8*m.b12*m.b14 + 384*m.b6*m.b8*m.b13*m.b15 + 384*m.b6*m.b8*m.b14*m.b16 + 384*
                       m.b6*m.b8*m.b15*m.b17 + 384*m.b6*m.b8*m.b16*m.b18 + 320*m.b6*m.b8*m.b17*m.b19 + 256*m.b6*m.b8*
                       m.b18*m.b20 + 192*m.b6*m.b8*m.b19*m.b21 + 128*m.b6*m.b8*m.b20*m.b22 + 64*m.b6*m.b8*m.b21*m.b23 + 
                       384*m.b6*m.b9*m.b10*m.b13 + 384*m.b6*m.b9*m.b11*m.b14 + 384*m.b6*m.b9*m.b12*m.b15 + 384*m.b6*m.b9
                       *m.b13*m.b16 + 384*m.b6*m.b9*m.b14*m.b17 + 384*m.b6*m.b9*m.b15*m.b18 + 320*m.b6*m.b9*m.b16*m.b19
                        + 256*m.b6*m.b9*m.b17*m.b20 + 192*m.b6*m.b9*m.b18*m.b21 + 128*m.b6*m.b9*m.b19*m.b22 + 64*m.b6*
                       m.b9*m.b20*m.b23 + 384*m.b6*m.b10*m.b11*m.b15 + 384*m.b6*m.b10*m.b12*m.b16 + 384*m.b6*m.b10*m.b13
                       *m.b17 + 384*m.b6*m.b10*m.b14*m.b18 + 320*m.b6*m.b10*m.b15*m.b19 + 256*m.b6*m.b10*m.b16*m.b20 + 
                       192*m.b6*m.b10*m.b17*m.b21 + 128*m.b6*m.b10*m.b18*m.b22 + 64*m.b6*m.b10*m.b19*m.b23 + 384*m.b6*
                       m.b11*m.b12*m.b17 + 384*m.b6*m.b11*m.b13*m.b18 + 320*m.b6*m.b11*m.b14*m.b19 + 256*m.b6*m.b11*
                       m.b15*m.b20 + 192*m.b6*m.b11*m.b16*m.b21 + 128*m.b6*m.b11*m.b17*m.b22 + 64*m.b6*m.b11*m.b18*m.b23
                        + 320*m.b6*m.b12*m.b13*m.b19 + 256*m.b6*m.b12*m.b14*m.b20 + 192*m.b6*m.b12*m.b15*m.b21 + 128*
                       m.b6*m.b12*m.b16*m.b22 + 64*m.b6*m.b12*m.b17*m.b23 + 192*m.b6*m.b13*m.b14*m.b21 + 128*m.b6*m.b13*
                       m.b15*m.b22 + 64*m.b6*m.b13*m.b16*m.b23 + 64*m.b6*m.b14*m.b15*m.b23 + 448*m.b7*m.b8*m.b9*m.b10 + 
                       448*m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*m.b11*m.b12 + 448*m.b7*m.b8*m.b12*m.b13 + 448*m.b7*m.b8
                       *m.b13*m.b14 + 448*m.b7*m.b8*m.b14*m.b15 + 448*m.b7*m.b8*m.b15*m.b16 + 448*m.b7*m.b8*m.b16*m.b17
                        + 448*m.b7*m.b8*m.b17*m.b18 + 384*m.b7*m.b8*m.b18*m.b19 + 320*m.b7*m.b8*m.b19*m.b20 + 256*m.b7*
                       m.b8*m.b20*m.b21 + 192*m.b7*m.b8*m.b21*m.b22 + 128*m.b7*m.b8*m.b22*m.b23 + 64*m.b7*m.b8*m.b23*
                       m.b24 + 448*m.b7*m.b9*m.b10*m.b12 + 448*m.b7*m.b9*m.b11*m.b13 + 448*m.b7*m.b9*m.b12*m.b14 + 448*
                       m.b7*m.b9*m.b13*m.b15 + 448*m.b7*m.b9*m.b14*m.b16 + 448*m.b7*m.b9*m.b15*m.b17 + 448*m.b7*m.b9*
                       m.b16*m.b18 + 384*m.b7*m.b9*m.b17*m.b19 + 320*m.b7*m.b9*m.b18*m.b20 + 256*m.b7*m.b9*m.b19*m.b21
                        + 192*m.b7*m.b9*m.b20*m.b22 + 128*m.b7*m.b9*m.b21*m.b23 + 64*m.b7*m.b9*m.b22*m.b24 + 448*m.b7*
                       m.b10*m.b11*m.b14 + 448*m.b7*m.b10*m.b12*m.b15 + 448*m.b7*m.b10*m.b13*m.b16 + 448*m.b7*m.b10*
                       m.b14*m.b17 + 448*m.b7*m.b10*m.b15*m.b18 + 384*m.b7*m.b10*m.b16*m.b19 + 320*m.b7*m.b10*m.b17*
                       m.b20 + 256*m.b7*m.b10*m.b18*m.b21 + 192*m.b7*m.b10*m.b19*m.b22 + 128*m.b7*m.b10*m.b20*m.b23 + 64
                       *m.b7*m.b10*m.b21*m.b24 + 448*m.b7*m.b11*m.b12*m.b16 + 448*m.b7*m.b11*m.b13*m.b17 + 448*m.b7*
                       m.b11*m.b14*m.b18 + 384*m.b7*m.b11*m.b15*m.b19 + 320*m.b7*m.b11*m.b16*m.b20 + 256*m.b7*m.b11*
                       m.b17*m.b21 + 192*m.b7*m.b11*m.b18*m.b22 + 128*m.b7*m.b11*m.b19*m.b23 + 64*m.b7*m.b11*m.b20*m.b24
                        + 448*m.b7*m.b12*m.b13*m.b18 + 384*m.b7*m.b12*m.b14*m.b19 + 320*m.b7*m.b12*m.b15*m.b20 + 256*
                       m.b7*m.b12*m.b16*m.b21 + 192*m.b7*m.b12*m.b17*m.b22 + 128*m.b7*m.b12*m.b18*m.b23 + 64*m.b7*m.b12*
                       m.b19*m.b24 + 320*m.b7*m.b13*m.b14*m.b20 + 256*m.b7*m.b13*m.b15*m.b21 + 192*m.b7*m.b13*m.b16*
                       m.b22 + 128*m.b7*m.b13*m.b17*m.b23 + 64*m.b7*m.b13*m.b18*m.b24 + 192*m.b7*m.b14*m.b15*m.b22 + 128
                       *m.b7*m.b14*m.b16*m.b23 + 64*m.b7*m.b14*m.b17*m.b24 + 64*m.b7*m.b15*m.b16*m.b24 + 512*m.b8*m.b9*
                       m.b10*m.b11 + 512*m.b8*m.b9*m.b11*m.b12 + 512*m.b8*m.b9*m.b12*m.b13 + 512*m.b8*m.b9*m.b13*m.b14
                        + 512*m.b8*m.b9*m.b14*m.b15 + 512*m.b8*m.b9*m.b15*m.b16 + 512*m.b8*m.b9*m.b16*m.b17 + 512*m.b8*
                       m.b9*m.b17*m.b18 + 448*m.b8*m.b9*m.b18*m.b19 + 384*m.b8*m.b9*m.b19*m.b20 + 320*m.b8*m.b9*m.b20*
                       m.b21 + 256*m.b8*m.b9*m.b21*m.b22 + 192*m.b8*m.b9*m.b22*m.b23 + 128*m.b8*m.b9*m.b23*m.b24 + 64*
                       m.b8*m.b9*m.b24*m.b25 + 512*m.b8*m.b10*m.b11*m.b13 + 512*m.b8*m.b10*m.b12*m.b14 + 512*m.b8*m.b10*
                       m.b13*m.b15 + 512*m.b8*m.b10*m.b14*m.b16 + 512*m.b8*m.b10*m.b15*m.b17 + 512*m.b8*m.b10*m.b16*
                       m.b18 + 448*m.b8*m.b10*m.b17*m.b19 + 384*m.b8*m.b10*m.b18*m.b20 + 320*m.b8*m.b10*m.b19*m.b21 + 
                       256*m.b8*m.b10*m.b20*m.b22 + 192*m.b8*m.b10*m.b21*m.b23 + 128*m.b8*m.b10*m.b22*m.b24 + 64*m.b8*
                       m.b10*m.b23*m.b25 + 512*m.b8*m.b11*m.b12*m.b15 + 512*m.b8*m.b11*m.b13*m.b16 + 512*m.b8*m.b11*
                       m.b14*m.b17 + 512*m.b8*m.b11*m.b15*m.b18 + 448*m.b8*m.b11*m.b16*m.b19 + 384*m.b8*m.b11*m.b17*
                       m.b20 + 320*m.b8*m.b11*m.b18*m.b21 + 256*m.b8*m.b11*m.b19*m.b22 + 192*m.b8*m.b11*m.b20*m.b23 + 
                       128*m.b8*m.b11*m.b21*m.b24 + 64*m.b8*m.b11*m.b22*m.b25 + 512*m.b8*m.b12*m.b13*m.b17 + 512*m.b8*
                       m.b12*m.b14*m.b18 + 448*m.b8*m.b12*m.b15*m.b19 + 384*m.b8*m.b12*m.b16*m.b20 + 320*m.b8*m.b12*
                       m.b17*m.b21 + 256*m.b8*m.b12*m.b18*m.b22 + 192*m.b8*m.b12*m.b19*m.b23 + 128*m.b8*m.b12*m.b20*
                       m.b24 + 64*m.b8*m.b12*m.b21*m.b25 + 448*m.b8*m.b13*m.b14*m.b19 + 384*m.b8*m.b13*m.b15*m.b20 + 320
                       *m.b8*m.b13*m.b16*m.b21 + 256*m.b8*m.b13*m.b17*m.b22 + 192*m.b8*m.b13*m.b18*m.b23 + 128*m.b8*
                       m.b13*m.b19*m.b24 + 64*m.b8*m.b13*m.b20*m.b25 + 320*m.b8*m.b14*m.b15*m.b21 + 256*m.b8*m.b14*m.b16
                       *m.b22 + 192*m.b8*m.b14*m.b17*m.b23 + 128*m.b8*m.b14*m.b18*m.b24 + 64*m.b8*m.b14*m.b19*m.b25 + 
                       192*m.b8*m.b15*m.b16*m.b23 + 128*m.b8*m.b15*m.b17*m.b24 + 64*m.b8*m.b15*m.b18*m.b25 + 64*m.b8*
                       m.b16*m.b17*m.b25 + 576*m.b9*m.b10*m.b11*m.b12 + 576*m.b9*m.b10*m.b12*m.b13 + 576*m.b9*m.b10*
                       m.b13*m.b14 + 576*m.b9*m.b10*m.b14*m.b15 + 576*m.b9*m.b10*m.b15*m.b16 + 576*m.b9*m.b10*m.b16*
                       m.b17 + 576*m.b9*m.b10*m.b17*m.b18 + 512*m.b9*m.b10*m.b18*m.b19 + 448*m.b9*m.b10*m.b19*m.b20 + 
                       384*m.b9*m.b10*m.b20*m.b21 + 320*m.b9*m.b10*m.b21*m.b22 + 256*m.b9*m.b10*m.b22*m.b23 + 192*m.b9*
                       m.b10*m.b23*m.b24 + 128*m.b9*m.b10*m.b24*m.b25 + 64*m.b9*m.b10*m.b25*m.b26 + 576*m.b9*m.b11*m.b12
                       *m.b14 + 576*m.b9*m.b11*m.b13*m.b15 + 576*m.b9*m.b11*m.b14*m.b16 + 576*m.b9*m.b11*m.b15*m.b17 + 
                       576*m.b9*m.b11*m.b16*m.b18 + 512*m.b9*m.b11*m.b17*m.b19 + 448*m.b9*m.b11*m.b18*m.b20 + 384*m.b9*
                       m.b11*m.b19*m.b21 + 320*m.b9*m.b11*m.b20*m.b22 + 256*m.b9*m.b11*m.b21*m.b23 + 192*m.b9*m.b11*
                       m.b22*m.b24 + 128*m.b9*m.b11*m.b23*m.b25 + 64*m.b9*m.b11*m.b24*m.b26 + 576*m.b9*m.b12*m.b13*m.b16
                        + 576*m.b9*m.b12*m.b14*m.b17 + 576*m.b9*m.b12*m.b15*m.b18 + 512*m.b9*m.b12*m.b16*m.b19 + 448*
                       m.b9*m.b12*m.b17*m.b20 + 384*m.b9*m.b12*m.b18*m.b21 + 320*m.b9*m.b12*m.b19*m.b22 + 256*m.b9*m.b12
                       *m.b20*m.b23 + 192*m.b9*m.b12*m.b21*m.b24 + 128*m.b9*m.b12*m.b22*m.b25 + 64*m.b9*m.b12*m.b23*
                       m.b26 + 576*m.b9*m.b13*m.b14*m.b18 + 512*m.b9*m.b13*m.b15*m.b19 + 448*m.b9*m.b13*m.b16*m.b20 + 
                       384*m.b9*m.b13*m.b17*m.b21 + 320*m.b9*m.b13*m.b18*m.b22 + 256*m.b9*m.b13*m.b19*m.b23 + 192*m.b9*
                       m.b13*m.b20*m.b24 + 128*m.b9*m.b13*m.b21*m.b25 + 64*m.b9*m.b13*m.b22*m.b26 + 448*m.b9*m.b14*m.b15
                       *m.b20 + 384*m.b9*m.b14*m.b16*m.b21 + 320*m.b9*m.b14*m.b17*m.b22 + 256*m.b9*m.b14*m.b18*m.b23 + 
                       192*m.b9*m.b14*m.b19*m.b24 + 128*m.b9*m.b14*m.b20*m.b25 + 64*m.b9*m.b14*m.b21*m.b26 + 320*m.b9*
                       m.b15*m.b16*m.b22 + 256*m.b9*m.b15*m.b17*m.b23 + 192*m.b9*m.b15*m.b18*m.b24 + 128*m.b9*m.b15*
                       m.b19*m.b25 + 64*m.b9*m.b15*m.b20*m.b26 + 192*m.b9*m.b16*m.b17*m.b24 + 128*m.b9*m.b16*m.b18*m.b25
                        + 64*m.b9*m.b16*m.b19*m.b26 + 64*m.b9*m.b17*m.b18*m.b26 + 640*m.b10*m.b11*m.b12*m.b13 + 640*
                       m.b10*m.b11*m.b13*m.b14 + 640*m.b10*m.b11*m.b14*m.b15 + 640*m.b10*m.b11*m.b15*m.b16 + 640*m.b10*
                       m.b11*m.b16*m.b17 + 640*m.b10*m.b11*m.b17*m.b18 + 576*m.b10*m.b11*m.b18*m.b19 + 512*m.b10*m.b11*
                       m.b19*m.b20 + 448*m.b10*m.b11*m.b20*m.b21 + 384*m.b10*m.b11*m.b21*m.b22 + 320*m.b10*m.b11*m.b22*
                       m.b23 + 256*m.b10*m.b11*m.b23*m.b24 + 192*m.b10*m.b11*m.b24*m.b25 + 128*m.b10*m.b11*m.b25*m.b26
                        + 64*m.b10*m.b11*m.b26*m.b27 + 640*m.b10*m.b12*m.b13*m.b15 + 640*m.b10*m.b12*m.b14*m.b16 + 640*
                       m.b10*m.b12*m.b15*m.b17 + 640*m.b10*m.b12*m.b16*m.b18 + 576*m.b10*m.b12*m.b17*m.b19 + 512*m.b10*
                       m.b12*m.b18*m.b20 + 448*m.b10*m.b12*m.b19*m.b21 + 384*m.b10*m.b12*m.b20*m.b22 + 320*m.b10*m.b12*
                       m.b21*m.b23 + 256*m.b10*m.b12*m.b22*m.b24 + 192*m.b10*m.b12*m.b23*m.b25 + 128*m.b10*m.b12*m.b24*
                       m.b26 + 64*m.b10*m.b12*m.b25*m.b27 + 640*m.b10*m.b13*m.b14*m.b17 + 640*m.b10*m.b13*m.b15*m.b18 + 
                       576*m.b10*m.b13*m.b16*m.b19 + 512*m.b10*m.b13*m.b17*m.b20 + 448*m.b10*m.b13*m.b18*m.b21 + 384*
                       m.b10*m.b13*m.b19*m.b22 + 320*m.b10*m.b13*m.b20*m.b23 + 256*m.b10*m.b13*m.b21*m.b24 + 192*m.b10*
                       m.b13*m.b22*m.b25 + 128*m.b10*m.b13*m.b23*m.b26 + 64*m.b10*m.b13*m.b24*m.b27 + 576*m.b10*m.b14*
                       m.b15*m.b19 + 512*m.b10*m.b14*m.b16*m.b20 + 448*m.b10*m.b14*m.b17*m.b21 + 384*m.b10*m.b14*m.b18*
                       m.b22 + 320*m.b10*m.b14*m.b19*m.b23 + 256*m.b10*m.b14*m.b20*m.b24 + 192*m.b10*m.b14*m.b21*m.b25
                        + 128*m.b10*m.b14*m.b22*m.b26 + 64*m.b10*m.b14*m.b23*m.b27 + 448*m.b10*m.b15*m.b16*m.b21 + 384*
                       m.b10*m.b15*m.b17*m.b22 + 320*m.b10*m.b15*m.b18*m.b23 + 256*m.b10*m.b15*m.b19*m.b24 + 192*m.b10*
                       m.b15*m.b20*m.b25 + 128*m.b10*m.b15*m.b21*m.b26 + 64*m.b10*m.b15*m.b22*m.b27 + 320*m.b10*m.b16*
                       m.b17*m.b23 + 256*m.b10*m.b16*m.b18*m.b24 + 192*m.b10*m.b16*m.b19*m.b25 + 128*m.b10*m.b16*m.b20*
                       m.b26 + 64*m.b10*m.b16*m.b21*m.b27 + 192*m.b10*m.b17*m.b18*m.b25 + 128*m.b10*m.b17*m.b19*m.b26 + 
                       64*m.b10*m.b17*m.b20*m.b27 + 64*m.b10*m.b18*m.b19*m.b27 + 704*m.b11*m.b12*m.b13*m.b14 + 704*m.b11
                       *m.b12*m.b14*m.b15 + 704*m.b11*m.b12*m.b15*m.b16 + 704*m.b11*m.b12*m.b16*m.b17 + 704*m.b11*m.b12*
                       m.b17*m.b18 + 640*m.b11*m.b12*m.b18*m.b19 + 576*m.b11*m.b12*m.b19*m.b20 + 512*m.b11*m.b12*m.b20*
                       m.b21 + 448*m.b11*m.b12*m.b21*m.b22 + 384*m.b11*m.b12*m.b22*m.b23 + 320*m.b11*m.b12*m.b23*m.b24
                        + 256*m.b11*m.b12*m.b24*m.b25 + 192*m.b11*m.b12*m.b25*m.b26 + 128*m.b11*m.b12*m.b26*m.b27 + 64*
                       m.b11*m.b12*m.b27*m.b28 + 704*m.b11*m.b13*m.b14*m.b16 + 704*m.b11*m.b13*m.b15*m.b17 + 704*m.b11*
                       m.b13*m.b16*m.b18 + 640*m.b11*m.b13*m.b17*m.b19 + 576*m.b11*m.b13*m.b18*m.b20 + 512*m.b11*m.b13*
                       m.b19*m.b21 + 448*m.b11*m.b13*m.b20*m.b22 + 384*m.b11*m.b13*m.b21*m.b23 + 320*m.b11*m.b13*m.b22*
                       m.b24 + 256*m.b11*m.b13*m.b23*m.b25 + 192*m.b11*m.b13*m.b24*m.b26 + 128*m.b11*m.b13*m.b25*m.b27
                        + 64*m.b11*m.b13*m.b26*m.b28 + 704*m.b11*m.b14*m.b15*m.b18 + 640*m.b11*m.b14*m.b16*m.b19 + 576*
                       m.b11*m.b14*m.b17*m.b20 + 512*m.b11*m.b14*m.b18*m.b21 + 448*m.b11*m.b14*m.b19*m.b22 + 384*m.b11*
                       m.b14*m.b20*m.b23 + 320*m.b11*m.b14*m.b21*m.b24 + 256*m.b11*m.b14*m.b22*m.b25 + 192*m.b11*m.b14*
                       m.b23*m.b26 + 128*m.b11*m.b14*m.b24*m.b27 + 64*m.b11*m.b14*m.b25*m.b28 + 576*m.b11*m.b15*m.b16*
                       m.b20 + 512*m.b11*m.b15*m.b17*m.b21 + 448*m.b11*m.b15*m.b18*m.b22 + 384*m.b11*m.b15*m.b19*m.b23
                        + 320*m.b11*m.b15*m.b20*m.b24 + 256*m.b11*m.b15*m.b21*m.b25 + 192*m.b11*m.b15*m.b22*m.b26 + 128*
                       m.b11*m.b15*m.b23*m.b27 + 64*m.b11*m.b15*m.b24*m.b28 + 448*m.b11*m.b16*m.b17*m.b22 + 384*m.b11*
                       m.b16*m.b18*m.b23 + 320*m.b11*m.b16*m.b19*m.b24 + 256*m.b11*m.b16*m.b20*m.b25 + 192*m.b11*m.b16*
                       m.b21*m.b26 + 128*m.b11*m.b16*m.b22*m.b27 + 64*m.b11*m.b16*m.b23*m.b28 + 320*m.b11*m.b17*m.b18*
                       m.b24 + 256*m.b11*m.b17*m.b19*m.b25 + 192*m.b11*m.b17*m.b20*m.b26 + 128*m.b11*m.b17*m.b21*m.b27
                        + 64*m.b11*m.b17*m.b22*m.b28 + 192*m.b11*m.b18*m.b19*m.b26 + 128*m.b11*m.b18*m.b20*m.b27 + 64*
                       m.b11*m.b18*m.b21*m.b28 + 64*m.b11*m.b19*m.b20*m.b28 + 768*m.b12*m.b13*m.b14*m.b15 + 768*m.b12*
                       m.b13*m.b15*m.b16 + 768*m.b12*m.b13*m.b16*m.b17 + 768*m.b12*m.b13*m.b17*m.b18 + 704*m.b12*m.b13*
                       m.b18*m.b19 + 640*m.b12*m.b13*m.b19*m.b20 + 576*m.b12*m.b13*m.b20*m.b21 + 512*m.b12*m.b13*m.b21*
                       m.b22 + 448*m.b12*m.b13*m.b22*m.b23 + 384*m.b12*m.b13*m.b23*m.b24 + 320*m.b12*m.b13*m.b24*m.b25
                        + 256*m.b12*m.b13*m.b25*m.b26 + 192*m.b12*m.b13*m.b26*m.b27 + 128*m.b12*m.b13*m.b27*m.b28 + 64*
                       m.b12*m.b13*m.b28*m.b29 + 768*m.b12*m.b14*m.b15*m.b17 + 768*m.b12*m.b14*m.b16*m.b18 + 704*m.b12*
                       m.b14*m.b17*m.b19 + 640*m.b12*m.b14*m.b18*m.b20 + 576*m.b12*m.b14*m.b19*m.b21 + 512*m.b12*m.b14*
                       m.b20*m.b22 + 448*m.b12*m.b14*m.b21*m.b23 + 384*m.b12*m.b14*m.b22*m.b24 + 320*m.b12*m.b14*m.b23*
                       m.b25 + 256*m.b12*m.b14*m.b24*m.b26 + 192*m.b12*m.b14*m.b25*m.b27 + 128*m.b12*m.b14*m.b26*m.b28
                        + 64*m.b12*m.b14*m.b27*m.b29 + 704*m.b12*m.b15*m.b16*m.b19 + 640*m.b12*m.b15*m.b17*m.b20 + 576*
                       m.b12*m.b15*m.b18*m.b21 + 512*m.b12*m.b15*m.b19*m.b22 + 448*m.b12*m.b15*m.b20*m.b23 + 384*m.b12*
                       m.b15*m.b21*m.b24 + 320*m.b12*m.b15*m.b22*m.b25 + 256*m.b12*m.b15*m.b23*m.b26 + 192*m.b12*m.b15*
                       m.b24*m.b27 + 128*m.b12*m.b15*m.b25*m.b28 + 64*m.b12*m.b15*m.b26*m.b29 + 576*m.b12*m.b16*m.b17*
                       m.b21 + 512*m.b12*m.b16*m.b18*m.b22 + 448*m.b12*m.b16*m.b19*m.b23 + 384*m.b12*m.b16*m.b20*m.b24
                        + 320*m.b12*m.b16*m.b21*m.b25 + 256*m.b12*m.b16*m.b22*m.b26 + 192*m.b12*m.b16*m.b23*m.b27 + 128*
                       m.b12*m.b16*m.b24*m.b28 + 64*m.b12*m.b16*m.b25*m.b29 + 448*m.b12*m.b17*m.b18*m.b23 + 384*m.b12*
                       m.b17*m.b19*m.b24 + 320*m.b12*m.b17*m.b20*m.b25 + 256*m.b12*m.b17*m.b21*m.b26 + 192*m.b12*m.b17*
                       m.b22*m.b27 + 128*m.b12*m.b17*m.b23*m.b28 + 64*m.b12*m.b17*m.b24*m.b29 + 320*m.b12*m.b18*m.b19*
                       m.b25 + 256*m.b12*m.b18*m.b20*m.b26 + 192*m.b12*m.b18*m.b21*m.b27 + 128*m.b12*m.b18*m.b22*m.b28
                        + 64*m.b12*m.b18*m.b23*m.b29 + 192*m.b12*m.b19*m.b20*m.b27 + 128*m.b12*m.b19*m.b21*m.b28 + 64*
                       m.b12*m.b19*m.b22*m.b29 + 64*m.b12*m.b20*m.b21*m.b29 + 832*m.b13*m.b14*m.b15*m.b16 + 832*m.b13*
                       m.b14*m.b16*m.b17 + 832*m.b13*m.b14*m.b17*m.b18 + 768*m.b13*m.b14*m.b18*m.b19 + 704*m.b13*m.b14*
                       m.b19*m.b20 + 640*m.b13*m.b14*m.b20*m.b21 + 576*m.b13*m.b14*m.b21*m.b22 + 512*m.b13*m.b14*m.b22*
                       m.b23 + 448*m.b13*m.b14*m.b23*m.b24 + 384*m.b13*m.b14*m.b24*m.b25 + 320*m.b13*m.b14*m.b25*m.b26
                        + 256*m.b13*m.b14*m.b26*m.b27 + 192*m.b13*m.b14*m.b27*m.b28 + 128*m.b13*m.b14*m.b28*m.b29 + 64*
                       m.b13*m.b14*m.b29*m.b30 + 832*m.b13*m.b15*m.b16*m.b18 + 768*m.b13*m.b15*m.b17*m.b19 + 704*m.b13*
                       m.b15*m.b18*m.b20 + 640*m.b13*m.b15*m.b19*m.b21 + 576*m.b13*m.b15*m.b20*m.b22 + 512*m.b13*m.b15*
                       m.b21*m.b23 + 448*m.b13*m.b15*m.b22*m.b24 + 384*m.b13*m.b15*m.b23*m.b25 + 320*m.b13*m.b15*m.b24*
                       m.b26 + 256*m.b13*m.b15*m.b25*m.b27 + 192*m.b13*m.b15*m.b26*m.b28 + 128*m.b13*m.b15*m.b27*m.b29
                        + 64*m.b13*m.b15*m.b28*m.b30 + 704*m.b13*m.b16*m.b17*m.b20 + 640*m.b13*m.b16*m.b18*m.b21 + 576*
                       m.b13*m.b16*m.b19*m.b22 + 512*m.b13*m.b16*m.b20*m.b23 + 448*m.b13*m.b16*m.b21*m.b24 + 384*m.b13*
                       m.b16*m.b22*m.b25 + 320*m.b13*m.b16*m.b23*m.b26 + 256*m.b13*m.b16*m.b24*m.b27 + 192*m.b13*m.b16*
                       m.b25*m.b28 + 128*m.b13*m.b16*m.b26*m.b29 + 64*m.b13*m.b16*m.b27*m.b30 + 576*m.b13*m.b17*m.b18*
                       m.b22 + 512*m.b13*m.b17*m.b19*m.b23 + 448*m.b13*m.b17*m.b20*m.b24 + 384*m.b13*m.b17*m.b21*m.b25
                        + 320*m.b13*m.b17*m.b22*m.b26 + 256*m.b13*m.b17*m.b23*m.b27 + 192*m.b13*m.b17*m.b24*m.b28 + 128*
                       m.b13*m.b17*m.b25*m.b29 + 64*m.b13*m.b17*m.b26*m.b30 + 448*m.b13*m.b18*m.b19*m.b24 + 384*m.b13*
                       m.b18*m.b20*m.b25 + 320*m.b13*m.b18*m.b21*m.b26 + 256*m.b13*m.b18*m.b22*m.b27 + 192*m.b13*m.b18*
                       m.b23*m.b28 + 128*m.b13*m.b18*m.b24*m.b29 + 64*m.b13*m.b18*m.b25*m.b30 + 320*m.b13*m.b19*m.b20*
                       m.b26 + 256*m.b13*m.b19*m.b21*m.b27 + 192*m.b13*m.b19*m.b22*m.b28 + 128*m.b13*m.b19*m.b23*m.b29
                        + 64*m.b13*m.b19*m.b24*m.b30 + 192*m.b13*m.b20*m.b21*m.b28 + 128*m.b13*m.b20*m.b22*m.b29 + 64*
                       m.b13*m.b20*m.b23*m.b30 + 64*m.b13*m.b21*m.b22*m.b30 + 896*m.b14*m.b15*m.b16*m.b17 + 896*m.b14*
                       m.b15*m.b17*m.b18 + 832*m.b14*m.b15*m.b18*m.b19 + 768*m.b14*m.b15*m.b19*m.b20 + 704*m.b14*m.b15*
                       m.b20*m.b21 + 640*m.b14*m.b15*m.b21*m.b22 + 576*m.b14*m.b15*m.b22*m.b23 + 512*m.b14*m.b15*m.b23*
                       m.b24 + 448*m.b14*m.b15*m.b24*m.b25 + 384*m.b14*m.b15*m.b25*m.b26 + 320*m.b14*m.b15*m.b26*m.b27
                        + 256*m.b14*m.b15*m.b27*m.b28 + 192*m.b14*m.b15*m.b28*m.b29 + 128*m.b14*m.b15*m.b29*m.b30 + 64*
                       m.b14*m.b15*m.b30*m.b31 + 832*m.b14*m.b16*m.b17*m.b19 + 768*m.b14*m.b16*m.b18*m.b20 + 704*m.b14*
                       m.b16*m.b19*m.b21 + 640*m.b14*m.b16*m.b20*m.b22 + 576*m.b14*m.b16*m.b21*m.b23 + 512*m.b14*m.b16*
                       m.b22*m.b24 + 448*m.b14*m.b16*m.b23*m.b25 + 384*m.b14*m.b16*m.b24*m.b26 + 320*m.b14*m.b16*m.b25*
                       m.b27 + 256*m.b14*m.b16*m.b26*m.b28 + 192*m.b14*m.b16*m.b27*m.b29 + 128*m.b14*m.b16*m.b28*m.b30
                        + 64*m.b14*m.b16*m.b29*m.b31 + 704*m.b14*m.b17*m.b18*m.b21 + 640*m.b14*m.b17*m.b19*m.b22 + 576*
                       m.b14*m.b17*m.b20*m.b23 + 512*m.b14*m.b17*m.b21*m.b24 + 448*m.b14*m.b17*m.b22*m.b25 + 384*m.b14*
                       m.b17*m.b23*m.b26 + 320*m.b14*m.b17*m.b24*m.b27 + 256*m.b14*m.b17*m.b25*m.b28 + 192*m.b14*m.b17*
                       m.b26*m.b29 + 128*m.b14*m.b17*m.b27*m.b30 + 64*m.b14*m.b17*m.b28*m.b31 + 576*m.b14*m.b18*m.b19*
                       m.b23 + 512*m.b14*m.b18*m.b20*m.b24 + 448*m.b14*m.b18*m.b21*m.b25 + 384*m.b14*m.b18*m.b22*m.b26
                        + 320*m.b14*m.b18*m.b23*m.b27 + 256*m.b14*m.b18*m.b24*m.b28 + 192*m.b14*m.b18*m.b25*m.b29 + 128*
                       m.b14*m.b18*m.b26*m.b30 + 64*m.b14*m.b18*m.b27*m.b31 + 448*m.b14*m.b19*m.b20*m.b25 + 384*m.b14*
                       m.b19*m.b21*m.b26 + 320*m.b14*m.b19*m.b22*m.b27 + 256*m.b14*m.b19*m.b23*m.b28 + 192*m.b14*m.b19*
                       m.b24*m.b29 + 128*m.b14*m.b19*m.b25*m.b30 + 64*m.b14*m.b19*m.b26*m.b31 + 320*m.b14*m.b20*m.b21*
                       m.b27 + 256*m.b14*m.b20*m.b22*m.b28 + 192*m.b14*m.b20*m.b23*m.b29 + 128*m.b14*m.b20*m.b24*m.b30
                        + 64*m.b14*m.b20*m.b25*m.b31 + 192*m.b14*m.b21*m.b22*m.b29 + 128*m.b14*m.b21*m.b23*m.b30 + 64*
                       m.b14*m.b21*m.b24*m.b31 + 64*m.b14*m.b22*m.b23*m.b31 + 960*m.b15*m.b16*m.b17*m.b18 + 896*m.b15*
                       m.b16*m.b18*m.b19 + 832*m.b15*m.b16*m.b19*m.b20 + 768*m.b15*m.b16*m.b20*m.b21 + 704*m.b15*m.b16*
                       m.b21*m.b22 + 640*m.b15*m.b16*m.b22*m.b23 + 576*m.b15*m.b16*m.b23*m.b24 + 512*m.b15*m.b16*m.b24*
                       m.b25 + 448*m.b15*m.b16*m.b25*m.b26 + 384*m.b15*m.b16*m.b26*m.b27 + 320*m.b15*m.b16*m.b27*m.b28
                        + 256*m.b15*m.b16*m.b28*m.b29 + 192*m.b15*m.b16*m.b29*m.b30 + 128*m.b15*m.b16*m.b30*m.b31 + 64*
                       m.b15*m.b16*m.b31*m.b32 + 832*m.b15*m.b17*m.b18*m.b20 + 768*m.b15*m.b17*m.b19*m.b21 + 704*m.b15*
                       m.b17*m.b20*m.b22 + 640*m.b15*m.b17*m.b21*m.b23 + 576*m.b15*m.b17*m.b22*m.b24 + 512*m.b15*m.b17*
                       m.b23*m.b25 + 448*m.b15*m.b17*m.b24*m.b26 + 384*m.b15*m.b17*m.b25*m.b27 + 320*m.b15*m.b17*m.b26*
                       m.b28 + 256*m.b15*m.b17*m.b27*m.b29 + 192*m.b15*m.b17*m.b28*m.b30 + 128*m.b15*m.b17*m.b29*m.b31
                        + 64*m.b15*m.b17*m.b30*m.b32 + 704*m.b15*m.b18*m.b19*m.b22 + 640*m.b15*m.b18*m.b20*m.b23 + 576*
                       m.b15*m.b18*m.b21*m.b24 + 512*m.b15*m.b18*m.b22*m.b25 + 448*m.b15*m.b18*m.b23*m.b26 + 384*m.b15*
                       m.b18*m.b24*m.b27 + 320*m.b15*m.b18*m.b25*m.b28 + 256*m.b15*m.b18*m.b26*m.b29 + 192*m.b15*m.b18*
                       m.b27*m.b30 + 128*m.b15*m.b18*m.b28*m.b31 + 64*m.b15*m.b18*m.b29*m.b32 + 576*m.b15*m.b19*m.b20*
                       m.b24 + 512*m.b15*m.b19*m.b21*m.b25 + 448*m.b15*m.b19*m.b22*m.b26 + 384*m.b15*m.b19*m.b23*m.b27
                        + 320*m.b15*m.b19*m.b24*m.b28 + 256*m.b15*m.b19*m.b25*m.b29 + 192*m.b15*m.b19*m.b26*m.b30 + 128*
                       m.b15*m.b19*m.b27*m.b31 + 64*m.b15*m.b19*m.b28*m.b32 + 448*m.b15*m.b20*m.b21*m.b26 + 384*m.b15*
                       m.b20*m.b22*m.b27 + 320*m.b15*m.b20*m.b23*m.b28 + 256*m.b15*m.b20*m.b24*m.b29 + 192*m.b15*m.b20*
                       m.b25*m.b30 + 128*m.b15*m.b20*m.b26*m.b31 + 64*m.b15*m.b20*m.b27*m.b32 + 320*m.b15*m.b21*m.b22*
                       m.b28 + 256*m.b15*m.b21*m.b23*m.b29 + 192*m.b15*m.b21*m.b24*m.b30 + 128*m.b15*m.b21*m.b25*m.b31
                        + 64*m.b15*m.b21*m.b26*m.b32 + 192*m.b15*m.b22*m.b23*m.b30 + 128*m.b15*m.b22*m.b24*m.b31 + 64*
                       m.b15*m.b22*m.b25*m.b32 + 64*m.b15*m.b23*m.b24*m.b32 + 960*m.b16*m.b17*m.b18*m.b19 + 896*m.b16*
                       m.b17*m.b19*m.b20 + 832*m.b16*m.b17*m.b20*m.b21 + 768*m.b16*m.b17*m.b21*m.b22 + 704*m.b16*m.b17*
                       m.b22*m.b23 + 640*m.b16*m.b17*m.b23*m.b24 + 576*m.b16*m.b17*m.b24*m.b25 + 512*m.b16*m.b17*m.b25*
                       m.b26 + 448*m.b16*m.b17*m.b26*m.b27 + 384*m.b16*m.b17*m.b27*m.b28 + 320*m.b16*m.b17*m.b28*m.b29
                        + 256*m.b16*m.b17*m.b29*m.b30 + 192*m.b16*m.b17*m.b30*m.b31 + 128*m.b16*m.b17*m.b31*m.b32 + 64*
                       m.b16*m.b17*m.b32*m.b33 + 832*m.b16*m.b18*m.b19*m.b21 + 768*m.b16*m.b18*m.b20*m.b22 + 704*m.b16*
                       m.b18*m.b21*m.b23 + 640*m.b16*m.b18*m.b22*m.b24 + 576*m.b16*m.b18*m.b23*m.b25 + 512*m.b16*m.b18*
                       m.b24*m.b26 + 448*m.b16*m.b18*m.b25*m.b27 + 384*m.b16*m.b18*m.b26*m.b28 + 320*m.b16*m.b18*m.b27*
                       m.b29 + 256*m.b16*m.b18*m.b28*m.b30 + 192*m.b16*m.b18*m.b29*m.b31 + 128*m.b16*m.b18*m.b30*m.b32
                        + 64*m.b16*m.b18*m.b31*m.b33 + 704*m.b16*m.b19*m.b20*m.b23 + 640*m.b16*m.b19*m.b21*m.b24 + 576*
                       m.b16*m.b19*m.b22*m.b25 + 512*m.b16*m.b19*m.b23*m.b26 + 448*m.b16*m.b19*m.b24*m.b27 + 384*m.b16*
                       m.b19*m.b25*m.b28 + 320*m.b16*m.b19*m.b26*m.b29 + 256*m.b16*m.b19*m.b27*m.b30 + 192*m.b16*m.b19*
                       m.b28*m.b31 + 128*m.b16*m.b19*m.b29*m.b32 + 64*m.b16*m.b19*m.b30*m.b33 + 576*m.b16*m.b20*m.b21*
                       m.b25 + 512*m.b16*m.b20*m.b22*m.b26 + 448*m.b16*m.b20*m.b23*m.b27 + 384*m.b16*m.b20*m.b24*m.b28
                        + 320*m.b16*m.b20*m.b25*m.b29 + 256*m.b16*m.b20*m.b26*m.b30 + 192*m.b16*m.b20*m.b27*m.b31 + 128*
                       m.b16*m.b20*m.b28*m.b32 + 64*m.b16*m.b20*m.b29*m.b33 + 448*m.b16*m.b21*m.b22*m.b27 + 384*m.b16*
                       m.b21*m.b23*m.b28 + 320*m.b16*m.b21*m.b24*m.b29 + 256*m.b16*m.b21*m.b25*m.b30 + 192*m.b16*m.b21*
                       m.b26*m.b31 + 128*m.b16*m.b21*m.b27*m.b32 + 64*m.b16*m.b21*m.b28*m.b33 + 320*m.b16*m.b22*m.b23*
                       m.b29 + 256*m.b16*m.b22*m.b24*m.b30 + 192*m.b16*m.b22*m.b25*m.b31 + 128*m.b16*m.b22*m.b26*m.b32
                        + 64*m.b16*m.b22*m.b27*m.b33 + 192*m.b16*m.b23*m.b24*m.b31 + 128*m.b16*m.b23*m.b25*m.b32 + 64*
                       m.b16*m.b23*m.b26*m.b33 + 64*m.b16*m.b24*m.b25*m.b33 + 960*m.b17*m.b18*m.b19*m.b20 + 896*m.b17*
                       m.b18*m.b20*m.b21 + 832*m.b17*m.b18*m.b21*m.b22 + 768*m.b17*m.b18*m.b22*m.b23 + 704*m.b17*m.b18*
                       m.b23*m.b24 + 640*m.b17*m.b18*m.b24*m.b25 + 576*m.b17*m.b18*m.b25*m.b26 + 512*m.b17*m.b18*m.b26*
                       m.b27 + 448*m.b17*m.b18*m.b27*m.b28 + 384*m.b17*m.b18*m.b28*m.b29 + 320*m.b17*m.b18*m.b29*m.b30
                        + 256*m.b17*m.b18*m.b30*m.b31 + 192*m.b17*m.b18*m.b31*m.b32 + 128*m.b17*m.b18*m.b32*m.b33 + 64*
                       m.b17*m.b18*m.b33*m.b34 + 832*m.b17*m.b19*m.b20*m.b22 + 768*m.b17*m.b19*m.b21*m.b23 + 704*m.b17*
                       m.b19*m.b22*m.b24 + 640*m.b17*m.b19*m.b23*m.b25 + 576*m.b17*m.b19*m.b24*m.b26 + 512*m.b17*m.b19*
                       m.b25*m.b27 + 448*m.b17*m.b19*m.b26*m.b28 + 384*m.b17*m.b19*m.b27*m.b29 + 320*m.b17*m.b19*m.b28*
                       m.b30 + 256*m.b17*m.b19*m.b29*m.b31 + 192*m.b17*m.b19*m.b30*m.b32 + 128*m.b17*m.b19*m.b31*m.b33
                        + 64*m.b17*m.b19*m.b32*m.b34 + 704*m.b17*m.b20*m.b21*m.b24 + 640*m.b17*m.b20*m.b22*m.b25 + 576*
                       m.b17*m.b20*m.b23*m.b26 + 512*m.b17*m.b20*m.b24*m.b27 + 448*m.b17*m.b20*m.b25*m.b28 + 384*m.b17*
                       m.b20*m.b26*m.b29 + 320*m.b17*m.b20*m.b27*m.b30 + 256*m.b17*m.b20*m.b28*m.b31 + 192*m.b17*m.b20*
                       m.b29*m.b32 + 128*m.b17*m.b20*m.b30*m.b33 + 64*m.b17*m.b20*m.b31*m.b34 + 576*m.b17*m.b21*m.b22*
                       m.b26 + 512*m.b17*m.b21*m.b23*m.b27 + 448*m.b17*m.b21*m.b24*m.b28 + 384*m.b17*m.b21*m.b25*m.b29
                        + 320*m.b17*m.b21*m.b26*m.b30 + 256*m.b17*m.b21*m.b27*m.b31 + 192*m.b17*m.b21*m.b28*m.b32 + 128*
                       m.b17*m.b21*m.b29*m.b33 + 64*m.b17*m.b21*m.b30*m.b34 + 448*m.b17*m.b22*m.b23*m.b28 + 384*m.b17*
                       m.b22*m.b24*m.b29 + 320*m.b17*m.b22*m.b25*m.b30 + 256*m.b17*m.b22*m.b26*m.b31 + 192*m.b17*m.b22*
                       m.b27*m.b32 + 128*m.b17*m.b22*m.b28*m.b33 + 64*m.b17*m.b22*m.b29*m.b34 + 320*m.b17*m.b23*m.b24*
                       m.b30 + 256*m.b17*m.b23*m.b25*m.b31 + 192*m.b17*m.b23*m.b26*m.b32 + 128*m.b17*m.b23*m.b27*m.b33
                        + 64*m.b17*m.b23*m.b28*m.b34 + 192*m.b17*m.b24*m.b25*m.b32 + 128*m.b17*m.b24*m.b26*m.b33 + 64*
                       m.b17*m.b24*m.b27*m.b34 + 64*m.b17*m.b25*m.b26*m.b34 + 960*m.b18*m.b19*m.b20*m.b21 + 896*m.b18*
                       m.b19*m.b21*m.b22 + 832*m.b18*m.b19*m.b22*m.b23 + 768*m.b18*m.b19*m.b23*m.b24 + 704*m.b18*m.b19*
                       m.b24*m.b25 + 640*m.b18*m.b19*m.b25*m.b26 + 576*m.b18*m.b19*m.b26*m.b27 + 512*m.b18*m.b19*m.b27*
                       m.b28 + 448*m.b18*m.b19*m.b28*m.b29 + 384*m.b18*m.b19*m.b29*m.b30 + 320*m.b18*m.b19*m.b30*m.b31
                        + 256*m.b18*m.b19*m.b31*m.b32 + 192*m.b18*m.b19*m.b32*m.b33 + 128*m.b18*m.b19*m.b33*m.b34 + 64*
                       m.b18*m.b19*m.b34*m.b35 + 832*m.b18*m.b20*m.b21*m.b23 + 768*m.b18*m.b20*m.b22*m.b24 + 704*m.b18*
                       m.b20*m.b23*m.b25 + 640*m.b18*m.b20*m.b24*m.b26 + 576*m.b18*m.b20*m.b25*m.b27 + 512*m.b18*m.b20*
                       m.b26*m.b28 + 448*m.b18*m.b20*m.b27*m.b29 + 384*m.b18*m.b20*m.b28*m.b30 + 320*m.b18*m.b20*m.b29*
                       m.b31 + 256*m.b18*m.b20*m.b30*m.b32 + 192*m.b18*m.b20*m.b31*m.b33 + 128*m.b18*m.b20*m.b32*m.b34
                        + 64*m.b18*m.b20*m.b33*m.b35 + 704*m.b18*m.b21*m.b22*m.b25 + 640*m.b18*m.b21*m.b23*m.b26 + 576*
                       m.b18*m.b21*m.b24*m.b27 + 512*m.b18*m.b21*m.b25*m.b28 + 448*m.b18*m.b21*m.b26*m.b29 + 384*m.b18*
                       m.b21*m.b27*m.b30 + 320*m.b18*m.b21*m.b28*m.b31 + 256*m.b18*m.b21*m.b29*m.b32 + 192*m.b18*m.b21*
                       m.b30*m.b33 + 128*m.b18*m.b21*m.b31*m.b34 + 64*m.b18*m.b21*m.b32*m.b35 + 576*m.b18*m.b22*m.b23*
                       m.b27 + 512*m.b18*m.b22*m.b24*m.b28 + 448*m.b18*m.b22*m.b25*m.b29 + 384*m.b18*m.b22*m.b26*m.b30
                        + 320*m.b18*m.b22*m.b27*m.b31 + 256*m.b18*m.b22*m.b28*m.b32 + 192*m.b18*m.b22*m.b29*m.b33 + 128*
                       m.b18*m.b22*m.b30*m.b34 + 64*m.b18*m.b22*m.b31*m.b35 + 448*m.b18*m.b23*m.b24*m.b29 + 384*m.b18*
                       m.b23*m.b25*m.b30 + 320*m.b18*m.b23*m.b26*m.b31 + 256*m.b18*m.b23*m.b27*m.b32 + 192*m.b18*m.b23*
                       m.b28*m.b33 + 128*m.b18*m.b23*m.b29*m.b34 + 64*m.b18*m.b23*m.b30*m.b35 + 320*m.b18*m.b24*m.b25*
                       m.b31 + 256*m.b18*m.b24*m.b26*m.b32 + 192*m.b18*m.b24*m.b27*m.b33 + 128*m.b18*m.b24*m.b28*m.b34
                        + 64*m.b18*m.b24*m.b29*m.b35 + 192*m.b18*m.b25*m.b26*m.b33 + 128*m.b18*m.b25*m.b27*m.b34 + 64*
                       m.b18*m.b25*m.b28*m.b35 + 64*m.b18*m.b26*m.b27*m.b35 + 896*m.b19*m.b20*m.b21*m.b22 + 832*m.b19*
                       m.b20*m.b22*m.b23 + 768*m.b19*m.b20*m.b23*m.b24 + 704*m.b19*m.b20*m.b24*m.b25 + 640*m.b19*m.b20*
                       m.b25*m.b26 + 576*m.b19*m.b20*m.b26*m.b27 + 512*m.b19*m.b20*m.b27*m.b28 + 448*m.b19*m.b20*m.b28*
                       m.b29 + 384*m.b19*m.b20*m.b29*m.b30 + 320*m.b19*m.b20*m.b30*m.b31 + 256*m.b19*m.b20*m.b31*m.b32
                        + 192*m.b19*m.b20*m.b32*m.b33 + 128*m.b19*m.b20*m.b33*m.b34 + 64*m.b19*m.b20*m.b34*m.b35 + 768*
                       m.b19*m.b21*m.b22*m.b24 + 704*m.b19*m.b21*m.b23*m.b25 + 640*m.b19*m.b21*m.b24*m.b26 + 576*m.b19*
                       m.b21*m.b25*m.b27 + 512*m.b19*m.b21*m.b26*m.b28 + 448*m.b19*m.b21*m.b27*m.b29 + 384*m.b19*m.b21*
                       m.b28*m.b30 + 320*m.b19*m.b21*m.b29*m.b31 + 256*m.b19*m.b21*m.b30*m.b32 + 192*m.b19*m.b21*m.b31*
                       m.b33 + 128*m.b19*m.b21*m.b32*m.b34 + 64*m.b19*m.b21*m.b33*m.b35 + 640*m.b19*m.b22*m.b23*m.b26 + 
                       576*m.b19*m.b22*m.b24*m.b27 + 512*m.b19*m.b22*m.b25*m.b28 + 448*m.b19*m.b22*m.b26*m.b29 + 384*
                       m.b19*m.b22*m.b27*m.b30 + 320*m.b19*m.b22*m.b28*m.b31 + 256*m.b19*m.b22*m.b29*m.b32 + 192*m.b19*
                       m.b22*m.b30*m.b33 + 128*m.b19*m.b22*m.b31*m.b34 + 64*m.b19*m.b22*m.b32*m.b35 + 512*m.b19*m.b23*
                       m.b24*m.b28 + 448*m.b19*m.b23*m.b25*m.b29 + 384*m.b19*m.b23*m.b26*m.b30 + 320*m.b19*m.b23*m.b27*
                       m.b31 + 256*m.b19*m.b23*m.b28*m.b32 + 192*m.b19*m.b23*m.b29*m.b33 + 128*m.b19*m.b23*m.b30*m.b34
                        + 64*m.b19*m.b23*m.b31*m.b35 + 384*m.b19*m.b24*m.b25*m.b30 + 320*m.b19*m.b24*m.b26*m.b31 + 256*
                       m.b19*m.b24*m.b27*m.b32 + 192*m.b19*m.b24*m.b28*m.b33 + 128*m.b19*m.b24*m.b29*m.b34 + 64*m.b19*
                       m.b24*m.b30*m.b35 + 256*m.b19*m.b25*m.b26*m.b32 + 192*m.b19*m.b25*m.b27*m.b33 + 128*m.b19*m.b25*
                       m.b28*m.b34 + 64*m.b19*m.b25*m.b29*m.b35 + 128*m.b19*m.b26*m.b27*m.b34 + 64*m.b19*m.b26*m.b28*
                       m.b35 + 832*m.b20*m.b21*m.b22*m.b23 + 768*m.b20*m.b21*m.b23*m.b24 + 704*m.b20*m.b21*m.b24*m.b25
                        + 640*m.b20*m.b21*m.b25*m.b26 + 576*m.b20*m.b21*m.b26*m.b27 + 512*m.b20*m.b21*m.b27*m.b28 + 448*
                       m.b20*m.b21*m.b28*m.b29 + 384*m.b20*m.b21*m.b29*m.b30 + 320*m.b20*m.b21*m.b30*m.b31 + 256*m.b20*
                       m.b21*m.b31*m.b32 + 192*m.b20*m.b21*m.b32*m.b33 + 128*m.b20*m.b21*m.b33*m.b34 + 64*m.b20*m.b21*
                       m.b34*m.b35 + 704*m.b20*m.b22*m.b23*m.b25 + 640*m.b20*m.b22*m.b24*m.b26 + 576*m.b20*m.b22*m.b25*
                       m.b27 + 512*m.b20*m.b22*m.b26*m.b28 + 448*m.b20*m.b22*m.b27*m.b29 + 384*m.b20*m.b22*m.b28*m.b30
                        + 320*m.b20*m.b22*m.b29*m.b31 + 256*m.b20*m.b22*m.b30*m.b32 + 192*m.b20*m.b22*m.b31*m.b33 + 128*
                       m.b20*m.b22*m.b32*m.b34 + 64*m.b20*m.b22*m.b33*m.b35 + 576*m.b20*m.b23*m.b24*m.b27 + 512*m.b20*
                       m.b23*m.b25*m.b28 + 448*m.b20*m.b23*m.b26*m.b29 + 384*m.b20*m.b23*m.b27*m.b30 + 320*m.b20*m.b23*
                       m.b28*m.b31 + 256*m.b20*m.b23*m.b29*m.b32 + 192*m.b20*m.b23*m.b30*m.b33 + 128*m.b20*m.b23*m.b31*
                       m.b34 + 64*m.b20*m.b23*m.b32*m.b35 + 448*m.b20*m.b24*m.b25*m.b29 + 384*m.b20*m.b24*m.b26*m.b30 + 
                       320*m.b20*m.b24*m.b27*m.b31 + 256*m.b20*m.b24*m.b28*m.b32 + 192*m.b20*m.b24*m.b29*m.b33 + 128*
                       m.b20*m.b24*m.b30*m.b34 + 64*m.b20*m.b24*m.b31*m.b35 + 320*m.b20*m.b25*m.b26*m.b31 + 256*m.b20*
                       m.b25*m.b27*m.b32 + 192*m.b20*m.b25*m.b28*m.b33 + 128*m.b20*m.b25*m.b29*m.b34 + 64*m.b20*m.b25*
                       m.b30*m.b35 + 192*m.b20*m.b26*m.b27*m.b33 + 128*m.b20*m.b26*m.b28*m.b34 + 64*m.b20*m.b26*m.b29*
                       m.b35 + 64*m.b20*m.b27*m.b28*m.b35 + 768*m.b21*m.b22*m.b23*m.b24 + 704*m.b21*m.b22*m.b24*m.b25 + 
                       640*m.b21*m.b22*m.b25*m.b26 + 576*m.b21*m.b22*m.b26*m.b27 + 512*m.b21*m.b22*m.b27*m.b28 + 448*
                       m.b21*m.b22*m.b28*m.b29 + 384*m.b21*m.b22*m.b29*m.b30 + 320*m.b21*m.b22*m.b30*m.b31 + 256*m.b21*
                       m.b22*m.b31*m.b32 + 192*m.b21*m.b22*m.b32*m.b33 + 128*m.b21*m.b22*m.b33*m.b34 + 64*m.b21*m.b22*
                       m.b34*m.b35 + 640*m.b21*m.b23*m.b24*m.b26 + 576*m.b21*m.b23*m.b25*m.b27 + 512*m.b21*m.b23*m.b26*
                       m.b28 + 448*m.b21*m.b23*m.b27*m.b29 + 384*m.b21*m.b23*m.b28*m.b30 + 320*m.b21*m.b23*m.b29*m.b31
                        + 256*m.b21*m.b23*m.b30*m.b32 + 192*m.b21*m.b23*m.b31*m.b33 + 128*m.b21*m.b23*m.b32*m.b34 + 64*
                       m.b21*m.b23*m.b33*m.b35 + 512*m.b21*m.b24*m.b25*m.b28 + 448*m.b21*m.b24*m.b26*m.b29 + 384*m.b21*
                       m.b24*m.b27*m.b30 + 320*m.b21*m.b24*m.b28*m.b31 + 256*m.b21*m.b24*m.b29*m.b32 + 192*m.b21*m.b24*
                       m.b30*m.b33 + 128*m.b21*m.b24*m.b31*m.b34 + 64*m.b21*m.b24*m.b32*m.b35 + 384*m.b21*m.b25*m.b26*
                       m.b30 + 320*m.b21*m.b25*m.b27*m.b31 + 256*m.b21*m.b25*m.b28*m.b32 + 192*m.b21*m.b25*m.b29*m.b33
                        + 128*m.b21*m.b25*m.b30*m.b34 + 64*m.b21*m.b25*m.b31*m.b35 + 256*m.b21*m.b26*m.b27*m.b32 + 192*
                       m.b21*m.b26*m.b28*m.b33 + 128*m.b21*m.b26*m.b29*m.b34 + 64*m.b21*m.b26*m.b30*m.b35 + 128*m.b21*
                       m.b27*m.b28*m.b34 + 64*m.b21*m.b27*m.b29*m.b35 + 704*m.b22*m.b23*m.b24*m.b25 + 640*m.b22*m.b23*
                       m.b25*m.b26 + 576*m.b22*m.b23*m.b26*m.b27 + 512*m.b22*m.b23*m.b27*m.b28 + 448*m.b22*m.b23*m.b28*
                       m.b29 + 384*m.b22*m.b23*m.b29*m.b30 + 320*m.b22*m.b23*m.b30*m.b31 + 256*m.b22*m.b23*m.b31*m.b32
                        + 192*m.b22*m.b23*m.b32*m.b33 + 128*m.b22*m.b23*m.b33*m.b34 + 64*m.b22*m.b23*m.b34*m.b35 + 576*
                       m.b22*m.b24*m.b25*m.b27 + 512*m.b22*m.b24*m.b26*m.b28 + 448*m.b22*m.b24*m.b27*m.b29 + 384*m.b22*
                       m.b24*m.b28*m.b30 + 320*m.b22*m.b24*m.b29*m.b31 + 256*m.b22*m.b24*m.b30*m.b32 + 192*m.b22*m.b24*
                       m.b31*m.b33 + 128*m.b22*m.b24*m.b32*m.b34 + 64*m.b22*m.b24*m.b33*m.b35 + 448*m.b22*m.b25*m.b26*
                       m.b29 + 384*m.b22*m.b25*m.b27*m.b30 + 320*m.b22*m.b25*m.b28*m.b31 + 256*m.b22*m.b25*m.b29*m.b32
                        + 192*m.b22*m.b25*m.b30*m.b33 + 128*m.b22*m.b25*m.b31*m.b34 + 64*m.b22*m.b25*m.b32*m.b35 + 320*
                       m.b22*m.b26*m.b27*m.b31 + 256*m.b22*m.b26*m.b28*m.b32 + 192*m.b22*m.b26*m.b29*m.b33 + 128*m.b22*
                       m.b26*m.b30*m.b34 + 64*m.b22*m.b26*m.b31*m.b35 + 192*m.b22*m.b27*m.b28*m.b33 + 128*m.b22*m.b27*
                       m.b29*m.b34 + 64*m.b22*m.b27*m.b30*m.b35 + 64*m.b22*m.b28*m.b29*m.b35 + 640*m.b23*m.b24*m.b25*
                       m.b26 + 576*m.b23*m.b24*m.b26*m.b27 + 512*m.b23*m.b24*m.b27*m.b28 + 448*m.b23*m.b24*m.b28*m.b29
                        + 384*m.b23*m.b24*m.b29*m.b30 + 320*m.b23*m.b24*m.b30*m.b31 + 256*m.b23*m.b24*m.b31*m.b32 + 192*
                       m.b23*m.b24*m.b32*m.b33 + 128*m.b23*m.b24*m.b33*m.b34 + 64*m.b23*m.b24*m.b34*m.b35 + 512*m.b23*
                       m.b25*m.b26*m.b28 + 448*m.b23*m.b25*m.b27*m.b29 + 384*m.b23*m.b25*m.b28*m.b30 + 320*m.b23*m.b25*
                       m.b29*m.b31 + 256*m.b23*m.b25*m.b30*m.b32 + 192*m.b23*m.b25*m.b31*m.b33 + 128*m.b23*m.b25*m.b32*
                       m.b34 + 64*m.b23*m.b25*m.b33*m.b35 + 384*m.b23*m.b26*m.b27*m.b30 + 320*m.b23*m.b26*m.b28*m.b31 + 
                       256*m.b23*m.b26*m.b29*m.b32 + 192*m.b23*m.b26*m.b30*m.b33 + 128*m.b23*m.b26*m.b31*m.b34 + 64*
                       m.b23*m.b26*m.b32*m.b35 + 256*m.b23*m.b27*m.b28*m.b32 + 192*m.b23*m.b27*m.b29*m.b33 + 128*m.b23*
                       m.b27*m.b30*m.b34 + 64*m.b23*m.b27*m.b31*m.b35 + 128*m.b23*m.b28*m.b29*m.b34 + 64*m.b23*m.b28*
                       m.b30*m.b35 + 576*m.b24*m.b25*m.b26*m.b27 + 512*m.b24*m.b25*m.b27*m.b28 + 448*m.b24*m.b25*m.b28*
                       m.b29 + 384*m.b24*m.b25*m.b29*m.b30 + 320*m.b24*m.b25*m.b30*m.b31 + 256*m.b24*m.b25*m.b31*m.b32
                        + 192*m.b24*m.b25*m.b32*m.b33 + 128*m.b24*m.b25*m.b33*m.b34 + 64*m.b24*m.b25*m.b34*m.b35 + 448*
                       m.b24*m.b26*m.b27*m.b29 + 384*m.b24*m.b26*m.b28*m.b30 + 320*m.b24*m.b26*m.b29*m.b31 + 256*m.b24*
                       m.b26*m.b30*m.b32 + 192*m.b24*m.b26*m.b31*m.b33 + 128*m.b24*m.b26*m.b32*m.b34 + 64*m.b24*m.b26*
                       m.b33*m.b35 + 320*m.b24*m.b27*m.b28*m.b31 + 256*m.b24*m.b27*m.b29*m.b32 + 192*m.b24*m.b27*m.b30*
                       m.b33 + 128*m.b24*m.b27*m.b31*m.b34 + 64*m.b24*m.b27*m.b32*m.b35 + 192*m.b24*m.b28*m.b29*m.b33 + 
                       128*m.b24*m.b28*m.b30*m.b34 + 64*m.b24*m.b28*m.b31*m.b35 + 64*m.b24*m.b29*m.b30*m.b35 + 512*m.b25
                       *m.b26*m.b27*m.b28 + 448*m.b25*m.b26*m.b28*m.b29 + 384*m.b25*m.b26*m.b29*m.b30 + 320*m.b25*m.b26*
                       m.b30*m.b31 + 256*m.b25*m.b26*m.b31*m.b32 + 192*m.b25*m.b26*m.b32*m.b33 + 128*m.b25*m.b26*m.b33*
                       m.b34 + 64*m.b25*m.b26*m.b34*m.b35 + 384*m.b25*m.b27*m.b28*m.b30 + 320*m.b25*m.b27*m.b29*m.b31 + 
                       256*m.b25*m.b27*m.b30*m.b32 + 192*m.b25*m.b27*m.b31*m.b33 + 128*m.b25*m.b27*m.b32*m.b34 + 64*
                       m.b25*m.b27*m.b33*m.b35 + 256*m.b25*m.b28*m.b29*m.b32 + 192*m.b25*m.b28*m.b30*m.b33 + 128*m.b25*
                       m.b28*m.b31*m.b34 + 64*m.b25*m.b28*m.b32*m.b35 + 128*m.b25*m.b29*m.b30*m.b34 + 64*m.b25*m.b29*
                       m.b31*m.b35 + 448*m.b26*m.b27*m.b28*m.b29 + 384*m.b26*m.b27*m.b29*m.b30 + 320*m.b26*m.b27*m.b30*
                       m.b31 + 256*m.b26*m.b27*m.b31*m.b32 + 192*m.b26*m.b27*m.b32*m.b33 + 128*m.b26*m.b27*m.b33*m.b34
                        + 64*m.b26*m.b27*m.b34*m.b35 + 320*m.b26*m.b28*m.b29*m.b31 + 256*m.b26*m.b28*m.b30*m.b32 + 192*
                       m.b26*m.b28*m.b31*m.b33 + 128*m.b26*m.b28*m.b32*m.b34 + 64*m.b26*m.b28*m.b33*m.b35 + 192*m.b26*
                       m.b29*m.b30*m.b33 + 128*m.b26*m.b29*m.b31*m.b34 + 64*m.b26*m.b29*m.b32*m.b35 + 64*m.b26*m.b30*
                       m.b31*m.b35 + 384*m.b27*m.b28*m.b29*m.b30 + 320*m.b27*m.b28*m.b30*m.b31 + 256*m.b27*m.b28*m.b31*
                       m.b32 + 192*m.b27*m.b28*m.b32*m.b33 + 128*m.b27*m.b28*m.b33*m.b34 + 64*m.b27*m.b28*m.b34*m.b35 + 
                       256*m.b27*m.b29*m.b30*m.b32 + 192*m.b27*m.b29*m.b31*m.b33 + 128*m.b27*m.b29*m.b32*m.b34 + 64*
                       m.b27*m.b29*m.b33*m.b35 + 128*m.b27*m.b30*m.b31*m.b34 + 64*m.b27*m.b30*m.b32*m.b35 + 320*m.b28*
                       m.b29*m.b30*m.b31 + 256*m.b28*m.b29*m.b31*m.b32 + 192*m.b28*m.b29*m.b32*m.b33 + 128*m.b28*m.b29*
                       m.b33*m.b34 + 64*m.b28*m.b29*m.b34*m.b35 + 192*m.b28*m.b30*m.b31*m.b33 + 128*m.b28*m.b30*m.b32*
                       m.b34 + 64*m.b28*m.b30*m.b33*m.b35 + 64*m.b28*m.b31*m.b32*m.b35 + 256*m.b29*m.b30*m.b31*m.b32 + 
                       192*m.b29*m.b30*m.b32*m.b33 + 128*m.b29*m.b30*m.b33*m.b34 + 64*m.b29*m.b30*m.b34*m.b35 + 128*
                       m.b29*m.b31*m.b32*m.b34 + 64*m.b29*m.b31*m.b33*m.b35 + 192*m.b30*m.b31*m.b32*m.b33 + 128*m.b30*
                       m.b31*m.b33*m.b34 + 64*m.b30*m.b31*m.b34*m.b35 + 64*m.b30*m.b32*m.b33*m.b35 + 128*m.b31*m.b32*
                       m.b33*m.b34 + 64*m.b31*m.b32*m.b34*m.b35 + 64*m.b32*m.b33*m.b34*m.b35 - 32*m.b1*m.b2*m.b3 - 64*
                       m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 
                       64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1*m.b2*
                       m.b13 - 64*m.b1*m.b2*m.b14 - 64*m.b1*m.b2*m.b15 - 64*m.b1*m.b2*m.b16 - 64*m.b1*m.b2*m.b17 - 32*
                       m.b1*m.b2*m.b18 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7
                        - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*m.b11 - 64*m.b1*m.b3
                       *m.b12 - 64*m.b1*m.b3*m.b13 - 64*m.b1*m.b3*m.b14 - 64*m.b1*m.b3*m.b15 - 64*m.b1*m.b3*m.b16 - 32*
                       m.b1*m.b3*m.b17 - 32*m.b1*m.b3*m.b18 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b7
                        - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64*m.b1*m.b4
                       *m.b12 - 64*m.b1*m.b4*m.b13 - 64*m.b1*m.b4*m.b14 - 64*m.b1*m.b4*m.b15 - 32*m.b1*m.b4*m.b16 - 32*
                       m.b1*m.b4*m.b17 - 32*m.b1*m.b4*m.b18 - 64*m.b1*m.b5*m.b6 - 64*m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8
                        - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 64*m.b1*m.b5*m.b11 - 64*m.b1*m.b5*m.b12 - 64*m.b1*
                       m.b5*m.b13 - 64*m.b1*m.b5*m.b14 - 32*m.b1*m.b5*m.b15 - 32*m.b1*m.b5*m.b16 - 32*m.b1*m.b5*m.b17 - 
                       32*m.b1*m.b5*m.b18 - 64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*
                       m.b10 - 32*m.b1*m.b6*m.b11 - 64*m.b1*m.b6*m.b12 - 64*m.b1*m.b6*m.b13 - 32*m.b1*m.b6*m.b14 - 32*
                       m.b1*m.b6*m.b15 - 32*m.b1*m.b6*m.b16 - 32*m.b1*m.b6*m.b17 - 32*m.b1*m.b6*m.b18 - 64*m.b1*m.b7*
                       m.b8 - 64*m.b1*m.b7*m.b9 - 64*m.b1*m.b7*m.b10 - 64*m.b1*m.b7*m.b11 - 64*m.b1*m.b7*m.b12 - 32*m.b1
                       *m.b7*m.b14 - 32*m.b1*m.b7*m.b15 - 32*m.b1*m.b7*m.b16 - 32*m.b1*m.b7*m.b17 - 32*m.b1*m.b7*m.b18
                        - 64*m.b1*m.b8*m.b9 - 64*m.b1*m.b8*m.b10 - 64*m.b1*m.b8*m.b11 - 32*m.b1*m.b8*m.b12 - 32*m.b1*
                       m.b8*m.b13 - 32*m.b1*m.b8*m.b14 - 32*m.b1*m.b8*m.b16 - 32*m.b1*m.b8*m.b17 - 32*m.b1*m.b8*m.b18 - 
                       64*m.b1*m.b9*m.b10 - 32*m.b1*m.b9*m.b11 - 32*m.b1*m.b9*m.b12 - 32*m.b1*m.b9*m.b13 - 32*m.b1*m.b9*
                       m.b14 - 32*m.b1*m.b9*m.b15 - 32*m.b1*m.b9*m.b16 - 32*m.b1*m.b9*m.b18 - 32*m.b1*m.b10*m.b11 - 32*
                       m.b1*m.b10*m.b12 - 32*m.b1*m.b10*m.b13 - 32*m.b1*m.b10*m.b14 - 32*m.b1*m.b10*m.b15 - 32*m.b1*
                       m.b10*m.b16 - 32*m.b1*m.b10*m.b17 - 32*m.b1*m.b10*m.b18 - 32*m.b1*m.b11*m.b12 - 32*m.b1*m.b11*
                       m.b13 - 32*m.b1*m.b11*m.b14 - 32*m.b1*m.b11*m.b15 - 32*m.b1*m.b11*m.b16 - 32*m.b1*m.b11*m.b17 - 
                       32*m.b1*m.b11*m.b18 - 32*m.b1*m.b12*m.b13 - 32*m.b1*m.b12*m.b14 - 32*m.b1*m.b12*m.b15 - 32*m.b1*
                       m.b12*m.b16 - 32*m.b1*m.b12*m.b17 - 32*m.b1*m.b12*m.b18 - 32*m.b1*m.b13*m.b14 - 32*m.b1*m.b13*
                       m.b15 - 32*m.b1*m.b13*m.b16 - 32*m.b1*m.b13*m.b17 - 32*m.b1*m.b13*m.b18 - 32*m.b1*m.b14*m.b15 - 
                       32*m.b1*m.b14*m.b16 - 32*m.b1*m.b14*m.b17 - 32*m.b1*m.b14*m.b18 - 32*m.b1*m.b15*m.b16 - 32*m.b1*
                       m.b15*m.b17 - 32*m.b1*m.b15*m.b18 - 32*m.b1*m.b16*m.b17 - 32*m.b1*m.b16*m.b18 - 32*m.b1*m.b17*
                       m.b18 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*
                       m.b2*m.b3*m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*m.b11 - 128*m.b2*m.b3*
                       m.b12 - 128*m.b2*m.b3*m.b13 - 128*m.b2*m.b3*m.b14 - 128*m.b2*m.b3*m.b15 - 128*m.b2*m.b3*m.b16 - 
                       128*m.b2*m.b3*m.b17 - 96*m.b2*m.b3*m.b18 - 32*m.b2*m.b3*m.b19 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4
                       *m.b6 - 128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 128*m.b2*m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*
                       m.b2*m.b4*m.b11 - 128*m.b2*m.b4*m.b12 - 128*m.b2*m.b4*m.b13 - 128*m.b2*m.b4*m.b14 - 128*m.b2*m.b4
                       *m.b15 - 128*m.b2*m.b4*m.b16 - 96*m.b2*m.b4*m.b17 - 64*m.b2*m.b4*m.b18 - 32*m.b2*m.b4*m.b19 - 160
                       *m.b2*m.b5*m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*
                       m.b10 - 128*m.b2*m.b5*m.b11 - 128*m.b2*m.b5*m.b12 - 128*m.b2*m.b5*m.b13 - 128*m.b2*m.b5*m.b14 - 
                       128*m.b2*m.b5*m.b15 - 96*m.b2*m.b5*m.b16 - 64*m.b2*m.b5*m.b17 - 64*m.b2*m.b5*m.b18 - 32*m.b2*m.b5
                       *m.b19 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*m.b8 - 128*m.b2*m.b6*m.b9 - 64*m.b2*m.b6*m.b10 - 128*
                       m.b2*m.b6*m.b11 - 128*m.b2*m.b6*m.b12 - 128*m.b2*m.b6*m.b13 - 128*m.b2*m.b6*m.b14 - 96*m.b2*m.b6*
                       m.b15 - 64*m.b2*m.b6*m.b16 - 64*m.b2*m.b6*m.b17 - 64*m.b2*m.b6*m.b18 - 32*m.b2*m.b6*m.b19 - 160*
                       m.b2*m.b7*m.b8 - 128*m.b2*m.b7*m.b9 - 128*m.b2*m.b7*m.b10 - 128*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*
                       m.b12 - 128*m.b2*m.b7*m.b13 - 96*m.b2*m.b7*m.b14 - 64*m.b2*m.b7*m.b15 - 64*m.b2*m.b7*m.b16 - 64*
                       m.b2*m.b7*m.b17 - 64*m.b2*m.b7*m.b18 - 32*m.b2*m.b7*m.b19 - 160*m.b2*m.b8*m.b9 - 128*m.b2*m.b8*
                       m.b10 - 128*m.b2*m.b8*m.b11 - 128*m.b2*m.b8*m.b12 - 96*m.b2*m.b8*m.b13 - 64*m.b2*m.b8*m.b15 - 64*
                       m.b2*m.b8*m.b16 - 64*m.b2*m.b8*m.b17 - 64*m.b2*m.b8*m.b18 - 32*m.b2*m.b8*m.b19 - 160*m.b2*m.b9*
                       m.b10 - 128*m.b2*m.b9*m.b11 - 96*m.b2*m.b9*m.b12 - 64*m.b2*m.b9*m.b13 - 64*m.b2*m.b9*m.b14 - 64*
                       m.b2*m.b9*m.b15 - 64*m.b2*m.b9*m.b17 - 64*m.b2*m.b9*m.b18 - 32*m.b2*m.b9*m.b19 - 128*m.b2*m.b10*
                       m.b11 - 64*m.b2*m.b10*m.b12 - 64*m.b2*m.b10*m.b13 - 64*m.b2*m.b10*m.b14 - 64*m.b2*m.b10*m.b15 - 
                       64*m.b2*m.b10*m.b16 - 64*m.b2*m.b10*m.b17 - 32*m.b2*m.b10*m.b19 - 96*m.b2*m.b11*m.b12 - 64*m.b2*
                       m.b11*m.b13 - 64*m.b2*m.b11*m.b14 - 64*m.b2*m.b11*m.b15 - 64*m.b2*m.b11*m.b16 - 64*m.b2*m.b11*
                       m.b17 - 64*m.b2*m.b11*m.b18 - 32*m.b2*m.b11*m.b19 - 96*m.b2*m.b12*m.b13 - 64*m.b2*m.b12*m.b14 - 
                       64*m.b2*m.b12*m.b15 - 64*m.b2*m.b12*m.b16 - 64*m.b2*m.b12*m.b17 - 64*m.b2*m.b12*m.b18 - 32*m.b2*
                       m.b12*m.b19 - 96*m.b2*m.b13*m.b14 - 64*m.b2*m.b13*m.b15 - 64*m.b2*m.b13*m.b16 - 64*m.b2*m.b13*
                       m.b17 - 64*m.b2*m.b13*m.b18 - 32*m.b2*m.b13*m.b19 - 96*m.b2*m.b14*m.b15 - 64*m.b2*m.b14*m.b16 - 
                       64*m.b2*m.b14*m.b17 - 64*m.b2*m.b14*m.b18 - 32*m.b2*m.b14*m.b19 - 96*m.b2*m.b15*m.b16 - 64*m.b2*
                       m.b15*m.b17 - 64*m.b2*m.b15*m.b18 - 32*m.b2*m.b15*m.b19 - 96*m.b2*m.b16*m.b17 - 64*m.b2*m.b16*
                       m.b18 - 32*m.b2*m.b16*m.b19 - 96*m.b2*m.b17*m.b18 - 32*m.b2*m.b17*m.b19 - 32*m.b2*m.b18*m.b19 - 
                       160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4
                       *m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*m.b12 - 192*m.b3*m.b4*m.b13 - 
                       192*m.b3*m.b4*m.b14 - 192*m.b3*m.b4*m.b15 - 192*m.b3*m.b4*m.b16 - 192*m.b3*m.b4*m.b17 - 160*m.b3*
                       m.b4*m.b18 - 96*m.b3*m.b4*m.b19 - 32*m.b3*m.b4*m.b20 - 256*m.b3*m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 
                       192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*m.b10 - 192*m.b3*m.b5*m.b11 - 192*m.b3*
                       m.b5*m.b12 - 192*m.b3*m.b5*m.b13 - 192*m.b3*m.b5*m.b14 - 192*m.b3*m.b5*m.b15 - 192*m.b3*m.b5*
                       m.b16 - 160*m.b3*m.b5*m.b17 - 128*m.b3*m.b5*m.b18 - 64*m.b3*m.b5*m.b19 - 32*m.b3*m.b5*m.b20 - 256
                       *m.b3*m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*m.b9 - 192*m.b3*m.b6*m.b10 - 192*m.b3*m.b6*
                       m.b11 - 192*m.b3*m.b6*m.b12 - 192*m.b3*m.b6*m.b13 - 192*m.b3*m.b6*m.b14 - 192*m.b3*m.b6*m.b15 - 
                       160*m.b3*m.b6*m.b16 - 128*m.b3*m.b6*m.b17 - 96*m.b3*m.b6*m.b18 - 64*m.b3*m.b6*m.b19 - 32*m.b3*
                       m.b6*m.b20 - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 192*m.b3*m.b7*m.b10 - 96*m.b3*m.b7*m.b11
                        - 192*m.b3*m.b7*m.b12 - 192*m.b3*m.b7*m.b13 - 192*m.b3*m.b7*m.b14 - 160*m.b3*m.b7*m.b15 - 128*
                       m.b3*m.b7*m.b16 - 96*m.b3*m.b7*m.b17 - 96*m.b3*m.b7*m.b18 - 64*m.b3*m.b7*m.b19 - 32*m.b3*m.b7*
                       m.b20 - 256*m.b3*m.b8*m.b9 - 224*m.b3*m.b8*m.b10 - 192*m.b3*m.b8*m.b11 - 192*m.b3*m.b8*m.b12 - 96
                       *m.b3*m.b8*m.b13 - 160*m.b3*m.b8*m.b14 - 128*m.b3*m.b8*m.b15 - 96*m.b3*m.b8*m.b16 - 96*m.b3*m.b8*
                       m.b17 - 96*m.b3*m.b8*m.b18 - 64*m.b3*m.b8*m.b19 - 32*m.b3*m.b8*m.b20 - 256*m.b3*m.b9*m.b10 - 224*
                       m.b3*m.b9*m.b11 - 192*m.b3*m.b9*m.b12 - 160*m.b3*m.b9*m.b13 - 128*m.b3*m.b9*m.b14 - 96*m.b3*m.b9*
                       m.b16 - 96*m.b3*m.b9*m.b17 - 96*m.b3*m.b9*m.b18 - 64*m.b3*m.b9*m.b19 - 32*m.b3*m.b9*m.b20 - 256*
                       m.b3*m.b10*m.b11 - 192*m.b3*m.b10*m.b12 - 128*m.b3*m.b10*m.b13 - 96*m.b3*m.b10*m.b14 - 96*m.b3*
                       m.b10*m.b15 - 96*m.b3*m.b10*m.b16 - 96*m.b3*m.b10*m.b18 - 64*m.b3*m.b10*m.b19 - 32*m.b3*m.b10*
                       m.b20 - 192*m.b3*m.b11*m.b12 - 128*m.b3*m.b11*m.b13 - 96*m.b3*m.b11*m.b14 - 96*m.b3*m.b11*m.b15
                        - 96*m.b3*m.b11*m.b16 - 96*m.b3*m.b11*m.b17 - 96*m.b3*m.b11*m.b18 - 32*m.b3*m.b11*m.b20 - 160*
                       m.b3*m.b12*m.b13 - 128*m.b3*m.b12*m.b14 - 96*m.b3*m.b12*m.b15 - 96*m.b3*m.b12*m.b16 - 96*m.b3*
                       m.b12*m.b17 - 96*m.b3*m.b12*m.b18 - 64*m.b3*m.b12*m.b19 - 32*m.b3*m.b12*m.b20 - 160*m.b3*m.b13*
                       m.b14 - 128*m.b3*m.b13*m.b15 - 96*m.b3*m.b13*m.b16 - 96*m.b3*m.b13*m.b17 - 96*m.b3*m.b13*m.b18 - 
                       64*m.b3*m.b13*m.b19 - 32*m.b3*m.b13*m.b20 - 160*m.b3*m.b14*m.b15 - 128*m.b3*m.b14*m.b16 - 96*m.b3
                       *m.b14*m.b17 - 96*m.b3*m.b14*m.b18 - 64*m.b3*m.b14*m.b19 - 32*m.b3*m.b14*m.b20 - 160*m.b3*m.b15*
                       m.b16 - 128*m.b3*m.b15*m.b17 - 96*m.b3*m.b15*m.b18 - 64*m.b3*m.b15*m.b19 - 32*m.b3*m.b15*m.b20 - 
                       160*m.b3*m.b16*m.b17 - 128*m.b3*m.b16*m.b18 - 64*m.b3*m.b16*m.b19 - 32*m.b3*m.b16*m.b20 - 160*
                       m.b3*m.b17*m.b18 - 64*m.b3*m.b17*m.b19 - 32*m.b3*m.b17*m.b20 - 96*m.b3*m.b18*m.b19 - 32*m.b3*
                       m.b18*m.b20 - 32*m.b3*m.b19*m.b20 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8
                        - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 256*m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 256*
                       m.b4*m.b5*m.b13 - 256*m.b4*m.b5*m.b14 - 256*m.b4*m.b5*m.b15 - 256*m.b4*m.b5*m.b16 - 256*m.b4*m.b5
                       *m.b17 - 224*m.b4*m.b5*m.b18 - 160*m.b4*m.b5*m.b19 - 96*m.b4*m.b5*m.b20 - 32*m.b4*m.b5*m.b21 - 
                       352*m.b4*m.b6*m.b7 - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10 - 256*m.b4*
                       m.b6*m.b11 - 256*m.b4*m.b6*m.b12 - 256*m.b4*m.b6*m.b13 - 256*m.b4*m.b6*m.b14 - 256*m.b4*m.b6*
                       m.b15 - 256*m.b4*m.b6*m.b16 - 224*m.b4*m.b6*m.b17 - 192*m.b4*m.b6*m.b18 - 128*m.b4*m.b6*m.b19 - 
                       64*m.b4*m.b6*m.b20 - 32*m.b4*m.b6*m.b21 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*m.b4*m.b7
                       *m.b10 - 256*m.b4*m.b7*m.b11 - 256*m.b4*m.b7*m.b12 - 256*m.b4*m.b7*m.b13 - 256*m.b4*m.b7*m.b14 - 
                       256*m.b4*m.b7*m.b15 - 224*m.b4*m.b7*m.b16 - 192*m.b4*m.b7*m.b17 - 160*m.b4*m.b7*m.b18 - 96*m.b4*
                       m.b7*m.b19 - 64*m.b4*m.b7*m.b20 - 32*m.b4*m.b7*m.b21 - 352*m.b4*m.b8*m.b9 - 320*m.b4*m.b8*m.b10
                        - 288*m.b4*m.b8*m.b11 - 128*m.b4*m.b8*m.b12 - 256*m.b4*m.b8*m.b13 - 256*m.b4*m.b8*m.b14 - 224*
                       m.b4*m.b8*m.b15 - 192*m.b4*m.b8*m.b16 - 160*m.b4*m.b8*m.b17 - 128*m.b4*m.b8*m.b18 - 96*m.b4*m.b8*
                       m.b19 - 64*m.b4*m.b8*m.b20 - 32*m.b4*m.b8*m.b21 - 352*m.b4*m.b9*m.b10 - 320*m.b4*m.b9*m.b11 - 288
                       *m.b4*m.b9*m.b12 - 256*m.b4*m.b9*m.b13 - 96*m.b4*m.b9*m.b14 - 192*m.b4*m.b9*m.b15 - 160*m.b4*m.b9
                       *m.b16 - 128*m.b4*m.b9*m.b17 - 128*m.b4*m.b9*m.b18 - 96*m.b4*m.b9*m.b19 - 64*m.b4*m.b9*m.b20 - 32
                       *m.b4*m.b9*m.b21 - 352*m.b4*m.b10*m.b11 - 320*m.b4*m.b10*m.b12 - 256*m.b4*m.b10*m.b13 - 192*m.b4*
                       m.b10*m.b14 - 160*m.b4*m.b10*m.b15 - 128*m.b4*m.b10*m.b17 - 128*m.b4*m.b10*m.b18 - 96*m.b4*m.b10*
                       m.b19 - 64*m.b4*m.b10*m.b20 - 32*m.b4*m.b10*m.b21 - 320*m.b4*m.b11*m.b12 - 256*m.b4*m.b11*m.b13
                        - 192*m.b4*m.b11*m.b14 - 128*m.b4*m.b11*m.b15 - 128*m.b4*m.b11*m.b16 - 128*m.b4*m.b11*m.b17 - 96
                       *m.b4*m.b11*m.b19 - 64*m.b4*m.b11*m.b20 - 32*m.b4*m.b11*m.b21 - 256*m.b4*m.b12*m.b13 - 192*m.b4*
                       m.b12*m.b14 - 160*m.b4*m.b12*m.b15 - 128*m.b4*m.b12*m.b16 - 128*m.b4*m.b12*m.b17 - 128*m.b4*m.b12
                       *m.b18 - 96*m.b4*m.b12*m.b19 - 32*m.b4*m.b12*m.b21 - 224*m.b4*m.b13*m.b14 - 192*m.b4*m.b13*m.b15
                        - 160*m.b4*m.b13*m.b16 - 128*m.b4*m.b13*m.b17 - 128*m.b4*m.b13*m.b18 - 96*m.b4*m.b13*m.b19 - 64*
                       m.b4*m.b13*m.b20 - 32*m.b4*m.b13*m.b21 - 224*m.b4*m.b14*m.b15 - 192*m.b4*m.b14*m.b16 - 160*m.b4*
                       m.b14*m.b17 - 128*m.b4*m.b14*m.b18 - 96*m.b4*m.b14*m.b19 - 64*m.b4*m.b14*m.b20 - 32*m.b4*m.b14*
                       m.b21 - 224*m.b4*m.b15*m.b16 - 192*m.b4*m.b15*m.b17 - 160*m.b4*m.b15*m.b18 - 96*m.b4*m.b15*m.b19
                        - 64*m.b4*m.b15*m.b20 - 32*m.b4*m.b15*m.b21 - 224*m.b4*m.b16*m.b17 - 192*m.b4*m.b16*m.b18 - 96*
                       m.b4*m.b16*m.b19 - 64*m.b4*m.b16*m.b20 - 32*m.b4*m.b16*m.b21 - 224*m.b4*m.b17*m.b18 - 128*m.b4*
                       m.b17*m.b19 - 64*m.b4*m.b17*m.b20 - 32*m.b4*m.b17*m.b21 - 160*m.b4*m.b18*m.b19 - 64*m.b4*m.b18*
                       m.b20 - 32*m.b4*m.b18*m.b21 - 96*m.b4*m.b19*m.b20 - 32*m.b4*m.b19*m.b21 - 32*m.b4*m.b20*m.b21 - 
                       288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*m.b5*
                       m.b6*m.b11 - 320*m.b5*m.b6*m.b12 - 320*m.b5*m.b6*m.b13 - 320*m.b5*m.b6*m.b14 - 320*m.b5*m.b6*
                       m.b15 - 320*m.b5*m.b6*m.b16 - 320*m.b5*m.b6*m.b17 - 288*m.b5*m.b6*m.b18 - 224*m.b5*m.b6*m.b19 - 
                       160*m.b5*m.b6*m.b20 - 96*m.b5*m.b6*m.b21 - 32*m.b5*m.b6*m.b22 - 448*m.b5*m.b7*m.b8 - 256*m.b5*
                       m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*m.b5*m.b7*m.b11 - 320*m.b5*m.b7*m.b12 - 320*m.b5*m.b7*m.b13
                        - 320*m.b5*m.b7*m.b14 - 320*m.b5*m.b7*m.b15 - 320*m.b5*m.b7*m.b16 - 288*m.b5*m.b7*m.b17 - 256*
                       m.b5*m.b7*m.b18 - 192*m.b5*m.b7*m.b19 - 128*m.b5*m.b7*m.b20 - 64*m.b5*m.b7*m.b21 - 32*m.b5*m.b7*
                       m.b22 - 448*m.b5*m.b8*m.b9 - 416*m.b5*m.b8*m.b10 - 224*m.b5*m.b8*m.b11 - 352*m.b5*m.b8*m.b12 - 
                       320*m.b5*m.b8*m.b13 - 320*m.b5*m.b8*m.b14 - 320*m.b5*m.b8*m.b15 - 288*m.b5*m.b8*m.b16 - 256*m.b5*
                       m.b8*m.b17 - 224*m.b5*m.b8*m.b18 - 160*m.b5*m.b8*m.b19 - 96*m.b5*m.b8*m.b20 - 64*m.b5*m.b8*m.b21
                        - 32*m.b5*m.b8*m.b22 - 448*m.b5*m.b9*m.b10 - 416*m.b5*m.b9*m.b11 - 384*m.b5*m.b9*m.b12 - 192*
                       m.b5*m.b9*m.b13 - 320*m.b5*m.b9*m.b14 - 288*m.b5*m.b9*m.b15 - 256*m.b5*m.b9*m.b16 - 224*m.b5*m.b9
                       *m.b17 - 192*m.b5*m.b9*m.b18 - 128*m.b5*m.b9*m.b19 - 96*m.b5*m.b9*m.b20 - 64*m.b5*m.b9*m.b21 - 32
                       *m.b5*m.b9*m.b22 - 448*m.b5*m.b10*m.b11 - 416*m.b5*m.b10*m.b12 - 384*m.b5*m.b10*m.b13 - 320*m.b5*
                       m.b10*m.b14 - 96*m.b5*m.b10*m.b15 - 224*m.b5*m.b10*m.b16 - 192*m.b5*m.b10*m.b17 - 160*m.b5*m.b10*
                       m.b18 - 128*m.b5*m.b10*m.b19 - 96*m.b5*m.b10*m.b20 - 64*m.b5*m.b10*m.b21 - 32*m.b5*m.b10*m.b22 - 
                       448*m.b5*m.b11*m.b12 - 384*m.b5*m.b11*m.b13 - 320*m.b5*m.b11*m.b14 - 256*m.b5*m.b11*m.b15 - 192*
                       m.b5*m.b11*m.b16 - 160*m.b5*m.b11*m.b18 - 128*m.b5*m.b11*m.b19 - 96*m.b5*m.b11*m.b20 - 64*m.b5*
                       m.b11*m.b21 - 32*m.b5*m.b11*m.b22 - 384*m.b5*m.b12*m.b13 - 320*m.b5*m.b12*m.b14 - 256*m.b5*m.b12*
                       m.b15 - 192*m.b5*m.b12*m.b16 - 160*m.b5*m.b12*m.b17 - 160*m.b5*m.b12*m.b18 - 96*m.b5*m.b12*m.b20
                        - 64*m.b5*m.b12*m.b21 - 32*m.b5*m.b12*m.b22 - 320*m.b5*m.b13*m.b14 - 256*m.b5*m.b13*m.b15 - 224*
                       m.b5*m.b13*m.b16 - 192*m.b5*m.b13*m.b17 - 160*m.b5*m.b13*m.b18 - 128*m.b5*m.b13*m.b19 - 96*m.b5*
                       m.b13*m.b20 - 32*m.b5*m.b13*m.b22 - 288*m.b5*m.b14*m.b15 - 256*m.b5*m.b14*m.b16 - 224*m.b5*m.b14*
                       m.b17 - 192*m.b5*m.b14*m.b18 - 128*m.b5*m.b14*m.b19 - 96*m.b5*m.b14*m.b20 - 64*m.b5*m.b14*m.b21
                        - 32*m.b5*m.b14*m.b22 - 288*m.b5*m.b15*m.b16 - 256*m.b5*m.b15*m.b17 - 224*m.b5*m.b15*m.b18 - 128
                       *m.b5*m.b15*m.b19 - 96*m.b5*m.b15*m.b20 - 64*m.b5*m.b15*m.b21 - 32*m.b5*m.b15*m.b22 - 288*m.b5*
                       m.b16*m.b17 - 256*m.b5*m.b16*m.b18 - 160*m.b5*m.b16*m.b19 - 96*m.b5*m.b16*m.b20 - 64*m.b5*m.b16*
                       m.b21 - 32*m.b5*m.b16*m.b22 - 288*m.b5*m.b17*m.b18 - 192*m.b5*m.b17*m.b19 - 96*m.b5*m.b17*m.b20
                        - 64*m.b5*m.b17*m.b21 - 32*m.b5*m.b17*m.b22 - 224*m.b5*m.b18*m.b19 - 128*m.b5*m.b18*m.b20 - 64*
                       m.b5*m.b18*m.b21 - 32*m.b5*m.b18*m.b22 - 160*m.b5*m.b19*m.b20 - 64*m.b5*m.b19*m.b21 - 32*m.b5*
                       m.b19*m.b22 - 96*m.b5*m.b20*m.b21 - 32*m.b5*m.b20*m.b22 - 32*m.b5*m.b21*m.b22 - 352*m.b6*m.b7*
                       m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*m.b7*m.b11 - 416*m.b6*m.b7*m.b12 - 384
                       *m.b6*m.b7*m.b13 - 384*m.b6*m.b7*m.b14 - 384*m.b6*m.b7*m.b15 - 384*m.b6*m.b7*m.b16 - 384*m.b6*
                       m.b7*m.b17 - 352*m.b6*m.b7*m.b18 - 288*m.b6*m.b7*m.b19 - 224*m.b6*m.b7*m.b20 - 160*m.b6*m.b7*
                       m.b21 - 96*m.b6*m.b7*m.b22 - 32*m.b6*m.b7*m.b23 - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10 - 480*
                       m.b6*m.b8*m.b11 - 448*m.b6*m.b8*m.b12 - 416*m.b6*m.b8*m.b13 - 384*m.b6*m.b8*m.b14 - 384*m.b6*m.b8
                       *m.b15 - 384*m.b6*m.b8*m.b16 - 352*m.b6*m.b8*m.b17 - 320*m.b6*m.b8*m.b18 - 256*m.b6*m.b8*m.b19 - 
                       192*m.b6*m.b8*m.b20 - 128*m.b6*m.b8*m.b21 - 64*m.b6*m.b8*m.b22 - 32*m.b6*m.b8*m.b23 - 544*m.b6*
                       m.b9*m.b10 - 512*m.b6*m.b9*m.b11 - 288*m.b6*m.b9*m.b12 - 448*m.b6*m.b9*m.b13 - 416*m.b6*m.b9*
                       m.b14 - 384*m.b6*m.b9*m.b15 - 352*m.b6*m.b9*m.b16 - 320*m.b6*m.b9*m.b17 - 288*m.b6*m.b9*m.b18 - 
                       224*m.b6*m.b9*m.b19 - 160*m.b6*m.b9*m.b20 - 96*m.b6*m.b9*m.b21 - 64*m.b6*m.b9*m.b22 - 32*m.b6*
                       m.b9*m.b23 - 544*m.b6*m.b10*m.b11 - 512*m.b6*m.b10*m.b12 - 480*m.b6*m.b10*m.b13 - 256*m.b6*m.b10*
                       m.b14 - 384*m.b6*m.b10*m.b15 - 320*m.b6*m.b10*m.b16 - 288*m.b6*m.b10*m.b17 - 256*m.b6*m.b10*m.b18
                        - 192*m.b6*m.b10*m.b19 - 128*m.b6*m.b10*m.b20 - 96*m.b6*m.b10*m.b21 - 64*m.b6*m.b10*m.b22 - 32*
                       m.b6*m.b10*m.b23 - 544*m.b6*m.b11*m.b12 - 512*m.b6*m.b11*m.b13 - 448*m.b6*m.b11*m.b14 - 384*m.b6*
                       m.b11*m.b15 - 128*m.b6*m.b11*m.b16 - 256*m.b6*m.b11*m.b17 - 224*m.b6*m.b11*m.b18 - 160*m.b6*m.b11
                       *m.b19 - 128*m.b6*m.b11*m.b20 - 96*m.b6*m.b11*m.b21 - 64*m.b6*m.b11*m.b22 - 32*m.b6*m.b11*m.b23
                        - 512*m.b6*m.b12*m.b13 - 448*m.b6*m.b12*m.b14 - 384*m.b6*m.b12*m.b15 - 320*m.b6*m.b12*m.b16 - 
                       256*m.b6*m.b12*m.b17 - 160*m.b6*m.b12*m.b19 - 128*m.b6*m.b12*m.b20 - 96*m.b6*m.b12*m.b21 - 64*
                       m.b6*m.b12*m.b22 - 32*m.b6*m.b12*m.b23 - 448*m.b6*m.b13*m.b14 - 384*m.b6*m.b13*m.b15 - 320*m.b6*
                       m.b13*m.b16 - 256*m.b6*m.b13*m.b17 - 224*m.b6*m.b13*m.b18 - 160*m.b6*m.b13*m.b19 - 96*m.b6*m.b13*
                       m.b21 - 64*m.b6*m.b13*m.b22 - 32*m.b6*m.b13*m.b23 - 384*m.b6*m.b14*m.b15 - 320*m.b6*m.b14*m.b16
                        - 288*m.b6*m.b14*m.b17 - 256*m.b6*m.b14*m.b18 - 160*m.b6*m.b14*m.b19 - 128*m.b6*m.b14*m.b20 - 96
                       *m.b6*m.b14*m.b21 - 32*m.b6*m.b14*m.b23 - 352*m.b6*m.b15*m.b16 - 320*m.b6*m.b15*m.b17 - 288*m.b6*
                       m.b15*m.b18 - 192*m.b6*m.b15*m.b19 - 128*m.b6*m.b15*m.b20 - 96*m.b6*m.b15*m.b21 - 64*m.b6*m.b15*
                       m.b22 - 32*m.b6*m.b15*m.b23 - 352*m.b6*m.b16*m.b17 - 320*m.b6*m.b16*m.b18 - 224*m.b6*m.b16*m.b19
                        - 128*m.b6*m.b16*m.b20 - 96*m.b6*m.b16*m.b21 - 64*m.b6*m.b16*m.b22 - 32*m.b6*m.b16*m.b23 - 352*
                       m.b6*m.b17*m.b18 - 256*m.b6*m.b17*m.b19 - 160*m.b6*m.b17*m.b20 - 96*m.b6*m.b17*m.b21 - 64*m.b6*
                       m.b17*m.b22 - 32*m.b6*m.b17*m.b23 - 288*m.b6*m.b18*m.b19 - 192*m.b6*m.b18*m.b20 - 96*m.b6*m.b18*
                       m.b21 - 64*m.b6*m.b18*m.b22 - 32*m.b6*m.b18*m.b23 - 224*m.b6*m.b19*m.b20 - 128*m.b6*m.b19*m.b21
                        - 64*m.b6*m.b19*m.b22 - 32*m.b6*m.b19*m.b23 - 160*m.b6*m.b20*m.b21 - 64*m.b6*m.b20*m.b22 - 32*
                       m.b6*m.b20*m.b23 - 96*m.b6*m.b21*m.b22 - 32*m.b6*m.b21*m.b23 - 32*m.b6*m.b22*m.b23 - 416*m.b7*
                       m.b8*m.b9 - 608*m.b7*m.b8*m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*m.b8*m.b12 - 512*m.b7*m.b8*m.b13
                        - 480*m.b7*m.b8*m.b14 - 448*m.b7*m.b8*m.b15 - 448*m.b7*m.b8*m.b16 - 448*m.b7*m.b8*m.b17 - 416*
                       m.b7*m.b8*m.b18 - 352*m.b7*m.b8*m.b19 - 288*m.b7*m.b8*m.b20 - 224*m.b7*m.b8*m.b21 - 160*m.b7*m.b8
                       *m.b22 - 96*m.b7*m.b8*m.b23 - 32*m.b7*m.b8*m.b24 - 640*m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 
                       576*m.b7*m.b9*m.b12 - 544*m.b7*m.b9*m.b13 - 512*m.b7*m.b9*m.b14 - 480*m.b7*m.b9*m.b15 - 448*m.b7*
                       m.b9*m.b16 - 416*m.b7*m.b9*m.b17 - 384*m.b7*m.b9*m.b18 - 320*m.b7*m.b9*m.b19 - 256*m.b7*m.b9*
                       m.b20 - 192*m.b7*m.b9*m.b21 - 128*m.b7*m.b9*m.b22 - 64*m.b7*m.b9*m.b23 - 32*m.b7*m.b9*m.b24 - 640
                       *m.b7*m.b10*m.b11 - 608*m.b7*m.b10*m.b12 - 352*m.b7*m.b10*m.b13 - 544*m.b7*m.b10*m.b14 - 512*m.b7
                       *m.b10*m.b15 - 448*m.b7*m.b10*m.b16 - 384*m.b7*m.b10*m.b17 - 352*m.b7*m.b10*m.b18 - 288*m.b7*
                       m.b10*m.b19 - 224*m.b7*m.b10*m.b20 - 160*m.b7*m.b10*m.b21 - 96*m.b7*m.b10*m.b22 - 64*m.b7*m.b10*
                       m.b23 - 32*m.b7*m.b10*m.b24 - 640*m.b7*m.b11*m.b12 - 608*m.b7*m.b11*m.b13 - 576*m.b7*m.b11*m.b14
                        - 288*m.b7*m.b11*m.b15 - 448*m.b7*m.b11*m.b16 - 384*m.b7*m.b11*m.b17 - 320*m.b7*m.b11*m.b18 - 
                       256*m.b7*m.b11*m.b19 - 192*m.b7*m.b11*m.b20 - 128*m.b7*m.b11*m.b21 - 96*m.b7*m.b11*m.b22 - 64*
                       m.b7*m.b11*m.b23 - 32*m.b7*m.b11*m.b24 - 640*m.b7*m.b12*m.b13 - 576*m.b7*m.b12*m.b14 - 512*m.b7*
                       m.b12*m.b15 - 448*m.b7*m.b12*m.b16 - 160*m.b7*m.b12*m.b17 - 320*m.b7*m.b12*m.b18 - 224*m.b7*m.b12
                       *m.b19 - 160*m.b7*m.b12*m.b20 - 128*m.b7*m.b12*m.b21 - 96*m.b7*m.b12*m.b22 - 64*m.b7*m.b12*m.b23
                        - 32*m.b7*m.b12*m.b24 - 576*m.b7*m.b13*m.b14 - 512*m.b7*m.b13*m.b15 - 448*m.b7*m.b13*m.b16 - 384
                       *m.b7*m.b13*m.b17 - 320*m.b7*m.b13*m.b18 - 160*m.b7*m.b13*m.b20 - 128*m.b7*m.b13*m.b21 - 96*m.b7*
                       m.b13*m.b22 - 64*m.b7*m.b13*m.b23 - 32*m.b7*m.b13*m.b24 - 512*m.b7*m.b14*m.b15 - 448*m.b7*m.b14*
                       m.b16 - 384*m.b7*m.b14*m.b17 - 320*m.b7*m.b14*m.b18 - 224*m.b7*m.b14*m.b19 - 160*m.b7*m.b14*m.b20
                        - 96*m.b7*m.b14*m.b22 - 64*m.b7*m.b14*m.b23 - 32*m.b7*m.b14*m.b24 - 448*m.b7*m.b15*m.b16 - 384*
                       m.b7*m.b15*m.b17 - 352*m.b7*m.b15*m.b18 - 256*m.b7*m.b15*m.b19 - 160*m.b7*m.b15*m.b20 - 128*m.b7*
                       m.b15*m.b21 - 96*m.b7*m.b15*m.b22 - 32*m.b7*m.b15*m.b24 - 416*m.b7*m.b16*m.b17 - 384*m.b7*m.b16*
                       m.b18 - 288*m.b7*m.b16*m.b19 - 192*m.b7*m.b16*m.b20 - 128*m.b7*m.b16*m.b21 - 96*m.b7*m.b16*m.b22
                        - 64*m.b7*m.b16*m.b23 - 32*m.b7*m.b16*m.b24 - 416*m.b7*m.b17*m.b18 - 320*m.b7*m.b17*m.b19 - 224*
                       m.b7*m.b17*m.b20 - 128*m.b7*m.b17*m.b21 - 96*m.b7*m.b17*m.b22 - 64*m.b7*m.b17*m.b23 - 32*m.b7*
                       m.b17*m.b24 - 352*m.b7*m.b18*m.b19 - 256*m.b7*m.b18*m.b20 - 160*m.b7*m.b18*m.b21 - 96*m.b7*m.b18*
                       m.b22 - 64*m.b7*m.b18*m.b23 - 32*m.b7*m.b18*m.b24 - 288*m.b7*m.b19*m.b20 - 192*m.b7*m.b19*m.b21
                        - 96*m.b7*m.b19*m.b22 - 64*m.b7*m.b19*m.b23 - 32*m.b7*m.b19*m.b24 - 224*m.b7*m.b20*m.b21 - 128*
                       m.b7*m.b20*m.b22 - 64*m.b7*m.b20*m.b23 - 32*m.b7*m.b20*m.b24 - 160*m.b7*m.b21*m.b22 - 64*m.b7*
                       m.b21*m.b23 - 32*m.b7*m.b21*m.b24 - 96*m.b7*m.b22*m.b23 - 32*m.b7*m.b22*m.b24 - 32*m.b7*m.b23*
                       m.b24 - 480*m.b8*m.b9*m.b10 - 704*m.b8*m.b9*m.b11 - 672*m.b8*m.b9*m.b12 - 640*m.b8*m.b9*m.b13 - 
                       608*m.b8*m.b9*m.b14 - 576*m.b8*m.b9*m.b15 - 544*m.b8*m.b9*m.b16 - 512*m.b8*m.b9*m.b17 - 480*m.b8*
                       m.b9*m.b18 - 416*m.b8*m.b9*m.b19 - 352*m.b8*m.b9*m.b20 - 288*m.b8*m.b9*m.b21 - 224*m.b8*m.b9*
                       m.b22 - 160*m.b8*m.b9*m.b23 - 96*m.b8*m.b9*m.b24 - 32*m.b8*m.b9*m.b25 - 736*m.b8*m.b10*m.b11 - 
                       448*m.b8*m.b10*m.b12 - 672*m.b8*m.b10*m.b13 - 640*m.b8*m.b10*m.b14 - 608*m.b8*m.b10*m.b15 - 576*
                       m.b8*m.b10*m.b16 - 512*m.b8*m.b10*m.b17 - 448*m.b8*m.b10*m.b18 - 384*m.b8*m.b10*m.b19 - 320*m.b8*
                       m.b10*m.b20 - 256*m.b8*m.b10*m.b21 - 192*m.b8*m.b10*m.b22 - 128*m.b8*m.b10*m.b23 - 64*m.b8*m.b10*
                       m.b24 - 32*m.b8*m.b10*m.b25 - 736*m.b8*m.b11*m.b12 - 704*m.b8*m.b11*m.b13 - 416*m.b8*m.b11*m.b14
                        - 640*m.b8*m.b11*m.b15 - 576*m.b8*m.b11*m.b16 - 512*m.b8*m.b11*m.b17 - 448*m.b8*m.b11*m.b18 - 
                       352*m.b8*m.b11*m.b19 - 288*m.b8*m.b11*m.b20 - 224*m.b8*m.b11*m.b21 - 160*m.b8*m.b11*m.b22 - 96*
                       m.b8*m.b11*m.b23 - 64*m.b8*m.b11*m.b24 - 32*m.b8*m.b11*m.b25 - 736*m.b8*m.b12*m.b13 - 704*m.b8*
                       m.b12*m.b14 - 640*m.b8*m.b12*m.b15 - 320*m.b8*m.b12*m.b16 - 512*m.b8*m.b12*m.b17 - 448*m.b8*m.b12
                       *m.b18 - 320*m.b8*m.b12*m.b19 - 256*m.b8*m.b12*m.b20 - 192*m.b8*m.b12*m.b21 - 128*m.b8*m.b12*
                       m.b22 - 96*m.b8*m.b12*m.b23 - 64*m.b8*m.b12*m.b24 - 32*m.b8*m.b12*m.b25 - 704*m.b8*m.b13*m.b14 - 
                       640*m.b8*m.b13*m.b15 - 576*m.b8*m.b13*m.b16 - 512*m.b8*m.b13*m.b17 - 192*m.b8*m.b13*m.b18 - 320*
                       m.b8*m.b13*m.b19 - 224*m.b8*m.b13*m.b20 - 160*m.b8*m.b13*m.b21 - 128*m.b8*m.b13*m.b22 - 96*m.b8*
                       m.b13*m.b23 - 64*m.b8*m.b13*m.b24 - 32*m.b8*m.b13*m.b25 - 640*m.b8*m.b14*m.b15 - 576*m.b8*m.b14*
                       m.b16 - 512*m.b8*m.b14*m.b17 - 448*m.b8*m.b14*m.b18 - 320*m.b8*m.b14*m.b19 - 160*m.b8*m.b14*m.b21
                        - 128*m.b8*m.b14*m.b22 - 96*m.b8*m.b14*m.b23 - 64*m.b8*m.b14*m.b24 - 32*m.b8*m.b14*m.b25 - 576*
                       m.b8*m.b15*m.b16 - 512*m.b8*m.b15*m.b17 - 448*m.b8*m.b15*m.b18 - 320*m.b8*m.b15*m.b19 - 224*m.b8*
                       m.b15*m.b20 - 160*m.b8*m.b15*m.b21 - 96*m.b8*m.b15*m.b23 - 64*m.b8*m.b15*m.b24 - 32*m.b8*m.b15*
                       m.b25 - 512*m.b8*m.b16*m.b17 - 448*m.b8*m.b16*m.b18 - 352*m.b8*m.b16*m.b19 - 256*m.b8*m.b16*m.b20
                        - 160*m.b8*m.b16*m.b21 - 128*m.b8*m.b16*m.b22 - 96*m.b8*m.b16*m.b23 - 32*m.b8*m.b16*m.b25 - 480*
                       m.b8*m.b17*m.b18 - 384*m.b8*m.b17*m.b19 - 288*m.b8*m.b17*m.b20 - 192*m.b8*m.b17*m.b21 - 128*m.b8*
                       m.b17*m.b22 - 96*m.b8*m.b17*m.b23 - 64*m.b8*m.b17*m.b24 - 32*m.b8*m.b17*m.b25 - 416*m.b8*m.b18*
                       m.b19 - 320*m.b8*m.b18*m.b20 - 224*m.b8*m.b18*m.b21 - 128*m.b8*m.b18*m.b22 - 96*m.b8*m.b18*m.b23
                        - 64*m.b8*m.b18*m.b24 - 32*m.b8*m.b18*m.b25 - 352*m.b8*m.b19*m.b20 - 256*m.b8*m.b19*m.b21 - 160*
                       m.b8*m.b19*m.b22 - 96*m.b8*m.b19*m.b23 - 64*m.b8*m.b19*m.b24 - 32*m.b8*m.b19*m.b25 - 288*m.b8*
                       m.b20*m.b21 - 192*m.b8*m.b20*m.b22 - 96*m.b8*m.b20*m.b23 - 64*m.b8*m.b20*m.b24 - 32*m.b8*m.b20*
                       m.b25 - 224*m.b8*m.b21*m.b22 - 128*m.b8*m.b21*m.b23 - 64*m.b8*m.b21*m.b24 - 32*m.b8*m.b21*m.b25
                        - 160*m.b8*m.b22*m.b23 - 64*m.b8*m.b22*m.b24 - 32*m.b8*m.b22*m.b25 - 96*m.b8*m.b23*m.b24 - 32*
                       m.b8*m.b23*m.b25 - 32*m.b8*m.b24*m.b25 - 544*m.b9*m.b10*m.b11 - 800*m.b9*m.b10*m.b12 - 768*m.b9*
                       m.b10*m.b13 - 736*m.b9*m.b10*m.b14 - 704*m.b9*m.b10*m.b15 - 672*m.b9*m.b10*m.b16 - 640*m.b9*m.b10
                       *m.b17 - 576*m.b9*m.b10*m.b18 - 480*m.b9*m.b10*m.b19 - 416*m.b9*m.b10*m.b20 - 352*m.b9*m.b10*
                       m.b21 - 288*m.b9*m.b10*m.b22 - 224*m.b9*m.b10*m.b23 - 160*m.b9*m.b10*m.b24 - 96*m.b9*m.b10*m.b25
                        - 32*m.b9*m.b10*m.b26 - 832*m.b9*m.b11*m.b12 - 512*m.b9*m.b11*m.b13 - 768*m.b9*m.b11*m.b14 - 736
                       *m.b9*m.b11*m.b15 - 704*m.b9*m.b11*m.b16 - 640*m.b9*m.b11*m.b17 - 576*m.b9*m.b11*m.b18 - 448*m.b9
                       *m.b11*m.b19 - 384*m.b9*m.b11*m.b20 - 320*m.b9*m.b11*m.b21 - 256*m.b9*m.b11*m.b22 - 192*m.b9*
                       m.b11*m.b23 - 128*m.b9*m.b11*m.b24 - 64*m.b9*m.b11*m.b25 - 32*m.b9*m.b11*m.b26 - 832*m.b9*m.b12*
                       m.b13 - 800*m.b9*m.b12*m.b14 - 480*m.b9*m.b12*m.b15 - 704*m.b9*m.b12*m.b16 - 640*m.b9*m.b12*m.b17
                        - 576*m.b9*m.b12*m.b18 - 448*m.b9*m.b12*m.b19 - 352*m.b9*m.b12*m.b20 - 288*m.b9*m.b12*m.b21 - 
                       224*m.b9*m.b12*m.b22 - 160*m.b9*m.b12*m.b23 - 96*m.b9*m.b12*m.b24 - 64*m.b9*m.b12*m.b25 - 32*m.b9
                       *m.b12*m.b26 - 832*m.b9*m.b13*m.b14 - 768*m.b9*m.b13*m.b15 - 704*m.b9*m.b13*m.b16 - 352*m.b9*
                       m.b13*m.b17 - 576*m.b9*m.b13*m.b18 - 448*m.b9*m.b13*m.b19 - 320*m.b9*m.b13*m.b20 - 256*m.b9*m.b13
                       *m.b21 - 192*m.b9*m.b13*m.b22 - 128*m.b9*m.b13*m.b23 - 96*m.b9*m.b13*m.b24 - 64*m.b9*m.b13*m.b25
                        - 32*m.b9*m.b13*m.b26 - 768*m.b9*m.b14*m.b15 - 704*m.b9*m.b14*m.b16 - 640*m.b9*m.b14*m.b17 - 576
                       *m.b9*m.b14*m.b18 - 192*m.b9*m.b14*m.b19 - 320*m.b9*m.b14*m.b20 - 224*m.b9*m.b14*m.b21 - 160*m.b9
                       *m.b14*m.b22 - 128*m.b9*m.b14*m.b23 - 96*m.b9*m.b14*m.b24 - 64*m.b9*m.b14*m.b25 - 32*m.b9*m.b14*
                       m.b26 - 704*m.b9*m.b15*m.b16 - 640*m.b9*m.b15*m.b17 - 576*m.b9*m.b15*m.b18 - 448*m.b9*m.b15*m.b19
                        - 320*m.b9*m.b15*m.b20 - 160*m.b9*m.b15*m.b22 - 128*m.b9*m.b15*m.b23 - 96*m.b9*m.b15*m.b24 - 64*
                       m.b9*m.b15*m.b25 - 32*m.b9*m.b15*m.b26 - 640*m.b9*m.b16*m.b17 - 576*m.b9*m.b16*m.b18 - 448*m.b9*
                       m.b16*m.b19 - 320*m.b9*m.b16*m.b20 - 224*m.b9*m.b16*m.b21 - 160*m.b9*m.b16*m.b22 - 96*m.b9*m.b16*
                       m.b24 - 64*m.b9*m.b16*m.b25 - 32*m.b9*m.b16*m.b26 - 576*m.b9*m.b17*m.b18 - 448*m.b9*m.b17*m.b19
                        - 352*m.b9*m.b17*m.b20 - 256*m.b9*m.b17*m.b21 - 160*m.b9*m.b17*m.b22 - 128*m.b9*m.b17*m.b23 - 96
                       *m.b9*m.b17*m.b24 - 32*m.b9*m.b17*m.b26 - 480*m.b9*m.b18*m.b19 - 384*m.b9*m.b18*m.b20 - 288*m.b9*
                       m.b18*m.b21 - 192*m.b9*m.b18*m.b22 - 128*m.b9*m.b18*m.b23 - 96*m.b9*m.b18*m.b24 - 64*m.b9*m.b18*
                       m.b25 - 32*m.b9*m.b18*m.b26 - 416*m.b9*m.b19*m.b20 - 320*m.b9*m.b19*m.b21 - 224*m.b9*m.b19*m.b22
                        - 128*m.b9*m.b19*m.b23 - 96*m.b9*m.b19*m.b24 - 64*m.b9*m.b19*m.b25 - 32*m.b9*m.b19*m.b26 - 352*
                       m.b9*m.b20*m.b21 - 256*m.b9*m.b20*m.b22 - 160*m.b9*m.b20*m.b23 - 96*m.b9*m.b20*m.b24 - 64*m.b9*
                       m.b20*m.b25 - 32*m.b9*m.b20*m.b26 - 288*m.b9*m.b21*m.b22 - 192*m.b9*m.b21*m.b23 - 96*m.b9*m.b21*
                       m.b24 - 64*m.b9*m.b21*m.b25 - 32*m.b9*m.b21*m.b26 - 224*m.b9*m.b22*m.b23 - 128*m.b9*m.b22*m.b24
                        - 64*m.b9*m.b22*m.b25 - 32*m.b9*m.b22*m.b26 - 160*m.b9*m.b23*m.b24 - 64*m.b9*m.b23*m.b25 - 32*
                       m.b9*m.b23*m.b26 - 96*m.b9*m.b24*m.b25 - 32*m.b9*m.b24*m.b26 - 32*m.b9*m.b25*m.b26 - 608*m.b10*
                       m.b11*m.b12 - 896*m.b10*m.b11*m.b13 - 864*m.b10*m.b11*m.b14 - 832*m.b10*m.b11*m.b15 - 800*m.b10*
                       m.b11*m.b16 - 768*m.b10*m.b11*m.b17 - 704*m.b10*m.b11*m.b18 - 576*m.b10*m.b11*m.b19 - 480*m.b10*
                       m.b11*m.b20 - 416*m.b10*m.b11*m.b21 - 352*m.b10*m.b11*m.b22 - 288*m.b10*m.b11*m.b23 - 224*m.b10*
                       m.b11*m.b24 - 160*m.b10*m.b11*m.b25 - 96*m.b10*m.b11*m.b26 - 32*m.b10*m.b11*m.b27 - 928*m.b10*
                       m.b12*m.b13 - 576*m.b10*m.b12*m.b14 - 864*m.b10*m.b12*m.b15 - 832*m.b10*m.b12*m.b16 - 768*m.b10*
                       m.b12*m.b17 - 704*m.b10*m.b12*m.b18 - 576*m.b10*m.b12*m.b19 - 448*m.b10*m.b12*m.b20 - 384*m.b10*
                       m.b12*m.b21 - 320*m.b10*m.b12*m.b22 - 256*m.b10*m.b12*m.b23 - 192*m.b10*m.b12*m.b24 - 128*m.b10*
                       m.b12*m.b25 - 64*m.b10*m.b12*m.b26 - 32*m.b10*m.b12*m.b27 - 928*m.b10*m.b13*m.b14 - 896*m.b10*
                       m.b13*m.b15 - 512*m.b10*m.b13*m.b16 - 768*m.b10*m.b13*m.b17 - 704*m.b10*m.b13*m.b18 - 576*m.b10*
                       m.b13*m.b19 - 448*m.b10*m.b13*m.b20 - 352*m.b10*m.b13*m.b21 - 288*m.b10*m.b13*m.b22 - 224*m.b10*
                       m.b13*m.b23 - 160*m.b10*m.b13*m.b24 - 96*m.b10*m.b13*m.b25 - 64*m.b10*m.b13*m.b26 - 32*m.b10*
                       m.b13*m.b27 - 896*m.b10*m.b14*m.b15 - 832*m.b10*m.b14*m.b16 - 768*m.b10*m.b14*m.b17 - 384*m.b10*
                       m.b14*m.b18 - 576*m.b10*m.b14*m.b19 - 448*m.b10*m.b14*m.b20 - 320*m.b10*m.b14*m.b21 - 256*m.b10*
                       m.b14*m.b22 - 192*m.b10*m.b14*m.b23 - 128*m.b10*m.b14*m.b24 - 96*m.b10*m.b14*m.b25 - 64*m.b10*
                       m.b14*m.b26 - 32*m.b10*m.b14*m.b27 - 832*m.b10*m.b15*m.b16 - 768*m.b10*m.b15*m.b17 - 704*m.b10*
                       m.b15*m.b18 - 576*m.b10*m.b15*m.b19 - 192*m.b10*m.b15*m.b20 - 320*m.b10*m.b15*m.b21 - 224*m.b10*
                       m.b15*m.b22 - 160*m.b10*m.b15*m.b23 - 128*m.b10*m.b15*m.b24 - 96*m.b10*m.b15*m.b25 - 64*m.b10*
                       m.b15*m.b26 - 32*m.b10*m.b15*m.b27 - 768*m.b10*m.b16*m.b17 - 704*m.b10*m.b16*m.b18 - 576*m.b10*
                       m.b16*m.b19 - 448*m.b10*m.b16*m.b20 - 320*m.b10*m.b16*m.b21 - 160*m.b10*m.b16*m.b23 - 128*m.b10*
                       m.b16*m.b24 - 96*m.b10*m.b16*m.b25 - 64*m.b10*m.b16*m.b26 - 32*m.b10*m.b16*m.b27 - 704*m.b10*
                       m.b17*m.b18 - 576*m.b10*m.b17*m.b19 - 448*m.b10*m.b17*m.b20 - 320*m.b10*m.b17*m.b21 - 224*m.b10*
                       m.b17*m.b22 - 160*m.b10*m.b17*m.b23 - 96*m.b10*m.b17*m.b25 - 64*m.b10*m.b17*m.b26 - 32*m.b10*
                       m.b17*m.b27 - 576*m.b10*m.b18*m.b19 - 448*m.b10*m.b18*m.b20 - 352*m.b10*m.b18*m.b21 - 256*m.b10*
                       m.b18*m.b22 - 160*m.b10*m.b18*m.b23 - 128*m.b10*m.b18*m.b24 - 96*m.b10*m.b18*m.b25 - 32*m.b10*
                       m.b18*m.b27 - 480*m.b10*m.b19*m.b20 - 384*m.b10*m.b19*m.b21 - 288*m.b10*m.b19*m.b22 - 192*m.b10*
                       m.b19*m.b23 - 128*m.b10*m.b19*m.b24 - 96*m.b10*m.b19*m.b25 - 64*m.b10*m.b19*m.b26 - 32*m.b10*
                       m.b19*m.b27 - 416*m.b10*m.b20*m.b21 - 320*m.b10*m.b20*m.b22 - 224*m.b10*m.b20*m.b23 - 128*m.b10*
                       m.b20*m.b24 - 96*m.b10*m.b20*m.b25 - 64*m.b10*m.b20*m.b26 - 32*m.b10*m.b20*m.b27 - 352*m.b10*
                       m.b21*m.b22 - 256*m.b10*m.b21*m.b23 - 160*m.b10*m.b21*m.b24 - 96*m.b10*m.b21*m.b25 - 64*m.b10*
                       m.b21*m.b26 - 32*m.b10*m.b21*m.b27 - 288*m.b10*m.b22*m.b23 - 192*m.b10*m.b22*m.b24 - 96*m.b10*
                       m.b22*m.b25 - 64*m.b10*m.b22*m.b26 - 32*m.b10*m.b22*m.b27 - 224*m.b10*m.b23*m.b24 - 128*m.b10*
                       m.b23*m.b25 - 64*m.b10*m.b23*m.b26 - 32*m.b10*m.b23*m.b27 - 160*m.b10*m.b24*m.b25 - 64*m.b10*
                       m.b24*m.b26 - 32*m.b10*m.b24*m.b27 - 96*m.b10*m.b25*m.b26 - 32*m.b10*m.b25*m.b27 - 32*m.b10*m.b26
                       *m.b27 - 672*m.b11*m.b12*m.b13 - 992*m.b11*m.b12*m.b14 - 960*m.b11*m.b12*m.b15 - 928*m.b11*m.b12*
                       m.b16 - 896*m.b11*m.b12*m.b17 - 832*m.b11*m.b12*m.b18 - 704*m.b11*m.b12*m.b19 - 576*m.b11*m.b12*
                       m.b20 - 480*m.b11*m.b12*m.b21 - 416*m.b11*m.b12*m.b22 - 352*m.b11*m.b12*m.b23 - 288*m.b11*m.b12*
                       m.b24 - 224*m.b11*m.b12*m.b25 - 160*m.b11*m.b12*m.b26 - 96*m.b11*m.b12*m.b27 - 32*m.b11*m.b12*
                       m.b28 - 1024*m.b11*m.b13*m.b14 - 640*m.b11*m.b13*m.b15 - 960*m.b11*m.b13*m.b16 - 896*m.b11*m.b13*
                       m.b17 - 832*m.b11*m.b13*m.b18 - 704*m.b11*m.b13*m.b19 - 576*m.b11*m.b13*m.b20 - 448*m.b11*m.b13*
                       m.b21 - 384*m.b11*m.b13*m.b22 - 320*m.b11*m.b13*m.b23 - 256*m.b11*m.b13*m.b24 - 192*m.b11*m.b13*
                       m.b25 - 128*m.b11*m.b13*m.b26 - 64*m.b11*m.b13*m.b27 - 32*m.b11*m.b13*m.b28 - 1024*m.b11*m.b14*
                       m.b15 - 960*m.b11*m.b14*m.b16 - 544*m.b11*m.b14*m.b17 - 832*m.b11*m.b14*m.b18 - 704*m.b11*m.b14*
                       m.b19 - 576*m.b11*m.b14*m.b20 - 448*m.b11*m.b14*m.b21 - 352*m.b11*m.b14*m.b22 - 288*m.b11*m.b14*
                       m.b23 - 224*m.b11*m.b14*m.b24 - 160*m.b11*m.b14*m.b25 - 96*m.b11*m.b14*m.b26 - 64*m.b11*m.b14*
                       m.b27 - 32*m.b11*m.b14*m.b28 - 960*m.b11*m.b15*m.b16 - 896*m.b11*m.b15*m.b17 - 832*m.b11*m.b15*
                       m.b18 - 384*m.b11*m.b15*m.b19 - 576*m.b11*m.b15*m.b20 - 448*m.b11*m.b15*m.b21 - 320*m.b11*m.b15*
                       m.b22 - 256*m.b11*m.b15*m.b23 - 192*m.b11*m.b15*m.b24 - 128*m.b11*m.b15*m.b25 - 96*m.b11*m.b15*
                       m.b26 - 64*m.b11*m.b15*m.b27 - 32*m.b11*m.b15*m.b28 - 896*m.b11*m.b16*m.b17 - 832*m.b11*m.b16*
                       m.b18 - 704*m.b11*m.b16*m.b19 - 576*m.b11*m.b16*m.b20 - 192*m.b11*m.b16*m.b21 - 320*m.b11*m.b16*
                       m.b22 - 224*m.b11*m.b16*m.b23 - 160*m.b11*m.b16*m.b24 - 128*m.b11*m.b16*m.b25 - 96*m.b11*m.b16*
                       m.b26 - 64*m.b11*m.b16*m.b27 - 32*m.b11*m.b16*m.b28 - 832*m.b11*m.b17*m.b18 - 704*m.b11*m.b17*
                       m.b19 - 576*m.b11*m.b17*m.b20 - 448*m.b11*m.b17*m.b21 - 320*m.b11*m.b17*m.b22 - 160*m.b11*m.b17*
                       m.b24 - 128*m.b11*m.b17*m.b25 - 96*m.b11*m.b17*m.b26 - 64*m.b11*m.b17*m.b27 - 32*m.b11*m.b17*
                       m.b28 - 704*m.b11*m.b18*m.b19 - 576*m.b11*m.b18*m.b20 - 448*m.b11*m.b18*m.b21 - 320*m.b11*m.b18*
                       m.b22 - 224*m.b11*m.b18*m.b23 - 160*m.b11*m.b18*m.b24 - 96*m.b11*m.b18*m.b26 - 64*m.b11*m.b18*
                       m.b27 - 32*m.b11*m.b18*m.b28 - 576*m.b11*m.b19*m.b20 - 448*m.b11*m.b19*m.b21 - 352*m.b11*m.b19*
                       m.b22 - 256*m.b11*m.b19*m.b23 - 160*m.b11*m.b19*m.b24 - 128*m.b11*m.b19*m.b25 - 96*m.b11*m.b19*
                       m.b26 - 32*m.b11*m.b19*m.b28 - 480*m.b11*m.b20*m.b21 - 384*m.b11*m.b20*m.b22 - 288*m.b11*m.b20*
                       m.b23 - 192*m.b11*m.b20*m.b24 - 128*m.b11*m.b20*m.b25 - 96*m.b11*m.b20*m.b26 - 64*m.b11*m.b20*
                       m.b27 - 32*m.b11*m.b20*m.b28 - 416*m.b11*m.b21*m.b22 - 320*m.b11*m.b21*m.b23 - 224*m.b11*m.b21*
                       m.b24 - 128*m.b11*m.b21*m.b25 - 96*m.b11*m.b21*m.b26 - 64*m.b11*m.b21*m.b27 - 32*m.b11*m.b21*
                       m.b28 - 352*m.b11*m.b22*m.b23 - 256*m.b11*m.b22*m.b24 - 160*m.b11*m.b22*m.b25 - 96*m.b11*m.b22*
                       m.b26 - 64*m.b11*m.b22*m.b27 - 32*m.b11*m.b22*m.b28 - 288*m.b11*m.b23*m.b24 - 192*m.b11*m.b23*
                       m.b25 - 96*m.b11*m.b23*m.b26 - 64*m.b11*m.b23*m.b27 - 32*m.b11*m.b23*m.b28 - 224*m.b11*m.b24*
                       m.b25 - 128*m.b11*m.b24*m.b26 - 64*m.b11*m.b24*m.b27 - 32*m.b11*m.b24*m.b28 - 160*m.b11*m.b25*
                       m.b26 - 64*m.b11*m.b25*m.b27 - 32*m.b11*m.b25*m.b28 - 96*m.b11*m.b26*m.b27 - 32*m.b11*m.b26*m.b28
                        - 32*m.b11*m.b27*m.b28 - 736*m.b12*m.b13*m.b14 - 1088*m.b12*m.b13*m.b15 - 1056*m.b12*m.b13*m.b16
                        - 1024*m.b12*m.b13*m.b17 - 960*m.b12*m.b13*m.b18 - 832*m.b12*m.b13*m.b19 - 704*m.b12*m.b13*m.b20
                        - 576*m.b12*m.b13*m.b21 - 480*m.b12*m.b13*m.b22 - 416*m.b12*m.b13*m.b23 - 352*m.b12*m.b13*m.b24
                        - 288*m.b12*m.b13*m.b25 - 224*m.b12*m.b13*m.b26 - 160*m.b12*m.b13*m.b27 - 96*m.b12*m.b13*m.b28
                        - 32*m.b12*m.b13*m.b29 - 1120*m.b12*m.b14*m.b15 - 704*m.b12*m.b14*m.b16 - 1024*m.b12*m.b14*m.b17
                        - 960*m.b12*m.b14*m.b18 - 832*m.b12*m.b14*m.b19 - 704*m.b12*m.b14*m.b20 - 576*m.b12*m.b14*m.b21
                        - 448*m.b12*m.b14*m.b22 - 384*m.b12*m.b14*m.b23 - 320*m.b12*m.b14*m.b24 - 256*m.b12*m.b14*m.b25
                        - 192*m.b12*m.b14*m.b26 - 128*m.b12*m.b14*m.b27 - 64*m.b12*m.b14*m.b28 - 32*m.b12*m.b14*m.b29 - 
                       1088*m.b12*m.b15*m.b16 - 1024*m.b12*m.b15*m.b17 - 576*m.b12*m.b15*m.b18 - 832*m.b12*m.b15*m.b19
                        - 704*m.b12*m.b15*m.b20 - 576*m.b12*m.b15*m.b21 - 448*m.b12*m.b15*m.b22 - 352*m.b12*m.b15*m.b23
                        - 288*m.b12*m.b15*m.b24 - 224*m.b12*m.b15*m.b25 - 160*m.b12*m.b15*m.b26 - 96*m.b12*m.b15*m.b27
                        - 64*m.b12*m.b15*m.b28 - 32*m.b12*m.b15*m.b29 - 1024*m.b12*m.b16*m.b17 - 960*m.b12*m.b16*m.b18
                        - 832*m.b12*m.b16*m.b19 - 384*m.b12*m.b16*m.b20 - 576*m.b12*m.b16*m.b21 - 448*m.b12*m.b16*m.b22
                        - 320*m.b12*m.b16*m.b23 - 256*m.b12*m.b16*m.b24 - 192*m.b12*m.b16*m.b25 - 128*m.b12*m.b16*m.b26
                        - 96*m.b12*m.b16*m.b27 - 64*m.b12*m.b16*m.b28 - 32*m.b12*m.b16*m.b29 - 960*m.b12*m.b17*m.b18 - 
                       832*m.b12*m.b17*m.b19 - 704*m.b12*m.b17*m.b20 - 576*m.b12*m.b17*m.b21 - 192*m.b12*m.b17*m.b22 - 
                       320*m.b12*m.b17*m.b23 - 224*m.b12*m.b17*m.b24 - 160*m.b12*m.b17*m.b25 - 128*m.b12*m.b17*m.b26 - 
                       96*m.b12*m.b17*m.b27 - 64*m.b12*m.b17*m.b28 - 32*m.b12*m.b17*m.b29 - 832*m.b12*m.b18*m.b19 - 704*
                       m.b12*m.b18*m.b20 - 576*m.b12*m.b18*m.b21 - 448*m.b12*m.b18*m.b22 - 320*m.b12*m.b18*m.b23 - 160*
                       m.b12*m.b18*m.b25 - 128*m.b12*m.b18*m.b26 - 96*m.b12*m.b18*m.b27 - 64*m.b12*m.b18*m.b28 - 32*
                       m.b12*m.b18*m.b29 - 704*m.b12*m.b19*m.b20 - 576*m.b12*m.b19*m.b21 - 448*m.b12*m.b19*m.b22 - 320*
                       m.b12*m.b19*m.b23 - 224*m.b12*m.b19*m.b24 - 160*m.b12*m.b19*m.b25 - 96*m.b12*m.b19*m.b27 - 64*
                       m.b12*m.b19*m.b28 - 32*m.b12*m.b19*m.b29 - 576*m.b12*m.b20*m.b21 - 448*m.b12*m.b20*m.b22 - 352*
                       m.b12*m.b20*m.b23 - 256*m.b12*m.b20*m.b24 - 160*m.b12*m.b20*m.b25 - 128*m.b12*m.b20*m.b26 - 96*
                       m.b12*m.b20*m.b27 - 32*m.b12*m.b20*m.b29 - 480*m.b12*m.b21*m.b22 - 384*m.b12*m.b21*m.b23 - 288*
                       m.b12*m.b21*m.b24 - 192*m.b12*m.b21*m.b25 - 128*m.b12*m.b21*m.b26 - 96*m.b12*m.b21*m.b27 - 64*
                       m.b12*m.b21*m.b28 - 32*m.b12*m.b21*m.b29 - 416*m.b12*m.b22*m.b23 - 320*m.b12*m.b22*m.b24 - 224*
                       m.b12*m.b22*m.b25 - 128*m.b12*m.b22*m.b26 - 96*m.b12*m.b22*m.b27 - 64*m.b12*m.b22*m.b28 - 32*
                       m.b12*m.b22*m.b29 - 352*m.b12*m.b23*m.b24 - 256*m.b12*m.b23*m.b25 - 160*m.b12*m.b23*m.b26 - 96*
                       m.b12*m.b23*m.b27 - 64*m.b12*m.b23*m.b28 - 32*m.b12*m.b23*m.b29 - 288*m.b12*m.b24*m.b25 - 192*
                       m.b12*m.b24*m.b26 - 96*m.b12*m.b24*m.b27 - 64*m.b12*m.b24*m.b28 - 32*m.b12*m.b24*m.b29 - 224*
                       m.b12*m.b25*m.b26 - 128*m.b12*m.b25*m.b27 - 64*m.b12*m.b25*m.b28 - 32*m.b12*m.b25*m.b29 - 160*
                       m.b12*m.b26*m.b27 - 64*m.b12*m.b26*m.b28 - 32*m.b12*m.b26*m.b29 - 96*m.b12*m.b27*m.b28 - 32*m.b12
                       *m.b27*m.b29 - 32*m.b12*m.b28*m.b29 - 800*m.b13*m.b14*m.b15 - 1184*m.b13*m.b14*m.b16 - 1152*m.b13
                       *m.b14*m.b17 - 1088*m.b13*m.b14*m.b18 - 960*m.b13*m.b14*m.b19 - 832*m.b13*m.b14*m.b20 - 704*m.b13
                       *m.b14*m.b21 - 576*m.b13*m.b14*m.b22 - 480*m.b13*m.b14*m.b23 - 416*m.b13*m.b14*m.b24 - 352*m.b13*
                       m.b14*m.b25 - 288*m.b13*m.b14*m.b26 - 224*m.b13*m.b14*m.b27 - 160*m.b13*m.b14*m.b28 - 96*m.b13*
                       m.b14*m.b29 - 32*m.b13*m.b14*m.b30 - 1216*m.b13*m.b15*m.b16 - 736*m.b13*m.b15*m.b17 - 1088*m.b13*
                       m.b15*m.b18 - 960*m.b13*m.b15*m.b19 - 832*m.b13*m.b15*m.b20 - 704*m.b13*m.b15*m.b21 - 576*m.b13*
                       m.b15*m.b22 - 448*m.b13*m.b15*m.b23 - 384*m.b13*m.b15*m.b24 - 320*m.b13*m.b15*m.b25 - 256*m.b13*
                       m.b15*m.b26 - 192*m.b13*m.b15*m.b27 - 128*m.b13*m.b15*m.b28 - 64*m.b13*m.b15*m.b29 - 32*m.b13*
                       m.b15*m.b30 - 1152*m.b13*m.b16*m.b17 - 1088*m.b13*m.b16*m.b18 - 576*m.b13*m.b16*m.b19 - 832*m.b13
                       *m.b16*m.b20 - 704*m.b13*m.b16*m.b21 - 576*m.b13*m.b16*m.b22 - 448*m.b13*m.b16*m.b23 - 352*m.b13*
                       m.b16*m.b24 - 288*m.b13*m.b16*m.b25 - 224*m.b13*m.b16*m.b26 - 160*m.b13*m.b16*m.b27 - 96*m.b13*
                       m.b16*m.b28 - 64*m.b13*m.b16*m.b29 - 32*m.b13*m.b16*m.b30 - 1088*m.b13*m.b17*m.b18 - 960*m.b13*
                       m.b17*m.b19 - 832*m.b13*m.b17*m.b20 - 384*m.b13*m.b17*m.b21 - 576*m.b13*m.b17*m.b22 - 448*m.b13*
                       m.b17*m.b23 - 320*m.b13*m.b17*m.b24 - 256*m.b13*m.b17*m.b25 - 192*m.b13*m.b17*m.b26 - 128*m.b13*
                       m.b17*m.b27 - 96*m.b13*m.b17*m.b28 - 64*m.b13*m.b17*m.b29 - 32*m.b13*m.b17*m.b30 - 960*m.b13*
                       m.b18*m.b19 - 832*m.b13*m.b18*m.b20 - 704*m.b13*m.b18*m.b21 - 576*m.b13*m.b18*m.b22 - 192*m.b13*
                       m.b18*m.b23 - 320*m.b13*m.b18*m.b24 - 224*m.b13*m.b18*m.b25 - 160*m.b13*m.b18*m.b26 - 128*m.b13*
                       m.b18*m.b27 - 96*m.b13*m.b18*m.b28 - 64*m.b13*m.b18*m.b29 - 32*m.b13*m.b18*m.b30 - 832*m.b13*
                       m.b19*m.b20 - 704*m.b13*m.b19*m.b21 - 576*m.b13*m.b19*m.b22 - 448*m.b13*m.b19*m.b23 - 320*m.b13*
                       m.b19*m.b24 - 160*m.b13*m.b19*m.b26 - 128*m.b13*m.b19*m.b27 - 96*m.b13*m.b19*m.b28 - 64*m.b13*
                       m.b19*m.b29 - 32*m.b13*m.b19*m.b30 - 704*m.b13*m.b20*m.b21 - 576*m.b13*m.b20*m.b22 - 448*m.b13*
                       m.b20*m.b23 - 320*m.b13*m.b20*m.b24 - 224*m.b13*m.b20*m.b25 - 160*m.b13*m.b20*m.b26 - 96*m.b13*
                       m.b20*m.b28 - 64*m.b13*m.b20*m.b29 - 32*m.b13*m.b20*m.b30 - 576*m.b13*m.b21*m.b22 - 448*m.b13*
                       m.b21*m.b23 - 352*m.b13*m.b21*m.b24 - 256*m.b13*m.b21*m.b25 - 160*m.b13*m.b21*m.b26 - 128*m.b13*
                       m.b21*m.b27 - 96*m.b13*m.b21*m.b28 - 32*m.b13*m.b21*m.b30 - 480*m.b13*m.b22*m.b23 - 384*m.b13*
                       m.b22*m.b24 - 288*m.b13*m.b22*m.b25 - 192*m.b13*m.b22*m.b26 - 128*m.b13*m.b22*m.b27 - 96*m.b13*
                       m.b22*m.b28 - 64*m.b13*m.b22*m.b29 - 32*m.b13*m.b22*m.b30 - 416*m.b13*m.b23*m.b24 - 320*m.b13*
                       m.b23*m.b25 - 224*m.b13*m.b23*m.b26 - 128*m.b13*m.b23*m.b27 - 96*m.b13*m.b23*m.b28 - 64*m.b13*
                       m.b23*m.b29 - 32*m.b13*m.b23*m.b30 - 352*m.b13*m.b24*m.b25 - 256*m.b13*m.b24*m.b26 - 160*m.b13*
                       m.b24*m.b27 - 96*m.b13*m.b24*m.b28 - 64*m.b13*m.b24*m.b29 - 32*m.b13*m.b24*m.b30 - 288*m.b13*
                       m.b25*m.b26 - 192*m.b13*m.b25*m.b27 - 96*m.b13*m.b25*m.b28 - 64*m.b13*m.b25*m.b29 - 32*m.b13*
                       m.b25*m.b30 - 224*m.b13*m.b26*m.b27 - 128*m.b13*m.b26*m.b28 - 64*m.b13*m.b26*m.b29 - 32*m.b13*
                       m.b26*m.b30 - 160*m.b13*m.b27*m.b28 - 64*m.b13*m.b27*m.b29 - 32*m.b13*m.b27*m.b30 - 96*m.b13*
                       m.b28*m.b29 - 32*m.b13*m.b28*m.b30 - 32*m.b13*m.b29*m.b30 - 864*m.b14*m.b15*m.b16 - 1280*m.b14*
                       m.b15*m.b17 - 1216*m.b14*m.b15*m.b18 - 1088*m.b14*m.b15*m.b19 - 960*m.b14*m.b15*m.b20 - 832*m.b14
                       *m.b15*m.b21 - 704*m.b14*m.b15*m.b22 - 576*m.b14*m.b15*m.b23 - 480*m.b14*m.b15*m.b24 - 416*m.b14*
                       m.b15*m.b25 - 352*m.b14*m.b15*m.b26 - 288*m.b14*m.b15*m.b27 - 224*m.b14*m.b15*m.b28 - 160*m.b14*
                       m.b15*m.b29 - 96*m.b14*m.b15*m.b30 - 32*m.b14*m.b15*m.b31 - 1280*m.b14*m.b16*m.b17 - 768*m.b14*
                       m.b16*m.b18 - 1088*m.b14*m.b16*m.b19 - 960*m.b14*m.b16*m.b20 - 832*m.b14*m.b16*m.b21 - 704*m.b14*
                       m.b16*m.b22 - 576*m.b14*m.b16*m.b23 - 448*m.b14*m.b16*m.b24 - 384*m.b14*m.b16*m.b25 - 320*m.b14*
                       m.b16*m.b26 - 256*m.b14*m.b16*m.b27 - 192*m.b14*m.b16*m.b28 - 128*m.b14*m.b16*m.b29 - 64*m.b14*
                       m.b16*m.b30 - 32*m.b14*m.b16*m.b31 - 1216*m.b14*m.b17*m.b18 - 1088*m.b14*m.b17*m.b19 - 576*m.b14*
                       m.b17*m.b20 - 832*m.b14*m.b17*m.b21 - 704*m.b14*m.b17*m.b22 - 576*m.b14*m.b17*m.b23 - 448*m.b14*
                       m.b17*m.b24 - 352*m.b14*m.b17*m.b25 - 288*m.b14*m.b17*m.b26 - 224*m.b14*m.b17*m.b27 - 160*m.b14*
                       m.b17*m.b28 - 96*m.b14*m.b17*m.b29 - 64*m.b14*m.b17*m.b30 - 32*m.b14*m.b17*m.b31 - 1088*m.b14*
                       m.b18*m.b19 - 960*m.b14*m.b18*m.b20 - 832*m.b14*m.b18*m.b21 - 384*m.b14*m.b18*m.b22 - 576*m.b14*
                       m.b18*m.b23 - 448*m.b14*m.b18*m.b24 - 320*m.b14*m.b18*m.b25 - 256*m.b14*m.b18*m.b26 - 192*m.b14*
                       m.b18*m.b27 - 128*m.b14*m.b18*m.b28 - 96*m.b14*m.b18*m.b29 - 64*m.b14*m.b18*m.b30 - 32*m.b14*
                       m.b18*m.b31 - 960*m.b14*m.b19*m.b20 - 832*m.b14*m.b19*m.b21 - 704*m.b14*m.b19*m.b22 - 576*m.b14*
                       m.b19*m.b23 - 192*m.b14*m.b19*m.b24 - 320*m.b14*m.b19*m.b25 - 224*m.b14*m.b19*m.b26 - 160*m.b14*
                       m.b19*m.b27 - 128*m.b14*m.b19*m.b28 - 96*m.b14*m.b19*m.b29 - 64*m.b14*m.b19*m.b30 - 32*m.b14*
                       m.b19*m.b31 - 832*m.b14*m.b20*m.b21 - 704*m.b14*m.b20*m.b22 - 576*m.b14*m.b20*m.b23 - 448*m.b14*
                       m.b20*m.b24 - 320*m.b14*m.b20*m.b25 - 160*m.b14*m.b20*m.b27 - 128*m.b14*m.b20*m.b28 - 96*m.b14*
                       m.b20*m.b29 - 64*m.b14*m.b20*m.b30 - 32*m.b14*m.b20*m.b31 - 704*m.b14*m.b21*m.b22 - 576*m.b14*
                       m.b21*m.b23 - 448*m.b14*m.b21*m.b24 - 320*m.b14*m.b21*m.b25 - 224*m.b14*m.b21*m.b26 - 160*m.b14*
                       m.b21*m.b27 - 96*m.b14*m.b21*m.b29 - 64*m.b14*m.b21*m.b30 - 32*m.b14*m.b21*m.b31 - 576*m.b14*
                       m.b22*m.b23 - 448*m.b14*m.b22*m.b24 - 352*m.b14*m.b22*m.b25 - 256*m.b14*m.b22*m.b26 - 160*m.b14*
                       m.b22*m.b27 - 128*m.b14*m.b22*m.b28 - 96*m.b14*m.b22*m.b29 - 32*m.b14*m.b22*m.b31 - 480*m.b14*
                       m.b23*m.b24 - 384*m.b14*m.b23*m.b25 - 288*m.b14*m.b23*m.b26 - 192*m.b14*m.b23*m.b27 - 128*m.b14*
                       m.b23*m.b28 - 96*m.b14*m.b23*m.b29 - 64*m.b14*m.b23*m.b30 - 32*m.b14*m.b23*m.b31 - 416*m.b14*
                       m.b24*m.b25 - 320*m.b14*m.b24*m.b26 - 224*m.b14*m.b24*m.b27 - 128*m.b14*m.b24*m.b28 - 96*m.b14*
                       m.b24*m.b29 - 64*m.b14*m.b24*m.b30 - 32*m.b14*m.b24*m.b31 - 352*m.b14*m.b25*m.b26 - 256*m.b14*
                       m.b25*m.b27 - 160*m.b14*m.b25*m.b28 - 96*m.b14*m.b25*m.b29 - 64*m.b14*m.b25*m.b30 - 32*m.b14*
                       m.b25*m.b31 - 288*m.b14*m.b26*m.b27 - 192*m.b14*m.b26*m.b28 - 96*m.b14*m.b26*m.b29 - 64*m.b14*
                       m.b26*m.b30 - 32*m.b14*m.b26*m.b31 - 224*m.b14*m.b27*m.b28 - 128*m.b14*m.b27*m.b29 - 64*m.b14*
                       m.b27*m.b30 - 32*m.b14*m.b27*m.b31 - 160*m.b14*m.b28*m.b29 - 64*m.b14*m.b28*m.b30 - 32*m.b14*
                       m.b28*m.b31 - 96*m.b14*m.b29*m.b30 - 32*m.b14*m.b29*m.b31 - 32*m.b14*m.b30*m.b31 - 928*m.b15*
                       m.b16*m.b17 - 1344*m.b15*m.b16*m.b18 - 1216*m.b15*m.b16*m.b19 - 1088*m.b15*m.b16*m.b20 - 960*
                       m.b15*m.b16*m.b21 - 832*m.b15*m.b16*m.b22 - 704*m.b15*m.b16*m.b23 - 576*m.b15*m.b16*m.b24 - 480*
                       m.b15*m.b16*m.b25 - 416*m.b15*m.b16*m.b26 - 352*m.b15*m.b16*m.b27 - 288*m.b15*m.b16*m.b28 - 224*
                       m.b15*m.b16*m.b29 - 160*m.b15*m.b16*m.b30 - 96*m.b15*m.b16*m.b31 - 32*m.b15*m.b16*m.b32 - 1344*
                       m.b15*m.b17*m.b18 - 768*m.b15*m.b17*m.b19 - 1088*m.b15*m.b17*m.b20 - 960*m.b15*m.b17*m.b21 - 832*
                       m.b15*m.b17*m.b22 - 704*m.b15*m.b17*m.b23 - 576*m.b15*m.b17*m.b24 - 448*m.b15*m.b17*m.b25 - 384*
                       m.b15*m.b17*m.b26 - 320*m.b15*m.b17*m.b27 - 256*m.b15*m.b17*m.b28 - 192*m.b15*m.b17*m.b29 - 128*
                       m.b15*m.b17*m.b30 - 64*m.b15*m.b17*m.b31 - 32*m.b15*m.b17*m.b32 - 1216*m.b15*m.b18*m.b19 - 1088*
                       m.b15*m.b18*m.b20 - 576*m.b15*m.b18*m.b21 - 832*m.b15*m.b18*m.b22 - 704*m.b15*m.b18*m.b23 - 576*
                       m.b15*m.b18*m.b24 - 448*m.b15*m.b18*m.b25 - 352*m.b15*m.b18*m.b26 - 288*m.b15*m.b18*m.b27 - 224*
                       m.b15*m.b18*m.b28 - 160*m.b15*m.b18*m.b29 - 96*m.b15*m.b18*m.b30 - 64*m.b15*m.b18*m.b31 - 32*
                       m.b15*m.b18*m.b32 - 1088*m.b15*m.b19*m.b20 - 960*m.b15*m.b19*m.b21 - 832*m.b15*m.b19*m.b22 - 384*
                       m.b15*m.b19*m.b23 - 576*m.b15*m.b19*m.b24 - 448*m.b15*m.b19*m.b25 - 320*m.b15*m.b19*m.b26 - 256*
                       m.b15*m.b19*m.b27 - 192*m.b15*m.b19*m.b28 - 128*m.b15*m.b19*m.b29 - 96*m.b15*m.b19*m.b30 - 64*
                       m.b15*m.b19*m.b31 - 32*m.b15*m.b19*m.b32 - 960*m.b15*m.b20*m.b21 - 832*m.b15*m.b20*m.b22 - 704*
                       m.b15*m.b20*m.b23 - 576*m.b15*m.b20*m.b24 - 192*m.b15*m.b20*m.b25 - 320*m.b15*m.b20*m.b26 - 224*
                       m.b15*m.b20*m.b27 - 160*m.b15*m.b20*m.b28 - 128*m.b15*m.b20*m.b29 - 96*m.b15*m.b20*m.b30 - 64*
                       m.b15*m.b20*m.b31 - 32*m.b15*m.b20*m.b32 - 832*m.b15*m.b21*m.b22 - 704*m.b15*m.b21*m.b23 - 576*
                       m.b15*m.b21*m.b24 - 448*m.b15*m.b21*m.b25 - 320*m.b15*m.b21*m.b26 - 160*m.b15*m.b21*m.b28 - 128*
                       m.b15*m.b21*m.b29 - 96*m.b15*m.b21*m.b30 - 64*m.b15*m.b21*m.b31 - 32*m.b15*m.b21*m.b32 - 704*
                       m.b15*m.b22*m.b23 - 576*m.b15*m.b22*m.b24 - 448*m.b15*m.b22*m.b25 - 320*m.b15*m.b22*m.b26 - 224*
                       m.b15*m.b22*m.b27 - 160*m.b15*m.b22*m.b28 - 96*m.b15*m.b22*m.b30 - 64*m.b15*m.b22*m.b31 - 32*
                       m.b15*m.b22*m.b32 - 576*m.b15*m.b23*m.b24 - 448*m.b15*m.b23*m.b25 - 352*m.b15*m.b23*m.b26 - 256*
                       m.b15*m.b23*m.b27 - 160*m.b15*m.b23*m.b28 - 128*m.b15*m.b23*m.b29 - 96*m.b15*m.b23*m.b30 - 32*
                       m.b15*m.b23*m.b32 - 480*m.b15*m.b24*m.b25 - 384*m.b15*m.b24*m.b26 - 288*m.b15*m.b24*m.b27 - 192*
                       m.b15*m.b24*m.b28 - 128*m.b15*m.b24*m.b29 - 96*m.b15*m.b24*m.b30 - 64*m.b15*m.b24*m.b31 - 32*
                       m.b15*m.b24*m.b32 - 416*m.b15*m.b25*m.b26 - 320*m.b15*m.b25*m.b27 - 224*m.b15*m.b25*m.b28 - 128*
                       m.b15*m.b25*m.b29 - 96*m.b15*m.b25*m.b30 - 64*m.b15*m.b25*m.b31 - 32*m.b15*m.b25*m.b32 - 352*
                       m.b15*m.b26*m.b27 - 256*m.b15*m.b26*m.b28 - 160*m.b15*m.b26*m.b29 - 96*m.b15*m.b26*m.b30 - 64*
                       m.b15*m.b26*m.b31 - 32*m.b15*m.b26*m.b32 - 288*m.b15*m.b27*m.b28 - 192*m.b15*m.b27*m.b29 - 96*
                       m.b15*m.b27*m.b30 - 64*m.b15*m.b27*m.b31 - 32*m.b15*m.b27*m.b32 - 224*m.b15*m.b28*m.b29 - 128*
                       m.b15*m.b28*m.b30 - 64*m.b15*m.b28*m.b31 - 32*m.b15*m.b28*m.b32 - 160*m.b15*m.b29*m.b30 - 64*
                       m.b15*m.b29*m.b31 - 32*m.b15*m.b29*m.b32 - 96*m.b15*m.b30*m.b31 - 32*m.b15*m.b30*m.b32 - 32*m.b15
                       *m.b31*m.b32 - 960*m.b16*m.b17*m.b18 - 1344*m.b16*m.b17*m.b19 - 1216*m.b16*m.b17*m.b20 - 1088*
                       m.b16*m.b17*m.b21 - 960*m.b16*m.b17*m.b22 - 832*m.b16*m.b17*m.b23 - 704*m.b16*m.b17*m.b24 - 576*
                       m.b16*m.b17*m.b25 - 480*m.b16*m.b17*m.b26 - 416*m.b16*m.b17*m.b27 - 352*m.b16*m.b17*m.b28 - 288*
                       m.b16*m.b17*m.b29 - 224*m.b16*m.b17*m.b30 - 160*m.b16*m.b17*m.b31 - 96*m.b16*m.b17*m.b32 - 32*
                       m.b16*m.b17*m.b33 - 1344*m.b16*m.b18*m.b19 - 768*m.b16*m.b18*m.b20 - 1088*m.b16*m.b18*m.b21 - 960
                       *m.b16*m.b18*m.b22 - 832*m.b16*m.b18*m.b23 - 704*m.b16*m.b18*m.b24 - 576*m.b16*m.b18*m.b25 - 448*
                       m.b16*m.b18*m.b26 - 384*m.b16*m.b18*m.b27 - 320*m.b16*m.b18*m.b28 - 256*m.b16*m.b18*m.b29 - 192*
                       m.b16*m.b18*m.b30 - 128*m.b16*m.b18*m.b31 - 64*m.b16*m.b18*m.b32 - 32*m.b16*m.b18*m.b33 - 1216*
                       m.b16*m.b19*m.b20 - 1088*m.b16*m.b19*m.b21 - 576*m.b16*m.b19*m.b22 - 832*m.b16*m.b19*m.b23 - 704*
                       m.b16*m.b19*m.b24 - 576*m.b16*m.b19*m.b25 - 448*m.b16*m.b19*m.b26 - 352*m.b16*m.b19*m.b27 - 288*
                       m.b16*m.b19*m.b28 - 224*m.b16*m.b19*m.b29 - 160*m.b16*m.b19*m.b30 - 96*m.b16*m.b19*m.b31 - 64*
                       m.b16*m.b19*m.b32 - 32*m.b16*m.b19*m.b33 - 1088*m.b16*m.b20*m.b21 - 960*m.b16*m.b20*m.b22 - 832*
                       m.b16*m.b20*m.b23 - 384*m.b16*m.b20*m.b24 - 576*m.b16*m.b20*m.b25 - 448*m.b16*m.b20*m.b26 - 320*
                       m.b16*m.b20*m.b27 - 256*m.b16*m.b20*m.b28 - 192*m.b16*m.b20*m.b29 - 128*m.b16*m.b20*m.b30 - 96*
                       m.b16*m.b20*m.b31 - 64*m.b16*m.b20*m.b32 - 32*m.b16*m.b20*m.b33 - 960*m.b16*m.b21*m.b22 - 832*
                       m.b16*m.b21*m.b23 - 704*m.b16*m.b21*m.b24 - 576*m.b16*m.b21*m.b25 - 192*m.b16*m.b21*m.b26 - 320*
                       m.b16*m.b21*m.b27 - 224*m.b16*m.b21*m.b28 - 160*m.b16*m.b21*m.b29 - 128*m.b16*m.b21*m.b30 - 96*
                       m.b16*m.b21*m.b31 - 64*m.b16*m.b21*m.b32 - 32*m.b16*m.b21*m.b33 - 832*m.b16*m.b22*m.b23 - 704*
                       m.b16*m.b22*m.b24 - 576*m.b16*m.b22*m.b25 - 448*m.b16*m.b22*m.b26 - 320*m.b16*m.b22*m.b27 - 160*
                       m.b16*m.b22*m.b29 - 128*m.b16*m.b22*m.b30 - 96*m.b16*m.b22*m.b31 - 64*m.b16*m.b22*m.b32 - 32*
                       m.b16*m.b22*m.b33 - 704*m.b16*m.b23*m.b24 - 576*m.b16*m.b23*m.b25 - 448*m.b16*m.b23*m.b26 - 320*
                       m.b16*m.b23*m.b27 - 224*m.b16*m.b23*m.b28 - 160*m.b16*m.b23*m.b29 - 96*m.b16*m.b23*m.b31 - 64*
                       m.b16*m.b23*m.b32 - 32*m.b16*m.b23*m.b33 - 576*m.b16*m.b24*m.b25 - 448*m.b16*m.b24*m.b26 - 352*
                       m.b16*m.b24*m.b27 - 256*m.b16*m.b24*m.b28 - 160*m.b16*m.b24*m.b29 - 128*m.b16*m.b24*m.b30 - 96*
                       m.b16*m.b24*m.b31 - 32*m.b16*m.b24*m.b33 - 480*m.b16*m.b25*m.b26 - 384*m.b16*m.b25*m.b27 - 288*
                       m.b16*m.b25*m.b28 - 192*m.b16*m.b25*m.b29 - 128*m.b16*m.b25*m.b30 - 96*m.b16*m.b25*m.b31 - 64*
                       m.b16*m.b25*m.b32 - 32*m.b16*m.b25*m.b33 - 416*m.b16*m.b26*m.b27 - 320*m.b16*m.b26*m.b28 - 224*
                       m.b16*m.b26*m.b29 - 128*m.b16*m.b26*m.b30 - 96*m.b16*m.b26*m.b31 - 64*m.b16*m.b26*m.b32 - 32*
                       m.b16*m.b26*m.b33 - 352*m.b16*m.b27*m.b28 - 256*m.b16*m.b27*m.b29 - 160*m.b16*m.b27*m.b30 - 96*
                       m.b16*m.b27*m.b31 - 64*m.b16*m.b27*m.b32 - 32*m.b16*m.b27*m.b33 - 288*m.b16*m.b28*m.b29 - 192*
                       m.b16*m.b28*m.b30 - 96*m.b16*m.b28*m.b31 - 64*m.b16*m.b28*m.b32 - 32*m.b16*m.b28*m.b33 - 224*
                       m.b16*m.b29*m.b30 - 128*m.b16*m.b29*m.b31 - 64*m.b16*m.b29*m.b32 - 32*m.b16*m.b29*m.b33 - 160*
                       m.b16*m.b30*m.b31 - 64*m.b16*m.b30*m.b32 - 32*m.b16*m.b30*m.b33 - 96*m.b16*m.b31*m.b32 - 32*m.b16
                       *m.b31*m.b33 - 32*m.b16*m.b32*m.b33 - 960*m.b17*m.b18*m.b19 - 1344*m.b17*m.b18*m.b20 - 1216*m.b17
                       *m.b18*m.b21 - 1088*m.b17*m.b18*m.b22 - 960*m.b17*m.b18*m.b23 - 832*m.b17*m.b18*m.b24 - 704*m.b17
                       *m.b18*m.b25 - 576*m.b17*m.b18*m.b26 - 480*m.b17*m.b18*m.b27 - 416*m.b17*m.b18*m.b28 - 352*m.b17*
                       m.b18*m.b29 - 288*m.b17*m.b18*m.b30 - 224*m.b17*m.b18*m.b31 - 160*m.b17*m.b18*m.b32 - 96*m.b17*
                       m.b18*m.b33 - 32*m.b17*m.b18*m.b34 - 1344*m.b17*m.b19*m.b20 - 768*m.b17*m.b19*m.b21 - 1088*m.b17*
                       m.b19*m.b22 - 960*m.b17*m.b19*m.b23 - 832*m.b17*m.b19*m.b24 - 704*m.b17*m.b19*m.b25 - 576*m.b17*
                       m.b19*m.b26 - 448*m.b17*m.b19*m.b27 - 384*m.b17*m.b19*m.b28 - 320*m.b17*m.b19*m.b29 - 256*m.b17*
                       m.b19*m.b30 - 192*m.b17*m.b19*m.b31 - 128*m.b17*m.b19*m.b32 - 64*m.b17*m.b19*m.b33 - 32*m.b17*
                       m.b19*m.b34 - 1216*m.b17*m.b20*m.b21 - 1088*m.b17*m.b20*m.b22 - 576*m.b17*m.b20*m.b23 - 832*m.b17
                       *m.b20*m.b24 - 704*m.b17*m.b20*m.b25 - 576*m.b17*m.b20*m.b26 - 448*m.b17*m.b20*m.b27 - 352*m.b17*
                       m.b20*m.b28 - 288*m.b17*m.b20*m.b29 - 224*m.b17*m.b20*m.b30 - 160*m.b17*m.b20*m.b31 - 96*m.b17*
                       m.b20*m.b32 - 64*m.b17*m.b20*m.b33 - 32*m.b17*m.b20*m.b34 - 1088*m.b17*m.b21*m.b22 - 960*m.b17*
                       m.b21*m.b23 - 832*m.b17*m.b21*m.b24 - 384*m.b17*m.b21*m.b25 - 576*m.b17*m.b21*m.b26 - 448*m.b17*
                       m.b21*m.b27 - 320*m.b17*m.b21*m.b28 - 256*m.b17*m.b21*m.b29 - 192*m.b17*m.b21*m.b30 - 128*m.b17*
                       m.b21*m.b31 - 96*m.b17*m.b21*m.b32 - 64*m.b17*m.b21*m.b33 - 32*m.b17*m.b21*m.b34 - 960*m.b17*
                       m.b22*m.b23 - 832*m.b17*m.b22*m.b24 - 704*m.b17*m.b22*m.b25 - 576*m.b17*m.b22*m.b26 - 192*m.b17*
                       m.b22*m.b27 - 320*m.b17*m.b22*m.b28 - 224*m.b17*m.b22*m.b29 - 160*m.b17*m.b22*m.b30 - 128*m.b17*
                       m.b22*m.b31 - 96*m.b17*m.b22*m.b32 - 64*m.b17*m.b22*m.b33 - 32*m.b17*m.b22*m.b34 - 832*m.b17*
                       m.b23*m.b24 - 704*m.b17*m.b23*m.b25 - 576*m.b17*m.b23*m.b26 - 448*m.b17*m.b23*m.b27 - 320*m.b17*
                       m.b23*m.b28 - 160*m.b17*m.b23*m.b30 - 128*m.b17*m.b23*m.b31 - 96*m.b17*m.b23*m.b32 - 64*m.b17*
                       m.b23*m.b33 - 32*m.b17*m.b23*m.b34 - 704*m.b17*m.b24*m.b25 - 576*m.b17*m.b24*m.b26 - 448*m.b17*
                       m.b24*m.b27 - 320*m.b17*m.b24*m.b28 - 224*m.b17*m.b24*m.b29 - 160*m.b17*m.b24*m.b30 - 96*m.b17*
                       m.b24*m.b32 - 64*m.b17*m.b24*m.b33 - 32*m.b17*m.b24*m.b34 - 576*m.b17*m.b25*m.b26 - 448*m.b17*
                       m.b25*m.b27 - 352*m.b17*m.b25*m.b28 - 256*m.b17*m.b25*m.b29 - 160*m.b17*m.b25*m.b30 - 128*m.b17*
                       m.b25*m.b31 - 96*m.b17*m.b25*m.b32 - 32*m.b17*m.b25*m.b34 - 480*m.b17*m.b26*m.b27 - 384*m.b17*
                       m.b26*m.b28 - 288*m.b17*m.b26*m.b29 - 192*m.b17*m.b26*m.b30 - 128*m.b17*m.b26*m.b31 - 96*m.b17*
                       m.b26*m.b32 - 64*m.b17*m.b26*m.b33 - 32*m.b17*m.b26*m.b34 - 416*m.b17*m.b27*m.b28 - 320*m.b17*
                       m.b27*m.b29 - 224*m.b17*m.b27*m.b30 - 128*m.b17*m.b27*m.b31 - 96*m.b17*m.b27*m.b32 - 64*m.b17*
                       m.b27*m.b33 - 32*m.b17*m.b27*m.b34 - 352*m.b17*m.b28*m.b29 - 256*m.b17*m.b28*m.b30 - 160*m.b17*
                       m.b28*m.b31 - 96*m.b17*m.b28*m.b32 - 64*m.b17*m.b28*m.b33 - 32*m.b17*m.b28*m.b34 - 288*m.b17*
                       m.b29*m.b30 - 192*m.b17*m.b29*m.b31 - 96*m.b17*m.b29*m.b32 - 64*m.b17*m.b29*m.b33 - 32*m.b17*
                       m.b29*m.b34 - 224*m.b17*m.b30*m.b31 - 128*m.b17*m.b30*m.b32 - 64*m.b17*m.b30*m.b33 - 32*m.b17*
                       m.b30*m.b34 - 160*m.b17*m.b31*m.b32 - 64*m.b17*m.b31*m.b33 - 32*m.b17*m.b31*m.b34 - 96*m.b17*
                       m.b32*m.b33 - 32*m.b17*m.b32*m.b34 - 32*m.b17*m.b33*m.b34 - 960*m.b18*m.b19*m.b20 - 1344*m.b18*
                       m.b19*m.b21 - 1216*m.b18*m.b19*m.b22 - 1088*m.b18*m.b19*m.b23 - 960*m.b18*m.b19*m.b24 - 832*m.b18
                       *m.b19*m.b25 - 704*m.b18*m.b19*m.b26 - 576*m.b18*m.b19*m.b27 - 480*m.b18*m.b19*m.b28 - 416*m.b18*
                       m.b19*m.b29 - 352*m.b18*m.b19*m.b30 - 288*m.b18*m.b19*m.b31 - 224*m.b18*m.b19*m.b32 - 160*m.b18*
                       m.b19*m.b33 - 96*m.b18*m.b19*m.b34 - 32*m.b18*m.b19*m.b35 - 1344*m.b18*m.b20*m.b21 - 768*m.b18*
                       m.b20*m.b22 - 1088*m.b18*m.b20*m.b23 - 960*m.b18*m.b20*m.b24 - 832*m.b18*m.b20*m.b25 - 704*m.b18*
                       m.b20*m.b26 - 576*m.b18*m.b20*m.b27 - 448*m.b18*m.b20*m.b28 - 384*m.b18*m.b20*m.b29 - 320*m.b18*
                       m.b20*m.b30 - 256*m.b18*m.b20*m.b31 - 192*m.b18*m.b20*m.b32 - 128*m.b18*m.b20*m.b33 - 64*m.b18*
                       m.b20*m.b34 - 32*m.b18*m.b20*m.b35 - 1216*m.b18*m.b21*m.b22 - 1088*m.b18*m.b21*m.b23 - 576*m.b18*
                       m.b21*m.b24 - 832*m.b18*m.b21*m.b25 - 704*m.b18*m.b21*m.b26 - 576*m.b18*m.b21*m.b27 - 448*m.b18*
                       m.b21*m.b28 - 352*m.b18*m.b21*m.b29 - 288*m.b18*m.b21*m.b30 - 224*m.b18*m.b21*m.b31 - 160*m.b18*
                       m.b21*m.b32 - 96*m.b18*m.b21*m.b33 - 64*m.b18*m.b21*m.b34 - 32*m.b18*m.b21*m.b35 - 1088*m.b18*
                       m.b22*m.b23 - 960*m.b18*m.b22*m.b24 - 832*m.b18*m.b22*m.b25 - 384*m.b18*m.b22*m.b26 - 576*m.b18*
                       m.b22*m.b27 - 448*m.b18*m.b22*m.b28 - 320*m.b18*m.b22*m.b29 - 256*m.b18*m.b22*m.b30 - 192*m.b18*
                       m.b22*m.b31 - 128*m.b18*m.b22*m.b32 - 96*m.b18*m.b22*m.b33 - 64*m.b18*m.b22*m.b34 - 32*m.b18*
                       m.b22*m.b35 - 960*m.b18*m.b23*m.b24 - 832*m.b18*m.b23*m.b25 - 704*m.b18*m.b23*m.b26 - 576*m.b18*
                       m.b23*m.b27 - 192*m.b18*m.b23*m.b28 - 320*m.b18*m.b23*m.b29 - 224*m.b18*m.b23*m.b30 - 160*m.b18*
                       m.b23*m.b31 - 128*m.b18*m.b23*m.b32 - 96*m.b18*m.b23*m.b33 - 64*m.b18*m.b23*m.b34 - 32*m.b18*
                       m.b23*m.b35 - 832*m.b18*m.b24*m.b25 - 704*m.b18*m.b24*m.b26 - 576*m.b18*m.b24*m.b27 - 448*m.b18*
                       m.b24*m.b28 - 320*m.b18*m.b24*m.b29 - 160*m.b18*m.b24*m.b31 - 128*m.b18*m.b24*m.b32 - 96*m.b18*
                       m.b24*m.b33 - 64*m.b18*m.b24*m.b34 - 32*m.b18*m.b24*m.b35 - 704*m.b18*m.b25*m.b26 - 576*m.b18*
                       m.b25*m.b27 - 448*m.b18*m.b25*m.b28 - 320*m.b18*m.b25*m.b29 - 224*m.b18*m.b25*m.b30 - 160*m.b18*
                       m.b25*m.b31 - 96*m.b18*m.b25*m.b33 - 64*m.b18*m.b25*m.b34 - 32*m.b18*m.b25*m.b35 - 576*m.b18*
                       m.b26*m.b27 - 448*m.b18*m.b26*m.b28 - 352*m.b18*m.b26*m.b29 - 256*m.b18*m.b26*m.b30 - 160*m.b18*
                       m.b26*m.b31 - 128*m.b18*m.b26*m.b32 - 96*m.b18*m.b26*m.b33 - 32*m.b18*m.b26*m.b35 - 480*m.b18*
                       m.b27*m.b28 - 384*m.b18*m.b27*m.b29 - 288*m.b18*m.b27*m.b30 - 192*m.b18*m.b27*m.b31 - 128*m.b18*
                       m.b27*m.b32 - 96*m.b18*m.b27*m.b33 - 64*m.b18*m.b27*m.b34 - 32*m.b18*m.b27*m.b35 - 416*m.b18*
                       m.b28*m.b29 - 320*m.b18*m.b28*m.b30 - 224*m.b18*m.b28*m.b31 - 128*m.b18*m.b28*m.b32 - 96*m.b18*
                       m.b28*m.b33 - 64*m.b18*m.b28*m.b34 - 32*m.b18*m.b28*m.b35 - 352*m.b18*m.b29*m.b30 - 256*m.b18*
                       m.b29*m.b31 - 160*m.b18*m.b29*m.b32 - 96*m.b18*m.b29*m.b33 - 64*m.b18*m.b29*m.b34 - 32*m.b18*
                       m.b29*m.b35 - 288*m.b18*m.b30*m.b31 - 192*m.b18*m.b30*m.b32 - 96*m.b18*m.b30*m.b33 - 64*m.b18*
                       m.b30*m.b34 - 32*m.b18*m.b30*m.b35 - 224*m.b18*m.b31*m.b32 - 128*m.b18*m.b31*m.b33 - 64*m.b18*
                       m.b31*m.b34 - 32*m.b18*m.b31*m.b35 - 160*m.b18*m.b32*m.b33 - 64*m.b18*m.b32*m.b34 - 32*m.b18*
                       m.b32*m.b35 - 96*m.b18*m.b33*m.b34 - 32*m.b18*m.b33*m.b35 - 32*m.b18*m.b34*m.b35 - 928*m.b19*
                       m.b20*m.b21 - 1280*m.b19*m.b20*m.b22 - 1152*m.b19*m.b20*m.b23 - 1024*m.b19*m.b20*m.b24 - 896*
                       m.b19*m.b20*m.b25 - 768*m.b19*m.b20*m.b26 - 640*m.b19*m.b20*m.b27 - 512*m.b19*m.b20*m.b28 - 416*
                       m.b19*m.b20*m.b29 - 352*m.b19*m.b20*m.b30 - 288*m.b19*m.b20*m.b31 - 224*m.b19*m.b20*m.b32 - 160*
                       m.b19*m.b20*m.b33 - 96*m.b19*m.b20*m.b34 - 32*m.b19*m.b20*m.b35 - 1280*m.b19*m.b21*m.b22 - 736*
                       m.b19*m.b21*m.b23 - 1024*m.b19*m.b21*m.b24 - 896*m.b19*m.b21*m.b25 - 768*m.b19*m.b21*m.b26 - 640*
                       m.b19*m.b21*m.b27 - 512*m.b19*m.b21*m.b28 - 384*m.b19*m.b21*m.b29 - 320*m.b19*m.b21*m.b30 - 256*
                       m.b19*m.b21*m.b31 - 192*m.b19*m.b21*m.b32 - 128*m.b19*m.b21*m.b33 - 64*m.b19*m.b21*m.b34 - 32*
                       m.b19*m.b21*m.b35 - 1152*m.b19*m.b22*m.b23 - 1024*m.b19*m.b22*m.b24 - 544*m.b19*m.b22*m.b25 - 768
                       *m.b19*m.b22*m.b26 - 640*m.b19*m.b22*m.b27 - 512*m.b19*m.b22*m.b28 - 384*m.b19*m.b22*m.b29 - 288*
                       m.b19*m.b22*m.b30 - 224*m.b19*m.b22*m.b31 - 160*m.b19*m.b22*m.b32 - 96*m.b19*m.b22*m.b33 - 64*
                       m.b19*m.b22*m.b34 - 32*m.b19*m.b22*m.b35 - 1024*m.b19*m.b23*m.b24 - 896*m.b19*m.b23*m.b25 - 768*
                       m.b19*m.b23*m.b26 - 352*m.b19*m.b23*m.b27 - 512*m.b19*m.b23*m.b28 - 384*m.b19*m.b23*m.b29 - 256*
                       m.b19*m.b23*m.b30 - 192*m.b19*m.b23*m.b31 - 128*m.b19*m.b23*m.b32 - 96*m.b19*m.b23*m.b33 - 64*
                       m.b19*m.b23*m.b34 - 32*m.b19*m.b23*m.b35 - 896*m.b19*m.b24*m.b25 - 768*m.b19*m.b24*m.b26 - 640*
                       m.b19*m.b24*m.b27 - 512*m.b19*m.b24*m.b28 - 160*m.b19*m.b24*m.b29 - 256*m.b19*m.b24*m.b30 - 160*
                       m.b19*m.b24*m.b31 - 128*m.b19*m.b24*m.b32 - 96*m.b19*m.b24*m.b33 - 64*m.b19*m.b24*m.b34 - 32*
                       m.b19*m.b24*m.b35 - 768*m.b19*m.b25*m.b26 - 640*m.b19*m.b25*m.b27 - 512*m.b19*m.b25*m.b28 - 384*
                       m.b19*m.b25*m.b29 - 256*m.b19*m.b25*m.b30 - 128*m.b19*m.b25*m.b32 - 96*m.b19*m.b25*m.b33 - 64*
                       m.b19*m.b25*m.b34 - 32*m.b19*m.b25*m.b35 - 640*m.b19*m.b26*m.b27 - 512*m.b19*m.b26*m.b28 - 384*
                       m.b19*m.b26*m.b29 - 288*m.b19*m.b26*m.b30 - 192*m.b19*m.b26*m.b31 - 128*m.b19*m.b26*m.b32 - 64*
                       m.b19*m.b26*m.b34 - 32*m.b19*m.b26*m.b35 - 512*m.b19*m.b27*m.b28 - 416*m.b19*m.b27*m.b29 - 320*
                       m.b19*m.b27*m.b30 - 224*m.b19*m.b27*m.b31 - 128*m.b19*m.b27*m.b32 - 96*m.b19*m.b27*m.b33 - 64*
                       m.b19*m.b27*m.b34 - 448*m.b19*m.b28*m.b29 - 352*m.b19*m.b28*m.b30 - 256*m.b19*m.b28*m.b31 - 160*
                       m.b19*m.b28*m.b32 - 96*m.b19*m.b28*m.b33 - 64*m.b19*m.b28*m.b34 - 32*m.b19*m.b28*m.b35 - 384*
                       m.b19*m.b29*m.b30 - 288*m.b19*m.b29*m.b31 - 192*m.b19*m.b29*m.b32 - 96*m.b19*m.b29*m.b33 - 64*
                       m.b19*m.b29*m.b34 - 32*m.b19*m.b29*m.b35 - 320*m.b19*m.b30*m.b31 - 224*m.b19*m.b30*m.b32 - 128*
                       m.b19*m.b30*m.b33 - 64*m.b19*m.b30*m.b34 - 32*m.b19*m.b30*m.b35 - 256*m.b19*m.b31*m.b32 - 160*
                       m.b19*m.b31*m.b33 - 64*m.b19*m.b31*m.b34 - 32*m.b19*m.b31*m.b35 - 192*m.b19*m.b32*m.b33 - 96*
                       m.b19*m.b32*m.b34 - 32*m.b19*m.b32*m.b35 - 128*m.b19*m.b33*m.b34 - 32*m.b19*m.b33*m.b35 - 64*
                       m.b19*m.b34*m.b35 - 864*m.b20*m.b21*m.b22 - 1216*m.b20*m.b21*m.b23 - 1088*m.b20*m.b21*m.b24 - 960
                       *m.b20*m.b21*m.b25 - 832*m.b20*m.b21*m.b26 - 704*m.b20*m.b21*m.b27 - 576*m.b20*m.b21*m.b28 - 448*
                       m.b20*m.b21*m.b29 - 352*m.b20*m.b21*m.b30 - 288*m.b20*m.b21*m.b31 - 224*m.b20*m.b21*m.b32 - 160*
                       m.b20*m.b21*m.b33 - 96*m.b20*m.b21*m.b34 - 32*m.b20*m.b21*m.b35 - 1184*m.b20*m.b22*m.b23 - 704*
                       m.b20*m.b22*m.b24 - 960*m.b20*m.b22*m.b25 - 832*m.b20*m.b22*m.b26 - 704*m.b20*m.b22*m.b27 - 576*
                       m.b20*m.b22*m.b28 - 448*m.b20*m.b22*m.b29 - 320*m.b20*m.b22*m.b30 - 256*m.b20*m.b22*m.b31 - 192*
                       m.b20*m.b22*m.b32 - 128*m.b20*m.b22*m.b33 - 64*m.b20*m.b22*m.b34 - 32*m.b20*m.b22*m.b35 - 1056*
                       m.b20*m.b23*m.b24 - 960*m.b20*m.b23*m.b25 - 512*m.b20*m.b23*m.b26 - 704*m.b20*m.b23*m.b27 - 576*
                       m.b20*m.b23*m.b28 - 448*m.b20*m.b23*m.b29 - 320*m.b20*m.b23*m.b30 - 224*m.b20*m.b23*m.b31 - 160*
                       m.b20*m.b23*m.b32 - 96*m.b20*m.b23*m.b33 - 64*m.b20*m.b23*m.b34 - 32*m.b20*m.b23*m.b35 - 928*
                       m.b20*m.b24*m.b25 - 832*m.b20*m.b24*m.b26 - 704*m.b20*m.b24*m.b27 - 320*m.b20*m.b24*m.b28 - 448*
                       m.b20*m.b24*m.b29 - 320*m.b20*m.b24*m.b30 - 192*m.b20*m.b24*m.b31 - 128*m.b20*m.b24*m.b32 - 96*
                       m.b20*m.b24*m.b33 - 64*m.b20*m.b24*m.b34 - 32*m.b20*m.b24*m.b35 - 800*m.b20*m.b25*m.b26 - 704*
                       m.b20*m.b25*m.b27 - 576*m.b20*m.b25*m.b28 - 448*m.b20*m.b25*m.b29 - 128*m.b20*m.b25*m.b30 - 192*
                       m.b20*m.b25*m.b31 - 128*m.b20*m.b25*m.b32 - 96*m.b20*m.b25*m.b33 - 64*m.b20*m.b25*m.b34 - 32*
                       m.b20*m.b25*m.b35 - 672*m.b20*m.b26*m.b27 - 576*m.b20*m.b26*m.b28 - 448*m.b20*m.b26*m.b29 - 320*
                       m.b20*m.b26*m.b30 - 224*m.b20*m.b26*m.b31 - 96*m.b20*m.b26*m.b33 - 64*m.b20*m.b26*m.b34 - 32*
                       m.b20*m.b26*m.b35 - 544*m.b20*m.b27*m.b28 - 448*m.b20*m.b27*m.b29 - 352*m.b20*m.b27*m.b30 - 256*
                       m.b20*m.b27*m.b31 - 160*m.b20*m.b27*m.b32 - 96*m.b20*m.b27*m.b33 - 32*m.b20*m.b27*m.b35 - 448*
                       m.b20*m.b28*m.b29 - 384*m.b20*m.b28*m.b30 - 288*m.b20*m.b28*m.b31 - 192*m.b20*m.b28*m.b32 - 96*
                       m.b20*m.b28*m.b33 - 64*m.b20*m.b28*m.b34 - 32*m.b20*m.b28*m.b35 - 384*m.b20*m.b29*m.b30 - 320*
                       m.b20*m.b29*m.b31 - 224*m.b20*m.b29*m.b32 - 128*m.b20*m.b29*m.b33 - 64*m.b20*m.b29*m.b34 - 32*
                       m.b20*m.b29*m.b35 - 320*m.b20*m.b30*m.b31 - 256*m.b20*m.b30*m.b32 - 160*m.b20*m.b30*m.b33 - 64*
                       m.b20*m.b30*m.b34 - 32*m.b20*m.b30*m.b35 - 256*m.b20*m.b31*m.b32 - 192*m.b20*m.b31*m.b33 - 96*
                       m.b20*m.b31*m.b34 - 32*m.b20*m.b31*m.b35 - 192*m.b20*m.b32*m.b33 - 128*m.b20*m.b32*m.b34 - 32*
                       m.b20*m.b32*m.b35 - 128*m.b20*m.b33*m.b34 - 64*m.b20*m.b33*m.b35 - 64*m.b20*m.b34*m.b35 - 800*
                       m.b21*m.b22*m.b23 - 1120*m.b21*m.b22*m.b24 - 1024*m.b21*m.b22*m.b25 - 896*m.b21*m.b22*m.b26 - 768
                       *m.b21*m.b22*m.b27 - 640*m.b21*m.b22*m.b28 - 512*m.b21*m.b22*m.b29 - 384*m.b21*m.b22*m.b30 - 288*
                       m.b21*m.b22*m.b31 - 224*m.b21*m.b22*m.b32 - 160*m.b21*m.b22*m.b33 - 96*m.b21*m.b22*m.b34 - 32*
                       m.b21*m.b22*m.b35 - 1088*m.b21*m.b23*m.b24 - 640*m.b21*m.b23*m.b25 - 896*m.b21*m.b23*m.b26 - 768*
                       m.b21*m.b23*m.b27 - 640*m.b21*m.b23*m.b28 - 512*m.b21*m.b23*m.b29 - 384*m.b21*m.b23*m.b30 - 256*
                       m.b21*m.b23*m.b31 - 192*m.b21*m.b23*m.b32 - 128*m.b21*m.b23*m.b33 - 64*m.b21*m.b23*m.b34 - 32*
                       m.b21*m.b23*m.b35 - 960*m.b21*m.b24*m.b25 - 864*m.b21*m.b24*m.b26 - 480*m.b21*m.b24*m.b27 - 640*
                       m.b21*m.b24*m.b28 - 512*m.b21*m.b24*m.b29 - 384*m.b21*m.b24*m.b30 - 256*m.b21*m.b24*m.b31 - 160*
                       m.b21*m.b24*m.b32 - 96*m.b21*m.b24*m.b33 - 64*m.b21*m.b24*m.b34 - 32*m.b21*m.b24*m.b35 - 832*
                       m.b21*m.b25*m.b26 - 736*m.b21*m.b25*m.b27 - 640*m.b21*m.b25*m.b28 - 288*m.b21*m.b25*m.b29 - 384*
                       m.b21*m.b25*m.b30 - 256*m.b21*m.b25*m.b31 - 128*m.b21*m.b25*m.b32 - 96*m.b21*m.b25*m.b33 - 64*
                       m.b21*m.b25*m.b34 - 32*m.b21*m.b25*m.b35 - 704*m.b21*m.b26*m.b27 - 608*m.b21*m.b26*m.b28 - 512*
                       m.b21*m.b26*m.b29 - 384*m.b21*m.b26*m.b30 - 96*m.b21*m.b26*m.b31 - 160*m.b21*m.b26*m.b32 - 96*
                       m.b21*m.b26*m.b33 - 64*m.b21*m.b26*m.b34 - 32*m.b21*m.b26*m.b35 - 576*m.b21*m.b27*m.b28 - 480*
                       m.b21*m.b27*m.b29 - 384*m.b21*m.b27*m.b30 - 288*m.b21*m.b27*m.b31 - 192*m.b21*m.b27*m.b32 - 64*
                       m.b21*m.b27*m.b34 - 32*m.b21*m.b27*m.b35 - 448*m.b21*m.b28*m.b29 - 384*m.b21*m.b28*m.b30 - 320*
                       m.b21*m.b28*m.b31 - 224*m.b21*m.b28*m.b32 - 128*m.b21*m.b28*m.b33 - 64*m.b21*m.b28*m.b34 - 384*
                       m.b21*m.b29*m.b30 - 320*m.b21*m.b29*m.b31 - 256*m.b21*m.b29*m.b32 - 160*m.b21*m.b29*m.b33 - 64*
                       m.b21*m.b29*m.b34 - 32*m.b21*m.b29*m.b35 - 320*m.b21*m.b30*m.b31 - 256*m.b21*m.b30*m.b32 - 192*
                       m.b21*m.b30*m.b33 - 96*m.b21*m.b30*m.b34 - 32*m.b21*m.b30*m.b35 - 256*m.b21*m.b31*m.b32 - 192*
                       m.b21*m.b31*m.b33 - 128*m.b21*m.b31*m.b34 - 32*m.b21*m.b31*m.b35 - 192*m.b21*m.b32*m.b33 - 128*
                       m.b21*m.b32*m.b34 - 64*m.b21*m.b32*m.b35 - 128*m.b21*m.b33*m.b34 - 64*m.b21*m.b33*m.b35 - 64*
                       m.b21*m.b34*m.b35 - 736*m.b22*m.b23*m.b24 - 1024*m.b22*m.b23*m.b25 - 928*m.b22*m.b23*m.b26 - 832*
                       m.b22*m.b23*m.b27 - 704*m.b22*m.b23*m.b28 - 576*m.b22*m.b23*m.b29 - 448*m.b22*m.b23*m.b30 - 320*
                       m.b22*m.b23*m.b31 - 224*m.b22*m.b23*m.b32 - 160*m.b22*m.b23*m.b33 - 96*m.b22*m.b23*m.b34 - 32*
                       m.b22*m.b23*m.b35 - 992*m.b22*m.b24*m.b25 - 576*m.b22*m.b24*m.b26 - 800*m.b22*m.b24*m.b27 - 704*
                       m.b22*m.b24*m.b28 - 576*m.b22*m.b24*m.b29 - 448*m.b22*m.b24*m.b30 - 320*m.b22*m.b24*m.b31 - 192*
                       m.b22*m.b24*m.b32 - 128*m.b22*m.b24*m.b33 - 64*m.b22*m.b24*m.b34 - 32*m.b22*m.b24*m.b35 - 864*
                       m.b22*m.b25*m.b26 - 768*m.b22*m.b25*m.b27 - 416*m.b22*m.b25*m.b28 - 576*m.b22*m.b25*m.b29 - 448*
                       m.b22*m.b25*m.b30 - 320*m.b22*m.b25*m.b31 - 192*m.b22*m.b25*m.b32 - 96*m.b22*m.b25*m.b33 - 64*
                       m.b22*m.b25*m.b34 - 32*m.b22*m.b25*m.b35 - 736*m.b22*m.b26*m.b27 - 640*m.b22*m.b26*m.b28 - 544*
                       m.b22*m.b26*m.b29 - 256*m.b22*m.b26*m.b30 - 320*m.b22*m.b26*m.b31 - 192*m.b22*m.b26*m.b32 - 96*
                       m.b22*m.b26*m.b33 - 64*m.b22*m.b26*m.b34 - 32*m.b22*m.b26*m.b35 - 608*m.b22*m.b27*m.b28 - 512*
                       m.b22*m.b27*m.b29 - 416*m.b22*m.b27*m.b30 - 320*m.b22*m.b27*m.b31 - 96*m.b22*m.b27*m.b32 - 128*
                       m.b22*m.b27*m.b33 - 64*m.b22*m.b27*m.b34 - 32*m.b22*m.b27*m.b35 - 480*m.b22*m.b28*m.b29 - 384*
                       m.b22*m.b28*m.b30 - 320*m.b22*m.b28*m.b31 - 256*m.b22*m.b28*m.b32 - 160*m.b22*m.b28*m.b33 - 32*
                       m.b22*m.b28*m.b35 - 384*m.b22*m.b29*m.b30 - 320*m.b22*m.b29*m.b31 - 256*m.b22*m.b29*m.b32 - 192*
                       m.b22*m.b29*m.b33 - 96*m.b22*m.b29*m.b34 - 32*m.b22*m.b29*m.b35 - 320*m.b22*m.b30*m.b31 - 256*
                       m.b22*m.b30*m.b32 - 192*m.b22*m.b30*m.b33 - 128*m.b22*m.b30*m.b34 - 32*m.b22*m.b30*m.b35 - 256*
                       m.b22*m.b31*m.b32 - 192*m.b22*m.b31*m.b33 - 128*m.b22*m.b31*m.b34 - 64*m.b22*m.b31*m.b35 - 192*
                       m.b22*m.b32*m.b33 - 128*m.b22*m.b32*m.b34 - 64*m.b22*m.b32*m.b35 - 128*m.b22*m.b33*m.b34 - 64*
                       m.b22*m.b33*m.b35 - 64*m.b22*m.b34*m.b35 - 672*m.b23*m.b24*m.b25 - 928*m.b23*m.b24*m.b26 - 832*
                       m.b23*m.b24*m.b27 - 736*m.b23*m.b24*m.b28 - 640*m.b23*m.b24*m.b29 - 512*m.b23*m.b24*m.b30 - 384*
                       m.b23*m.b24*m.b31 - 256*m.b23*m.b24*m.b32 - 160*m.b23*m.b24*m.b33 - 96*m.b23*m.b24*m.b34 - 32*
                       m.b23*m.b24*m.b35 - 896*m.b23*m.b25*m.b26 - 512*m.b23*m.b25*m.b27 - 704*m.b23*m.b25*m.b28 - 608*
                       m.b23*m.b25*m.b29 - 512*m.b23*m.b25*m.b30 - 384*m.b23*m.b25*m.b31 - 256*m.b23*m.b25*m.b32 - 128*
                       m.b23*m.b25*m.b33 - 64*m.b23*m.b25*m.b34 - 32*m.b23*m.b25*m.b35 - 768*m.b23*m.b26*m.b27 - 672*
                       m.b23*m.b26*m.b28 - 352*m.b23*m.b26*m.b29 - 480*m.b23*m.b26*m.b30 - 384*m.b23*m.b26*m.b31 - 256*
                       m.b23*m.b26*m.b32 - 128*m.b23*m.b26*m.b33 - 64*m.b23*m.b26*m.b34 - 32*m.b23*m.b26*m.b35 - 640*
                       m.b23*m.b27*m.b28 - 544*m.b23*m.b27*m.b29 - 448*m.b23*m.b27*m.b30 - 192*m.b23*m.b27*m.b31 - 256*
                       m.b23*m.b27*m.b32 - 160*m.b23*m.b27*m.b33 - 64*m.b23*m.b27*m.b34 - 32*m.b23*m.b27*m.b35 - 512*
                       m.b23*m.b28*m.b29 - 416*m.b23*m.b28*m.b30 - 320*m.b23*m.b28*m.b31 - 256*m.b23*m.b28*m.b32 - 96*
                       m.b23*m.b28*m.b33 - 96*m.b23*m.b28*m.b34 - 32*m.b23*m.b28*m.b35 - 384*m.b23*m.b29*m.b30 - 320*
                       m.b23*m.b29*m.b31 - 256*m.b23*m.b29*m.b32 - 192*m.b23*m.b29*m.b33 - 128*m.b23*m.b29*m.b34 - 320*
                       m.b23*m.b30*m.b31 - 256*m.b23*m.b30*m.b32 - 192*m.b23*m.b30*m.b33 - 128*m.b23*m.b30*m.b34 - 64*
                       m.b23*m.b30*m.b35 - 256*m.b23*m.b31*m.b32 - 192*m.b23*m.b31*m.b33 - 128*m.b23*m.b31*m.b34 - 64*
                       m.b23*m.b31*m.b35 - 192*m.b23*m.b32*m.b33 - 128*m.b23*m.b32*m.b34 - 64*m.b23*m.b32*m.b35 - 128*
                       m.b23*m.b33*m.b34 - 64*m.b23*m.b33*m.b35 - 64*m.b23*m.b34*m.b35 - 608*m.b24*m.b25*m.b26 - 832*
                       m.b24*m.b25*m.b27 - 736*m.b24*m.b25*m.b28 - 640*m.b24*m.b25*m.b29 - 544*m.b24*m.b25*m.b30 - 448*
                       m.b24*m.b25*m.b31 - 320*m.b24*m.b25*m.b32 - 192*m.b24*m.b25*m.b33 - 96*m.b24*m.b25*m.b34 - 32*
                       m.b24*m.b25*m.b35 - 800*m.b24*m.b26*m.b27 - 448*m.b24*m.b26*m.b28 - 608*m.b24*m.b26*m.b29 - 512*
                       m.b24*m.b26*m.b30 - 416*m.b24*m.b26*m.b31 - 320*m.b24*m.b26*m.b32 - 192*m.b24*m.b26*m.b33 - 64*
                       m.b24*m.b26*m.b34 - 32*m.b24*m.b26*m.b35 - 672*m.b24*m.b27*m.b28 - 576*m.b24*m.b27*m.b29 - 288*
                       m.b24*m.b27*m.b30 - 384*m.b24*m.b27*m.b31 - 288*m.b24*m.b27*m.b32 - 192*m.b24*m.b27*m.b33 - 96*
                       m.b24*m.b27*m.b34 - 32*m.b24*m.b27*m.b35 - 544*m.b24*m.b28*m.b29 - 448*m.b24*m.b28*m.b30 - 352*
                       m.b24*m.b28*m.b31 - 128*m.b24*m.b28*m.b32 - 192*m.b24*m.b28*m.b33 - 128*m.b24*m.b28*m.b34 - 32*
                       m.b24*m.b28*m.b35 - 416*m.b24*m.b29*m.b30 - 320*m.b24*m.b29*m.b31 - 256*m.b24*m.b29*m.b32 - 192*
                       m.b24*m.b29*m.b33 - 64*m.b24*m.b29*m.b34 - 64*m.b24*m.b29*m.b35 - 320*m.b24*m.b30*m.b31 - 256*
                       m.b24*m.b30*m.b32 - 192*m.b24*m.b30*m.b33 - 128*m.b24*m.b30*m.b34 - 64*m.b24*m.b30*m.b35 - 256*
                       m.b24*m.b31*m.b32 - 192*m.b24*m.b31*m.b33 - 128*m.b24*m.b31*m.b34 - 64*m.b24*m.b31*m.b35 - 192*
                       m.b24*m.b32*m.b33 - 128*m.b24*m.b32*m.b34 - 64*m.b24*m.b32*m.b35 - 128*m.b24*m.b33*m.b34 - 64*
                       m.b24*m.b33*m.b35 - 64*m.b24*m.b34*m.b35 - 544*m.b25*m.b26*m.b27 - 736*m.b25*m.b26*m.b28 - 640*
                       m.b25*m.b26*m.b29 - 544*m.b25*m.b26*m.b30 - 448*m.b25*m.b26*m.b31 - 352*m.b25*m.b26*m.b32 - 256*
                       m.b25*m.b26*m.b33 - 128*m.b25*m.b26*m.b34 - 32*m.b25*m.b26*m.b35 - 704*m.b25*m.b27*m.b28 - 384*
                       m.b25*m.b27*m.b29 - 512*m.b25*m.b27*m.b30 - 416*m.b25*m.b27*m.b31 - 320*m.b25*m.b27*m.b32 - 224*
                       m.b25*m.b27*m.b33 - 128*m.b25*m.b27*m.b34 - 32*m.b25*m.b27*m.b35 - 576*m.b25*m.b28*m.b29 - 480*
                       m.b25*m.b28*m.b30 - 224*m.b25*m.b28*m.b31 - 288*m.b25*m.b28*m.b32 - 192*m.b25*m.b28*m.b33 - 128*
                       m.b25*m.b28*m.b34 - 64*m.b25*m.b28*m.b35 - 448*m.b25*m.b29*m.b30 - 352*m.b25*m.b29*m.b31 - 256*
                       m.b25*m.b29*m.b32 - 96*m.b25*m.b29*m.b33 - 128*m.b25*m.b29*m.b34 - 64*m.b25*m.b29*m.b35 - 320*
                       m.b25*m.b30*m.b31 - 256*m.b25*m.b30*m.b32 - 192*m.b25*m.b30*m.b33 - 128*m.b25*m.b30*m.b34 - 32*
                       m.b25*m.b30*m.b35 - 256*m.b25*m.b31*m.b32 - 192*m.b25*m.b31*m.b33 - 128*m.b25*m.b31*m.b34 - 64*
                       m.b25*m.b31*m.b35 - 192*m.b25*m.b32*m.b33 - 128*m.b25*m.b32*m.b34 - 64*m.b25*m.b32*m.b35 - 128*
                       m.b25*m.b33*m.b34 - 64*m.b25*m.b33*m.b35 - 64*m.b25*m.b34*m.b35 - 480*m.b26*m.b27*m.b28 - 640*
                       m.b26*m.b27*m.b29 - 544*m.b26*m.b27*m.b30 - 448*m.b26*m.b27*m.b31 - 352*m.b26*m.b27*m.b32 - 256*
                       m.b26*m.b27*m.b33 - 160*m.b26*m.b27*m.b34 - 64*m.b26*m.b27*m.b35 - 608*m.b26*m.b28*m.b29 - 320*
                       m.b26*m.b28*m.b30 - 416*m.b26*m.b28*m.b31 - 320*m.b26*m.b28*m.b32 - 224*m.b26*m.b28*m.b33 - 128*
                       m.b26*m.b28*m.b34 - 64*m.b26*m.b28*m.b35 - 480*m.b26*m.b29*m.b30 - 384*m.b26*m.b29*m.b31 - 160*
                       m.b26*m.b29*m.b32 - 192*m.b26*m.b29*m.b33 - 128*m.b26*m.b29*m.b34 - 64*m.b26*m.b29*m.b35 - 352*
                       m.b26*m.b30*m.b31 - 256*m.b26*m.b30*m.b32 - 192*m.b26*m.b30*m.b33 - 64*m.b26*m.b30*m.b34 - 64*
                       m.b26*m.b30*m.b35 - 256*m.b26*m.b31*m.b32 - 192*m.b26*m.b31*m.b33 - 128*m.b26*m.b31*m.b34 - 64*
                       m.b26*m.b31*m.b35 - 192*m.b26*m.b32*m.b33 - 128*m.b26*m.b32*m.b34 - 64*m.b26*m.b32*m.b35 - 128*
                       m.b26*m.b33*m.b34 - 64*m.b26*m.b33*m.b35 - 64*m.b26*m.b34*m.b35 - 416*m.b27*m.b28*m.b29 - 544*
                       m.b27*m.b28*m.b30 - 448*m.b27*m.b28*m.b31 - 352*m.b27*m.b28*m.b32 - 256*m.b27*m.b28*m.b33 - 160*
                       m.b27*m.b28*m.b34 - 64*m.b27*m.b28*m.b35 - 512*m.b27*m.b29*m.b30 - 256*m.b27*m.b29*m.b31 - 320*
                       m.b27*m.b29*m.b32 - 224*m.b27*m.b29*m.b33 - 128*m.b27*m.b29*m.b34 - 64*m.b27*m.b29*m.b35 - 384*
                       m.b27*m.b30*m.b31 - 288*m.b27*m.b30*m.b32 - 96*m.b27*m.b30*m.b33 - 128*m.b27*m.b30*m.b34 - 64*
                       m.b27*m.b30*m.b35 - 256*m.b27*m.b31*m.b32 - 192*m.b27*m.b31*m.b33 - 128*m.b27*m.b31*m.b34 - 32*
                       m.b27*m.b31*m.b35 - 192*m.b27*m.b32*m.b33 - 128*m.b27*m.b32*m.b34 - 64*m.b27*m.b32*m.b35 - 128*
                       m.b27*m.b33*m.b34 - 64*m.b27*m.b33*m.b35 - 64*m.b27*m.b34*m.b35 - 352*m.b28*m.b29*m.b30 - 448*
                       m.b28*m.b29*m.b31 - 352*m.b28*m.b29*m.b32 - 256*m.b28*m.b29*m.b33 - 160*m.b28*m.b29*m.b34 - 64*
                       m.b28*m.b29*m.b35 - 416*m.b28*m.b30*m.b31 - 192*m.b28*m.b30*m.b32 - 224*m.b28*m.b30*m.b33 - 128*
                       m.b28*m.b30*m.b34 - 64*m.b28*m.b30*m.b35 - 288*m.b28*m.b31*m.b32 - 192*m.b28*m.b31*m.b33 - 64*
                       m.b28*m.b31*m.b34 - 64*m.b28*m.b31*m.b35 - 192*m.b28*m.b32*m.b33 - 128*m.b28*m.b32*m.b34 - 64*
                       m.b28*m.b32*m.b35 - 128*m.b28*m.b33*m.b34 - 64*m.b28*m.b33*m.b35 - 64*m.b28*m.b34*m.b35 - 288*
                       m.b29*m.b30*m.b31 - 352*m.b29*m.b30*m.b32 - 256*m.b29*m.b30*m.b33 - 160*m.b29*m.b30*m.b34 - 64*
                       m.b29*m.b30*m.b35 - 320*m.b29*m.b31*m.b32 - 128*m.b29*m.b31*m.b33 - 128*m.b29*m.b31*m.b34 - 64*
                       m.b29*m.b31*m.b35 - 192*m.b29*m.b32*m.b33 - 128*m.b29*m.b32*m.b34 - 32*m.b29*m.b32*m.b35 - 128*
                       m.b29*m.b33*m.b34 - 64*m.b29*m.b33*m.b35 - 64*m.b29*m.b34*m.b35 - 224*m.b30*m.b31*m.b32 - 256*
                       m.b30*m.b31*m.b33 - 160*m.b30*m.b31*m.b34 - 64*m.b30*m.b31*m.b35 - 224*m.b30*m.b32*m.b33 - 64*
                       m.b30*m.b32*m.b34 - 64*m.b30*m.b32*m.b35 - 128*m.b30*m.b33*m.b34 - 64*m.b30*m.b33*m.b35 - 64*
                       m.b30*m.b34*m.b35 - 160*m.b31*m.b32*m.b33 - 160*m.b31*m.b32*m.b34 - 64*m.b31*m.b32*m.b35 - 128*
                       m.b31*m.b33*m.b34 - 32*m.b31*m.b33*m.b35 - 64*m.b31*m.b34*m.b35 - 96*m.b32*m.b33*m.b34 - 64*m.b32
                       *m.b33*m.b35 - 64*m.b32*m.b34*m.b35 - 32*m.b33*m.b34*m.b35 + 240*m.b1*m.b2 + 232*m.b1*m.b3 + 224*
                       m.b1*m.b4 + 216*m.b1*m.b5 + 208*m.b1*m.b6 + 200*m.b1*m.b7 + 192*m.b1*m.b8 + 184*m.b1*m.b9 + 192*
                       m.b1*m.b10 + 184*m.b1*m.b11 + 176*m.b1*m.b12 + 168*m.b1*m.b13 + 160*m.b1*m.b14 + 152*m.b1*m.b15
                        + 144*m.b1*m.b16 + 136*m.b1*m.b17 + 128*m.b1*m.b18 + 480*m.b2*m.b3 + 480*m.b2*m.b4 + 464*m.b2*
                       m.b5 + 448*m.b2*m.b6 + 432*m.b2*m.b7 + 416*m.b2*m.b8 + 400*m.b2*m.b9 + 384*m.b2*m.b10 + 400*m.b2*
                       m.b11 + 384*m.b2*m.b12 + 368*m.b2*m.b13 + 352*m.b2*m.b14 + 336*m.b2*m.b15 + 320*m.b2*m.b16 + 304*
                       m.b2*m.b17 + 272*m.b2*m.b18 + 128*m.b2*m.b19 + 736*m.b3*m.b4 + 728*m.b3*m.b5 + 720*m.b3*m.b6 + 
                       696*m.b3*m.b7 + 672*m.b3*m.b8 + 648*m.b3*m.b9 + 624*m.b3*m.b10 + 616*m.b3*m.b11 + 624*m.b3*m.b12
                        + 600*m.b3*m.b13 + 576*m.b3*m.b14 + 552*m.b3*m.b15 + 528*m.b3*m.b16 + 488*m.b3*m.b17 + 448*m.b3*
                       m.b18 + 272*m.b3*m.b19 + 128*m.b3*m.b20 + 1008*m.b4*m.b5 + 992*m.b4*m.b6 + 976*m.b4*m.b7 + 960*
                       m.b4*m.b8 + 928*m.b4*m.b9 + 896*m.b4*m.b10 + 864*m.b4*m.b11 + 864*m.b4*m.b12 + 864*m.b4*m.b13 + 
                       832*m.b4*m.b14 + 800*m.b4*m.b15 + 752*m.b4*m.b16 + 704*m.b4*m.b17 + 640*m.b4*m.b18 + 448*m.b4*
                       m.b19 + 272*m.b4*m.b20 + 128*m.b4*m.b21 + 1296*m.b5*m.b6 + 1272*m.b5*m.b7 + 1248*m.b5*m.b8 + 1224
                       *m.b5*m.b9 + 1200*m.b5*m.b10 + 1160*m.b5*m.b11 + 1136*m.b5*m.b12 + 1128*m.b5*m.b13 + 1120*m.b5*
                       m.b14 + 1064*m.b5*m.b15 + 1008*m.b5*m.b16 + 936*m.b5*m.b17 + 864*m.b5*m.b18 + 640*m.b5*m.b19 + 
                       448*m.b5*m.b20 + 272*m.b5*m.b21 + 128*m.b5*m.b22 + 1600*m.b6*m.b7 + 1568*m.b6*m.b8 + 1536*m.b6*
                       m.b9 + 1504*m.b6*m.b10 + 1472*m.b6*m.b11 + 1440*m.b6*m.b12 + 1424*m.b6*m.b13 + 1392*m.b6*m.b14 + 
                       1360*m.b6*m.b15 + 1280*m.b6*m.b16 + 1200*m.b6*m.b17 + 1104*m.b6*m.b18 + 864*m.b6*m.b19 + 640*m.b6
                       *m.b20 + 448*m.b6*m.b21 + 272*m.b6*m.b22 + 128*m.b6*m.b23 + 1920*m.b7*m.b8 + 1880*m.b7*m.b9 + 
                       1840*m.b7*m.b10 + 1800*m.b7*m.b11 + 1760*m.b7*m.b12 + 1720*m.b7*m.b13 + 1696*m.b7*m.b14 + 1640*
                       m.b7*m.b15 + 1584*m.b7*m.b16 + 1480*m.b7*m.b17 + 1376*m.b7*m.b18 + 1104*m.b7*m.b19 + 864*m.b7*
                       m.b20 + 640*m.b7*m.b21 + 448*m.b7*m.b22 + 272*m.b7*m.b23 + 128*m.b7*m.b24 + 2256*m.b8*m.b9 + 2208
                       *m.b8*m.b10 + 2160*m.b8*m.b11 + 2096*m.b8*m.b12 + 2032*m.b8*m.b13 + 1984*m.b8*m.b14 + 1936*m.b8*
                       m.b15 + 1872*m.b8*m.b16 + 1792*m.b8*m.b17 + 1664*m.b8*m.b18 + 1376*m.b8*m.b19 + 1104*m.b8*m.b20
                        + 864*m.b8*m.b21 + 640*m.b8*m.b22 + 448*m.b8*m.b23 + 272*m.b8*m.b24 + 128*m.b8*m.b25 + 2608*m.b9
                       *m.b10 + 2536*m.b9*m.b11 + 2464*m.b9*m.b12 + 2376*m.b9*m.b13 + 2304*m.b9*m.b14 + 2232*m.b9*m.b15
                        + 2160*m.b9*m.b16 + 2072*m.b9*m.b17 + 1984*m.b9*m.b18 + 1664*m.b9*m.b19 + 1376*m.b9*m.b20 + 1104
                       *m.b9*m.b21 + 864*m.b9*m.b22 + 640*m.b9*m.b23 + 448*m.b9*m.b24 + 272*m.b9*m.b25 + 128*m.b9*m.b26
                        + 2944*m.b10*m.b11 + 2848*m.b10*m.b12 + 2752*m.b10*m.b13 + 2640*m.b10*m.b14 + 2560*m.b10*m.b15
                        + 2464*m.b10*m.b16 + 2368*m.b10*m.b17 + 2256*m.b10*m.b18 + 1984*m.b10*m.b19 + 1664*m.b10*m.b20
                        + 1376*m.b10*m.b21 + 1104*m.b10*m.b22 + 864*m.b10*m.b23 + 640*m.b10*m.b24 + 448*m.b10*m.b25 + 
                       272*m.b10*m.b26 + 128*m.b10*m.b27 + 3264*m.b11*m.b12 + 3144*m.b11*m.b13 + 3024*m.b11*m.b14 + 2904
                       *m.b11*m.b15 + 2800*m.b11*m.b16 + 2680*m.b11*m.b17 + 2560*m.b11*m.b18 + 2256*m.b11*m.b19 + 1984*
                       m.b11*m.b20 + 1664*m.b11*m.b21 + 1376*m.b11*m.b22 + 1104*m.b11*m.b23 + 864*m.b11*m.b24 + 640*
                       m.b11*m.b25 + 448*m.b11*m.b26 + 272*m.b11*m.b27 + 128*m.b11*m.b28 + 3568*m.b12*m.b13 + 3424*m.b12
                       *m.b14 + 3280*m.b12*m.b15 + 3152*m.b12*m.b16 + 3024*m.b12*m.b17 + 2880*m.b12*m.b18 + 2560*m.b12*
                       m.b19 + 2256*m.b12*m.b20 + 1984*m.b12*m.b21 + 1664*m.b12*m.b22 + 1376*m.b12*m.b23 + 1104*m.b12*
                       m.b24 + 864*m.b12*m.b25 + 640*m.b12*m.b26 + 448*m.b12*m.b27 + 272*m.b12*m.b28 + 128*m.b12*m.b29
                        + 3856*m.b13*m.b14 + 3688*m.b13*m.b15 + 3536*m.b13*m.b16 + 3384*m.b13*m.b17 + 3232*m.b13*m.b18
                        + 2880*m.b13*m.b19 + 2560*m.b13*m.b20 + 2256*m.b13*m.b21 + 1984*m.b13*m.b22 + 1664*m.b13*m.b23
                        + 1376*m.b13*m.b24 + 1104*m.b13*m.b25 + 864*m.b13*m.b26 + 640*m.b13*m.b27 + 448*m.b13*m.b28 + 
                       272*m.b13*m.b29 + 128*m.b13*m.b30 + 4128*m.b14*m.b15 + 3936*m.b14*m.b16 + 3776*m.b14*m.b17 + 3600
                       *m.b14*m.b18 + 3232*m.b14*m.b19 + 2880*m.b14*m.b20 + 2560*m.b14*m.b21 + 2256*m.b14*m.b22 + 1984*
                       m.b14*m.b23 + 1664*m.b14*m.b24 + 1376*m.b14*m.b25 + 1104*m.b14*m.b26 + 864*m.b14*m.b27 + 640*
                       m.b14*m.b28 + 448*m.b14*m.b29 + 272*m.b14*m.b30 + 128*m.b14*m.b31 + 4384*m.b15*m.b16 + 4184*m.b15
                       *m.b17 + 4000*m.b15*m.b18 + 3600*m.b15*m.b19 + 3232*m.b15*m.b20 + 2880*m.b15*m.b21 + 2560*m.b15*
                       m.b22 + 2256*m.b15*m.b23 + 1984*m.b15*m.b24 + 1664*m.b15*m.b25 + 1376*m.b15*m.b26 + 1104*m.b15*
                       m.b27 + 864*m.b15*m.b28 + 640*m.b15*m.b29 + 448*m.b15*m.b30 + 272*m.b15*m.b31 + 128*m.b15*m.b32
                        + 4624*m.b16*m.b17 + 4416*m.b16*m.b18 + 4000*m.b16*m.b19 + 3600*m.b16*m.b20 + 3232*m.b16*m.b21
                        + 2880*m.b16*m.b22 + 2560*m.b16*m.b23 + 2256*m.b16*m.b24 + 1984*m.b16*m.b25 + 1664*m.b16*m.b26
                        + 1376*m.b16*m.b27 + 1104*m.b16*m.b28 + 864*m.b16*m.b29 + 640*m.b16*m.b30 + 448*m.b16*m.b31 + 
                       272*m.b16*m.b32 + 128*m.b16*m.b33 + 4864*m.b17*m.b18 + 4416*m.b17*m.b19 + 4000*m.b17*m.b20 + 3600
                       *m.b17*m.b21 + 3232*m.b17*m.b22 + 2880*m.b17*m.b23 + 2560*m.b17*m.b24 + 2256*m.b17*m.b25 + 1984*
                       m.b17*m.b26 + 1664*m.b17*m.b27 + 1376*m.b17*m.b28 + 1104*m.b17*m.b29 + 864*m.b17*m.b30 + 640*
                       m.b17*m.b31 + 448*m.b17*m.b32 + 272*m.b17*m.b33 + 128*m.b17*m.b34 + 4864*m.b18*m.b19 + 4416*m.b18
                       *m.b20 + 4000*m.b18*m.b21 + 3600*m.b18*m.b22 + 3232*m.b18*m.b23 + 2880*m.b18*m.b24 + 2560*m.b18*
                       m.b25 + 2256*m.b18*m.b26 + 1984*m.b18*m.b27 + 1664*m.b18*m.b28 + 1376*m.b18*m.b29 + 1104*m.b18*
                       m.b30 + 864*m.b18*m.b31 + 640*m.b18*m.b32 + 448*m.b18*m.b33 + 272*m.b18*m.b34 + 128*m.b18*m.b35
                        + 4624*m.b19*m.b20 + 4184*m.b19*m.b21 + 3776*m.b19*m.b22 + 3384*m.b19*m.b23 + 3024*m.b19*m.b24
                        + 2680*m.b19*m.b25 + 2368*m.b19*m.b26 + 2072*m.b19*m.b27 + 1792*m.b19*m.b28 + 1480*m.b19*m.b29
                        + 1200*m.b19*m.b30 + 936*m.b19*m.b31 + 704*m.b19*m.b32 + 488*m.b19*m.b33 + 304*m.b19*m.b34 + 136
                       *m.b19*m.b35 + 4384*m.b20*m.b21 + 3936*m.b20*m.b22 + 3536*m.b20*m.b23 + 3152*m.b20*m.b24 + 2800*
                       m.b20*m.b25 + 2464*m.b20*m.b26 + 2160*m.b20*m.b27 + 1872*m.b20*m.b28 + 1584*m.b20*m.b29 + 1280*
                       m.b20*m.b30 + 1008*m.b20*m.b31 + 752*m.b20*m.b32 + 528*m.b20*m.b33 + 320*m.b20*m.b34 + 144*m.b20*
                       m.b35 + 4128*m.b21*m.b22 + 3688*m.b21*m.b23 + 3280*m.b21*m.b24 + 2904*m.b21*m.b25 + 2560*m.b21*
                       m.b26 + 2232*m.b21*m.b27 + 1936*m.b21*m.b28 + 1640*m.b21*m.b29 + 1360*m.b21*m.b30 + 1064*m.b21*
                       m.b31 + 800*m.b21*m.b32 + 552*m.b21*m.b33 + 336*m.b21*m.b34 + 152*m.b21*m.b35 + 3856*m.b22*m.b23
                        + 3424*m.b22*m.b24 + 3024*m.b22*m.b25 + 2640*m.b22*m.b26 + 2304*m.b22*m.b27 + 1984*m.b22*m.b28
                        + 1696*m.b22*m.b29 + 1392*m.b22*m.b30 + 1120*m.b22*m.b31 + 832*m.b22*m.b32 + 576*m.b22*m.b33 + 
                       352*m.b22*m.b34 + 160*m.b22*m.b35 + 3568*m.b23*m.b24 + 3144*m.b23*m.b25 + 2752*m.b23*m.b26 + 2376
                       *m.b23*m.b27 + 2032*m.b23*m.b28 + 1720*m.b23*m.b29 + 1424*m.b23*m.b30 + 1128*m.b23*m.b31 + 864*
                       m.b23*m.b32 + 600*m.b23*m.b33 + 368*m.b23*m.b34 + 168*m.b23*m.b35 + 3264*m.b24*m.b25 + 2848*m.b24
                       *m.b26 + 2464*m.b24*m.b27 + 2096*m.b24*m.b28 + 1760*m.b24*m.b29 + 1440*m.b24*m.b30 + 1136*m.b24*
                       m.b31 + 864*m.b24*m.b32 + 624*m.b24*m.b33 + 384*m.b24*m.b34 + 176*m.b24*m.b35 + 2944*m.b25*m.b26
                        + 2536*m.b25*m.b27 + 2160*m.b25*m.b28 + 1800*m.b25*m.b29 + 1472*m.b25*m.b30 + 1160*m.b25*m.b31
                        + 864*m.b25*m.b32 + 616*m.b25*m.b33 + 400*m.b25*m.b34 + 184*m.b25*m.b35 + 2608*m.b26*m.b27 + 
                       2208*m.b26*m.b28 + 1840*m.b26*m.b29 + 1504*m.b26*m.b30 + 1200*m.b26*m.b31 + 896*m.b26*m.b32 + 624
                       *m.b26*m.b33 + 384*m.b26*m.b34 + 192*m.b26*m.b35 + 2256*m.b27*m.b28 + 1880*m.b27*m.b29 + 1536*
                       m.b27*m.b30 + 1224*m.b27*m.b31 + 928*m.b27*m.b32 + 648*m.b27*m.b33 + 400*m.b27*m.b34 + 184*m.b27*
                       m.b35 + 1920*m.b28*m.b29 + 1568*m.b28*m.b30 + 1248*m.b28*m.b31 + 960*m.b28*m.b32 + 672*m.b28*
                       m.b33 + 416*m.b28*m.b34 + 192*m.b28*m.b35 + 1600*m.b29*m.b30 + 1272*m.b29*m.b31 + 976*m.b29*m.b32
                        + 696*m.b29*m.b33 + 432*m.b29*m.b34 + 200*m.b29*m.b35 + 1296*m.b30*m.b31 + 992*m.b30*m.b32 + 720
                       *m.b30*m.b33 + 448*m.b30*m.b34 + 208*m.b30*m.b35 + 1008*m.b31*m.b32 + 728*m.b31*m.b33 + 464*m.b31
                       *m.b34 + 216*m.b31*m.b35 + 736*m.b32*m.b33 + 480*m.b32*m.b34 + 224*m.b32*m.b35 + 480*m.b33*m.b34
                        + 232*m.b33*m.b35 + 240*m.b34*m.b35 - 544*m.b1 - 1144*m.b2 - 1792*m.b3 - 2480*m.b4 - 3200*m.b5
                        - 3944*m.b6 - 4704*m.b7 - 5472*m.b8 - 6240*m.b9 - 7008*m.b10 - 7776*m.b11 - 8536*m.b12 - 9280*
                       m.b13 - 10000*m.b14 - 10688*m.b15 - 11336*m.b16 - 11936*m.b17 - 12480*m.b18 - 11936*m.b19 - 11336
                       *m.b20 - 10688*m.b21 - 10000*m.b22 - 9280*m.b23 - 8536*m.b24 - 7776*m.b25 - 7008*m.b26 - 6240*
                       m.b27 - 5472*m.b28 - 4704*m.b29 - 3944*m.b30 - 3200*m.b31 - 2480*m.b32 - 1792*m.b33 - 1144*m.b34
                        - 544*m.b35 - m.x36 <= 0)

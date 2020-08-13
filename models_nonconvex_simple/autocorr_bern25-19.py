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
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b2*m.b14*m.b15 + 64*m.b1*m.b2*m.b15*m.b16 + 64*m.b1*m.b2*m.b16*m.b17 + 64*m.b1*m.b2*m.b17*
                       m.b18 + 64*m.b1*m.b2*m.b18*m.b19 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3
                       *m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11 + 64*m.b1
                       *m.b3*m.b10*m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*m.b3*m.b13*
                       m.b15 + 64*m.b1*m.b3*m.b14*m.b16 + 64*m.b1*m.b3*m.b15*m.b17 + 64*m.b1*m.b3*m.b16*m.b18 + 64*m.b1*
                       m.b3*m.b17*m.b19 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64
                       *m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*m.b9*m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*m.b1*m.b4*m.b11*
                       m.b14 + 64*m.b1*m.b4*m.b12*m.b15 + 64*m.b1*m.b4*m.b13*m.b16 + 64*m.b1*m.b4*m.b14*m.b17 + 64*m.b1*
                       m.b4*m.b15*m.b18 + 64*m.b1*m.b4*m.b16*m.b19 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11
                        + 64*m.b1*m.b5*m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*m.b14 + 64*m.b1*m.b5*
                       m.b11*m.b15 + 64*m.b1*m.b5*m.b12*m.b16 + 64*m.b1*m.b5*m.b13*m.b17 + 64*m.b1*m.b5*m.b14*m.b18 + 64
                       *m.b1*m.b5*m.b15*m.b19 + 64*m.b1*m.b6*m.b7*m.b12 + 64*m.b1*m.b6*m.b8*m.b13 + 64*m.b1*m.b6*m.b9*
                       m.b14 + 64*m.b1*m.b6*m.b10*m.b15 + 64*m.b1*m.b6*m.b11*m.b16 + 64*m.b1*m.b6*m.b12*m.b17 + 64*m.b1*
                       m.b6*m.b13*m.b18 + 64*m.b1*m.b6*m.b14*m.b19 + 64*m.b1*m.b7*m.b8*m.b14 + 64*m.b1*m.b7*m.b9*m.b15
                        + 64*m.b1*m.b7*m.b10*m.b16 + 64*m.b1*m.b7*m.b11*m.b17 + 64*m.b1*m.b7*m.b12*m.b18 + 64*m.b1*m.b7*
                       m.b13*m.b19 + 64*m.b1*m.b8*m.b9*m.b16 + 64*m.b1*m.b8*m.b10*m.b17 + 64*m.b1*m.b8*m.b11*m.b18 + 64*
                       m.b1*m.b8*m.b12*m.b19 + 64*m.b1*m.b9*m.b10*m.b18 + 64*m.b1*m.b9*m.b11*m.b19 + 128*m.b2*m.b3*m.b4*
                       m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*
                       m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*m.b10 + 128*m.b2*m.b3*m.b10*m.b11 + 128*m.b2*m.b3*m.b11*m.b12
                        + 128*m.b2*m.b3*m.b12*m.b13 + 128*m.b2*m.b3*m.b13*m.b14 + 128*m.b2*m.b3*m.b14*m.b15 + 128*m.b2*
                       m.b3*m.b15*m.b16 + 128*m.b2*m.b3*m.b16*m.b17 + 128*m.b2*m.b3*m.b17*m.b18 + 128*m.b2*m.b3*m.b18*
                       m.b19 + 64*m.b2*m.b3*m.b19*m.b20 + 128*m.b2*m.b4*m.b5*m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*
                       m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12
                        + 128*m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*m.b12*m.b14 + 128*m.b2*m.b4*m.b13*m.b15 + 128*m.b2*
                       m.b4*m.b14*m.b16 + 128*m.b2*m.b4*m.b15*m.b17 + 128*m.b2*m.b4*m.b16*m.b18 + 128*m.b2*m.b4*m.b17*
                       m.b19 + 64*m.b2*m.b4*m.b18*m.b20 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5*m.b7*m.b10 + 128*m.b2*
                       m.b5*m.b8*m.b11 + 128*m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*m.b13 + 128*m.b2*m.b5*m.b11*
                       m.b14 + 128*m.b2*m.b5*m.b12*m.b15 + 128*m.b2*m.b5*m.b13*m.b16 + 128*m.b2*m.b5*m.b14*m.b17 + 128*
                       m.b2*m.b5*m.b15*m.b18 + 128*m.b2*m.b5*m.b16*m.b19 + 64*m.b2*m.b5*m.b17*m.b20 + 128*m.b2*m.b6*m.b7
                       *m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*m.b13 + 128*m.b2*m.b6*m.b10*m.b14 + 128*
                       m.b2*m.b6*m.b11*m.b15 + 128*m.b2*m.b6*m.b12*m.b16 + 128*m.b2*m.b6*m.b13*m.b17 + 128*m.b2*m.b6*
                       m.b14*m.b18 + 128*m.b2*m.b6*m.b15*m.b19 + 64*m.b2*m.b6*m.b16*m.b20 + 128*m.b2*m.b7*m.b8*m.b13 + 
                       128*m.b2*m.b7*m.b9*m.b14 + 128*m.b2*m.b7*m.b10*m.b15 + 128*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b7*
                       m.b12*m.b17 + 128*m.b2*m.b7*m.b13*m.b18 + 128*m.b2*m.b7*m.b14*m.b19 + 64*m.b2*m.b7*m.b15*m.b20 + 
                       128*m.b2*m.b8*m.b9*m.b15 + 128*m.b2*m.b8*m.b10*m.b16 + 128*m.b2*m.b8*m.b11*m.b17 + 128*m.b2*m.b8*
                       m.b12*m.b18 + 128*m.b2*m.b8*m.b13*m.b19 + 64*m.b2*m.b8*m.b14*m.b20 + 128*m.b2*m.b9*m.b10*m.b17 + 
                       128*m.b2*m.b9*m.b11*m.b18 + 128*m.b2*m.b9*m.b12*m.b19 + 64*m.b2*m.b9*m.b13*m.b20 + 128*m.b2*m.b10
                       *m.b11*m.b19 + 64*m.b2*m.b10*m.b12*m.b20 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*m.b7 + 
                       192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*m.b10 + 192*m.b3*m.b4*
                       m.b10*m.b11 + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b4*m.b12*m.b13 + 192*m.b3*m.b4*m.b13*m.b14
                        + 192*m.b3*m.b4*m.b14*m.b15 + 192*m.b3*m.b4*m.b15*m.b16 + 192*m.b3*m.b4*m.b16*m.b17 + 192*m.b3*
                       m.b4*m.b17*m.b18 + 192*m.b3*m.b4*m.b18*m.b19 + 128*m.b3*m.b4*m.b19*m.b20 + 64*m.b3*m.b4*m.b20*
                       m.b21 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*m.b5*m.b8*m.b10 + 192*m.b3*
                       m.b5*m.b9*m.b11 + 192*m.b3*m.b5*m.b10*m.b12 + 192*m.b3*m.b5*m.b11*m.b13 + 192*m.b3*m.b5*m.b12*
                       m.b14 + 192*m.b3*m.b5*m.b13*m.b15 + 192*m.b3*m.b5*m.b14*m.b16 + 192*m.b3*m.b5*m.b15*m.b17 + 192*
                       m.b3*m.b5*m.b16*m.b18 + 192*m.b3*m.b5*m.b17*m.b19 + 128*m.b3*m.b5*m.b18*m.b20 + 64*m.b3*m.b5*
                       m.b19*m.b21 + 192*m.b3*m.b6*m.b7*m.b10 + 192*m.b3*m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 
                       192*m.b3*m.b6*m.b10*m.b13 + 192*m.b3*m.b6*m.b11*m.b14 + 192*m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b6
                       *m.b13*m.b16 + 192*m.b3*m.b6*m.b14*m.b17 + 192*m.b3*m.b6*m.b15*m.b18 + 192*m.b3*m.b6*m.b16*m.b19
                        + 128*m.b3*m.b6*m.b17*m.b20 + 64*m.b3*m.b6*m.b18*m.b21 + 192*m.b3*m.b7*m.b8*m.b12 + 192*m.b3*
                       m.b7*m.b9*m.b13 + 192*m.b3*m.b7*m.b10*m.b14 + 192*m.b3*m.b7*m.b11*m.b15 + 192*m.b3*m.b7*m.b12*
                       m.b16 + 192*m.b3*m.b7*m.b13*m.b17 + 192*m.b3*m.b7*m.b14*m.b18 + 192*m.b3*m.b7*m.b15*m.b19 + 128*
                       m.b3*m.b7*m.b16*m.b20 + 64*m.b3*m.b7*m.b17*m.b21 + 192*m.b3*m.b8*m.b9*m.b14 + 192*m.b3*m.b8*m.b10
                       *m.b15 + 192*m.b3*m.b8*m.b11*m.b16 + 192*m.b3*m.b8*m.b12*m.b17 + 192*m.b3*m.b8*m.b13*m.b18 + 192*
                       m.b3*m.b8*m.b14*m.b19 + 128*m.b3*m.b8*m.b15*m.b20 + 64*m.b3*m.b8*m.b16*m.b21 + 192*m.b3*m.b9*
                       m.b10*m.b16 + 192*m.b3*m.b9*m.b11*m.b17 + 192*m.b3*m.b9*m.b12*m.b18 + 192*m.b3*m.b9*m.b13*m.b19
                        + 128*m.b3*m.b9*m.b14*m.b20 + 64*m.b3*m.b9*m.b15*m.b21 + 192*m.b3*m.b10*m.b11*m.b18 + 192*m.b3*
                       m.b10*m.b12*m.b19 + 128*m.b3*m.b10*m.b13*m.b20 + 64*m.b3*m.b10*m.b14*m.b21 + 128*m.b3*m.b11*m.b12
                       *m.b20 + 64*m.b3*m.b11*m.b13*m.b21 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*m.b4
                       *m.b5*m.b8*m.b9 + 256*m.b4*m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5*m.b11*
                       m.b12 + 256*m.b4*m.b5*m.b12*m.b13 + 256*m.b4*m.b5*m.b13*m.b14 + 256*m.b4*m.b5*m.b14*m.b15 + 256*
                       m.b4*m.b5*m.b15*m.b16 + 256*m.b4*m.b5*m.b16*m.b17 + 256*m.b4*m.b5*m.b17*m.b18 + 256*m.b4*m.b5*
                       m.b18*m.b19 + 192*m.b4*m.b5*m.b19*m.b20 + 128*m.b4*m.b5*m.b20*m.b21 + 64*m.b4*m.b5*m.b21*m.b22 + 
                       256*m.b4*m.b6*m.b7*m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11 + 256*m.b4*m.b6*
                       m.b10*m.b12 + 256*m.b4*m.b6*m.b11*m.b13 + 256*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*m.b6*m.b13*m.b15
                        + 256*m.b4*m.b6*m.b14*m.b16 + 256*m.b4*m.b6*m.b15*m.b17 + 256*m.b4*m.b6*m.b16*m.b18 + 256*m.b4*
                       m.b6*m.b17*m.b19 + 192*m.b4*m.b6*m.b18*m.b20 + 128*m.b4*m.b6*m.b19*m.b21 + 64*m.b4*m.b6*m.b20*
                       m.b22 + 256*m.b4*m.b7*m.b8*m.b11 + 256*m.b4*m.b7*m.b9*m.b12 + 256*m.b4*m.b7*m.b10*m.b13 + 256*
                       m.b4*m.b7*m.b11*m.b14 + 256*m.b4*m.b7*m.b12*m.b15 + 256*m.b4*m.b7*m.b13*m.b16 + 256*m.b4*m.b7*
                       m.b14*m.b17 + 256*m.b4*m.b7*m.b15*m.b18 + 256*m.b4*m.b7*m.b16*m.b19 + 192*m.b4*m.b7*m.b17*m.b20
                        + 128*m.b4*m.b7*m.b18*m.b21 + 64*m.b4*m.b7*m.b19*m.b22 + 256*m.b4*m.b8*m.b9*m.b13 + 256*m.b4*
                       m.b8*m.b10*m.b14 + 256*m.b4*m.b8*m.b11*m.b15 + 256*m.b4*m.b8*m.b12*m.b16 + 256*m.b4*m.b8*m.b13*
                       m.b17 + 256*m.b4*m.b8*m.b14*m.b18 + 256*m.b4*m.b8*m.b15*m.b19 + 192*m.b4*m.b8*m.b16*m.b20 + 128*
                       m.b4*m.b8*m.b17*m.b21 + 64*m.b4*m.b8*m.b18*m.b22 + 256*m.b4*m.b9*m.b10*m.b15 + 256*m.b4*m.b9*
                       m.b11*m.b16 + 256*m.b4*m.b9*m.b12*m.b17 + 256*m.b4*m.b9*m.b13*m.b18 + 256*m.b4*m.b9*m.b14*m.b19
                        + 192*m.b4*m.b9*m.b15*m.b20 + 128*m.b4*m.b9*m.b16*m.b21 + 64*m.b4*m.b9*m.b17*m.b22 + 256*m.b4*
                       m.b10*m.b11*m.b17 + 256*m.b4*m.b10*m.b12*m.b18 + 256*m.b4*m.b10*m.b13*m.b19 + 192*m.b4*m.b10*
                       m.b14*m.b20 + 128*m.b4*m.b10*m.b15*m.b21 + 64*m.b4*m.b10*m.b16*m.b22 + 256*m.b4*m.b11*m.b12*m.b19
                        + 192*m.b4*m.b11*m.b13*m.b20 + 128*m.b4*m.b11*m.b14*m.b21 + 64*m.b4*m.b11*m.b15*m.b22 + 128*m.b4
                       *m.b12*m.b13*m.b21 + 64*m.b4*m.b12*m.b14*m.b22 + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*
                       m.b9 + 320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*m.b10*m.b11 + 320*m.b5*m.b6*m.b11*m.b12 + 320*
                       m.b5*m.b6*m.b12*m.b13 + 320*m.b5*m.b6*m.b13*m.b14 + 320*m.b5*m.b6*m.b14*m.b15 + 320*m.b5*m.b6*
                       m.b15*m.b16 + 320*m.b5*m.b6*m.b16*m.b17 + 320*m.b5*m.b6*m.b17*m.b18 + 320*m.b5*m.b6*m.b18*m.b19
                        + 256*m.b5*m.b6*m.b19*m.b20 + 192*m.b5*m.b6*m.b20*m.b21 + 128*m.b5*m.b6*m.b21*m.b22 + 64*m.b5*
                       m.b6*m.b22*m.b23 + 320*m.b5*m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*m.b11 + 320*m.b5*m.b7*m.b10*
                       m.b12 + 320*m.b5*m.b7*m.b11*m.b13 + 320*m.b5*m.b7*m.b12*m.b14 + 320*m.b5*m.b7*m.b13*m.b15 + 320*
                       m.b5*m.b7*m.b14*m.b16 + 320*m.b5*m.b7*m.b15*m.b17 + 320*m.b5*m.b7*m.b16*m.b18 + 320*m.b5*m.b7*
                       m.b17*m.b19 + 256*m.b5*m.b7*m.b18*m.b20 + 192*m.b5*m.b7*m.b19*m.b21 + 128*m.b5*m.b7*m.b20*m.b22
                        + 64*m.b5*m.b7*m.b21*m.b23 + 320*m.b5*m.b8*m.b9*m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 320*m.b5*
                       m.b8*m.b11*m.b14 + 320*m.b5*m.b8*m.b12*m.b15 + 320*m.b5*m.b8*m.b13*m.b16 + 320*m.b5*m.b8*m.b14*
                       m.b17 + 320*m.b5*m.b8*m.b15*m.b18 + 320*m.b5*m.b8*m.b16*m.b19 + 256*m.b5*m.b8*m.b17*m.b20 + 192*
                       m.b5*m.b8*m.b18*m.b21 + 128*m.b5*m.b8*m.b19*m.b22 + 64*m.b5*m.b8*m.b20*m.b23 + 320*m.b5*m.b9*
                       m.b10*m.b14 + 320*m.b5*m.b9*m.b11*m.b15 + 320*m.b5*m.b9*m.b12*m.b16 + 320*m.b5*m.b9*m.b13*m.b17
                        + 320*m.b5*m.b9*m.b14*m.b18 + 320*m.b5*m.b9*m.b15*m.b19 + 256*m.b5*m.b9*m.b16*m.b20 + 192*m.b5*
                       m.b9*m.b17*m.b21 + 128*m.b5*m.b9*m.b18*m.b22 + 64*m.b5*m.b9*m.b19*m.b23 + 320*m.b5*m.b10*m.b11*
                       m.b16 + 320*m.b5*m.b10*m.b12*m.b17 + 320*m.b5*m.b10*m.b13*m.b18 + 320*m.b5*m.b10*m.b14*m.b19 + 
                       256*m.b5*m.b10*m.b15*m.b20 + 192*m.b5*m.b10*m.b16*m.b21 + 128*m.b5*m.b10*m.b17*m.b22 + 64*m.b5*
                       m.b10*m.b18*m.b23 + 320*m.b5*m.b11*m.b12*m.b18 + 320*m.b5*m.b11*m.b13*m.b19 + 256*m.b5*m.b11*
                       m.b14*m.b20 + 192*m.b5*m.b11*m.b15*m.b21 + 128*m.b5*m.b11*m.b16*m.b22 + 64*m.b5*m.b11*m.b17*m.b23
                        + 256*m.b5*m.b12*m.b13*m.b20 + 192*m.b5*m.b12*m.b14*m.b21 + 128*m.b5*m.b12*m.b15*m.b22 + 64*m.b5
                       *m.b12*m.b16*m.b23 + 128*m.b5*m.b13*m.b14*m.b22 + 64*m.b5*m.b13*m.b15*m.b23 + 384*m.b6*m.b7*m.b8*
                       m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12 + 384*
                       m.b6*m.b7*m.b12*m.b13 + 384*m.b6*m.b7*m.b13*m.b14 + 384*m.b6*m.b7*m.b14*m.b15 + 384*m.b6*m.b7*
                       m.b15*m.b16 + 384*m.b6*m.b7*m.b16*m.b17 + 384*m.b6*m.b7*m.b17*m.b18 + 384*m.b6*m.b7*m.b18*m.b19
                        + 320*m.b6*m.b7*m.b19*m.b20 + 256*m.b6*m.b7*m.b20*m.b21 + 192*m.b6*m.b7*m.b21*m.b22 + 128*m.b6*
                       m.b7*m.b22*m.b23 + 64*m.b6*m.b7*m.b23*m.b24 + 384*m.b6*m.b8*m.b9*m.b11 + 384*m.b6*m.b8*m.b10*
                       m.b12 + 384*m.b6*m.b8*m.b11*m.b13 + 384*m.b6*m.b8*m.b12*m.b14 + 384*m.b6*m.b8*m.b13*m.b15 + 384*
                       m.b6*m.b8*m.b14*m.b16 + 384*m.b6*m.b8*m.b15*m.b17 + 384*m.b6*m.b8*m.b16*m.b18 + 384*m.b6*m.b8*
                       m.b17*m.b19 + 320*m.b6*m.b8*m.b18*m.b20 + 256*m.b6*m.b8*m.b19*m.b21 + 192*m.b6*m.b8*m.b20*m.b22
                        + 128*m.b6*m.b8*m.b21*m.b23 + 64*m.b6*m.b8*m.b22*m.b24 + 384*m.b6*m.b9*m.b10*m.b13 + 384*m.b6*
                       m.b9*m.b11*m.b14 + 384*m.b6*m.b9*m.b12*m.b15 + 384*m.b6*m.b9*m.b13*m.b16 + 384*m.b6*m.b9*m.b14*
                       m.b17 + 384*m.b6*m.b9*m.b15*m.b18 + 384*m.b6*m.b9*m.b16*m.b19 + 320*m.b6*m.b9*m.b17*m.b20 + 256*
                       m.b6*m.b9*m.b18*m.b21 + 192*m.b6*m.b9*m.b19*m.b22 + 128*m.b6*m.b9*m.b20*m.b23 + 64*m.b6*m.b9*
                       m.b21*m.b24 + 384*m.b6*m.b10*m.b11*m.b15 + 384*m.b6*m.b10*m.b12*m.b16 + 384*m.b6*m.b10*m.b13*
                       m.b17 + 384*m.b6*m.b10*m.b14*m.b18 + 384*m.b6*m.b10*m.b15*m.b19 + 320*m.b6*m.b10*m.b16*m.b20 + 
                       256*m.b6*m.b10*m.b17*m.b21 + 192*m.b6*m.b10*m.b18*m.b22 + 128*m.b6*m.b10*m.b19*m.b23 + 64*m.b6*
                       m.b10*m.b20*m.b24 + 384*m.b6*m.b11*m.b12*m.b17 + 384*m.b6*m.b11*m.b13*m.b18 + 384*m.b6*m.b11*
                       m.b14*m.b19 + 320*m.b6*m.b11*m.b15*m.b20 + 256*m.b6*m.b11*m.b16*m.b21 + 192*m.b6*m.b11*m.b17*
                       m.b22 + 128*m.b6*m.b11*m.b18*m.b23 + 64*m.b6*m.b11*m.b19*m.b24 + 384*m.b6*m.b12*m.b13*m.b19 + 320
                       *m.b6*m.b12*m.b14*m.b20 + 256*m.b6*m.b12*m.b15*m.b21 + 192*m.b6*m.b12*m.b16*m.b22 + 128*m.b6*
                       m.b12*m.b17*m.b23 + 64*m.b6*m.b12*m.b18*m.b24 + 256*m.b6*m.b13*m.b14*m.b21 + 192*m.b6*m.b13*m.b15
                       *m.b22 + 128*m.b6*m.b13*m.b16*m.b23 + 64*m.b6*m.b13*m.b17*m.b24 + 128*m.b6*m.b14*m.b15*m.b23 + 64
                       *m.b6*m.b14*m.b16*m.b24 + 448*m.b7*m.b8*m.b9*m.b10 + 448*m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*
                       m.b11*m.b12 + 448*m.b7*m.b8*m.b12*m.b13 + 448*m.b7*m.b8*m.b13*m.b14 + 448*m.b7*m.b8*m.b14*m.b15
                        + 448*m.b7*m.b8*m.b15*m.b16 + 448*m.b7*m.b8*m.b16*m.b17 + 448*m.b7*m.b8*m.b17*m.b18 + 448*m.b7*
                       m.b8*m.b18*m.b19 + 384*m.b7*m.b8*m.b19*m.b20 + 320*m.b7*m.b8*m.b20*m.b21 + 256*m.b7*m.b8*m.b21*
                       m.b22 + 192*m.b7*m.b8*m.b22*m.b23 + 128*m.b7*m.b8*m.b23*m.b24 + 64*m.b7*m.b8*m.b24*m.b25 + 448*
                       m.b7*m.b9*m.b10*m.b12 + 448*m.b7*m.b9*m.b11*m.b13 + 448*m.b7*m.b9*m.b12*m.b14 + 448*m.b7*m.b9*
                       m.b13*m.b15 + 448*m.b7*m.b9*m.b14*m.b16 + 448*m.b7*m.b9*m.b15*m.b17 + 448*m.b7*m.b9*m.b16*m.b18
                        + 448*m.b7*m.b9*m.b17*m.b19 + 384*m.b7*m.b9*m.b18*m.b20 + 320*m.b7*m.b9*m.b19*m.b21 + 256*m.b7*
                       m.b9*m.b20*m.b22 + 192*m.b7*m.b9*m.b21*m.b23 + 128*m.b7*m.b9*m.b22*m.b24 + 64*m.b7*m.b9*m.b23*
                       m.b25 + 448*m.b7*m.b10*m.b11*m.b14 + 448*m.b7*m.b10*m.b12*m.b15 + 448*m.b7*m.b10*m.b13*m.b16 + 
                       448*m.b7*m.b10*m.b14*m.b17 + 448*m.b7*m.b10*m.b15*m.b18 + 448*m.b7*m.b10*m.b16*m.b19 + 384*m.b7*
                       m.b10*m.b17*m.b20 + 320*m.b7*m.b10*m.b18*m.b21 + 256*m.b7*m.b10*m.b19*m.b22 + 192*m.b7*m.b10*
                       m.b20*m.b23 + 128*m.b7*m.b10*m.b21*m.b24 + 64*m.b7*m.b10*m.b22*m.b25 + 448*m.b7*m.b11*m.b12*m.b16
                        + 448*m.b7*m.b11*m.b13*m.b17 + 448*m.b7*m.b11*m.b14*m.b18 + 448*m.b7*m.b11*m.b15*m.b19 + 384*
                       m.b7*m.b11*m.b16*m.b20 + 320*m.b7*m.b11*m.b17*m.b21 + 256*m.b7*m.b11*m.b18*m.b22 + 192*m.b7*m.b11
                       *m.b19*m.b23 + 128*m.b7*m.b11*m.b20*m.b24 + 64*m.b7*m.b11*m.b21*m.b25 + 448*m.b7*m.b12*m.b13*
                       m.b18 + 448*m.b7*m.b12*m.b14*m.b19 + 384*m.b7*m.b12*m.b15*m.b20 + 320*m.b7*m.b12*m.b16*m.b21 + 
                       256*m.b7*m.b12*m.b17*m.b22 + 192*m.b7*m.b12*m.b18*m.b23 + 128*m.b7*m.b12*m.b19*m.b24 + 64*m.b7*
                       m.b12*m.b20*m.b25 + 384*m.b7*m.b13*m.b14*m.b20 + 320*m.b7*m.b13*m.b15*m.b21 + 256*m.b7*m.b13*
                       m.b16*m.b22 + 192*m.b7*m.b13*m.b17*m.b23 + 128*m.b7*m.b13*m.b18*m.b24 + 64*m.b7*m.b13*m.b19*m.b25
                        + 256*m.b7*m.b14*m.b15*m.b22 + 192*m.b7*m.b14*m.b16*m.b23 + 128*m.b7*m.b14*m.b17*m.b24 + 64*m.b7
                       *m.b14*m.b18*m.b25 + 128*m.b7*m.b15*m.b16*m.b24 + 64*m.b7*m.b15*m.b17*m.b25 + 448*m.b8*m.b9*m.b10
                       *m.b11 + 448*m.b8*m.b9*m.b11*m.b12 + 448*m.b8*m.b9*m.b12*m.b13 + 448*m.b8*m.b9*m.b13*m.b14 + 512*
                       m.b8*m.b9*m.b14*m.b15 + 512*m.b8*m.b9*m.b15*m.b16 + 512*m.b8*m.b9*m.b16*m.b17 + 512*m.b8*m.b9*
                       m.b17*m.b18 + 448*m.b8*m.b9*m.b18*m.b19 + 384*m.b8*m.b9*m.b19*m.b20 + 320*m.b8*m.b9*m.b20*m.b21
                        + 256*m.b8*m.b9*m.b21*m.b22 + 192*m.b8*m.b9*m.b22*m.b23 + 128*m.b8*m.b9*m.b23*m.b24 + 64*m.b8*
                       m.b9*m.b24*m.b25 + 448*m.b8*m.b10*m.b11*m.b13 + 448*m.b8*m.b10*m.b12*m.b14 + 512*m.b8*m.b10*m.b13
                       *m.b15 + 512*m.b8*m.b10*m.b14*m.b16 + 512*m.b8*m.b10*m.b15*m.b17 + 512*m.b8*m.b10*m.b16*m.b18 + 
                       448*m.b8*m.b10*m.b17*m.b19 + 384*m.b8*m.b10*m.b18*m.b20 + 320*m.b8*m.b10*m.b19*m.b21 + 256*m.b8*
                       m.b10*m.b20*m.b22 + 192*m.b8*m.b10*m.b21*m.b23 + 128*m.b8*m.b10*m.b22*m.b24 + 64*m.b8*m.b10*m.b23
                       *m.b25 + 512*m.b8*m.b11*m.b12*m.b15 + 512*m.b8*m.b11*m.b13*m.b16 + 512*m.b8*m.b11*m.b14*m.b17 + 
                       512*m.b8*m.b11*m.b15*m.b18 + 448*m.b8*m.b11*m.b16*m.b19 + 384*m.b8*m.b11*m.b17*m.b20 + 320*m.b8*
                       m.b11*m.b18*m.b21 + 256*m.b8*m.b11*m.b19*m.b22 + 192*m.b8*m.b11*m.b20*m.b23 + 128*m.b8*m.b11*
                       m.b21*m.b24 + 64*m.b8*m.b11*m.b22*m.b25 + 512*m.b8*m.b12*m.b13*m.b17 + 512*m.b8*m.b12*m.b14*m.b18
                        + 448*m.b8*m.b12*m.b15*m.b19 + 384*m.b8*m.b12*m.b16*m.b20 + 320*m.b8*m.b12*m.b17*m.b21 + 256*
                       m.b8*m.b12*m.b18*m.b22 + 192*m.b8*m.b12*m.b19*m.b23 + 128*m.b8*m.b12*m.b20*m.b24 + 64*m.b8*m.b12*
                       m.b21*m.b25 + 448*m.b8*m.b13*m.b14*m.b19 + 384*m.b8*m.b13*m.b15*m.b20 + 320*m.b8*m.b13*m.b16*
                       m.b21 + 256*m.b8*m.b13*m.b17*m.b22 + 192*m.b8*m.b13*m.b18*m.b23 + 128*m.b8*m.b13*m.b19*m.b24 + 64
                       *m.b8*m.b13*m.b20*m.b25 + 320*m.b8*m.b14*m.b15*m.b21 + 256*m.b8*m.b14*m.b16*m.b22 + 192*m.b8*
                       m.b14*m.b17*m.b23 + 128*m.b8*m.b14*m.b18*m.b24 + 64*m.b8*m.b14*m.b19*m.b25 + 192*m.b8*m.b15*m.b16
                       *m.b23 + 128*m.b8*m.b15*m.b17*m.b24 + 64*m.b8*m.b15*m.b18*m.b25 + 64*m.b8*m.b16*m.b17*m.b25 + 448
                       *m.b9*m.b10*m.b11*m.b12 + 448*m.b9*m.b10*m.b12*m.b13 + 448*m.b9*m.b10*m.b13*m.b14 + 448*m.b9*
                       m.b10*m.b14*m.b15 + 576*m.b9*m.b10*m.b15*m.b16 + 576*m.b9*m.b10*m.b16*m.b17 + 512*m.b9*m.b10*
                       m.b17*m.b18 + 448*m.b9*m.b10*m.b18*m.b19 + 384*m.b9*m.b10*m.b19*m.b20 + 320*m.b9*m.b10*m.b20*
                       m.b21 + 256*m.b9*m.b10*m.b21*m.b22 + 192*m.b9*m.b10*m.b22*m.b23 + 128*m.b9*m.b10*m.b23*m.b24 + 64
                       *m.b9*m.b10*m.b24*m.b25 + 448*m.b9*m.b11*m.b12*m.b14 + 448*m.b9*m.b11*m.b13*m.b15 + 576*m.b9*
                       m.b11*m.b14*m.b16 + 576*m.b9*m.b11*m.b15*m.b17 + 512*m.b9*m.b11*m.b16*m.b18 + 448*m.b9*m.b11*
                       m.b17*m.b19 + 384*m.b9*m.b11*m.b18*m.b20 + 320*m.b9*m.b11*m.b19*m.b21 + 256*m.b9*m.b11*m.b20*
                       m.b22 + 192*m.b9*m.b11*m.b21*m.b23 + 128*m.b9*m.b11*m.b22*m.b24 + 64*m.b9*m.b11*m.b23*m.b25 + 576
                       *m.b9*m.b12*m.b13*m.b16 + 576*m.b9*m.b12*m.b14*m.b17 + 512*m.b9*m.b12*m.b15*m.b18 + 448*m.b9*
                       m.b12*m.b16*m.b19 + 384*m.b9*m.b12*m.b17*m.b20 + 320*m.b9*m.b12*m.b18*m.b21 + 256*m.b9*m.b12*
                       m.b19*m.b22 + 192*m.b9*m.b12*m.b20*m.b23 + 128*m.b9*m.b12*m.b21*m.b24 + 64*m.b9*m.b12*m.b22*m.b25
                        + 512*m.b9*m.b13*m.b14*m.b18 + 448*m.b9*m.b13*m.b15*m.b19 + 384*m.b9*m.b13*m.b16*m.b20 + 320*
                       m.b9*m.b13*m.b17*m.b21 + 256*m.b9*m.b13*m.b18*m.b22 + 192*m.b9*m.b13*m.b19*m.b23 + 128*m.b9*m.b13
                       *m.b20*m.b24 + 64*m.b9*m.b13*m.b21*m.b25 + 384*m.b9*m.b14*m.b15*m.b20 + 320*m.b9*m.b14*m.b16*
                       m.b21 + 256*m.b9*m.b14*m.b17*m.b22 + 192*m.b9*m.b14*m.b18*m.b23 + 128*m.b9*m.b14*m.b19*m.b24 + 64
                       *m.b9*m.b14*m.b20*m.b25 + 256*m.b9*m.b15*m.b16*m.b22 + 192*m.b9*m.b15*m.b17*m.b23 + 128*m.b9*
                       m.b15*m.b18*m.b24 + 64*m.b9*m.b15*m.b19*m.b25 + 128*m.b9*m.b16*m.b17*m.b24 + 64*m.b9*m.b16*m.b18*
                       m.b25 + 448*m.b10*m.b11*m.b12*m.b13 + 448*m.b10*m.b11*m.b13*m.b14 + 448*m.b10*m.b11*m.b14*m.b15
                        + 448*m.b10*m.b11*m.b15*m.b16 + 576*m.b10*m.b11*m.b16*m.b17 + 512*m.b10*m.b11*m.b17*m.b18 + 448*
                       m.b10*m.b11*m.b18*m.b19 + 384*m.b10*m.b11*m.b19*m.b20 + 320*m.b10*m.b11*m.b20*m.b21 + 256*m.b10*
                       m.b11*m.b21*m.b22 + 192*m.b10*m.b11*m.b22*m.b23 + 128*m.b10*m.b11*m.b23*m.b24 + 64*m.b10*m.b11*
                       m.b24*m.b25 + 448*m.b10*m.b12*m.b13*m.b15 + 448*m.b10*m.b12*m.b14*m.b16 + 576*m.b10*m.b12*m.b15*
                       m.b17 + 512*m.b10*m.b12*m.b16*m.b18 + 448*m.b10*m.b12*m.b17*m.b19 + 384*m.b10*m.b12*m.b18*m.b20
                        + 320*m.b10*m.b12*m.b19*m.b21 + 256*m.b10*m.b12*m.b20*m.b22 + 192*m.b10*m.b12*m.b21*m.b23 + 128*
                       m.b10*m.b12*m.b22*m.b24 + 64*m.b10*m.b12*m.b23*m.b25 + 576*m.b10*m.b13*m.b14*m.b17 + 512*m.b10*
                       m.b13*m.b15*m.b18 + 448*m.b10*m.b13*m.b16*m.b19 + 384*m.b10*m.b13*m.b17*m.b20 + 320*m.b10*m.b13*
                       m.b18*m.b21 + 256*m.b10*m.b13*m.b19*m.b22 + 192*m.b10*m.b13*m.b20*m.b23 + 128*m.b10*m.b13*m.b21*
                       m.b24 + 64*m.b10*m.b13*m.b22*m.b25 + 448*m.b10*m.b14*m.b15*m.b19 + 384*m.b10*m.b14*m.b16*m.b20 + 
                       320*m.b10*m.b14*m.b17*m.b21 + 256*m.b10*m.b14*m.b18*m.b22 + 192*m.b10*m.b14*m.b19*m.b23 + 128*
                       m.b10*m.b14*m.b20*m.b24 + 64*m.b10*m.b14*m.b21*m.b25 + 320*m.b10*m.b15*m.b16*m.b21 + 256*m.b10*
                       m.b15*m.b17*m.b22 + 192*m.b10*m.b15*m.b18*m.b23 + 128*m.b10*m.b15*m.b19*m.b24 + 64*m.b10*m.b15*
                       m.b20*m.b25 + 192*m.b10*m.b16*m.b17*m.b23 + 128*m.b10*m.b16*m.b18*m.b24 + 64*m.b10*m.b16*m.b19*
                       m.b25 + 64*m.b10*m.b17*m.b18*m.b25 + 448*m.b11*m.b12*m.b13*m.b14 + 448*m.b11*m.b12*m.b14*m.b15 + 
                       448*m.b11*m.b12*m.b15*m.b16 + 448*m.b11*m.b12*m.b16*m.b17 + 512*m.b11*m.b12*m.b17*m.b18 + 448*
                       m.b11*m.b12*m.b18*m.b19 + 384*m.b11*m.b12*m.b19*m.b20 + 320*m.b11*m.b12*m.b20*m.b21 + 256*m.b11*
                       m.b12*m.b21*m.b22 + 192*m.b11*m.b12*m.b22*m.b23 + 128*m.b11*m.b12*m.b23*m.b24 + 64*m.b11*m.b12*
                       m.b24*m.b25 + 448*m.b11*m.b13*m.b14*m.b16 + 448*m.b11*m.b13*m.b15*m.b17 + 512*m.b11*m.b13*m.b16*
                       m.b18 + 448*m.b11*m.b13*m.b17*m.b19 + 384*m.b11*m.b13*m.b18*m.b20 + 320*m.b11*m.b13*m.b19*m.b21
                        + 256*m.b11*m.b13*m.b20*m.b22 + 192*m.b11*m.b13*m.b21*m.b23 + 128*m.b11*m.b13*m.b22*m.b24 + 64*
                       m.b11*m.b13*m.b23*m.b25 + 512*m.b11*m.b14*m.b15*m.b18 + 448*m.b11*m.b14*m.b16*m.b19 + 384*m.b11*
                       m.b14*m.b17*m.b20 + 320*m.b11*m.b14*m.b18*m.b21 + 256*m.b11*m.b14*m.b19*m.b22 + 192*m.b11*m.b14*
                       m.b20*m.b23 + 128*m.b11*m.b14*m.b21*m.b24 + 64*m.b11*m.b14*m.b22*m.b25 + 384*m.b11*m.b15*m.b16*
                       m.b20 + 320*m.b11*m.b15*m.b17*m.b21 + 256*m.b11*m.b15*m.b18*m.b22 + 192*m.b11*m.b15*m.b19*m.b23
                        + 128*m.b11*m.b15*m.b20*m.b24 + 64*m.b11*m.b15*m.b21*m.b25 + 256*m.b11*m.b16*m.b17*m.b22 + 192*
                       m.b11*m.b16*m.b18*m.b23 + 128*m.b11*m.b16*m.b19*m.b24 + 64*m.b11*m.b16*m.b20*m.b25 + 128*m.b11*
                       m.b17*m.b18*m.b24 + 64*m.b11*m.b17*m.b19*m.b25 + 448*m.b12*m.b13*m.b14*m.b15 + 448*m.b12*m.b13*
                       m.b15*m.b16 + 448*m.b12*m.b13*m.b16*m.b17 + 448*m.b12*m.b13*m.b17*m.b18 + 448*m.b12*m.b13*m.b18*
                       m.b19 + 384*m.b12*m.b13*m.b19*m.b20 + 320*m.b12*m.b13*m.b20*m.b21 + 256*m.b12*m.b13*m.b21*m.b22
                        + 192*m.b12*m.b13*m.b22*m.b23 + 128*m.b12*m.b13*m.b23*m.b24 + 64*m.b12*m.b13*m.b24*m.b25 + 448*
                       m.b12*m.b14*m.b15*m.b17 + 448*m.b12*m.b14*m.b16*m.b18 + 448*m.b12*m.b14*m.b17*m.b19 + 384*m.b12*
                       m.b14*m.b18*m.b20 + 320*m.b12*m.b14*m.b19*m.b21 + 256*m.b12*m.b14*m.b20*m.b22 + 192*m.b12*m.b14*
                       m.b21*m.b23 + 128*m.b12*m.b14*m.b22*m.b24 + 64*m.b12*m.b14*m.b23*m.b25 + 448*m.b12*m.b15*m.b16*
                       m.b19 + 384*m.b12*m.b15*m.b17*m.b20 + 320*m.b12*m.b15*m.b18*m.b21 + 256*m.b12*m.b15*m.b19*m.b22
                        + 192*m.b12*m.b15*m.b20*m.b23 + 128*m.b12*m.b15*m.b21*m.b24 + 64*m.b12*m.b15*m.b22*m.b25 + 320*
                       m.b12*m.b16*m.b17*m.b21 + 256*m.b12*m.b16*m.b18*m.b22 + 192*m.b12*m.b16*m.b19*m.b23 + 128*m.b12*
                       m.b16*m.b20*m.b24 + 64*m.b12*m.b16*m.b21*m.b25 + 192*m.b12*m.b17*m.b18*m.b23 + 128*m.b12*m.b17*
                       m.b19*m.b24 + 64*m.b12*m.b17*m.b20*m.b25 + 64*m.b12*m.b18*m.b19*m.b25 + 448*m.b13*m.b14*m.b15*
                       m.b16 + 448*m.b13*m.b14*m.b16*m.b17 + 448*m.b13*m.b14*m.b17*m.b18 + 448*m.b13*m.b14*m.b18*m.b19
                        + 384*m.b13*m.b14*m.b19*m.b20 + 320*m.b13*m.b14*m.b20*m.b21 + 256*m.b13*m.b14*m.b21*m.b22 + 192*
                       m.b13*m.b14*m.b22*m.b23 + 128*m.b13*m.b14*m.b23*m.b24 + 64*m.b13*m.b14*m.b24*m.b25 + 448*m.b13*
                       m.b15*m.b16*m.b18 + 448*m.b13*m.b15*m.b17*m.b19 + 384*m.b13*m.b15*m.b18*m.b20 + 320*m.b13*m.b15*
                       m.b19*m.b21 + 256*m.b13*m.b15*m.b20*m.b22 + 192*m.b13*m.b15*m.b21*m.b23 + 128*m.b13*m.b15*m.b22*
                       m.b24 + 64*m.b13*m.b15*m.b23*m.b25 + 384*m.b13*m.b16*m.b17*m.b20 + 320*m.b13*m.b16*m.b18*m.b21 + 
                       256*m.b13*m.b16*m.b19*m.b22 + 192*m.b13*m.b16*m.b20*m.b23 + 128*m.b13*m.b16*m.b21*m.b24 + 64*
                       m.b13*m.b16*m.b22*m.b25 + 256*m.b13*m.b17*m.b18*m.b22 + 192*m.b13*m.b17*m.b19*m.b23 + 128*m.b13*
                       m.b17*m.b20*m.b24 + 64*m.b13*m.b17*m.b21*m.b25 + 128*m.b13*m.b18*m.b19*m.b24 + 64*m.b13*m.b18*
                       m.b20*m.b25 + 448*m.b14*m.b15*m.b16*m.b17 + 448*m.b14*m.b15*m.b17*m.b18 + 448*m.b14*m.b15*m.b18*
                       m.b19 + 384*m.b14*m.b15*m.b19*m.b20 + 320*m.b14*m.b15*m.b20*m.b21 + 256*m.b14*m.b15*m.b21*m.b22
                        + 192*m.b14*m.b15*m.b22*m.b23 + 128*m.b14*m.b15*m.b23*m.b24 + 64*m.b14*m.b15*m.b24*m.b25 + 448*
                       m.b14*m.b16*m.b17*m.b19 + 384*m.b14*m.b16*m.b18*m.b20 + 320*m.b14*m.b16*m.b19*m.b21 + 256*m.b14*
                       m.b16*m.b20*m.b22 + 192*m.b14*m.b16*m.b21*m.b23 + 128*m.b14*m.b16*m.b22*m.b24 + 64*m.b14*m.b16*
                       m.b23*m.b25 + 320*m.b14*m.b17*m.b18*m.b21 + 256*m.b14*m.b17*m.b19*m.b22 + 192*m.b14*m.b17*m.b20*
                       m.b23 + 128*m.b14*m.b17*m.b21*m.b24 + 64*m.b14*m.b17*m.b22*m.b25 + 192*m.b14*m.b18*m.b19*m.b23 + 
                       128*m.b14*m.b18*m.b20*m.b24 + 64*m.b14*m.b18*m.b21*m.b25 + 64*m.b14*m.b19*m.b20*m.b25 + 448*m.b15
                       *m.b16*m.b17*m.b18 + 448*m.b15*m.b16*m.b18*m.b19 + 384*m.b15*m.b16*m.b19*m.b20 + 320*m.b15*m.b16*
                       m.b20*m.b21 + 256*m.b15*m.b16*m.b21*m.b22 + 192*m.b15*m.b16*m.b22*m.b23 + 128*m.b15*m.b16*m.b23*
                       m.b24 + 64*m.b15*m.b16*m.b24*m.b25 + 384*m.b15*m.b17*m.b18*m.b20 + 320*m.b15*m.b17*m.b19*m.b21 + 
                       256*m.b15*m.b17*m.b20*m.b22 + 192*m.b15*m.b17*m.b21*m.b23 + 128*m.b15*m.b17*m.b22*m.b24 + 64*
                       m.b15*m.b17*m.b23*m.b25 + 256*m.b15*m.b18*m.b19*m.b22 + 192*m.b15*m.b18*m.b20*m.b23 + 128*m.b15*
                       m.b18*m.b21*m.b24 + 64*m.b15*m.b18*m.b22*m.b25 + 128*m.b15*m.b19*m.b20*m.b24 + 64*m.b15*m.b19*
                       m.b21*m.b25 + 448*m.b16*m.b17*m.b18*m.b19 + 384*m.b16*m.b17*m.b19*m.b20 + 320*m.b16*m.b17*m.b20*
                       m.b21 + 256*m.b16*m.b17*m.b21*m.b22 + 192*m.b16*m.b17*m.b22*m.b23 + 128*m.b16*m.b17*m.b23*m.b24
                        + 64*m.b16*m.b17*m.b24*m.b25 + 320*m.b16*m.b18*m.b19*m.b21 + 256*m.b16*m.b18*m.b20*m.b22 + 192*
                       m.b16*m.b18*m.b21*m.b23 + 128*m.b16*m.b18*m.b22*m.b24 + 64*m.b16*m.b18*m.b23*m.b25 + 192*m.b16*
                       m.b19*m.b20*m.b23 + 128*m.b16*m.b19*m.b21*m.b24 + 64*m.b16*m.b19*m.b22*m.b25 + 64*m.b16*m.b20*
                       m.b21*m.b25 + 384*m.b17*m.b18*m.b19*m.b20 + 320*m.b17*m.b18*m.b20*m.b21 + 256*m.b17*m.b18*m.b21*
                       m.b22 + 192*m.b17*m.b18*m.b22*m.b23 + 128*m.b17*m.b18*m.b23*m.b24 + 64*m.b17*m.b18*m.b24*m.b25 + 
                       256*m.b17*m.b19*m.b20*m.b22 + 192*m.b17*m.b19*m.b21*m.b23 + 128*m.b17*m.b19*m.b22*m.b24 + 64*
                       m.b17*m.b19*m.b23*m.b25 + 128*m.b17*m.b20*m.b21*m.b24 + 64*m.b17*m.b20*m.b22*m.b25 + 320*m.b18*
                       m.b19*m.b20*m.b21 + 256*m.b18*m.b19*m.b21*m.b22 + 192*m.b18*m.b19*m.b22*m.b23 + 128*m.b18*m.b19*
                       m.b23*m.b24 + 64*m.b18*m.b19*m.b24*m.b25 + 192*m.b18*m.b20*m.b21*m.b23 + 128*m.b18*m.b20*m.b22*
                       m.b24 + 64*m.b18*m.b20*m.b23*m.b25 + 64*m.b18*m.b21*m.b22*m.b25 + 256*m.b19*m.b20*m.b21*m.b22 + 
                       192*m.b19*m.b20*m.b22*m.b23 + 128*m.b19*m.b20*m.b23*m.b24 + 64*m.b19*m.b20*m.b24*m.b25 + 128*
                       m.b19*m.b21*m.b22*m.b24 + 64*m.b19*m.b21*m.b23*m.b25 + 192*m.b20*m.b21*m.b22*m.b23 + 128*m.b20*
                       m.b21*m.b23*m.b24 + 64*m.b20*m.b21*m.b24*m.b25 + 64*m.b20*m.b22*m.b23*m.b25 + 128*m.b21*m.b22*
                       m.b23*m.b24 + 64*m.b21*m.b22*m.b24*m.b25 + 64*m.b22*m.b23*m.b24*m.b25 - 32*m.b1*m.b2*m.b3 - 64*
                       m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 
                       64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1*m.b2*
                       m.b13 - 64*m.b1*m.b2*m.b14 - 64*m.b1*m.b2*m.b15 - 64*m.b1*m.b2*m.b16 - 64*m.b1*m.b2*m.b17 - 64*
                       m.b1*m.b2*m.b18 - 32*m.b1*m.b2*m.b19 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6
                        - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*
                       m.b11 - 64*m.b1*m.b3*m.b12 - 64*m.b1*m.b3*m.b13 - 64*m.b1*m.b3*m.b14 - 64*m.b1*m.b3*m.b15 - 64*
                       m.b1*m.b3*m.b16 - 64*m.b1*m.b3*m.b17 - 32*m.b1*m.b3*m.b18 - 32*m.b1*m.b3*m.b19 - 64*m.b1*m.b4*
                       m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*
                       m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64*m.b1*m.b4*m.b12 - 64*m.b1*m.b4*m.b13 - 64*m.b1*m.b4*m.b14 - 
                       64*m.b1*m.b4*m.b15 - 64*m.b1*m.b4*m.b16 - 32*m.b1*m.b4*m.b17 - 32*m.b1*m.b4*m.b18 - 32*m.b1*m.b4*
                       m.b19 - 64*m.b1*m.b5*m.b6 - 64*m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*
                       m.b5*m.b10 - 64*m.b1*m.b5*m.b11 - 64*m.b1*m.b5*m.b12 - 64*m.b1*m.b5*m.b13 - 64*m.b1*m.b5*m.b14 - 
                       64*m.b1*m.b5*m.b15 - 32*m.b1*m.b5*m.b16 - 32*m.b1*m.b5*m.b17 - 32*m.b1*m.b5*m.b18 - 32*m.b1*m.b5*
                       m.b19 - 64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10 - 32*m.b1*
                       m.b6*m.b11 - 64*m.b1*m.b6*m.b12 - 64*m.b1*m.b6*m.b13 - 64*m.b1*m.b6*m.b14 - 32*m.b1*m.b6*m.b15 - 
                       32*m.b1*m.b6*m.b16 - 32*m.b1*m.b6*m.b17 - 32*m.b1*m.b6*m.b18 - 32*m.b1*m.b6*m.b19 - 64*m.b1*m.b7*
                       m.b8 - 64*m.b1*m.b7*m.b9 - 64*m.b1*m.b7*m.b10 - 64*m.b1*m.b7*m.b11 - 64*m.b1*m.b7*m.b12 - 32*m.b1
                       *m.b7*m.b13 - 32*m.b1*m.b7*m.b14 - 32*m.b1*m.b7*m.b15 - 32*m.b1*m.b7*m.b16 - 32*m.b1*m.b7*m.b17
                        - 32*m.b1*m.b7*m.b18 - 32*m.b1*m.b7*m.b19 - 64*m.b1*m.b8*m.b9 - 64*m.b1*m.b8*m.b10 - 64*m.b1*
                       m.b8*m.b11 - 64*m.b1*m.b8*m.b12 - 32*m.b1*m.b8*m.b13 - 32*m.b1*m.b8*m.b14 - 32*m.b1*m.b8*m.b16 - 
                       32*m.b1*m.b8*m.b17 - 32*m.b1*m.b8*m.b18 - 32*m.b1*m.b8*m.b19 - 64*m.b1*m.b9*m.b10 - 64*m.b1*m.b9*
                       m.b11 - 32*m.b1*m.b9*m.b12 - 32*m.b1*m.b9*m.b13 - 32*m.b1*m.b9*m.b14 - 32*m.b1*m.b9*m.b15 - 32*
                       m.b1*m.b9*m.b16 - 32*m.b1*m.b9*m.b18 - 32*m.b1*m.b9*m.b19 - 32*m.b1*m.b10*m.b11 - 32*m.b1*m.b10*
                       m.b12 - 32*m.b1*m.b10*m.b13 - 32*m.b1*m.b10*m.b14 - 32*m.b1*m.b10*m.b15 - 32*m.b1*m.b10*m.b16 - 
                       32*m.b1*m.b10*m.b17 - 32*m.b1*m.b10*m.b18 - 32*m.b1*m.b11*m.b12 - 32*m.b1*m.b11*m.b13 - 32*m.b1*
                       m.b11*m.b14 - 32*m.b1*m.b11*m.b15 - 32*m.b1*m.b11*m.b16 - 32*m.b1*m.b11*m.b17 - 32*m.b1*m.b11*
                       m.b18 - 32*m.b1*m.b11*m.b19 - 32*m.b1*m.b12*m.b13 - 32*m.b1*m.b12*m.b14 - 32*m.b1*m.b12*m.b15 - 
                       32*m.b1*m.b12*m.b16 - 32*m.b1*m.b12*m.b17 - 32*m.b1*m.b12*m.b18 - 32*m.b1*m.b12*m.b19 - 32*m.b1*
                       m.b13*m.b14 - 32*m.b1*m.b13*m.b15 - 32*m.b1*m.b13*m.b16 - 32*m.b1*m.b13*m.b17 - 32*m.b1*m.b13*
                       m.b18 - 32*m.b1*m.b13*m.b19 - 32*m.b1*m.b14*m.b15 - 32*m.b1*m.b14*m.b16 - 32*m.b1*m.b14*m.b17 - 
                       32*m.b1*m.b14*m.b18 - 32*m.b1*m.b14*m.b19 - 32*m.b1*m.b15*m.b16 - 32*m.b1*m.b15*m.b17 - 32*m.b1*
                       m.b15*m.b18 - 32*m.b1*m.b15*m.b19 - 32*m.b1*m.b16*m.b17 - 32*m.b1*m.b16*m.b18 - 32*m.b1*m.b16*
                       m.b19 - 32*m.b1*m.b17*m.b18 - 32*m.b1*m.b17*m.b19 - 32*m.b1*m.b18*m.b19 - 96*m.b2*m.b3*m.b4 - 128
                       *m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*m.b3*
                       m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*m.b11 - 128*m.b2*m.b3*m.b12 - 128*m.b2*m.b3*m.b13 - 
                       128*m.b2*m.b3*m.b14 - 128*m.b2*m.b3*m.b15 - 128*m.b2*m.b3*m.b16 - 128*m.b2*m.b3*m.b17 - 128*m.b2*
                       m.b3*m.b18 - 96*m.b2*m.b3*m.b19 - 32*m.b2*m.b3*m.b20 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 
                       128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 128*m.b2*m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*
                       m.b4*m.b11 - 128*m.b2*m.b4*m.b12 - 128*m.b2*m.b4*m.b13 - 128*m.b2*m.b4*m.b14 - 128*m.b2*m.b4*
                       m.b15 - 128*m.b2*m.b4*m.b16 - 128*m.b2*m.b4*m.b17 - 96*m.b2*m.b4*m.b18 - 64*m.b2*m.b4*m.b19 - 32*
                       m.b2*m.b4*m.b20 - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*m.b8 - 128*m.b2*m.b5*
                       m.b9 - 128*m.b2*m.b5*m.b10 - 128*m.b2*m.b5*m.b11 - 128*m.b2*m.b5*m.b12 - 128*m.b2*m.b5*m.b13 - 
                       128*m.b2*m.b5*m.b14 - 128*m.b2*m.b5*m.b15 - 128*m.b2*m.b5*m.b16 - 96*m.b2*m.b5*m.b17 - 64*m.b2*
                       m.b5*m.b18 - 64*m.b2*m.b5*m.b19 - 32*m.b2*m.b5*m.b20 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*m.b8 - 
                       128*m.b2*m.b6*m.b9 - 64*m.b2*m.b6*m.b10 - 128*m.b2*m.b6*m.b11 - 128*m.b2*m.b6*m.b12 - 128*m.b2*
                       m.b6*m.b13 - 128*m.b2*m.b6*m.b14 - 128*m.b2*m.b6*m.b15 - 96*m.b2*m.b6*m.b16 - 64*m.b2*m.b6*m.b17
                        - 64*m.b2*m.b6*m.b18 - 64*m.b2*m.b6*m.b19 - 32*m.b2*m.b6*m.b20 - 160*m.b2*m.b7*m.b8 - 128*m.b2*
                       m.b7*m.b9 - 128*m.b2*m.b7*m.b10 - 128*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b12 - 128*m.b2*m.b7*m.b13
                        - 128*m.b2*m.b7*m.b14 - 96*m.b2*m.b7*m.b15 - 64*m.b2*m.b7*m.b16 - 64*m.b2*m.b7*m.b17 - 64*m.b2*
                       m.b7*m.b18 - 64*m.b2*m.b7*m.b19 - 32*m.b2*m.b7*m.b20 - 160*m.b2*m.b8*m.b9 - 128*m.b2*m.b8*m.b10
                        - 128*m.b2*m.b8*m.b11 - 128*m.b2*m.b8*m.b12 - 128*m.b2*m.b8*m.b13 - 32*m.b2*m.b8*m.b14 - 64*m.b2
                       *m.b8*m.b15 - 64*m.b2*m.b8*m.b16 - 64*m.b2*m.b8*m.b17 - 64*m.b2*m.b8*m.b18 - 64*m.b2*m.b8*m.b19
                        - 32*m.b2*m.b8*m.b20 - 160*m.b2*m.b9*m.b10 - 128*m.b2*m.b9*m.b11 - 128*m.b2*m.b9*m.b12 - 96*m.b2
                       *m.b9*m.b13 - 64*m.b2*m.b9*m.b14 - 64*m.b2*m.b9*m.b15 - 64*m.b2*m.b9*m.b17 - 64*m.b2*m.b9*m.b18
                        - 64*m.b2*m.b9*m.b19 - 32*m.b2*m.b9*m.b20 - 160*m.b2*m.b10*m.b11 - 96*m.b2*m.b10*m.b12 - 64*m.b2
                       *m.b10*m.b13 - 64*m.b2*m.b10*m.b14 - 64*m.b2*m.b10*m.b15 - 64*m.b2*m.b10*m.b16 - 64*m.b2*m.b10*
                       m.b17 - 64*m.b2*m.b10*m.b19 - 32*m.b2*m.b10*m.b20 - 96*m.b2*m.b11*m.b12 - 64*m.b2*m.b11*m.b13 - 
                       64*m.b2*m.b11*m.b14 - 64*m.b2*m.b11*m.b15 - 64*m.b2*m.b11*m.b16 - 64*m.b2*m.b11*m.b17 - 64*m.b2*
                       m.b11*m.b18 - 64*m.b2*m.b11*m.b19 - 96*m.b2*m.b12*m.b13 - 64*m.b2*m.b12*m.b14 - 64*m.b2*m.b12*
                       m.b15 - 64*m.b2*m.b12*m.b16 - 64*m.b2*m.b12*m.b17 - 64*m.b2*m.b12*m.b18 - 64*m.b2*m.b12*m.b19 - 
                       32*m.b2*m.b12*m.b20 - 96*m.b2*m.b13*m.b14 - 64*m.b2*m.b13*m.b15 - 64*m.b2*m.b13*m.b16 - 64*m.b2*
                       m.b13*m.b17 - 64*m.b2*m.b13*m.b18 - 64*m.b2*m.b13*m.b19 - 32*m.b2*m.b13*m.b20 - 96*m.b2*m.b14*
                       m.b15 - 64*m.b2*m.b14*m.b16 - 64*m.b2*m.b14*m.b17 - 64*m.b2*m.b14*m.b18 - 64*m.b2*m.b14*m.b19 - 
                       32*m.b2*m.b14*m.b20 - 96*m.b2*m.b15*m.b16 - 64*m.b2*m.b15*m.b17 - 64*m.b2*m.b15*m.b18 - 64*m.b2*
                       m.b15*m.b19 - 32*m.b2*m.b15*m.b20 - 96*m.b2*m.b16*m.b17 - 64*m.b2*m.b16*m.b18 - 64*m.b2*m.b16*
                       m.b19 - 32*m.b2*m.b16*m.b20 - 96*m.b2*m.b17*m.b18 - 64*m.b2*m.b17*m.b19 - 32*m.b2*m.b17*m.b20 - 
                       96*m.b2*m.b18*m.b19 - 32*m.b2*m.b18*m.b20 - 32*m.b2*m.b19*m.b20 - 160*m.b3*m.b4*m.b5 - 224*m.b3*
                       m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4*m.b9 - 192*m.b3*m.b4*m.b10 - 
                       192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*m.b12 - 192*m.b3*m.b4*m.b13 - 192*m.b3*m.b4*m.b14 - 192*m.b3*
                       m.b4*m.b15 - 192*m.b3*m.b4*m.b16 - 192*m.b3*m.b4*m.b17 - 192*m.b3*m.b4*m.b18 - 160*m.b3*m.b4*
                       m.b19 - 96*m.b3*m.b4*m.b20 - 32*m.b3*m.b4*m.b21 - 256*m.b3*m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*
                       m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*m.b10 - 192*m.b3*m.b5*m.b11 - 192*m.b3*m.b5*
                       m.b12 - 192*m.b3*m.b5*m.b13 - 192*m.b3*m.b5*m.b14 - 192*m.b3*m.b5*m.b15 - 192*m.b3*m.b5*m.b16 - 
                       192*m.b3*m.b5*m.b17 - 160*m.b3*m.b5*m.b18 - 128*m.b3*m.b5*m.b19 - 64*m.b3*m.b5*m.b20 - 32*m.b3*
                       m.b5*m.b21 - 256*m.b3*m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*m.b9 - 192*m.b3*m.b6*m.b10 - 
                       192*m.b3*m.b6*m.b11 - 192*m.b3*m.b6*m.b12 - 192*m.b3*m.b6*m.b13 - 192*m.b3*m.b6*m.b14 - 192*m.b3*
                       m.b6*m.b15 - 192*m.b3*m.b6*m.b16 - 160*m.b3*m.b6*m.b17 - 128*m.b3*m.b6*m.b18 - 96*m.b3*m.b6*m.b19
                        - 64*m.b3*m.b6*m.b20 - 32*m.b3*m.b6*m.b21 - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 192*m.b3*
                       m.b7*m.b10 - 96*m.b3*m.b7*m.b11 - 192*m.b3*m.b7*m.b12 - 192*m.b3*m.b7*m.b13 - 192*m.b3*m.b7*m.b14
                        - 192*m.b3*m.b7*m.b15 - 160*m.b3*m.b7*m.b16 - 128*m.b3*m.b7*m.b17 - 96*m.b3*m.b7*m.b18 - 96*m.b3
                       *m.b7*m.b19 - 64*m.b3*m.b7*m.b20 - 32*m.b3*m.b7*m.b21 - 256*m.b3*m.b8*m.b9 - 224*m.b3*m.b8*m.b10
                        - 192*m.b3*m.b8*m.b11 - 192*m.b3*m.b8*m.b12 - 96*m.b3*m.b8*m.b13 - 192*m.b3*m.b8*m.b14 - 160*
                       m.b3*m.b8*m.b15 - 128*m.b3*m.b8*m.b16 - 96*m.b3*m.b8*m.b17 - 96*m.b3*m.b8*m.b18 - 96*m.b3*m.b8*
                       m.b19 - 64*m.b3*m.b8*m.b20 - 32*m.b3*m.b8*m.b21 - 256*m.b3*m.b9*m.b10 - 224*m.b3*m.b9*m.b11 - 192
                       *m.b3*m.b9*m.b12 - 192*m.b3*m.b9*m.b13 - 160*m.b3*m.b9*m.b14 - 32*m.b3*m.b9*m.b15 - 96*m.b3*m.b9*
                       m.b16 - 96*m.b3*m.b9*m.b17 - 96*m.b3*m.b9*m.b18 - 96*m.b3*m.b9*m.b19 - 64*m.b3*m.b9*m.b20 - 32*
                       m.b3*m.b9*m.b21 - 256*m.b3*m.b10*m.b11 - 224*m.b3*m.b10*m.b12 - 160*m.b3*m.b10*m.b13 - 128*m.b3*
                       m.b10*m.b14 - 96*m.b3*m.b10*m.b15 - 96*m.b3*m.b10*m.b16 - 96*m.b3*m.b10*m.b18 - 96*m.b3*m.b10*
                       m.b19 - 64*m.b3*m.b10*m.b20 - 32*m.b3*m.b10*m.b21 - 224*m.b3*m.b11*m.b12 - 160*m.b3*m.b11*m.b13
                        - 96*m.b3*m.b11*m.b14 - 96*m.b3*m.b11*m.b15 - 96*m.b3*m.b11*m.b16 - 96*m.b3*m.b11*m.b17 - 96*
                       m.b3*m.b11*m.b18 - 64*m.b3*m.b11*m.b20 - 32*m.b3*m.b11*m.b21 - 160*m.b3*m.b12*m.b13 - 128*m.b3*
                       m.b12*m.b14 - 96*m.b3*m.b12*m.b15 - 96*m.b3*m.b12*m.b16 - 96*m.b3*m.b12*m.b17 - 96*m.b3*m.b12*
                       m.b18 - 96*m.b3*m.b12*m.b19 - 64*m.b3*m.b12*m.b20 - 160*m.b3*m.b13*m.b14 - 128*m.b3*m.b13*m.b15
                        - 96*m.b3*m.b13*m.b16 - 96*m.b3*m.b13*m.b17 - 96*m.b3*m.b13*m.b18 - 96*m.b3*m.b13*m.b19 - 64*
                       m.b3*m.b13*m.b20 - 32*m.b3*m.b13*m.b21 - 160*m.b3*m.b14*m.b15 - 128*m.b3*m.b14*m.b16 - 96*m.b3*
                       m.b14*m.b17 - 96*m.b3*m.b14*m.b18 - 96*m.b3*m.b14*m.b19 - 64*m.b3*m.b14*m.b20 - 32*m.b3*m.b14*
                       m.b21 - 160*m.b3*m.b15*m.b16 - 128*m.b3*m.b15*m.b17 - 96*m.b3*m.b15*m.b18 - 96*m.b3*m.b15*m.b19
                        - 64*m.b3*m.b15*m.b20 - 32*m.b3*m.b15*m.b21 - 160*m.b3*m.b16*m.b17 - 128*m.b3*m.b16*m.b18 - 96*
                       m.b3*m.b16*m.b19 - 64*m.b3*m.b16*m.b20 - 32*m.b3*m.b16*m.b21 - 160*m.b3*m.b17*m.b18 - 128*m.b3*
                       m.b17*m.b19 - 64*m.b3*m.b17*m.b20 - 32*m.b3*m.b17*m.b21 - 160*m.b3*m.b18*m.b19 - 64*m.b3*m.b18*
                       m.b20 - 32*m.b3*m.b18*m.b21 - 96*m.b3*m.b19*m.b20 - 32*m.b3*m.b19*m.b21 - 32*m.b3*m.b20*m.b21 - 
                       224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5
                       *m.b10 - 256*m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 256*m.b4*m.b5*m.b13 - 256*m.b4*m.b5*m.b14 - 
                       256*m.b4*m.b5*m.b15 - 256*m.b4*m.b5*m.b16 - 256*m.b4*m.b5*m.b17 - 256*m.b4*m.b5*m.b18 - 224*m.b4*
                       m.b5*m.b19 - 160*m.b4*m.b5*m.b20 - 96*m.b4*m.b5*m.b21 - 32*m.b4*m.b5*m.b22 - 352*m.b4*m.b6*m.b7
                        - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10 - 256*m.b4*m.b6*m.b11 - 256*m.b4
                       *m.b6*m.b12 - 256*m.b4*m.b6*m.b13 - 256*m.b4*m.b6*m.b14 - 256*m.b4*m.b6*m.b15 - 256*m.b4*m.b6*
                       m.b16 - 256*m.b4*m.b6*m.b17 - 224*m.b4*m.b6*m.b18 - 192*m.b4*m.b6*m.b19 - 128*m.b4*m.b6*m.b20 - 
                       64*m.b4*m.b6*m.b21 - 32*m.b4*m.b6*m.b22 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*m.b4*m.b7
                       *m.b10 - 256*m.b4*m.b7*m.b11 - 256*m.b4*m.b7*m.b12 - 256*m.b4*m.b7*m.b13 - 256*m.b4*m.b7*m.b14 - 
                       256*m.b4*m.b7*m.b15 - 256*m.b4*m.b7*m.b16 - 224*m.b4*m.b7*m.b17 - 192*m.b4*m.b7*m.b18 - 160*m.b4*
                       m.b7*m.b19 - 96*m.b4*m.b7*m.b20 - 64*m.b4*m.b7*m.b21 - 32*m.b4*m.b7*m.b22 - 352*m.b4*m.b8*m.b9 - 
                       320*m.b4*m.b8*m.b10 - 288*m.b4*m.b8*m.b11 - 128*m.b4*m.b8*m.b12 - 256*m.b4*m.b8*m.b13 - 256*m.b4*
                       m.b8*m.b14 - 256*m.b4*m.b8*m.b15 - 224*m.b4*m.b8*m.b16 - 192*m.b4*m.b8*m.b17 - 160*m.b4*m.b8*
                       m.b18 - 128*m.b4*m.b8*m.b19 - 96*m.b4*m.b8*m.b20 - 64*m.b4*m.b8*m.b21 - 32*m.b4*m.b8*m.b22 - 352*
                       m.b4*m.b9*m.b10 - 320*m.b4*m.b9*m.b11 - 288*m.b4*m.b9*m.b12 - 256*m.b4*m.b9*m.b13 - 128*m.b4*m.b9
                       *m.b14 - 224*m.b4*m.b9*m.b15 - 192*m.b4*m.b9*m.b16 - 160*m.b4*m.b9*m.b17 - 128*m.b4*m.b9*m.b18 - 
                       128*m.b4*m.b9*m.b19 - 96*m.b4*m.b9*m.b20 - 64*m.b4*m.b9*m.b21 - 32*m.b4*m.b9*m.b22 - 352*m.b4*
                       m.b10*m.b11 - 320*m.b4*m.b10*m.b12 - 288*m.b4*m.b10*m.b13 - 224*m.b4*m.b10*m.b14 - 192*m.b4*m.b10
                       *m.b15 - 32*m.b4*m.b10*m.b16 - 128*m.b4*m.b10*m.b17 - 128*m.b4*m.b10*m.b18 - 128*m.b4*m.b10*m.b19
                        - 96*m.b4*m.b10*m.b20 - 64*m.b4*m.b10*m.b21 - 32*m.b4*m.b10*m.b22 - 352*m.b4*m.b11*m.b12 - 288*
                       m.b4*m.b11*m.b13 - 224*m.b4*m.b11*m.b14 - 160*m.b4*m.b11*m.b15 - 128*m.b4*m.b11*m.b16 - 128*m.b4*
                       m.b11*m.b17 - 128*m.b4*m.b11*m.b19 - 96*m.b4*m.b11*m.b20 - 64*m.b4*m.b11*m.b21 - 32*m.b4*m.b11*
                       m.b22 - 288*m.b4*m.b12*m.b13 - 224*m.b4*m.b12*m.b14 - 160*m.b4*m.b12*m.b15 - 128*m.b4*m.b12*m.b16
                        - 128*m.b4*m.b12*m.b17 - 128*m.b4*m.b12*m.b18 - 128*m.b4*m.b12*m.b19 - 64*m.b4*m.b12*m.b21 - 32*
                       m.b4*m.b12*m.b22 - 224*m.b4*m.b13*m.b14 - 192*m.b4*m.b13*m.b15 - 160*m.b4*m.b13*m.b16 - 128*m.b4*
                       m.b13*m.b17 - 128*m.b4*m.b13*m.b18 - 128*m.b4*m.b13*m.b19 - 96*m.b4*m.b13*m.b20 - 64*m.b4*m.b13*
                       m.b21 - 224*m.b4*m.b14*m.b15 - 192*m.b4*m.b14*m.b16 - 160*m.b4*m.b14*m.b17 - 128*m.b4*m.b14*m.b18
                        - 128*m.b4*m.b14*m.b19 - 96*m.b4*m.b14*m.b20 - 64*m.b4*m.b14*m.b21 - 32*m.b4*m.b14*m.b22 - 224*
                       m.b4*m.b15*m.b16 - 192*m.b4*m.b15*m.b17 - 160*m.b4*m.b15*m.b18 - 128*m.b4*m.b15*m.b19 - 96*m.b4*
                       m.b15*m.b20 - 64*m.b4*m.b15*m.b21 - 32*m.b4*m.b15*m.b22 - 224*m.b4*m.b16*m.b17 - 192*m.b4*m.b16*
                       m.b18 - 160*m.b4*m.b16*m.b19 - 96*m.b4*m.b16*m.b20 - 64*m.b4*m.b16*m.b21 - 32*m.b4*m.b16*m.b22 - 
                       224*m.b4*m.b17*m.b18 - 192*m.b4*m.b17*m.b19 - 96*m.b4*m.b17*m.b20 - 64*m.b4*m.b17*m.b21 - 32*m.b4
                       *m.b17*m.b22 - 224*m.b4*m.b18*m.b19 - 128*m.b4*m.b18*m.b20 - 64*m.b4*m.b18*m.b21 - 32*m.b4*m.b18*
                       m.b22 - 160*m.b4*m.b19*m.b20 - 64*m.b4*m.b19*m.b21 - 32*m.b4*m.b19*m.b22 - 96*m.b4*m.b20*m.b21 - 
                       32*m.b4*m.b20*m.b22 - 32*m.b4*m.b21*m.b22 - 288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*
                       m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*m.b5*m.b6*m.b11 - 320*m.b5*m.b6*m.b12 - 320*m.b5*m.b6*m.b13
                        - 320*m.b5*m.b6*m.b14 - 320*m.b5*m.b6*m.b15 - 320*m.b5*m.b6*m.b16 - 320*m.b5*m.b6*m.b17 - 320*
                       m.b5*m.b6*m.b18 - 288*m.b5*m.b6*m.b19 - 224*m.b5*m.b6*m.b20 - 160*m.b5*m.b6*m.b21 - 96*m.b5*m.b6*
                       m.b22 - 32*m.b5*m.b6*m.b23 - 448*m.b5*m.b7*m.b8 - 256*m.b5*m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*
                       m.b5*m.b7*m.b11 - 320*m.b5*m.b7*m.b12 - 320*m.b5*m.b7*m.b13 - 320*m.b5*m.b7*m.b14 - 320*m.b5*m.b7
                       *m.b15 - 320*m.b5*m.b7*m.b16 - 320*m.b5*m.b7*m.b17 - 288*m.b5*m.b7*m.b18 - 256*m.b5*m.b7*m.b19 - 
                       192*m.b5*m.b7*m.b20 - 128*m.b5*m.b7*m.b21 - 64*m.b5*m.b7*m.b22 - 32*m.b5*m.b7*m.b23 - 448*m.b5*
                       m.b8*m.b9 - 416*m.b5*m.b8*m.b10 - 224*m.b5*m.b8*m.b11 - 352*m.b5*m.b8*m.b12 - 320*m.b5*m.b8*m.b13
                        - 320*m.b5*m.b8*m.b14 - 320*m.b5*m.b8*m.b15 - 320*m.b5*m.b8*m.b16 - 288*m.b5*m.b8*m.b17 - 256*
                       m.b5*m.b8*m.b18 - 224*m.b5*m.b8*m.b19 - 160*m.b5*m.b8*m.b20 - 96*m.b5*m.b8*m.b21 - 64*m.b5*m.b8*
                       m.b22 - 32*m.b5*m.b8*m.b23 - 448*m.b5*m.b9*m.b10 - 416*m.b5*m.b9*m.b11 - 384*m.b5*m.b9*m.b12 - 
                       192*m.b5*m.b9*m.b13 - 320*m.b5*m.b9*m.b14 - 320*m.b5*m.b9*m.b15 - 288*m.b5*m.b9*m.b16 - 256*m.b5*
                       m.b9*m.b17 - 224*m.b5*m.b9*m.b18 - 192*m.b5*m.b9*m.b19 - 128*m.b5*m.b9*m.b20 - 96*m.b5*m.b9*m.b21
                        - 64*m.b5*m.b9*m.b22 - 32*m.b5*m.b9*m.b23 - 448*m.b5*m.b10*m.b11 - 416*m.b5*m.b10*m.b12 - 384*
                       m.b5*m.b10*m.b13 - 352*m.b5*m.b10*m.b14 - 128*m.b5*m.b10*m.b15 - 256*m.b5*m.b10*m.b16 - 224*m.b5*
                       m.b10*m.b17 - 192*m.b5*m.b10*m.b18 - 160*m.b5*m.b10*m.b19 - 128*m.b5*m.b10*m.b20 - 96*m.b5*m.b10*
                       m.b21 - 64*m.b5*m.b10*m.b22 - 32*m.b5*m.b10*m.b23 - 448*m.b5*m.b11*m.b12 - 416*m.b5*m.b11*m.b13
                        - 352*m.b5*m.b11*m.b14 - 288*m.b5*m.b11*m.b15 - 224*m.b5*m.b11*m.b16 - 32*m.b5*m.b11*m.b17 - 160
                       *m.b5*m.b11*m.b18 - 160*m.b5*m.b11*m.b19 - 128*m.b5*m.b11*m.b20 - 96*m.b5*m.b11*m.b21 - 64*m.b5*
                       m.b11*m.b22 - 32*m.b5*m.b11*m.b23 - 416*m.b5*m.b12*m.b13 - 352*m.b5*m.b12*m.b14 - 288*m.b5*m.b12*
                       m.b15 - 224*m.b5*m.b12*m.b16 - 160*m.b5*m.b12*m.b17 - 160*m.b5*m.b12*m.b18 - 128*m.b5*m.b12*m.b20
                        - 96*m.b5*m.b12*m.b21 - 64*m.b5*m.b12*m.b22 - 32*m.b5*m.b12*m.b23 - 352*m.b5*m.b13*m.b14 - 288*
                       m.b5*m.b13*m.b15 - 224*m.b5*m.b13*m.b16 - 192*m.b5*m.b13*m.b17 - 160*m.b5*m.b13*m.b18 - 160*m.b5*
                       m.b13*m.b19 - 128*m.b5*m.b13*m.b20 - 64*m.b5*m.b13*m.b22 - 32*m.b5*m.b13*m.b23 - 288*m.b5*m.b14*
                       m.b15 - 256*m.b5*m.b14*m.b16 - 224*m.b5*m.b14*m.b17 - 192*m.b5*m.b14*m.b18 - 160*m.b5*m.b14*m.b19
                        - 128*m.b5*m.b14*m.b20 - 96*m.b5*m.b14*m.b21 - 64*m.b5*m.b14*m.b22 - 288*m.b5*m.b15*m.b16 - 256*
                       m.b5*m.b15*m.b17 - 224*m.b5*m.b15*m.b18 - 192*m.b5*m.b15*m.b19 - 128*m.b5*m.b15*m.b20 - 96*m.b5*
                       m.b15*m.b21 - 64*m.b5*m.b15*m.b22 - 32*m.b5*m.b15*m.b23 - 288*m.b5*m.b16*m.b17 - 256*m.b5*m.b16*
                       m.b18 - 224*m.b5*m.b16*m.b19 - 128*m.b5*m.b16*m.b20 - 96*m.b5*m.b16*m.b21 - 64*m.b5*m.b16*m.b22
                        - 32*m.b5*m.b16*m.b23 - 288*m.b5*m.b17*m.b18 - 256*m.b5*m.b17*m.b19 - 160*m.b5*m.b17*m.b20 - 96*
                       m.b5*m.b17*m.b21 - 64*m.b5*m.b17*m.b22 - 32*m.b5*m.b17*m.b23 - 288*m.b5*m.b18*m.b19 - 192*m.b5*
                       m.b18*m.b20 - 96*m.b5*m.b18*m.b21 - 64*m.b5*m.b18*m.b22 - 32*m.b5*m.b18*m.b23 - 224*m.b5*m.b19*
                       m.b20 - 128*m.b5*m.b19*m.b21 - 64*m.b5*m.b19*m.b22 - 32*m.b5*m.b19*m.b23 - 160*m.b5*m.b20*m.b21
                        - 64*m.b5*m.b20*m.b22 - 32*m.b5*m.b20*m.b23 - 96*m.b5*m.b21*m.b22 - 32*m.b5*m.b21*m.b23 - 32*
                       m.b5*m.b22*m.b23 - 352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*m.b7*
                       m.b11 - 416*m.b6*m.b7*m.b12 - 384*m.b6*m.b7*m.b13 - 384*m.b6*m.b7*m.b14 - 384*m.b6*m.b7*m.b15 - 
                       384*m.b6*m.b7*m.b16 - 384*m.b6*m.b7*m.b17 - 384*m.b6*m.b7*m.b18 - 352*m.b6*m.b7*m.b19 - 288*m.b6*
                       m.b7*m.b20 - 224*m.b6*m.b7*m.b21 - 160*m.b6*m.b7*m.b22 - 96*m.b6*m.b7*m.b23 - 32*m.b6*m.b7*m.b24
                        - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10 - 480*m.b6*m.b8*m.b11 - 448*m.b6*m.b8*m.b12 - 416*
                       m.b6*m.b8*m.b13 - 384*m.b6*m.b8*m.b14 - 384*m.b6*m.b8*m.b15 - 384*m.b6*m.b8*m.b16 - 384*m.b6*m.b8
                       *m.b17 - 352*m.b6*m.b8*m.b18 - 320*m.b6*m.b8*m.b19 - 256*m.b6*m.b8*m.b20 - 192*m.b6*m.b8*m.b21 - 
                       128*m.b6*m.b8*m.b22 - 64*m.b6*m.b8*m.b23 - 32*m.b6*m.b8*m.b24 - 544*m.b6*m.b9*m.b10 - 512*m.b6*
                       m.b9*m.b11 - 288*m.b6*m.b9*m.b12 - 448*m.b6*m.b9*m.b13 - 416*m.b6*m.b9*m.b14 - 384*m.b6*m.b9*
                       m.b15 - 384*m.b6*m.b9*m.b16 - 352*m.b6*m.b9*m.b17 - 320*m.b6*m.b9*m.b18 - 288*m.b6*m.b9*m.b19 - 
                       224*m.b6*m.b9*m.b20 - 160*m.b6*m.b9*m.b21 - 96*m.b6*m.b9*m.b22 - 64*m.b6*m.b9*m.b23 - 32*m.b6*
                       m.b9*m.b24 - 544*m.b6*m.b10*m.b11 - 512*m.b6*m.b10*m.b12 - 480*m.b6*m.b10*m.b13 - 256*m.b6*m.b10*
                       m.b14 - 416*m.b6*m.b10*m.b15 - 352*m.b6*m.b10*m.b16 - 320*m.b6*m.b10*m.b17 - 288*m.b6*m.b10*m.b18
                        - 256*m.b6*m.b10*m.b19 - 192*m.b6*m.b10*m.b20 - 128*m.b6*m.b10*m.b21 - 96*m.b6*m.b10*m.b22 - 64*
                       m.b6*m.b10*m.b23 - 32*m.b6*m.b10*m.b24 - 544*m.b6*m.b11*m.b12 - 512*m.b6*m.b11*m.b13 - 480*m.b6*
                       m.b11*m.b14 - 416*m.b6*m.b11*m.b15 - 160*m.b6*m.b11*m.b16 - 288*m.b6*m.b11*m.b17 - 256*m.b6*m.b11
                       *m.b18 - 224*m.b6*m.b11*m.b19 - 160*m.b6*m.b11*m.b20 - 128*m.b6*m.b11*m.b21 - 96*m.b6*m.b11*m.b22
                        - 64*m.b6*m.b11*m.b23 - 32*m.b6*m.b11*m.b24 - 544*m.b6*m.b12*m.b13 - 480*m.b6*m.b12*m.b14 - 416*
                       m.b6*m.b12*m.b15 - 352*m.b6*m.b12*m.b16 - 288*m.b6*m.b12*m.b17 - 32*m.b6*m.b12*m.b18 - 192*m.b6*
                       m.b12*m.b19 - 160*m.b6*m.b12*m.b20 - 128*m.b6*m.b12*m.b21 - 96*m.b6*m.b12*m.b22 - 64*m.b6*m.b12*
                       m.b23 - 32*m.b6*m.b12*m.b24 - 480*m.b6*m.b13*m.b14 - 416*m.b6*m.b13*m.b15 - 352*m.b6*m.b13*m.b16
                        - 288*m.b6*m.b13*m.b17 - 224*m.b6*m.b13*m.b18 - 192*m.b6*m.b13*m.b19 - 128*m.b6*m.b13*m.b21 - 96
                       *m.b6*m.b13*m.b22 - 64*m.b6*m.b13*m.b23 - 32*m.b6*m.b13*m.b24 - 416*m.b6*m.b14*m.b15 - 352*m.b6*
                       m.b14*m.b16 - 288*m.b6*m.b14*m.b17 - 256*m.b6*m.b14*m.b18 - 224*m.b6*m.b14*m.b19 - 160*m.b6*m.b14
                       *m.b20 - 128*m.b6*m.b14*m.b21 - 64*m.b6*m.b14*m.b23 - 32*m.b6*m.b14*m.b24 - 352*m.b6*m.b15*m.b16
                        - 320*m.b6*m.b15*m.b17 - 288*m.b6*m.b15*m.b18 - 256*m.b6*m.b15*m.b19 - 160*m.b6*m.b15*m.b20 - 
                       128*m.b6*m.b15*m.b21 - 96*m.b6*m.b15*m.b22 - 64*m.b6*m.b15*m.b23 - 352*m.b6*m.b16*m.b17 - 320*
                       m.b6*m.b16*m.b18 - 288*m.b6*m.b16*m.b19 - 192*m.b6*m.b16*m.b20 - 128*m.b6*m.b16*m.b21 - 96*m.b6*
                       m.b16*m.b22 - 64*m.b6*m.b16*m.b23 - 32*m.b6*m.b16*m.b24 - 352*m.b6*m.b17*m.b18 - 320*m.b6*m.b17*
                       m.b19 - 224*m.b6*m.b17*m.b20 - 128*m.b6*m.b17*m.b21 - 96*m.b6*m.b17*m.b22 - 64*m.b6*m.b17*m.b23
                        - 32*m.b6*m.b17*m.b24 - 352*m.b6*m.b18*m.b19 - 256*m.b6*m.b18*m.b20 - 160*m.b6*m.b18*m.b21 - 96*
                       m.b6*m.b18*m.b22 - 64*m.b6*m.b18*m.b23 - 32*m.b6*m.b18*m.b24 - 288*m.b6*m.b19*m.b20 - 192*m.b6*
                       m.b19*m.b21 - 96*m.b6*m.b19*m.b22 - 64*m.b6*m.b19*m.b23 - 32*m.b6*m.b19*m.b24 - 224*m.b6*m.b20*
                       m.b21 - 128*m.b6*m.b20*m.b22 - 64*m.b6*m.b20*m.b23 - 32*m.b6*m.b20*m.b24 - 160*m.b6*m.b21*m.b22
                        - 64*m.b6*m.b21*m.b23 - 32*m.b6*m.b21*m.b24 - 96*m.b6*m.b22*m.b23 - 32*m.b6*m.b22*m.b24 - 32*
                       m.b6*m.b23*m.b24 - 416*m.b7*m.b8*m.b9 - 608*m.b7*m.b8*m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*m.b8
                       *m.b12 - 512*m.b7*m.b8*m.b13 - 480*m.b7*m.b8*m.b14 - 448*m.b7*m.b8*m.b15 - 448*m.b7*m.b8*m.b16 - 
                       448*m.b7*m.b8*m.b17 - 448*m.b7*m.b8*m.b18 - 416*m.b7*m.b8*m.b19 - 352*m.b7*m.b8*m.b20 - 288*m.b7*
                       m.b8*m.b21 - 224*m.b7*m.b8*m.b22 - 160*m.b7*m.b8*m.b23 - 96*m.b7*m.b8*m.b24 - 32*m.b7*m.b8*m.b25
                        - 640*m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 576*m.b7*m.b9*m.b12 - 544*m.b7*m.b9*m.b13 - 512*
                       m.b7*m.b9*m.b14 - 480*m.b7*m.b9*m.b15 - 448*m.b7*m.b9*m.b16 - 448*m.b7*m.b9*m.b17 - 416*m.b7*m.b9
                       *m.b18 - 384*m.b7*m.b9*m.b19 - 320*m.b7*m.b9*m.b20 - 256*m.b7*m.b9*m.b21 - 192*m.b7*m.b9*m.b22 - 
                       128*m.b7*m.b9*m.b23 - 64*m.b7*m.b9*m.b24 - 32*m.b7*m.b9*m.b25 - 640*m.b7*m.b10*m.b11 - 608*m.b7*
                       m.b10*m.b12 - 352*m.b7*m.b10*m.b13 - 544*m.b7*m.b10*m.b14 - 512*m.b7*m.b10*m.b15 - 480*m.b7*m.b10
                       *m.b16 - 416*m.b7*m.b10*m.b17 - 384*m.b7*m.b10*m.b18 - 352*m.b7*m.b10*m.b19 - 288*m.b7*m.b10*
                       m.b20 - 224*m.b7*m.b10*m.b21 - 160*m.b7*m.b10*m.b22 - 96*m.b7*m.b10*m.b23 - 64*m.b7*m.b10*m.b24
                        - 32*m.b7*m.b10*m.b25 - 640*m.b7*m.b11*m.b12 - 608*m.b7*m.b11*m.b13 - 576*m.b7*m.b11*m.b14 - 320
                       *m.b7*m.b11*m.b15 - 480*m.b7*m.b11*m.b16 - 416*m.b7*m.b11*m.b17 - 352*m.b7*m.b11*m.b18 - 320*m.b7
                       *m.b11*m.b19 - 256*m.b7*m.b11*m.b20 - 192*m.b7*m.b11*m.b21 - 128*m.b7*m.b11*m.b22 - 96*m.b7*m.b11
                       *m.b23 - 64*m.b7*m.b11*m.b24 - 32*m.b7*m.b11*m.b25 - 640*m.b7*m.b12*m.b13 - 608*m.b7*m.b12*m.b14
                        - 544*m.b7*m.b12*m.b15 - 480*m.b7*m.b12*m.b16 - 192*m.b7*m.b12*m.b17 - 352*m.b7*m.b12*m.b18 - 
                       288*m.b7*m.b12*m.b19 - 224*m.b7*m.b12*m.b20 - 160*m.b7*m.b12*m.b21 - 128*m.b7*m.b12*m.b22 - 96*
                       m.b7*m.b12*m.b23 - 64*m.b7*m.b12*m.b24 - 32*m.b7*m.b12*m.b25 - 608*m.b7*m.b13*m.b14 - 544*m.b7*
                       m.b13*m.b15 - 480*m.b7*m.b13*m.b16 - 416*m.b7*m.b13*m.b17 - 352*m.b7*m.b13*m.b18 - 64*m.b7*m.b13*
                       m.b19 - 192*m.b7*m.b13*m.b20 - 160*m.b7*m.b13*m.b21 - 128*m.b7*m.b13*m.b22 - 96*m.b7*m.b13*m.b23
                        - 64*m.b7*m.b13*m.b24 - 32*m.b7*m.b13*m.b25 - 544*m.b7*m.b14*m.b15 - 480*m.b7*m.b14*m.b16 - 416*
                       m.b7*m.b14*m.b17 - 352*m.b7*m.b14*m.b18 - 288*m.b7*m.b14*m.b19 - 192*m.b7*m.b14*m.b20 - 128*m.b7*
                       m.b14*m.b22 - 96*m.b7*m.b14*m.b23 - 64*m.b7*m.b14*m.b24 - 32*m.b7*m.b14*m.b25 - 480*m.b7*m.b15*
                       m.b16 - 416*m.b7*m.b15*m.b17 - 352*m.b7*m.b15*m.b18 - 320*m.b7*m.b15*m.b19 - 224*m.b7*m.b15*m.b20
                        - 160*m.b7*m.b15*m.b21 - 128*m.b7*m.b15*m.b22 - 64*m.b7*m.b15*m.b24 - 32*m.b7*m.b15*m.b25 - 416*
                       m.b7*m.b16*m.b17 - 384*m.b7*m.b16*m.b18 - 352*m.b7*m.b16*m.b19 - 256*m.b7*m.b16*m.b20 - 160*m.b7*
                       m.b16*m.b21 - 128*m.b7*m.b16*m.b22 - 96*m.b7*m.b16*m.b23 - 64*m.b7*m.b16*m.b24 - 416*m.b7*m.b17*
                       m.b18 - 384*m.b7*m.b17*m.b19 - 288*m.b7*m.b17*m.b20 - 192*m.b7*m.b17*m.b21 - 128*m.b7*m.b17*m.b22
                        - 96*m.b7*m.b17*m.b23 - 64*m.b7*m.b17*m.b24 - 32*m.b7*m.b17*m.b25 - 416*m.b7*m.b18*m.b19 - 320*
                       m.b7*m.b18*m.b20 - 224*m.b7*m.b18*m.b21 - 128*m.b7*m.b18*m.b22 - 96*m.b7*m.b18*m.b23 - 64*m.b7*
                       m.b18*m.b24 - 32*m.b7*m.b18*m.b25 - 352*m.b7*m.b19*m.b20 - 256*m.b7*m.b19*m.b21 - 160*m.b7*m.b19*
                       m.b22 - 96*m.b7*m.b19*m.b23 - 64*m.b7*m.b19*m.b24 - 32*m.b7*m.b19*m.b25 - 288*m.b7*m.b20*m.b21 - 
                       192*m.b7*m.b20*m.b22 - 96*m.b7*m.b20*m.b23 - 64*m.b7*m.b20*m.b24 - 32*m.b7*m.b20*m.b25 - 224*m.b7
                       *m.b21*m.b22 - 128*m.b7*m.b21*m.b23 - 64*m.b7*m.b21*m.b24 - 32*m.b7*m.b21*m.b25 - 160*m.b7*m.b22*
                       m.b23 - 64*m.b7*m.b22*m.b24 - 32*m.b7*m.b22*m.b25 - 96*m.b7*m.b23*m.b24 - 32*m.b7*m.b23*m.b25 - 
                       32*m.b7*m.b24*m.b25 - 448*m.b8*m.b9*m.b10 - 640*m.b8*m.b9*m.b11 - 608*m.b8*m.b9*m.b12 - 576*m.b8*
                       m.b9*m.b13 - 576*m.b8*m.b9*m.b14 - 576*m.b8*m.b9*m.b15 - 544*m.b8*m.b9*m.b16 - 512*m.b8*m.b9*
                       m.b17 - 480*m.b8*m.b9*m.b18 - 416*m.b8*m.b9*m.b19 - 352*m.b8*m.b9*m.b20 - 288*m.b8*m.b9*m.b21 - 
                       224*m.b8*m.b9*m.b22 - 160*m.b8*m.b9*m.b23 - 96*m.b8*m.b9*m.b24 - 32*m.b8*m.b9*m.b25 - 672*m.b8*
                       m.b10*m.b11 - 416*m.b8*m.b10*m.b12 - 640*m.b8*m.b10*m.b13 - 608*m.b8*m.b10*m.b14 - 608*m.b8*m.b10
                       *m.b15 - 576*m.b8*m.b10*m.b16 - 512*m.b8*m.b10*m.b17 - 448*m.b8*m.b10*m.b18 - 384*m.b8*m.b10*
                       m.b19 - 320*m.b8*m.b10*m.b20 - 256*m.b8*m.b10*m.b21 - 192*m.b8*m.b10*m.b22 - 128*m.b8*m.b10*m.b23
                        - 64*m.b8*m.b10*m.b24 - 32*m.b8*m.b10*m.b25 - 704*m.b8*m.b11*m.b12 - 672*m.b8*m.b11*m.b13 - 416*
                       m.b8*m.b11*m.b14 - 640*m.b8*m.b11*m.b15 - 576*m.b8*m.b11*m.b16 - 512*m.b8*m.b11*m.b17 - 448*m.b8*
                       m.b11*m.b18 - 352*m.b8*m.b11*m.b19 - 288*m.b8*m.b11*m.b20 - 224*m.b8*m.b11*m.b21 - 160*m.b8*m.b11
                       *m.b22 - 96*m.b8*m.b11*m.b23 - 64*m.b8*m.b11*m.b24 - 32*m.b8*m.b11*m.b25 - 704*m.b8*m.b12*m.b13
                        - 672*m.b8*m.b12*m.b14 - 640*m.b8*m.b12*m.b15 - 320*m.b8*m.b12*m.b16 - 512*m.b8*m.b12*m.b17 - 
                       448*m.b8*m.b12*m.b18 - 352*m.b8*m.b12*m.b19 - 256*m.b8*m.b12*m.b20 - 192*m.b8*m.b12*m.b21 - 128*
                       m.b8*m.b12*m.b22 - 96*m.b8*m.b12*m.b23 - 64*m.b8*m.b12*m.b24 - 32*m.b8*m.b12*m.b25 - 672*m.b8*
                       m.b13*m.b14 - 640*m.b8*m.b13*m.b15 - 576*m.b8*m.b13*m.b16 - 512*m.b8*m.b13*m.b17 - 192*m.b8*m.b13
                       *m.b18 - 352*m.b8*m.b13*m.b19 - 224*m.b8*m.b13*m.b20 - 160*m.b8*m.b13*m.b21 - 128*m.b8*m.b13*
                       m.b22 - 96*m.b8*m.b13*m.b23 - 64*m.b8*m.b13*m.b24 - 32*m.b8*m.b13*m.b25 - 640*m.b8*m.b14*m.b15 - 
                       576*m.b8*m.b14*m.b16 - 512*m.b8*m.b14*m.b17 - 448*m.b8*m.b14*m.b18 - 352*m.b8*m.b14*m.b19 - 32*
                       m.b8*m.b14*m.b20 - 160*m.b8*m.b14*m.b21 - 128*m.b8*m.b14*m.b22 - 96*m.b8*m.b14*m.b23 - 64*m.b8*
                       m.b14*m.b24 - 32*m.b8*m.b14*m.b25 - 576*m.b8*m.b15*m.b16 - 512*m.b8*m.b15*m.b17 - 448*m.b8*m.b15*
                       m.b18 - 352*m.b8*m.b15*m.b19 - 256*m.b8*m.b15*m.b20 - 160*m.b8*m.b15*m.b21 - 96*m.b8*m.b15*m.b23
                        - 64*m.b8*m.b15*m.b24 - 32*m.b8*m.b15*m.b25 - 512*m.b8*m.b16*m.b17 - 448*m.b8*m.b16*m.b18 - 384*
                       m.b8*m.b16*m.b19 - 288*m.b8*m.b16*m.b20 - 192*m.b8*m.b16*m.b21 - 128*m.b8*m.b16*m.b22 - 96*m.b8*
                       m.b16*m.b23 - 32*m.b8*m.b16*m.b25 - 480*m.b8*m.b17*m.b18 - 416*m.b8*m.b17*m.b19 - 320*m.b8*m.b17*
                       m.b20 - 224*m.b8*m.b17*m.b21 - 128*m.b8*m.b17*m.b22 - 96*m.b8*m.b17*m.b23 - 64*m.b8*m.b17*m.b24
                        - 32*m.b8*m.b17*m.b25 - 448*m.b8*m.b18*m.b19 - 352*m.b8*m.b18*m.b20 - 256*m.b8*m.b18*m.b21 - 160
                       *m.b8*m.b18*m.b22 - 96*m.b8*m.b18*m.b23 - 64*m.b8*m.b18*m.b24 - 32*m.b8*m.b18*m.b25 - 384*m.b8*
                       m.b19*m.b20 - 288*m.b8*m.b19*m.b21 - 192*m.b8*m.b19*m.b22 - 96*m.b8*m.b19*m.b23 - 64*m.b8*m.b19*
                       m.b24 - 32*m.b8*m.b19*m.b25 - 320*m.b8*m.b20*m.b21 - 224*m.b8*m.b20*m.b22 - 128*m.b8*m.b20*m.b23
                        - 64*m.b8*m.b20*m.b24 - 32*m.b8*m.b20*m.b25 - 256*m.b8*m.b21*m.b22 - 160*m.b8*m.b21*m.b23 - 64*
                       m.b8*m.b21*m.b24 - 32*m.b8*m.b21*m.b25 - 192*m.b8*m.b22*m.b23 - 96*m.b8*m.b22*m.b24 - 32*m.b8*
                       m.b22*m.b25 - 128*m.b8*m.b23*m.b24 - 32*m.b8*m.b23*m.b25 - 64*m.b8*m.b24*m.b25 - 448*m.b9*m.b10*
                       m.b11 - 672*m.b9*m.b10*m.b12 - 640*m.b9*m.b10*m.b13 - 608*m.b9*m.b10*m.b14 - 640*m.b9*m.b10*m.b15
                        - 672*m.b9*m.b10*m.b16 - 608*m.b9*m.b10*m.b17 - 512*m.b9*m.b10*m.b18 - 416*m.b9*m.b10*m.b19 - 
                       352*m.b9*m.b10*m.b20 - 288*m.b9*m.b10*m.b21 - 224*m.b9*m.b10*m.b22 - 160*m.b9*m.b10*m.b23 - 96*
                       m.b9*m.b10*m.b24 - 32*m.b9*m.b10*m.b25 - 672*m.b9*m.b11*m.b12 - 448*m.b9*m.b11*m.b13 - 704*m.b9*
                       m.b11*m.b14 - 672*m.b9*m.b11*m.b15 - 672*m.b9*m.b11*m.b16 - 608*m.b9*m.b11*m.b17 - 512*m.b9*m.b11
                       *m.b18 - 416*m.b9*m.b11*m.b19 - 320*m.b9*m.b11*m.b20 - 256*m.b9*m.b11*m.b21 - 192*m.b9*m.b11*
                       m.b22 - 128*m.b9*m.b11*m.b23 - 64*m.b9*m.b11*m.b24 - 32*m.b9*m.b11*m.b25 - 736*m.b9*m.b12*m.b13
                        - 736*m.b9*m.b12*m.b14 - 448*m.b9*m.b12*m.b15 - 672*m.b9*m.b12*m.b16 - 608*m.b9*m.b12*m.b17 - 
                       512*m.b9*m.b12*m.b18 - 416*m.b9*m.b12*m.b19 - 288*m.b9*m.b12*m.b20 - 224*m.b9*m.b12*m.b21 - 160*
                       m.b9*m.b12*m.b22 - 96*m.b9*m.b12*m.b23 - 64*m.b9*m.b12*m.b24 - 32*m.b9*m.b12*m.b25 - 704*m.b9*
                       m.b13*m.b14 - 672*m.b9*m.b13*m.b15 - 672*m.b9*m.b13*m.b16 - 320*m.b9*m.b13*m.b17 - 512*m.b9*m.b13
                       *m.b18 - 416*m.b9*m.b13*m.b19 - 288*m.b9*m.b13*m.b20 - 192*m.b9*m.b13*m.b21 - 128*m.b9*m.b13*
                       m.b22 - 96*m.b9*m.b13*m.b23 - 64*m.b9*m.b13*m.b24 - 32*m.b9*m.b13*m.b25 - 672*m.b9*m.b14*m.b15 - 
                       672*m.b9*m.b14*m.b16 - 608*m.b9*m.b14*m.b17 - 512*m.b9*m.b14*m.b18 - 192*m.b9*m.b14*m.b19 - 288*
                       m.b9*m.b14*m.b20 - 160*m.b9*m.b14*m.b21 - 128*m.b9*m.b14*m.b22 - 96*m.b9*m.b14*m.b23 - 64*m.b9*
                       m.b14*m.b24 - 32*m.b9*m.b14*m.b25 - 672*m.b9*m.b15*m.b16 - 608*m.b9*m.b15*m.b17 - 512*m.b9*m.b15*
                       m.b18 - 416*m.b9*m.b15*m.b19 - 288*m.b9*m.b15*m.b20 - 32*m.b9*m.b15*m.b21 - 128*m.b9*m.b15*m.b22
                        - 96*m.b9*m.b15*m.b23 - 64*m.b9*m.b15*m.b24 - 32*m.b9*m.b15*m.b25 - 608*m.b9*m.b16*m.b17 - 512*
                       m.b9*m.b16*m.b18 - 416*m.b9*m.b16*m.b19 - 320*m.b9*m.b16*m.b20 - 224*m.b9*m.b16*m.b21 - 128*m.b9*
                       m.b16*m.b22 - 64*m.b9*m.b16*m.b24 - 32*m.b9*m.b16*m.b25 - 512*m.b9*m.b17*m.b18 - 448*m.b9*m.b17*
                       m.b19 - 352*m.b9*m.b17*m.b20 - 256*m.b9*m.b17*m.b21 - 160*m.b9*m.b17*m.b22 - 96*m.b9*m.b17*m.b23
                        - 64*m.b9*m.b17*m.b24 - 448*m.b9*m.b18*m.b19 - 384*m.b9*m.b18*m.b20 - 288*m.b9*m.b18*m.b21 - 192
                       *m.b9*m.b18*m.b22 - 96*m.b9*m.b18*m.b23 - 64*m.b9*m.b18*m.b24 - 32*m.b9*m.b18*m.b25 - 384*m.b9*
                       m.b19*m.b20 - 320*m.b9*m.b19*m.b21 - 224*m.b9*m.b19*m.b22 - 128*m.b9*m.b19*m.b23 - 64*m.b9*m.b19*
                       m.b24 - 32*m.b9*m.b19*m.b25 - 320*m.b9*m.b20*m.b21 - 256*m.b9*m.b20*m.b22 - 160*m.b9*m.b20*m.b23
                        - 64*m.b9*m.b20*m.b24 - 32*m.b9*m.b20*m.b25 - 256*m.b9*m.b21*m.b22 - 192*m.b9*m.b21*m.b23 - 96*
                       m.b9*m.b21*m.b24 - 32*m.b9*m.b21*m.b25 - 192*m.b9*m.b22*m.b23 - 128*m.b9*m.b22*m.b24 - 32*m.b9*
                       m.b22*m.b25 - 128*m.b9*m.b23*m.b24 - 64*m.b9*m.b23*m.b25 - 64*m.b9*m.b24*m.b25 - 448*m.b10*m.b11*
                       m.b12 - 672*m.b10*m.b11*m.b13 - 672*m.b10*m.b11*m.b14 - 640*m.b10*m.b11*m.b15 - 672*m.b10*m.b11*
                       m.b16 - 672*m.b10*m.b11*m.b17 - 576*m.b10*m.b11*m.b18 - 480*m.b10*m.b11*m.b19 - 352*m.b10*m.b11*
                       m.b20 - 288*m.b10*m.b11*m.b21 - 224*m.b10*m.b11*m.b22 - 160*m.b10*m.b11*m.b23 - 96*m.b10*m.b11*
                       m.b24 - 32*m.b10*m.b11*m.b25 - 672*m.b10*m.b12*m.b13 - 448*m.b10*m.b12*m.b14 - 736*m.b10*m.b12*
                       m.b15 - 672*m.b10*m.b12*m.b16 - 672*m.b10*m.b12*m.b17 - 576*m.b10*m.b12*m.b18 - 480*m.b10*m.b12*
                       m.b19 - 352*m.b10*m.b12*m.b20 - 256*m.b10*m.b12*m.b21 - 192*m.b10*m.b12*m.b22 - 128*m.b10*m.b12*
                       m.b23 - 64*m.b10*m.b12*m.b24 - 32*m.b10*m.b12*m.b25 - 736*m.b10*m.b13*m.b14 - 736*m.b10*m.b13*
                       m.b15 - 448*m.b10*m.b13*m.b16 - 672*m.b10*m.b13*m.b17 - 576*m.b10*m.b13*m.b18 - 480*m.b10*m.b13*
                       m.b19 - 352*m.b10*m.b13*m.b20 - 224*m.b10*m.b13*m.b21 - 160*m.b10*m.b13*m.b22 - 96*m.b10*m.b13*
                       m.b23 - 64*m.b10*m.b13*m.b24 - 32*m.b10*m.b13*m.b25 - 672*m.b10*m.b14*m.b15 - 672*m.b10*m.b14*
                       m.b16 - 672*m.b10*m.b14*m.b17 - 320*m.b10*m.b14*m.b18 - 480*m.b10*m.b14*m.b19 - 352*m.b10*m.b14*
                       m.b20 - 224*m.b10*m.b14*m.b21 - 128*m.b10*m.b14*m.b22 - 96*m.b10*m.b14*m.b23 - 64*m.b10*m.b14*
                       m.b24 - 32*m.b10*m.b14*m.b25 - 672*m.b10*m.b15*m.b16 - 672*m.b10*m.b15*m.b17 - 576*m.b10*m.b15*
                       m.b18 - 480*m.b10*m.b15*m.b19 - 160*m.b10*m.b15*m.b20 - 224*m.b10*m.b15*m.b21 - 128*m.b10*m.b15*
                       m.b22 - 96*m.b10*m.b15*m.b23 - 64*m.b10*m.b15*m.b24 - 32*m.b10*m.b15*m.b25 - 672*m.b10*m.b16*
                       m.b17 - 576*m.b10*m.b16*m.b18 - 480*m.b10*m.b16*m.b19 - 352*m.b10*m.b16*m.b20 - 256*m.b10*m.b16*
                       m.b21 - 32*m.b10*m.b16*m.b22 - 96*m.b10*m.b16*m.b23 - 64*m.b10*m.b16*m.b24 - 32*m.b10*m.b16*m.b25
                        - 544*m.b10*m.b17*m.b18 - 448*m.b10*m.b17*m.b19 - 384*m.b10*m.b17*m.b20 - 288*m.b10*m.b17*m.b21
                        - 192*m.b10*m.b17*m.b22 - 96*m.b10*m.b17*m.b23 - 32*m.b10*m.b17*m.b25 - 448*m.b10*m.b18*m.b19 - 
                       384*m.b10*m.b18*m.b20 - 320*m.b10*m.b18*m.b21 - 224*m.b10*m.b18*m.b22 - 128*m.b10*m.b18*m.b23 - 
                       64*m.b10*m.b18*m.b24 - 32*m.b10*m.b18*m.b25 - 384*m.b10*m.b19*m.b20 - 320*m.b10*m.b19*m.b21 - 256
                       *m.b10*m.b19*m.b22 - 160*m.b10*m.b19*m.b23 - 64*m.b10*m.b19*m.b24 - 32*m.b10*m.b19*m.b25 - 320*
                       m.b10*m.b20*m.b21 - 256*m.b10*m.b20*m.b22 - 192*m.b10*m.b20*m.b23 - 96*m.b10*m.b20*m.b24 - 32*
                       m.b10*m.b20*m.b25 - 256*m.b10*m.b21*m.b22 - 192*m.b10*m.b21*m.b23 - 128*m.b10*m.b21*m.b24 - 32*
                       m.b10*m.b21*m.b25 - 192*m.b10*m.b22*m.b23 - 128*m.b10*m.b22*m.b24 - 64*m.b10*m.b22*m.b25 - 128*
                       m.b10*m.b23*m.b24 - 64*m.b10*m.b23*m.b25 - 64*m.b10*m.b24*m.b25 - 448*m.b11*m.b12*m.b13 - 672*
                       m.b11*m.b12*m.b14 - 704*m.b11*m.b12*m.b15 - 672*m.b11*m.b12*m.b16 - 672*m.b11*m.b12*m.b17 - 640*
                       m.b11*m.b12*m.b18 - 544*m.b11*m.b12*m.b19 - 416*m.b11*m.b12*m.b20 - 288*m.b11*m.b12*m.b21 - 224*
                       m.b11*m.b12*m.b22 - 160*m.b11*m.b12*m.b23 - 96*m.b11*m.b12*m.b24 - 32*m.b11*m.b12*m.b25 - 672*
                       m.b11*m.b13*m.b14 - 448*m.b11*m.b13*m.b15 - 736*m.b11*m.b13*m.b16 - 672*m.b11*m.b13*m.b17 - 640*
                       m.b11*m.b13*m.b18 - 544*m.b11*m.b13*m.b19 - 416*m.b11*m.b13*m.b20 - 288*m.b11*m.b13*m.b21 - 192*
                       m.b11*m.b13*m.b22 - 128*m.b11*m.b13*m.b23 - 64*m.b11*m.b13*m.b24 - 32*m.b11*m.b13*m.b25 - 704*
                       m.b11*m.b14*m.b15 - 736*m.b11*m.b14*m.b16 - 448*m.b11*m.b14*m.b17 - 640*m.b11*m.b14*m.b18 - 544*
                       m.b11*m.b14*m.b19 - 416*m.b11*m.b14*m.b20 - 288*m.b11*m.b14*m.b21 - 160*m.b11*m.b14*m.b22 - 96*
                       m.b11*m.b14*m.b23 - 64*m.b11*m.b14*m.b24 - 32*m.b11*m.b14*m.b25 - 640*m.b11*m.b15*m.b16 - 672*
                       m.b11*m.b15*m.b17 - 640*m.b11*m.b15*m.b18 - 320*m.b11*m.b15*m.b19 - 416*m.b11*m.b15*m.b20 - 288*
                       m.b11*m.b15*m.b21 - 160*m.b11*m.b15*m.b22 - 96*m.b11*m.b15*m.b23 - 64*m.b11*m.b15*m.b24 - 32*
                       m.b11*m.b15*m.b25 - 640*m.b11*m.b16*m.b17 - 608*m.b11*m.b16*m.b18 - 512*m.b11*m.b16*m.b19 - 416*
                       m.b11*m.b16*m.b20 - 128*m.b11*m.b16*m.b21 - 192*m.b11*m.b16*m.b22 - 96*m.b11*m.b16*m.b23 - 64*
                       m.b11*m.b16*m.b24 - 32*m.b11*m.b16*m.b25 - 576*m.b11*m.b17*m.b18 - 480*m.b11*m.b17*m.b19 - 384*
                       m.b11*m.b17*m.b20 - 320*m.b11*m.b17*m.b21 - 224*m.b11*m.b17*m.b22 - 32*m.b11*m.b17*m.b23 - 64*
                       m.b11*m.b17*m.b24 - 32*m.b11*m.b17*m.b25 - 448*m.b11*m.b18*m.b19 - 384*m.b11*m.b18*m.b20 - 320*
                       m.b11*m.b18*m.b21 - 256*m.b11*m.b18*m.b22 - 160*m.b11*m.b18*m.b23 - 64*m.b11*m.b18*m.b24 - 384*
                       m.b11*m.b19*m.b20 - 320*m.b11*m.b19*m.b21 - 256*m.b11*m.b19*m.b22 - 192*m.b11*m.b19*m.b23 - 96*
                       m.b11*m.b19*m.b24 - 32*m.b11*m.b19*m.b25 - 320*m.b11*m.b20*m.b21 - 256*m.b11*m.b20*m.b22 - 192*
                       m.b11*m.b20*m.b23 - 128*m.b11*m.b20*m.b24 - 32*m.b11*m.b20*m.b25 - 256*m.b11*m.b21*m.b22 - 192*
                       m.b11*m.b21*m.b23 - 128*m.b11*m.b21*m.b24 - 64*m.b11*m.b21*m.b25 - 192*m.b11*m.b22*m.b23 - 128*
                       m.b11*m.b22*m.b24 - 64*m.b11*m.b22*m.b25 - 128*m.b11*m.b23*m.b24 - 64*m.b11*m.b23*m.b25 - 64*
                       m.b11*m.b24*m.b25 - 448*m.b12*m.b13*m.b14 - 672*m.b12*m.b13*m.b15 - 736*m.b12*m.b13*m.b16 - 704*
                       m.b12*m.b13*m.b17 - 672*m.b12*m.b13*m.b18 - 608*m.b12*m.b13*m.b19 - 480*m.b12*m.b13*m.b20 - 352*
                       m.b12*m.b13*m.b21 - 224*m.b12*m.b13*m.b22 - 160*m.b12*m.b13*m.b23 - 96*m.b12*m.b13*m.b24 - 32*
                       m.b12*m.b13*m.b25 - 672*m.b12*m.b14*m.b15 - 448*m.b12*m.b14*m.b16 - 736*m.b12*m.b14*m.b17 - 672*
                       m.b12*m.b14*m.b18 - 608*m.b12*m.b14*m.b19 - 480*m.b12*m.b14*m.b20 - 352*m.b12*m.b14*m.b21 - 224*
                       m.b12*m.b14*m.b22 - 128*m.b12*m.b14*m.b23 - 64*m.b12*m.b14*m.b24 - 32*m.b12*m.b14*m.b25 - 672*
                       m.b12*m.b15*m.b16 - 704*m.b12*m.b15*m.b17 - 416*m.b12*m.b15*m.b18 - 576*m.b12*m.b15*m.b19 - 480*
                       m.b12*m.b15*m.b20 - 352*m.b12*m.b15*m.b21 - 224*m.b12*m.b15*m.b22 - 96*m.b12*m.b15*m.b23 - 64*
                       m.b12*m.b15*m.b24 - 32*m.b12*m.b15*m.b25 - 608*m.b12*m.b16*m.b17 - 608*m.b12*m.b16*m.b18 - 544*
                       m.b12*m.b16*m.b19 - 256*m.b12*m.b16*m.b20 - 352*m.b12*m.b16*m.b21 - 224*m.b12*m.b16*m.b22 - 128*
                       m.b12*m.b16*m.b23 - 64*m.b12*m.b16*m.b24 - 32*m.b12*m.b16*m.b25 - 576*m.b12*m.b17*m.b18 - 512*
                       m.b12*m.b17*m.b19 - 416*m.b12*m.b17*m.b20 - 320*m.b12*m.b17*m.b21 - 128*m.b12*m.b17*m.b22 - 160*
                       m.b12*m.b17*m.b23 - 64*m.b12*m.b17*m.b24 - 32*m.b12*m.b17*m.b25 - 480*m.b12*m.b18*m.b19 - 384*
                       m.b12*m.b18*m.b20 - 320*m.b12*m.b18*m.b21 - 256*m.b12*m.b18*m.b22 - 192*m.b12*m.b18*m.b23 - 32*
                       m.b12*m.b18*m.b24 - 32*m.b12*m.b18*m.b25 - 384*m.b12*m.b19*m.b20 - 320*m.b12*m.b19*m.b21 - 256*
                       m.b12*m.b19*m.b22 - 192*m.b12*m.b19*m.b23 - 128*m.b12*m.b19*m.b24 - 32*m.b12*m.b19*m.b25 - 320*
                       m.b12*m.b20*m.b21 - 256*m.b12*m.b20*m.b22 - 192*m.b12*m.b20*m.b23 - 128*m.b12*m.b20*m.b24 - 64*
                       m.b12*m.b20*m.b25 - 256*m.b12*m.b21*m.b22 - 192*m.b12*m.b21*m.b23 - 128*m.b12*m.b21*m.b24 - 64*
                       m.b12*m.b21*m.b25 - 192*m.b12*m.b22*m.b23 - 128*m.b12*m.b22*m.b24 - 64*m.b12*m.b22*m.b25 - 128*
                       m.b12*m.b23*m.b24 - 64*m.b12*m.b23*m.b25 - 64*m.b12*m.b24*m.b25 - 448*m.b13*m.b14*m.b15 - 672*
                       m.b13*m.b14*m.b16 - 736*m.b13*m.b14*m.b17 - 704*m.b13*m.b14*m.b18 - 640*m.b13*m.b14*m.b19 - 544*
                       m.b13*m.b14*m.b20 - 416*m.b13*m.b14*m.b21 - 288*m.b13*m.b14*m.b22 - 160*m.b13*m.b14*m.b23 - 96*
                       m.b13*m.b14*m.b24 - 32*m.b13*m.b14*m.b25 - 672*m.b13*m.b15*m.b16 - 448*m.b13*m.b15*m.b17 - 672*
                       m.b13*m.b15*m.b18 - 608*m.b13*m.b15*m.b19 - 512*m.b13*m.b15*m.b20 - 416*m.b13*m.b15*m.b21 - 288*
                       m.b13*m.b15*m.b22 - 160*m.b13*m.b15*m.b23 - 64*m.b13*m.b15*m.b24 - 32*m.b13*m.b15*m.b25 - 640*
                       m.b13*m.b16*m.b17 - 640*m.b13*m.b16*m.b18 - 352*m.b13*m.b16*m.b19 - 480*m.b13*m.b16*m.b20 - 384*
                       m.b13*m.b16*m.b21 - 288*m.b13*m.b16*m.b22 - 160*m.b13*m.b16*m.b23 - 64*m.b13*m.b16*m.b24 - 32*
                       m.b13*m.b16*m.b25 - 576*m.b13*m.b17*m.b18 - 544*m.b13*m.b17*m.b19 - 448*m.b13*m.b17*m.b20 - 192*
                       m.b13*m.b17*m.b21 - 256*m.b13*m.b17*m.b22 - 192*m.b13*m.b17*m.b23 - 96*m.b13*m.b17*m.b24 - 32*
                       m.b13*m.b17*m.b25 - 512*m.b13*m.b18*m.b19 - 416*m.b13*m.b18*m.b20 - 320*m.b13*m.b18*m.b21 - 256*
                       m.b13*m.b18*m.b22 - 96*m.b13*m.b18*m.b23 - 128*m.b13*m.b18*m.b24 - 32*m.b13*m.b18*m.b25 - 384*
                       m.b13*m.b19*m.b20 - 320*m.b13*m.b19*m.b21 - 256*m.b13*m.b19*m.b22 - 192*m.b13*m.b19*m.b23 - 128*
                       m.b13*m.b19*m.b24 - 32*m.b13*m.b19*m.b25 - 320*m.b13*m.b20*m.b21 - 256*m.b13*m.b20*m.b22 - 192*
                       m.b13*m.b20*m.b23 - 128*m.b13*m.b20*m.b24 - 64*m.b13*m.b20*m.b25 - 256*m.b13*m.b21*m.b22 - 192*
                       m.b13*m.b21*m.b23 - 128*m.b13*m.b21*m.b24 - 64*m.b13*m.b21*m.b25 - 192*m.b13*m.b22*m.b23 - 128*
                       m.b13*m.b22*m.b24 - 64*m.b13*m.b22*m.b25 - 128*m.b13*m.b23*m.b24 - 64*m.b13*m.b23*m.b25 - 64*
                       m.b13*m.b24*m.b25 - 448*m.b14*m.b15*m.b16 - 672*m.b14*m.b15*m.b17 - 704*m.b14*m.b15*m.b18 - 640*
                       m.b14*m.b15*m.b19 - 544*m.b14*m.b15*m.b20 - 448*m.b14*m.b15*m.b21 - 352*m.b14*m.b15*m.b22 - 224*
                       m.b14*m.b15*m.b23 - 96*m.b14*m.b15*m.b24 - 32*m.b14*m.b15*m.b25 - 672*m.b14*m.b16*m.b17 - 416*
                       m.b14*m.b16*m.b18 - 608*m.b14*m.b16*m.b19 - 512*m.b14*m.b16*m.b20 - 416*m.b14*m.b16*m.b21 - 320*
                       m.b14*m.b16*m.b22 - 224*m.b14*m.b16*m.b23 - 96*m.b14*m.b16*m.b24 - 32*m.b14*m.b16*m.b25 - 608*
                       m.b14*m.b17*m.b18 - 576*m.b14*m.b17*m.b19 - 288*m.b14*m.b17*m.b20 - 384*m.b14*m.b17*m.b21 - 288*
                       m.b14*m.b17*m.b22 - 192*m.b14*m.b17*m.b23 - 128*m.b14*m.b17*m.b24 - 32*m.b14*m.b17*m.b25 - 544*
                       m.b14*m.b18*m.b19 - 448*m.b14*m.b18*m.b20 - 352*m.b14*m.b18*m.b21 - 128*m.b14*m.b18*m.b22 - 192*
                       m.b14*m.b18*m.b23 - 128*m.b14*m.b18*m.b24 - 64*m.b14*m.b18*m.b25 - 416*m.b14*m.b19*m.b20 - 320*
                       m.b14*m.b19*m.b21 - 256*m.b14*m.b19*m.b22 - 192*m.b14*m.b19*m.b23 - 64*m.b14*m.b19*m.b24 - 64*
                       m.b14*m.b19*m.b25 - 320*m.b14*m.b20*m.b21 - 256*m.b14*m.b20*m.b22 - 192*m.b14*m.b20*m.b23 - 128*
                       m.b14*m.b20*m.b24 - 64*m.b14*m.b20*m.b25 - 256*m.b14*m.b21*m.b22 - 192*m.b14*m.b21*m.b23 - 128*
                       m.b14*m.b21*m.b24 - 64*m.b14*m.b21*m.b25 - 192*m.b14*m.b22*m.b23 - 128*m.b14*m.b22*m.b24 - 64*
                       m.b14*m.b22*m.b25 - 128*m.b14*m.b23*m.b24 - 64*m.b14*m.b23*m.b25 - 64*m.b14*m.b24*m.b25 - 448*
                       m.b15*m.b16*m.b17 - 672*m.b15*m.b16*m.b18 - 640*m.b15*m.b16*m.b19 - 544*m.b15*m.b16*m.b20 - 448*
                       m.b15*m.b16*m.b21 - 352*m.b15*m.b16*m.b22 - 256*m.b15*m.b16*m.b23 - 160*m.b15*m.b16*m.b24 - 32*
                       m.b15*m.b16*m.b25 - 640*m.b15*m.b17*m.b18 - 384*m.b15*m.b17*m.b19 - 512*m.b15*m.b17*m.b20 - 416*
                       m.b15*m.b17*m.b21 - 320*m.b15*m.b17*m.b22 - 224*m.b15*m.b17*m.b23 - 128*m.b15*m.b17*m.b24 - 64*
                       m.b15*m.b17*m.b25 - 576*m.b15*m.b18*m.b19 - 480*m.b15*m.b18*m.b20 - 224*m.b15*m.b18*m.b21 - 288*
                       m.b15*m.b18*m.b22 - 192*m.b15*m.b18*m.b23 - 128*m.b15*m.b18*m.b24 - 64*m.b15*m.b18*m.b25 - 448*
                       m.b15*m.b19*m.b20 - 352*m.b15*m.b19*m.b21 - 256*m.b15*m.b19*m.b22 - 96*m.b15*m.b19*m.b23 - 128*
                       m.b15*m.b19*m.b24 - 64*m.b15*m.b19*m.b25 - 320*m.b15*m.b20*m.b21 - 256*m.b15*m.b20*m.b22 - 192*
                       m.b15*m.b20*m.b23 - 128*m.b15*m.b20*m.b24 - 32*m.b15*m.b20*m.b25 - 256*m.b15*m.b21*m.b22 - 192*
                       m.b15*m.b21*m.b23 - 128*m.b15*m.b21*m.b24 - 64*m.b15*m.b21*m.b25 - 192*m.b15*m.b22*m.b23 - 128*
                       m.b15*m.b22*m.b24 - 64*m.b15*m.b22*m.b25 - 128*m.b15*m.b23*m.b24 - 64*m.b15*m.b23*m.b25 - 64*
                       m.b15*m.b24*m.b25 - 448*m.b16*m.b17*m.b18 - 640*m.b16*m.b17*m.b19 - 544*m.b16*m.b17*m.b20 - 448*
                       m.b16*m.b17*m.b21 - 352*m.b16*m.b17*m.b22 - 256*m.b16*m.b17*m.b23 - 160*m.b16*m.b17*m.b24 - 64*
                       m.b16*m.b17*m.b25 - 608*m.b16*m.b18*m.b19 - 320*m.b16*m.b18*m.b20 - 416*m.b16*m.b18*m.b21 - 320*
                       m.b16*m.b18*m.b22 - 224*m.b16*m.b18*m.b23 - 128*m.b16*m.b18*m.b24 - 64*m.b16*m.b18*m.b25 - 480*
                       m.b16*m.b19*m.b20 - 384*m.b16*m.b19*m.b21 - 160*m.b16*m.b19*m.b22 - 192*m.b16*m.b19*m.b23 - 128*
                       m.b16*m.b19*m.b24 - 64*m.b16*m.b19*m.b25 - 352*m.b16*m.b20*m.b21 - 256*m.b16*m.b20*m.b22 - 192*
                       m.b16*m.b20*m.b23 - 64*m.b16*m.b20*m.b24 - 64*m.b16*m.b20*m.b25 - 256*m.b16*m.b21*m.b22 - 192*
                       m.b16*m.b21*m.b23 - 128*m.b16*m.b21*m.b24 - 64*m.b16*m.b21*m.b25 - 192*m.b16*m.b22*m.b23 - 128*
                       m.b16*m.b22*m.b24 - 64*m.b16*m.b22*m.b25 - 128*m.b16*m.b23*m.b24 - 64*m.b16*m.b23*m.b25 - 64*
                       m.b16*m.b24*m.b25 - 416*m.b17*m.b18*m.b19 - 544*m.b17*m.b18*m.b20 - 448*m.b17*m.b18*m.b21 - 352*
                       m.b17*m.b18*m.b22 - 256*m.b17*m.b18*m.b23 - 160*m.b17*m.b18*m.b24 - 64*m.b17*m.b18*m.b25 - 512*
                       m.b17*m.b19*m.b20 - 256*m.b17*m.b19*m.b21 - 320*m.b17*m.b19*m.b22 - 224*m.b17*m.b19*m.b23 - 128*
                       m.b17*m.b19*m.b24 - 64*m.b17*m.b19*m.b25 - 384*m.b17*m.b20*m.b21 - 288*m.b17*m.b20*m.b22 - 96*
                       m.b17*m.b20*m.b23 - 128*m.b17*m.b20*m.b24 - 64*m.b17*m.b20*m.b25 - 256*m.b17*m.b21*m.b22 - 192*
                       m.b17*m.b21*m.b23 - 128*m.b17*m.b21*m.b24 - 32*m.b17*m.b21*m.b25 - 192*m.b17*m.b22*m.b23 - 128*
                       m.b17*m.b22*m.b24 - 64*m.b17*m.b22*m.b25 - 128*m.b17*m.b23*m.b24 - 64*m.b17*m.b23*m.b25 - 64*
                       m.b17*m.b24*m.b25 - 352*m.b18*m.b19*m.b20 - 448*m.b18*m.b19*m.b21 - 352*m.b18*m.b19*m.b22 - 256*
                       m.b18*m.b19*m.b23 - 160*m.b18*m.b19*m.b24 - 64*m.b18*m.b19*m.b25 - 416*m.b18*m.b20*m.b21 - 192*
                       m.b18*m.b20*m.b22 - 224*m.b18*m.b20*m.b23 - 128*m.b18*m.b20*m.b24 - 64*m.b18*m.b20*m.b25 - 288*
                       m.b18*m.b21*m.b22 - 192*m.b18*m.b21*m.b23 - 64*m.b18*m.b21*m.b24 - 64*m.b18*m.b21*m.b25 - 192*
                       m.b18*m.b22*m.b23 - 128*m.b18*m.b22*m.b24 - 64*m.b18*m.b22*m.b25 - 128*m.b18*m.b23*m.b24 - 64*
                       m.b18*m.b23*m.b25 - 64*m.b18*m.b24*m.b25 - 288*m.b19*m.b20*m.b21 - 352*m.b19*m.b20*m.b22 - 256*
                       m.b19*m.b20*m.b23 - 160*m.b19*m.b20*m.b24 - 64*m.b19*m.b20*m.b25 - 320*m.b19*m.b21*m.b22 - 128*
                       m.b19*m.b21*m.b23 - 128*m.b19*m.b21*m.b24 - 64*m.b19*m.b21*m.b25 - 192*m.b19*m.b22*m.b23 - 128*
                       m.b19*m.b22*m.b24 - 32*m.b19*m.b22*m.b25 - 128*m.b19*m.b23*m.b24 - 64*m.b19*m.b23*m.b25 - 64*
                       m.b19*m.b24*m.b25 - 224*m.b20*m.b21*m.b22 - 256*m.b20*m.b21*m.b23 - 160*m.b20*m.b21*m.b24 - 64*
                       m.b20*m.b21*m.b25 - 224*m.b20*m.b22*m.b23 - 64*m.b20*m.b22*m.b24 - 64*m.b20*m.b22*m.b25 - 128*
                       m.b20*m.b23*m.b24 - 64*m.b20*m.b23*m.b25 - 64*m.b20*m.b24*m.b25 - 160*m.b21*m.b22*m.b23 - 160*
                       m.b21*m.b22*m.b24 - 64*m.b21*m.b22*m.b25 - 128*m.b21*m.b23*m.b24 - 32*m.b21*m.b23*m.b25 - 64*
                       m.b21*m.b24*m.b25 - 96*m.b22*m.b23*m.b24 - 64*m.b22*m.b23*m.b25 - 64*m.b22*m.b24*m.b25 - 32*m.b23
                       *m.b24*m.b25 + 256*m.b1*m.b2 + 248*m.b1*m.b3 + 240*m.b1*m.b4 + 232*m.b1*m.b5 + 224*m.b1*m.b6 + 
                       216*m.b1*m.b7 + 208*m.b1*m.b8 + 200*m.b1*m.b9 + 192*m.b1*m.b10 + 200*m.b1*m.b11 + 192*m.b1*m.b12
                        + 184*m.b1*m.b13 + 176*m.b1*m.b14 + 168*m.b1*m.b15 + 160*m.b1*m.b16 + 152*m.b1*m.b17 + 144*m.b1*
                       m.b18 + 136*m.b1*m.b19 + 512*m.b2*m.b3 + 512*m.b2*m.b4 + 496*m.b2*m.b5 + 480*m.b2*m.b6 + 464*m.b2
                       *m.b7 + 448*m.b2*m.b8 + 432*m.b2*m.b9 + 416*m.b2*m.b10 + 416*m.b2*m.b11 + 416*m.b2*m.b12 + 400*
                       m.b2*m.b13 + 384*m.b2*m.b14 + 368*m.b2*m.b15 + 352*m.b2*m.b16 + 336*m.b2*m.b17 + 320*m.b2*m.b18
                        + 288*m.b2*m.b19 + 136*m.b2*m.b20 + 784*m.b3*m.b4 + 776*m.b3*m.b5 + 768*m.b3*m.b6 + 744*m.b3*
                       m.b7 + 720*m.b3*m.b8 + 696*m.b3*m.b9 + 672*m.b3*m.b10 + 648*m.b3*m.b11 + 656*m.b3*m.b12 + 648*
                       m.b3*m.b13 + 624*m.b3*m.b14 + 600*m.b3*m.b15 + 576*m.b3*m.b16 + 552*m.b3*m.b17 + 512*m.b3*m.b18
                        + 472*m.b3*m.b19 + 288*m.b3*m.b20 + 136*m.b3*m.b21 + 1072*m.b4*m.b5 + 1056*m.b4*m.b6 + 1040*m.b4
                       *m.b7 + 1024*m.b4*m.b8 + 992*m.b4*m.b9 + 960*m.b4*m.b10 + 928*m.b4*m.b11 + 912*m.b4*m.b12 + 912*
                       m.b4*m.b13 + 896*m.b4*m.b14 + 864*m.b4*m.b15 + 832*m.b4*m.b16 + 784*m.b4*m.b17 + 736*m.b4*m.b18
                        + 672*m.b4*m.b19 + 472*m.b4*m.b20 + 288*m.b4*m.b21 + 136*m.b4*m.b22 + 1376*m.b5*m.b6 + 1352*m.b5
                       *m.b7 + 1328*m.b5*m.b8 + 1304*m.b5*m.b9 + 1280*m.b5*m.b10 + 1240*m.b5*m.b11 + 1200*m.b5*m.b12 + 
                       1192*m.b5*m.b13 + 1184*m.b5*m.b14 + 1160*m.b5*m.b15 + 1104*m.b5*m.b16 + 1048*m.b5*m.b17 + 976*
                       m.b5*m.b18 + 904*m.b5*m.b19 + 672*m.b5*m.b20 + 472*m.b5*m.b21 + 288*m.b5*m.b22 + 136*m.b5*m.b23
                        + 1696*m.b6*m.b7 + 1664*m.b6*m.b8 + 1632*m.b6*m.b9 + 1600*m.b6*m.b10 + 1568*m.b6*m.b11 + 1536*
                       m.b6*m.b12 + 1504*m.b6*m.b13 + 1488*m.b6*m.b14 + 1456*m.b6*m.b15 + 1408*m.b6*m.b16 + 1328*m.b6*
                       m.b17 + 1248*m.b6*m.b18 + 1152*m.b6*m.b19 + 904*m.b6*m.b20 + 672*m.b6*m.b21 + 472*m.b6*m.b22 + 
                       288*m.b6*m.b23 + 136*m.b6*m.b24 + 2032*m.b7*m.b8 + 1992*m.b7*m.b9 + 1952*m.b7*m.b10 + 1912*m.b7*
                       m.b11 + 1872*m.b7*m.b12 + 1832*m.b7*m.b13 + 1808*m.b7*m.b14 + 1768*m.b7*m.b15 + 1712*m.b7*m.b16
                        + 1640*m.b7*m.b17 + 1536*m.b7*m.b18 + 1432*m.b7*m.b19 + 1152*m.b7*m.b20 + 904*m.b7*m.b21 + 672*
                       m.b7*m.b22 + 472*m.b7*m.b23 + 288*m.b7*m.b24 + 136*m.b7*m.b25 + 2192*m.b8*m.b9 + 2152*m.b8*m.b10
                        + 2112*m.b8*m.b11 + 2056*m.b8*m.b12 + 2000*m.b8*m.b13 + 1976*m.b8*m.b14 + 1968*m.b8*m.b15 + 1912
                       *m.b8*m.b16 + 1840*m.b8*m.b17 + 1720*m.b8*m.b18 + 1536*m.b8*m.b19 + 1248*m.b8*m.b20 + 976*m.b8*
                       m.b21 + 736*m.b8*m.b22 + 512*m.b8*m.b23 + 320*m.b8*m.b24 + 144*m.b8*m.b25 + 2320*m.b9*m.b10 + 
                       2264*m.b9*m.b11 + 2208*m.b9*m.b12 + 2120*m.b9*m.b13 + 2096*m.b9*m.b14 + 2072*m.b9*m.b15 + 2080*
                       m.b9*m.b16 + 1992*m.b9*m.b17 + 1840*m.b9*m.b18 + 1640*m.b9*m.b19 + 1328*m.b9*m.b20 + 1048*m.b9*
                       m.b21 + 784*m.b9*m.b22 + 552*m.b9*m.b23 + 336*m.b9*m.b24 + 152*m.b9*m.b25 + 2384*m.b10*m.b11 + 
                       2312*m.b10*m.b12 + 2240*m.b10*m.b13 + 2152*m.b10*m.b14 + 2144*m.b10*m.b15 + 2120*m.b10*m.b16 + 
                       2080*m.b10*m.b17 + 1912*m.b10*m.b18 + 1712*m.b10*m.b19 + 1408*m.b10*m.b20 + 1104*m.b10*m.b21 + 
                       832*m.b10*m.b22 + 576*m.b10*m.b23 + 352*m.b10*m.b24 + 160*m.b10*m.b25 + 2432*m.b11*m.b12 + 2344*
                       m.b11*m.b13 + 2272*m.b11*m.b14 + 2184*m.b11*m.b15 + 2144*m.b11*m.b16 + 2072*m.b11*m.b17 + 1968*
                       m.b11*m.b18 + 1768*m.b11*m.b19 + 1456*m.b11*m.b20 + 1160*m.b11*m.b21 + 864*m.b11*m.b22 + 600*
                       m.b11*m.b23 + 368*m.b11*m.b24 + 168*m.b11*m.b25 + 2480*m.b12*m.b13 + 2376*m.b12*m.b14 + 2272*
                       m.b12*m.b15 + 2152*m.b12*m.b16 + 2096*m.b12*m.b17 + 1976*m.b12*m.b18 + 1808*m.b12*m.b19 + 1488*
                       m.b12*m.b20 + 1184*m.b12*m.b21 + 896*m.b12*m.b22 + 624*m.b12*m.b23 + 384*m.b12*m.b24 + 176*m.b12*
                       m.b25 + 2480*m.b13*m.b14 + 2344*m.b13*m.b15 + 2240*m.b13*m.b16 + 2120*m.b13*m.b17 + 2000*m.b13*
                       m.b18 + 1832*m.b13*m.b19 + 1504*m.b13*m.b20 + 1192*m.b13*m.b21 + 912*m.b13*m.b22 + 648*m.b13*
                       m.b23 + 400*m.b13*m.b24 + 184*m.b13*m.b25 + 2432*m.b14*m.b15 + 2312*m.b14*m.b16 + 2208*m.b14*
                       m.b17 + 2056*m.b14*m.b18 + 1872*m.b14*m.b19 + 1536*m.b14*m.b20 + 1200*m.b14*m.b21 + 912*m.b14*
                       m.b22 + 656*m.b14*m.b23 + 416*m.b14*m.b24 + 192*m.b14*m.b25 + 2384*m.b15*m.b16 + 2264*m.b15*m.b17
                        + 2112*m.b15*m.b18 + 1912*m.b15*m.b19 + 1568*m.b15*m.b20 + 1240*m.b15*m.b21 + 928*m.b15*m.b22 + 
                       648*m.b15*m.b23 + 416*m.b15*m.b24 + 200*m.b15*m.b25 + 2320*m.b16*m.b17 + 2152*m.b16*m.b18 + 1952*
                       m.b16*m.b19 + 1600*m.b16*m.b20 + 1280*m.b16*m.b21 + 960*m.b16*m.b22 + 672*m.b16*m.b23 + 416*m.b16
                       *m.b24 + 192*m.b16*m.b25 + 2192*m.b17*m.b18 + 1992*m.b17*m.b19 + 1632*m.b17*m.b20 + 1304*m.b17*
                       m.b21 + 992*m.b17*m.b22 + 696*m.b17*m.b23 + 432*m.b17*m.b24 + 200*m.b17*m.b25 + 2032*m.b18*m.b19
                        + 1664*m.b18*m.b20 + 1328*m.b18*m.b21 + 1024*m.b18*m.b22 + 720*m.b18*m.b23 + 448*m.b18*m.b24 + 
                       208*m.b18*m.b25 + 1696*m.b19*m.b20 + 1352*m.b19*m.b21 + 1040*m.b19*m.b22 + 744*m.b19*m.b23 + 464*
                       m.b19*m.b24 + 216*m.b19*m.b25 + 1376*m.b20*m.b21 + 1056*m.b20*m.b22 + 768*m.b20*m.b23 + 480*m.b20
                       *m.b24 + 224*m.b20*m.b25 + 1072*m.b21*m.b22 + 776*m.b21*m.b23 + 496*m.b21*m.b24 + 232*m.b21*m.b25
                        + 784*m.b22*m.b23 + 512*m.b22*m.b24 + 240*m.b22*m.b25 + 512*m.b23*m.b24 + 248*m.b23*m.b25 + 256*
                       m.b24*m.b25 - 612*m.b1 - 1284*m.b2 - 2008*m.b3 - 2776*m.b4 - 3580*m.b5 - 4412*m.b6 - 5264*m.b7 - 
                       5628*m.b8 - 5872*m.b9 - 5996*m.b10 - 6072*m.b11 - 6108*m.b12 - 6112*m.b13 - 6108*m.b14 - 6072*
                       m.b15 - 5996*m.b16 - 5872*m.b17 - 5628*m.b18 - 5264*m.b19 - 4412*m.b20 - 3580*m.b21 - 2776*m.b22
                        - 2008*m.b23 - 1284*m.b24 - 612*m.b25 - m.x26 <= 0)

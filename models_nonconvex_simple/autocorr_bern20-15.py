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
                       m.b20 + 384*m.b7*m.b8*m.b9*m.b10 + 384*m.b7*m.b8*m.b10*m.b11 + 384*m.b7*m.b8*m.b11*m.b12 + 448*
                       m.b7*m.b8*m.b12*m.b13 + 448*m.b7*m.b8*m.b13*m.b14 + 384*m.b7*m.b8*m.b14*m.b15 + 320*m.b7*m.b8*
                       m.b15*m.b16 + 256*m.b7*m.b8*m.b16*m.b17 + 192*m.b7*m.b8*m.b17*m.b18 + 128*m.b7*m.b8*m.b18*m.b19
                        + 64*m.b7*m.b8*m.b19*m.b20 + 384*m.b7*m.b9*m.b10*m.b12 + 448*m.b7*m.b9*m.b11*m.b13 + 448*m.b7*
                       m.b9*m.b12*m.b14 + 384*m.b7*m.b9*m.b13*m.b15 + 320*m.b7*m.b9*m.b14*m.b16 + 256*m.b7*m.b9*m.b15*
                       m.b17 + 192*m.b7*m.b9*m.b16*m.b18 + 128*m.b7*m.b9*m.b17*m.b19 + 64*m.b7*m.b9*m.b18*m.b20 + 448*
                       m.b7*m.b10*m.b11*m.b14 + 384*m.b7*m.b10*m.b12*m.b15 + 320*m.b7*m.b10*m.b13*m.b16 + 256*m.b7*m.b10
                       *m.b14*m.b17 + 192*m.b7*m.b10*m.b15*m.b18 + 128*m.b7*m.b10*m.b16*m.b19 + 64*m.b7*m.b10*m.b17*
                       m.b20 + 320*m.b7*m.b11*m.b12*m.b16 + 256*m.b7*m.b11*m.b13*m.b17 + 192*m.b7*m.b11*m.b14*m.b18 + 
                       128*m.b7*m.b11*m.b15*m.b19 + 64*m.b7*m.b11*m.b16*m.b20 + 192*m.b7*m.b12*m.b13*m.b18 + 128*m.b7*
                       m.b12*m.b14*m.b19 + 64*m.b7*m.b12*m.b15*m.b20 + 64*m.b7*m.b13*m.b14*m.b20 + 384*m.b8*m.b9*m.b10*
                       m.b11 + 384*m.b8*m.b9*m.b11*m.b12 + 384*m.b8*m.b9*m.b12*m.b13 + 448*m.b8*m.b9*m.b13*m.b14 + 384*
                       m.b8*m.b9*m.b14*m.b15 + 320*m.b8*m.b9*m.b15*m.b16 + 256*m.b8*m.b9*m.b16*m.b17 + 192*m.b8*m.b9*
                       m.b17*m.b18 + 128*m.b8*m.b9*m.b18*m.b19 + 64*m.b8*m.b9*m.b19*m.b20 + 384*m.b8*m.b10*m.b11*m.b13
                        + 448*m.b8*m.b10*m.b12*m.b14 + 384*m.b8*m.b10*m.b13*m.b15 + 320*m.b8*m.b10*m.b14*m.b16 + 256*
                       m.b8*m.b10*m.b15*m.b17 + 192*m.b8*m.b10*m.b16*m.b18 + 128*m.b8*m.b10*m.b17*m.b19 + 64*m.b8*m.b10*
                       m.b18*m.b20 + 384*m.b8*m.b11*m.b12*m.b15 + 320*m.b8*m.b11*m.b13*m.b16 + 256*m.b8*m.b11*m.b14*
                       m.b17 + 192*m.b8*m.b11*m.b15*m.b18 + 128*m.b8*m.b11*m.b16*m.b19 + 64*m.b8*m.b11*m.b17*m.b20 + 256
                       *m.b8*m.b12*m.b13*m.b17 + 192*m.b8*m.b12*m.b14*m.b18 + 128*m.b8*m.b12*m.b15*m.b19 + 64*m.b8*m.b12
                       *m.b16*m.b20 + 128*m.b8*m.b13*m.b14*m.b19 + 64*m.b8*m.b13*m.b15*m.b20 + 384*m.b9*m.b10*m.b11*
                       m.b12 + 384*m.b9*m.b10*m.b12*m.b13 + 384*m.b9*m.b10*m.b13*m.b14 + 384*m.b9*m.b10*m.b14*m.b15 + 
                       320*m.b9*m.b10*m.b15*m.b16 + 256*m.b9*m.b10*m.b16*m.b17 + 192*m.b9*m.b10*m.b17*m.b18 + 128*m.b9*
                       m.b10*m.b18*m.b19 + 64*m.b9*m.b10*m.b19*m.b20 + 384*m.b9*m.b11*m.b12*m.b14 + 384*m.b9*m.b11*m.b13
                       *m.b15 + 320*m.b9*m.b11*m.b14*m.b16 + 256*m.b9*m.b11*m.b15*m.b17 + 192*m.b9*m.b11*m.b16*m.b18 + 
                       128*m.b9*m.b11*m.b17*m.b19 + 64*m.b9*m.b11*m.b18*m.b20 + 320*m.b9*m.b12*m.b13*m.b16 + 256*m.b9*
                       m.b12*m.b14*m.b17 + 192*m.b9*m.b12*m.b15*m.b18 + 128*m.b9*m.b12*m.b16*m.b19 + 64*m.b9*m.b12*m.b17
                       *m.b20 + 192*m.b9*m.b13*m.b14*m.b18 + 128*m.b9*m.b13*m.b15*m.b19 + 64*m.b9*m.b13*m.b16*m.b20 + 64
                       *m.b9*m.b14*m.b15*m.b20 + 384*m.b10*m.b11*m.b12*m.b13 + 384*m.b10*m.b11*m.b13*m.b14 + 384*m.b10*
                       m.b11*m.b14*m.b15 + 320*m.b10*m.b11*m.b15*m.b16 + 256*m.b10*m.b11*m.b16*m.b17 + 192*m.b10*m.b11*
                       m.b17*m.b18 + 128*m.b10*m.b11*m.b18*m.b19 + 64*m.b10*m.b11*m.b19*m.b20 + 384*m.b10*m.b12*m.b13*
                       m.b15 + 320*m.b10*m.b12*m.b14*m.b16 + 256*m.b10*m.b12*m.b15*m.b17 + 192*m.b10*m.b12*m.b16*m.b18
                        + 128*m.b10*m.b12*m.b17*m.b19 + 64*m.b10*m.b12*m.b18*m.b20 + 256*m.b10*m.b13*m.b14*m.b17 + 192*
                       m.b10*m.b13*m.b15*m.b18 + 128*m.b10*m.b13*m.b16*m.b19 + 64*m.b10*m.b13*m.b17*m.b20 + 128*m.b10*
                       m.b14*m.b15*m.b19 + 64*m.b10*m.b14*m.b16*m.b20 + 384*m.b11*m.b12*m.b13*m.b14 + 384*m.b11*m.b12*
                       m.b14*m.b15 + 320*m.b11*m.b12*m.b15*m.b16 + 256*m.b11*m.b12*m.b16*m.b17 + 192*m.b11*m.b12*m.b17*
                       m.b18 + 128*m.b11*m.b12*m.b18*m.b19 + 64*m.b11*m.b12*m.b19*m.b20 + 320*m.b11*m.b13*m.b14*m.b16 + 
                       256*m.b11*m.b13*m.b15*m.b17 + 192*m.b11*m.b13*m.b16*m.b18 + 128*m.b11*m.b13*m.b17*m.b19 + 64*
                       m.b11*m.b13*m.b18*m.b20 + 192*m.b11*m.b14*m.b15*m.b18 + 128*m.b11*m.b14*m.b16*m.b19 + 64*m.b11*
                       m.b14*m.b17*m.b20 + 64*m.b11*m.b15*m.b16*m.b20 + 384*m.b12*m.b13*m.b14*m.b15 + 320*m.b12*m.b13*
                       m.b15*m.b16 + 256*m.b12*m.b13*m.b16*m.b17 + 192*m.b12*m.b13*m.b17*m.b18 + 128*m.b12*m.b13*m.b18*
                       m.b19 + 64*m.b12*m.b13*m.b19*m.b20 + 256*m.b12*m.b14*m.b15*m.b17 + 192*m.b12*m.b14*m.b16*m.b18 + 
                       128*m.b12*m.b14*m.b17*m.b19 + 64*m.b12*m.b14*m.b18*m.b20 + 128*m.b12*m.b15*m.b16*m.b19 + 64*m.b12
                       *m.b15*m.b17*m.b20 + 320*m.b13*m.b14*m.b15*m.b16 + 256*m.b13*m.b14*m.b16*m.b17 + 192*m.b13*m.b14*
                       m.b17*m.b18 + 128*m.b13*m.b14*m.b18*m.b19 + 64*m.b13*m.b14*m.b19*m.b20 + 192*m.b13*m.b15*m.b16*
                       m.b18 + 128*m.b13*m.b15*m.b17*m.b19 + 64*m.b13*m.b15*m.b18*m.b20 + 64*m.b13*m.b16*m.b17*m.b20 + 
                       256*m.b14*m.b15*m.b16*m.b17 + 192*m.b14*m.b15*m.b17*m.b18 + 128*m.b14*m.b15*m.b18*m.b19 + 64*
                       m.b14*m.b15*m.b19*m.b20 + 128*m.b14*m.b16*m.b17*m.b19 + 64*m.b14*m.b16*m.b18*m.b20 + 192*m.b15*
                       m.b16*m.b17*m.b18 + 128*m.b15*m.b16*m.b18*m.b19 + 64*m.b15*m.b16*m.b19*m.b20 + 64*m.b15*m.b17*
                       m.b18*m.b20 + 128*m.b16*m.b17*m.b18*m.b19 + 64*m.b16*m.b17*m.b19*m.b20 + 64*m.b17*m.b18*m.b19*
                       m.b20 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*
                       m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*
                       m.b1*m.b2*m.b12 - 64*m.b1*m.b2*m.b13 - 64*m.b1*m.b2*m.b14 - 32*m.b1*m.b2*m.b15 - 64*m.b1*m.b3*
                       m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*
                       m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*m.b11 - 64*m.b1*m.b3*m.b12 - 64*m.b1*m.b3*m.b13 - 
                       32*m.b1*m.b3*m.b14 - 32*m.b1*m.b3*m.b15 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*
                       m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64*m.b1*
                       m.b4*m.b12 - 32*m.b1*m.b4*m.b13 - 32*m.b1*m.b4*m.b14 - 32*m.b1*m.b4*m.b15 - 64*m.b1*m.b5*m.b6 - 
                       64*m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 64*m.b1*m.b5*
                       m.b11 - 32*m.b1*m.b5*m.b12 - 32*m.b1*m.b5*m.b13 - 32*m.b1*m.b5*m.b14 - 32*m.b1*m.b5*m.b15 - 64*
                       m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10 - 32*m.b1*m.b6*m.b12
                        - 32*m.b1*m.b6*m.b13 - 32*m.b1*m.b6*m.b14 - 32*m.b1*m.b6*m.b15 - 64*m.b1*m.b7*m.b8 - 64*m.b1*
                       m.b7*m.b9 - 32*m.b1*m.b7*m.b10 - 32*m.b1*m.b7*m.b11 - 32*m.b1*m.b7*m.b12 - 32*m.b1*m.b7*m.b14 - 
                       32*m.b1*m.b7*m.b15 - 32*m.b1*m.b8*m.b9 - 32*m.b1*m.b8*m.b10 - 32*m.b1*m.b8*m.b11 - 32*m.b1*m.b8*
                       m.b12 - 32*m.b1*m.b8*m.b13 - 32*m.b1*m.b8*m.b14 - 32*m.b1*m.b9*m.b10 - 32*m.b1*m.b9*m.b11 - 32*
                       m.b1*m.b9*m.b12 - 32*m.b1*m.b9*m.b13 - 32*m.b1*m.b9*m.b14 - 32*m.b1*m.b9*m.b15 - 32*m.b1*m.b10*
                       m.b11 - 32*m.b1*m.b10*m.b12 - 32*m.b1*m.b10*m.b13 - 32*m.b1*m.b10*m.b14 - 32*m.b1*m.b10*m.b15 - 
                       32*m.b1*m.b11*m.b12 - 32*m.b1*m.b11*m.b13 - 32*m.b1*m.b11*m.b14 - 32*m.b1*m.b11*m.b15 - 32*m.b1*
                       m.b12*m.b13 - 32*m.b1*m.b12*m.b14 - 32*m.b1*m.b12*m.b15 - 32*m.b1*m.b13*m.b14 - 32*m.b1*m.b13*
                       m.b15 - 32*m.b1*m.b14*m.b15 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*
                       m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*
                       m.b11 - 128*m.b2*m.b3*m.b12 - 128*m.b2*m.b3*m.b13 - 128*m.b2*m.b3*m.b14 - 96*m.b2*m.b3*m.b15 - 32
                       *m.b2*m.b3*m.b16 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*
                       m.b8 - 128*m.b2*m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*m.b4*m.b11 - 128*m.b2*m.b4*m.b12 - 128
                       *m.b2*m.b4*m.b13 - 96*m.b2*m.b4*m.b14 - 64*m.b2*m.b4*m.b15 - 32*m.b2*m.b4*m.b16 - 160*m.b2*m.b5*
                       m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*m.b10 - 128*
                       m.b2*m.b5*m.b11 - 128*m.b2*m.b5*m.b12 - 96*m.b2*m.b5*m.b13 - 64*m.b2*m.b5*m.b14 - 64*m.b2*m.b5*
                       m.b15 - 32*m.b2*m.b5*m.b16 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*m.b8 - 128*m.b2*m.b6*m.b9 - 64*
                       m.b2*m.b6*m.b10 - 128*m.b2*m.b6*m.b11 - 96*m.b2*m.b6*m.b12 - 64*m.b2*m.b6*m.b13 - 64*m.b2*m.b6*
                       m.b14 - 64*m.b2*m.b6*m.b15 - 32*m.b2*m.b6*m.b16 - 160*m.b2*m.b7*m.b8 - 128*m.b2*m.b7*m.b9 - 128*
                       m.b2*m.b7*m.b10 - 96*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b13 - 64*m.b2*m.b7*m.b14 - 64*m.b2*m.b7*
                       m.b15 - 32*m.b2*m.b7*m.b16 - 160*m.b2*m.b8*m.b9 - 96*m.b2*m.b8*m.b10 - 64*m.b2*m.b8*m.b11 - 64*
                       m.b2*m.b8*m.b12 - 64*m.b2*m.b8*m.b13 - 64*m.b2*m.b8*m.b15 - 32*m.b2*m.b8*m.b16 - 96*m.b2*m.b9*
                       m.b10 - 64*m.b2*m.b9*m.b11 - 64*m.b2*m.b9*m.b12 - 64*m.b2*m.b9*m.b13 - 64*m.b2*m.b9*m.b14 - 64*
                       m.b2*m.b9*m.b15 - 96*m.b2*m.b10*m.b11 - 64*m.b2*m.b10*m.b12 - 64*m.b2*m.b10*m.b13 - 64*m.b2*m.b10
                       *m.b14 - 64*m.b2*m.b10*m.b15 - 32*m.b2*m.b10*m.b16 - 96*m.b2*m.b11*m.b12 - 64*m.b2*m.b11*m.b13 - 
                       64*m.b2*m.b11*m.b14 - 64*m.b2*m.b11*m.b15 - 32*m.b2*m.b11*m.b16 - 96*m.b2*m.b12*m.b13 - 64*m.b2*
                       m.b12*m.b14 - 64*m.b2*m.b12*m.b15 - 32*m.b2*m.b12*m.b16 - 96*m.b2*m.b13*m.b14 - 64*m.b2*m.b13*
                       m.b15 - 32*m.b2*m.b13*m.b16 - 96*m.b2*m.b14*m.b15 - 32*m.b2*m.b14*m.b16 - 32*m.b2*m.b15*m.b16 - 
                       160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4
                       *m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*m.b12 - 192*m.b3*m.b4*m.b13 - 
                       192*m.b3*m.b4*m.b14 - 160*m.b3*m.b4*m.b15 - 96*m.b3*m.b4*m.b16 - 32*m.b3*m.b4*m.b17 - 256*m.b3*
                       m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*m.b10 - 
                       192*m.b3*m.b5*m.b11 - 192*m.b3*m.b5*m.b12 - 192*m.b3*m.b5*m.b13 - 160*m.b3*m.b5*m.b14 - 128*m.b3*
                       m.b5*m.b15 - 64*m.b3*m.b5*m.b16 - 32*m.b3*m.b5*m.b17 - 256*m.b3*m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 
                       96*m.b3*m.b6*m.b9 - 192*m.b3*m.b6*m.b10 - 192*m.b3*m.b6*m.b11 - 192*m.b3*m.b6*m.b12 - 160*m.b3*
                       m.b6*m.b13 - 128*m.b3*m.b6*m.b14 - 96*m.b3*m.b6*m.b15 - 64*m.b3*m.b6*m.b16 - 32*m.b3*m.b6*m.b17
                        - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 192*m.b3*m.b7*m.b10 - 96*m.b3*m.b7*m.b11 - 160*m.b3*
                       m.b7*m.b12 - 128*m.b3*m.b7*m.b13 - 96*m.b3*m.b7*m.b14 - 96*m.b3*m.b7*m.b15 - 64*m.b3*m.b7*m.b16
                        - 32*m.b3*m.b7*m.b17 - 256*m.b3*m.b8*m.b9 - 224*m.b3*m.b8*m.b10 - 160*m.b3*m.b8*m.b11 - 128*m.b3
                       *m.b8*m.b12 - 96*m.b3*m.b8*m.b14 - 96*m.b3*m.b8*m.b15 - 64*m.b3*m.b8*m.b16 - 32*m.b3*m.b8*m.b17
                        - 224*m.b3*m.b9*m.b10 - 160*m.b3*m.b9*m.b11 - 96*m.b3*m.b9*m.b12 - 96*m.b3*m.b9*m.b13 - 96*m.b3*
                       m.b9*m.b14 - 64*m.b3*m.b9*m.b16 - 32*m.b3*m.b9*m.b17 - 160*m.b3*m.b10*m.b11 - 128*m.b3*m.b10*
                       m.b12 - 96*m.b3*m.b10*m.b13 - 96*m.b3*m.b10*m.b14 - 96*m.b3*m.b10*m.b15 - 64*m.b3*m.b10*m.b16 - 
                       160*m.b3*m.b11*m.b12 - 128*m.b3*m.b11*m.b13 - 96*m.b3*m.b11*m.b14 - 96*m.b3*m.b11*m.b15 - 64*m.b3
                       *m.b11*m.b16 - 32*m.b3*m.b11*m.b17 - 160*m.b3*m.b12*m.b13 - 128*m.b3*m.b12*m.b14 - 96*m.b3*m.b12*
                       m.b15 - 64*m.b3*m.b12*m.b16 - 32*m.b3*m.b12*m.b17 - 160*m.b3*m.b13*m.b14 - 128*m.b3*m.b13*m.b15
                        - 64*m.b3*m.b13*m.b16 - 32*m.b3*m.b13*m.b17 - 160*m.b3*m.b14*m.b15 - 64*m.b3*m.b14*m.b16 - 32*
                       m.b3*m.b14*m.b17 - 96*m.b3*m.b15*m.b16 - 32*m.b3*m.b15*m.b17 - 32*m.b3*m.b16*m.b17 - 224*m.b4*
                       m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 
                       256*m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 256*m.b4*m.b5*m.b13 - 256*m.b4*m.b5*m.b14 - 224*m.b4*
                       m.b5*m.b15 - 160*m.b4*m.b5*m.b16 - 96*m.b4*m.b5*m.b17 - 32*m.b4*m.b5*m.b18 - 352*m.b4*m.b6*m.b7
                        - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10 - 256*m.b4*m.b6*m.b11 - 256*m.b4
                       *m.b6*m.b12 - 256*m.b4*m.b6*m.b13 - 224*m.b4*m.b6*m.b14 - 192*m.b4*m.b6*m.b15 - 128*m.b4*m.b6*
                       m.b16 - 64*m.b4*m.b6*m.b17 - 32*m.b4*m.b6*m.b18 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*
                       m.b4*m.b7*m.b10 - 256*m.b4*m.b7*m.b11 - 256*m.b4*m.b7*m.b12 - 224*m.b4*m.b7*m.b13 - 192*m.b4*m.b7
                       *m.b14 - 160*m.b4*m.b7*m.b15 - 96*m.b4*m.b7*m.b16 - 64*m.b4*m.b7*m.b17 - 32*m.b4*m.b7*m.b18 - 352
                       *m.b4*m.b8*m.b9 - 320*m.b4*m.b8*m.b10 - 288*m.b4*m.b8*m.b11 - 96*m.b4*m.b8*m.b12 - 192*m.b4*m.b8*
                       m.b13 - 160*m.b4*m.b8*m.b14 - 128*m.b4*m.b8*m.b15 - 96*m.b4*m.b8*m.b16 - 64*m.b4*m.b8*m.b17 - 32*
                       m.b4*m.b8*m.b18 - 352*m.b4*m.b9*m.b10 - 288*m.b4*m.b9*m.b11 - 224*m.b4*m.b9*m.b12 - 160*m.b4*m.b9
                       *m.b13 - 128*m.b4*m.b9*m.b15 - 96*m.b4*m.b9*m.b16 - 64*m.b4*m.b9*m.b17 - 32*m.b4*m.b9*m.b18 - 288
                       *m.b4*m.b10*m.b11 - 224*m.b4*m.b10*m.b12 - 160*m.b4*m.b10*m.b13 - 128*m.b4*m.b10*m.b14 - 128*m.b4
                       *m.b10*m.b15 - 64*m.b4*m.b10*m.b17 - 32*m.b4*m.b10*m.b18 - 224*m.b4*m.b11*m.b12 - 192*m.b4*m.b11*
                       m.b13 - 160*m.b4*m.b11*m.b14 - 128*m.b4*m.b11*m.b15 - 96*m.b4*m.b11*m.b16 - 64*m.b4*m.b11*m.b17
                        - 224*m.b4*m.b12*m.b13 - 192*m.b4*m.b12*m.b14 - 160*m.b4*m.b12*m.b15 - 96*m.b4*m.b12*m.b16 - 64*
                       m.b4*m.b12*m.b17 - 32*m.b4*m.b12*m.b18 - 224*m.b4*m.b13*m.b14 - 192*m.b4*m.b13*m.b15 - 96*m.b4*
                       m.b13*m.b16 - 64*m.b4*m.b13*m.b17 - 32*m.b4*m.b13*m.b18 - 224*m.b4*m.b14*m.b15 - 128*m.b4*m.b14*
                       m.b16 - 64*m.b4*m.b14*m.b17 - 32*m.b4*m.b14*m.b18 - 160*m.b4*m.b15*m.b16 - 64*m.b4*m.b15*m.b17 - 
                       32*m.b4*m.b15*m.b18 - 96*m.b4*m.b16*m.b17 - 32*m.b4*m.b16*m.b18 - 32*m.b4*m.b17*m.b18 - 288*m.b5*
                       m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*m.b5*m.b6*m.b11
                        - 320*m.b5*m.b6*m.b12 - 320*m.b5*m.b6*m.b13 - 320*m.b5*m.b6*m.b14 - 288*m.b5*m.b6*m.b15 - 224*
                       m.b5*m.b6*m.b16 - 160*m.b5*m.b6*m.b17 - 96*m.b5*m.b6*m.b18 - 32*m.b5*m.b6*m.b19 - 448*m.b5*m.b7*
                       m.b8 - 256*m.b5*m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*m.b5*m.b7*m.b11 - 320*m.b5*m.b7*m.b12 - 320
                       *m.b5*m.b7*m.b13 - 288*m.b5*m.b7*m.b14 - 256*m.b5*m.b7*m.b15 - 192*m.b5*m.b7*m.b16 - 128*m.b5*
                       m.b7*m.b17 - 64*m.b5*m.b7*m.b18 - 32*m.b5*m.b7*m.b19 - 448*m.b5*m.b8*m.b9 - 416*m.b5*m.b8*m.b10
                        - 224*m.b5*m.b8*m.b11 - 352*m.b5*m.b8*m.b12 - 288*m.b5*m.b8*m.b13 - 256*m.b5*m.b8*m.b14 - 224*
                       m.b5*m.b8*m.b15 - 160*m.b5*m.b8*m.b16 - 96*m.b5*m.b8*m.b17 - 64*m.b5*m.b8*m.b18 - 32*m.b5*m.b8*
                       m.b19 - 448*m.b5*m.b9*m.b10 - 416*m.b5*m.b9*m.b11 - 352*m.b5*m.b9*m.b12 - 128*m.b5*m.b9*m.b13 - 
                       224*m.b5*m.b9*m.b14 - 192*m.b5*m.b9*m.b15 - 128*m.b5*m.b9*m.b16 - 96*m.b5*m.b9*m.b17 - 64*m.b5*
                       m.b9*m.b18 - 32*m.b5*m.b9*m.b19 - 416*m.b5*m.b10*m.b11 - 352*m.b5*m.b10*m.b12 - 288*m.b5*m.b10*
                       m.b13 - 224*m.b5*m.b10*m.b14 - 128*m.b5*m.b10*m.b16 - 96*m.b5*m.b10*m.b17 - 64*m.b5*m.b10*m.b18
                        - 32*m.b5*m.b10*m.b19 - 352*m.b5*m.b11*m.b12 - 288*m.b5*m.b11*m.b13 - 224*m.b5*m.b11*m.b14 - 192
                       *m.b5*m.b11*m.b15 - 128*m.b5*m.b11*m.b16 - 64*m.b5*m.b11*m.b18 - 32*m.b5*m.b11*m.b19 - 288*m.b5*
                       m.b12*m.b13 - 256*m.b5*m.b12*m.b14 - 224*m.b5*m.b12*m.b15 - 128*m.b5*m.b12*m.b16 - 96*m.b5*m.b12*
                       m.b17 - 64*m.b5*m.b12*m.b18 - 288*m.b5*m.b13*m.b14 - 256*m.b5*m.b13*m.b15 - 160*m.b5*m.b13*m.b16
                        - 96*m.b5*m.b13*m.b17 - 64*m.b5*m.b13*m.b18 - 32*m.b5*m.b13*m.b19 - 288*m.b5*m.b14*m.b15 - 192*
                       m.b5*m.b14*m.b16 - 96*m.b5*m.b14*m.b17 - 64*m.b5*m.b14*m.b18 - 32*m.b5*m.b14*m.b19 - 224*m.b5*
                       m.b15*m.b16 - 128*m.b5*m.b15*m.b17 - 64*m.b5*m.b15*m.b18 - 32*m.b5*m.b15*m.b19 - 160*m.b5*m.b16*
                       m.b17 - 64*m.b5*m.b16*m.b18 - 32*m.b5*m.b16*m.b19 - 96*m.b5*m.b17*m.b18 - 32*m.b5*m.b17*m.b19 - 
                       32*m.b5*m.b18*m.b19 - 352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*
                       m.b7*m.b11 - 416*m.b6*m.b7*m.b12 - 384*m.b6*m.b7*m.b13 - 384*m.b6*m.b7*m.b14 - 352*m.b6*m.b7*
                       m.b15 - 288*m.b6*m.b7*m.b16 - 224*m.b6*m.b7*m.b17 - 160*m.b6*m.b7*m.b18 - 96*m.b6*m.b7*m.b19 - 32
                       *m.b6*m.b7*m.b20 - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10 - 480*m.b6*m.b8*m.b11 - 448*m.b6*m.b8
                       *m.b12 - 416*m.b6*m.b8*m.b13 - 352*m.b6*m.b8*m.b14 - 320*m.b6*m.b8*m.b15 - 256*m.b6*m.b8*m.b16 - 
                       192*m.b6*m.b8*m.b17 - 128*m.b6*m.b8*m.b18 - 64*m.b6*m.b8*m.b19 - 32*m.b6*m.b8*m.b20 - 544*m.b6*
                       m.b9*m.b10 - 512*m.b6*m.b9*m.b11 - 288*m.b6*m.b9*m.b12 - 416*m.b6*m.b9*m.b13 - 352*m.b6*m.b9*
                       m.b14 - 288*m.b6*m.b9*m.b15 - 224*m.b6*m.b9*m.b16 - 160*m.b6*m.b9*m.b17 - 96*m.b6*m.b9*m.b18 - 64
                       *m.b6*m.b9*m.b19 - 32*m.b6*m.b9*m.b20 - 544*m.b6*m.b10*m.b11 - 480*m.b6*m.b10*m.b12 - 416*m.b6*
                       m.b10*m.b13 - 160*m.b6*m.b10*m.b14 - 288*m.b6*m.b10*m.b15 - 192*m.b6*m.b10*m.b16 - 128*m.b6*m.b10
                       *m.b17 - 96*m.b6*m.b10*m.b18 - 64*m.b6*m.b10*m.b19 - 32*m.b6*m.b10*m.b20 - 480*m.b6*m.b11*m.b12
                        - 416*m.b6*m.b11*m.b13 - 352*m.b6*m.b11*m.b14 - 288*m.b6*m.b11*m.b15 - 128*m.b6*m.b11*m.b17 - 96
                       *m.b6*m.b11*m.b18 - 64*m.b6*m.b11*m.b19 - 32*m.b6*m.b11*m.b20 - 416*m.b6*m.b12*m.b13 - 352*m.b6*
                       m.b12*m.b14 - 288*m.b6*m.b12*m.b15 - 192*m.b6*m.b12*m.b16 - 128*m.b6*m.b12*m.b17 - 64*m.b6*m.b12*
                       m.b19 - 32*m.b6*m.b12*m.b20 - 352*m.b6*m.b13*m.b14 - 320*m.b6*m.b13*m.b15 - 224*m.b6*m.b13*m.b16
                        - 128*m.b6*m.b13*m.b17 - 96*m.b6*m.b13*m.b18 - 64*m.b6*m.b13*m.b19 - 352*m.b6*m.b14*m.b15 - 256*
                       m.b6*m.b14*m.b16 - 160*m.b6*m.b14*m.b17 - 96*m.b6*m.b14*m.b18 - 64*m.b6*m.b14*m.b19 - 32*m.b6*
                       m.b14*m.b20 - 288*m.b6*m.b15*m.b16 - 192*m.b6*m.b15*m.b17 - 96*m.b6*m.b15*m.b18 - 64*m.b6*m.b15*
                       m.b19 - 32*m.b6*m.b15*m.b20 - 224*m.b6*m.b16*m.b17 - 128*m.b6*m.b16*m.b18 - 64*m.b6*m.b16*m.b19
                        - 32*m.b6*m.b16*m.b20 - 160*m.b6*m.b17*m.b18 - 64*m.b6*m.b17*m.b19 - 32*m.b6*m.b17*m.b20 - 96*
                       m.b6*m.b18*m.b19 - 32*m.b6*m.b18*m.b20 - 32*m.b6*m.b19*m.b20 - 384*m.b7*m.b8*m.b9 - 544*m.b7*m.b8
                       *m.b10 - 512*m.b7*m.b8*m.b11 - 512*m.b7*m.b8*m.b12 - 512*m.b7*m.b8*m.b13 - 448*m.b7*m.b8*m.b14 - 
                       352*m.b7*m.b8*m.b15 - 288*m.b7*m.b8*m.b16 - 224*m.b7*m.b8*m.b17 - 160*m.b7*m.b8*m.b18 - 96*m.b7*
                       m.b8*m.b19 - 32*m.b7*m.b8*m.b20 - 576*m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 544*m.b7*m.b9*m.b12
                        - 512*m.b7*m.b9*m.b13 - 448*m.b7*m.b9*m.b14 - 352*m.b7*m.b9*m.b15 - 256*m.b7*m.b9*m.b16 - 192*
                       m.b7*m.b9*m.b17 - 128*m.b7*m.b9*m.b18 - 64*m.b7*m.b9*m.b19 - 32*m.b7*m.b9*m.b20 - 608*m.b7*m.b10*
                       m.b11 - 544*m.b7*m.b10*m.b12 - 288*m.b7*m.b10*m.b13 - 448*m.b7*m.b10*m.b14 - 352*m.b7*m.b10*m.b15
                        - 224*m.b7*m.b10*m.b16 - 160*m.b7*m.b10*m.b17 - 96*m.b7*m.b10*m.b18 - 64*m.b7*m.b10*m.b19 - 32*
                       m.b7*m.b10*m.b20 - 544*m.b7*m.b11*m.b12 - 512*m.b7*m.b11*m.b13 - 448*m.b7*m.b11*m.b14 - 160*m.b7*
                       m.b11*m.b15 - 224*m.b7*m.b11*m.b16 - 128*m.b7*m.b11*m.b17 - 96*m.b7*m.b11*m.b18 - 64*m.b7*m.b11*
                       m.b19 - 32*m.b7*m.b11*m.b20 - 512*m.b7*m.b12*m.b13 - 448*m.b7*m.b12*m.b14 - 352*m.b7*m.b12*m.b15
                        - 224*m.b7*m.b12*m.b16 - 96*m.b7*m.b12*m.b18 - 64*m.b7*m.b12*m.b19 - 32*m.b7*m.b12*m.b20 - 448*
                       m.b7*m.b13*m.b14 - 352*m.b7*m.b13*m.b15 - 256*m.b7*m.b13*m.b16 - 160*m.b7*m.b13*m.b17 - 96*m.b7*
                       m.b13*m.b18 - 32*m.b7*m.b13*m.b20 - 384*m.b7*m.b14*m.b15 - 288*m.b7*m.b14*m.b16 - 192*m.b7*m.b14*
                       m.b17 - 96*m.b7*m.b14*m.b18 - 64*m.b7*m.b14*m.b19 - 32*m.b7*m.b14*m.b20 - 320*m.b7*m.b15*m.b16 - 
                       224*m.b7*m.b15*m.b17 - 128*m.b7*m.b15*m.b18 - 64*m.b7*m.b15*m.b19 - 32*m.b7*m.b15*m.b20 - 256*
                       m.b7*m.b16*m.b17 - 160*m.b7*m.b16*m.b18 - 64*m.b7*m.b16*m.b19 - 32*m.b7*m.b16*m.b20 - 192*m.b7*
                       m.b17*m.b18 - 96*m.b7*m.b17*m.b19 - 32*m.b7*m.b17*m.b20 - 128*m.b7*m.b18*m.b19 - 32*m.b7*m.b18*
                       m.b20 - 64*m.b7*m.b19*m.b20 - 384*m.b8*m.b9*m.b10 - 576*m.b8*m.b9*m.b11 - 544*m.b8*m.b9*m.b12 - 
                       544*m.b8*m.b9*m.b13 - 512*m.b8*m.b9*m.b14 - 416*m.b8*m.b9*m.b15 - 288*m.b8*m.b9*m.b16 - 224*m.b8*
                       m.b9*m.b17 - 160*m.b8*m.b9*m.b18 - 96*m.b8*m.b9*m.b19 - 32*m.b8*m.b9*m.b20 - 576*m.b8*m.b10*m.b11
                        - 416*m.b8*m.b10*m.b12 - 544*m.b8*m.b10*m.b13 - 512*m.b8*m.b10*m.b14 - 416*m.b8*m.b10*m.b15 - 
                       288*m.b8*m.b10*m.b16 - 192*m.b8*m.b10*m.b17 - 128*m.b8*m.b10*m.b18 - 64*m.b8*m.b10*m.b19 - 32*
                       m.b8*m.b10*m.b20 - 576*m.b8*m.b11*m.b12 - 544*m.b8*m.b11*m.b13 - 288*m.b8*m.b11*m.b14 - 416*m.b8*
                       m.b11*m.b15 - 288*m.b8*m.b11*m.b16 - 160*m.b8*m.b11*m.b17 - 96*m.b8*m.b11*m.b18 - 64*m.b8*m.b11*
                       m.b19 - 32*m.b8*m.b11*m.b20 - 544*m.b8*m.b12*m.b13 - 512*m.b8*m.b12*m.b14 - 416*m.b8*m.b12*m.b15
                        - 128*m.b8*m.b12*m.b16 - 160*m.b8*m.b12*m.b17 - 96*m.b8*m.b12*m.b18 - 64*m.b8*m.b12*m.b19 - 32*
                       m.b8*m.b12*m.b20 - 512*m.b8*m.b13*m.b14 - 416*m.b8*m.b13*m.b15 - 288*m.b8*m.b13*m.b16 - 192*m.b8*
                       m.b13*m.b17 - 64*m.b8*m.b13*m.b19 - 32*m.b8*m.b13*m.b20 - 384*m.b8*m.b14*m.b15 - 320*m.b8*m.b14*
                       m.b16 - 224*m.b8*m.b14*m.b17 - 128*m.b8*m.b14*m.b18 - 64*m.b8*m.b14*m.b19 - 320*m.b8*m.b15*m.b16
                        - 256*m.b8*m.b15*m.b17 - 160*m.b8*m.b15*m.b18 - 64*m.b8*m.b15*m.b19 - 32*m.b8*m.b15*m.b20 - 256*
                       m.b8*m.b16*m.b17 - 192*m.b8*m.b16*m.b18 - 96*m.b8*m.b16*m.b19 - 32*m.b8*m.b16*m.b20 - 192*m.b8*
                       m.b17*m.b18 - 128*m.b8*m.b17*m.b19 - 32*m.b8*m.b17*m.b20 - 128*m.b8*m.b18*m.b19 - 64*m.b8*m.b18*
                       m.b20 - 64*m.b8*m.b19*m.b20 - 384*m.b9*m.b10*m.b11 - 576*m.b9*m.b10*m.b12 - 576*m.b9*m.b10*m.b13
                        - 544*m.b9*m.b10*m.b14 - 480*m.b9*m.b10*m.b15 - 352*m.b9*m.b10*m.b16 - 224*m.b9*m.b10*m.b17 - 
                       160*m.b9*m.b10*m.b18 - 96*m.b9*m.b10*m.b19 - 32*m.b9*m.b10*m.b20 - 576*m.b9*m.b11*m.b12 - 416*
                       m.b9*m.b11*m.b13 - 544*m.b9*m.b11*m.b14 - 480*m.b9*m.b11*m.b15 - 352*m.b9*m.b11*m.b16 - 224*m.b9*
                       m.b11*m.b17 - 128*m.b9*m.b11*m.b18 - 64*m.b9*m.b11*m.b19 - 32*m.b9*m.b11*m.b20 - 544*m.b9*m.b12*
                       m.b13 - 544*m.b9*m.b12*m.b14 - 288*m.b9*m.b12*m.b15 - 352*m.b9*m.b12*m.b16 - 224*m.b9*m.b12*m.b17
                        - 96*m.b9*m.b12*m.b18 - 64*m.b9*m.b12*m.b19 - 32*m.b9*m.b12*m.b20 - 512*m.b9*m.b13*m.b14 - 448*
                       m.b9*m.b13*m.b15 - 352*m.b9*m.b13*m.b16 - 96*m.b9*m.b13*m.b17 - 128*m.b9*m.b13*m.b18 - 64*m.b9*
                       m.b13*m.b19 - 32*m.b9*m.b13*m.b20 - 416*m.b9*m.b14*m.b15 - 320*m.b9*m.b14*m.b16 - 256*m.b9*m.b14*
                       m.b17 - 160*m.b9*m.b14*m.b18 - 32*m.b9*m.b14*m.b20 - 320*m.b9*m.b15*m.b16 - 256*m.b9*m.b15*m.b17
                        - 192*m.b9*m.b15*m.b18 - 96*m.b9*m.b15*m.b19 - 32*m.b9*m.b15*m.b20 - 256*m.b9*m.b16*m.b17 - 192*
                       m.b9*m.b16*m.b18 - 128*m.b9*m.b16*m.b19 - 32*m.b9*m.b16*m.b20 - 192*m.b9*m.b17*m.b18 - 128*m.b9*
                       m.b17*m.b19 - 64*m.b9*m.b17*m.b20 - 128*m.b9*m.b18*m.b19 - 64*m.b9*m.b18*m.b20 - 64*m.b9*m.b19*
                       m.b20 - 384*m.b10*m.b11*m.b12 - 576*m.b10*m.b11*m.b13 - 608*m.b10*m.b11*m.b14 - 544*m.b10*m.b11*
                       m.b15 - 416*m.b10*m.b11*m.b16 - 288*m.b10*m.b11*m.b17 - 160*m.b10*m.b11*m.b18 - 96*m.b10*m.b11*
                       m.b19 - 32*m.b10*m.b11*m.b20 - 576*m.b10*m.b12*m.b13 - 384*m.b10*m.b12*m.b14 - 512*m.b10*m.b12*
                       m.b15 - 416*m.b10*m.b12*m.b16 - 288*m.b10*m.b12*m.b17 - 160*m.b10*m.b12*m.b18 - 64*m.b10*m.b12*
                       m.b19 - 32*m.b10*m.b12*m.b20 - 512*m.b10*m.b13*m.b14 - 480*m.b10*m.b13*m.b15 - 224*m.b10*m.b13*
                       m.b16 - 288*m.b10*m.b13*m.b17 - 160*m.b10*m.b13*m.b18 - 64*m.b10*m.b13*m.b19 - 32*m.b10*m.b13*
                       m.b20 - 448*m.b10*m.b14*m.b15 - 352*m.b10*m.b14*m.b16 - 256*m.b10*m.b14*m.b17 - 96*m.b10*m.b14*
                       m.b18 - 96*m.b10*m.b14*m.b19 - 32*m.b10*m.b14*m.b20 - 320*m.b10*m.b15*m.b16 - 256*m.b10*m.b15*
                       m.b17 - 192*m.b10*m.b15*m.b18 - 128*m.b10*m.b15*m.b19 - 256*m.b10*m.b16*m.b17 - 192*m.b10*m.b16*
                       m.b18 - 128*m.b10*m.b16*m.b19 - 64*m.b10*m.b16*m.b20 - 192*m.b10*m.b17*m.b18 - 128*m.b10*m.b17*
                       m.b19 - 64*m.b10*m.b17*m.b20 - 128*m.b10*m.b18*m.b19 - 64*m.b10*m.b18*m.b20 - 64*m.b10*m.b19*
                       m.b20 - 384*m.b11*m.b12*m.b13 - 576*m.b11*m.b12*m.b14 - 544*m.b11*m.b12*m.b15 - 448*m.b11*m.b12*
                       m.b16 - 352*m.b11*m.b12*m.b17 - 224*m.b11*m.b12*m.b18 - 96*m.b11*m.b12*m.b19 - 32*m.b11*m.b12*
                       m.b20 - 544*m.b11*m.b13*m.b14 - 320*m.b11*m.b13*m.b15 - 416*m.b11*m.b13*m.b16 - 320*m.b11*m.b13*
                       m.b17 - 224*m.b11*m.b13*m.b18 - 96*m.b11*m.b13*m.b19 - 32*m.b11*m.b13*m.b20 - 480*m.b11*m.b14*
                       m.b15 - 384*m.b11*m.b14*m.b16 - 160*m.b11*m.b14*m.b17 - 192*m.b11*m.b14*m.b18 - 128*m.b11*m.b14*
                       m.b19 - 32*m.b11*m.b14*m.b20 - 352*m.b11*m.b15*m.b16 - 256*m.b11*m.b15*m.b17 - 192*m.b11*m.b15*
                       m.b18 - 64*m.b11*m.b15*m.b19 - 64*m.b11*m.b15*m.b20 - 256*m.b11*m.b16*m.b17 - 192*m.b11*m.b16*
                       m.b18 - 128*m.b11*m.b16*m.b19 - 64*m.b11*m.b16*m.b20 - 192*m.b11*m.b17*m.b18 - 128*m.b11*m.b17*
                       m.b19 - 64*m.b11*m.b17*m.b20 - 128*m.b11*m.b18*m.b19 - 64*m.b11*m.b18*m.b20 - 64*m.b11*m.b19*
                       m.b20 - 384*m.b12*m.b13*m.b14 - 544*m.b12*m.b13*m.b15 - 448*m.b12*m.b13*m.b16 - 352*m.b12*m.b13*
                       m.b17 - 256*m.b12*m.b13*m.b18 - 160*m.b12*m.b13*m.b19 - 32*m.b12*m.b13*m.b20 - 512*m.b12*m.b14*
                       m.b15 - 256*m.b12*m.b14*m.b16 - 320*m.b12*m.b14*m.b17 - 224*m.b12*m.b14*m.b18 - 128*m.b12*m.b14*
                       m.b19 - 64*m.b12*m.b14*m.b20 - 384*m.b12*m.b15*m.b16 - 288*m.b12*m.b15*m.b17 - 96*m.b12*m.b15*
                       m.b18 - 128*m.b12*m.b15*m.b19 - 64*m.b12*m.b15*m.b20 - 256*m.b12*m.b16*m.b17 - 192*m.b12*m.b16*
                       m.b18 - 128*m.b12*m.b16*m.b19 - 32*m.b12*m.b16*m.b20 - 192*m.b12*m.b17*m.b18 - 128*m.b12*m.b17*
                       m.b19 - 64*m.b12*m.b17*m.b20 - 128*m.b12*m.b18*m.b19 - 64*m.b12*m.b18*m.b20 - 64*m.b12*m.b19*
                       m.b20 - 352*m.b13*m.b14*m.b15 - 448*m.b13*m.b14*m.b16 - 352*m.b13*m.b14*m.b17 - 256*m.b13*m.b14*
                       m.b18 - 160*m.b13*m.b14*m.b19 - 64*m.b13*m.b14*m.b20 - 416*m.b13*m.b15*m.b16 - 192*m.b13*m.b15*
                       m.b17 - 224*m.b13*m.b15*m.b18 - 128*m.b13*m.b15*m.b19 - 64*m.b13*m.b15*m.b20 - 288*m.b13*m.b16*
                       m.b17 - 192*m.b13*m.b16*m.b18 - 64*m.b13*m.b16*m.b19 - 64*m.b13*m.b16*m.b20 - 192*m.b13*m.b17*
                       m.b18 - 128*m.b13*m.b17*m.b19 - 64*m.b13*m.b17*m.b20 - 128*m.b13*m.b18*m.b19 - 64*m.b13*m.b18*
                       m.b20 - 64*m.b13*m.b19*m.b20 - 288*m.b14*m.b15*m.b16 - 352*m.b14*m.b15*m.b17 - 256*m.b14*m.b15*
                       m.b18 - 160*m.b14*m.b15*m.b19 - 64*m.b14*m.b15*m.b20 - 320*m.b14*m.b16*m.b17 - 128*m.b14*m.b16*
                       m.b18 - 128*m.b14*m.b16*m.b19 - 64*m.b14*m.b16*m.b20 - 192*m.b14*m.b17*m.b18 - 128*m.b14*m.b17*
                       m.b19 - 32*m.b14*m.b17*m.b20 - 128*m.b14*m.b18*m.b19 - 64*m.b14*m.b18*m.b20 - 64*m.b14*m.b19*
                       m.b20 - 224*m.b15*m.b16*m.b17 - 256*m.b15*m.b16*m.b18 - 160*m.b15*m.b16*m.b19 - 64*m.b15*m.b16*
                       m.b20 - 224*m.b15*m.b17*m.b18 - 64*m.b15*m.b17*m.b19 - 64*m.b15*m.b17*m.b20 - 128*m.b15*m.b18*
                       m.b19 - 64*m.b15*m.b18*m.b20 - 64*m.b15*m.b19*m.b20 - 160*m.b16*m.b17*m.b18 - 160*m.b16*m.b17*
                       m.b19 - 64*m.b16*m.b17*m.b20 - 128*m.b16*m.b18*m.b19 - 32*m.b16*m.b18*m.b20 - 64*m.b16*m.b19*
                       m.b20 - 96*m.b17*m.b18*m.b19 - 64*m.b17*m.b18*m.b20 - 64*m.b17*m.b19*m.b20 - 32*m.b18*m.b19*m.b20
                        + 192*m.b1*m.b2 + 184*m.b1*m.b3 + 176*m.b1*m.b4 + 168*m.b1*m.b5 + 160*m.b1*m.b6 + 152*m.b1*m.b7
                        + 144*m.b1*m.b8 + 152*m.b1*m.b9 + 144*m.b1*m.b10 + 136*m.b1*m.b11 + 128*m.b1*m.b12 + 120*m.b1*
                       m.b13 + 112*m.b1*m.b14 + 104*m.b1*m.b15 + 384*m.b2*m.b3 + 384*m.b2*m.b4 + 368*m.b2*m.b5 + 352*
                       m.b2*m.b6 + 336*m.b2*m.b7 + 320*m.b2*m.b8 + 320*m.b2*m.b9 + 320*m.b2*m.b10 + 304*m.b2*m.b11 + 288
                       *m.b2*m.b12 + 272*m.b2*m.b13 + 256*m.b2*m.b14 + 224*m.b2*m.b15 + 104*m.b2*m.b16 + 592*m.b3*m.b4
                        + 584*m.b3*m.b5 + 576*m.b3*m.b6 + 552*m.b3*m.b7 + 528*m.b3*m.b8 + 504*m.b3*m.b9 + 512*m.b3*m.b10
                        + 504*m.b3*m.b11 + 480*m.b3*m.b12 + 456*m.b3*m.b13 + 416*m.b3*m.b14 + 376*m.b3*m.b15 + 224*m.b3*
                       m.b16 + 104*m.b3*m.b17 + 816*m.b4*m.b5 + 800*m.b4*m.b6 + 784*m.b4*m.b7 + 768*m.b4*m.b8 + 736*m.b4
                       *m.b9 + 720*m.b4*m.b10 + 720*m.b4*m.b11 + 704*m.b4*m.b12 + 656*m.b4*m.b13 + 608*m.b4*m.b14 + 544*
                       m.b4*m.b15 + 376*m.b4*m.b16 + 224*m.b4*m.b17 + 104*m.b4*m.b18 + 1056*m.b5*m.b6 + 1032*m.b5*m.b7
                        + 1008*m.b5*m.b8 + 984*m.b5*m.b9 + 960*m.b5*m.b10 + 952*m.b5*m.b11 + 928*m.b5*m.b12 + 888*m.b5*
                       m.b13 + 816*m.b5*m.b14 + 744*m.b5*m.b15 + 544*m.b5*m.b16 + 376*m.b5*m.b17 + 224*m.b5*m.b18 + 104*
                       m.b5*m.b19 + 1312*m.b6*m.b7 + 1280*m.b6*m.b8 + 1248*m.b6*m.b9 + 1216*m.b6*m.b10 + 1184*m.b6*m.b11
                        + 1168*m.b6*m.b12 + 1120*m.b6*m.b13 + 1056*m.b6*m.b14 + 960*m.b6*m.b15 + 744*m.b6*m.b16 + 544*
                       m.b6*m.b17 + 376*m.b6*m.b18 + 224*m.b6*m.b19 + 104*m.b6*m.b20 + 1424*m.b7*m.b8 + 1392*m.b7*m.b9
                        + 1328*m.b7*m.b10 + 1296*m.b7*m.b11 + 1264*m.b7*m.b12 + 1248*m.b7*m.b13 + 1200*m.b7*m.b14 + 1056
                       *m.b7*m.b15 + 816*m.b7*m.b16 + 608*m.b7*m.b17 + 416*m.b7*m.b18 + 256*m.b7*m.b19 + 112*m.b7*m.b20
                        + 1488*m.b8*m.b9 + 1424*m.b8*m.b10 + 1344*m.b8*m.b11 + 1328*m.b8*m.b12 + 1296*m.b8*m.b13 + 1248*
                       m.b8*m.b14 + 1120*m.b8*m.b15 + 888*m.b8*m.b16 + 656*m.b8*m.b17 + 456*m.b8*m.b18 + 272*m.b8*m.b19
                        + 120*m.b8*m.b20 + 1520*m.b9*m.b10 + 1456*m.b9*m.b11 + 1360*m.b9*m.b12 + 1328*m.b9*m.b13 + 1264*
                       m.b9*m.b14 + 1168*m.b9*m.b15 + 928*m.b9*m.b16 + 704*m.b9*m.b17 + 480*m.b9*m.b18 + 288*m.b9*m.b19
                        + 128*m.b9*m.b20 + 1552*m.b10*m.b11 + 1456*m.b10*m.b12 + 1344*m.b10*m.b13 + 1296*m.b10*m.b14 + 
                       1184*m.b10*m.b15 + 952*m.b10*m.b16 + 720*m.b10*m.b17 + 504*m.b10*m.b18 + 304*m.b10*m.b19 + 136*
                       m.b10*m.b20 + 1520*m.b11*m.b12 + 1424*m.b11*m.b13 + 1328*m.b11*m.b14 + 1216*m.b11*m.b15 + 960*
                       m.b11*m.b16 + 720*m.b11*m.b17 + 512*m.b11*m.b18 + 320*m.b11*m.b19 + 144*m.b11*m.b20 + 1488*m.b12*
                       m.b13 + 1392*m.b12*m.b14 + 1248*m.b12*m.b15 + 984*m.b12*m.b16 + 736*m.b12*m.b17 + 504*m.b12*m.b18
                        + 320*m.b12*m.b19 + 152*m.b12*m.b20 + 1424*m.b13*m.b14 + 1280*m.b13*m.b15 + 1008*m.b13*m.b16 + 
                       768*m.b13*m.b17 + 528*m.b13*m.b18 + 320*m.b13*m.b19 + 144*m.b13*m.b20 + 1312*m.b14*m.b15 + 1032*
                       m.b14*m.b16 + 784*m.b14*m.b17 + 552*m.b14*m.b18 + 336*m.b14*m.b19 + 152*m.b14*m.b20 + 1056*m.b15*
                       m.b16 + 800*m.b15*m.b17 + 576*m.b15*m.b18 + 352*m.b15*m.b19 + 160*m.b15*m.b20 + 816*m.b16*m.b17
                        + 584*m.b16*m.b18 + 368*m.b16*m.b19 + 168*m.b16*m.b20 + 592*m.b17*m.b18 + 384*m.b17*m.b19 + 176*
                       m.b17*m.b20 + 384*m.b18*m.b19 + 184*m.b18*m.b20 + 192*m.b19*m.b20 - 364*m.b1 - 772*m.b2 - 1216*
                       m.b3 - 1688*m.b4 - 2180*m.b5 - 2684*m.b6 - 2868*m.b7 - 2956*m.b8 - 3012*m.b9 - 3036*m.b10 - 3036*
                       m.b11 - 3012*m.b12 - 2956*m.b13 - 2868*m.b14 - 2684*m.b15 - 2180*m.b16 - 1688*m.b17 - 1216*m.b18
                        - 772*m.b19 - 364*m.b20 - m.x21 <= 0)

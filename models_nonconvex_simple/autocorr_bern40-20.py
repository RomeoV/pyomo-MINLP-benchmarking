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
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b2*m.b14*m.b15 + 64*m.b1*m.b2*m.b15*m.b16 + 64*m.b1*m.b2*m.b16*m.b17 + 64*m.b1*m.b2*m.b17*
                       m.b18 + 64*m.b1*m.b2*m.b18*m.b19 + 64*m.b1*m.b2*m.b19*m.b20 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*
                       m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*
                       m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3*m.b10*m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*
                       m.b14 + 64*m.b1*m.b3*m.b13*m.b15 + 64*m.b1*m.b3*m.b14*m.b16 + 64*m.b1*m.b3*m.b15*m.b17 + 64*m.b1*
                       m.b3*m.b16*m.b18 + 64*m.b1*m.b3*m.b17*m.b19 + 64*m.b1*m.b3*m.b18*m.b20 + 64*m.b1*m.b4*m.b5*m.b8
                        + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*m.b9
                       *m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*m.b1*m.b4*m.b11*m.b14 + 64*m.b1*m.b4*m.b12*m.b15 + 64*m.b1
                       *m.b4*m.b13*m.b16 + 64*m.b1*m.b4*m.b14*m.b17 + 64*m.b1*m.b4*m.b15*m.b18 + 64*m.b1*m.b4*m.b16*
                       m.b19 + 64*m.b1*m.b4*m.b17*m.b20 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11 + 64*m.b1*
                       m.b5*m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*m.b14 + 64*m.b1*m.b5*m.b11*m.b15
                        + 64*m.b1*m.b5*m.b12*m.b16 + 64*m.b1*m.b5*m.b13*m.b17 + 64*m.b1*m.b5*m.b14*m.b18 + 64*m.b1*m.b5*
                       m.b15*m.b19 + 64*m.b1*m.b5*m.b16*m.b20 + 64*m.b1*m.b6*m.b7*m.b12 + 64*m.b1*m.b6*m.b8*m.b13 + 64*
                       m.b1*m.b6*m.b9*m.b14 + 64*m.b1*m.b6*m.b10*m.b15 + 64*m.b1*m.b6*m.b11*m.b16 + 64*m.b1*m.b6*m.b12*
                       m.b17 + 64*m.b1*m.b6*m.b13*m.b18 + 64*m.b1*m.b6*m.b14*m.b19 + 64*m.b1*m.b6*m.b15*m.b20 + 64*m.b1*
                       m.b7*m.b8*m.b14 + 64*m.b1*m.b7*m.b9*m.b15 + 64*m.b1*m.b7*m.b10*m.b16 + 64*m.b1*m.b7*m.b11*m.b17
                        + 64*m.b1*m.b7*m.b12*m.b18 + 64*m.b1*m.b7*m.b13*m.b19 + 64*m.b1*m.b7*m.b14*m.b20 + 64*m.b1*m.b8*
                       m.b9*m.b16 + 64*m.b1*m.b8*m.b10*m.b17 + 64*m.b1*m.b8*m.b11*m.b18 + 64*m.b1*m.b8*m.b12*m.b19 + 64*
                       m.b1*m.b8*m.b13*m.b20 + 64*m.b1*m.b9*m.b10*m.b18 + 64*m.b1*m.b9*m.b11*m.b19 + 64*m.b1*m.b9*m.b12*
                       m.b20 + 64*m.b1*m.b10*m.b11*m.b20 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*
                       m.b3*m.b6*m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*m.b10 + 
                       128*m.b2*m.b3*m.b10*m.b11 + 128*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*m.b12*m.b13 + 128*m.b2*m.b3
                       *m.b13*m.b14 + 128*m.b2*m.b3*m.b14*m.b15 + 128*m.b2*m.b3*m.b15*m.b16 + 128*m.b2*m.b3*m.b16*m.b17
                        + 128*m.b2*m.b3*m.b17*m.b18 + 128*m.b2*m.b3*m.b18*m.b19 + 128*m.b2*m.b3*m.b19*m.b20 + 64*m.b2*
                       m.b3*m.b20*m.b21 + 128*m.b2*m.b4*m.b5*m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 
                       128*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*
                       m.b11*m.b13 + 128*m.b2*m.b4*m.b12*m.b14 + 128*m.b2*m.b4*m.b13*m.b15 + 128*m.b2*m.b4*m.b14*m.b16
                        + 128*m.b2*m.b4*m.b15*m.b17 + 128*m.b2*m.b4*m.b16*m.b18 + 128*m.b2*m.b4*m.b17*m.b19 + 128*m.b2*
                       m.b4*m.b18*m.b20 + 64*m.b2*m.b4*m.b19*m.b21 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5*m.b7*m.b10
                        + 128*m.b2*m.b5*m.b8*m.b11 + 128*m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*m.b13 + 128*m.b2*
                       m.b5*m.b11*m.b14 + 128*m.b2*m.b5*m.b12*m.b15 + 128*m.b2*m.b5*m.b13*m.b16 + 128*m.b2*m.b5*m.b14*
                       m.b17 + 128*m.b2*m.b5*m.b15*m.b18 + 128*m.b2*m.b5*m.b16*m.b19 + 128*m.b2*m.b5*m.b17*m.b20 + 64*
                       m.b2*m.b5*m.b18*m.b21 + 128*m.b2*m.b6*m.b7*m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*
                       m.b13 + 128*m.b2*m.b6*m.b10*m.b14 + 128*m.b2*m.b6*m.b11*m.b15 + 128*m.b2*m.b6*m.b12*m.b16 + 128*
                       m.b2*m.b6*m.b13*m.b17 + 128*m.b2*m.b6*m.b14*m.b18 + 128*m.b2*m.b6*m.b15*m.b19 + 128*m.b2*m.b6*
                       m.b16*m.b20 + 64*m.b2*m.b6*m.b17*m.b21 + 128*m.b2*m.b7*m.b8*m.b13 + 128*m.b2*m.b7*m.b9*m.b14 + 
                       128*m.b2*m.b7*m.b10*m.b15 + 128*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b7*m.b12*m.b17 + 128*m.b2*m.b7
                       *m.b13*m.b18 + 128*m.b2*m.b7*m.b14*m.b19 + 128*m.b2*m.b7*m.b15*m.b20 + 64*m.b2*m.b7*m.b16*m.b21
                        + 128*m.b2*m.b8*m.b9*m.b15 + 128*m.b2*m.b8*m.b10*m.b16 + 128*m.b2*m.b8*m.b11*m.b17 + 128*m.b2*
                       m.b8*m.b12*m.b18 + 128*m.b2*m.b8*m.b13*m.b19 + 128*m.b2*m.b8*m.b14*m.b20 + 64*m.b2*m.b8*m.b15*
                       m.b21 + 128*m.b2*m.b9*m.b10*m.b17 + 128*m.b2*m.b9*m.b11*m.b18 + 128*m.b2*m.b9*m.b12*m.b19 + 128*
                       m.b2*m.b9*m.b13*m.b20 + 64*m.b2*m.b9*m.b14*m.b21 + 128*m.b2*m.b10*m.b11*m.b19 + 128*m.b2*m.b10*
                       m.b12*m.b20 + 64*m.b2*m.b10*m.b13*m.b21 + 64*m.b2*m.b11*m.b12*m.b21 + 192*m.b3*m.b4*m.b5*m.b6 + 
                       192*m.b3*m.b4*m.b6*m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*
                       m.b10 + 192*m.b3*m.b4*m.b10*m.b11 + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b4*m.b12*m.b13 + 192*
                       m.b3*m.b4*m.b13*m.b14 + 192*m.b3*m.b4*m.b14*m.b15 + 192*m.b3*m.b4*m.b15*m.b16 + 192*m.b3*m.b4*
                       m.b16*m.b17 + 192*m.b3*m.b4*m.b17*m.b18 + 192*m.b3*m.b4*m.b18*m.b19 + 192*m.b3*m.b4*m.b19*m.b20
                        + 128*m.b3*m.b4*m.b20*m.b21 + 64*m.b3*m.b4*m.b21*m.b22 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5
                       *m.b7*m.b9 + 192*m.b3*m.b5*m.b8*m.b10 + 192*m.b3*m.b5*m.b9*m.b11 + 192*m.b3*m.b5*m.b10*m.b12 + 
                       192*m.b3*m.b5*m.b11*m.b13 + 192*m.b3*m.b5*m.b12*m.b14 + 192*m.b3*m.b5*m.b13*m.b15 + 192*m.b3*m.b5
                       *m.b14*m.b16 + 192*m.b3*m.b5*m.b15*m.b17 + 192*m.b3*m.b5*m.b16*m.b18 + 192*m.b3*m.b5*m.b17*m.b19
                        + 192*m.b3*m.b5*m.b18*m.b20 + 128*m.b3*m.b5*m.b19*m.b21 + 64*m.b3*m.b5*m.b20*m.b22 + 192*m.b3*
                       m.b6*m.b7*m.b10 + 192*m.b3*m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*m.b10*m.b13
                        + 192*m.b3*m.b6*m.b11*m.b14 + 192*m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b6*m.b13*m.b16 + 192*m.b3*
                       m.b6*m.b14*m.b17 + 192*m.b3*m.b6*m.b15*m.b18 + 192*m.b3*m.b6*m.b16*m.b19 + 192*m.b3*m.b6*m.b17*
                       m.b20 + 128*m.b3*m.b6*m.b18*m.b21 + 64*m.b3*m.b6*m.b19*m.b22 + 192*m.b3*m.b7*m.b8*m.b12 + 192*
                       m.b3*m.b7*m.b9*m.b13 + 192*m.b3*m.b7*m.b10*m.b14 + 192*m.b3*m.b7*m.b11*m.b15 + 192*m.b3*m.b7*
                       m.b12*m.b16 + 192*m.b3*m.b7*m.b13*m.b17 + 192*m.b3*m.b7*m.b14*m.b18 + 192*m.b3*m.b7*m.b15*m.b19
                        + 192*m.b3*m.b7*m.b16*m.b20 + 128*m.b3*m.b7*m.b17*m.b21 + 64*m.b3*m.b7*m.b18*m.b22 + 192*m.b3*
                       m.b8*m.b9*m.b14 + 192*m.b3*m.b8*m.b10*m.b15 + 192*m.b3*m.b8*m.b11*m.b16 + 192*m.b3*m.b8*m.b12*
                       m.b17 + 192*m.b3*m.b8*m.b13*m.b18 + 192*m.b3*m.b8*m.b14*m.b19 + 192*m.b3*m.b8*m.b15*m.b20 + 128*
                       m.b3*m.b8*m.b16*m.b21 + 64*m.b3*m.b8*m.b17*m.b22 + 192*m.b3*m.b9*m.b10*m.b16 + 192*m.b3*m.b9*
                       m.b11*m.b17 + 192*m.b3*m.b9*m.b12*m.b18 + 192*m.b3*m.b9*m.b13*m.b19 + 192*m.b3*m.b9*m.b14*m.b20
                        + 128*m.b3*m.b9*m.b15*m.b21 + 64*m.b3*m.b9*m.b16*m.b22 + 192*m.b3*m.b10*m.b11*m.b18 + 192*m.b3*
                       m.b10*m.b12*m.b19 + 192*m.b3*m.b10*m.b13*m.b20 + 128*m.b3*m.b10*m.b14*m.b21 + 64*m.b3*m.b10*m.b15
                       *m.b22 + 192*m.b3*m.b11*m.b12*m.b20 + 128*m.b3*m.b11*m.b13*m.b21 + 64*m.b3*m.b11*m.b14*m.b22 + 64
                       *m.b3*m.b12*m.b13*m.b22 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*m.b4*m.b5*m.b8*
                       m.b9 + 256*m.b4*m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5*m.b11*m.b12 + 256*
                       m.b4*m.b5*m.b12*m.b13 + 256*m.b4*m.b5*m.b13*m.b14 + 256*m.b4*m.b5*m.b14*m.b15 + 256*m.b4*m.b5*
                       m.b15*m.b16 + 256*m.b4*m.b5*m.b16*m.b17 + 256*m.b4*m.b5*m.b17*m.b18 + 256*m.b4*m.b5*m.b18*m.b19
                        + 256*m.b4*m.b5*m.b19*m.b20 + 192*m.b4*m.b5*m.b20*m.b21 + 128*m.b4*m.b5*m.b21*m.b22 + 64*m.b4*
                       m.b5*m.b22*m.b23 + 256*m.b4*m.b6*m.b7*m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11
                        + 256*m.b4*m.b6*m.b10*m.b12 + 256*m.b4*m.b6*m.b11*m.b13 + 256*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*
                       m.b6*m.b13*m.b15 + 256*m.b4*m.b6*m.b14*m.b16 + 256*m.b4*m.b6*m.b15*m.b17 + 256*m.b4*m.b6*m.b16*
                       m.b18 + 256*m.b4*m.b6*m.b17*m.b19 + 256*m.b4*m.b6*m.b18*m.b20 + 192*m.b4*m.b6*m.b19*m.b21 + 128*
                       m.b4*m.b6*m.b20*m.b22 + 64*m.b4*m.b6*m.b21*m.b23 + 256*m.b4*m.b7*m.b8*m.b11 + 256*m.b4*m.b7*m.b9*
                       m.b12 + 256*m.b4*m.b7*m.b10*m.b13 + 256*m.b4*m.b7*m.b11*m.b14 + 256*m.b4*m.b7*m.b12*m.b15 + 256*
                       m.b4*m.b7*m.b13*m.b16 + 256*m.b4*m.b7*m.b14*m.b17 + 256*m.b4*m.b7*m.b15*m.b18 + 256*m.b4*m.b7*
                       m.b16*m.b19 + 256*m.b4*m.b7*m.b17*m.b20 + 192*m.b4*m.b7*m.b18*m.b21 + 128*m.b4*m.b7*m.b19*m.b22
                        + 64*m.b4*m.b7*m.b20*m.b23 + 256*m.b4*m.b8*m.b9*m.b13 + 256*m.b4*m.b8*m.b10*m.b14 + 256*m.b4*
                       m.b8*m.b11*m.b15 + 256*m.b4*m.b8*m.b12*m.b16 + 256*m.b4*m.b8*m.b13*m.b17 + 256*m.b4*m.b8*m.b14*
                       m.b18 + 256*m.b4*m.b8*m.b15*m.b19 + 256*m.b4*m.b8*m.b16*m.b20 + 192*m.b4*m.b8*m.b17*m.b21 + 128*
                       m.b4*m.b8*m.b18*m.b22 + 64*m.b4*m.b8*m.b19*m.b23 + 256*m.b4*m.b9*m.b10*m.b15 + 256*m.b4*m.b9*
                       m.b11*m.b16 + 256*m.b4*m.b9*m.b12*m.b17 + 256*m.b4*m.b9*m.b13*m.b18 + 256*m.b4*m.b9*m.b14*m.b19
                        + 256*m.b4*m.b9*m.b15*m.b20 + 192*m.b4*m.b9*m.b16*m.b21 + 128*m.b4*m.b9*m.b17*m.b22 + 64*m.b4*
                       m.b9*m.b18*m.b23 + 256*m.b4*m.b10*m.b11*m.b17 + 256*m.b4*m.b10*m.b12*m.b18 + 256*m.b4*m.b10*m.b13
                       *m.b19 + 256*m.b4*m.b10*m.b14*m.b20 + 192*m.b4*m.b10*m.b15*m.b21 + 128*m.b4*m.b10*m.b16*m.b22 + 
                       64*m.b4*m.b10*m.b17*m.b23 + 256*m.b4*m.b11*m.b12*m.b19 + 256*m.b4*m.b11*m.b13*m.b20 + 192*m.b4*
                       m.b11*m.b14*m.b21 + 128*m.b4*m.b11*m.b15*m.b22 + 64*m.b4*m.b11*m.b16*m.b23 + 192*m.b4*m.b12*m.b13
                       *m.b21 + 128*m.b4*m.b12*m.b14*m.b22 + 64*m.b4*m.b12*m.b15*m.b23 + 64*m.b4*m.b13*m.b14*m.b23 + 320
                       *m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*m.b10*
                       m.b11 + 320*m.b5*m.b6*m.b11*m.b12 + 320*m.b5*m.b6*m.b12*m.b13 + 320*m.b5*m.b6*m.b13*m.b14 + 320*
                       m.b5*m.b6*m.b14*m.b15 + 320*m.b5*m.b6*m.b15*m.b16 + 320*m.b5*m.b6*m.b16*m.b17 + 320*m.b5*m.b6*
                       m.b17*m.b18 + 320*m.b5*m.b6*m.b18*m.b19 + 320*m.b5*m.b6*m.b19*m.b20 + 256*m.b5*m.b6*m.b20*m.b21
                        + 192*m.b5*m.b6*m.b21*m.b22 + 128*m.b5*m.b6*m.b22*m.b23 + 64*m.b5*m.b6*m.b23*m.b24 + 320*m.b5*
                       m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*m.b11 + 320*m.b5*m.b7*m.b10*m.b12 + 320*m.b5*m.b7*m.b11*
                       m.b13 + 320*m.b5*m.b7*m.b12*m.b14 + 320*m.b5*m.b7*m.b13*m.b15 + 320*m.b5*m.b7*m.b14*m.b16 + 320*
                       m.b5*m.b7*m.b15*m.b17 + 320*m.b5*m.b7*m.b16*m.b18 + 320*m.b5*m.b7*m.b17*m.b19 + 320*m.b5*m.b7*
                       m.b18*m.b20 + 256*m.b5*m.b7*m.b19*m.b21 + 192*m.b5*m.b7*m.b20*m.b22 + 128*m.b5*m.b7*m.b21*m.b23
                        + 64*m.b5*m.b7*m.b22*m.b24 + 320*m.b5*m.b8*m.b9*m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 320*m.b5*
                       m.b8*m.b11*m.b14 + 320*m.b5*m.b8*m.b12*m.b15 + 320*m.b5*m.b8*m.b13*m.b16 + 320*m.b5*m.b8*m.b14*
                       m.b17 + 320*m.b5*m.b8*m.b15*m.b18 + 320*m.b5*m.b8*m.b16*m.b19 + 320*m.b5*m.b8*m.b17*m.b20 + 256*
                       m.b5*m.b8*m.b18*m.b21 + 192*m.b5*m.b8*m.b19*m.b22 + 128*m.b5*m.b8*m.b20*m.b23 + 64*m.b5*m.b8*
                       m.b21*m.b24 + 320*m.b5*m.b9*m.b10*m.b14 + 320*m.b5*m.b9*m.b11*m.b15 + 320*m.b5*m.b9*m.b12*m.b16
                        + 320*m.b5*m.b9*m.b13*m.b17 + 320*m.b5*m.b9*m.b14*m.b18 + 320*m.b5*m.b9*m.b15*m.b19 + 320*m.b5*
                       m.b9*m.b16*m.b20 + 256*m.b5*m.b9*m.b17*m.b21 + 192*m.b5*m.b9*m.b18*m.b22 + 128*m.b5*m.b9*m.b19*
                       m.b23 + 64*m.b5*m.b9*m.b20*m.b24 + 320*m.b5*m.b10*m.b11*m.b16 + 320*m.b5*m.b10*m.b12*m.b17 + 320*
                       m.b5*m.b10*m.b13*m.b18 + 320*m.b5*m.b10*m.b14*m.b19 + 320*m.b5*m.b10*m.b15*m.b20 + 256*m.b5*m.b10
                       *m.b16*m.b21 + 192*m.b5*m.b10*m.b17*m.b22 + 128*m.b5*m.b10*m.b18*m.b23 + 64*m.b5*m.b10*m.b19*
                       m.b24 + 320*m.b5*m.b11*m.b12*m.b18 + 320*m.b5*m.b11*m.b13*m.b19 + 320*m.b5*m.b11*m.b14*m.b20 + 
                       256*m.b5*m.b11*m.b15*m.b21 + 192*m.b5*m.b11*m.b16*m.b22 + 128*m.b5*m.b11*m.b17*m.b23 + 64*m.b5*
                       m.b11*m.b18*m.b24 + 320*m.b5*m.b12*m.b13*m.b20 + 256*m.b5*m.b12*m.b14*m.b21 + 192*m.b5*m.b12*
                       m.b15*m.b22 + 128*m.b5*m.b12*m.b16*m.b23 + 64*m.b5*m.b12*m.b17*m.b24 + 192*m.b5*m.b13*m.b14*m.b22
                        + 128*m.b5*m.b13*m.b15*m.b23 + 64*m.b5*m.b13*m.b16*m.b24 + 64*m.b5*m.b14*m.b15*m.b24 + 384*m.b6*
                       m.b7*m.b8*m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12
                        + 384*m.b6*m.b7*m.b12*m.b13 + 384*m.b6*m.b7*m.b13*m.b14 + 384*m.b6*m.b7*m.b14*m.b15 + 384*m.b6*
                       m.b7*m.b15*m.b16 + 384*m.b6*m.b7*m.b16*m.b17 + 384*m.b6*m.b7*m.b17*m.b18 + 384*m.b6*m.b7*m.b18*
                       m.b19 + 384*m.b6*m.b7*m.b19*m.b20 + 320*m.b6*m.b7*m.b20*m.b21 + 256*m.b6*m.b7*m.b21*m.b22 + 192*
                       m.b6*m.b7*m.b22*m.b23 + 128*m.b6*m.b7*m.b23*m.b24 + 64*m.b6*m.b7*m.b24*m.b25 + 384*m.b6*m.b8*m.b9
                       *m.b11 + 384*m.b6*m.b8*m.b10*m.b12 + 384*m.b6*m.b8*m.b11*m.b13 + 384*m.b6*m.b8*m.b12*m.b14 + 384*
                       m.b6*m.b8*m.b13*m.b15 + 384*m.b6*m.b8*m.b14*m.b16 + 384*m.b6*m.b8*m.b15*m.b17 + 384*m.b6*m.b8*
                       m.b16*m.b18 + 384*m.b6*m.b8*m.b17*m.b19 + 384*m.b6*m.b8*m.b18*m.b20 + 320*m.b6*m.b8*m.b19*m.b21
                        + 256*m.b6*m.b8*m.b20*m.b22 + 192*m.b6*m.b8*m.b21*m.b23 + 128*m.b6*m.b8*m.b22*m.b24 + 64*m.b6*
                       m.b8*m.b23*m.b25 + 384*m.b6*m.b9*m.b10*m.b13 + 384*m.b6*m.b9*m.b11*m.b14 + 384*m.b6*m.b9*m.b12*
                       m.b15 + 384*m.b6*m.b9*m.b13*m.b16 + 384*m.b6*m.b9*m.b14*m.b17 + 384*m.b6*m.b9*m.b15*m.b18 + 384*
                       m.b6*m.b9*m.b16*m.b19 + 384*m.b6*m.b9*m.b17*m.b20 + 320*m.b6*m.b9*m.b18*m.b21 + 256*m.b6*m.b9*
                       m.b19*m.b22 + 192*m.b6*m.b9*m.b20*m.b23 + 128*m.b6*m.b9*m.b21*m.b24 + 64*m.b6*m.b9*m.b22*m.b25 + 
                       384*m.b6*m.b10*m.b11*m.b15 + 384*m.b6*m.b10*m.b12*m.b16 + 384*m.b6*m.b10*m.b13*m.b17 + 384*m.b6*
                       m.b10*m.b14*m.b18 + 384*m.b6*m.b10*m.b15*m.b19 + 384*m.b6*m.b10*m.b16*m.b20 + 320*m.b6*m.b10*
                       m.b17*m.b21 + 256*m.b6*m.b10*m.b18*m.b22 + 192*m.b6*m.b10*m.b19*m.b23 + 128*m.b6*m.b10*m.b20*
                       m.b24 + 64*m.b6*m.b10*m.b21*m.b25 + 384*m.b6*m.b11*m.b12*m.b17 + 384*m.b6*m.b11*m.b13*m.b18 + 384
                       *m.b6*m.b11*m.b14*m.b19 + 384*m.b6*m.b11*m.b15*m.b20 + 320*m.b6*m.b11*m.b16*m.b21 + 256*m.b6*
                       m.b11*m.b17*m.b22 + 192*m.b6*m.b11*m.b18*m.b23 + 128*m.b6*m.b11*m.b19*m.b24 + 64*m.b6*m.b11*m.b20
                       *m.b25 + 384*m.b6*m.b12*m.b13*m.b19 + 384*m.b6*m.b12*m.b14*m.b20 + 320*m.b6*m.b12*m.b15*m.b21 + 
                       256*m.b6*m.b12*m.b16*m.b22 + 192*m.b6*m.b12*m.b17*m.b23 + 128*m.b6*m.b12*m.b18*m.b24 + 64*m.b6*
                       m.b12*m.b19*m.b25 + 320*m.b6*m.b13*m.b14*m.b21 + 256*m.b6*m.b13*m.b15*m.b22 + 192*m.b6*m.b13*
                       m.b16*m.b23 + 128*m.b6*m.b13*m.b17*m.b24 + 64*m.b6*m.b13*m.b18*m.b25 + 192*m.b6*m.b14*m.b15*m.b23
                        + 128*m.b6*m.b14*m.b16*m.b24 + 64*m.b6*m.b14*m.b17*m.b25 + 64*m.b6*m.b15*m.b16*m.b25 + 448*m.b7*
                       m.b8*m.b9*m.b10 + 448*m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*m.b11*m.b12 + 448*m.b7*m.b8*m.b12*
                       m.b13 + 448*m.b7*m.b8*m.b13*m.b14 + 448*m.b7*m.b8*m.b14*m.b15 + 448*m.b7*m.b8*m.b15*m.b16 + 448*
                       m.b7*m.b8*m.b16*m.b17 + 448*m.b7*m.b8*m.b17*m.b18 + 448*m.b7*m.b8*m.b18*m.b19 + 448*m.b7*m.b8*
                       m.b19*m.b20 + 384*m.b7*m.b8*m.b20*m.b21 + 320*m.b7*m.b8*m.b21*m.b22 + 256*m.b7*m.b8*m.b22*m.b23
                        + 192*m.b7*m.b8*m.b23*m.b24 + 128*m.b7*m.b8*m.b24*m.b25 + 64*m.b7*m.b8*m.b25*m.b26 + 448*m.b7*
                       m.b9*m.b10*m.b12 + 448*m.b7*m.b9*m.b11*m.b13 + 448*m.b7*m.b9*m.b12*m.b14 + 448*m.b7*m.b9*m.b13*
                       m.b15 + 448*m.b7*m.b9*m.b14*m.b16 + 448*m.b7*m.b9*m.b15*m.b17 + 448*m.b7*m.b9*m.b16*m.b18 + 448*
                       m.b7*m.b9*m.b17*m.b19 + 448*m.b7*m.b9*m.b18*m.b20 + 384*m.b7*m.b9*m.b19*m.b21 + 320*m.b7*m.b9*
                       m.b20*m.b22 + 256*m.b7*m.b9*m.b21*m.b23 + 192*m.b7*m.b9*m.b22*m.b24 + 128*m.b7*m.b9*m.b23*m.b25
                        + 64*m.b7*m.b9*m.b24*m.b26 + 448*m.b7*m.b10*m.b11*m.b14 + 448*m.b7*m.b10*m.b12*m.b15 + 448*m.b7*
                       m.b10*m.b13*m.b16 + 448*m.b7*m.b10*m.b14*m.b17 + 448*m.b7*m.b10*m.b15*m.b18 + 448*m.b7*m.b10*
                       m.b16*m.b19 + 448*m.b7*m.b10*m.b17*m.b20 + 384*m.b7*m.b10*m.b18*m.b21 + 320*m.b7*m.b10*m.b19*
                       m.b22 + 256*m.b7*m.b10*m.b20*m.b23 + 192*m.b7*m.b10*m.b21*m.b24 + 128*m.b7*m.b10*m.b22*m.b25 + 64
                       *m.b7*m.b10*m.b23*m.b26 + 448*m.b7*m.b11*m.b12*m.b16 + 448*m.b7*m.b11*m.b13*m.b17 + 448*m.b7*
                       m.b11*m.b14*m.b18 + 448*m.b7*m.b11*m.b15*m.b19 + 448*m.b7*m.b11*m.b16*m.b20 + 384*m.b7*m.b11*
                       m.b17*m.b21 + 320*m.b7*m.b11*m.b18*m.b22 + 256*m.b7*m.b11*m.b19*m.b23 + 192*m.b7*m.b11*m.b20*
                       m.b24 + 128*m.b7*m.b11*m.b21*m.b25 + 64*m.b7*m.b11*m.b22*m.b26 + 448*m.b7*m.b12*m.b13*m.b18 + 448
                       *m.b7*m.b12*m.b14*m.b19 + 448*m.b7*m.b12*m.b15*m.b20 + 384*m.b7*m.b12*m.b16*m.b21 + 320*m.b7*
                       m.b12*m.b17*m.b22 + 256*m.b7*m.b12*m.b18*m.b23 + 192*m.b7*m.b12*m.b19*m.b24 + 128*m.b7*m.b12*
                       m.b20*m.b25 + 64*m.b7*m.b12*m.b21*m.b26 + 448*m.b7*m.b13*m.b14*m.b20 + 384*m.b7*m.b13*m.b15*m.b21
                        + 320*m.b7*m.b13*m.b16*m.b22 + 256*m.b7*m.b13*m.b17*m.b23 + 192*m.b7*m.b13*m.b18*m.b24 + 128*
                       m.b7*m.b13*m.b19*m.b25 + 64*m.b7*m.b13*m.b20*m.b26 + 320*m.b7*m.b14*m.b15*m.b22 + 256*m.b7*m.b14*
                       m.b16*m.b23 + 192*m.b7*m.b14*m.b17*m.b24 + 128*m.b7*m.b14*m.b18*m.b25 + 64*m.b7*m.b14*m.b19*m.b26
                        + 192*m.b7*m.b15*m.b16*m.b24 + 128*m.b7*m.b15*m.b17*m.b25 + 64*m.b7*m.b15*m.b18*m.b26 + 64*m.b7*
                       m.b16*m.b17*m.b26 + 512*m.b8*m.b9*m.b10*m.b11 + 512*m.b8*m.b9*m.b11*m.b12 + 512*m.b8*m.b9*m.b12*
                       m.b13 + 512*m.b8*m.b9*m.b13*m.b14 + 512*m.b8*m.b9*m.b14*m.b15 + 512*m.b8*m.b9*m.b15*m.b16 + 512*
                       m.b8*m.b9*m.b16*m.b17 + 512*m.b8*m.b9*m.b17*m.b18 + 512*m.b8*m.b9*m.b18*m.b19 + 512*m.b8*m.b9*
                       m.b19*m.b20 + 448*m.b8*m.b9*m.b20*m.b21 + 384*m.b8*m.b9*m.b21*m.b22 + 320*m.b8*m.b9*m.b22*m.b23
                        + 256*m.b8*m.b9*m.b23*m.b24 + 192*m.b8*m.b9*m.b24*m.b25 + 128*m.b8*m.b9*m.b25*m.b26 + 64*m.b8*
                       m.b9*m.b26*m.b27 + 512*m.b8*m.b10*m.b11*m.b13 + 512*m.b8*m.b10*m.b12*m.b14 + 512*m.b8*m.b10*m.b13
                       *m.b15 + 512*m.b8*m.b10*m.b14*m.b16 + 512*m.b8*m.b10*m.b15*m.b17 + 512*m.b8*m.b10*m.b16*m.b18 + 
                       512*m.b8*m.b10*m.b17*m.b19 + 512*m.b8*m.b10*m.b18*m.b20 + 448*m.b8*m.b10*m.b19*m.b21 + 384*m.b8*
                       m.b10*m.b20*m.b22 + 320*m.b8*m.b10*m.b21*m.b23 + 256*m.b8*m.b10*m.b22*m.b24 + 192*m.b8*m.b10*
                       m.b23*m.b25 + 128*m.b8*m.b10*m.b24*m.b26 + 64*m.b8*m.b10*m.b25*m.b27 + 512*m.b8*m.b11*m.b12*m.b15
                        + 512*m.b8*m.b11*m.b13*m.b16 + 512*m.b8*m.b11*m.b14*m.b17 + 512*m.b8*m.b11*m.b15*m.b18 + 512*
                       m.b8*m.b11*m.b16*m.b19 + 512*m.b8*m.b11*m.b17*m.b20 + 448*m.b8*m.b11*m.b18*m.b21 + 384*m.b8*m.b11
                       *m.b19*m.b22 + 320*m.b8*m.b11*m.b20*m.b23 + 256*m.b8*m.b11*m.b21*m.b24 + 192*m.b8*m.b11*m.b22*
                       m.b25 + 128*m.b8*m.b11*m.b23*m.b26 + 64*m.b8*m.b11*m.b24*m.b27 + 512*m.b8*m.b12*m.b13*m.b17 + 512
                       *m.b8*m.b12*m.b14*m.b18 + 512*m.b8*m.b12*m.b15*m.b19 + 512*m.b8*m.b12*m.b16*m.b20 + 448*m.b8*
                       m.b12*m.b17*m.b21 + 384*m.b8*m.b12*m.b18*m.b22 + 320*m.b8*m.b12*m.b19*m.b23 + 256*m.b8*m.b12*
                       m.b20*m.b24 + 192*m.b8*m.b12*m.b21*m.b25 + 128*m.b8*m.b12*m.b22*m.b26 + 64*m.b8*m.b12*m.b23*m.b27
                        + 512*m.b8*m.b13*m.b14*m.b19 + 512*m.b8*m.b13*m.b15*m.b20 + 448*m.b8*m.b13*m.b16*m.b21 + 384*
                       m.b8*m.b13*m.b17*m.b22 + 320*m.b8*m.b13*m.b18*m.b23 + 256*m.b8*m.b13*m.b19*m.b24 + 192*m.b8*m.b13
                       *m.b20*m.b25 + 128*m.b8*m.b13*m.b21*m.b26 + 64*m.b8*m.b13*m.b22*m.b27 + 448*m.b8*m.b14*m.b15*
                       m.b21 + 384*m.b8*m.b14*m.b16*m.b22 + 320*m.b8*m.b14*m.b17*m.b23 + 256*m.b8*m.b14*m.b18*m.b24 + 
                       192*m.b8*m.b14*m.b19*m.b25 + 128*m.b8*m.b14*m.b20*m.b26 + 64*m.b8*m.b14*m.b21*m.b27 + 320*m.b8*
                       m.b15*m.b16*m.b23 + 256*m.b8*m.b15*m.b17*m.b24 + 192*m.b8*m.b15*m.b18*m.b25 + 128*m.b8*m.b15*
                       m.b19*m.b26 + 64*m.b8*m.b15*m.b20*m.b27 + 192*m.b8*m.b16*m.b17*m.b25 + 128*m.b8*m.b16*m.b18*m.b26
                        + 64*m.b8*m.b16*m.b19*m.b27 + 64*m.b8*m.b17*m.b18*m.b27 + 576*m.b9*m.b10*m.b11*m.b12 + 576*m.b9*
                       m.b10*m.b12*m.b13 + 576*m.b9*m.b10*m.b13*m.b14 + 576*m.b9*m.b10*m.b14*m.b15 + 576*m.b9*m.b10*
                       m.b15*m.b16 + 576*m.b9*m.b10*m.b16*m.b17 + 576*m.b9*m.b10*m.b17*m.b18 + 576*m.b9*m.b10*m.b18*
                       m.b19 + 576*m.b9*m.b10*m.b19*m.b20 + 512*m.b9*m.b10*m.b20*m.b21 + 448*m.b9*m.b10*m.b21*m.b22 + 
                       384*m.b9*m.b10*m.b22*m.b23 + 320*m.b9*m.b10*m.b23*m.b24 + 256*m.b9*m.b10*m.b24*m.b25 + 192*m.b9*
                       m.b10*m.b25*m.b26 + 128*m.b9*m.b10*m.b26*m.b27 + 64*m.b9*m.b10*m.b27*m.b28 + 576*m.b9*m.b11*m.b12
                       *m.b14 + 576*m.b9*m.b11*m.b13*m.b15 + 576*m.b9*m.b11*m.b14*m.b16 + 576*m.b9*m.b11*m.b15*m.b17 + 
                       576*m.b9*m.b11*m.b16*m.b18 + 576*m.b9*m.b11*m.b17*m.b19 + 576*m.b9*m.b11*m.b18*m.b20 + 512*m.b9*
                       m.b11*m.b19*m.b21 + 448*m.b9*m.b11*m.b20*m.b22 + 384*m.b9*m.b11*m.b21*m.b23 + 320*m.b9*m.b11*
                       m.b22*m.b24 + 256*m.b9*m.b11*m.b23*m.b25 + 192*m.b9*m.b11*m.b24*m.b26 + 128*m.b9*m.b11*m.b25*
                       m.b27 + 64*m.b9*m.b11*m.b26*m.b28 + 576*m.b9*m.b12*m.b13*m.b16 + 576*m.b9*m.b12*m.b14*m.b17 + 576
                       *m.b9*m.b12*m.b15*m.b18 + 576*m.b9*m.b12*m.b16*m.b19 + 576*m.b9*m.b12*m.b17*m.b20 + 512*m.b9*
                       m.b12*m.b18*m.b21 + 448*m.b9*m.b12*m.b19*m.b22 + 384*m.b9*m.b12*m.b20*m.b23 + 320*m.b9*m.b12*
                       m.b21*m.b24 + 256*m.b9*m.b12*m.b22*m.b25 + 192*m.b9*m.b12*m.b23*m.b26 + 128*m.b9*m.b12*m.b24*
                       m.b27 + 64*m.b9*m.b12*m.b25*m.b28 + 576*m.b9*m.b13*m.b14*m.b18 + 576*m.b9*m.b13*m.b15*m.b19 + 576
                       *m.b9*m.b13*m.b16*m.b20 + 512*m.b9*m.b13*m.b17*m.b21 + 448*m.b9*m.b13*m.b18*m.b22 + 384*m.b9*
                       m.b13*m.b19*m.b23 + 320*m.b9*m.b13*m.b20*m.b24 + 256*m.b9*m.b13*m.b21*m.b25 + 192*m.b9*m.b13*
                       m.b22*m.b26 + 128*m.b9*m.b13*m.b23*m.b27 + 64*m.b9*m.b13*m.b24*m.b28 + 576*m.b9*m.b14*m.b15*m.b20
                        + 512*m.b9*m.b14*m.b16*m.b21 + 448*m.b9*m.b14*m.b17*m.b22 + 384*m.b9*m.b14*m.b18*m.b23 + 320*
                       m.b9*m.b14*m.b19*m.b24 + 256*m.b9*m.b14*m.b20*m.b25 + 192*m.b9*m.b14*m.b21*m.b26 + 128*m.b9*m.b14
                       *m.b22*m.b27 + 64*m.b9*m.b14*m.b23*m.b28 + 448*m.b9*m.b15*m.b16*m.b22 + 384*m.b9*m.b15*m.b17*
                       m.b23 + 320*m.b9*m.b15*m.b18*m.b24 + 256*m.b9*m.b15*m.b19*m.b25 + 192*m.b9*m.b15*m.b20*m.b26 + 
                       128*m.b9*m.b15*m.b21*m.b27 + 64*m.b9*m.b15*m.b22*m.b28 + 320*m.b9*m.b16*m.b17*m.b24 + 256*m.b9*
                       m.b16*m.b18*m.b25 + 192*m.b9*m.b16*m.b19*m.b26 + 128*m.b9*m.b16*m.b20*m.b27 + 64*m.b9*m.b16*m.b21
                       *m.b28 + 192*m.b9*m.b17*m.b18*m.b26 + 128*m.b9*m.b17*m.b19*m.b27 + 64*m.b9*m.b17*m.b20*m.b28 + 64
                       *m.b9*m.b18*m.b19*m.b28 + 640*m.b10*m.b11*m.b12*m.b13 + 640*m.b10*m.b11*m.b13*m.b14 + 640*m.b10*
                       m.b11*m.b14*m.b15 + 640*m.b10*m.b11*m.b15*m.b16 + 640*m.b10*m.b11*m.b16*m.b17 + 640*m.b10*m.b11*
                       m.b17*m.b18 + 640*m.b10*m.b11*m.b18*m.b19 + 640*m.b10*m.b11*m.b19*m.b20 + 576*m.b10*m.b11*m.b20*
                       m.b21 + 512*m.b10*m.b11*m.b21*m.b22 + 448*m.b10*m.b11*m.b22*m.b23 + 384*m.b10*m.b11*m.b23*m.b24
                        + 320*m.b10*m.b11*m.b24*m.b25 + 256*m.b10*m.b11*m.b25*m.b26 + 192*m.b10*m.b11*m.b26*m.b27 + 128*
                       m.b10*m.b11*m.b27*m.b28 + 64*m.b10*m.b11*m.b28*m.b29 + 640*m.b10*m.b12*m.b13*m.b15 + 640*m.b10*
                       m.b12*m.b14*m.b16 + 640*m.b10*m.b12*m.b15*m.b17 + 640*m.b10*m.b12*m.b16*m.b18 + 640*m.b10*m.b12*
                       m.b17*m.b19 + 640*m.b10*m.b12*m.b18*m.b20 + 576*m.b10*m.b12*m.b19*m.b21 + 512*m.b10*m.b12*m.b20*
                       m.b22 + 448*m.b10*m.b12*m.b21*m.b23 + 384*m.b10*m.b12*m.b22*m.b24 + 320*m.b10*m.b12*m.b23*m.b25
                        + 256*m.b10*m.b12*m.b24*m.b26 + 192*m.b10*m.b12*m.b25*m.b27 + 128*m.b10*m.b12*m.b26*m.b28 + 64*
                       m.b10*m.b12*m.b27*m.b29 + 640*m.b10*m.b13*m.b14*m.b17 + 640*m.b10*m.b13*m.b15*m.b18 + 640*m.b10*
                       m.b13*m.b16*m.b19 + 640*m.b10*m.b13*m.b17*m.b20 + 576*m.b10*m.b13*m.b18*m.b21 + 512*m.b10*m.b13*
                       m.b19*m.b22 + 448*m.b10*m.b13*m.b20*m.b23 + 384*m.b10*m.b13*m.b21*m.b24 + 320*m.b10*m.b13*m.b22*
                       m.b25 + 256*m.b10*m.b13*m.b23*m.b26 + 192*m.b10*m.b13*m.b24*m.b27 + 128*m.b10*m.b13*m.b25*m.b28
                        + 64*m.b10*m.b13*m.b26*m.b29 + 640*m.b10*m.b14*m.b15*m.b19 + 640*m.b10*m.b14*m.b16*m.b20 + 576*
                       m.b10*m.b14*m.b17*m.b21 + 512*m.b10*m.b14*m.b18*m.b22 + 448*m.b10*m.b14*m.b19*m.b23 + 384*m.b10*
                       m.b14*m.b20*m.b24 + 320*m.b10*m.b14*m.b21*m.b25 + 256*m.b10*m.b14*m.b22*m.b26 + 192*m.b10*m.b14*
                       m.b23*m.b27 + 128*m.b10*m.b14*m.b24*m.b28 + 64*m.b10*m.b14*m.b25*m.b29 + 576*m.b10*m.b15*m.b16*
                       m.b21 + 512*m.b10*m.b15*m.b17*m.b22 + 448*m.b10*m.b15*m.b18*m.b23 + 384*m.b10*m.b15*m.b19*m.b24
                        + 320*m.b10*m.b15*m.b20*m.b25 + 256*m.b10*m.b15*m.b21*m.b26 + 192*m.b10*m.b15*m.b22*m.b27 + 128*
                       m.b10*m.b15*m.b23*m.b28 + 64*m.b10*m.b15*m.b24*m.b29 + 448*m.b10*m.b16*m.b17*m.b23 + 384*m.b10*
                       m.b16*m.b18*m.b24 + 320*m.b10*m.b16*m.b19*m.b25 + 256*m.b10*m.b16*m.b20*m.b26 + 192*m.b10*m.b16*
                       m.b21*m.b27 + 128*m.b10*m.b16*m.b22*m.b28 + 64*m.b10*m.b16*m.b23*m.b29 + 320*m.b10*m.b17*m.b18*
                       m.b25 + 256*m.b10*m.b17*m.b19*m.b26 + 192*m.b10*m.b17*m.b20*m.b27 + 128*m.b10*m.b17*m.b21*m.b28
                        + 64*m.b10*m.b17*m.b22*m.b29 + 192*m.b10*m.b18*m.b19*m.b27 + 128*m.b10*m.b18*m.b20*m.b28 + 64*
                       m.b10*m.b18*m.b21*m.b29 + 64*m.b10*m.b19*m.b20*m.b29 + 704*m.b11*m.b12*m.b13*m.b14 + 704*m.b11*
                       m.b12*m.b14*m.b15 + 704*m.b11*m.b12*m.b15*m.b16 + 704*m.b11*m.b12*m.b16*m.b17 + 704*m.b11*m.b12*
                       m.b17*m.b18 + 704*m.b11*m.b12*m.b18*m.b19 + 704*m.b11*m.b12*m.b19*m.b20 + 640*m.b11*m.b12*m.b20*
                       m.b21 + 576*m.b11*m.b12*m.b21*m.b22 + 512*m.b11*m.b12*m.b22*m.b23 + 448*m.b11*m.b12*m.b23*m.b24
                        + 384*m.b11*m.b12*m.b24*m.b25 + 320*m.b11*m.b12*m.b25*m.b26 + 256*m.b11*m.b12*m.b26*m.b27 + 192*
                       m.b11*m.b12*m.b27*m.b28 + 128*m.b11*m.b12*m.b28*m.b29 + 64*m.b11*m.b12*m.b29*m.b30 + 704*m.b11*
                       m.b13*m.b14*m.b16 + 704*m.b11*m.b13*m.b15*m.b17 + 704*m.b11*m.b13*m.b16*m.b18 + 704*m.b11*m.b13*
                       m.b17*m.b19 + 704*m.b11*m.b13*m.b18*m.b20 + 640*m.b11*m.b13*m.b19*m.b21 + 576*m.b11*m.b13*m.b20*
                       m.b22 + 512*m.b11*m.b13*m.b21*m.b23 + 448*m.b11*m.b13*m.b22*m.b24 + 384*m.b11*m.b13*m.b23*m.b25
                        + 320*m.b11*m.b13*m.b24*m.b26 + 256*m.b11*m.b13*m.b25*m.b27 + 192*m.b11*m.b13*m.b26*m.b28 + 128*
                       m.b11*m.b13*m.b27*m.b29 + 64*m.b11*m.b13*m.b28*m.b30 + 704*m.b11*m.b14*m.b15*m.b18 + 704*m.b11*
                       m.b14*m.b16*m.b19 + 704*m.b11*m.b14*m.b17*m.b20 + 640*m.b11*m.b14*m.b18*m.b21 + 576*m.b11*m.b14*
                       m.b19*m.b22 + 512*m.b11*m.b14*m.b20*m.b23 + 448*m.b11*m.b14*m.b21*m.b24 + 384*m.b11*m.b14*m.b22*
                       m.b25 + 320*m.b11*m.b14*m.b23*m.b26 + 256*m.b11*m.b14*m.b24*m.b27 + 192*m.b11*m.b14*m.b25*m.b28
                        + 128*m.b11*m.b14*m.b26*m.b29 + 64*m.b11*m.b14*m.b27*m.b30 + 704*m.b11*m.b15*m.b16*m.b20 + 640*
                       m.b11*m.b15*m.b17*m.b21 + 576*m.b11*m.b15*m.b18*m.b22 + 512*m.b11*m.b15*m.b19*m.b23 + 448*m.b11*
                       m.b15*m.b20*m.b24 + 384*m.b11*m.b15*m.b21*m.b25 + 320*m.b11*m.b15*m.b22*m.b26 + 256*m.b11*m.b15*
                       m.b23*m.b27 + 192*m.b11*m.b15*m.b24*m.b28 + 128*m.b11*m.b15*m.b25*m.b29 + 64*m.b11*m.b15*m.b26*
                       m.b30 + 576*m.b11*m.b16*m.b17*m.b22 + 512*m.b11*m.b16*m.b18*m.b23 + 448*m.b11*m.b16*m.b19*m.b24
                        + 384*m.b11*m.b16*m.b20*m.b25 + 320*m.b11*m.b16*m.b21*m.b26 + 256*m.b11*m.b16*m.b22*m.b27 + 192*
                       m.b11*m.b16*m.b23*m.b28 + 128*m.b11*m.b16*m.b24*m.b29 + 64*m.b11*m.b16*m.b25*m.b30 + 448*m.b11*
                       m.b17*m.b18*m.b24 + 384*m.b11*m.b17*m.b19*m.b25 + 320*m.b11*m.b17*m.b20*m.b26 + 256*m.b11*m.b17*
                       m.b21*m.b27 + 192*m.b11*m.b17*m.b22*m.b28 + 128*m.b11*m.b17*m.b23*m.b29 + 64*m.b11*m.b17*m.b24*
                       m.b30 + 320*m.b11*m.b18*m.b19*m.b26 + 256*m.b11*m.b18*m.b20*m.b27 + 192*m.b11*m.b18*m.b21*m.b28
                        + 128*m.b11*m.b18*m.b22*m.b29 + 64*m.b11*m.b18*m.b23*m.b30 + 192*m.b11*m.b19*m.b20*m.b28 + 128*
                       m.b11*m.b19*m.b21*m.b29 + 64*m.b11*m.b19*m.b22*m.b30 + 64*m.b11*m.b20*m.b21*m.b30 + 768*m.b12*
                       m.b13*m.b14*m.b15 + 768*m.b12*m.b13*m.b15*m.b16 + 768*m.b12*m.b13*m.b16*m.b17 + 768*m.b12*m.b13*
                       m.b17*m.b18 + 768*m.b12*m.b13*m.b18*m.b19 + 768*m.b12*m.b13*m.b19*m.b20 + 704*m.b12*m.b13*m.b20*
                       m.b21 + 640*m.b12*m.b13*m.b21*m.b22 + 576*m.b12*m.b13*m.b22*m.b23 + 512*m.b12*m.b13*m.b23*m.b24
                        + 448*m.b12*m.b13*m.b24*m.b25 + 384*m.b12*m.b13*m.b25*m.b26 + 320*m.b12*m.b13*m.b26*m.b27 + 256*
                       m.b12*m.b13*m.b27*m.b28 + 192*m.b12*m.b13*m.b28*m.b29 + 128*m.b12*m.b13*m.b29*m.b30 + 64*m.b12*
                       m.b13*m.b30*m.b31 + 768*m.b12*m.b14*m.b15*m.b17 + 768*m.b12*m.b14*m.b16*m.b18 + 768*m.b12*m.b14*
                       m.b17*m.b19 + 768*m.b12*m.b14*m.b18*m.b20 + 704*m.b12*m.b14*m.b19*m.b21 + 640*m.b12*m.b14*m.b20*
                       m.b22 + 576*m.b12*m.b14*m.b21*m.b23 + 512*m.b12*m.b14*m.b22*m.b24 + 448*m.b12*m.b14*m.b23*m.b25
                        + 384*m.b12*m.b14*m.b24*m.b26 + 320*m.b12*m.b14*m.b25*m.b27 + 256*m.b12*m.b14*m.b26*m.b28 + 192*
                       m.b12*m.b14*m.b27*m.b29 + 128*m.b12*m.b14*m.b28*m.b30 + 64*m.b12*m.b14*m.b29*m.b31 + 768*m.b12*
                       m.b15*m.b16*m.b19 + 768*m.b12*m.b15*m.b17*m.b20 + 704*m.b12*m.b15*m.b18*m.b21 + 640*m.b12*m.b15*
                       m.b19*m.b22 + 576*m.b12*m.b15*m.b20*m.b23 + 512*m.b12*m.b15*m.b21*m.b24 + 448*m.b12*m.b15*m.b22*
                       m.b25 + 384*m.b12*m.b15*m.b23*m.b26 + 320*m.b12*m.b15*m.b24*m.b27 + 256*m.b12*m.b15*m.b25*m.b28
                        + 192*m.b12*m.b15*m.b26*m.b29 + 128*m.b12*m.b15*m.b27*m.b30 + 64*m.b12*m.b15*m.b28*m.b31 + 704*
                       m.b12*m.b16*m.b17*m.b21 + 640*m.b12*m.b16*m.b18*m.b22 + 576*m.b12*m.b16*m.b19*m.b23 + 512*m.b12*
                       m.b16*m.b20*m.b24 + 448*m.b12*m.b16*m.b21*m.b25 + 384*m.b12*m.b16*m.b22*m.b26 + 320*m.b12*m.b16*
                       m.b23*m.b27 + 256*m.b12*m.b16*m.b24*m.b28 + 192*m.b12*m.b16*m.b25*m.b29 + 128*m.b12*m.b16*m.b26*
                       m.b30 + 64*m.b12*m.b16*m.b27*m.b31 + 576*m.b12*m.b17*m.b18*m.b23 + 512*m.b12*m.b17*m.b19*m.b24 + 
                       448*m.b12*m.b17*m.b20*m.b25 + 384*m.b12*m.b17*m.b21*m.b26 + 320*m.b12*m.b17*m.b22*m.b27 + 256*
                       m.b12*m.b17*m.b23*m.b28 + 192*m.b12*m.b17*m.b24*m.b29 + 128*m.b12*m.b17*m.b25*m.b30 + 64*m.b12*
                       m.b17*m.b26*m.b31 + 448*m.b12*m.b18*m.b19*m.b25 + 384*m.b12*m.b18*m.b20*m.b26 + 320*m.b12*m.b18*
                       m.b21*m.b27 + 256*m.b12*m.b18*m.b22*m.b28 + 192*m.b12*m.b18*m.b23*m.b29 + 128*m.b12*m.b18*m.b24*
                       m.b30 + 64*m.b12*m.b18*m.b25*m.b31 + 320*m.b12*m.b19*m.b20*m.b27 + 256*m.b12*m.b19*m.b21*m.b28 + 
                       192*m.b12*m.b19*m.b22*m.b29 + 128*m.b12*m.b19*m.b23*m.b30 + 64*m.b12*m.b19*m.b24*m.b31 + 192*
                       m.b12*m.b20*m.b21*m.b29 + 128*m.b12*m.b20*m.b22*m.b30 + 64*m.b12*m.b20*m.b23*m.b31 + 64*m.b12*
                       m.b21*m.b22*m.b31 + 832*m.b13*m.b14*m.b15*m.b16 + 832*m.b13*m.b14*m.b16*m.b17 + 832*m.b13*m.b14*
                       m.b17*m.b18 + 832*m.b13*m.b14*m.b18*m.b19 + 832*m.b13*m.b14*m.b19*m.b20 + 768*m.b13*m.b14*m.b20*
                       m.b21 + 704*m.b13*m.b14*m.b21*m.b22 + 640*m.b13*m.b14*m.b22*m.b23 + 576*m.b13*m.b14*m.b23*m.b24
                        + 512*m.b13*m.b14*m.b24*m.b25 + 448*m.b13*m.b14*m.b25*m.b26 + 384*m.b13*m.b14*m.b26*m.b27 + 320*
                       m.b13*m.b14*m.b27*m.b28 + 256*m.b13*m.b14*m.b28*m.b29 + 192*m.b13*m.b14*m.b29*m.b30 + 128*m.b13*
                       m.b14*m.b30*m.b31 + 64*m.b13*m.b14*m.b31*m.b32 + 832*m.b13*m.b15*m.b16*m.b18 + 832*m.b13*m.b15*
                       m.b17*m.b19 + 832*m.b13*m.b15*m.b18*m.b20 + 768*m.b13*m.b15*m.b19*m.b21 + 704*m.b13*m.b15*m.b20*
                       m.b22 + 640*m.b13*m.b15*m.b21*m.b23 + 576*m.b13*m.b15*m.b22*m.b24 + 512*m.b13*m.b15*m.b23*m.b25
                        + 448*m.b13*m.b15*m.b24*m.b26 + 384*m.b13*m.b15*m.b25*m.b27 + 320*m.b13*m.b15*m.b26*m.b28 + 256*
                       m.b13*m.b15*m.b27*m.b29 + 192*m.b13*m.b15*m.b28*m.b30 + 128*m.b13*m.b15*m.b29*m.b31 + 64*m.b13*
                       m.b15*m.b30*m.b32 + 832*m.b13*m.b16*m.b17*m.b20 + 768*m.b13*m.b16*m.b18*m.b21 + 704*m.b13*m.b16*
                       m.b19*m.b22 + 640*m.b13*m.b16*m.b20*m.b23 + 576*m.b13*m.b16*m.b21*m.b24 + 512*m.b13*m.b16*m.b22*
                       m.b25 + 448*m.b13*m.b16*m.b23*m.b26 + 384*m.b13*m.b16*m.b24*m.b27 + 320*m.b13*m.b16*m.b25*m.b28
                        + 256*m.b13*m.b16*m.b26*m.b29 + 192*m.b13*m.b16*m.b27*m.b30 + 128*m.b13*m.b16*m.b28*m.b31 + 64*
                       m.b13*m.b16*m.b29*m.b32 + 704*m.b13*m.b17*m.b18*m.b22 + 640*m.b13*m.b17*m.b19*m.b23 + 576*m.b13*
                       m.b17*m.b20*m.b24 + 512*m.b13*m.b17*m.b21*m.b25 + 448*m.b13*m.b17*m.b22*m.b26 + 384*m.b13*m.b17*
                       m.b23*m.b27 + 320*m.b13*m.b17*m.b24*m.b28 + 256*m.b13*m.b17*m.b25*m.b29 + 192*m.b13*m.b17*m.b26*
                       m.b30 + 128*m.b13*m.b17*m.b27*m.b31 + 64*m.b13*m.b17*m.b28*m.b32 + 576*m.b13*m.b18*m.b19*m.b24 + 
                       512*m.b13*m.b18*m.b20*m.b25 + 448*m.b13*m.b18*m.b21*m.b26 + 384*m.b13*m.b18*m.b22*m.b27 + 320*
                       m.b13*m.b18*m.b23*m.b28 + 256*m.b13*m.b18*m.b24*m.b29 + 192*m.b13*m.b18*m.b25*m.b30 + 128*m.b13*
                       m.b18*m.b26*m.b31 + 64*m.b13*m.b18*m.b27*m.b32 + 448*m.b13*m.b19*m.b20*m.b26 + 384*m.b13*m.b19*
                       m.b21*m.b27 + 320*m.b13*m.b19*m.b22*m.b28 + 256*m.b13*m.b19*m.b23*m.b29 + 192*m.b13*m.b19*m.b24*
                       m.b30 + 128*m.b13*m.b19*m.b25*m.b31 + 64*m.b13*m.b19*m.b26*m.b32 + 320*m.b13*m.b20*m.b21*m.b28 + 
                       256*m.b13*m.b20*m.b22*m.b29 + 192*m.b13*m.b20*m.b23*m.b30 + 128*m.b13*m.b20*m.b24*m.b31 + 64*
                       m.b13*m.b20*m.b25*m.b32 + 192*m.b13*m.b21*m.b22*m.b30 + 128*m.b13*m.b21*m.b23*m.b31 + 64*m.b13*
                       m.b21*m.b24*m.b32 + 64*m.b13*m.b22*m.b23*m.b32 + 896*m.b14*m.b15*m.b16*m.b17 + 896*m.b14*m.b15*
                       m.b17*m.b18 + 896*m.b14*m.b15*m.b18*m.b19 + 896*m.b14*m.b15*m.b19*m.b20 + 832*m.b14*m.b15*m.b20*
                       m.b21 + 768*m.b14*m.b15*m.b21*m.b22 + 704*m.b14*m.b15*m.b22*m.b23 + 640*m.b14*m.b15*m.b23*m.b24
                        + 576*m.b14*m.b15*m.b24*m.b25 + 512*m.b14*m.b15*m.b25*m.b26 + 448*m.b14*m.b15*m.b26*m.b27 + 384*
                       m.b14*m.b15*m.b27*m.b28 + 320*m.b14*m.b15*m.b28*m.b29 + 256*m.b14*m.b15*m.b29*m.b30 + 192*m.b14*
                       m.b15*m.b30*m.b31 + 128*m.b14*m.b15*m.b31*m.b32 + 64*m.b14*m.b15*m.b32*m.b33 + 896*m.b14*m.b16*
                       m.b17*m.b19 + 896*m.b14*m.b16*m.b18*m.b20 + 832*m.b14*m.b16*m.b19*m.b21 + 768*m.b14*m.b16*m.b20*
                       m.b22 + 704*m.b14*m.b16*m.b21*m.b23 + 640*m.b14*m.b16*m.b22*m.b24 + 576*m.b14*m.b16*m.b23*m.b25
                        + 512*m.b14*m.b16*m.b24*m.b26 + 448*m.b14*m.b16*m.b25*m.b27 + 384*m.b14*m.b16*m.b26*m.b28 + 320*
                       m.b14*m.b16*m.b27*m.b29 + 256*m.b14*m.b16*m.b28*m.b30 + 192*m.b14*m.b16*m.b29*m.b31 + 128*m.b14*
                       m.b16*m.b30*m.b32 + 64*m.b14*m.b16*m.b31*m.b33 + 832*m.b14*m.b17*m.b18*m.b21 + 768*m.b14*m.b17*
                       m.b19*m.b22 + 704*m.b14*m.b17*m.b20*m.b23 + 640*m.b14*m.b17*m.b21*m.b24 + 576*m.b14*m.b17*m.b22*
                       m.b25 + 512*m.b14*m.b17*m.b23*m.b26 + 448*m.b14*m.b17*m.b24*m.b27 + 384*m.b14*m.b17*m.b25*m.b28
                        + 320*m.b14*m.b17*m.b26*m.b29 + 256*m.b14*m.b17*m.b27*m.b30 + 192*m.b14*m.b17*m.b28*m.b31 + 128*
                       m.b14*m.b17*m.b29*m.b32 + 64*m.b14*m.b17*m.b30*m.b33 + 704*m.b14*m.b18*m.b19*m.b23 + 640*m.b14*
                       m.b18*m.b20*m.b24 + 576*m.b14*m.b18*m.b21*m.b25 + 512*m.b14*m.b18*m.b22*m.b26 + 448*m.b14*m.b18*
                       m.b23*m.b27 + 384*m.b14*m.b18*m.b24*m.b28 + 320*m.b14*m.b18*m.b25*m.b29 + 256*m.b14*m.b18*m.b26*
                       m.b30 + 192*m.b14*m.b18*m.b27*m.b31 + 128*m.b14*m.b18*m.b28*m.b32 + 64*m.b14*m.b18*m.b29*m.b33 + 
                       576*m.b14*m.b19*m.b20*m.b25 + 512*m.b14*m.b19*m.b21*m.b26 + 448*m.b14*m.b19*m.b22*m.b27 + 384*
                       m.b14*m.b19*m.b23*m.b28 + 320*m.b14*m.b19*m.b24*m.b29 + 256*m.b14*m.b19*m.b25*m.b30 + 192*m.b14*
                       m.b19*m.b26*m.b31 + 128*m.b14*m.b19*m.b27*m.b32 + 64*m.b14*m.b19*m.b28*m.b33 + 448*m.b14*m.b20*
                       m.b21*m.b27 + 384*m.b14*m.b20*m.b22*m.b28 + 320*m.b14*m.b20*m.b23*m.b29 + 256*m.b14*m.b20*m.b24*
                       m.b30 + 192*m.b14*m.b20*m.b25*m.b31 + 128*m.b14*m.b20*m.b26*m.b32 + 64*m.b14*m.b20*m.b27*m.b33 + 
                       320*m.b14*m.b21*m.b22*m.b29 + 256*m.b14*m.b21*m.b23*m.b30 + 192*m.b14*m.b21*m.b24*m.b31 + 128*
                       m.b14*m.b21*m.b25*m.b32 + 64*m.b14*m.b21*m.b26*m.b33 + 192*m.b14*m.b22*m.b23*m.b31 + 128*m.b14*
                       m.b22*m.b24*m.b32 + 64*m.b14*m.b22*m.b25*m.b33 + 64*m.b14*m.b23*m.b24*m.b33 + 960*m.b15*m.b16*
                       m.b17*m.b18 + 960*m.b15*m.b16*m.b18*m.b19 + 960*m.b15*m.b16*m.b19*m.b20 + 896*m.b15*m.b16*m.b20*
                       m.b21 + 832*m.b15*m.b16*m.b21*m.b22 + 768*m.b15*m.b16*m.b22*m.b23 + 704*m.b15*m.b16*m.b23*m.b24
                        + 640*m.b15*m.b16*m.b24*m.b25 + 576*m.b15*m.b16*m.b25*m.b26 + 512*m.b15*m.b16*m.b26*m.b27 + 448*
                       m.b15*m.b16*m.b27*m.b28 + 384*m.b15*m.b16*m.b28*m.b29 + 320*m.b15*m.b16*m.b29*m.b30 + 256*m.b15*
                       m.b16*m.b30*m.b31 + 192*m.b15*m.b16*m.b31*m.b32 + 128*m.b15*m.b16*m.b32*m.b33 + 64*m.b15*m.b16*
                       m.b33*m.b34 + 960*m.b15*m.b17*m.b18*m.b20 + 896*m.b15*m.b17*m.b19*m.b21 + 832*m.b15*m.b17*m.b20*
                       m.b22 + 768*m.b15*m.b17*m.b21*m.b23 + 704*m.b15*m.b17*m.b22*m.b24 + 640*m.b15*m.b17*m.b23*m.b25
                        + 576*m.b15*m.b17*m.b24*m.b26 + 512*m.b15*m.b17*m.b25*m.b27 + 448*m.b15*m.b17*m.b26*m.b28 + 384*
                       m.b15*m.b17*m.b27*m.b29 + 320*m.b15*m.b17*m.b28*m.b30 + 256*m.b15*m.b17*m.b29*m.b31 + 192*m.b15*
                       m.b17*m.b30*m.b32 + 128*m.b15*m.b17*m.b31*m.b33 + 64*m.b15*m.b17*m.b32*m.b34 + 832*m.b15*m.b18*
                       m.b19*m.b22 + 768*m.b15*m.b18*m.b20*m.b23 + 704*m.b15*m.b18*m.b21*m.b24 + 640*m.b15*m.b18*m.b22*
                       m.b25 + 576*m.b15*m.b18*m.b23*m.b26 + 512*m.b15*m.b18*m.b24*m.b27 + 448*m.b15*m.b18*m.b25*m.b28
                        + 384*m.b15*m.b18*m.b26*m.b29 + 320*m.b15*m.b18*m.b27*m.b30 + 256*m.b15*m.b18*m.b28*m.b31 + 192*
                       m.b15*m.b18*m.b29*m.b32 + 128*m.b15*m.b18*m.b30*m.b33 + 64*m.b15*m.b18*m.b31*m.b34 + 704*m.b15*
                       m.b19*m.b20*m.b24 + 640*m.b15*m.b19*m.b21*m.b25 + 576*m.b15*m.b19*m.b22*m.b26 + 512*m.b15*m.b19*
                       m.b23*m.b27 + 448*m.b15*m.b19*m.b24*m.b28 + 384*m.b15*m.b19*m.b25*m.b29 + 320*m.b15*m.b19*m.b26*
                       m.b30 + 256*m.b15*m.b19*m.b27*m.b31 + 192*m.b15*m.b19*m.b28*m.b32 + 128*m.b15*m.b19*m.b29*m.b33
                        + 64*m.b15*m.b19*m.b30*m.b34 + 576*m.b15*m.b20*m.b21*m.b26 + 512*m.b15*m.b20*m.b22*m.b27 + 448*
                       m.b15*m.b20*m.b23*m.b28 + 384*m.b15*m.b20*m.b24*m.b29 + 320*m.b15*m.b20*m.b25*m.b30 + 256*m.b15*
                       m.b20*m.b26*m.b31 + 192*m.b15*m.b20*m.b27*m.b32 + 128*m.b15*m.b20*m.b28*m.b33 + 64*m.b15*m.b20*
                       m.b29*m.b34 + 448*m.b15*m.b21*m.b22*m.b28 + 384*m.b15*m.b21*m.b23*m.b29 + 320*m.b15*m.b21*m.b24*
                       m.b30 + 256*m.b15*m.b21*m.b25*m.b31 + 192*m.b15*m.b21*m.b26*m.b32 + 128*m.b15*m.b21*m.b27*m.b33
                        + 64*m.b15*m.b21*m.b28*m.b34 + 320*m.b15*m.b22*m.b23*m.b30 + 256*m.b15*m.b22*m.b24*m.b31 + 192*
                       m.b15*m.b22*m.b25*m.b32 + 128*m.b15*m.b22*m.b26*m.b33 + 64*m.b15*m.b22*m.b27*m.b34 + 192*m.b15*
                       m.b23*m.b24*m.b32 + 128*m.b15*m.b23*m.b25*m.b33 + 64*m.b15*m.b23*m.b26*m.b34 + 64*m.b15*m.b24*
                       m.b25*m.b34 + 1024*m.b16*m.b17*m.b18*m.b19 + 1024*m.b16*m.b17*m.b19*m.b20 + 960*m.b16*m.b17*m.b20
                       *m.b21 + 896*m.b16*m.b17*m.b21*m.b22 + 832*m.b16*m.b17*m.b22*m.b23 + 768*m.b16*m.b17*m.b23*m.b24
                        + 704*m.b16*m.b17*m.b24*m.b25 + 640*m.b16*m.b17*m.b25*m.b26 + 576*m.b16*m.b17*m.b26*m.b27 + 512*
                       m.b16*m.b17*m.b27*m.b28 + 448*m.b16*m.b17*m.b28*m.b29 + 384*m.b16*m.b17*m.b29*m.b30 + 320*m.b16*
                       m.b17*m.b30*m.b31 + 256*m.b16*m.b17*m.b31*m.b32 + 192*m.b16*m.b17*m.b32*m.b33 + 128*m.b16*m.b17*
                       m.b33*m.b34 + 64*m.b16*m.b17*m.b34*m.b35 + 960*m.b16*m.b18*m.b19*m.b21 + 896*m.b16*m.b18*m.b20*
                       m.b22 + 832*m.b16*m.b18*m.b21*m.b23 + 768*m.b16*m.b18*m.b22*m.b24 + 704*m.b16*m.b18*m.b23*m.b25
                        + 640*m.b16*m.b18*m.b24*m.b26 + 576*m.b16*m.b18*m.b25*m.b27 + 512*m.b16*m.b18*m.b26*m.b28 + 448*
                       m.b16*m.b18*m.b27*m.b29 + 384*m.b16*m.b18*m.b28*m.b30 + 320*m.b16*m.b18*m.b29*m.b31 + 256*m.b16*
                       m.b18*m.b30*m.b32 + 192*m.b16*m.b18*m.b31*m.b33 + 128*m.b16*m.b18*m.b32*m.b34 + 64*m.b16*m.b18*
                       m.b33*m.b35 + 832*m.b16*m.b19*m.b20*m.b23 + 768*m.b16*m.b19*m.b21*m.b24 + 704*m.b16*m.b19*m.b22*
                       m.b25 + 640*m.b16*m.b19*m.b23*m.b26 + 576*m.b16*m.b19*m.b24*m.b27 + 512*m.b16*m.b19*m.b25*m.b28
                        + 448*m.b16*m.b19*m.b26*m.b29 + 384*m.b16*m.b19*m.b27*m.b30 + 320*m.b16*m.b19*m.b28*m.b31 + 256*
                       m.b16*m.b19*m.b29*m.b32 + 192*m.b16*m.b19*m.b30*m.b33 + 128*m.b16*m.b19*m.b31*m.b34 + 64*m.b16*
                       m.b19*m.b32*m.b35 + 704*m.b16*m.b20*m.b21*m.b25 + 640*m.b16*m.b20*m.b22*m.b26 + 576*m.b16*m.b20*
                       m.b23*m.b27 + 512*m.b16*m.b20*m.b24*m.b28 + 448*m.b16*m.b20*m.b25*m.b29 + 384*m.b16*m.b20*m.b26*
                       m.b30 + 320*m.b16*m.b20*m.b27*m.b31 + 256*m.b16*m.b20*m.b28*m.b32 + 192*m.b16*m.b20*m.b29*m.b33
                        + 128*m.b16*m.b20*m.b30*m.b34 + 64*m.b16*m.b20*m.b31*m.b35 + 576*m.b16*m.b21*m.b22*m.b27 + 512*
                       m.b16*m.b21*m.b23*m.b28 + 448*m.b16*m.b21*m.b24*m.b29 + 384*m.b16*m.b21*m.b25*m.b30 + 320*m.b16*
                       m.b21*m.b26*m.b31 + 256*m.b16*m.b21*m.b27*m.b32 + 192*m.b16*m.b21*m.b28*m.b33 + 128*m.b16*m.b21*
                       m.b29*m.b34 + 64*m.b16*m.b21*m.b30*m.b35 + 448*m.b16*m.b22*m.b23*m.b29 + 384*m.b16*m.b22*m.b24*
                       m.b30 + 320*m.b16*m.b22*m.b25*m.b31 + 256*m.b16*m.b22*m.b26*m.b32 + 192*m.b16*m.b22*m.b27*m.b33
                        + 128*m.b16*m.b22*m.b28*m.b34 + 64*m.b16*m.b22*m.b29*m.b35 + 320*m.b16*m.b23*m.b24*m.b31 + 256*
                       m.b16*m.b23*m.b25*m.b32 + 192*m.b16*m.b23*m.b26*m.b33 + 128*m.b16*m.b23*m.b27*m.b34 + 64*m.b16*
                       m.b23*m.b28*m.b35 + 192*m.b16*m.b24*m.b25*m.b33 + 128*m.b16*m.b24*m.b26*m.b34 + 64*m.b16*m.b24*
                       m.b27*m.b35 + 64*m.b16*m.b25*m.b26*m.b35 + 1088*m.b17*m.b18*m.b19*m.b20 + 1024*m.b17*m.b18*m.b20*
                       m.b21 + 960*m.b17*m.b18*m.b21*m.b22 + 896*m.b17*m.b18*m.b22*m.b23 + 832*m.b17*m.b18*m.b23*m.b24
                        + 768*m.b17*m.b18*m.b24*m.b25 + 704*m.b17*m.b18*m.b25*m.b26 + 640*m.b17*m.b18*m.b26*m.b27 + 576*
                       m.b17*m.b18*m.b27*m.b28 + 512*m.b17*m.b18*m.b28*m.b29 + 448*m.b17*m.b18*m.b29*m.b30 + 384*m.b17*
                       m.b18*m.b30*m.b31 + 320*m.b17*m.b18*m.b31*m.b32 + 256*m.b17*m.b18*m.b32*m.b33 + 192*m.b17*m.b18*
                       m.b33*m.b34 + 128*m.b17*m.b18*m.b34*m.b35 + 64*m.b17*m.b18*m.b35*m.b36 + 960*m.b17*m.b19*m.b20*
                       m.b22 + 896*m.b17*m.b19*m.b21*m.b23 + 832*m.b17*m.b19*m.b22*m.b24 + 768*m.b17*m.b19*m.b23*m.b25
                        + 704*m.b17*m.b19*m.b24*m.b26 + 640*m.b17*m.b19*m.b25*m.b27 + 576*m.b17*m.b19*m.b26*m.b28 + 512*
                       m.b17*m.b19*m.b27*m.b29 + 448*m.b17*m.b19*m.b28*m.b30 + 384*m.b17*m.b19*m.b29*m.b31 + 320*m.b17*
                       m.b19*m.b30*m.b32 + 256*m.b17*m.b19*m.b31*m.b33 + 192*m.b17*m.b19*m.b32*m.b34 + 128*m.b17*m.b19*
                       m.b33*m.b35 + 64*m.b17*m.b19*m.b34*m.b36 + 832*m.b17*m.b20*m.b21*m.b24 + 768*m.b17*m.b20*m.b22*
                       m.b25 + 704*m.b17*m.b20*m.b23*m.b26 + 640*m.b17*m.b20*m.b24*m.b27 + 576*m.b17*m.b20*m.b25*m.b28
                        + 512*m.b17*m.b20*m.b26*m.b29 + 448*m.b17*m.b20*m.b27*m.b30 + 384*m.b17*m.b20*m.b28*m.b31 + 320*
                       m.b17*m.b20*m.b29*m.b32 + 256*m.b17*m.b20*m.b30*m.b33 + 192*m.b17*m.b20*m.b31*m.b34 + 128*m.b17*
                       m.b20*m.b32*m.b35 + 64*m.b17*m.b20*m.b33*m.b36 + 704*m.b17*m.b21*m.b22*m.b26 + 640*m.b17*m.b21*
                       m.b23*m.b27 + 576*m.b17*m.b21*m.b24*m.b28 + 512*m.b17*m.b21*m.b25*m.b29 + 448*m.b17*m.b21*m.b26*
                       m.b30 + 384*m.b17*m.b21*m.b27*m.b31 + 320*m.b17*m.b21*m.b28*m.b32 + 256*m.b17*m.b21*m.b29*m.b33
                        + 192*m.b17*m.b21*m.b30*m.b34 + 128*m.b17*m.b21*m.b31*m.b35 + 64*m.b17*m.b21*m.b32*m.b36 + 576*
                       m.b17*m.b22*m.b23*m.b28 + 512*m.b17*m.b22*m.b24*m.b29 + 448*m.b17*m.b22*m.b25*m.b30 + 384*m.b17*
                       m.b22*m.b26*m.b31 + 320*m.b17*m.b22*m.b27*m.b32 + 256*m.b17*m.b22*m.b28*m.b33 + 192*m.b17*m.b22*
                       m.b29*m.b34 + 128*m.b17*m.b22*m.b30*m.b35 + 64*m.b17*m.b22*m.b31*m.b36 + 448*m.b17*m.b23*m.b24*
                       m.b30 + 384*m.b17*m.b23*m.b25*m.b31 + 320*m.b17*m.b23*m.b26*m.b32 + 256*m.b17*m.b23*m.b27*m.b33
                        + 192*m.b17*m.b23*m.b28*m.b34 + 128*m.b17*m.b23*m.b29*m.b35 + 64*m.b17*m.b23*m.b30*m.b36 + 320*
                       m.b17*m.b24*m.b25*m.b32 + 256*m.b17*m.b24*m.b26*m.b33 + 192*m.b17*m.b24*m.b27*m.b34 + 128*m.b17*
                       m.b24*m.b28*m.b35 + 64*m.b17*m.b24*m.b29*m.b36 + 192*m.b17*m.b25*m.b26*m.b34 + 128*m.b17*m.b25*
                       m.b27*m.b35 + 64*m.b17*m.b25*m.b28*m.b36 + 64*m.b17*m.b26*m.b27*m.b36 + 1088*m.b18*m.b19*m.b20*
                       m.b21 + 1024*m.b18*m.b19*m.b21*m.b22 + 960*m.b18*m.b19*m.b22*m.b23 + 896*m.b18*m.b19*m.b23*m.b24
                        + 832*m.b18*m.b19*m.b24*m.b25 + 768*m.b18*m.b19*m.b25*m.b26 + 704*m.b18*m.b19*m.b26*m.b27 + 640*
                       m.b18*m.b19*m.b27*m.b28 + 576*m.b18*m.b19*m.b28*m.b29 + 512*m.b18*m.b19*m.b29*m.b30 + 448*m.b18*
                       m.b19*m.b30*m.b31 + 384*m.b18*m.b19*m.b31*m.b32 + 320*m.b18*m.b19*m.b32*m.b33 + 256*m.b18*m.b19*
                       m.b33*m.b34 + 192*m.b18*m.b19*m.b34*m.b35 + 128*m.b18*m.b19*m.b35*m.b36 + 64*m.b18*m.b19*m.b36*
                       m.b37 + 960*m.b18*m.b20*m.b21*m.b23 + 896*m.b18*m.b20*m.b22*m.b24 + 832*m.b18*m.b20*m.b23*m.b25
                        + 768*m.b18*m.b20*m.b24*m.b26 + 704*m.b18*m.b20*m.b25*m.b27 + 640*m.b18*m.b20*m.b26*m.b28 + 576*
                       m.b18*m.b20*m.b27*m.b29 + 512*m.b18*m.b20*m.b28*m.b30 + 448*m.b18*m.b20*m.b29*m.b31 + 384*m.b18*
                       m.b20*m.b30*m.b32 + 320*m.b18*m.b20*m.b31*m.b33 + 256*m.b18*m.b20*m.b32*m.b34 + 192*m.b18*m.b20*
                       m.b33*m.b35 + 128*m.b18*m.b20*m.b34*m.b36 + 64*m.b18*m.b20*m.b35*m.b37 + 832*m.b18*m.b21*m.b22*
                       m.b25 + 768*m.b18*m.b21*m.b23*m.b26 + 704*m.b18*m.b21*m.b24*m.b27 + 640*m.b18*m.b21*m.b25*m.b28
                        + 576*m.b18*m.b21*m.b26*m.b29 + 512*m.b18*m.b21*m.b27*m.b30 + 448*m.b18*m.b21*m.b28*m.b31 + 384*
                       m.b18*m.b21*m.b29*m.b32 + 320*m.b18*m.b21*m.b30*m.b33 + 256*m.b18*m.b21*m.b31*m.b34 + 192*m.b18*
                       m.b21*m.b32*m.b35 + 128*m.b18*m.b21*m.b33*m.b36 + 64*m.b18*m.b21*m.b34*m.b37 + 704*m.b18*m.b22*
                       m.b23*m.b27 + 640*m.b18*m.b22*m.b24*m.b28 + 576*m.b18*m.b22*m.b25*m.b29 + 512*m.b18*m.b22*m.b26*
                       m.b30 + 448*m.b18*m.b22*m.b27*m.b31 + 384*m.b18*m.b22*m.b28*m.b32 + 320*m.b18*m.b22*m.b29*m.b33
                        + 256*m.b18*m.b22*m.b30*m.b34 + 192*m.b18*m.b22*m.b31*m.b35 + 128*m.b18*m.b22*m.b32*m.b36 + 64*
                       m.b18*m.b22*m.b33*m.b37 + 576*m.b18*m.b23*m.b24*m.b29 + 512*m.b18*m.b23*m.b25*m.b30 + 448*m.b18*
                       m.b23*m.b26*m.b31 + 384*m.b18*m.b23*m.b27*m.b32 + 320*m.b18*m.b23*m.b28*m.b33 + 256*m.b18*m.b23*
                       m.b29*m.b34 + 192*m.b18*m.b23*m.b30*m.b35 + 128*m.b18*m.b23*m.b31*m.b36 + 64*m.b18*m.b23*m.b32*
                       m.b37 + 448*m.b18*m.b24*m.b25*m.b31 + 384*m.b18*m.b24*m.b26*m.b32 + 320*m.b18*m.b24*m.b27*m.b33
                        + 256*m.b18*m.b24*m.b28*m.b34 + 192*m.b18*m.b24*m.b29*m.b35 + 128*m.b18*m.b24*m.b30*m.b36 + 64*
                       m.b18*m.b24*m.b31*m.b37 + 320*m.b18*m.b25*m.b26*m.b33 + 256*m.b18*m.b25*m.b27*m.b34 + 192*m.b18*
                       m.b25*m.b28*m.b35 + 128*m.b18*m.b25*m.b29*m.b36 + 64*m.b18*m.b25*m.b30*m.b37 + 192*m.b18*m.b26*
                       m.b27*m.b35 + 128*m.b18*m.b26*m.b28*m.b36 + 64*m.b18*m.b26*m.b29*m.b37 + 64*m.b18*m.b27*m.b28*
                       m.b37 + 1088*m.b19*m.b20*m.b21*m.b22 + 1024*m.b19*m.b20*m.b22*m.b23 + 960*m.b19*m.b20*m.b23*m.b24
                        + 896*m.b19*m.b20*m.b24*m.b25 + 832*m.b19*m.b20*m.b25*m.b26 + 768*m.b19*m.b20*m.b26*m.b27 + 704*
                       m.b19*m.b20*m.b27*m.b28 + 640*m.b19*m.b20*m.b28*m.b29 + 576*m.b19*m.b20*m.b29*m.b30 + 512*m.b19*
                       m.b20*m.b30*m.b31 + 448*m.b19*m.b20*m.b31*m.b32 + 384*m.b19*m.b20*m.b32*m.b33 + 320*m.b19*m.b20*
                       m.b33*m.b34 + 256*m.b19*m.b20*m.b34*m.b35 + 192*m.b19*m.b20*m.b35*m.b36 + 128*m.b19*m.b20*m.b36*
                       m.b37 + 64*m.b19*m.b20*m.b37*m.b38 + 960*m.b19*m.b21*m.b22*m.b24 + 896*m.b19*m.b21*m.b23*m.b25 + 
                       832*m.b19*m.b21*m.b24*m.b26 + 768*m.b19*m.b21*m.b25*m.b27 + 704*m.b19*m.b21*m.b26*m.b28 + 640*
                       m.b19*m.b21*m.b27*m.b29 + 576*m.b19*m.b21*m.b28*m.b30 + 512*m.b19*m.b21*m.b29*m.b31 + 448*m.b19*
                       m.b21*m.b30*m.b32 + 384*m.b19*m.b21*m.b31*m.b33 + 320*m.b19*m.b21*m.b32*m.b34 + 256*m.b19*m.b21*
                       m.b33*m.b35 + 192*m.b19*m.b21*m.b34*m.b36 + 128*m.b19*m.b21*m.b35*m.b37 + 64*m.b19*m.b21*m.b36*
                       m.b38 + 832*m.b19*m.b22*m.b23*m.b26 + 768*m.b19*m.b22*m.b24*m.b27 + 704*m.b19*m.b22*m.b25*m.b28
                        + 640*m.b19*m.b22*m.b26*m.b29 + 576*m.b19*m.b22*m.b27*m.b30 + 512*m.b19*m.b22*m.b28*m.b31 + 448*
                       m.b19*m.b22*m.b29*m.b32 + 384*m.b19*m.b22*m.b30*m.b33 + 320*m.b19*m.b22*m.b31*m.b34 + 256*m.b19*
                       m.b22*m.b32*m.b35 + 192*m.b19*m.b22*m.b33*m.b36 + 128*m.b19*m.b22*m.b34*m.b37 + 64*m.b19*m.b22*
                       m.b35*m.b38 + 704*m.b19*m.b23*m.b24*m.b28 + 640*m.b19*m.b23*m.b25*m.b29 + 576*m.b19*m.b23*m.b26*
                       m.b30 + 512*m.b19*m.b23*m.b27*m.b31 + 448*m.b19*m.b23*m.b28*m.b32 + 384*m.b19*m.b23*m.b29*m.b33
                        + 320*m.b19*m.b23*m.b30*m.b34 + 256*m.b19*m.b23*m.b31*m.b35 + 192*m.b19*m.b23*m.b32*m.b36 + 128*
                       m.b19*m.b23*m.b33*m.b37 + 64*m.b19*m.b23*m.b34*m.b38 + 576*m.b19*m.b24*m.b25*m.b30 + 512*m.b19*
                       m.b24*m.b26*m.b31 + 448*m.b19*m.b24*m.b27*m.b32 + 384*m.b19*m.b24*m.b28*m.b33 + 320*m.b19*m.b24*
                       m.b29*m.b34 + 256*m.b19*m.b24*m.b30*m.b35 + 192*m.b19*m.b24*m.b31*m.b36 + 128*m.b19*m.b24*m.b32*
                       m.b37 + 64*m.b19*m.b24*m.b33*m.b38 + 448*m.b19*m.b25*m.b26*m.b32 + 384*m.b19*m.b25*m.b27*m.b33 + 
                       320*m.b19*m.b25*m.b28*m.b34 + 256*m.b19*m.b25*m.b29*m.b35 + 192*m.b19*m.b25*m.b30*m.b36 + 128*
                       m.b19*m.b25*m.b31*m.b37 + 64*m.b19*m.b25*m.b32*m.b38 + 320*m.b19*m.b26*m.b27*m.b34 + 256*m.b19*
                       m.b26*m.b28*m.b35 + 192*m.b19*m.b26*m.b29*m.b36 + 128*m.b19*m.b26*m.b30*m.b37 + 64*m.b19*m.b26*
                       m.b31*m.b38 + 192*m.b19*m.b27*m.b28*m.b36 + 128*m.b19*m.b27*m.b29*m.b37 + 64*m.b19*m.b27*m.b30*
                       m.b38 + 64*m.b19*m.b28*m.b29*m.b38 + 1088*m.b20*m.b21*m.b22*m.b23 + 1024*m.b20*m.b21*m.b23*m.b24
                        + 960*m.b20*m.b21*m.b24*m.b25 + 896*m.b20*m.b21*m.b25*m.b26 + 832*m.b20*m.b21*m.b26*m.b27 + 768*
                       m.b20*m.b21*m.b27*m.b28 + 704*m.b20*m.b21*m.b28*m.b29 + 640*m.b20*m.b21*m.b29*m.b30 + 576*m.b20*
                       m.b21*m.b30*m.b31 + 512*m.b20*m.b21*m.b31*m.b32 + 448*m.b20*m.b21*m.b32*m.b33 + 384*m.b20*m.b21*
                       m.b33*m.b34 + 320*m.b20*m.b21*m.b34*m.b35 + 256*m.b20*m.b21*m.b35*m.b36 + 192*m.b20*m.b21*m.b36*
                       m.b37 + 128*m.b20*m.b21*m.b37*m.b38 + 64*m.b20*m.b21*m.b38*m.b39 + 960*m.b20*m.b22*m.b23*m.b25 + 
                       896*m.b20*m.b22*m.b24*m.b26 + 832*m.b20*m.b22*m.b25*m.b27 + 768*m.b20*m.b22*m.b26*m.b28 + 704*
                       m.b20*m.b22*m.b27*m.b29 + 640*m.b20*m.b22*m.b28*m.b30 + 576*m.b20*m.b22*m.b29*m.b31 + 512*m.b20*
                       m.b22*m.b30*m.b32 + 448*m.b20*m.b22*m.b31*m.b33 + 384*m.b20*m.b22*m.b32*m.b34 + 320*m.b20*m.b22*
                       m.b33*m.b35 + 256*m.b20*m.b22*m.b34*m.b36 + 192*m.b20*m.b22*m.b35*m.b37 + 128*m.b20*m.b22*m.b36*
                       m.b38 + 64*m.b20*m.b22*m.b37*m.b39 + 832*m.b20*m.b23*m.b24*m.b27 + 768*m.b20*m.b23*m.b25*m.b28 + 
                       704*m.b20*m.b23*m.b26*m.b29 + 640*m.b20*m.b23*m.b27*m.b30 + 576*m.b20*m.b23*m.b28*m.b31 + 512*
                       m.b20*m.b23*m.b29*m.b32 + 448*m.b20*m.b23*m.b30*m.b33 + 384*m.b20*m.b23*m.b31*m.b34 + 320*m.b20*
                       m.b23*m.b32*m.b35 + 256*m.b20*m.b23*m.b33*m.b36 + 192*m.b20*m.b23*m.b34*m.b37 + 128*m.b20*m.b23*
                       m.b35*m.b38 + 64*m.b20*m.b23*m.b36*m.b39 + 704*m.b20*m.b24*m.b25*m.b29 + 640*m.b20*m.b24*m.b26*
                       m.b30 + 576*m.b20*m.b24*m.b27*m.b31 + 512*m.b20*m.b24*m.b28*m.b32 + 448*m.b20*m.b24*m.b29*m.b33
                        + 384*m.b20*m.b24*m.b30*m.b34 + 320*m.b20*m.b24*m.b31*m.b35 + 256*m.b20*m.b24*m.b32*m.b36 + 192*
                       m.b20*m.b24*m.b33*m.b37 + 128*m.b20*m.b24*m.b34*m.b38 + 64*m.b20*m.b24*m.b35*m.b39 + 576*m.b20*
                       m.b25*m.b26*m.b31 + 512*m.b20*m.b25*m.b27*m.b32 + 448*m.b20*m.b25*m.b28*m.b33 + 384*m.b20*m.b25*
                       m.b29*m.b34 + 320*m.b20*m.b25*m.b30*m.b35 + 256*m.b20*m.b25*m.b31*m.b36 + 192*m.b20*m.b25*m.b32*
                       m.b37 + 128*m.b20*m.b25*m.b33*m.b38 + 64*m.b20*m.b25*m.b34*m.b39 + 448*m.b20*m.b26*m.b27*m.b33 + 
                       384*m.b20*m.b26*m.b28*m.b34 + 320*m.b20*m.b26*m.b29*m.b35 + 256*m.b20*m.b26*m.b30*m.b36 + 192*
                       m.b20*m.b26*m.b31*m.b37 + 128*m.b20*m.b26*m.b32*m.b38 + 64*m.b20*m.b26*m.b33*m.b39 + 320*m.b20*
                       m.b27*m.b28*m.b35 + 256*m.b20*m.b27*m.b29*m.b36 + 192*m.b20*m.b27*m.b30*m.b37 + 128*m.b20*m.b27*
                       m.b31*m.b38 + 64*m.b20*m.b27*m.b32*m.b39 + 192*m.b20*m.b28*m.b29*m.b37 + 128*m.b20*m.b28*m.b30*
                       m.b38 + 64*m.b20*m.b28*m.b31*m.b39 + 64*m.b20*m.b29*m.b30*m.b39 + 1088*m.b21*m.b22*m.b23*m.b24 + 
                       1024*m.b21*m.b22*m.b24*m.b25 + 960*m.b21*m.b22*m.b25*m.b26 + 896*m.b21*m.b22*m.b26*m.b27 + 832*
                       m.b21*m.b22*m.b27*m.b28 + 768*m.b21*m.b22*m.b28*m.b29 + 704*m.b21*m.b22*m.b29*m.b30 + 640*m.b21*
                       m.b22*m.b30*m.b31 + 576*m.b21*m.b22*m.b31*m.b32 + 512*m.b21*m.b22*m.b32*m.b33 + 448*m.b21*m.b22*
                       m.b33*m.b34 + 384*m.b21*m.b22*m.b34*m.b35 + 320*m.b21*m.b22*m.b35*m.b36 + 256*m.b21*m.b22*m.b36*
                       m.b37 + 192*m.b21*m.b22*m.b37*m.b38 + 128*m.b21*m.b22*m.b38*m.b39 + 64*m.b21*m.b22*m.b39*m.b40 + 
                       960*m.b21*m.b23*m.b24*m.b26 + 896*m.b21*m.b23*m.b25*m.b27 + 832*m.b21*m.b23*m.b26*m.b28 + 768*
                       m.b21*m.b23*m.b27*m.b29 + 704*m.b21*m.b23*m.b28*m.b30 + 640*m.b21*m.b23*m.b29*m.b31 + 576*m.b21*
                       m.b23*m.b30*m.b32 + 512*m.b21*m.b23*m.b31*m.b33 + 448*m.b21*m.b23*m.b32*m.b34 + 384*m.b21*m.b23*
                       m.b33*m.b35 + 320*m.b21*m.b23*m.b34*m.b36 + 256*m.b21*m.b23*m.b35*m.b37 + 192*m.b21*m.b23*m.b36*
                       m.b38 + 128*m.b21*m.b23*m.b37*m.b39 + 64*m.b21*m.b23*m.b38*m.b40 + 832*m.b21*m.b24*m.b25*m.b28 + 
                       768*m.b21*m.b24*m.b26*m.b29 + 704*m.b21*m.b24*m.b27*m.b30 + 640*m.b21*m.b24*m.b28*m.b31 + 576*
                       m.b21*m.b24*m.b29*m.b32 + 512*m.b21*m.b24*m.b30*m.b33 + 448*m.b21*m.b24*m.b31*m.b34 + 384*m.b21*
                       m.b24*m.b32*m.b35 + 320*m.b21*m.b24*m.b33*m.b36 + 256*m.b21*m.b24*m.b34*m.b37 + 192*m.b21*m.b24*
                       m.b35*m.b38 + 128*m.b21*m.b24*m.b36*m.b39 + 64*m.b21*m.b24*m.b37*m.b40 + 704*m.b21*m.b25*m.b26*
                       m.b30 + 640*m.b21*m.b25*m.b27*m.b31 + 576*m.b21*m.b25*m.b28*m.b32 + 512*m.b21*m.b25*m.b29*m.b33
                        + 448*m.b21*m.b25*m.b30*m.b34 + 384*m.b21*m.b25*m.b31*m.b35 + 320*m.b21*m.b25*m.b32*m.b36 + 256*
                       m.b21*m.b25*m.b33*m.b37 + 192*m.b21*m.b25*m.b34*m.b38 + 128*m.b21*m.b25*m.b35*m.b39 + 64*m.b21*
                       m.b25*m.b36*m.b40 + 576*m.b21*m.b26*m.b27*m.b32 + 512*m.b21*m.b26*m.b28*m.b33 + 448*m.b21*m.b26*
                       m.b29*m.b34 + 384*m.b21*m.b26*m.b30*m.b35 + 320*m.b21*m.b26*m.b31*m.b36 + 256*m.b21*m.b26*m.b32*
                       m.b37 + 192*m.b21*m.b26*m.b33*m.b38 + 128*m.b21*m.b26*m.b34*m.b39 + 64*m.b21*m.b26*m.b35*m.b40 + 
                       448*m.b21*m.b27*m.b28*m.b34 + 384*m.b21*m.b27*m.b29*m.b35 + 320*m.b21*m.b27*m.b30*m.b36 + 256*
                       m.b21*m.b27*m.b31*m.b37 + 192*m.b21*m.b27*m.b32*m.b38 + 128*m.b21*m.b27*m.b33*m.b39 + 64*m.b21*
                       m.b27*m.b34*m.b40 + 320*m.b21*m.b28*m.b29*m.b36 + 256*m.b21*m.b28*m.b30*m.b37 + 192*m.b21*m.b28*
                       m.b31*m.b38 + 128*m.b21*m.b28*m.b32*m.b39 + 64*m.b21*m.b28*m.b33*m.b40 + 192*m.b21*m.b29*m.b30*
                       m.b38 + 128*m.b21*m.b29*m.b31*m.b39 + 64*m.b21*m.b29*m.b32*m.b40 + 64*m.b21*m.b30*m.b31*m.b40 + 
                       1024*m.b22*m.b23*m.b24*m.b25 + 960*m.b22*m.b23*m.b25*m.b26 + 896*m.b22*m.b23*m.b26*m.b27 + 832*
                       m.b22*m.b23*m.b27*m.b28 + 768*m.b22*m.b23*m.b28*m.b29 + 704*m.b22*m.b23*m.b29*m.b30 + 640*m.b22*
                       m.b23*m.b30*m.b31 + 576*m.b22*m.b23*m.b31*m.b32 + 512*m.b22*m.b23*m.b32*m.b33 + 448*m.b22*m.b23*
                       m.b33*m.b34 + 384*m.b22*m.b23*m.b34*m.b35 + 320*m.b22*m.b23*m.b35*m.b36 + 256*m.b22*m.b23*m.b36*
                       m.b37 + 192*m.b22*m.b23*m.b37*m.b38 + 128*m.b22*m.b23*m.b38*m.b39 + 64*m.b22*m.b23*m.b39*m.b40 + 
                       896*m.b22*m.b24*m.b25*m.b27 + 832*m.b22*m.b24*m.b26*m.b28 + 768*m.b22*m.b24*m.b27*m.b29 + 704*
                       m.b22*m.b24*m.b28*m.b30 + 640*m.b22*m.b24*m.b29*m.b31 + 576*m.b22*m.b24*m.b30*m.b32 + 512*m.b22*
                       m.b24*m.b31*m.b33 + 448*m.b22*m.b24*m.b32*m.b34 + 384*m.b22*m.b24*m.b33*m.b35 + 320*m.b22*m.b24*
                       m.b34*m.b36 + 256*m.b22*m.b24*m.b35*m.b37 + 192*m.b22*m.b24*m.b36*m.b38 + 128*m.b22*m.b24*m.b37*
                       m.b39 + 64*m.b22*m.b24*m.b38*m.b40 + 768*m.b22*m.b25*m.b26*m.b29 + 704*m.b22*m.b25*m.b27*m.b30 + 
                       640*m.b22*m.b25*m.b28*m.b31 + 576*m.b22*m.b25*m.b29*m.b32 + 512*m.b22*m.b25*m.b30*m.b33 + 448*
                       m.b22*m.b25*m.b31*m.b34 + 384*m.b22*m.b25*m.b32*m.b35 + 320*m.b22*m.b25*m.b33*m.b36 + 256*m.b22*
                       m.b25*m.b34*m.b37 + 192*m.b22*m.b25*m.b35*m.b38 + 128*m.b22*m.b25*m.b36*m.b39 + 64*m.b22*m.b25*
                       m.b37*m.b40 + 640*m.b22*m.b26*m.b27*m.b31 + 576*m.b22*m.b26*m.b28*m.b32 + 512*m.b22*m.b26*m.b29*
                       m.b33 + 448*m.b22*m.b26*m.b30*m.b34 + 384*m.b22*m.b26*m.b31*m.b35 + 320*m.b22*m.b26*m.b32*m.b36
                        + 256*m.b22*m.b26*m.b33*m.b37 + 192*m.b22*m.b26*m.b34*m.b38 + 128*m.b22*m.b26*m.b35*m.b39 + 64*
                       m.b22*m.b26*m.b36*m.b40 + 512*m.b22*m.b27*m.b28*m.b33 + 448*m.b22*m.b27*m.b29*m.b34 + 384*m.b22*
                       m.b27*m.b30*m.b35 + 320*m.b22*m.b27*m.b31*m.b36 + 256*m.b22*m.b27*m.b32*m.b37 + 192*m.b22*m.b27*
                       m.b33*m.b38 + 128*m.b22*m.b27*m.b34*m.b39 + 64*m.b22*m.b27*m.b35*m.b40 + 384*m.b22*m.b28*m.b29*
                       m.b35 + 320*m.b22*m.b28*m.b30*m.b36 + 256*m.b22*m.b28*m.b31*m.b37 + 192*m.b22*m.b28*m.b32*m.b38
                        + 128*m.b22*m.b28*m.b33*m.b39 + 64*m.b22*m.b28*m.b34*m.b40 + 256*m.b22*m.b29*m.b30*m.b37 + 192*
                       m.b22*m.b29*m.b31*m.b38 + 128*m.b22*m.b29*m.b32*m.b39 + 64*m.b22*m.b29*m.b33*m.b40 + 128*m.b22*
                       m.b30*m.b31*m.b39 + 64*m.b22*m.b30*m.b32*m.b40 + 960*m.b23*m.b24*m.b25*m.b26 + 896*m.b23*m.b24*
                       m.b26*m.b27 + 832*m.b23*m.b24*m.b27*m.b28 + 768*m.b23*m.b24*m.b28*m.b29 + 704*m.b23*m.b24*m.b29*
                       m.b30 + 640*m.b23*m.b24*m.b30*m.b31 + 576*m.b23*m.b24*m.b31*m.b32 + 512*m.b23*m.b24*m.b32*m.b33
                        + 448*m.b23*m.b24*m.b33*m.b34 + 384*m.b23*m.b24*m.b34*m.b35 + 320*m.b23*m.b24*m.b35*m.b36 + 256*
                       m.b23*m.b24*m.b36*m.b37 + 192*m.b23*m.b24*m.b37*m.b38 + 128*m.b23*m.b24*m.b38*m.b39 + 64*m.b23*
                       m.b24*m.b39*m.b40 + 832*m.b23*m.b25*m.b26*m.b28 + 768*m.b23*m.b25*m.b27*m.b29 + 704*m.b23*m.b25*
                       m.b28*m.b30 + 640*m.b23*m.b25*m.b29*m.b31 + 576*m.b23*m.b25*m.b30*m.b32 + 512*m.b23*m.b25*m.b31*
                       m.b33 + 448*m.b23*m.b25*m.b32*m.b34 + 384*m.b23*m.b25*m.b33*m.b35 + 320*m.b23*m.b25*m.b34*m.b36
                        + 256*m.b23*m.b25*m.b35*m.b37 + 192*m.b23*m.b25*m.b36*m.b38 + 128*m.b23*m.b25*m.b37*m.b39 + 64*
                       m.b23*m.b25*m.b38*m.b40 + 704*m.b23*m.b26*m.b27*m.b30 + 640*m.b23*m.b26*m.b28*m.b31 + 576*m.b23*
                       m.b26*m.b29*m.b32 + 512*m.b23*m.b26*m.b30*m.b33 + 448*m.b23*m.b26*m.b31*m.b34 + 384*m.b23*m.b26*
                       m.b32*m.b35 + 320*m.b23*m.b26*m.b33*m.b36 + 256*m.b23*m.b26*m.b34*m.b37 + 192*m.b23*m.b26*m.b35*
                       m.b38 + 128*m.b23*m.b26*m.b36*m.b39 + 64*m.b23*m.b26*m.b37*m.b40 + 576*m.b23*m.b27*m.b28*m.b32 + 
                       512*m.b23*m.b27*m.b29*m.b33 + 448*m.b23*m.b27*m.b30*m.b34 + 384*m.b23*m.b27*m.b31*m.b35 + 320*
                       m.b23*m.b27*m.b32*m.b36 + 256*m.b23*m.b27*m.b33*m.b37 + 192*m.b23*m.b27*m.b34*m.b38 + 128*m.b23*
                       m.b27*m.b35*m.b39 + 64*m.b23*m.b27*m.b36*m.b40 + 448*m.b23*m.b28*m.b29*m.b34 + 384*m.b23*m.b28*
                       m.b30*m.b35 + 320*m.b23*m.b28*m.b31*m.b36 + 256*m.b23*m.b28*m.b32*m.b37 + 192*m.b23*m.b28*m.b33*
                       m.b38 + 128*m.b23*m.b28*m.b34*m.b39 + 64*m.b23*m.b28*m.b35*m.b40 + 320*m.b23*m.b29*m.b30*m.b36 + 
                       256*m.b23*m.b29*m.b31*m.b37 + 192*m.b23*m.b29*m.b32*m.b38 + 128*m.b23*m.b29*m.b33*m.b39 + 64*
                       m.b23*m.b29*m.b34*m.b40 + 192*m.b23*m.b30*m.b31*m.b38 + 128*m.b23*m.b30*m.b32*m.b39 + 64*m.b23*
                       m.b30*m.b33*m.b40 + 64*m.b23*m.b31*m.b32*m.b40 + 896*m.b24*m.b25*m.b26*m.b27 + 832*m.b24*m.b25*
                       m.b27*m.b28 + 768*m.b24*m.b25*m.b28*m.b29 + 704*m.b24*m.b25*m.b29*m.b30 + 640*m.b24*m.b25*m.b30*
                       m.b31 + 576*m.b24*m.b25*m.b31*m.b32 + 512*m.b24*m.b25*m.b32*m.b33 + 448*m.b24*m.b25*m.b33*m.b34
                        + 384*m.b24*m.b25*m.b34*m.b35 + 320*m.b24*m.b25*m.b35*m.b36 + 256*m.b24*m.b25*m.b36*m.b37 + 192*
                       m.b24*m.b25*m.b37*m.b38 + 128*m.b24*m.b25*m.b38*m.b39 + 64*m.b24*m.b25*m.b39*m.b40 + 768*m.b24*
                       m.b26*m.b27*m.b29 + 704*m.b24*m.b26*m.b28*m.b30 + 640*m.b24*m.b26*m.b29*m.b31 + 576*m.b24*m.b26*
                       m.b30*m.b32 + 512*m.b24*m.b26*m.b31*m.b33 + 448*m.b24*m.b26*m.b32*m.b34 + 384*m.b24*m.b26*m.b33*
                       m.b35 + 320*m.b24*m.b26*m.b34*m.b36 + 256*m.b24*m.b26*m.b35*m.b37 + 192*m.b24*m.b26*m.b36*m.b38
                        + 128*m.b24*m.b26*m.b37*m.b39 + 64*m.b24*m.b26*m.b38*m.b40 + 640*m.b24*m.b27*m.b28*m.b31 + 576*
                       m.b24*m.b27*m.b29*m.b32 + 512*m.b24*m.b27*m.b30*m.b33 + 448*m.b24*m.b27*m.b31*m.b34 + 384*m.b24*
                       m.b27*m.b32*m.b35 + 320*m.b24*m.b27*m.b33*m.b36 + 256*m.b24*m.b27*m.b34*m.b37 + 192*m.b24*m.b27*
                       m.b35*m.b38 + 128*m.b24*m.b27*m.b36*m.b39 + 64*m.b24*m.b27*m.b37*m.b40 + 512*m.b24*m.b28*m.b29*
                       m.b33 + 448*m.b24*m.b28*m.b30*m.b34 + 384*m.b24*m.b28*m.b31*m.b35 + 320*m.b24*m.b28*m.b32*m.b36
                        + 256*m.b24*m.b28*m.b33*m.b37 + 192*m.b24*m.b28*m.b34*m.b38 + 128*m.b24*m.b28*m.b35*m.b39 + 64*
                       m.b24*m.b28*m.b36*m.b40 + 384*m.b24*m.b29*m.b30*m.b35 + 320*m.b24*m.b29*m.b31*m.b36 + 256*m.b24*
                       m.b29*m.b32*m.b37 + 192*m.b24*m.b29*m.b33*m.b38 + 128*m.b24*m.b29*m.b34*m.b39 + 64*m.b24*m.b29*
                       m.b35*m.b40 + 256*m.b24*m.b30*m.b31*m.b37 + 192*m.b24*m.b30*m.b32*m.b38 + 128*m.b24*m.b30*m.b33*
                       m.b39 + 64*m.b24*m.b30*m.b34*m.b40 + 128*m.b24*m.b31*m.b32*m.b39 + 64*m.b24*m.b31*m.b33*m.b40 + 
                       832*m.b25*m.b26*m.b27*m.b28 + 768*m.b25*m.b26*m.b28*m.b29 + 704*m.b25*m.b26*m.b29*m.b30 + 640*
                       m.b25*m.b26*m.b30*m.b31 + 576*m.b25*m.b26*m.b31*m.b32 + 512*m.b25*m.b26*m.b32*m.b33 + 448*m.b25*
                       m.b26*m.b33*m.b34 + 384*m.b25*m.b26*m.b34*m.b35 + 320*m.b25*m.b26*m.b35*m.b36 + 256*m.b25*m.b26*
                       m.b36*m.b37 + 192*m.b25*m.b26*m.b37*m.b38 + 128*m.b25*m.b26*m.b38*m.b39 + 64*m.b25*m.b26*m.b39*
                       m.b40 + 704*m.b25*m.b27*m.b28*m.b30 + 640*m.b25*m.b27*m.b29*m.b31 + 576*m.b25*m.b27*m.b30*m.b32
                        + 512*m.b25*m.b27*m.b31*m.b33 + 448*m.b25*m.b27*m.b32*m.b34 + 384*m.b25*m.b27*m.b33*m.b35 + 320*
                       m.b25*m.b27*m.b34*m.b36 + 256*m.b25*m.b27*m.b35*m.b37 + 192*m.b25*m.b27*m.b36*m.b38 + 128*m.b25*
                       m.b27*m.b37*m.b39 + 64*m.b25*m.b27*m.b38*m.b40 + 576*m.b25*m.b28*m.b29*m.b32 + 512*m.b25*m.b28*
                       m.b30*m.b33 + 448*m.b25*m.b28*m.b31*m.b34 + 384*m.b25*m.b28*m.b32*m.b35 + 320*m.b25*m.b28*m.b33*
                       m.b36 + 256*m.b25*m.b28*m.b34*m.b37 + 192*m.b25*m.b28*m.b35*m.b38 + 128*m.b25*m.b28*m.b36*m.b39
                        + 64*m.b25*m.b28*m.b37*m.b40 + 448*m.b25*m.b29*m.b30*m.b34 + 384*m.b25*m.b29*m.b31*m.b35 + 320*
                       m.b25*m.b29*m.b32*m.b36 + 256*m.b25*m.b29*m.b33*m.b37 + 192*m.b25*m.b29*m.b34*m.b38 + 128*m.b25*
                       m.b29*m.b35*m.b39 + 64*m.b25*m.b29*m.b36*m.b40 + 320*m.b25*m.b30*m.b31*m.b36 + 256*m.b25*m.b30*
                       m.b32*m.b37 + 192*m.b25*m.b30*m.b33*m.b38 + 128*m.b25*m.b30*m.b34*m.b39 + 64*m.b25*m.b30*m.b35*
                       m.b40 + 192*m.b25*m.b31*m.b32*m.b38 + 128*m.b25*m.b31*m.b33*m.b39 + 64*m.b25*m.b31*m.b34*m.b40 + 
                       64*m.b25*m.b32*m.b33*m.b40 + 768*m.b26*m.b27*m.b28*m.b29 + 704*m.b26*m.b27*m.b29*m.b30 + 640*
                       m.b26*m.b27*m.b30*m.b31 + 576*m.b26*m.b27*m.b31*m.b32 + 512*m.b26*m.b27*m.b32*m.b33 + 448*m.b26*
                       m.b27*m.b33*m.b34 + 384*m.b26*m.b27*m.b34*m.b35 + 320*m.b26*m.b27*m.b35*m.b36 + 256*m.b26*m.b27*
                       m.b36*m.b37 + 192*m.b26*m.b27*m.b37*m.b38 + 128*m.b26*m.b27*m.b38*m.b39 + 64*m.b26*m.b27*m.b39*
                       m.b40 + 640*m.b26*m.b28*m.b29*m.b31 + 576*m.b26*m.b28*m.b30*m.b32 + 512*m.b26*m.b28*m.b31*m.b33
                        + 448*m.b26*m.b28*m.b32*m.b34 + 384*m.b26*m.b28*m.b33*m.b35 + 320*m.b26*m.b28*m.b34*m.b36 + 256*
                       m.b26*m.b28*m.b35*m.b37 + 192*m.b26*m.b28*m.b36*m.b38 + 128*m.b26*m.b28*m.b37*m.b39 + 64*m.b26*
                       m.b28*m.b38*m.b40 + 512*m.b26*m.b29*m.b30*m.b33 + 448*m.b26*m.b29*m.b31*m.b34 + 384*m.b26*m.b29*
                       m.b32*m.b35 + 320*m.b26*m.b29*m.b33*m.b36 + 256*m.b26*m.b29*m.b34*m.b37 + 192*m.b26*m.b29*m.b35*
                       m.b38 + 128*m.b26*m.b29*m.b36*m.b39 + 64*m.b26*m.b29*m.b37*m.b40 + 384*m.b26*m.b30*m.b31*m.b35 + 
                       320*m.b26*m.b30*m.b32*m.b36 + 256*m.b26*m.b30*m.b33*m.b37 + 192*m.b26*m.b30*m.b34*m.b38 + 128*
                       m.b26*m.b30*m.b35*m.b39 + 64*m.b26*m.b30*m.b36*m.b40 + 256*m.b26*m.b31*m.b32*m.b37 + 192*m.b26*
                       m.b31*m.b33*m.b38 + 128*m.b26*m.b31*m.b34*m.b39 + 64*m.b26*m.b31*m.b35*m.b40 + 128*m.b26*m.b32*
                       m.b33*m.b39 + 64*m.b26*m.b32*m.b34*m.b40 + 704*m.b27*m.b28*m.b29*m.b30 + 640*m.b27*m.b28*m.b30*
                       m.b31 + 576*m.b27*m.b28*m.b31*m.b32 + 512*m.b27*m.b28*m.b32*m.b33 + 448*m.b27*m.b28*m.b33*m.b34
                        + 384*m.b27*m.b28*m.b34*m.b35 + 320*m.b27*m.b28*m.b35*m.b36 + 256*m.b27*m.b28*m.b36*m.b37 + 192*
                       m.b27*m.b28*m.b37*m.b38 + 128*m.b27*m.b28*m.b38*m.b39 + 64*m.b27*m.b28*m.b39*m.b40 + 576*m.b27*
                       m.b29*m.b30*m.b32 + 512*m.b27*m.b29*m.b31*m.b33 + 448*m.b27*m.b29*m.b32*m.b34 + 384*m.b27*m.b29*
                       m.b33*m.b35 + 320*m.b27*m.b29*m.b34*m.b36 + 256*m.b27*m.b29*m.b35*m.b37 + 192*m.b27*m.b29*m.b36*
                       m.b38 + 128*m.b27*m.b29*m.b37*m.b39 + 64*m.b27*m.b29*m.b38*m.b40 + 448*m.b27*m.b30*m.b31*m.b34 + 
                       384*m.b27*m.b30*m.b32*m.b35 + 320*m.b27*m.b30*m.b33*m.b36 + 256*m.b27*m.b30*m.b34*m.b37 + 192*
                       m.b27*m.b30*m.b35*m.b38 + 128*m.b27*m.b30*m.b36*m.b39 + 64*m.b27*m.b30*m.b37*m.b40 + 320*m.b27*
                       m.b31*m.b32*m.b36 + 256*m.b27*m.b31*m.b33*m.b37 + 192*m.b27*m.b31*m.b34*m.b38 + 128*m.b27*m.b31*
                       m.b35*m.b39 + 64*m.b27*m.b31*m.b36*m.b40 + 192*m.b27*m.b32*m.b33*m.b38 + 128*m.b27*m.b32*m.b34*
                       m.b39 + 64*m.b27*m.b32*m.b35*m.b40 + 64*m.b27*m.b33*m.b34*m.b40 + 640*m.b28*m.b29*m.b30*m.b31 + 
                       576*m.b28*m.b29*m.b31*m.b32 + 512*m.b28*m.b29*m.b32*m.b33 + 448*m.b28*m.b29*m.b33*m.b34 + 384*
                       m.b28*m.b29*m.b34*m.b35 + 320*m.b28*m.b29*m.b35*m.b36 + 256*m.b28*m.b29*m.b36*m.b37 + 192*m.b28*
                       m.b29*m.b37*m.b38 + 128*m.b28*m.b29*m.b38*m.b39 + 64*m.b28*m.b29*m.b39*m.b40 + 512*m.b28*m.b30*
                       m.b31*m.b33 + 448*m.b28*m.b30*m.b32*m.b34 + 384*m.b28*m.b30*m.b33*m.b35 + 320*m.b28*m.b30*m.b34*
                       m.b36 + 256*m.b28*m.b30*m.b35*m.b37 + 192*m.b28*m.b30*m.b36*m.b38 + 128*m.b28*m.b30*m.b37*m.b39
                        + 64*m.b28*m.b30*m.b38*m.b40 + 384*m.b28*m.b31*m.b32*m.b35 + 320*m.b28*m.b31*m.b33*m.b36 + 256*
                       m.b28*m.b31*m.b34*m.b37 + 192*m.b28*m.b31*m.b35*m.b38 + 128*m.b28*m.b31*m.b36*m.b39 + 64*m.b28*
                       m.b31*m.b37*m.b40 + 256*m.b28*m.b32*m.b33*m.b37 + 192*m.b28*m.b32*m.b34*m.b38 + 128*m.b28*m.b32*
                       m.b35*m.b39 + 64*m.b28*m.b32*m.b36*m.b40 + 128*m.b28*m.b33*m.b34*m.b39 + 64*m.b28*m.b33*m.b35*
                       m.b40 + 576*m.b29*m.b30*m.b31*m.b32 + 512*m.b29*m.b30*m.b32*m.b33 + 448*m.b29*m.b30*m.b33*m.b34
                        + 384*m.b29*m.b30*m.b34*m.b35 + 320*m.b29*m.b30*m.b35*m.b36 + 256*m.b29*m.b30*m.b36*m.b37 + 192*
                       m.b29*m.b30*m.b37*m.b38 + 128*m.b29*m.b30*m.b38*m.b39 + 64*m.b29*m.b30*m.b39*m.b40 + 448*m.b29*
                       m.b31*m.b32*m.b34 + 384*m.b29*m.b31*m.b33*m.b35 + 320*m.b29*m.b31*m.b34*m.b36 + 256*m.b29*m.b31*
                       m.b35*m.b37 + 192*m.b29*m.b31*m.b36*m.b38 + 128*m.b29*m.b31*m.b37*m.b39 + 64*m.b29*m.b31*m.b38*
                       m.b40 + 320*m.b29*m.b32*m.b33*m.b36 + 256*m.b29*m.b32*m.b34*m.b37 + 192*m.b29*m.b32*m.b35*m.b38
                        + 128*m.b29*m.b32*m.b36*m.b39 + 64*m.b29*m.b32*m.b37*m.b40 + 192*m.b29*m.b33*m.b34*m.b38 + 128*
                       m.b29*m.b33*m.b35*m.b39 + 64*m.b29*m.b33*m.b36*m.b40 + 64*m.b29*m.b34*m.b35*m.b40 + 512*m.b30*
                       m.b31*m.b32*m.b33 + 448*m.b30*m.b31*m.b33*m.b34 + 384*m.b30*m.b31*m.b34*m.b35 + 320*m.b30*m.b31*
                       m.b35*m.b36 + 256*m.b30*m.b31*m.b36*m.b37 + 192*m.b30*m.b31*m.b37*m.b38 + 128*m.b30*m.b31*m.b38*
                       m.b39 + 64*m.b30*m.b31*m.b39*m.b40 + 384*m.b30*m.b32*m.b33*m.b35 + 320*m.b30*m.b32*m.b34*m.b36 + 
                       256*m.b30*m.b32*m.b35*m.b37 + 192*m.b30*m.b32*m.b36*m.b38 + 128*m.b30*m.b32*m.b37*m.b39 + 64*
                       m.b30*m.b32*m.b38*m.b40 + 256*m.b30*m.b33*m.b34*m.b37 + 192*m.b30*m.b33*m.b35*m.b38 + 128*m.b30*
                       m.b33*m.b36*m.b39 + 64*m.b30*m.b33*m.b37*m.b40 + 128*m.b30*m.b34*m.b35*m.b39 + 64*m.b30*m.b34*
                       m.b36*m.b40 + 448*m.b31*m.b32*m.b33*m.b34 + 384*m.b31*m.b32*m.b34*m.b35 + 320*m.b31*m.b32*m.b35*
                       m.b36 + 256*m.b31*m.b32*m.b36*m.b37 + 192*m.b31*m.b32*m.b37*m.b38 + 128*m.b31*m.b32*m.b38*m.b39
                        + 64*m.b31*m.b32*m.b39*m.b40 + 320*m.b31*m.b33*m.b34*m.b36 + 256*m.b31*m.b33*m.b35*m.b37 + 192*
                       m.b31*m.b33*m.b36*m.b38 + 128*m.b31*m.b33*m.b37*m.b39 + 64*m.b31*m.b33*m.b38*m.b40 + 192*m.b31*
                       m.b34*m.b35*m.b38 + 128*m.b31*m.b34*m.b36*m.b39 + 64*m.b31*m.b34*m.b37*m.b40 + 64*m.b31*m.b35*
                       m.b36*m.b40 + 384*m.b32*m.b33*m.b34*m.b35 + 320*m.b32*m.b33*m.b35*m.b36 + 256*m.b32*m.b33*m.b36*
                       m.b37 + 192*m.b32*m.b33*m.b37*m.b38 + 128*m.b32*m.b33*m.b38*m.b39 + 64*m.b32*m.b33*m.b39*m.b40 + 
                       256*m.b32*m.b34*m.b35*m.b37 + 192*m.b32*m.b34*m.b36*m.b38 + 128*m.b32*m.b34*m.b37*m.b39 + 64*
                       m.b32*m.b34*m.b38*m.b40 + 128*m.b32*m.b35*m.b36*m.b39 + 64*m.b32*m.b35*m.b37*m.b40 + 320*m.b33*
                       m.b34*m.b35*m.b36 + 256*m.b33*m.b34*m.b36*m.b37 + 192*m.b33*m.b34*m.b37*m.b38 + 128*m.b33*m.b34*
                       m.b38*m.b39 + 64*m.b33*m.b34*m.b39*m.b40 + 192*m.b33*m.b35*m.b36*m.b38 + 128*m.b33*m.b35*m.b37*
                       m.b39 + 64*m.b33*m.b35*m.b38*m.b40 + 64*m.b33*m.b36*m.b37*m.b40 + 256*m.b34*m.b35*m.b36*m.b37 + 
                       192*m.b34*m.b35*m.b37*m.b38 + 128*m.b34*m.b35*m.b38*m.b39 + 64*m.b34*m.b35*m.b39*m.b40 + 128*
                       m.b34*m.b36*m.b37*m.b39 + 64*m.b34*m.b36*m.b38*m.b40 + 192*m.b35*m.b36*m.b37*m.b38 + 128*m.b35*
                       m.b36*m.b38*m.b39 + 64*m.b35*m.b36*m.b39*m.b40 + 64*m.b35*m.b37*m.b38*m.b40 + 128*m.b36*m.b37*
                       m.b38*m.b39 + 64*m.b36*m.b37*m.b39*m.b40 + 64*m.b37*m.b38*m.b39*m.b40 - 32*m.b1*m.b2*m.b3 - 64*
                       m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 
                       64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1*m.b2*
                       m.b13 - 64*m.b1*m.b2*m.b14 - 64*m.b1*m.b2*m.b15 - 64*m.b1*m.b2*m.b16 - 64*m.b1*m.b2*m.b17 - 64*
                       m.b1*m.b2*m.b18 - 64*m.b1*m.b2*m.b19 - 32*m.b1*m.b2*m.b20 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5
                        - 64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*
                       m.b10 - 64*m.b1*m.b3*m.b11 - 64*m.b1*m.b3*m.b12 - 64*m.b1*m.b3*m.b13 - 64*m.b1*m.b3*m.b14 - 64*
                       m.b1*m.b3*m.b15 - 64*m.b1*m.b3*m.b16 - 64*m.b1*m.b3*m.b17 - 64*m.b1*m.b3*m.b18 - 32*m.b1*m.b3*
                       m.b19 - 32*m.b1*m.b3*m.b20 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b7 - 64*m.b1*
                       m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64*m.b1*m.b4*m.b12 - 64
                       *m.b1*m.b4*m.b13 - 64*m.b1*m.b4*m.b14 - 64*m.b1*m.b4*m.b15 - 64*m.b1*m.b4*m.b16 - 64*m.b1*m.b4*
                       m.b17 - 32*m.b1*m.b4*m.b18 - 32*m.b1*m.b4*m.b19 - 32*m.b1*m.b4*m.b20 - 64*m.b1*m.b5*m.b6 - 64*
                       m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 64*m.b1*m.b5*m.b11
                        - 64*m.b1*m.b5*m.b12 - 64*m.b1*m.b5*m.b13 - 64*m.b1*m.b5*m.b14 - 64*m.b1*m.b5*m.b15 - 64*m.b1*
                       m.b5*m.b16 - 32*m.b1*m.b5*m.b17 - 32*m.b1*m.b5*m.b18 - 32*m.b1*m.b5*m.b19 - 32*m.b1*m.b5*m.b20 - 
                       64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10 - 32*m.b1*m.b6*
                       m.b11 - 64*m.b1*m.b6*m.b12 - 64*m.b1*m.b6*m.b13 - 64*m.b1*m.b6*m.b14 - 64*m.b1*m.b6*m.b15 - 32*
                       m.b1*m.b6*m.b16 - 32*m.b1*m.b6*m.b17 - 32*m.b1*m.b6*m.b18 - 32*m.b1*m.b6*m.b19 - 32*m.b1*m.b6*
                       m.b20 - 64*m.b1*m.b7*m.b8 - 64*m.b1*m.b7*m.b9 - 64*m.b1*m.b7*m.b10 - 64*m.b1*m.b7*m.b11 - 64*m.b1
                       *m.b7*m.b12 - 32*m.b1*m.b7*m.b13 - 64*m.b1*m.b7*m.b14 - 32*m.b1*m.b7*m.b15 - 32*m.b1*m.b7*m.b16
                        - 32*m.b1*m.b7*m.b17 - 32*m.b1*m.b7*m.b18 - 32*m.b1*m.b7*m.b19 - 32*m.b1*m.b7*m.b20 - 64*m.b1*
                       m.b8*m.b9 - 64*m.b1*m.b8*m.b10 - 64*m.b1*m.b8*m.b11 - 64*m.b1*m.b8*m.b12 - 64*m.b1*m.b8*m.b13 - 
                       32*m.b1*m.b8*m.b14 - 32*m.b1*m.b8*m.b16 - 32*m.b1*m.b8*m.b17 - 32*m.b1*m.b8*m.b18 - 32*m.b1*m.b8*
                       m.b19 - 32*m.b1*m.b8*m.b20 - 64*m.b1*m.b9*m.b10 - 64*m.b1*m.b9*m.b11 - 64*m.b1*m.b9*m.b12 - 32*
                       m.b1*m.b9*m.b13 - 32*m.b1*m.b9*m.b14 - 32*m.b1*m.b9*m.b15 - 32*m.b1*m.b9*m.b16 - 32*m.b1*m.b9*
                       m.b18 - 32*m.b1*m.b9*m.b19 - 32*m.b1*m.b9*m.b20 - 64*m.b1*m.b10*m.b11 - 32*m.b1*m.b10*m.b12 - 32*
                       m.b1*m.b10*m.b13 - 32*m.b1*m.b10*m.b14 - 32*m.b1*m.b10*m.b15 - 32*m.b1*m.b10*m.b16 - 32*m.b1*
                       m.b10*m.b17 - 32*m.b1*m.b10*m.b18 - 32*m.b1*m.b10*m.b20 - 32*m.b1*m.b11*m.b12 - 32*m.b1*m.b11*
                       m.b13 - 32*m.b1*m.b11*m.b14 - 32*m.b1*m.b11*m.b15 - 32*m.b1*m.b11*m.b16 - 32*m.b1*m.b11*m.b17 - 
                       32*m.b1*m.b11*m.b18 - 32*m.b1*m.b11*m.b19 - 32*m.b1*m.b11*m.b20 - 32*m.b1*m.b12*m.b13 - 32*m.b1*
                       m.b12*m.b14 - 32*m.b1*m.b12*m.b15 - 32*m.b1*m.b12*m.b16 - 32*m.b1*m.b12*m.b17 - 32*m.b1*m.b12*
                       m.b18 - 32*m.b1*m.b12*m.b19 - 32*m.b1*m.b12*m.b20 - 32*m.b1*m.b13*m.b14 - 32*m.b1*m.b13*m.b15 - 
                       32*m.b1*m.b13*m.b16 - 32*m.b1*m.b13*m.b17 - 32*m.b1*m.b13*m.b18 - 32*m.b1*m.b13*m.b19 - 32*m.b1*
                       m.b13*m.b20 - 32*m.b1*m.b14*m.b15 - 32*m.b1*m.b14*m.b16 - 32*m.b1*m.b14*m.b17 - 32*m.b1*m.b14*
                       m.b18 - 32*m.b1*m.b14*m.b19 - 32*m.b1*m.b14*m.b20 - 32*m.b1*m.b15*m.b16 - 32*m.b1*m.b15*m.b17 - 
                       32*m.b1*m.b15*m.b18 - 32*m.b1*m.b15*m.b19 - 32*m.b1*m.b15*m.b20 - 32*m.b1*m.b16*m.b17 - 32*m.b1*
                       m.b16*m.b18 - 32*m.b1*m.b16*m.b19 - 32*m.b1*m.b16*m.b20 - 32*m.b1*m.b17*m.b18 - 32*m.b1*m.b17*
                       m.b19 - 32*m.b1*m.b17*m.b20 - 32*m.b1*m.b18*m.b19 - 32*m.b1*m.b18*m.b20 - 32*m.b1*m.b19*m.b20 - 
                       96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*m.b2*m.b3*
                       m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*m.b11 - 128*m.b2*m.b3*m.b12 - 128
                       *m.b2*m.b3*m.b13 - 128*m.b2*m.b3*m.b14 - 128*m.b2*m.b3*m.b15 - 128*m.b2*m.b3*m.b16 - 128*m.b2*
                       m.b3*m.b17 - 128*m.b2*m.b3*m.b18 - 128*m.b2*m.b3*m.b19 - 96*m.b2*m.b3*m.b20 - 32*m.b2*m.b3*m.b21
                        - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 128*m.b2*
                       m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*m.b4*m.b11 - 128*m.b2*m.b4*m.b12 - 128*m.b2*m.b4*m.b13
                        - 128*m.b2*m.b4*m.b14 - 128*m.b2*m.b4*m.b15 - 128*m.b2*m.b4*m.b16 - 128*m.b2*m.b4*m.b17 - 128*
                       m.b2*m.b4*m.b18 - 96*m.b2*m.b4*m.b19 - 64*m.b2*m.b4*m.b20 - 32*m.b2*m.b4*m.b21 - 160*m.b2*m.b5*
                       m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*m.b10 - 128*
                       m.b2*m.b5*m.b11 - 128*m.b2*m.b5*m.b12 - 128*m.b2*m.b5*m.b13 - 128*m.b2*m.b5*m.b14 - 128*m.b2*m.b5
                       *m.b15 - 128*m.b2*m.b5*m.b16 - 128*m.b2*m.b5*m.b17 - 96*m.b2*m.b5*m.b18 - 64*m.b2*m.b5*m.b19 - 64
                       *m.b2*m.b5*m.b20 - 32*m.b2*m.b5*m.b21 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*m.b8 - 128*m.b2*m.b6*
                       m.b9 - 64*m.b2*m.b6*m.b10 - 128*m.b2*m.b6*m.b11 - 128*m.b2*m.b6*m.b12 - 128*m.b2*m.b6*m.b13 - 128
                       *m.b2*m.b6*m.b14 - 128*m.b2*m.b6*m.b15 - 128*m.b2*m.b6*m.b16 - 96*m.b2*m.b6*m.b17 - 64*m.b2*m.b6*
                       m.b18 - 64*m.b2*m.b6*m.b19 - 64*m.b2*m.b6*m.b20 - 32*m.b2*m.b6*m.b21 - 160*m.b2*m.b7*m.b8 - 128*
                       m.b2*m.b7*m.b9 - 128*m.b2*m.b7*m.b10 - 128*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b12 - 128*m.b2*m.b7*
                       m.b13 - 128*m.b2*m.b7*m.b14 - 128*m.b2*m.b7*m.b15 - 96*m.b2*m.b7*m.b16 - 64*m.b2*m.b7*m.b17 - 64*
                       m.b2*m.b7*m.b18 - 64*m.b2*m.b7*m.b19 - 64*m.b2*m.b7*m.b20 - 32*m.b2*m.b7*m.b21 - 160*m.b2*m.b8*
                       m.b9 - 128*m.b2*m.b8*m.b10 - 128*m.b2*m.b8*m.b11 - 128*m.b2*m.b8*m.b12 - 128*m.b2*m.b8*m.b13 - 64
                       *m.b2*m.b8*m.b14 - 96*m.b2*m.b8*m.b15 - 64*m.b2*m.b8*m.b16 - 64*m.b2*m.b8*m.b17 - 64*m.b2*m.b8*
                       m.b18 - 64*m.b2*m.b8*m.b19 - 64*m.b2*m.b8*m.b20 - 32*m.b2*m.b8*m.b21 - 160*m.b2*m.b9*m.b10 - 128*
                       m.b2*m.b9*m.b11 - 128*m.b2*m.b9*m.b12 - 128*m.b2*m.b9*m.b13 - 96*m.b2*m.b9*m.b14 - 64*m.b2*m.b9*
                       m.b15 - 64*m.b2*m.b9*m.b17 - 64*m.b2*m.b9*m.b18 - 64*m.b2*m.b9*m.b19 - 64*m.b2*m.b9*m.b20 - 32*
                       m.b2*m.b9*m.b21 - 160*m.b2*m.b10*m.b11 - 128*m.b2*m.b10*m.b12 - 96*m.b2*m.b10*m.b13 - 64*m.b2*
                       m.b10*m.b14 - 64*m.b2*m.b10*m.b15 - 64*m.b2*m.b10*m.b16 - 64*m.b2*m.b10*m.b17 - 64*m.b2*m.b10*
                       m.b19 - 64*m.b2*m.b10*m.b20 - 32*m.b2*m.b10*m.b21 - 128*m.b2*m.b11*m.b12 - 64*m.b2*m.b11*m.b13 - 
                       64*m.b2*m.b11*m.b14 - 64*m.b2*m.b11*m.b15 - 64*m.b2*m.b11*m.b16 - 64*m.b2*m.b11*m.b17 - 64*m.b2*
                       m.b11*m.b18 - 64*m.b2*m.b11*m.b19 - 32*m.b2*m.b11*m.b21 - 96*m.b2*m.b12*m.b13 - 64*m.b2*m.b12*
                       m.b14 - 64*m.b2*m.b12*m.b15 - 64*m.b2*m.b12*m.b16 - 64*m.b2*m.b12*m.b17 - 64*m.b2*m.b12*m.b18 - 
                       64*m.b2*m.b12*m.b19 - 64*m.b2*m.b12*m.b20 - 32*m.b2*m.b12*m.b21 - 96*m.b2*m.b13*m.b14 - 64*m.b2*
                       m.b13*m.b15 - 64*m.b2*m.b13*m.b16 - 64*m.b2*m.b13*m.b17 - 64*m.b2*m.b13*m.b18 - 64*m.b2*m.b13*
                       m.b19 - 64*m.b2*m.b13*m.b20 - 32*m.b2*m.b13*m.b21 - 96*m.b2*m.b14*m.b15 - 64*m.b2*m.b14*m.b16 - 
                       64*m.b2*m.b14*m.b17 - 64*m.b2*m.b14*m.b18 - 64*m.b2*m.b14*m.b19 - 64*m.b2*m.b14*m.b20 - 32*m.b2*
                       m.b14*m.b21 - 96*m.b2*m.b15*m.b16 - 64*m.b2*m.b15*m.b17 - 64*m.b2*m.b15*m.b18 - 64*m.b2*m.b15*
                       m.b19 - 64*m.b2*m.b15*m.b20 - 32*m.b2*m.b15*m.b21 - 96*m.b2*m.b16*m.b17 - 64*m.b2*m.b16*m.b18 - 
                       64*m.b2*m.b16*m.b19 - 64*m.b2*m.b16*m.b20 - 32*m.b2*m.b16*m.b21 - 96*m.b2*m.b17*m.b18 - 64*m.b2*
                       m.b17*m.b19 - 64*m.b2*m.b17*m.b20 - 32*m.b2*m.b17*m.b21 - 96*m.b2*m.b18*m.b19 - 64*m.b2*m.b18*
                       m.b20 - 32*m.b2*m.b18*m.b21 - 96*m.b2*m.b19*m.b20 - 32*m.b2*m.b19*m.b21 - 32*m.b2*m.b20*m.b21 - 
                       160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4
                       *m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*m.b12 - 192*m.b3*m.b4*m.b13 - 
                       192*m.b3*m.b4*m.b14 - 192*m.b3*m.b4*m.b15 - 192*m.b3*m.b4*m.b16 - 192*m.b3*m.b4*m.b17 - 192*m.b3*
                       m.b4*m.b18 - 192*m.b3*m.b4*m.b19 - 160*m.b3*m.b4*m.b20 - 96*m.b3*m.b4*m.b21 - 32*m.b3*m.b4*m.b22
                        - 256*m.b3*m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*
                       m.b5*m.b10 - 192*m.b3*m.b5*m.b11 - 192*m.b3*m.b5*m.b12 - 192*m.b3*m.b5*m.b13 - 192*m.b3*m.b5*
                       m.b14 - 192*m.b3*m.b5*m.b15 - 192*m.b3*m.b5*m.b16 - 192*m.b3*m.b5*m.b17 - 192*m.b3*m.b5*m.b18 - 
                       160*m.b3*m.b5*m.b19 - 128*m.b3*m.b5*m.b20 - 64*m.b3*m.b5*m.b21 - 32*m.b3*m.b5*m.b22 - 256*m.b3*
                       m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*m.b9 - 192*m.b3*m.b6*m.b10 - 192*m.b3*m.b6*m.b11 - 
                       192*m.b3*m.b6*m.b12 - 192*m.b3*m.b6*m.b13 - 192*m.b3*m.b6*m.b14 - 192*m.b3*m.b6*m.b15 - 192*m.b3*
                       m.b6*m.b16 - 192*m.b3*m.b6*m.b17 - 160*m.b3*m.b6*m.b18 - 128*m.b3*m.b6*m.b19 - 96*m.b3*m.b6*m.b20
                        - 64*m.b3*m.b6*m.b21 - 32*m.b3*m.b6*m.b22 - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 192*m.b3*
                       m.b7*m.b10 - 96*m.b3*m.b7*m.b11 - 192*m.b3*m.b7*m.b12 - 192*m.b3*m.b7*m.b13 - 192*m.b3*m.b7*m.b14
                        - 192*m.b3*m.b7*m.b15 - 192*m.b3*m.b7*m.b16 - 160*m.b3*m.b7*m.b17 - 128*m.b3*m.b7*m.b18 - 96*
                       m.b3*m.b7*m.b19 - 96*m.b3*m.b7*m.b20 - 64*m.b3*m.b7*m.b21 - 32*m.b3*m.b7*m.b22 - 256*m.b3*m.b8*
                       m.b9 - 224*m.b3*m.b8*m.b10 - 192*m.b3*m.b8*m.b11 - 192*m.b3*m.b8*m.b12 - 96*m.b3*m.b8*m.b13 - 192
                       *m.b3*m.b8*m.b14 - 192*m.b3*m.b8*m.b15 - 160*m.b3*m.b8*m.b16 - 128*m.b3*m.b8*m.b17 - 96*m.b3*m.b8
                       *m.b18 - 96*m.b3*m.b8*m.b19 - 96*m.b3*m.b8*m.b20 - 64*m.b3*m.b8*m.b21 - 32*m.b3*m.b8*m.b22 - 256*
                       m.b3*m.b9*m.b10 - 224*m.b3*m.b9*m.b11 - 192*m.b3*m.b9*m.b12 - 192*m.b3*m.b9*m.b13 - 192*m.b3*m.b9
                       *m.b14 - 64*m.b3*m.b9*m.b15 - 128*m.b3*m.b9*m.b16 - 96*m.b3*m.b9*m.b17 - 96*m.b3*m.b9*m.b18 - 96*
                       m.b3*m.b9*m.b19 - 96*m.b3*m.b9*m.b20 - 64*m.b3*m.b9*m.b21 - 32*m.b3*m.b9*m.b22 - 256*m.b3*m.b10*
                       m.b11 - 224*m.b3*m.b10*m.b12 - 192*m.b3*m.b10*m.b13 - 160*m.b3*m.b10*m.b14 - 128*m.b3*m.b10*m.b15
                        - 96*m.b3*m.b10*m.b16 - 96*m.b3*m.b10*m.b18 - 96*m.b3*m.b10*m.b19 - 96*m.b3*m.b10*m.b20 - 64*
                       m.b3*m.b10*m.b21 - 32*m.b3*m.b10*m.b22 - 256*m.b3*m.b11*m.b12 - 192*m.b3*m.b11*m.b13 - 128*m.b3*
                       m.b11*m.b14 - 96*m.b3*m.b11*m.b15 - 96*m.b3*m.b11*m.b16 - 96*m.b3*m.b11*m.b17 - 96*m.b3*m.b11*
                       m.b18 - 96*m.b3*m.b11*m.b20 - 64*m.b3*m.b11*m.b21 - 32*m.b3*m.b11*m.b22 - 192*m.b3*m.b12*m.b13 - 
                       128*m.b3*m.b12*m.b14 - 96*m.b3*m.b12*m.b15 - 96*m.b3*m.b12*m.b16 - 96*m.b3*m.b12*m.b17 - 96*m.b3*
                       m.b12*m.b18 - 96*m.b3*m.b12*m.b19 - 96*m.b3*m.b12*m.b20 - 32*m.b3*m.b12*m.b22 - 160*m.b3*m.b13*
                       m.b14 - 128*m.b3*m.b13*m.b15 - 96*m.b3*m.b13*m.b16 - 96*m.b3*m.b13*m.b17 - 96*m.b3*m.b13*m.b18 - 
                       96*m.b3*m.b13*m.b19 - 96*m.b3*m.b13*m.b20 - 64*m.b3*m.b13*m.b21 - 32*m.b3*m.b13*m.b22 - 160*m.b3*
                       m.b14*m.b15 - 128*m.b3*m.b14*m.b16 - 96*m.b3*m.b14*m.b17 - 96*m.b3*m.b14*m.b18 - 96*m.b3*m.b14*
                       m.b19 - 96*m.b3*m.b14*m.b20 - 64*m.b3*m.b14*m.b21 - 32*m.b3*m.b14*m.b22 - 160*m.b3*m.b15*m.b16 - 
                       128*m.b3*m.b15*m.b17 - 96*m.b3*m.b15*m.b18 - 96*m.b3*m.b15*m.b19 - 96*m.b3*m.b15*m.b20 - 64*m.b3*
                       m.b15*m.b21 - 32*m.b3*m.b15*m.b22 - 160*m.b3*m.b16*m.b17 - 128*m.b3*m.b16*m.b18 - 96*m.b3*m.b16*
                       m.b19 - 96*m.b3*m.b16*m.b20 - 64*m.b3*m.b16*m.b21 - 32*m.b3*m.b16*m.b22 - 160*m.b3*m.b17*m.b18 - 
                       128*m.b3*m.b17*m.b19 - 96*m.b3*m.b17*m.b20 - 64*m.b3*m.b17*m.b21 - 32*m.b3*m.b17*m.b22 - 160*m.b3
                       *m.b18*m.b19 - 128*m.b3*m.b18*m.b20 - 64*m.b3*m.b18*m.b21 - 32*m.b3*m.b18*m.b22 - 160*m.b3*m.b19*
                       m.b20 - 64*m.b3*m.b19*m.b21 - 32*m.b3*m.b19*m.b22 - 96*m.b3*m.b20*m.b21 - 32*m.b3*m.b20*m.b22 - 
                       32*m.b3*m.b21*m.b22 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*
                       m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 256*m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 256*m.b4*m.b5*m.b13
                        - 256*m.b4*m.b5*m.b14 - 256*m.b4*m.b5*m.b15 - 256*m.b4*m.b5*m.b16 - 256*m.b4*m.b5*m.b17 - 256*
                       m.b4*m.b5*m.b18 - 256*m.b4*m.b5*m.b19 - 224*m.b4*m.b5*m.b20 - 160*m.b4*m.b5*m.b21 - 96*m.b4*m.b5*
                       m.b22 - 32*m.b4*m.b5*m.b23 - 352*m.b4*m.b6*m.b7 - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*
                       m.b4*m.b6*m.b10 - 256*m.b4*m.b6*m.b11 - 256*m.b4*m.b6*m.b12 - 256*m.b4*m.b6*m.b13 - 256*m.b4*m.b6
                       *m.b14 - 256*m.b4*m.b6*m.b15 - 256*m.b4*m.b6*m.b16 - 256*m.b4*m.b6*m.b17 - 256*m.b4*m.b6*m.b18 - 
                       224*m.b4*m.b6*m.b19 - 192*m.b4*m.b6*m.b20 - 128*m.b4*m.b6*m.b21 - 64*m.b4*m.b6*m.b22 - 32*m.b4*
                       m.b6*m.b23 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*m.b4*m.b7*m.b10 - 256*m.b4*m.b7*m.b11
                        - 256*m.b4*m.b7*m.b12 - 256*m.b4*m.b7*m.b13 - 256*m.b4*m.b7*m.b14 - 256*m.b4*m.b7*m.b15 - 256*
                       m.b4*m.b7*m.b16 - 256*m.b4*m.b7*m.b17 - 224*m.b4*m.b7*m.b18 - 192*m.b4*m.b7*m.b19 - 160*m.b4*m.b7
                       *m.b20 - 96*m.b4*m.b7*m.b21 - 64*m.b4*m.b7*m.b22 - 32*m.b4*m.b7*m.b23 - 352*m.b4*m.b8*m.b9 - 320*
                       m.b4*m.b8*m.b10 - 288*m.b4*m.b8*m.b11 - 128*m.b4*m.b8*m.b12 - 256*m.b4*m.b8*m.b13 - 256*m.b4*m.b8
                       *m.b14 - 256*m.b4*m.b8*m.b15 - 256*m.b4*m.b8*m.b16 - 224*m.b4*m.b8*m.b17 - 192*m.b4*m.b8*m.b18 - 
                       160*m.b4*m.b8*m.b19 - 128*m.b4*m.b8*m.b20 - 96*m.b4*m.b8*m.b21 - 64*m.b4*m.b8*m.b22 - 32*m.b4*
                       m.b8*m.b23 - 352*m.b4*m.b9*m.b10 - 320*m.b4*m.b9*m.b11 - 288*m.b4*m.b9*m.b12 - 256*m.b4*m.b9*
                       m.b13 - 128*m.b4*m.b9*m.b14 - 256*m.b4*m.b9*m.b15 - 224*m.b4*m.b9*m.b16 - 192*m.b4*m.b9*m.b17 - 
                       160*m.b4*m.b9*m.b18 - 128*m.b4*m.b9*m.b19 - 128*m.b4*m.b9*m.b20 - 96*m.b4*m.b9*m.b21 - 64*m.b4*
                       m.b9*m.b22 - 32*m.b4*m.b9*m.b23 - 352*m.b4*m.b10*m.b11 - 320*m.b4*m.b10*m.b12 - 288*m.b4*m.b10*
                       m.b13 - 256*m.b4*m.b10*m.b14 - 224*m.b4*m.b10*m.b15 - 64*m.b4*m.b10*m.b16 - 160*m.b4*m.b10*m.b17
                        - 128*m.b4*m.b10*m.b18 - 128*m.b4*m.b10*m.b19 - 128*m.b4*m.b10*m.b20 - 96*m.b4*m.b10*m.b21 - 64*
                       m.b4*m.b10*m.b22 - 32*m.b4*m.b10*m.b23 - 352*m.b4*m.b11*m.b12 - 320*m.b4*m.b11*m.b13 - 256*m.b4*
                       m.b11*m.b14 - 192*m.b4*m.b11*m.b15 - 160*m.b4*m.b11*m.b16 - 128*m.b4*m.b11*m.b17 - 128*m.b4*m.b11
                       *m.b19 - 128*m.b4*m.b11*m.b20 - 96*m.b4*m.b11*m.b21 - 64*m.b4*m.b11*m.b22 - 32*m.b4*m.b11*m.b23
                        - 320*m.b4*m.b12*m.b13 - 256*m.b4*m.b12*m.b14 - 192*m.b4*m.b12*m.b15 - 128*m.b4*m.b12*m.b16 - 
                       128*m.b4*m.b12*m.b17 - 128*m.b4*m.b12*m.b18 - 128*m.b4*m.b12*m.b19 - 96*m.b4*m.b12*m.b21 - 64*
                       m.b4*m.b12*m.b22 - 32*m.b4*m.b12*m.b23 - 256*m.b4*m.b13*m.b14 - 192*m.b4*m.b13*m.b15 - 160*m.b4*
                       m.b13*m.b16 - 128*m.b4*m.b13*m.b17 - 128*m.b4*m.b13*m.b18 - 128*m.b4*m.b13*m.b19 - 128*m.b4*m.b13
                       *m.b20 - 96*m.b4*m.b13*m.b21 - 32*m.b4*m.b13*m.b23 - 224*m.b4*m.b14*m.b15 - 192*m.b4*m.b14*m.b16
                        - 160*m.b4*m.b14*m.b17 - 128*m.b4*m.b14*m.b18 - 128*m.b4*m.b14*m.b19 - 128*m.b4*m.b14*m.b20 - 96
                       *m.b4*m.b14*m.b21 - 64*m.b4*m.b14*m.b22 - 32*m.b4*m.b14*m.b23 - 224*m.b4*m.b15*m.b16 - 192*m.b4*
                       m.b15*m.b17 - 160*m.b4*m.b15*m.b18 - 128*m.b4*m.b15*m.b19 - 128*m.b4*m.b15*m.b20 - 96*m.b4*m.b15*
                       m.b21 - 64*m.b4*m.b15*m.b22 - 32*m.b4*m.b15*m.b23 - 224*m.b4*m.b16*m.b17 - 192*m.b4*m.b16*m.b18
                        - 160*m.b4*m.b16*m.b19 - 128*m.b4*m.b16*m.b20 - 96*m.b4*m.b16*m.b21 - 64*m.b4*m.b16*m.b22 - 32*
                       m.b4*m.b16*m.b23 - 224*m.b4*m.b17*m.b18 - 192*m.b4*m.b17*m.b19 - 160*m.b4*m.b17*m.b20 - 96*m.b4*
                       m.b17*m.b21 - 64*m.b4*m.b17*m.b22 - 32*m.b4*m.b17*m.b23 - 224*m.b4*m.b18*m.b19 - 192*m.b4*m.b18*
                       m.b20 - 96*m.b4*m.b18*m.b21 - 64*m.b4*m.b18*m.b22 - 32*m.b4*m.b18*m.b23 - 224*m.b4*m.b19*m.b20 - 
                       128*m.b4*m.b19*m.b21 - 64*m.b4*m.b19*m.b22 - 32*m.b4*m.b19*m.b23 - 160*m.b4*m.b20*m.b21 - 64*m.b4
                       *m.b20*m.b22 - 32*m.b4*m.b20*m.b23 - 96*m.b4*m.b21*m.b22 - 32*m.b4*m.b21*m.b23 - 32*m.b4*m.b22*
                       m.b23 - 288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*
                       m.b5*m.b6*m.b11 - 320*m.b5*m.b6*m.b12 - 320*m.b5*m.b6*m.b13 - 320*m.b5*m.b6*m.b14 - 320*m.b5*m.b6
                       *m.b15 - 320*m.b5*m.b6*m.b16 - 320*m.b5*m.b6*m.b17 - 320*m.b5*m.b6*m.b18 - 320*m.b5*m.b6*m.b19 - 
                       288*m.b5*m.b6*m.b20 - 224*m.b5*m.b6*m.b21 - 160*m.b5*m.b6*m.b22 - 96*m.b5*m.b6*m.b23 - 32*m.b5*
                       m.b6*m.b24 - 448*m.b5*m.b7*m.b8 - 256*m.b5*m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*m.b5*m.b7*m.b11
                        - 320*m.b5*m.b7*m.b12 - 320*m.b5*m.b7*m.b13 - 320*m.b5*m.b7*m.b14 - 320*m.b5*m.b7*m.b15 - 320*
                       m.b5*m.b7*m.b16 - 320*m.b5*m.b7*m.b17 - 320*m.b5*m.b7*m.b18 - 288*m.b5*m.b7*m.b19 - 256*m.b5*m.b7
                       *m.b20 - 192*m.b5*m.b7*m.b21 - 128*m.b5*m.b7*m.b22 - 64*m.b5*m.b7*m.b23 - 32*m.b5*m.b7*m.b24 - 
                       448*m.b5*m.b8*m.b9 - 416*m.b5*m.b8*m.b10 - 224*m.b5*m.b8*m.b11 - 352*m.b5*m.b8*m.b12 - 320*m.b5*
                       m.b8*m.b13 - 320*m.b5*m.b8*m.b14 - 320*m.b5*m.b8*m.b15 - 320*m.b5*m.b8*m.b16 - 320*m.b5*m.b8*
                       m.b17 - 288*m.b5*m.b8*m.b18 - 256*m.b5*m.b8*m.b19 - 224*m.b5*m.b8*m.b20 - 160*m.b5*m.b8*m.b21 - 
                       96*m.b5*m.b8*m.b22 - 64*m.b5*m.b8*m.b23 - 32*m.b5*m.b8*m.b24 - 448*m.b5*m.b9*m.b10 - 416*m.b5*
                       m.b9*m.b11 - 384*m.b5*m.b9*m.b12 - 192*m.b5*m.b9*m.b13 - 320*m.b5*m.b9*m.b14 - 320*m.b5*m.b9*
                       m.b15 - 320*m.b5*m.b9*m.b16 - 288*m.b5*m.b9*m.b17 - 256*m.b5*m.b9*m.b18 - 224*m.b5*m.b9*m.b19 - 
                       192*m.b5*m.b9*m.b20 - 128*m.b5*m.b9*m.b21 - 96*m.b5*m.b9*m.b22 - 64*m.b5*m.b9*m.b23 - 32*m.b5*
                       m.b9*m.b24 - 448*m.b5*m.b10*m.b11 - 416*m.b5*m.b10*m.b12 - 384*m.b5*m.b10*m.b13 - 352*m.b5*m.b10*
                       m.b14 - 160*m.b5*m.b10*m.b15 - 288*m.b5*m.b10*m.b16 - 256*m.b5*m.b10*m.b17 - 224*m.b5*m.b10*m.b18
                        - 192*m.b5*m.b10*m.b19 - 160*m.b5*m.b10*m.b20 - 128*m.b5*m.b10*m.b21 - 96*m.b5*m.b10*m.b22 - 64*
                       m.b5*m.b10*m.b23 - 32*m.b5*m.b10*m.b24 - 448*m.b5*m.b11*m.b12 - 416*m.b5*m.b11*m.b13 - 384*m.b5*
                       m.b11*m.b14 - 320*m.b5*m.b11*m.b15 - 256*m.b5*m.b11*m.b16 - 64*m.b5*m.b11*m.b17 - 192*m.b5*m.b11*
                       m.b18 - 160*m.b5*m.b11*m.b19 - 160*m.b5*m.b11*m.b20 - 128*m.b5*m.b11*m.b21 - 96*m.b5*m.b11*m.b22
                        - 64*m.b5*m.b11*m.b23 - 32*m.b5*m.b11*m.b24 - 448*m.b5*m.b12*m.b13 - 384*m.b5*m.b12*m.b14 - 320*
                       m.b5*m.b12*m.b15 - 256*m.b5*m.b12*m.b16 - 192*m.b5*m.b12*m.b17 - 160*m.b5*m.b12*m.b18 - 160*m.b5*
                       m.b12*m.b20 - 128*m.b5*m.b12*m.b21 - 96*m.b5*m.b12*m.b22 - 64*m.b5*m.b12*m.b23 - 32*m.b5*m.b12*
                       m.b24 - 384*m.b5*m.b13*m.b14 - 320*m.b5*m.b13*m.b15 - 256*m.b5*m.b13*m.b16 - 192*m.b5*m.b13*m.b17
                        - 160*m.b5*m.b13*m.b18 - 160*m.b5*m.b13*m.b19 - 160*m.b5*m.b13*m.b20 - 96*m.b5*m.b13*m.b22 - 64*
                       m.b5*m.b13*m.b23 - 32*m.b5*m.b13*m.b24 - 320*m.b5*m.b14*m.b15 - 256*m.b5*m.b14*m.b16 - 224*m.b5*
                       m.b14*m.b17 - 192*m.b5*m.b14*m.b18 - 160*m.b5*m.b14*m.b19 - 160*m.b5*m.b14*m.b20 - 128*m.b5*m.b14
                       *m.b21 - 96*m.b5*m.b14*m.b22 - 32*m.b5*m.b14*m.b24 - 288*m.b5*m.b15*m.b16 - 256*m.b5*m.b15*m.b17
                        - 224*m.b5*m.b15*m.b18 - 192*m.b5*m.b15*m.b19 - 160*m.b5*m.b15*m.b20 - 128*m.b5*m.b15*m.b21 - 96
                       *m.b5*m.b15*m.b22 - 64*m.b5*m.b15*m.b23 - 32*m.b5*m.b15*m.b24 - 288*m.b5*m.b16*m.b17 - 256*m.b5*
                       m.b16*m.b18 - 224*m.b5*m.b16*m.b19 - 192*m.b5*m.b16*m.b20 - 128*m.b5*m.b16*m.b21 - 96*m.b5*m.b16*
                       m.b22 - 64*m.b5*m.b16*m.b23 - 32*m.b5*m.b16*m.b24 - 288*m.b5*m.b17*m.b18 - 256*m.b5*m.b17*m.b19
                        - 224*m.b5*m.b17*m.b20 - 128*m.b5*m.b17*m.b21 - 96*m.b5*m.b17*m.b22 - 64*m.b5*m.b17*m.b23 - 32*
                       m.b5*m.b17*m.b24 - 288*m.b5*m.b18*m.b19 - 256*m.b5*m.b18*m.b20 - 160*m.b5*m.b18*m.b21 - 96*m.b5*
                       m.b18*m.b22 - 64*m.b5*m.b18*m.b23 - 32*m.b5*m.b18*m.b24 - 288*m.b5*m.b19*m.b20 - 192*m.b5*m.b19*
                       m.b21 - 96*m.b5*m.b19*m.b22 - 64*m.b5*m.b19*m.b23 - 32*m.b5*m.b19*m.b24 - 224*m.b5*m.b20*m.b21 - 
                       128*m.b5*m.b20*m.b22 - 64*m.b5*m.b20*m.b23 - 32*m.b5*m.b20*m.b24 - 160*m.b5*m.b21*m.b22 - 64*m.b5
                       *m.b21*m.b23 - 32*m.b5*m.b21*m.b24 - 96*m.b5*m.b22*m.b23 - 32*m.b5*m.b22*m.b24 - 32*m.b5*m.b23*
                       m.b24 - 352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*m.b7*m.b11 - 416
                       *m.b6*m.b7*m.b12 - 384*m.b6*m.b7*m.b13 - 384*m.b6*m.b7*m.b14 - 384*m.b6*m.b7*m.b15 - 384*m.b6*
                       m.b7*m.b16 - 384*m.b6*m.b7*m.b17 - 384*m.b6*m.b7*m.b18 - 384*m.b6*m.b7*m.b19 - 352*m.b6*m.b7*
                       m.b20 - 288*m.b6*m.b7*m.b21 - 224*m.b6*m.b7*m.b22 - 160*m.b6*m.b7*m.b23 - 96*m.b6*m.b7*m.b24 - 32
                       *m.b6*m.b7*m.b25 - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10 - 480*m.b6*m.b8*m.b11 - 448*m.b6*m.b8
                       *m.b12 - 416*m.b6*m.b8*m.b13 - 384*m.b6*m.b8*m.b14 - 384*m.b6*m.b8*m.b15 - 384*m.b6*m.b8*m.b16 - 
                       384*m.b6*m.b8*m.b17 - 384*m.b6*m.b8*m.b18 - 352*m.b6*m.b8*m.b19 - 320*m.b6*m.b8*m.b20 - 256*m.b6*
                       m.b8*m.b21 - 192*m.b6*m.b8*m.b22 - 128*m.b6*m.b8*m.b23 - 64*m.b6*m.b8*m.b24 - 32*m.b6*m.b8*m.b25
                        - 544*m.b6*m.b9*m.b10 - 512*m.b6*m.b9*m.b11 - 288*m.b6*m.b9*m.b12 - 448*m.b6*m.b9*m.b13 - 416*
                       m.b6*m.b9*m.b14 - 384*m.b6*m.b9*m.b15 - 384*m.b6*m.b9*m.b16 - 384*m.b6*m.b9*m.b17 - 352*m.b6*m.b9
                       *m.b18 - 320*m.b6*m.b9*m.b19 - 288*m.b6*m.b9*m.b20 - 224*m.b6*m.b9*m.b21 - 160*m.b6*m.b9*m.b22 - 
                       96*m.b6*m.b9*m.b23 - 64*m.b6*m.b9*m.b24 - 32*m.b6*m.b9*m.b25 - 544*m.b6*m.b10*m.b11 - 512*m.b6*
                       m.b10*m.b12 - 480*m.b6*m.b10*m.b13 - 256*m.b6*m.b10*m.b14 - 416*m.b6*m.b10*m.b15 - 384*m.b6*m.b10
                       *m.b16 - 352*m.b6*m.b10*m.b17 - 320*m.b6*m.b10*m.b18 - 288*m.b6*m.b10*m.b19 - 256*m.b6*m.b10*
                       m.b20 - 192*m.b6*m.b10*m.b21 - 128*m.b6*m.b10*m.b22 - 96*m.b6*m.b10*m.b23 - 64*m.b6*m.b10*m.b24
                        - 32*m.b6*m.b10*m.b25 - 544*m.b6*m.b11*m.b12 - 512*m.b6*m.b11*m.b13 - 480*m.b6*m.b11*m.b14 - 448
                       *m.b6*m.b11*m.b15 - 192*m.b6*m.b11*m.b16 - 320*m.b6*m.b11*m.b17 - 288*m.b6*m.b11*m.b18 - 256*m.b6
                       *m.b11*m.b19 - 224*m.b6*m.b11*m.b20 - 160*m.b6*m.b11*m.b21 - 128*m.b6*m.b11*m.b22 - 96*m.b6*m.b11
                       *m.b23 - 64*m.b6*m.b11*m.b24 - 32*m.b6*m.b11*m.b25 - 544*m.b6*m.b12*m.b13 - 512*m.b6*m.b12*m.b14
                        - 448*m.b6*m.b12*m.b15 - 384*m.b6*m.b12*m.b16 - 320*m.b6*m.b12*m.b17 - 64*m.b6*m.b12*m.b18 - 224
                       *m.b6*m.b12*m.b19 - 192*m.b6*m.b12*m.b20 - 160*m.b6*m.b12*m.b21 - 128*m.b6*m.b12*m.b22 - 96*m.b6*
                       m.b12*m.b23 - 64*m.b6*m.b12*m.b24 - 32*m.b6*m.b12*m.b25 - 512*m.b6*m.b13*m.b14 - 448*m.b6*m.b13*
                       m.b15 - 384*m.b6*m.b13*m.b16 - 320*m.b6*m.b13*m.b17 - 256*m.b6*m.b13*m.b18 - 192*m.b6*m.b13*m.b19
                        - 160*m.b6*m.b13*m.b21 - 128*m.b6*m.b13*m.b22 - 96*m.b6*m.b13*m.b23 - 64*m.b6*m.b13*m.b24 - 32*
                       m.b6*m.b13*m.b25 - 448*m.b6*m.b14*m.b15 - 384*m.b6*m.b14*m.b16 - 320*m.b6*m.b14*m.b17 - 256*m.b6*
                       m.b14*m.b18 - 224*m.b6*m.b14*m.b19 - 192*m.b6*m.b14*m.b20 - 160*m.b6*m.b14*m.b21 - 96*m.b6*m.b14*
                       m.b23 - 64*m.b6*m.b14*m.b24 - 32*m.b6*m.b14*m.b25 - 384*m.b6*m.b15*m.b16 - 320*m.b6*m.b15*m.b17
                        - 288*m.b6*m.b15*m.b18 - 256*m.b6*m.b15*m.b19 - 224*m.b6*m.b15*m.b20 - 160*m.b6*m.b15*m.b21 - 
                       128*m.b6*m.b15*m.b22 - 96*m.b6*m.b15*m.b23 - 32*m.b6*m.b15*m.b25 - 352*m.b6*m.b16*m.b17 - 320*
                       m.b6*m.b16*m.b18 - 288*m.b6*m.b16*m.b19 - 256*m.b6*m.b16*m.b20 - 160*m.b6*m.b16*m.b21 - 128*m.b6*
                       m.b16*m.b22 - 96*m.b6*m.b16*m.b23 - 64*m.b6*m.b16*m.b24 - 32*m.b6*m.b16*m.b25 - 352*m.b6*m.b17*
                       m.b18 - 320*m.b6*m.b17*m.b19 - 288*m.b6*m.b17*m.b20 - 192*m.b6*m.b17*m.b21 - 128*m.b6*m.b17*m.b22
                        - 96*m.b6*m.b17*m.b23 - 64*m.b6*m.b17*m.b24 - 32*m.b6*m.b17*m.b25 - 352*m.b6*m.b18*m.b19 - 320*
                       m.b6*m.b18*m.b20 - 224*m.b6*m.b18*m.b21 - 128*m.b6*m.b18*m.b22 - 96*m.b6*m.b18*m.b23 - 64*m.b6*
                       m.b18*m.b24 - 32*m.b6*m.b18*m.b25 - 352*m.b6*m.b19*m.b20 - 256*m.b6*m.b19*m.b21 - 160*m.b6*m.b19*
                       m.b22 - 96*m.b6*m.b19*m.b23 - 64*m.b6*m.b19*m.b24 - 32*m.b6*m.b19*m.b25 - 288*m.b6*m.b20*m.b21 - 
                       192*m.b6*m.b20*m.b22 - 96*m.b6*m.b20*m.b23 - 64*m.b6*m.b20*m.b24 - 32*m.b6*m.b20*m.b25 - 224*m.b6
                       *m.b21*m.b22 - 128*m.b6*m.b21*m.b23 - 64*m.b6*m.b21*m.b24 - 32*m.b6*m.b21*m.b25 - 160*m.b6*m.b22*
                       m.b23 - 64*m.b6*m.b22*m.b24 - 32*m.b6*m.b22*m.b25 - 96*m.b6*m.b23*m.b24 - 32*m.b6*m.b23*m.b25 - 
                       32*m.b6*m.b24*m.b25 - 416*m.b7*m.b8*m.b9 - 608*m.b7*m.b8*m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*
                       m.b8*m.b12 - 512*m.b7*m.b8*m.b13 - 480*m.b7*m.b8*m.b14 - 448*m.b7*m.b8*m.b15 - 448*m.b7*m.b8*
                       m.b16 - 448*m.b7*m.b8*m.b17 - 448*m.b7*m.b8*m.b18 - 448*m.b7*m.b8*m.b19 - 416*m.b7*m.b8*m.b20 - 
                       352*m.b7*m.b8*m.b21 - 288*m.b7*m.b8*m.b22 - 224*m.b7*m.b8*m.b23 - 160*m.b7*m.b8*m.b24 - 96*m.b7*
                       m.b8*m.b25 - 32*m.b7*m.b8*m.b26 - 640*m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 576*m.b7*m.b9*m.b12
                        - 544*m.b7*m.b9*m.b13 - 512*m.b7*m.b9*m.b14 - 480*m.b7*m.b9*m.b15 - 448*m.b7*m.b9*m.b16 - 448*
                       m.b7*m.b9*m.b17 - 448*m.b7*m.b9*m.b18 - 416*m.b7*m.b9*m.b19 - 384*m.b7*m.b9*m.b20 - 320*m.b7*m.b9
                       *m.b21 - 256*m.b7*m.b9*m.b22 - 192*m.b7*m.b9*m.b23 - 128*m.b7*m.b9*m.b24 - 64*m.b7*m.b9*m.b25 - 
                       32*m.b7*m.b9*m.b26 - 640*m.b7*m.b10*m.b11 - 608*m.b7*m.b10*m.b12 - 352*m.b7*m.b10*m.b13 - 544*
                       m.b7*m.b10*m.b14 - 512*m.b7*m.b10*m.b15 - 480*m.b7*m.b10*m.b16 - 448*m.b7*m.b10*m.b17 - 416*m.b7*
                       m.b10*m.b18 - 384*m.b7*m.b10*m.b19 - 352*m.b7*m.b10*m.b20 - 288*m.b7*m.b10*m.b21 - 224*m.b7*m.b10
                       *m.b22 - 160*m.b7*m.b10*m.b23 - 96*m.b7*m.b10*m.b24 - 64*m.b7*m.b10*m.b25 - 32*m.b7*m.b10*m.b26
                        - 640*m.b7*m.b11*m.b12 - 608*m.b7*m.b11*m.b13 - 576*m.b7*m.b11*m.b14 - 320*m.b7*m.b11*m.b15 - 
                       512*m.b7*m.b11*m.b16 - 448*m.b7*m.b11*m.b17 - 384*m.b7*m.b11*m.b18 - 352*m.b7*m.b11*m.b19 - 320*
                       m.b7*m.b11*m.b20 - 256*m.b7*m.b11*m.b21 - 192*m.b7*m.b11*m.b22 - 128*m.b7*m.b11*m.b23 - 96*m.b7*
                       m.b11*m.b24 - 64*m.b7*m.b11*m.b25 - 32*m.b7*m.b11*m.b26 - 640*m.b7*m.b12*m.b13 - 608*m.b7*m.b12*
                       m.b14 - 576*m.b7*m.b12*m.b15 - 512*m.b7*m.b12*m.b16 - 224*m.b7*m.b12*m.b17 - 384*m.b7*m.b12*m.b18
                        - 320*m.b7*m.b12*m.b19 - 288*m.b7*m.b12*m.b20 - 224*m.b7*m.b12*m.b21 - 160*m.b7*m.b12*m.b22 - 
                       128*m.b7*m.b12*m.b23 - 96*m.b7*m.b12*m.b24 - 64*m.b7*m.b12*m.b25 - 32*m.b7*m.b12*m.b26 - 640*m.b7
                       *m.b13*m.b14 - 576*m.b7*m.b13*m.b15 - 512*m.b7*m.b13*m.b16 - 448*m.b7*m.b13*m.b17 - 384*m.b7*
                       m.b13*m.b18 - 96*m.b7*m.b13*m.b19 - 256*m.b7*m.b13*m.b20 - 192*m.b7*m.b13*m.b21 - 160*m.b7*m.b13*
                       m.b22 - 128*m.b7*m.b13*m.b23 - 96*m.b7*m.b13*m.b24 - 64*m.b7*m.b13*m.b25 - 32*m.b7*m.b13*m.b26 - 
                       576*m.b7*m.b14*m.b15 - 512*m.b7*m.b14*m.b16 - 448*m.b7*m.b14*m.b17 - 384*m.b7*m.b14*m.b18 - 320*
                       m.b7*m.b14*m.b19 - 256*m.b7*m.b14*m.b20 - 160*m.b7*m.b14*m.b22 - 128*m.b7*m.b14*m.b23 - 96*m.b7*
                       m.b14*m.b24 - 64*m.b7*m.b14*m.b25 - 32*m.b7*m.b14*m.b26 - 512*m.b7*m.b15*m.b16 - 448*m.b7*m.b15*
                       m.b17 - 384*m.b7*m.b15*m.b18 - 320*m.b7*m.b15*m.b19 - 288*m.b7*m.b15*m.b20 - 192*m.b7*m.b15*m.b21
                        - 160*m.b7*m.b15*m.b22 - 96*m.b7*m.b15*m.b24 - 64*m.b7*m.b15*m.b25 - 32*m.b7*m.b15*m.b26 - 448*
                       m.b7*m.b16*m.b17 - 384*m.b7*m.b16*m.b18 - 352*m.b7*m.b16*m.b19 - 320*m.b7*m.b16*m.b20 - 224*m.b7*
                       m.b16*m.b21 - 160*m.b7*m.b16*m.b22 - 128*m.b7*m.b16*m.b23 - 96*m.b7*m.b16*m.b24 - 32*m.b7*m.b16*
                       m.b26 - 416*m.b7*m.b17*m.b18 - 384*m.b7*m.b17*m.b19 - 352*m.b7*m.b17*m.b20 - 256*m.b7*m.b17*m.b21
                        - 160*m.b7*m.b17*m.b22 - 128*m.b7*m.b17*m.b23 - 96*m.b7*m.b17*m.b24 - 64*m.b7*m.b17*m.b25 - 32*
                       m.b7*m.b17*m.b26 - 416*m.b7*m.b18*m.b19 - 384*m.b7*m.b18*m.b20 - 288*m.b7*m.b18*m.b21 - 192*m.b7*
                       m.b18*m.b22 - 128*m.b7*m.b18*m.b23 - 96*m.b7*m.b18*m.b24 - 64*m.b7*m.b18*m.b25 - 32*m.b7*m.b18*
                       m.b26 - 416*m.b7*m.b19*m.b20 - 320*m.b7*m.b19*m.b21 - 224*m.b7*m.b19*m.b22 - 128*m.b7*m.b19*m.b23
                        - 96*m.b7*m.b19*m.b24 - 64*m.b7*m.b19*m.b25 - 32*m.b7*m.b19*m.b26 - 352*m.b7*m.b20*m.b21 - 256*
                       m.b7*m.b20*m.b22 - 160*m.b7*m.b20*m.b23 - 96*m.b7*m.b20*m.b24 - 64*m.b7*m.b20*m.b25 - 32*m.b7*
                       m.b20*m.b26 - 288*m.b7*m.b21*m.b22 - 192*m.b7*m.b21*m.b23 - 96*m.b7*m.b21*m.b24 - 64*m.b7*m.b21*
                       m.b25 - 32*m.b7*m.b21*m.b26 - 224*m.b7*m.b22*m.b23 - 128*m.b7*m.b22*m.b24 - 64*m.b7*m.b22*m.b25
                        - 32*m.b7*m.b22*m.b26 - 160*m.b7*m.b23*m.b24 - 64*m.b7*m.b23*m.b25 - 32*m.b7*m.b23*m.b26 - 96*
                       m.b7*m.b24*m.b25 - 32*m.b7*m.b24*m.b26 - 32*m.b7*m.b25*m.b26 - 480*m.b8*m.b9*m.b10 - 704*m.b8*
                       m.b9*m.b11 - 672*m.b8*m.b9*m.b12 - 640*m.b8*m.b9*m.b13 - 608*m.b8*m.b9*m.b14 - 576*m.b8*m.b9*
                       m.b15 - 544*m.b8*m.b9*m.b16 - 512*m.b8*m.b9*m.b17 - 512*m.b8*m.b9*m.b18 - 512*m.b8*m.b9*m.b19 - 
                       480*m.b8*m.b9*m.b20 - 416*m.b8*m.b9*m.b21 - 352*m.b8*m.b9*m.b22 - 288*m.b8*m.b9*m.b23 - 224*m.b8*
                       m.b9*m.b24 - 160*m.b8*m.b9*m.b25 - 96*m.b8*m.b9*m.b26 - 32*m.b8*m.b9*m.b27 - 736*m.b8*m.b10*m.b11
                        - 448*m.b8*m.b10*m.b12 - 672*m.b8*m.b10*m.b13 - 640*m.b8*m.b10*m.b14 - 608*m.b8*m.b10*m.b15 - 
                       576*m.b8*m.b10*m.b16 - 544*m.b8*m.b10*m.b17 - 512*m.b8*m.b10*m.b18 - 480*m.b8*m.b10*m.b19 - 448*
                       m.b8*m.b10*m.b20 - 384*m.b8*m.b10*m.b21 - 320*m.b8*m.b10*m.b22 - 256*m.b8*m.b10*m.b23 - 192*m.b8*
                       m.b10*m.b24 - 128*m.b8*m.b10*m.b25 - 64*m.b8*m.b10*m.b26 - 32*m.b8*m.b10*m.b27 - 736*m.b8*m.b11*
                       m.b12 - 704*m.b8*m.b11*m.b13 - 416*m.b8*m.b11*m.b14 - 640*m.b8*m.b11*m.b15 - 608*m.b8*m.b11*m.b16
                        - 576*m.b8*m.b11*m.b17 - 512*m.b8*m.b11*m.b18 - 448*m.b8*m.b11*m.b19 - 416*m.b8*m.b11*m.b20 - 
                       352*m.b8*m.b11*m.b21 - 288*m.b8*m.b11*m.b22 - 224*m.b8*m.b11*m.b23 - 160*m.b8*m.b11*m.b24 - 96*
                       m.b8*m.b11*m.b25 - 64*m.b8*m.b11*m.b26 - 32*m.b8*m.b11*m.b27 - 736*m.b8*m.b12*m.b13 - 704*m.b8*
                       m.b12*m.b14 - 672*m.b8*m.b12*m.b15 - 384*m.b8*m.b12*m.b16 - 576*m.b8*m.b12*m.b17 - 512*m.b8*m.b12
                       *m.b18 - 448*m.b8*m.b12*m.b19 - 384*m.b8*m.b12*m.b20 - 320*m.b8*m.b12*m.b21 - 256*m.b8*m.b12*
                       m.b22 - 192*m.b8*m.b12*m.b23 - 128*m.b8*m.b12*m.b24 - 96*m.b8*m.b12*m.b25 - 64*m.b8*m.b12*m.b26
                        - 32*m.b8*m.b12*m.b27 - 736*m.b8*m.b13*m.b14 - 704*m.b8*m.b13*m.b15 - 640*m.b8*m.b13*m.b16 - 576
                       *m.b8*m.b13*m.b17 - 256*m.b8*m.b13*m.b18 - 448*m.b8*m.b13*m.b19 - 384*m.b8*m.b13*m.b20 - 288*m.b8
                       *m.b13*m.b21 - 224*m.b8*m.b13*m.b22 - 160*m.b8*m.b13*m.b23 - 128*m.b8*m.b13*m.b24 - 96*m.b8*m.b13
                       *m.b25 - 64*m.b8*m.b13*m.b26 - 32*m.b8*m.b13*m.b27 - 704*m.b8*m.b14*m.b15 - 640*m.b8*m.b14*m.b16
                        - 576*m.b8*m.b14*m.b17 - 512*m.b8*m.b14*m.b18 - 448*m.b8*m.b14*m.b19 - 128*m.b8*m.b14*m.b20 - 
                       256*m.b8*m.b14*m.b21 - 192*m.b8*m.b14*m.b22 - 160*m.b8*m.b14*m.b23 - 128*m.b8*m.b14*m.b24 - 96*
                       m.b8*m.b14*m.b25 - 64*m.b8*m.b14*m.b26 - 32*m.b8*m.b14*m.b27 - 640*m.b8*m.b15*m.b16 - 576*m.b8*
                       m.b15*m.b17 - 512*m.b8*m.b15*m.b18 - 448*m.b8*m.b15*m.b19 - 384*m.b8*m.b15*m.b20 - 256*m.b8*m.b15
                       *m.b21 - 160*m.b8*m.b15*m.b23 - 128*m.b8*m.b15*m.b24 - 96*m.b8*m.b15*m.b25 - 64*m.b8*m.b15*m.b26
                        - 32*m.b8*m.b15*m.b27 - 576*m.b8*m.b16*m.b17 - 512*m.b8*m.b16*m.b18 - 448*m.b8*m.b16*m.b19 - 384
                       *m.b8*m.b16*m.b20 - 288*m.b8*m.b16*m.b21 - 192*m.b8*m.b16*m.b22 - 160*m.b8*m.b16*m.b23 - 96*m.b8*
                       m.b16*m.b25 - 64*m.b8*m.b16*m.b26 - 32*m.b8*m.b16*m.b27 - 512*m.b8*m.b17*m.b18 - 448*m.b8*m.b17*
                       m.b19 - 416*m.b8*m.b17*m.b20 - 320*m.b8*m.b17*m.b21 - 224*m.b8*m.b17*m.b22 - 160*m.b8*m.b17*m.b23
                        - 128*m.b8*m.b17*m.b24 - 96*m.b8*m.b17*m.b25 - 32*m.b8*m.b17*m.b27 - 480*m.b8*m.b18*m.b19 - 448*
                       m.b8*m.b18*m.b20 - 352*m.b8*m.b18*m.b21 - 256*m.b8*m.b18*m.b22 - 160*m.b8*m.b18*m.b23 - 128*m.b8*
                       m.b18*m.b24 - 96*m.b8*m.b18*m.b25 - 64*m.b8*m.b18*m.b26 - 32*m.b8*m.b18*m.b27 - 480*m.b8*m.b19*
                       m.b20 - 384*m.b8*m.b19*m.b21 - 288*m.b8*m.b19*m.b22 - 192*m.b8*m.b19*m.b23 - 128*m.b8*m.b19*m.b24
                        - 96*m.b8*m.b19*m.b25 - 64*m.b8*m.b19*m.b26 - 32*m.b8*m.b19*m.b27 - 416*m.b8*m.b20*m.b21 - 320*
                       m.b8*m.b20*m.b22 - 224*m.b8*m.b20*m.b23 - 128*m.b8*m.b20*m.b24 - 96*m.b8*m.b20*m.b25 - 64*m.b8*
                       m.b20*m.b26 - 32*m.b8*m.b20*m.b27 - 352*m.b8*m.b21*m.b22 - 256*m.b8*m.b21*m.b23 - 160*m.b8*m.b21*
                       m.b24 - 96*m.b8*m.b21*m.b25 - 64*m.b8*m.b21*m.b26 - 32*m.b8*m.b21*m.b27 - 288*m.b8*m.b22*m.b23 - 
                       192*m.b8*m.b22*m.b24 - 96*m.b8*m.b22*m.b25 - 64*m.b8*m.b22*m.b26 - 32*m.b8*m.b22*m.b27 - 224*m.b8
                       *m.b23*m.b24 - 128*m.b8*m.b23*m.b25 - 64*m.b8*m.b23*m.b26 - 32*m.b8*m.b23*m.b27 - 160*m.b8*m.b24*
                       m.b25 - 64*m.b8*m.b24*m.b26 - 32*m.b8*m.b24*m.b27 - 96*m.b8*m.b25*m.b26 - 32*m.b8*m.b25*m.b27 - 
                       32*m.b8*m.b26*m.b27 - 544*m.b9*m.b10*m.b11 - 800*m.b9*m.b10*m.b12 - 768*m.b9*m.b10*m.b13 - 736*
                       m.b9*m.b10*m.b14 - 704*m.b9*m.b10*m.b15 - 672*m.b9*m.b10*m.b16 - 640*m.b9*m.b10*m.b17 - 608*m.b9*
                       m.b10*m.b18 - 576*m.b9*m.b10*m.b19 - 544*m.b9*m.b10*m.b20 - 480*m.b9*m.b10*m.b21 - 416*m.b9*m.b10
                       *m.b22 - 352*m.b9*m.b10*m.b23 - 288*m.b9*m.b10*m.b24 - 224*m.b9*m.b10*m.b25 - 160*m.b9*m.b10*
                       m.b26 - 96*m.b9*m.b10*m.b27 - 32*m.b9*m.b10*m.b28 - 832*m.b9*m.b11*m.b12 - 512*m.b9*m.b11*m.b13
                        - 768*m.b9*m.b11*m.b14 - 736*m.b9*m.b11*m.b15 - 704*m.b9*m.b11*m.b16 - 672*m.b9*m.b11*m.b17 - 
                       640*m.b9*m.b11*m.b18 - 576*m.b9*m.b11*m.b19 - 512*m.b9*m.b11*m.b20 - 448*m.b9*m.b11*m.b21 - 384*
                       m.b9*m.b11*m.b22 - 320*m.b9*m.b11*m.b23 - 256*m.b9*m.b11*m.b24 - 192*m.b9*m.b11*m.b25 - 128*m.b9*
                       m.b11*m.b26 - 64*m.b9*m.b11*m.b27 - 32*m.b9*m.b11*m.b28 - 832*m.b9*m.b12*m.b13 - 800*m.b9*m.b12*
                       m.b14 - 480*m.b9*m.b12*m.b15 - 736*m.b9*m.b12*m.b16 - 704*m.b9*m.b12*m.b17 - 640*m.b9*m.b12*m.b18
                        - 576*m.b9*m.b12*m.b19 - 512*m.b9*m.b12*m.b20 - 416*m.b9*m.b12*m.b21 - 352*m.b9*m.b12*m.b22 - 
                       288*m.b9*m.b12*m.b23 - 224*m.b9*m.b12*m.b24 - 160*m.b9*m.b12*m.b25 - 96*m.b9*m.b12*m.b26 - 64*
                       m.b9*m.b12*m.b27 - 32*m.b9*m.b12*m.b28 - 832*m.b9*m.b13*m.b14 - 800*m.b9*m.b13*m.b15 - 768*m.b9*
                       m.b13*m.b16 - 416*m.b9*m.b13*m.b17 - 640*m.b9*m.b13*m.b18 - 576*m.b9*m.b13*m.b19 - 512*m.b9*m.b13
                       *m.b20 - 384*m.b9*m.b13*m.b21 - 320*m.b9*m.b13*m.b22 - 256*m.b9*m.b13*m.b23 - 192*m.b9*m.b13*
                       m.b24 - 128*m.b9*m.b13*m.b25 - 96*m.b9*m.b13*m.b26 - 64*m.b9*m.b13*m.b27 - 32*m.b9*m.b13*m.b28 - 
                       832*m.b9*m.b14*m.b15 - 768*m.b9*m.b14*m.b16 - 704*m.b9*m.b14*m.b17 - 640*m.b9*m.b14*m.b18 - 288*
                       m.b9*m.b14*m.b19 - 512*m.b9*m.b14*m.b20 - 384*m.b9*m.b14*m.b21 - 288*m.b9*m.b14*m.b22 - 224*m.b9*
                       m.b14*m.b23 - 160*m.b9*m.b14*m.b24 - 128*m.b9*m.b14*m.b25 - 96*m.b9*m.b14*m.b26 - 64*m.b9*m.b14*
                       m.b27 - 32*m.b9*m.b14*m.b28 - 768*m.b9*m.b15*m.b16 - 704*m.b9*m.b15*m.b17 - 640*m.b9*m.b15*m.b18
                        - 576*m.b9*m.b15*m.b19 - 512*m.b9*m.b15*m.b20 - 128*m.b9*m.b15*m.b21 - 256*m.b9*m.b15*m.b22 - 
                       192*m.b9*m.b15*m.b23 - 160*m.b9*m.b15*m.b24 - 128*m.b9*m.b15*m.b25 - 96*m.b9*m.b15*m.b26 - 64*
                       m.b9*m.b15*m.b27 - 32*m.b9*m.b15*m.b28 - 704*m.b9*m.b16*m.b17 - 640*m.b9*m.b16*m.b18 - 576*m.b9*
                       m.b16*m.b19 - 512*m.b9*m.b16*m.b20 - 384*m.b9*m.b16*m.b21 - 256*m.b9*m.b16*m.b22 - 160*m.b9*m.b16
                       *m.b24 - 128*m.b9*m.b16*m.b25 - 96*m.b9*m.b16*m.b26 - 64*m.b9*m.b16*m.b27 - 32*m.b9*m.b16*m.b28
                        - 640*m.b9*m.b17*m.b18 - 576*m.b9*m.b17*m.b19 - 512*m.b9*m.b17*m.b20 - 384*m.b9*m.b17*m.b21 - 
                       288*m.b9*m.b17*m.b22 - 192*m.b9*m.b17*m.b23 - 160*m.b9*m.b17*m.b24 - 96*m.b9*m.b17*m.b26 - 64*
                       m.b9*m.b17*m.b27 - 32*m.b9*m.b17*m.b28 - 576*m.b9*m.b18*m.b19 - 512*m.b9*m.b18*m.b20 - 416*m.b9*
                       m.b18*m.b21 - 320*m.b9*m.b18*m.b22 - 224*m.b9*m.b18*m.b23 - 160*m.b9*m.b18*m.b24 - 128*m.b9*m.b18
                       *m.b25 - 96*m.b9*m.b18*m.b26 - 32*m.b9*m.b18*m.b28 - 544*m.b9*m.b19*m.b20 - 448*m.b9*m.b19*m.b21
                        - 352*m.b9*m.b19*m.b22 - 256*m.b9*m.b19*m.b23 - 160*m.b9*m.b19*m.b24 - 128*m.b9*m.b19*m.b25 - 96
                       *m.b9*m.b19*m.b26 - 64*m.b9*m.b19*m.b27 - 32*m.b9*m.b19*m.b28 - 480*m.b9*m.b20*m.b21 - 384*m.b9*
                       m.b20*m.b22 - 288*m.b9*m.b20*m.b23 - 192*m.b9*m.b20*m.b24 - 128*m.b9*m.b20*m.b25 - 96*m.b9*m.b20*
                       m.b26 - 64*m.b9*m.b20*m.b27 - 32*m.b9*m.b20*m.b28 - 416*m.b9*m.b21*m.b22 - 320*m.b9*m.b21*m.b23
                        - 224*m.b9*m.b21*m.b24 - 128*m.b9*m.b21*m.b25 - 96*m.b9*m.b21*m.b26 - 64*m.b9*m.b21*m.b27 - 32*
                       m.b9*m.b21*m.b28 - 352*m.b9*m.b22*m.b23 - 256*m.b9*m.b22*m.b24 - 160*m.b9*m.b22*m.b25 - 96*m.b9*
                       m.b22*m.b26 - 64*m.b9*m.b22*m.b27 - 32*m.b9*m.b22*m.b28 - 288*m.b9*m.b23*m.b24 - 192*m.b9*m.b23*
                       m.b25 - 96*m.b9*m.b23*m.b26 - 64*m.b9*m.b23*m.b27 - 32*m.b9*m.b23*m.b28 - 224*m.b9*m.b24*m.b25 - 
                       128*m.b9*m.b24*m.b26 - 64*m.b9*m.b24*m.b27 - 32*m.b9*m.b24*m.b28 - 160*m.b9*m.b25*m.b26 - 64*m.b9
                       *m.b25*m.b27 - 32*m.b9*m.b25*m.b28 - 96*m.b9*m.b26*m.b27 - 32*m.b9*m.b26*m.b28 - 32*m.b9*m.b27*
                       m.b28 - 608*m.b10*m.b11*m.b12 - 896*m.b10*m.b11*m.b13 - 864*m.b10*m.b11*m.b14 - 832*m.b10*m.b11*
                       m.b15 - 800*m.b10*m.b11*m.b16 - 768*m.b10*m.b11*m.b17 - 736*m.b10*m.b11*m.b18 - 704*m.b10*m.b11*
                       m.b19 - 640*m.b10*m.b11*m.b20 - 544*m.b10*m.b11*m.b21 - 480*m.b10*m.b11*m.b22 - 416*m.b10*m.b11*
                       m.b23 - 352*m.b10*m.b11*m.b24 - 288*m.b10*m.b11*m.b25 - 224*m.b10*m.b11*m.b26 - 160*m.b10*m.b11*
                       m.b27 - 96*m.b10*m.b11*m.b28 - 32*m.b10*m.b11*m.b29 - 928*m.b10*m.b12*m.b13 - 576*m.b10*m.b12*
                       m.b14 - 864*m.b10*m.b12*m.b15 - 832*m.b10*m.b12*m.b16 - 800*m.b10*m.b12*m.b17 - 768*m.b10*m.b12*
                       m.b18 - 704*m.b10*m.b12*m.b19 - 640*m.b10*m.b12*m.b20 - 512*m.b10*m.b12*m.b21 - 448*m.b10*m.b12*
                       m.b22 - 384*m.b10*m.b12*m.b23 - 320*m.b10*m.b12*m.b24 - 256*m.b10*m.b12*m.b25 - 192*m.b10*m.b12*
                       m.b26 - 128*m.b10*m.b12*m.b27 - 64*m.b10*m.b12*m.b28 - 32*m.b10*m.b12*m.b29 - 928*m.b10*m.b13*
                       m.b14 - 896*m.b10*m.b13*m.b15 - 544*m.b10*m.b13*m.b16 - 832*m.b10*m.b13*m.b17 - 768*m.b10*m.b13*
                       m.b18 - 704*m.b10*m.b13*m.b19 - 640*m.b10*m.b13*m.b20 - 512*m.b10*m.b13*m.b21 - 416*m.b10*m.b13*
                       m.b22 - 352*m.b10*m.b13*m.b23 - 288*m.b10*m.b13*m.b24 - 224*m.b10*m.b13*m.b25 - 160*m.b10*m.b13*
                       m.b26 - 96*m.b10*m.b13*m.b27 - 64*m.b10*m.b13*m.b28 - 32*m.b10*m.b13*m.b29 - 928*m.b10*m.b14*
                       m.b15 - 896*m.b10*m.b14*m.b16 - 832*m.b10*m.b14*m.b17 - 448*m.b10*m.b14*m.b18 - 704*m.b10*m.b14*
                       m.b19 - 640*m.b10*m.b14*m.b20 - 512*m.b10*m.b14*m.b21 - 384*m.b10*m.b14*m.b22 - 320*m.b10*m.b14*
                       m.b23 - 256*m.b10*m.b14*m.b24 - 192*m.b10*m.b14*m.b25 - 128*m.b10*m.b14*m.b26 - 96*m.b10*m.b14*
                       m.b27 - 64*m.b10*m.b14*m.b28 - 32*m.b10*m.b14*m.b29 - 896*m.b10*m.b15*m.b16 - 832*m.b10*m.b15*
                       m.b17 - 768*m.b10*m.b15*m.b18 - 704*m.b10*m.b15*m.b19 - 320*m.b10*m.b15*m.b20 - 512*m.b10*m.b15*
                       m.b21 - 384*m.b10*m.b15*m.b22 - 288*m.b10*m.b15*m.b23 - 224*m.b10*m.b15*m.b24 - 160*m.b10*m.b15*
                       m.b25 - 128*m.b10*m.b15*m.b26 - 96*m.b10*m.b15*m.b27 - 64*m.b10*m.b15*m.b28 - 32*m.b10*m.b15*
                       m.b29 - 832*m.b10*m.b16*m.b17 - 768*m.b10*m.b16*m.b18 - 704*m.b10*m.b16*m.b19 - 640*m.b10*m.b16*
                       m.b20 - 512*m.b10*m.b16*m.b21 - 128*m.b10*m.b16*m.b22 - 256*m.b10*m.b16*m.b23 - 192*m.b10*m.b16*
                       m.b24 - 160*m.b10*m.b16*m.b25 - 128*m.b10*m.b16*m.b26 - 96*m.b10*m.b16*m.b27 - 64*m.b10*m.b16*
                       m.b28 - 32*m.b10*m.b16*m.b29 - 768*m.b10*m.b17*m.b18 - 704*m.b10*m.b17*m.b19 - 640*m.b10*m.b17*
                       m.b20 - 512*m.b10*m.b17*m.b21 - 384*m.b10*m.b17*m.b22 - 256*m.b10*m.b17*m.b23 - 160*m.b10*m.b17*
                       m.b25 - 128*m.b10*m.b17*m.b26 - 96*m.b10*m.b17*m.b27 - 64*m.b10*m.b17*m.b28 - 32*m.b10*m.b17*
                       m.b29 - 704*m.b10*m.b18*m.b19 - 640*m.b10*m.b18*m.b20 - 512*m.b10*m.b18*m.b21 - 384*m.b10*m.b18*
                       m.b22 - 288*m.b10*m.b18*m.b23 - 192*m.b10*m.b18*m.b24 - 160*m.b10*m.b18*m.b25 - 96*m.b10*m.b18*
                       m.b27 - 64*m.b10*m.b18*m.b28 - 32*m.b10*m.b18*m.b29 - 640*m.b10*m.b19*m.b20 - 512*m.b10*m.b19*
                       m.b21 - 416*m.b10*m.b19*m.b22 - 320*m.b10*m.b19*m.b23 - 224*m.b10*m.b19*m.b24 - 160*m.b10*m.b19*
                       m.b25 - 128*m.b10*m.b19*m.b26 - 96*m.b10*m.b19*m.b27 - 32*m.b10*m.b19*m.b29 - 544*m.b10*m.b20*
                       m.b21 - 448*m.b10*m.b20*m.b22 - 352*m.b10*m.b20*m.b23 - 256*m.b10*m.b20*m.b24 - 160*m.b10*m.b20*
                       m.b25 - 128*m.b10*m.b20*m.b26 - 96*m.b10*m.b20*m.b27 - 64*m.b10*m.b20*m.b28 - 32*m.b10*m.b20*
                       m.b29 - 480*m.b10*m.b21*m.b22 - 384*m.b10*m.b21*m.b23 - 288*m.b10*m.b21*m.b24 - 192*m.b10*m.b21*
                       m.b25 - 128*m.b10*m.b21*m.b26 - 96*m.b10*m.b21*m.b27 - 64*m.b10*m.b21*m.b28 - 32*m.b10*m.b21*
                       m.b29 - 416*m.b10*m.b22*m.b23 - 320*m.b10*m.b22*m.b24 - 224*m.b10*m.b22*m.b25 - 128*m.b10*m.b22*
                       m.b26 - 96*m.b10*m.b22*m.b27 - 64*m.b10*m.b22*m.b28 - 32*m.b10*m.b22*m.b29 - 352*m.b10*m.b23*
                       m.b24 - 256*m.b10*m.b23*m.b25 - 160*m.b10*m.b23*m.b26 - 96*m.b10*m.b23*m.b27 - 64*m.b10*m.b23*
                       m.b28 - 32*m.b10*m.b23*m.b29 - 288*m.b10*m.b24*m.b25 - 192*m.b10*m.b24*m.b26 - 96*m.b10*m.b24*
                       m.b27 - 64*m.b10*m.b24*m.b28 - 32*m.b10*m.b24*m.b29 - 224*m.b10*m.b25*m.b26 - 128*m.b10*m.b25*
                       m.b27 - 64*m.b10*m.b25*m.b28 - 32*m.b10*m.b25*m.b29 - 160*m.b10*m.b26*m.b27 - 64*m.b10*m.b26*
                       m.b28 - 32*m.b10*m.b26*m.b29 - 96*m.b10*m.b27*m.b28 - 32*m.b10*m.b27*m.b29 - 32*m.b10*m.b28*m.b29
                        - 672*m.b11*m.b12*m.b13 - 992*m.b11*m.b12*m.b14 - 960*m.b11*m.b12*m.b15 - 928*m.b11*m.b12*m.b16
                        - 896*m.b11*m.b12*m.b17 - 864*m.b11*m.b12*m.b18 - 832*m.b11*m.b12*m.b19 - 768*m.b11*m.b12*m.b20
                        - 640*m.b11*m.b12*m.b21 - 544*m.b11*m.b12*m.b22 - 480*m.b11*m.b12*m.b23 - 416*m.b11*m.b12*m.b24
                        - 352*m.b11*m.b12*m.b25 - 288*m.b11*m.b12*m.b26 - 224*m.b11*m.b12*m.b27 - 160*m.b11*m.b12*m.b28
                        - 96*m.b11*m.b12*m.b29 - 32*m.b11*m.b12*m.b30 - 1024*m.b11*m.b13*m.b14 - 640*m.b11*m.b13*m.b15
                        - 960*m.b11*m.b13*m.b16 - 928*m.b11*m.b13*m.b17 - 896*m.b11*m.b13*m.b18 - 832*m.b11*m.b13*m.b19
                        - 768*m.b11*m.b13*m.b20 - 640*m.b11*m.b13*m.b21 - 512*m.b11*m.b13*m.b22 - 448*m.b11*m.b13*m.b23
                        - 384*m.b11*m.b13*m.b24 - 320*m.b11*m.b13*m.b25 - 256*m.b11*m.b13*m.b26 - 192*m.b11*m.b13*m.b27
                        - 128*m.b11*m.b13*m.b28 - 64*m.b11*m.b13*m.b29 - 32*m.b11*m.b13*m.b30 - 1024*m.b11*m.b14*m.b15
                        - 992*m.b11*m.b14*m.b16 - 608*m.b11*m.b14*m.b17 - 896*m.b11*m.b14*m.b18 - 832*m.b11*m.b14*m.b19
                        - 768*m.b11*m.b14*m.b20 - 640*m.b11*m.b14*m.b21 - 512*m.b11*m.b14*m.b22 - 416*m.b11*m.b14*m.b23
                        - 352*m.b11*m.b14*m.b24 - 288*m.b11*m.b14*m.b25 - 224*m.b11*m.b14*m.b26 - 160*m.b11*m.b14*m.b27
                        - 96*m.b11*m.b14*m.b28 - 64*m.b11*m.b14*m.b29 - 32*m.b11*m.b14*m.b30 - 1024*m.b11*m.b15*m.b16 - 
                       960*m.b11*m.b15*m.b17 - 896*m.b11*m.b15*m.b18 - 480*m.b11*m.b15*m.b19 - 768*m.b11*m.b15*m.b20 - 
                       640*m.b11*m.b15*m.b21 - 512*m.b11*m.b15*m.b22 - 384*m.b11*m.b15*m.b23 - 320*m.b11*m.b15*m.b24 - 
                       256*m.b11*m.b15*m.b25 - 192*m.b11*m.b15*m.b26 - 128*m.b11*m.b15*m.b27 - 96*m.b11*m.b15*m.b28 - 64
                       *m.b11*m.b15*m.b29 - 32*m.b11*m.b15*m.b30 - 960*m.b11*m.b16*m.b17 - 896*m.b11*m.b16*m.b18 - 832*
                       m.b11*m.b16*m.b19 - 768*m.b11*m.b16*m.b20 - 320*m.b11*m.b16*m.b21 - 512*m.b11*m.b16*m.b22 - 384*
                       m.b11*m.b16*m.b23 - 288*m.b11*m.b16*m.b24 - 224*m.b11*m.b16*m.b25 - 160*m.b11*m.b16*m.b26 - 128*
                       m.b11*m.b16*m.b27 - 96*m.b11*m.b16*m.b28 - 64*m.b11*m.b16*m.b29 - 32*m.b11*m.b16*m.b30 - 896*
                       m.b11*m.b17*m.b18 - 832*m.b11*m.b17*m.b19 - 768*m.b11*m.b17*m.b20 - 640*m.b11*m.b17*m.b21 - 512*
                       m.b11*m.b17*m.b22 - 128*m.b11*m.b17*m.b23 - 256*m.b11*m.b17*m.b24 - 192*m.b11*m.b17*m.b25 - 160*
                       m.b11*m.b17*m.b26 - 128*m.b11*m.b17*m.b27 - 96*m.b11*m.b17*m.b28 - 64*m.b11*m.b17*m.b29 - 32*
                       m.b11*m.b17*m.b30 - 832*m.b11*m.b18*m.b19 - 768*m.b11*m.b18*m.b20 - 640*m.b11*m.b18*m.b21 - 512*
                       m.b11*m.b18*m.b22 - 384*m.b11*m.b18*m.b23 - 256*m.b11*m.b18*m.b24 - 160*m.b11*m.b18*m.b26 - 128*
                       m.b11*m.b18*m.b27 - 96*m.b11*m.b18*m.b28 - 64*m.b11*m.b18*m.b29 - 32*m.b11*m.b18*m.b30 - 768*
                       m.b11*m.b19*m.b20 - 640*m.b11*m.b19*m.b21 - 512*m.b11*m.b19*m.b22 - 384*m.b11*m.b19*m.b23 - 288*
                       m.b11*m.b19*m.b24 - 192*m.b11*m.b19*m.b25 - 160*m.b11*m.b19*m.b26 - 96*m.b11*m.b19*m.b28 - 64*
                       m.b11*m.b19*m.b29 - 32*m.b11*m.b19*m.b30 - 640*m.b11*m.b20*m.b21 - 512*m.b11*m.b20*m.b22 - 416*
                       m.b11*m.b20*m.b23 - 320*m.b11*m.b20*m.b24 - 224*m.b11*m.b20*m.b25 - 160*m.b11*m.b20*m.b26 - 128*
                       m.b11*m.b20*m.b27 - 96*m.b11*m.b20*m.b28 - 32*m.b11*m.b20*m.b30 - 544*m.b11*m.b21*m.b22 - 448*
                       m.b11*m.b21*m.b23 - 352*m.b11*m.b21*m.b24 - 256*m.b11*m.b21*m.b25 - 160*m.b11*m.b21*m.b26 - 128*
                       m.b11*m.b21*m.b27 - 96*m.b11*m.b21*m.b28 - 64*m.b11*m.b21*m.b29 - 32*m.b11*m.b21*m.b30 - 480*
                       m.b11*m.b22*m.b23 - 384*m.b11*m.b22*m.b24 - 288*m.b11*m.b22*m.b25 - 192*m.b11*m.b22*m.b26 - 128*
                       m.b11*m.b22*m.b27 - 96*m.b11*m.b22*m.b28 - 64*m.b11*m.b22*m.b29 - 32*m.b11*m.b22*m.b30 - 416*
                       m.b11*m.b23*m.b24 - 320*m.b11*m.b23*m.b25 - 224*m.b11*m.b23*m.b26 - 128*m.b11*m.b23*m.b27 - 96*
                       m.b11*m.b23*m.b28 - 64*m.b11*m.b23*m.b29 - 32*m.b11*m.b23*m.b30 - 352*m.b11*m.b24*m.b25 - 256*
                       m.b11*m.b24*m.b26 - 160*m.b11*m.b24*m.b27 - 96*m.b11*m.b24*m.b28 - 64*m.b11*m.b24*m.b29 - 32*
                       m.b11*m.b24*m.b30 - 288*m.b11*m.b25*m.b26 - 192*m.b11*m.b25*m.b27 - 96*m.b11*m.b25*m.b28 - 64*
                       m.b11*m.b25*m.b29 - 32*m.b11*m.b25*m.b30 - 224*m.b11*m.b26*m.b27 - 128*m.b11*m.b26*m.b28 - 64*
                       m.b11*m.b26*m.b29 - 32*m.b11*m.b26*m.b30 - 160*m.b11*m.b27*m.b28 - 64*m.b11*m.b27*m.b29 - 32*
                       m.b11*m.b27*m.b30 - 96*m.b11*m.b28*m.b29 - 32*m.b11*m.b28*m.b30 - 32*m.b11*m.b29*m.b30 - 736*
                       m.b12*m.b13*m.b14 - 1088*m.b12*m.b13*m.b15 - 1056*m.b12*m.b13*m.b16 - 1024*m.b12*m.b13*m.b17 - 
                       992*m.b12*m.b13*m.b18 - 960*m.b12*m.b13*m.b19 - 896*m.b12*m.b13*m.b20 - 768*m.b12*m.b13*m.b21 - 
                       640*m.b12*m.b13*m.b22 - 544*m.b12*m.b13*m.b23 - 480*m.b12*m.b13*m.b24 - 416*m.b12*m.b13*m.b25 - 
                       352*m.b12*m.b13*m.b26 - 288*m.b12*m.b13*m.b27 - 224*m.b12*m.b13*m.b28 - 160*m.b12*m.b13*m.b29 - 
                       96*m.b12*m.b13*m.b30 - 32*m.b12*m.b13*m.b31 - 1120*m.b12*m.b14*m.b15 - 704*m.b12*m.b14*m.b16 - 
                       1056*m.b12*m.b14*m.b17 - 1024*m.b12*m.b14*m.b18 - 960*m.b12*m.b14*m.b19 - 896*m.b12*m.b14*m.b20
                        - 768*m.b12*m.b14*m.b21 - 640*m.b12*m.b14*m.b22 - 512*m.b12*m.b14*m.b23 - 448*m.b12*m.b14*m.b24
                        - 384*m.b12*m.b14*m.b25 - 320*m.b12*m.b14*m.b26 - 256*m.b12*m.b14*m.b27 - 192*m.b12*m.b14*m.b28
                        - 128*m.b12*m.b14*m.b29 - 64*m.b12*m.b14*m.b30 - 32*m.b12*m.b14*m.b31 - 1120*m.b12*m.b15*m.b16
                        - 1088*m.b12*m.b15*m.b17 - 640*m.b12*m.b15*m.b18 - 960*m.b12*m.b15*m.b19 - 896*m.b12*m.b15*m.b20
                        - 768*m.b12*m.b15*m.b21 - 640*m.b12*m.b15*m.b22 - 512*m.b12*m.b15*m.b23 - 416*m.b12*m.b15*m.b24
                        - 352*m.b12*m.b15*m.b25 - 288*m.b12*m.b15*m.b26 - 224*m.b12*m.b15*m.b27 - 160*m.b12*m.b15*m.b28
                        - 96*m.b12*m.b15*m.b29 - 64*m.b12*m.b15*m.b30 - 32*m.b12*m.b15*m.b31 - 1088*m.b12*m.b16*m.b17 - 
                       1024*m.b12*m.b16*m.b18 - 960*m.b12*m.b16*m.b19 - 512*m.b12*m.b16*m.b20 - 768*m.b12*m.b16*m.b21 - 
                       640*m.b12*m.b16*m.b22 - 512*m.b12*m.b16*m.b23 - 384*m.b12*m.b16*m.b24 - 320*m.b12*m.b16*m.b25 - 
                       256*m.b12*m.b16*m.b26 - 192*m.b12*m.b16*m.b27 - 128*m.b12*m.b16*m.b28 - 96*m.b12*m.b16*m.b29 - 64
                       *m.b12*m.b16*m.b30 - 32*m.b12*m.b16*m.b31 - 1024*m.b12*m.b17*m.b18 - 960*m.b12*m.b17*m.b19 - 896*
                       m.b12*m.b17*m.b20 - 768*m.b12*m.b17*m.b21 - 320*m.b12*m.b17*m.b22 - 512*m.b12*m.b17*m.b23 - 384*
                       m.b12*m.b17*m.b24 - 288*m.b12*m.b17*m.b25 - 224*m.b12*m.b17*m.b26 - 160*m.b12*m.b17*m.b27 - 128*
                       m.b12*m.b17*m.b28 - 96*m.b12*m.b17*m.b29 - 64*m.b12*m.b17*m.b30 - 32*m.b12*m.b17*m.b31 - 960*
                       m.b12*m.b18*m.b19 - 896*m.b12*m.b18*m.b20 - 768*m.b12*m.b18*m.b21 - 640*m.b12*m.b18*m.b22 - 512*
                       m.b12*m.b18*m.b23 - 128*m.b12*m.b18*m.b24 - 256*m.b12*m.b18*m.b25 - 192*m.b12*m.b18*m.b26 - 160*
                       m.b12*m.b18*m.b27 - 128*m.b12*m.b18*m.b28 - 96*m.b12*m.b18*m.b29 - 64*m.b12*m.b18*m.b30 - 32*
                       m.b12*m.b18*m.b31 - 896*m.b12*m.b19*m.b20 - 768*m.b12*m.b19*m.b21 - 640*m.b12*m.b19*m.b22 - 512*
                       m.b12*m.b19*m.b23 - 384*m.b12*m.b19*m.b24 - 256*m.b12*m.b19*m.b25 - 160*m.b12*m.b19*m.b27 - 128*
                       m.b12*m.b19*m.b28 - 96*m.b12*m.b19*m.b29 - 64*m.b12*m.b19*m.b30 - 32*m.b12*m.b19*m.b31 - 768*
                       m.b12*m.b20*m.b21 - 640*m.b12*m.b20*m.b22 - 512*m.b12*m.b20*m.b23 - 384*m.b12*m.b20*m.b24 - 288*
                       m.b12*m.b20*m.b25 - 192*m.b12*m.b20*m.b26 - 160*m.b12*m.b20*m.b27 - 96*m.b12*m.b20*m.b29 - 64*
                       m.b12*m.b20*m.b30 - 32*m.b12*m.b20*m.b31 - 640*m.b12*m.b21*m.b22 - 512*m.b12*m.b21*m.b23 - 416*
                       m.b12*m.b21*m.b24 - 320*m.b12*m.b21*m.b25 - 224*m.b12*m.b21*m.b26 - 160*m.b12*m.b21*m.b27 - 128*
                       m.b12*m.b21*m.b28 - 96*m.b12*m.b21*m.b29 - 32*m.b12*m.b21*m.b31 - 544*m.b12*m.b22*m.b23 - 448*
                       m.b12*m.b22*m.b24 - 352*m.b12*m.b22*m.b25 - 256*m.b12*m.b22*m.b26 - 160*m.b12*m.b22*m.b27 - 128*
                       m.b12*m.b22*m.b28 - 96*m.b12*m.b22*m.b29 - 64*m.b12*m.b22*m.b30 - 32*m.b12*m.b22*m.b31 - 480*
                       m.b12*m.b23*m.b24 - 384*m.b12*m.b23*m.b25 - 288*m.b12*m.b23*m.b26 - 192*m.b12*m.b23*m.b27 - 128*
                       m.b12*m.b23*m.b28 - 96*m.b12*m.b23*m.b29 - 64*m.b12*m.b23*m.b30 - 32*m.b12*m.b23*m.b31 - 416*
                       m.b12*m.b24*m.b25 - 320*m.b12*m.b24*m.b26 - 224*m.b12*m.b24*m.b27 - 128*m.b12*m.b24*m.b28 - 96*
                       m.b12*m.b24*m.b29 - 64*m.b12*m.b24*m.b30 - 32*m.b12*m.b24*m.b31 - 352*m.b12*m.b25*m.b26 - 256*
                       m.b12*m.b25*m.b27 - 160*m.b12*m.b25*m.b28 - 96*m.b12*m.b25*m.b29 - 64*m.b12*m.b25*m.b30 - 32*
                       m.b12*m.b25*m.b31 - 288*m.b12*m.b26*m.b27 - 192*m.b12*m.b26*m.b28 - 96*m.b12*m.b26*m.b29 - 64*
                       m.b12*m.b26*m.b30 - 32*m.b12*m.b26*m.b31 - 224*m.b12*m.b27*m.b28 - 128*m.b12*m.b27*m.b29 - 64*
                       m.b12*m.b27*m.b30 - 32*m.b12*m.b27*m.b31 - 160*m.b12*m.b28*m.b29 - 64*m.b12*m.b28*m.b30 - 32*
                       m.b12*m.b28*m.b31 - 96*m.b12*m.b29*m.b30 - 32*m.b12*m.b29*m.b31 - 32*m.b12*m.b30*m.b31 - 800*
                       m.b13*m.b14*m.b15 - 1184*m.b13*m.b14*m.b16 - 1152*m.b13*m.b14*m.b17 - 1120*m.b13*m.b14*m.b18 - 
                       1088*m.b13*m.b14*m.b19 - 1024*m.b13*m.b14*m.b20 - 896*m.b13*m.b14*m.b21 - 768*m.b13*m.b14*m.b22
                        - 640*m.b13*m.b14*m.b23 - 544*m.b13*m.b14*m.b24 - 480*m.b13*m.b14*m.b25 - 416*m.b13*m.b14*m.b26
                        - 352*m.b13*m.b14*m.b27 - 288*m.b13*m.b14*m.b28 - 224*m.b13*m.b14*m.b29 - 160*m.b13*m.b14*m.b30
                        - 96*m.b13*m.b14*m.b31 - 32*m.b13*m.b14*m.b32 - 1216*m.b13*m.b15*m.b16 - 768*m.b13*m.b15*m.b17
                        - 1152*m.b13*m.b15*m.b18 - 1088*m.b13*m.b15*m.b19 - 1024*m.b13*m.b15*m.b20 - 896*m.b13*m.b15*
                       m.b21 - 768*m.b13*m.b15*m.b22 - 640*m.b13*m.b15*m.b23 - 512*m.b13*m.b15*m.b24 - 448*m.b13*m.b15*
                       m.b25 - 384*m.b13*m.b15*m.b26 - 320*m.b13*m.b15*m.b27 - 256*m.b13*m.b15*m.b28 - 192*m.b13*m.b15*
                       m.b29 - 128*m.b13*m.b15*m.b30 - 64*m.b13*m.b15*m.b31 - 32*m.b13*m.b15*m.b32 - 1216*m.b13*m.b16*
                       m.b17 - 1152*m.b13*m.b16*m.b18 - 672*m.b13*m.b16*m.b19 - 1024*m.b13*m.b16*m.b20 - 896*m.b13*m.b16
                       *m.b21 - 768*m.b13*m.b16*m.b22 - 640*m.b13*m.b16*m.b23 - 512*m.b13*m.b16*m.b24 - 416*m.b13*m.b16*
                       m.b25 - 352*m.b13*m.b16*m.b26 - 288*m.b13*m.b16*m.b27 - 224*m.b13*m.b16*m.b28 - 160*m.b13*m.b16*
                       m.b29 - 96*m.b13*m.b16*m.b30 - 64*m.b13*m.b16*m.b31 - 32*m.b13*m.b16*m.b32 - 1152*m.b13*m.b17*
                       m.b18 - 1088*m.b13*m.b17*m.b19 - 1024*m.b13*m.b17*m.b20 - 512*m.b13*m.b17*m.b21 - 768*m.b13*m.b17
                       *m.b22 - 640*m.b13*m.b17*m.b23 - 512*m.b13*m.b17*m.b24 - 384*m.b13*m.b17*m.b25 - 320*m.b13*m.b17*
                       m.b26 - 256*m.b13*m.b17*m.b27 - 192*m.b13*m.b17*m.b28 - 128*m.b13*m.b17*m.b29 - 96*m.b13*m.b17*
                       m.b30 - 64*m.b13*m.b17*m.b31 - 32*m.b13*m.b17*m.b32 - 1088*m.b13*m.b18*m.b19 - 1024*m.b13*m.b18*
                       m.b20 - 896*m.b13*m.b18*m.b21 - 768*m.b13*m.b18*m.b22 - 320*m.b13*m.b18*m.b23 - 512*m.b13*m.b18*
                       m.b24 - 384*m.b13*m.b18*m.b25 - 288*m.b13*m.b18*m.b26 - 224*m.b13*m.b18*m.b27 - 160*m.b13*m.b18*
                       m.b28 - 128*m.b13*m.b18*m.b29 - 96*m.b13*m.b18*m.b30 - 64*m.b13*m.b18*m.b31 - 32*m.b13*m.b18*
                       m.b32 - 1024*m.b13*m.b19*m.b20 - 896*m.b13*m.b19*m.b21 - 768*m.b13*m.b19*m.b22 - 640*m.b13*m.b19*
                       m.b23 - 512*m.b13*m.b19*m.b24 - 128*m.b13*m.b19*m.b25 - 256*m.b13*m.b19*m.b26 - 192*m.b13*m.b19*
                       m.b27 - 160*m.b13*m.b19*m.b28 - 128*m.b13*m.b19*m.b29 - 96*m.b13*m.b19*m.b30 - 64*m.b13*m.b19*
                       m.b31 - 32*m.b13*m.b19*m.b32 - 896*m.b13*m.b20*m.b21 - 768*m.b13*m.b20*m.b22 - 640*m.b13*m.b20*
                       m.b23 - 512*m.b13*m.b20*m.b24 - 384*m.b13*m.b20*m.b25 - 256*m.b13*m.b20*m.b26 - 160*m.b13*m.b20*
                       m.b28 - 128*m.b13*m.b20*m.b29 - 96*m.b13*m.b20*m.b30 - 64*m.b13*m.b20*m.b31 - 32*m.b13*m.b20*
                       m.b32 - 768*m.b13*m.b21*m.b22 - 640*m.b13*m.b21*m.b23 - 512*m.b13*m.b21*m.b24 - 384*m.b13*m.b21*
                       m.b25 - 288*m.b13*m.b21*m.b26 - 192*m.b13*m.b21*m.b27 - 160*m.b13*m.b21*m.b28 - 96*m.b13*m.b21*
                       m.b30 - 64*m.b13*m.b21*m.b31 - 32*m.b13*m.b21*m.b32 - 640*m.b13*m.b22*m.b23 - 512*m.b13*m.b22*
                       m.b24 - 416*m.b13*m.b22*m.b25 - 320*m.b13*m.b22*m.b26 - 224*m.b13*m.b22*m.b27 - 160*m.b13*m.b22*
                       m.b28 - 128*m.b13*m.b22*m.b29 - 96*m.b13*m.b22*m.b30 - 32*m.b13*m.b22*m.b32 - 544*m.b13*m.b23*
                       m.b24 - 448*m.b13*m.b23*m.b25 - 352*m.b13*m.b23*m.b26 - 256*m.b13*m.b23*m.b27 - 160*m.b13*m.b23*
                       m.b28 - 128*m.b13*m.b23*m.b29 - 96*m.b13*m.b23*m.b30 - 64*m.b13*m.b23*m.b31 - 32*m.b13*m.b23*
                       m.b32 - 480*m.b13*m.b24*m.b25 - 384*m.b13*m.b24*m.b26 - 288*m.b13*m.b24*m.b27 - 192*m.b13*m.b24*
                       m.b28 - 128*m.b13*m.b24*m.b29 - 96*m.b13*m.b24*m.b30 - 64*m.b13*m.b24*m.b31 - 32*m.b13*m.b24*
                       m.b32 - 416*m.b13*m.b25*m.b26 - 320*m.b13*m.b25*m.b27 - 224*m.b13*m.b25*m.b28 - 128*m.b13*m.b25*
                       m.b29 - 96*m.b13*m.b25*m.b30 - 64*m.b13*m.b25*m.b31 - 32*m.b13*m.b25*m.b32 - 352*m.b13*m.b26*
                       m.b27 - 256*m.b13*m.b26*m.b28 - 160*m.b13*m.b26*m.b29 - 96*m.b13*m.b26*m.b30 - 64*m.b13*m.b26*
                       m.b31 - 32*m.b13*m.b26*m.b32 - 288*m.b13*m.b27*m.b28 - 192*m.b13*m.b27*m.b29 - 96*m.b13*m.b27*
                       m.b30 - 64*m.b13*m.b27*m.b31 - 32*m.b13*m.b27*m.b32 - 224*m.b13*m.b28*m.b29 - 128*m.b13*m.b28*
                       m.b30 - 64*m.b13*m.b28*m.b31 - 32*m.b13*m.b28*m.b32 - 160*m.b13*m.b29*m.b30 - 64*m.b13*m.b29*
                       m.b31 - 32*m.b13*m.b29*m.b32 - 96*m.b13*m.b30*m.b31 - 32*m.b13*m.b30*m.b32 - 32*m.b13*m.b31*m.b32
                        - 864*m.b14*m.b15*m.b16 - 1280*m.b14*m.b15*m.b17 - 1248*m.b14*m.b15*m.b18 - 1216*m.b14*m.b15*
                       m.b19 - 1152*m.b14*m.b15*m.b20 - 1024*m.b14*m.b15*m.b21 - 896*m.b14*m.b15*m.b22 - 768*m.b14*m.b15
                       *m.b23 - 640*m.b14*m.b15*m.b24 - 544*m.b14*m.b15*m.b25 - 480*m.b14*m.b15*m.b26 - 416*m.b14*m.b15*
                       m.b27 - 352*m.b14*m.b15*m.b28 - 288*m.b14*m.b15*m.b29 - 224*m.b14*m.b15*m.b30 - 160*m.b14*m.b15*
                       m.b31 - 96*m.b14*m.b15*m.b32 - 32*m.b14*m.b15*m.b33 - 1312*m.b14*m.b16*m.b17 - 832*m.b14*m.b16*
                       m.b18 - 1216*m.b14*m.b16*m.b19 - 1152*m.b14*m.b16*m.b20 - 1024*m.b14*m.b16*m.b21 - 896*m.b14*
                       m.b16*m.b22 - 768*m.b14*m.b16*m.b23 - 640*m.b14*m.b16*m.b24 - 512*m.b14*m.b16*m.b25 - 448*m.b14*
                       m.b16*m.b26 - 384*m.b14*m.b16*m.b27 - 320*m.b14*m.b16*m.b28 - 256*m.b14*m.b16*m.b29 - 192*m.b14*
                       m.b16*m.b30 - 128*m.b14*m.b16*m.b31 - 64*m.b14*m.b16*m.b32 - 32*m.b14*m.b16*m.b33 - 1280*m.b14*
                       m.b17*m.b18 - 1216*m.b14*m.b17*m.b19 - 704*m.b14*m.b17*m.b20 - 1024*m.b14*m.b17*m.b21 - 896*m.b14
                       *m.b17*m.b22 - 768*m.b14*m.b17*m.b23 - 640*m.b14*m.b17*m.b24 - 512*m.b14*m.b17*m.b25 - 416*m.b14*
                       m.b17*m.b26 - 352*m.b14*m.b17*m.b27 - 288*m.b14*m.b17*m.b28 - 224*m.b14*m.b17*m.b29 - 160*m.b14*
                       m.b17*m.b30 - 96*m.b14*m.b17*m.b31 - 64*m.b14*m.b17*m.b32 - 32*m.b14*m.b17*m.b33 - 1216*m.b14*
                       m.b18*m.b19 - 1152*m.b14*m.b18*m.b20 - 1024*m.b14*m.b18*m.b21 - 512*m.b14*m.b18*m.b22 - 768*m.b14
                       *m.b18*m.b23 - 640*m.b14*m.b18*m.b24 - 512*m.b14*m.b18*m.b25 - 384*m.b14*m.b18*m.b26 - 320*m.b14*
                       m.b18*m.b27 - 256*m.b14*m.b18*m.b28 - 192*m.b14*m.b18*m.b29 - 128*m.b14*m.b18*m.b30 - 96*m.b14*
                       m.b18*m.b31 - 64*m.b14*m.b18*m.b32 - 32*m.b14*m.b18*m.b33 - 1152*m.b14*m.b19*m.b20 - 1024*m.b14*
                       m.b19*m.b21 - 896*m.b14*m.b19*m.b22 - 768*m.b14*m.b19*m.b23 - 320*m.b14*m.b19*m.b24 - 512*m.b14*
                       m.b19*m.b25 - 384*m.b14*m.b19*m.b26 - 288*m.b14*m.b19*m.b27 - 224*m.b14*m.b19*m.b28 - 160*m.b14*
                       m.b19*m.b29 - 128*m.b14*m.b19*m.b30 - 96*m.b14*m.b19*m.b31 - 64*m.b14*m.b19*m.b32 - 32*m.b14*
                       m.b19*m.b33 - 1024*m.b14*m.b20*m.b21 - 896*m.b14*m.b20*m.b22 - 768*m.b14*m.b20*m.b23 - 640*m.b14*
                       m.b20*m.b24 - 512*m.b14*m.b20*m.b25 - 128*m.b14*m.b20*m.b26 - 256*m.b14*m.b20*m.b27 - 192*m.b14*
                       m.b20*m.b28 - 160*m.b14*m.b20*m.b29 - 128*m.b14*m.b20*m.b30 - 96*m.b14*m.b20*m.b31 - 64*m.b14*
                       m.b20*m.b32 - 32*m.b14*m.b20*m.b33 - 896*m.b14*m.b21*m.b22 - 768*m.b14*m.b21*m.b23 - 640*m.b14*
                       m.b21*m.b24 - 512*m.b14*m.b21*m.b25 - 384*m.b14*m.b21*m.b26 - 256*m.b14*m.b21*m.b27 - 160*m.b14*
                       m.b21*m.b29 - 128*m.b14*m.b21*m.b30 - 96*m.b14*m.b21*m.b31 - 64*m.b14*m.b21*m.b32 - 32*m.b14*
                       m.b21*m.b33 - 768*m.b14*m.b22*m.b23 - 640*m.b14*m.b22*m.b24 - 512*m.b14*m.b22*m.b25 - 384*m.b14*
                       m.b22*m.b26 - 288*m.b14*m.b22*m.b27 - 192*m.b14*m.b22*m.b28 - 160*m.b14*m.b22*m.b29 - 96*m.b14*
                       m.b22*m.b31 - 64*m.b14*m.b22*m.b32 - 32*m.b14*m.b22*m.b33 - 640*m.b14*m.b23*m.b24 - 512*m.b14*
                       m.b23*m.b25 - 416*m.b14*m.b23*m.b26 - 320*m.b14*m.b23*m.b27 - 224*m.b14*m.b23*m.b28 - 160*m.b14*
                       m.b23*m.b29 - 128*m.b14*m.b23*m.b30 - 96*m.b14*m.b23*m.b31 - 32*m.b14*m.b23*m.b33 - 544*m.b14*
                       m.b24*m.b25 - 448*m.b14*m.b24*m.b26 - 352*m.b14*m.b24*m.b27 - 256*m.b14*m.b24*m.b28 - 160*m.b14*
                       m.b24*m.b29 - 128*m.b14*m.b24*m.b30 - 96*m.b14*m.b24*m.b31 - 64*m.b14*m.b24*m.b32 - 32*m.b14*
                       m.b24*m.b33 - 480*m.b14*m.b25*m.b26 - 384*m.b14*m.b25*m.b27 - 288*m.b14*m.b25*m.b28 - 192*m.b14*
                       m.b25*m.b29 - 128*m.b14*m.b25*m.b30 - 96*m.b14*m.b25*m.b31 - 64*m.b14*m.b25*m.b32 - 32*m.b14*
                       m.b25*m.b33 - 416*m.b14*m.b26*m.b27 - 320*m.b14*m.b26*m.b28 - 224*m.b14*m.b26*m.b29 - 128*m.b14*
                       m.b26*m.b30 - 96*m.b14*m.b26*m.b31 - 64*m.b14*m.b26*m.b32 - 32*m.b14*m.b26*m.b33 - 352*m.b14*
                       m.b27*m.b28 - 256*m.b14*m.b27*m.b29 - 160*m.b14*m.b27*m.b30 - 96*m.b14*m.b27*m.b31 - 64*m.b14*
                       m.b27*m.b32 - 32*m.b14*m.b27*m.b33 - 288*m.b14*m.b28*m.b29 - 192*m.b14*m.b28*m.b30 - 96*m.b14*
                       m.b28*m.b31 - 64*m.b14*m.b28*m.b32 - 32*m.b14*m.b28*m.b33 - 224*m.b14*m.b29*m.b30 - 128*m.b14*
                       m.b29*m.b31 - 64*m.b14*m.b29*m.b32 - 32*m.b14*m.b29*m.b33 - 160*m.b14*m.b30*m.b31 - 64*m.b14*
                       m.b30*m.b32 - 32*m.b14*m.b30*m.b33 - 96*m.b14*m.b31*m.b32 - 32*m.b14*m.b31*m.b33 - 32*m.b14*m.b32
                       *m.b33 - 928*m.b15*m.b16*m.b17 - 1376*m.b15*m.b16*m.b18 - 1344*m.b15*m.b16*m.b19 - 1280*m.b15*
                       m.b16*m.b20 - 1152*m.b15*m.b16*m.b21 - 1024*m.b15*m.b16*m.b22 - 896*m.b15*m.b16*m.b23 - 768*m.b15
                       *m.b16*m.b24 - 640*m.b15*m.b16*m.b25 - 544*m.b15*m.b16*m.b26 - 480*m.b15*m.b16*m.b27 - 416*m.b15*
                       m.b16*m.b28 - 352*m.b15*m.b16*m.b29 - 288*m.b15*m.b16*m.b30 - 224*m.b15*m.b16*m.b31 - 160*m.b15*
                       m.b16*m.b32 - 96*m.b15*m.b16*m.b33 - 32*m.b15*m.b16*m.b34 - 1408*m.b15*m.b17*m.b18 - 864*m.b15*
                       m.b17*m.b19 - 1280*m.b15*m.b17*m.b20 - 1152*m.b15*m.b17*m.b21 - 1024*m.b15*m.b17*m.b22 - 896*
                       m.b15*m.b17*m.b23 - 768*m.b15*m.b17*m.b24 - 640*m.b15*m.b17*m.b25 - 512*m.b15*m.b17*m.b26 - 448*
                       m.b15*m.b17*m.b27 - 384*m.b15*m.b17*m.b28 - 320*m.b15*m.b17*m.b29 - 256*m.b15*m.b17*m.b30 - 192*
                       m.b15*m.b17*m.b31 - 128*m.b15*m.b17*m.b32 - 64*m.b15*m.b17*m.b33 - 32*m.b15*m.b17*m.b34 - 1344*
                       m.b15*m.b18*m.b19 - 1280*m.b15*m.b18*m.b20 - 704*m.b15*m.b18*m.b21 - 1024*m.b15*m.b18*m.b22 - 896
                       *m.b15*m.b18*m.b23 - 768*m.b15*m.b18*m.b24 - 640*m.b15*m.b18*m.b25 - 512*m.b15*m.b18*m.b26 - 416*
                       m.b15*m.b18*m.b27 - 352*m.b15*m.b18*m.b28 - 288*m.b15*m.b18*m.b29 - 224*m.b15*m.b18*m.b30 - 160*
                       m.b15*m.b18*m.b31 - 96*m.b15*m.b18*m.b32 - 64*m.b15*m.b18*m.b33 - 32*m.b15*m.b18*m.b34 - 1280*
                       m.b15*m.b19*m.b20 - 1152*m.b15*m.b19*m.b21 - 1024*m.b15*m.b19*m.b22 - 512*m.b15*m.b19*m.b23 - 768
                       *m.b15*m.b19*m.b24 - 640*m.b15*m.b19*m.b25 - 512*m.b15*m.b19*m.b26 - 384*m.b15*m.b19*m.b27 - 320*
                       m.b15*m.b19*m.b28 - 256*m.b15*m.b19*m.b29 - 192*m.b15*m.b19*m.b30 - 128*m.b15*m.b19*m.b31 - 96*
                       m.b15*m.b19*m.b32 - 64*m.b15*m.b19*m.b33 - 32*m.b15*m.b19*m.b34 - 1152*m.b15*m.b20*m.b21 - 1024*
                       m.b15*m.b20*m.b22 - 896*m.b15*m.b20*m.b23 - 768*m.b15*m.b20*m.b24 - 320*m.b15*m.b20*m.b25 - 512*
                       m.b15*m.b20*m.b26 - 384*m.b15*m.b20*m.b27 - 288*m.b15*m.b20*m.b28 - 224*m.b15*m.b20*m.b29 - 160*
                       m.b15*m.b20*m.b30 - 128*m.b15*m.b20*m.b31 - 96*m.b15*m.b20*m.b32 - 64*m.b15*m.b20*m.b33 - 32*
                       m.b15*m.b20*m.b34 - 1024*m.b15*m.b21*m.b22 - 896*m.b15*m.b21*m.b23 - 768*m.b15*m.b21*m.b24 - 640*
                       m.b15*m.b21*m.b25 - 512*m.b15*m.b21*m.b26 - 128*m.b15*m.b21*m.b27 - 256*m.b15*m.b21*m.b28 - 192*
                       m.b15*m.b21*m.b29 - 160*m.b15*m.b21*m.b30 - 128*m.b15*m.b21*m.b31 - 96*m.b15*m.b21*m.b32 - 64*
                       m.b15*m.b21*m.b33 - 32*m.b15*m.b21*m.b34 - 896*m.b15*m.b22*m.b23 - 768*m.b15*m.b22*m.b24 - 640*
                       m.b15*m.b22*m.b25 - 512*m.b15*m.b22*m.b26 - 384*m.b15*m.b22*m.b27 - 256*m.b15*m.b22*m.b28 - 160*
                       m.b15*m.b22*m.b30 - 128*m.b15*m.b22*m.b31 - 96*m.b15*m.b22*m.b32 - 64*m.b15*m.b22*m.b33 - 32*
                       m.b15*m.b22*m.b34 - 768*m.b15*m.b23*m.b24 - 640*m.b15*m.b23*m.b25 - 512*m.b15*m.b23*m.b26 - 384*
                       m.b15*m.b23*m.b27 - 288*m.b15*m.b23*m.b28 - 192*m.b15*m.b23*m.b29 - 160*m.b15*m.b23*m.b30 - 96*
                       m.b15*m.b23*m.b32 - 64*m.b15*m.b23*m.b33 - 32*m.b15*m.b23*m.b34 - 640*m.b15*m.b24*m.b25 - 512*
                       m.b15*m.b24*m.b26 - 416*m.b15*m.b24*m.b27 - 320*m.b15*m.b24*m.b28 - 224*m.b15*m.b24*m.b29 - 160*
                       m.b15*m.b24*m.b30 - 128*m.b15*m.b24*m.b31 - 96*m.b15*m.b24*m.b32 - 32*m.b15*m.b24*m.b34 - 544*
                       m.b15*m.b25*m.b26 - 448*m.b15*m.b25*m.b27 - 352*m.b15*m.b25*m.b28 - 256*m.b15*m.b25*m.b29 - 160*
                       m.b15*m.b25*m.b30 - 128*m.b15*m.b25*m.b31 - 96*m.b15*m.b25*m.b32 - 64*m.b15*m.b25*m.b33 - 32*
                       m.b15*m.b25*m.b34 - 480*m.b15*m.b26*m.b27 - 384*m.b15*m.b26*m.b28 - 288*m.b15*m.b26*m.b29 - 192*
                       m.b15*m.b26*m.b30 - 128*m.b15*m.b26*m.b31 - 96*m.b15*m.b26*m.b32 - 64*m.b15*m.b26*m.b33 - 32*
                       m.b15*m.b26*m.b34 - 416*m.b15*m.b27*m.b28 - 320*m.b15*m.b27*m.b29 - 224*m.b15*m.b27*m.b30 - 128*
                       m.b15*m.b27*m.b31 - 96*m.b15*m.b27*m.b32 - 64*m.b15*m.b27*m.b33 - 32*m.b15*m.b27*m.b34 - 352*
                       m.b15*m.b28*m.b29 - 256*m.b15*m.b28*m.b30 - 160*m.b15*m.b28*m.b31 - 96*m.b15*m.b28*m.b32 - 64*
                       m.b15*m.b28*m.b33 - 32*m.b15*m.b28*m.b34 - 288*m.b15*m.b29*m.b30 - 192*m.b15*m.b29*m.b31 - 96*
                       m.b15*m.b29*m.b32 - 64*m.b15*m.b29*m.b33 - 32*m.b15*m.b29*m.b34 - 224*m.b15*m.b30*m.b31 - 128*
                       m.b15*m.b30*m.b32 - 64*m.b15*m.b30*m.b33 - 32*m.b15*m.b30*m.b34 - 160*m.b15*m.b31*m.b32 - 64*
                       m.b15*m.b31*m.b33 - 32*m.b15*m.b31*m.b34 - 96*m.b15*m.b32*m.b33 - 32*m.b15*m.b32*m.b34 - 32*m.b15
                       *m.b33*m.b34 - 992*m.b16*m.b17*m.b18 - 1472*m.b16*m.b17*m.b19 - 1408*m.b16*m.b17*m.b20 - 1280*
                       m.b16*m.b17*m.b21 - 1152*m.b16*m.b17*m.b22 - 1024*m.b16*m.b17*m.b23 - 896*m.b16*m.b17*m.b24 - 768
                       *m.b16*m.b17*m.b25 - 640*m.b16*m.b17*m.b26 - 544*m.b16*m.b17*m.b27 - 480*m.b16*m.b17*m.b28 - 416*
                       m.b16*m.b17*m.b29 - 352*m.b16*m.b17*m.b30 - 288*m.b16*m.b17*m.b31 - 224*m.b16*m.b17*m.b32 - 160*
                       m.b16*m.b17*m.b33 - 96*m.b16*m.b17*m.b34 - 32*m.b16*m.b17*m.b35 - 1472*m.b16*m.b18*m.b19 - 896*
                       m.b16*m.b18*m.b20 - 1280*m.b16*m.b18*m.b21 - 1152*m.b16*m.b18*m.b22 - 1024*m.b16*m.b18*m.b23 - 
                       896*m.b16*m.b18*m.b24 - 768*m.b16*m.b18*m.b25 - 640*m.b16*m.b18*m.b26 - 512*m.b16*m.b18*m.b27 - 
                       448*m.b16*m.b18*m.b28 - 384*m.b16*m.b18*m.b29 - 320*m.b16*m.b18*m.b30 - 256*m.b16*m.b18*m.b31 - 
                       192*m.b16*m.b18*m.b32 - 128*m.b16*m.b18*m.b33 - 64*m.b16*m.b18*m.b34 - 32*m.b16*m.b18*m.b35 - 
                       1408*m.b16*m.b19*m.b20 - 1280*m.b16*m.b19*m.b21 - 704*m.b16*m.b19*m.b22 - 1024*m.b16*m.b19*m.b23
                        - 896*m.b16*m.b19*m.b24 - 768*m.b16*m.b19*m.b25 - 640*m.b16*m.b19*m.b26 - 512*m.b16*m.b19*m.b27
                        - 416*m.b16*m.b19*m.b28 - 352*m.b16*m.b19*m.b29 - 288*m.b16*m.b19*m.b30 - 224*m.b16*m.b19*m.b31
                        - 160*m.b16*m.b19*m.b32 - 96*m.b16*m.b19*m.b33 - 64*m.b16*m.b19*m.b34 - 32*m.b16*m.b19*m.b35 - 
                       1280*m.b16*m.b20*m.b21 - 1152*m.b16*m.b20*m.b22 - 1024*m.b16*m.b20*m.b23 - 512*m.b16*m.b20*m.b24
                        - 768*m.b16*m.b20*m.b25 - 640*m.b16*m.b20*m.b26 - 512*m.b16*m.b20*m.b27 - 384*m.b16*m.b20*m.b28
                        - 320*m.b16*m.b20*m.b29 - 256*m.b16*m.b20*m.b30 - 192*m.b16*m.b20*m.b31 - 128*m.b16*m.b20*m.b32
                        - 96*m.b16*m.b20*m.b33 - 64*m.b16*m.b20*m.b34 - 32*m.b16*m.b20*m.b35 - 1152*m.b16*m.b21*m.b22 - 
                       1024*m.b16*m.b21*m.b23 - 896*m.b16*m.b21*m.b24 - 768*m.b16*m.b21*m.b25 - 320*m.b16*m.b21*m.b26 - 
                       512*m.b16*m.b21*m.b27 - 384*m.b16*m.b21*m.b28 - 288*m.b16*m.b21*m.b29 - 224*m.b16*m.b21*m.b30 - 
                       160*m.b16*m.b21*m.b31 - 128*m.b16*m.b21*m.b32 - 96*m.b16*m.b21*m.b33 - 64*m.b16*m.b21*m.b34 - 32*
                       m.b16*m.b21*m.b35 - 1024*m.b16*m.b22*m.b23 - 896*m.b16*m.b22*m.b24 - 768*m.b16*m.b22*m.b25 - 640*
                       m.b16*m.b22*m.b26 - 512*m.b16*m.b22*m.b27 - 128*m.b16*m.b22*m.b28 - 256*m.b16*m.b22*m.b29 - 192*
                       m.b16*m.b22*m.b30 - 160*m.b16*m.b22*m.b31 - 128*m.b16*m.b22*m.b32 - 96*m.b16*m.b22*m.b33 - 64*
                       m.b16*m.b22*m.b34 - 32*m.b16*m.b22*m.b35 - 896*m.b16*m.b23*m.b24 - 768*m.b16*m.b23*m.b25 - 640*
                       m.b16*m.b23*m.b26 - 512*m.b16*m.b23*m.b27 - 384*m.b16*m.b23*m.b28 - 256*m.b16*m.b23*m.b29 - 160*
                       m.b16*m.b23*m.b31 - 128*m.b16*m.b23*m.b32 - 96*m.b16*m.b23*m.b33 - 64*m.b16*m.b23*m.b34 - 32*
                       m.b16*m.b23*m.b35 - 768*m.b16*m.b24*m.b25 - 640*m.b16*m.b24*m.b26 - 512*m.b16*m.b24*m.b27 - 384*
                       m.b16*m.b24*m.b28 - 288*m.b16*m.b24*m.b29 - 192*m.b16*m.b24*m.b30 - 160*m.b16*m.b24*m.b31 - 96*
                       m.b16*m.b24*m.b33 - 64*m.b16*m.b24*m.b34 - 32*m.b16*m.b24*m.b35 - 640*m.b16*m.b25*m.b26 - 512*
                       m.b16*m.b25*m.b27 - 416*m.b16*m.b25*m.b28 - 320*m.b16*m.b25*m.b29 - 224*m.b16*m.b25*m.b30 - 160*
                       m.b16*m.b25*m.b31 - 128*m.b16*m.b25*m.b32 - 96*m.b16*m.b25*m.b33 - 32*m.b16*m.b25*m.b35 - 544*
                       m.b16*m.b26*m.b27 - 448*m.b16*m.b26*m.b28 - 352*m.b16*m.b26*m.b29 - 256*m.b16*m.b26*m.b30 - 160*
                       m.b16*m.b26*m.b31 - 128*m.b16*m.b26*m.b32 - 96*m.b16*m.b26*m.b33 - 64*m.b16*m.b26*m.b34 - 32*
                       m.b16*m.b26*m.b35 - 480*m.b16*m.b27*m.b28 - 384*m.b16*m.b27*m.b29 - 288*m.b16*m.b27*m.b30 - 192*
                       m.b16*m.b27*m.b31 - 128*m.b16*m.b27*m.b32 - 96*m.b16*m.b27*m.b33 - 64*m.b16*m.b27*m.b34 - 32*
                       m.b16*m.b27*m.b35 - 416*m.b16*m.b28*m.b29 - 320*m.b16*m.b28*m.b30 - 224*m.b16*m.b28*m.b31 - 128*
                       m.b16*m.b28*m.b32 - 96*m.b16*m.b28*m.b33 - 64*m.b16*m.b28*m.b34 - 32*m.b16*m.b28*m.b35 - 352*
                       m.b16*m.b29*m.b30 - 256*m.b16*m.b29*m.b31 - 160*m.b16*m.b29*m.b32 - 96*m.b16*m.b29*m.b33 - 64*
                       m.b16*m.b29*m.b34 - 32*m.b16*m.b29*m.b35 - 288*m.b16*m.b30*m.b31 - 192*m.b16*m.b30*m.b32 - 96*
                       m.b16*m.b30*m.b33 - 64*m.b16*m.b30*m.b34 - 32*m.b16*m.b30*m.b35 - 224*m.b16*m.b31*m.b32 - 128*
                       m.b16*m.b31*m.b33 - 64*m.b16*m.b31*m.b34 - 32*m.b16*m.b31*m.b35 - 160*m.b16*m.b32*m.b33 - 64*
                       m.b16*m.b32*m.b34 - 32*m.b16*m.b32*m.b35 - 96*m.b16*m.b33*m.b34 - 32*m.b16*m.b33*m.b35 - 32*m.b16
                       *m.b34*m.b35 - 1056*m.b17*m.b18*m.b19 - 1536*m.b17*m.b18*m.b20 - 1408*m.b17*m.b18*m.b21 - 1280*
                       m.b17*m.b18*m.b22 - 1152*m.b17*m.b18*m.b23 - 1024*m.b17*m.b18*m.b24 - 896*m.b17*m.b18*m.b25 - 768
                       *m.b17*m.b18*m.b26 - 640*m.b17*m.b18*m.b27 - 544*m.b17*m.b18*m.b28 - 480*m.b17*m.b18*m.b29 - 416*
                       m.b17*m.b18*m.b30 - 352*m.b17*m.b18*m.b31 - 288*m.b17*m.b18*m.b32 - 224*m.b17*m.b18*m.b33 - 160*
                       m.b17*m.b18*m.b34 - 96*m.b17*m.b18*m.b35 - 32*m.b17*m.b18*m.b36 - 1536*m.b17*m.b19*m.b20 - 896*
                       m.b17*m.b19*m.b21 - 1280*m.b17*m.b19*m.b22 - 1152*m.b17*m.b19*m.b23 - 1024*m.b17*m.b19*m.b24 - 
                       896*m.b17*m.b19*m.b25 - 768*m.b17*m.b19*m.b26 - 640*m.b17*m.b19*m.b27 - 512*m.b17*m.b19*m.b28 - 
                       448*m.b17*m.b19*m.b29 - 384*m.b17*m.b19*m.b30 - 320*m.b17*m.b19*m.b31 - 256*m.b17*m.b19*m.b32 - 
                       192*m.b17*m.b19*m.b33 - 128*m.b17*m.b19*m.b34 - 64*m.b17*m.b19*m.b35 - 32*m.b17*m.b19*m.b36 - 
                       1408*m.b17*m.b20*m.b21 - 1280*m.b17*m.b20*m.b22 - 704*m.b17*m.b20*m.b23 - 1024*m.b17*m.b20*m.b24
                        - 896*m.b17*m.b20*m.b25 - 768*m.b17*m.b20*m.b26 - 640*m.b17*m.b20*m.b27 - 512*m.b17*m.b20*m.b28
                        - 416*m.b17*m.b20*m.b29 - 352*m.b17*m.b20*m.b30 - 288*m.b17*m.b20*m.b31 - 224*m.b17*m.b20*m.b32
                        - 160*m.b17*m.b20*m.b33 - 96*m.b17*m.b20*m.b34 - 64*m.b17*m.b20*m.b35 - 32*m.b17*m.b20*m.b36 - 
                       1280*m.b17*m.b21*m.b22 - 1152*m.b17*m.b21*m.b23 - 1024*m.b17*m.b21*m.b24 - 512*m.b17*m.b21*m.b25
                        - 768*m.b17*m.b21*m.b26 - 640*m.b17*m.b21*m.b27 - 512*m.b17*m.b21*m.b28 - 384*m.b17*m.b21*m.b29
                        - 320*m.b17*m.b21*m.b30 - 256*m.b17*m.b21*m.b31 - 192*m.b17*m.b21*m.b32 - 128*m.b17*m.b21*m.b33
                        - 96*m.b17*m.b21*m.b34 - 64*m.b17*m.b21*m.b35 - 32*m.b17*m.b21*m.b36 - 1152*m.b17*m.b22*m.b23 - 
                       1024*m.b17*m.b22*m.b24 - 896*m.b17*m.b22*m.b25 - 768*m.b17*m.b22*m.b26 - 320*m.b17*m.b22*m.b27 - 
                       512*m.b17*m.b22*m.b28 - 384*m.b17*m.b22*m.b29 - 288*m.b17*m.b22*m.b30 - 224*m.b17*m.b22*m.b31 - 
                       160*m.b17*m.b22*m.b32 - 128*m.b17*m.b22*m.b33 - 96*m.b17*m.b22*m.b34 - 64*m.b17*m.b22*m.b35 - 32*
                       m.b17*m.b22*m.b36 - 1024*m.b17*m.b23*m.b24 - 896*m.b17*m.b23*m.b25 - 768*m.b17*m.b23*m.b26 - 640*
                       m.b17*m.b23*m.b27 - 512*m.b17*m.b23*m.b28 - 128*m.b17*m.b23*m.b29 - 256*m.b17*m.b23*m.b30 - 192*
                       m.b17*m.b23*m.b31 - 160*m.b17*m.b23*m.b32 - 128*m.b17*m.b23*m.b33 - 96*m.b17*m.b23*m.b34 - 64*
                       m.b17*m.b23*m.b35 - 32*m.b17*m.b23*m.b36 - 896*m.b17*m.b24*m.b25 - 768*m.b17*m.b24*m.b26 - 640*
                       m.b17*m.b24*m.b27 - 512*m.b17*m.b24*m.b28 - 384*m.b17*m.b24*m.b29 - 256*m.b17*m.b24*m.b30 - 160*
                       m.b17*m.b24*m.b32 - 128*m.b17*m.b24*m.b33 - 96*m.b17*m.b24*m.b34 - 64*m.b17*m.b24*m.b35 - 32*
                       m.b17*m.b24*m.b36 - 768*m.b17*m.b25*m.b26 - 640*m.b17*m.b25*m.b27 - 512*m.b17*m.b25*m.b28 - 384*
                       m.b17*m.b25*m.b29 - 288*m.b17*m.b25*m.b30 - 192*m.b17*m.b25*m.b31 - 160*m.b17*m.b25*m.b32 - 96*
                       m.b17*m.b25*m.b34 - 64*m.b17*m.b25*m.b35 - 32*m.b17*m.b25*m.b36 - 640*m.b17*m.b26*m.b27 - 512*
                       m.b17*m.b26*m.b28 - 416*m.b17*m.b26*m.b29 - 320*m.b17*m.b26*m.b30 - 224*m.b17*m.b26*m.b31 - 160*
                       m.b17*m.b26*m.b32 - 128*m.b17*m.b26*m.b33 - 96*m.b17*m.b26*m.b34 - 32*m.b17*m.b26*m.b36 - 544*
                       m.b17*m.b27*m.b28 - 448*m.b17*m.b27*m.b29 - 352*m.b17*m.b27*m.b30 - 256*m.b17*m.b27*m.b31 - 160*
                       m.b17*m.b27*m.b32 - 128*m.b17*m.b27*m.b33 - 96*m.b17*m.b27*m.b34 - 64*m.b17*m.b27*m.b35 - 32*
                       m.b17*m.b27*m.b36 - 480*m.b17*m.b28*m.b29 - 384*m.b17*m.b28*m.b30 - 288*m.b17*m.b28*m.b31 - 192*
                       m.b17*m.b28*m.b32 - 128*m.b17*m.b28*m.b33 - 96*m.b17*m.b28*m.b34 - 64*m.b17*m.b28*m.b35 - 32*
                       m.b17*m.b28*m.b36 - 416*m.b17*m.b29*m.b30 - 320*m.b17*m.b29*m.b31 - 224*m.b17*m.b29*m.b32 - 128*
                       m.b17*m.b29*m.b33 - 96*m.b17*m.b29*m.b34 - 64*m.b17*m.b29*m.b35 - 32*m.b17*m.b29*m.b36 - 352*
                       m.b17*m.b30*m.b31 - 256*m.b17*m.b30*m.b32 - 160*m.b17*m.b30*m.b33 - 96*m.b17*m.b30*m.b34 - 64*
                       m.b17*m.b30*m.b35 - 32*m.b17*m.b30*m.b36 - 288*m.b17*m.b31*m.b32 - 192*m.b17*m.b31*m.b33 - 96*
                       m.b17*m.b31*m.b34 - 64*m.b17*m.b31*m.b35 - 32*m.b17*m.b31*m.b36 - 224*m.b17*m.b32*m.b33 - 128*
                       m.b17*m.b32*m.b34 - 64*m.b17*m.b32*m.b35 - 32*m.b17*m.b32*m.b36 - 160*m.b17*m.b33*m.b34 - 64*
                       m.b17*m.b33*m.b35 - 32*m.b17*m.b33*m.b36 - 96*m.b17*m.b34*m.b35 - 32*m.b17*m.b34*m.b36 - 32*m.b17
                       *m.b35*m.b36 - 1088*m.b18*m.b19*m.b20 - 1536*m.b18*m.b19*m.b21 - 1408*m.b18*m.b19*m.b22 - 1280*
                       m.b18*m.b19*m.b23 - 1152*m.b18*m.b19*m.b24 - 1024*m.b18*m.b19*m.b25 - 896*m.b18*m.b19*m.b26 - 768
                       *m.b18*m.b19*m.b27 - 640*m.b18*m.b19*m.b28 - 544*m.b18*m.b19*m.b29 - 480*m.b18*m.b19*m.b30 - 416*
                       m.b18*m.b19*m.b31 - 352*m.b18*m.b19*m.b32 - 288*m.b18*m.b19*m.b33 - 224*m.b18*m.b19*m.b34 - 160*
                       m.b18*m.b19*m.b35 - 96*m.b18*m.b19*m.b36 - 32*m.b18*m.b19*m.b37 - 1536*m.b18*m.b20*m.b21 - 896*
                       m.b18*m.b20*m.b22 - 1280*m.b18*m.b20*m.b23 - 1152*m.b18*m.b20*m.b24 - 1024*m.b18*m.b20*m.b25 - 
                       896*m.b18*m.b20*m.b26 - 768*m.b18*m.b20*m.b27 - 640*m.b18*m.b20*m.b28 - 512*m.b18*m.b20*m.b29 - 
                       448*m.b18*m.b20*m.b30 - 384*m.b18*m.b20*m.b31 - 320*m.b18*m.b20*m.b32 - 256*m.b18*m.b20*m.b33 - 
                       192*m.b18*m.b20*m.b34 - 128*m.b18*m.b20*m.b35 - 64*m.b18*m.b20*m.b36 - 32*m.b18*m.b20*m.b37 - 
                       1408*m.b18*m.b21*m.b22 - 1280*m.b18*m.b21*m.b23 - 704*m.b18*m.b21*m.b24 - 1024*m.b18*m.b21*m.b25
                        - 896*m.b18*m.b21*m.b26 - 768*m.b18*m.b21*m.b27 - 640*m.b18*m.b21*m.b28 - 512*m.b18*m.b21*m.b29
                        - 416*m.b18*m.b21*m.b30 - 352*m.b18*m.b21*m.b31 - 288*m.b18*m.b21*m.b32 - 224*m.b18*m.b21*m.b33
                        - 160*m.b18*m.b21*m.b34 - 96*m.b18*m.b21*m.b35 - 64*m.b18*m.b21*m.b36 - 32*m.b18*m.b21*m.b37 - 
                       1280*m.b18*m.b22*m.b23 - 1152*m.b18*m.b22*m.b24 - 1024*m.b18*m.b22*m.b25 - 512*m.b18*m.b22*m.b26
                        - 768*m.b18*m.b22*m.b27 - 640*m.b18*m.b22*m.b28 - 512*m.b18*m.b22*m.b29 - 384*m.b18*m.b22*m.b30
                        - 320*m.b18*m.b22*m.b31 - 256*m.b18*m.b22*m.b32 - 192*m.b18*m.b22*m.b33 - 128*m.b18*m.b22*m.b34
                        - 96*m.b18*m.b22*m.b35 - 64*m.b18*m.b22*m.b36 - 32*m.b18*m.b22*m.b37 - 1152*m.b18*m.b23*m.b24 - 
                       1024*m.b18*m.b23*m.b25 - 896*m.b18*m.b23*m.b26 - 768*m.b18*m.b23*m.b27 - 320*m.b18*m.b23*m.b28 - 
                       512*m.b18*m.b23*m.b29 - 384*m.b18*m.b23*m.b30 - 288*m.b18*m.b23*m.b31 - 224*m.b18*m.b23*m.b32 - 
                       160*m.b18*m.b23*m.b33 - 128*m.b18*m.b23*m.b34 - 96*m.b18*m.b23*m.b35 - 64*m.b18*m.b23*m.b36 - 32*
                       m.b18*m.b23*m.b37 - 1024*m.b18*m.b24*m.b25 - 896*m.b18*m.b24*m.b26 - 768*m.b18*m.b24*m.b27 - 640*
                       m.b18*m.b24*m.b28 - 512*m.b18*m.b24*m.b29 - 128*m.b18*m.b24*m.b30 - 256*m.b18*m.b24*m.b31 - 192*
                       m.b18*m.b24*m.b32 - 160*m.b18*m.b24*m.b33 - 128*m.b18*m.b24*m.b34 - 96*m.b18*m.b24*m.b35 - 64*
                       m.b18*m.b24*m.b36 - 32*m.b18*m.b24*m.b37 - 896*m.b18*m.b25*m.b26 - 768*m.b18*m.b25*m.b27 - 640*
                       m.b18*m.b25*m.b28 - 512*m.b18*m.b25*m.b29 - 384*m.b18*m.b25*m.b30 - 256*m.b18*m.b25*m.b31 - 160*
                       m.b18*m.b25*m.b33 - 128*m.b18*m.b25*m.b34 - 96*m.b18*m.b25*m.b35 - 64*m.b18*m.b25*m.b36 - 32*
                       m.b18*m.b25*m.b37 - 768*m.b18*m.b26*m.b27 - 640*m.b18*m.b26*m.b28 - 512*m.b18*m.b26*m.b29 - 384*
                       m.b18*m.b26*m.b30 - 288*m.b18*m.b26*m.b31 - 192*m.b18*m.b26*m.b32 - 160*m.b18*m.b26*m.b33 - 96*
                       m.b18*m.b26*m.b35 - 64*m.b18*m.b26*m.b36 - 32*m.b18*m.b26*m.b37 - 640*m.b18*m.b27*m.b28 - 512*
                       m.b18*m.b27*m.b29 - 416*m.b18*m.b27*m.b30 - 320*m.b18*m.b27*m.b31 - 224*m.b18*m.b27*m.b32 - 160*
                       m.b18*m.b27*m.b33 - 128*m.b18*m.b27*m.b34 - 96*m.b18*m.b27*m.b35 - 32*m.b18*m.b27*m.b37 - 544*
                       m.b18*m.b28*m.b29 - 448*m.b18*m.b28*m.b30 - 352*m.b18*m.b28*m.b31 - 256*m.b18*m.b28*m.b32 - 160*
                       m.b18*m.b28*m.b33 - 128*m.b18*m.b28*m.b34 - 96*m.b18*m.b28*m.b35 - 64*m.b18*m.b28*m.b36 - 32*
                       m.b18*m.b28*m.b37 - 480*m.b18*m.b29*m.b30 - 384*m.b18*m.b29*m.b31 - 288*m.b18*m.b29*m.b32 - 192*
                       m.b18*m.b29*m.b33 - 128*m.b18*m.b29*m.b34 - 96*m.b18*m.b29*m.b35 - 64*m.b18*m.b29*m.b36 - 32*
                       m.b18*m.b29*m.b37 - 416*m.b18*m.b30*m.b31 - 320*m.b18*m.b30*m.b32 - 224*m.b18*m.b30*m.b33 - 128*
                       m.b18*m.b30*m.b34 - 96*m.b18*m.b30*m.b35 - 64*m.b18*m.b30*m.b36 - 32*m.b18*m.b30*m.b37 - 352*
                       m.b18*m.b31*m.b32 - 256*m.b18*m.b31*m.b33 - 160*m.b18*m.b31*m.b34 - 96*m.b18*m.b31*m.b35 - 64*
                       m.b18*m.b31*m.b36 - 32*m.b18*m.b31*m.b37 - 288*m.b18*m.b32*m.b33 - 192*m.b18*m.b32*m.b34 - 96*
                       m.b18*m.b32*m.b35 - 64*m.b18*m.b32*m.b36 - 32*m.b18*m.b32*m.b37 - 224*m.b18*m.b33*m.b34 - 128*
                       m.b18*m.b33*m.b35 - 64*m.b18*m.b33*m.b36 - 32*m.b18*m.b33*m.b37 - 160*m.b18*m.b34*m.b35 - 64*
                       m.b18*m.b34*m.b36 - 32*m.b18*m.b34*m.b37 - 96*m.b18*m.b35*m.b36 - 32*m.b18*m.b35*m.b37 - 32*m.b18
                       *m.b36*m.b37 - 1088*m.b19*m.b20*m.b21 - 1536*m.b19*m.b20*m.b22 - 1408*m.b19*m.b20*m.b23 - 1280*
                       m.b19*m.b20*m.b24 - 1152*m.b19*m.b20*m.b25 - 1024*m.b19*m.b20*m.b26 - 896*m.b19*m.b20*m.b27 - 768
                       *m.b19*m.b20*m.b28 - 640*m.b19*m.b20*m.b29 - 544*m.b19*m.b20*m.b30 - 480*m.b19*m.b20*m.b31 - 416*
                       m.b19*m.b20*m.b32 - 352*m.b19*m.b20*m.b33 - 288*m.b19*m.b20*m.b34 - 224*m.b19*m.b20*m.b35 - 160*
                       m.b19*m.b20*m.b36 - 96*m.b19*m.b20*m.b37 - 32*m.b19*m.b20*m.b38 - 1536*m.b19*m.b21*m.b22 - 896*
                       m.b19*m.b21*m.b23 - 1280*m.b19*m.b21*m.b24 - 1152*m.b19*m.b21*m.b25 - 1024*m.b19*m.b21*m.b26 - 
                       896*m.b19*m.b21*m.b27 - 768*m.b19*m.b21*m.b28 - 640*m.b19*m.b21*m.b29 - 512*m.b19*m.b21*m.b30 - 
                       448*m.b19*m.b21*m.b31 - 384*m.b19*m.b21*m.b32 - 320*m.b19*m.b21*m.b33 - 256*m.b19*m.b21*m.b34 - 
                       192*m.b19*m.b21*m.b35 - 128*m.b19*m.b21*m.b36 - 64*m.b19*m.b21*m.b37 - 32*m.b19*m.b21*m.b38 - 
                       1408*m.b19*m.b22*m.b23 - 1280*m.b19*m.b22*m.b24 - 704*m.b19*m.b22*m.b25 - 1024*m.b19*m.b22*m.b26
                        - 896*m.b19*m.b22*m.b27 - 768*m.b19*m.b22*m.b28 - 640*m.b19*m.b22*m.b29 - 512*m.b19*m.b22*m.b30
                        - 416*m.b19*m.b22*m.b31 - 352*m.b19*m.b22*m.b32 - 288*m.b19*m.b22*m.b33 - 224*m.b19*m.b22*m.b34
                        - 160*m.b19*m.b22*m.b35 - 96*m.b19*m.b22*m.b36 - 64*m.b19*m.b22*m.b37 - 32*m.b19*m.b22*m.b38 - 
                       1280*m.b19*m.b23*m.b24 - 1152*m.b19*m.b23*m.b25 - 1024*m.b19*m.b23*m.b26 - 512*m.b19*m.b23*m.b27
                        - 768*m.b19*m.b23*m.b28 - 640*m.b19*m.b23*m.b29 - 512*m.b19*m.b23*m.b30 - 384*m.b19*m.b23*m.b31
                        - 320*m.b19*m.b23*m.b32 - 256*m.b19*m.b23*m.b33 - 192*m.b19*m.b23*m.b34 - 128*m.b19*m.b23*m.b35
                        - 96*m.b19*m.b23*m.b36 - 64*m.b19*m.b23*m.b37 - 32*m.b19*m.b23*m.b38 - 1152*m.b19*m.b24*m.b25 - 
                       1024*m.b19*m.b24*m.b26 - 896*m.b19*m.b24*m.b27 - 768*m.b19*m.b24*m.b28 - 320*m.b19*m.b24*m.b29 - 
                       512*m.b19*m.b24*m.b30 - 384*m.b19*m.b24*m.b31 - 288*m.b19*m.b24*m.b32 - 224*m.b19*m.b24*m.b33 - 
                       160*m.b19*m.b24*m.b34 - 128*m.b19*m.b24*m.b35 - 96*m.b19*m.b24*m.b36 - 64*m.b19*m.b24*m.b37 - 32*
                       m.b19*m.b24*m.b38 - 1024*m.b19*m.b25*m.b26 - 896*m.b19*m.b25*m.b27 - 768*m.b19*m.b25*m.b28 - 640*
                       m.b19*m.b25*m.b29 - 512*m.b19*m.b25*m.b30 - 128*m.b19*m.b25*m.b31 - 256*m.b19*m.b25*m.b32 - 192*
                       m.b19*m.b25*m.b33 - 160*m.b19*m.b25*m.b34 - 128*m.b19*m.b25*m.b35 - 96*m.b19*m.b25*m.b36 - 64*
                       m.b19*m.b25*m.b37 - 32*m.b19*m.b25*m.b38 - 896*m.b19*m.b26*m.b27 - 768*m.b19*m.b26*m.b28 - 640*
                       m.b19*m.b26*m.b29 - 512*m.b19*m.b26*m.b30 - 384*m.b19*m.b26*m.b31 - 256*m.b19*m.b26*m.b32 - 160*
                       m.b19*m.b26*m.b34 - 128*m.b19*m.b26*m.b35 - 96*m.b19*m.b26*m.b36 - 64*m.b19*m.b26*m.b37 - 32*
                       m.b19*m.b26*m.b38 - 768*m.b19*m.b27*m.b28 - 640*m.b19*m.b27*m.b29 - 512*m.b19*m.b27*m.b30 - 384*
                       m.b19*m.b27*m.b31 - 288*m.b19*m.b27*m.b32 - 192*m.b19*m.b27*m.b33 - 160*m.b19*m.b27*m.b34 - 96*
                       m.b19*m.b27*m.b36 - 64*m.b19*m.b27*m.b37 - 32*m.b19*m.b27*m.b38 - 640*m.b19*m.b28*m.b29 - 512*
                       m.b19*m.b28*m.b30 - 416*m.b19*m.b28*m.b31 - 320*m.b19*m.b28*m.b32 - 224*m.b19*m.b28*m.b33 - 160*
                       m.b19*m.b28*m.b34 - 128*m.b19*m.b28*m.b35 - 96*m.b19*m.b28*m.b36 - 32*m.b19*m.b28*m.b38 - 544*
                       m.b19*m.b29*m.b30 - 448*m.b19*m.b29*m.b31 - 352*m.b19*m.b29*m.b32 - 256*m.b19*m.b29*m.b33 - 160*
                       m.b19*m.b29*m.b34 - 128*m.b19*m.b29*m.b35 - 96*m.b19*m.b29*m.b36 - 64*m.b19*m.b29*m.b37 - 32*
                       m.b19*m.b29*m.b38 - 480*m.b19*m.b30*m.b31 - 384*m.b19*m.b30*m.b32 - 288*m.b19*m.b30*m.b33 - 192*
                       m.b19*m.b30*m.b34 - 128*m.b19*m.b30*m.b35 - 96*m.b19*m.b30*m.b36 - 64*m.b19*m.b30*m.b37 - 32*
                       m.b19*m.b30*m.b38 - 416*m.b19*m.b31*m.b32 - 320*m.b19*m.b31*m.b33 - 224*m.b19*m.b31*m.b34 - 128*
                       m.b19*m.b31*m.b35 - 96*m.b19*m.b31*m.b36 - 64*m.b19*m.b31*m.b37 - 32*m.b19*m.b31*m.b38 - 352*
                       m.b19*m.b32*m.b33 - 256*m.b19*m.b32*m.b34 - 160*m.b19*m.b32*m.b35 - 96*m.b19*m.b32*m.b36 - 64*
                       m.b19*m.b32*m.b37 - 32*m.b19*m.b32*m.b38 - 288*m.b19*m.b33*m.b34 - 192*m.b19*m.b33*m.b35 - 96*
                       m.b19*m.b33*m.b36 - 64*m.b19*m.b33*m.b37 - 32*m.b19*m.b33*m.b38 - 224*m.b19*m.b34*m.b35 - 128*
                       m.b19*m.b34*m.b36 - 64*m.b19*m.b34*m.b37 - 32*m.b19*m.b34*m.b38 - 160*m.b19*m.b35*m.b36 - 64*
                       m.b19*m.b35*m.b37 - 32*m.b19*m.b35*m.b38 - 96*m.b19*m.b36*m.b37 - 32*m.b19*m.b36*m.b38 - 32*m.b19
                       *m.b37*m.b38 - 1088*m.b20*m.b21*m.b22 - 1536*m.b20*m.b21*m.b23 - 1408*m.b20*m.b21*m.b24 - 1280*
                       m.b20*m.b21*m.b25 - 1152*m.b20*m.b21*m.b26 - 1024*m.b20*m.b21*m.b27 - 896*m.b20*m.b21*m.b28 - 768
                       *m.b20*m.b21*m.b29 - 640*m.b20*m.b21*m.b30 - 544*m.b20*m.b21*m.b31 - 480*m.b20*m.b21*m.b32 - 416*
                       m.b20*m.b21*m.b33 - 352*m.b20*m.b21*m.b34 - 288*m.b20*m.b21*m.b35 - 224*m.b20*m.b21*m.b36 - 160*
                       m.b20*m.b21*m.b37 - 96*m.b20*m.b21*m.b38 - 32*m.b20*m.b21*m.b39 - 1536*m.b20*m.b22*m.b23 - 896*
                       m.b20*m.b22*m.b24 - 1280*m.b20*m.b22*m.b25 - 1152*m.b20*m.b22*m.b26 - 1024*m.b20*m.b22*m.b27 - 
                       896*m.b20*m.b22*m.b28 - 768*m.b20*m.b22*m.b29 - 640*m.b20*m.b22*m.b30 - 512*m.b20*m.b22*m.b31 - 
                       448*m.b20*m.b22*m.b32 - 384*m.b20*m.b22*m.b33 - 320*m.b20*m.b22*m.b34 - 256*m.b20*m.b22*m.b35 - 
                       192*m.b20*m.b22*m.b36 - 128*m.b20*m.b22*m.b37 - 64*m.b20*m.b22*m.b38 - 32*m.b20*m.b22*m.b39 - 
                       1408*m.b20*m.b23*m.b24 - 1280*m.b20*m.b23*m.b25 - 704*m.b20*m.b23*m.b26 - 1024*m.b20*m.b23*m.b27
                        - 896*m.b20*m.b23*m.b28 - 768*m.b20*m.b23*m.b29 - 640*m.b20*m.b23*m.b30 - 512*m.b20*m.b23*m.b31
                        - 416*m.b20*m.b23*m.b32 - 352*m.b20*m.b23*m.b33 - 288*m.b20*m.b23*m.b34 - 224*m.b20*m.b23*m.b35
                        - 160*m.b20*m.b23*m.b36 - 96*m.b20*m.b23*m.b37 - 64*m.b20*m.b23*m.b38 - 32*m.b20*m.b23*m.b39 - 
                       1280*m.b20*m.b24*m.b25 - 1152*m.b20*m.b24*m.b26 - 1024*m.b20*m.b24*m.b27 - 512*m.b20*m.b24*m.b28
                        - 768*m.b20*m.b24*m.b29 - 640*m.b20*m.b24*m.b30 - 512*m.b20*m.b24*m.b31 - 384*m.b20*m.b24*m.b32
                        - 320*m.b20*m.b24*m.b33 - 256*m.b20*m.b24*m.b34 - 192*m.b20*m.b24*m.b35 - 128*m.b20*m.b24*m.b36
                        - 96*m.b20*m.b24*m.b37 - 64*m.b20*m.b24*m.b38 - 32*m.b20*m.b24*m.b39 - 1152*m.b20*m.b25*m.b26 - 
                       1024*m.b20*m.b25*m.b27 - 896*m.b20*m.b25*m.b28 - 768*m.b20*m.b25*m.b29 - 320*m.b20*m.b25*m.b30 - 
                       512*m.b20*m.b25*m.b31 - 384*m.b20*m.b25*m.b32 - 288*m.b20*m.b25*m.b33 - 224*m.b20*m.b25*m.b34 - 
                       160*m.b20*m.b25*m.b35 - 128*m.b20*m.b25*m.b36 - 96*m.b20*m.b25*m.b37 - 64*m.b20*m.b25*m.b38 - 32*
                       m.b20*m.b25*m.b39 - 1024*m.b20*m.b26*m.b27 - 896*m.b20*m.b26*m.b28 - 768*m.b20*m.b26*m.b29 - 640*
                       m.b20*m.b26*m.b30 - 512*m.b20*m.b26*m.b31 - 128*m.b20*m.b26*m.b32 - 256*m.b20*m.b26*m.b33 - 192*
                       m.b20*m.b26*m.b34 - 160*m.b20*m.b26*m.b35 - 128*m.b20*m.b26*m.b36 - 96*m.b20*m.b26*m.b37 - 64*
                       m.b20*m.b26*m.b38 - 32*m.b20*m.b26*m.b39 - 896*m.b20*m.b27*m.b28 - 768*m.b20*m.b27*m.b29 - 640*
                       m.b20*m.b27*m.b30 - 512*m.b20*m.b27*m.b31 - 384*m.b20*m.b27*m.b32 - 256*m.b20*m.b27*m.b33 - 160*
                       m.b20*m.b27*m.b35 - 128*m.b20*m.b27*m.b36 - 96*m.b20*m.b27*m.b37 - 64*m.b20*m.b27*m.b38 - 32*
                       m.b20*m.b27*m.b39 - 768*m.b20*m.b28*m.b29 - 640*m.b20*m.b28*m.b30 - 512*m.b20*m.b28*m.b31 - 384*
                       m.b20*m.b28*m.b32 - 288*m.b20*m.b28*m.b33 - 192*m.b20*m.b28*m.b34 - 160*m.b20*m.b28*m.b35 - 96*
                       m.b20*m.b28*m.b37 - 64*m.b20*m.b28*m.b38 - 32*m.b20*m.b28*m.b39 - 640*m.b20*m.b29*m.b30 - 512*
                       m.b20*m.b29*m.b31 - 416*m.b20*m.b29*m.b32 - 320*m.b20*m.b29*m.b33 - 224*m.b20*m.b29*m.b34 - 160*
                       m.b20*m.b29*m.b35 - 128*m.b20*m.b29*m.b36 - 96*m.b20*m.b29*m.b37 - 32*m.b20*m.b29*m.b39 - 544*
                       m.b20*m.b30*m.b31 - 448*m.b20*m.b30*m.b32 - 352*m.b20*m.b30*m.b33 - 256*m.b20*m.b30*m.b34 - 160*
                       m.b20*m.b30*m.b35 - 128*m.b20*m.b30*m.b36 - 96*m.b20*m.b30*m.b37 - 64*m.b20*m.b30*m.b38 - 32*
                       m.b20*m.b30*m.b39 - 480*m.b20*m.b31*m.b32 - 384*m.b20*m.b31*m.b33 - 288*m.b20*m.b31*m.b34 - 192*
                       m.b20*m.b31*m.b35 - 128*m.b20*m.b31*m.b36 - 96*m.b20*m.b31*m.b37 - 64*m.b20*m.b31*m.b38 - 32*
                       m.b20*m.b31*m.b39 - 416*m.b20*m.b32*m.b33 - 320*m.b20*m.b32*m.b34 - 224*m.b20*m.b32*m.b35 - 128*
                       m.b20*m.b32*m.b36 - 96*m.b20*m.b32*m.b37 - 64*m.b20*m.b32*m.b38 - 32*m.b20*m.b32*m.b39 - 352*
                       m.b20*m.b33*m.b34 - 256*m.b20*m.b33*m.b35 - 160*m.b20*m.b33*m.b36 - 96*m.b20*m.b33*m.b37 - 64*
                       m.b20*m.b33*m.b38 - 32*m.b20*m.b33*m.b39 - 288*m.b20*m.b34*m.b35 - 192*m.b20*m.b34*m.b36 - 96*
                       m.b20*m.b34*m.b37 - 64*m.b20*m.b34*m.b38 - 32*m.b20*m.b34*m.b39 - 224*m.b20*m.b35*m.b36 - 128*
                       m.b20*m.b35*m.b37 - 64*m.b20*m.b35*m.b38 - 32*m.b20*m.b35*m.b39 - 160*m.b20*m.b36*m.b37 - 64*
                       m.b20*m.b36*m.b38 - 32*m.b20*m.b36*m.b39 - 96*m.b20*m.b37*m.b38 - 32*m.b20*m.b37*m.b39 - 32*m.b20
                       *m.b38*m.b39 - 1088*m.b21*m.b22*m.b23 - 1536*m.b21*m.b22*m.b24 - 1408*m.b21*m.b22*m.b25 - 1280*
                       m.b21*m.b22*m.b26 - 1152*m.b21*m.b22*m.b27 - 1024*m.b21*m.b22*m.b28 - 896*m.b21*m.b22*m.b29 - 768
                       *m.b21*m.b22*m.b30 - 640*m.b21*m.b22*m.b31 - 544*m.b21*m.b22*m.b32 - 480*m.b21*m.b22*m.b33 - 416*
                       m.b21*m.b22*m.b34 - 352*m.b21*m.b22*m.b35 - 288*m.b21*m.b22*m.b36 - 224*m.b21*m.b22*m.b37 - 160*
                       m.b21*m.b22*m.b38 - 96*m.b21*m.b22*m.b39 - 32*m.b21*m.b22*m.b40 - 1536*m.b21*m.b23*m.b24 - 896*
                       m.b21*m.b23*m.b25 - 1280*m.b21*m.b23*m.b26 - 1152*m.b21*m.b23*m.b27 - 1024*m.b21*m.b23*m.b28 - 
                       896*m.b21*m.b23*m.b29 - 768*m.b21*m.b23*m.b30 - 640*m.b21*m.b23*m.b31 - 512*m.b21*m.b23*m.b32 - 
                       448*m.b21*m.b23*m.b33 - 384*m.b21*m.b23*m.b34 - 320*m.b21*m.b23*m.b35 - 256*m.b21*m.b23*m.b36 - 
                       192*m.b21*m.b23*m.b37 - 128*m.b21*m.b23*m.b38 - 64*m.b21*m.b23*m.b39 - 32*m.b21*m.b23*m.b40 - 
                       1408*m.b21*m.b24*m.b25 - 1280*m.b21*m.b24*m.b26 - 704*m.b21*m.b24*m.b27 - 1024*m.b21*m.b24*m.b28
                        - 896*m.b21*m.b24*m.b29 - 768*m.b21*m.b24*m.b30 - 640*m.b21*m.b24*m.b31 - 512*m.b21*m.b24*m.b32
                        - 416*m.b21*m.b24*m.b33 - 352*m.b21*m.b24*m.b34 - 288*m.b21*m.b24*m.b35 - 224*m.b21*m.b24*m.b36
                        - 160*m.b21*m.b24*m.b37 - 96*m.b21*m.b24*m.b38 - 64*m.b21*m.b24*m.b39 - 32*m.b21*m.b24*m.b40 - 
                       1280*m.b21*m.b25*m.b26 - 1152*m.b21*m.b25*m.b27 - 1024*m.b21*m.b25*m.b28 - 512*m.b21*m.b25*m.b29
                        - 768*m.b21*m.b25*m.b30 - 640*m.b21*m.b25*m.b31 - 512*m.b21*m.b25*m.b32 - 384*m.b21*m.b25*m.b33
                        - 320*m.b21*m.b25*m.b34 - 256*m.b21*m.b25*m.b35 - 192*m.b21*m.b25*m.b36 - 128*m.b21*m.b25*m.b37
                        - 96*m.b21*m.b25*m.b38 - 64*m.b21*m.b25*m.b39 - 32*m.b21*m.b25*m.b40 - 1152*m.b21*m.b26*m.b27 - 
                       1024*m.b21*m.b26*m.b28 - 896*m.b21*m.b26*m.b29 - 768*m.b21*m.b26*m.b30 - 320*m.b21*m.b26*m.b31 - 
                       512*m.b21*m.b26*m.b32 - 384*m.b21*m.b26*m.b33 - 288*m.b21*m.b26*m.b34 - 224*m.b21*m.b26*m.b35 - 
                       160*m.b21*m.b26*m.b36 - 128*m.b21*m.b26*m.b37 - 96*m.b21*m.b26*m.b38 - 64*m.b21*m.b26*m.b39 - 32*
                       m.b21*m.b26*m.b40 - 1024*m.b21*m.b27*m.b28 - 896*m.b21*m.b27*m.b29 - 768*m.b21*m.b27*m.b30 - 640*
                       m.b21*m.b27*m.b31 - 512*m.b21*m.b27*m.b32 - 128*m.b21*m.b27*m.b33 - 256*m.b21*m.b27*m.b34 - 192*
                       m.b21*m.b27*m.b35 - 160*m.b21*m.b27*m.b36 - 128*m.b21*m.b27*m.b37 - 96*m.b21*m.b27*m.b38 - 64*
                       m.b21*m.b27*m.b39 - 32*m.b21*m.b27*m.b40 - 896*m.b21*m.b28*m.b29 - 768*m.b21*m.b28*m.b30 - 640*
                       m.b21*m.b28*m.b31 - 512*m.b21*m.b28*m.b32 - 384*m.b21*m.b28*m.b33 - 256*m.b21*m.b28*m.b34 - 160*
                       m.b21*m.b28*m.b36 - 128*m.b21*m.b28*m.b37 - 96*m.b21*m.b28*m.b38 - 64*m.b21*m.b28*m.b39 - 32*
                       m.b21*m.b28*m.b40 - 768*m.b21*m.b29*m.b30 - 640*m.b21*m.b29*m.b31 - 512*m.b21*m.b29*m.b32 - 384*
                       m.b21*m.b29*m.b33 - 288*m.b21*m.b29*m.b34 - 192*m.b21*m.b29*m.b35 - 160*m.b21*m.b29*m.b36 - 96*
                       m.b21*m.b29*m.b38 - 64*m.b21*m.b29*m.b39 - 32*m.b21*m.b29*m.b40 - 640*m.b21*m.b30*m.b31 - 512*
                       m.b21*m.b30*m.b32 - 416*m.b21*m.b30*m.b33 - 320*m.b21*m.b30*m.b34 - 224*m.b21*m.b30*m.b35 - 160*
                       m.b21*m.b30*m.b36 - 128*m.b21*m.b30*m.b37 - 96*m.b21*m.b30*m.b38 - 32*m.b21*m.b30*m.b40 - 544*
                       m.b21*m.b31*m.b32 - 448*m.b21*m.b31*m.b33 - 352*m.b21*m.b31*m.b34 - 256*m.b21*m.b31*m.b35 - 160*
                       m.b21*m.b31*m.b36 - 128*m.b21*m.b31*m.b37 - 96*m.b21*m.b31*m.b38 - 64*m.b21*m.b31*m.b39 - 32*
                       m.b21*m.b31*m.b40 - 480*m.b21*m.b32*m.b33 - 384*m.b21*m.b32*m.b34 - 288*m.b21*m.b32*m.b35 - 192*
                       m.b21*m.b32*m.b36 - 128*m.b21*m.b32*m.b37 - 96*m.b21*m.b32*m.b38 - 64*m.b21*m.b32*m.b39 - 32*
                       m.b21*m.b32*m.b40 - 416*m.b21*m.b33*m.b34 - 320*m.b21*m.b33*m.b35 - 224*m.b21*m.b33*m.b36 - 128*
                       m.b21*m.b33*m.b37 - 96*m.b21*m.b33*m.b38 - 64*m.b21*m.b33*m.b39 - 32*m.b21*m.b33*m.b40 - 352*
                       m.b21*m.b34*m.b35 - 256*m.b21*m.b34*m.b36 - 160*m.b21*m.b34*m.b37 - 96*m.b21*m.b34*m.b38 - 64*
                       m.b21*m.b34*m.b39 - 32*m.b21*m.b34*m.b40 - 288*m.b21*m.b35*m.b36 - 192*m.b21*m.b35*m.b37 - 96*
                       m.b21*m.b35*m.b38 - 64*m.b21*m.b35*m.b39 - 32*m.b21*m.b35*m.b40 - 224*m.b21*m.b36*m.b37 - 128*
                       m.b21*m.b36*m.b38 - 64*m.b21*m.b36*m.b39 - 32*m.b21*m.b36*m.b40 - 160*m.b21*m.b37*m.b38 - 64*
                       m.b21*m.b37*m.b39 - 32*m.b21*m.b37*m.b40 - 96*m.b21*m.b38*m.b39 - 32*m.b21*m.b38*m.b40 - 32*m.b21
                       *m.b39*m.b40 - 1056*m.b22*m.b23*m.b24 - 1472*m.b22*m.b23*m.b25 - 1344*m.b22*m.b23*m.b26 - 1216*
                       m.b22*m.b23*m.b27 - 1088*m.b22*m.b23*m.b28 - 960*m.b22*m.b23*m.b29 - 832*m.b22*m.b23*m.b30 - 704*
                       m.b22*m.b23*m.b31 - 576*m.b22*m.b23*m.b32 - 480*m.b22*m.b23*m.b33 - 416*m.b22*m.b23*m.b34 - 352*
                       m.b22*m.b23*m.b35 - 288*m.b22*m.b23*m.b36 - 224*m.b22*m.b23*m.b37 - 160*m.b22*m.b23*m.b38 - 96*
                       m.b22*m.b23*m.b39 - 32*m.b22*m.b23*m.b40 - 1472*m.b22*m.b24*m.b25 - 864*m.b22*m.b24*m.b26 - 1216*
                       m.b22*m.b24*m.b27 - 1088*m.b22*m.b24*m.b28 - 960*m.b22*m.b24*m.b29 - 832*m.b22*m.b24*m.b30 - 704*
                       m.b22*m.b24*m.b31 - 576*m.b22*m.b24*m.b32 - 448*m.b22*m.b24*m.b33 - 384*m.b22*m.b24*m.b34 - 320*
                       m.b22*m.b24*m.b35 - 256*m.b22*m.b24*m.b36 - 192*m.b22*m.b24*m.b37 - 128*m.b22*m.b24*m.b38 - 64*
                       m.b22*m.b24*m.b39 - 32*m.b22*m.b24*m.b40 - 1344*m.b22*m.b25*m.b26 - 1216*m.b22*m.b25*m.b27 - 672*
                       m.b22*m.b25*m.b28 - 960*m.b22*m.b25*m.b29 - 832*m.b22*m.b25*m.b30 - 704*m.b22*m.b25*m.b31 - 576*
                       m.b22*m.b25*m.b32 - 448*m.b22*m.b25*m.b33 - 352*m.b22*m.b25*m.b34 - 288*m.b22*m.b25*m.b35 - 224*
                       m.b22*m.b25*m.b36 - 160*m.b22*m.b25*m.b37 - 96*m.b22*m.b25*m.b38 - 64*m.b22*m.b25*m.b39 - 32*
                       m.b22*m.b25*m.b40 - 1216*m.b22*m.b26*m.b27 - 1088*m.b22*m.b26*m.b28 - 960*m.b22*m.b26*m.b29 - 480
                       *m.b22*m.b26*m.b30 - 704*m.b22*m.b26*m.b31 - 576*m.b22*m.b26*m.b32 - 448*m.b22*m.b26*m.b33 - 320*
                       m.b22*m.b26*m.b34 - 256*m.b22*m.b26*m.b35 - 192*m.b22*m.b26*m.b36 - 128*m.b22*m.b26*m.b37 - 96*
                       m.b22*m.b26*m.b38 - 64*m.b22*m.b26*m.b39 - 32*m.b22*m.b26*m.b40 - 1088*m.b22*m.b27*m.b28 - 960*
                       m.b22*m.b27*m.b29 - 832*m.b22*m.b27*m.b30 - 704*m.b22*m.b27*m.b31 - 288*m.b22*m.b27*m.b32 - 448*
                       m.b22*m.b27*m.b33 - 320*m.b22*m.b27*m.b34 - 224*m.b22*m.b27*m.b35 - 160*m.b22*m.b27*m.b36 - 128*
                       m.b22*m.b27*m.b37 - 96*m.b22*m.b27*m.b38 - 64*m.b22*m.b27*m.b39 - 32*m.b22*m.b27*m.b40 - 960*
                       m.b22*m.b28*m.b29 - 832*m.b22*m.b28*m.b30 - 704*m.b22*m.b28*m.b31 - 576*m.b22*m.b28*m.b32 - 448*
                       m.b22*m.b28*m.b33 - 96*m.b22*m.b28*m.b34 - 192*m.b22*m.b28*m.b35 - 160*m.b22*m.b28*m.b36 - 128*
                       m.b22*m.b28*m.b37 - 96*m.b22*m.b28*m.b38 - 64*m.b22*m.b28*m.b39 - 32*m.b22*m.b28*m.b40 - 832*
                       m.b22*m.b29*m.b30 - 704*m.b22*m.b29*m.b31 - 576*m.b22*m.b29*m.b32 - 448*m.b22*m.b29*m.b33 - 320*
                       m.b22*m.b29*m.b34 - 224*m.b22*m.b29*m.b35 - 128*m.b22*m.b29*m.b37 - 96*m.b22*m.b29*m.b38 - 64*
                       m.b22*m.b29*m.b39 - 32*m.b22*m.b29*m.b40 - 704*m.b22*m.b30*m.b31 - 576*m.b22*m.b30*m.b32 - 448*
                       m.b22*m.b30*m.b33 - 352*m.b22*m.b30*m.b34 - 256*m.b22*m.b30*m.b35 - 160*m.b22*m.b30*m.b36 - 128*
                       m.b22*m.b30*m.b37 - 64*m.b22*m.b30*m.b39 - 32*m.b22*m.b30*m.b40 - 576*m.b22*m.b31*m.b32 - 480*
                       m.b22*m.b31*m.b33 - 384*m.b22*m.b31*m.b34 - 288*m.b22*m.b31*m.b35 - 192*m.b22*m.b31*m.b36 - 128*
                       m.b22*m.b31*m.b37 - 96*m.b22*m.b31*m.b38 - 64*m.b22*m.b31*m.b39 - 512*m.b22*m.b32*m.b33 - 416*
                       m.b22*m.b32*m.b34 - 320*m.b22*m.b32*m.b35 - 224*m.b22*m.b32*m.b36 - 128*m.b22*m.b32*m.b37 - 96*
                       m.b22*m.b32*m.b38 - 64*m.b22*m.b32*m.b39 - 32*m.b22*m.b32*m.b40 - 448*m.b22*m.b33*m.b34 - 352*
                       m.b22*m.b33*m.b35 - 256*m.b22*m.b33*m.b36 - 160*m.b22*m.b33*m.b37 - 96*m.b22*m.b33*m.b38 - 64*
                       m.b22*m.b33*m.b39 - 32*m.b22*m.b33*m.b40 - 384*m.b22*m.b34*m.b35 - 288*m.b22*m.b34*m.b36 - 192*
                       m.b22*m.b34*m.b37 - 96*m.b22*m.b34*m.b38 - 64*m.b22*m.b34*m.b39 - 32*m.b22*m.b34*m.b40 - 320*
                       m.b22*m.b35*m.b36 - 224*m.b22*m.b35*m.b37 - 128*m.b22*m.b35*m.b38 - 64*m.b22*m.b35*m.b39 - 32*
                       m.b22*m.b35*m.b40 - 256*m.b22*m.b36*m.b37 - 160*m.b22*m.b36*m.b38 - 64*m.b22*m.b36*m.b39 - 32*
                       m.b22*m.b36*m.b40 - 192*m.b22*m.b37*m.b38 - 96*m.b22*m.b37*m.b39 - 32*m.b22*m.b37*m.b40 - 128*
                       m.b22*m.b38*m.b39 - 32*m.b22*m.b38*m.b40 - 64*m.b22*m.b39*m.b40 - 992*m.b23*m.b24*m.b25 - 1408*
                       m.b23*m.b24*m.b26 - 1280*m.b23*m.b24*m.b27 - 1152*m.b23*m.b24*m.b28 - 1024*m.b23*m.b24*m.b29 - 
                       896*m.b23*m.b24*m.b30 - 768*m.b23*m.b24*m.b31 - 640*m.b23*m.b24*m.b32 - 512*m.b23*m.b24*m.b33 - 
                       416*m.b23*m.b24*m.b34 - 352*m.b23*m.b24*m.b35 - 288*m.b23*m.b24*m.b36 - 224*m.b23*m.b24*m.b37 - 
                       160*m.b23*m.b24*m.b38 - 96*m.b23*m.b24*m.b39 - 32*m.b23*m.b24*m.b40 - 1376*m.b23*m.b25*m.b26 - 
                       832*m.b23*m.b25*m.b27 - 1152*m.b23*m.b25*m.b28 - 1024*m.b23*m.b25*m.b29 - 896*m.b23*m.b25*m.b30
                        - 768*m.b23*m.b25*m.b31 - 640*m.b23*m.b25*m.b32 - 512*m.b23*m.b25*m.b33 - 384*m.b23*m.b25*m.b34
                        - 320*m.b23*m.b25*m.b35 - 256*m.b23*m.b25*m.b36 - 192*m.b23*m.b25*m.b37 - 128*m.b23*m.b25*m.b38
                        - 64*m.b23*m.b25*m.b39 - 32*m.b23*m.b25*m.b40 - 1248*m.b23*m.b26*m.b27 - 1152*m.b23*m.b26*m.b28
                        - 640*m.b23*m.b26*m.b29 - 896*m.b23*m.b26*m.b30 - 768*m.b23*m.b26*m.b31 - 640*m.b23*m.b26*m.b32
                        - 512*m.b23*m.b26*m.b33 - 384*m.b23*m.b26*m.b34 - 288*m.b23*m.b26*m.b35 - 224*m.b23*m.b26*m.b36
                        - 160*m.b23*m.b26*m.b37 - 96*m.b23*m.b26*m.b38 - 64*m.b23*m.b26*m.b39 - 32*m.b23*m.b26*m.b40 - 
                       1120*m.b23*m.b27*m.b28 - 1024*m.b23*m.b27*m.b29 - 896*m.b23*m.b27*m.b30 - 448*m.b23*m.b27*m.b31
                        - 640*m.b23*m.b27*m.b32 - 512*m.b23*m.b27*m.b33 - 384*m.b23*m.b27*m.b34 - 256*m.b23*m.b27*m.b35
                        - 192*m.b23*m.b27*m.b36 - 128*m.b23*m.b27*m.b37 - 96*m.b23*m.b27*m.b38 - 64*m.b23*m.b27*m.b39 - 
                       32*m.b23*m.b27*m.b40 - 992*m.b23*m.b28*m.b29 - 896*m.b23*m.b28*m.b30 - 768*m.b23*m.b28*m.b31 - 
                       640*m.b23*m.b28*m.b32 - 256*m.b23*m.b28*m.b33 - 384*m.b23*m.b28*m.b34 - 256*m.b23*m.b28*m.b35 - 
                       160*m.b23*m.b28*m.b36 - 128*m.b23*m.b28*m.b37 - 96*m.b23*m.b28*m.b38 - 64*m.b23*m.b28*m.b39 - 32*
                       m.b23*m.b28*m.b40 - 864*m.b23*m.b29*m.b30 - 768*m.b23*m.b29*m.b31 - 640*m.b23*m.b29*m.b32 - 512*
                       m.b23*m.b29*m.b33 - 384*m.b23*m.b29*m.b34 - 64*m.b23*m.b29*m.b35 - 160*m.b23*m.b29*m.b36 - 128*
                       m.b23*m.b29*m.b37 - 96*m.b23*m.b29*m.b38 - 64*m.b23*m.b29*m.b39 - 32*m.b23*m.b29*m.b40 - 736*
                       m.b23*m.b30*m.b31 - 640*m.b23*m.b30*m.b32 - 512*m.b23*m.b30*m.b33 - 384*m.b23*m.b30*m.b34 - 288*
                       m.b23*m.b30*m.b35 - 192*m.b23*m.b30*m.b36 - 96*m.b23*m.b30*m.b38 - 64*m.b23*m.b30*m.b39 - 32*
                       m.b23*m.b30*m.b40 - 608*m.b23*m.b31*m.b32 - 512*m.b23*m.b31*m.b33 - 416*m.b23*m.b31*m.b34 - 320*
                       m.b23*m.b31*m.b35 - 224*m.b23*m.b31*m.b36 - 128*m.b23*m.b31*m.b37 - 96*m.b23*m.b31*m.b38 - 32*
                       m.b23*m.b31*m.b40 - 512*m.b23*m.b32*m.b33 - 448*m.b23*m.b32*m.b34 - 352*m.b23*m.b32*m.b35 - 256*
                       m.b23*m.b32*m.b36 - 160*m.b23*m.b32*m.b37 - 96*m.b23*m.b32*m.b38 - 64*m.b23*m.b32*m.b39 - 32*
                       m.b23*m.b32*m.b40 - 448*m.b23*m.b33*m.b34 - 384*m.b23*m.b33*m.b35 - 288*m.b23*m.b33*m.b36 - 192*
                       m.b23*m.b33*m.b37 - 96*m.b23*m.b33*m.b38 - 64*m.b23*m.b33*m.b39 - 32*m.b23*m.b33*m.b40 - 384*
                       m.b23*m.b34*m.b35 - 320*m.b23*m.b34*m.b36 - 224*m.b23*m.b34*m.b37 - 128*m.b23*m.b34*m.b38 - 64*
                       m.b23*m.b34*m.b39 - 32*m.b23*m.b34*m.b40 - 320*m.b23*m.b35*m.b36 - 256*m.b23*m.b35*m.b37 - 160*
                       m.b23*m.b35*m.b38 - 64*m.b23*m.b35*m.b39 - 32*m.b23*m.b35*m.b40 - 256*m.b23*m.b36*m.b37 - 192*
                       m.b23*m.b36*m.b38 - 96*m.b23*m.b36*m.b39 - 32*m.b23*m.b36*m.b40 - 192*m.b23*m.b37*m.b38 - 128*
                       m.b23*m.b37*m.b39 - 32*m.b23*m.b37*m.b40 - 128*m.b23*m.b38*m.b39 - 64*m.b23*m.b38*m.b40 - 64*
                       m.b23*m.b39*m.b40 - 928*m.b24*m.b25*m.b26 - 1312*m.b24*m.b25*m.b27 - 1216*m.b24*m.b25*m.b28 - 
                       1088*m.b24*m.b25*m.b29 - 960*m.b24*m.b25*m.b30 - 832*m.b24*m.b25*m.b31 - 704*m.b24*m.b25*m.b32 - 
                       576*m.b24*m.b25*m.b33 - 448*m.b24*m.b25*m.b34 - 352*m.b24*m.b25*m.b35 - 288*m.b24*m.b25*m.b36 - 
                       224*m.b24*m.b25*m.b37 - 160*m.b24*m.b25*m.b38 - 96*m.b24*m.b25*m.b39 - 32*m.b24*m.b25*m.b40 - 
                       1280*m.b24*m.b26*m.b27 - 768*m.b24*m.b26*m.b28 - 1088*m.b24*m.b26*m.b29 - 960*m.b24*m.b26*m.b30
                        - 832*m.b24*m.b26*m.b31 - 704*m.b24*m.b26*m.b32 - 576*m.b24*m.b26*m.b33 - 448*m.b24*m.b26*m.b34
                        - 320*m.b24*m.b26*m.b35 - 256*m.b24*m.b26*m.b36 - 192*m.b24*m.b26*m.b37 - 128*m.b24*m.b26*m.b38
                        - 64*m.b24*m.b26*m.b39 - 32*m.b24*m.b26*m.b40 - 1152*m.b24*m.b27*m.b28 - 1056*m.b24*m.b27*m.b29
                        - 608*m.b24*m.b27*m.b30 - 832*m.b24*m.b27*m.b31 - 704*m.b24*m.b27*m.b32 - 576*m.b24*m.b27*m.b33
                        - 448*m.b24*m.b27*m.b34 - 320*m.b24*m.b27*m.b35 - 224*m.b24*m.b27*m.b36 - 160*m.b24*m.b27*m.b37
                        - 96*m.b24*m.b27*m.b38 - 64*m.b24*m.b27*m.b39 - 32*m.b24*m.b27*m.b40 - 1024*m.b24*m.b28*m.b29 - 
                       928*m.b24*m.b28*m.b30 - 832*m.b24*m.b28*m.b31 - 416*m.b24*m.b28*m.b32 - 576*m.b24*m.b28*m.b33 - 
                       448*m.b24*m.b28*m.b34 - 320*m.b24*m.b28*m.b35 - 192*m.b24*m.b28*m.b36 - 128*m.b24*m.b28*m.b37 - 
                       96*m.b24*m.b28*m.b38 - 64*m.b24*m.b28*m.b39 - 32*m.b24*m.b28*m.b40 - 896*m.b24*m.b29*m.b30 - 800*
                       m.b24*m.b29*m.b31 - 704*m.b24*m.b29*m.b32 - 576*m.b24*m.b29*m.b33 - 224*m.b24*m.b29*m.b34 - 320*
                       m.b24*m.b29*m.b35 - 192*m.b24*m.b29*m.b36 - 128*m.b24*m.b29*m.b37 - 96*m.b24*m.b29*m.b38 - 64*
                       m.b24*m.b29*m.b39 - 32*m.b24*m.b29*m.b40 - 768*m.b24*m.b30*m.b31 - 672*m.b24*m.b30*m.b32 - 576*
                       m.b24*m.b30*m.b33 - 448*m.b24*m.b30*m.b34 - 320*m.b24*m.b30*m.b35 - 64*m.b24*m.b30*m.b36 - 128*
                       m.b24*m.b30*m.b37 - 96*m.b24*m.b30*m.b38 - 64*m.b24*m.b30*m.b39 - 32*m.b24*m.b30*m.b40 - 640*
                       m.b24*m.b31*m.b32 - 544*m.b24*m.b31*m.b33 - 448*m.b24*m.b31*m.b34 - 352*m.b24*m.b31*m.b35 - 256*
                       m.b24*m.b31*m.b36 - 160*m.b24*m.b31*m.b37 - 64*m.b24*m.b31*m.b39 - 32*m.b24*m.b31*m.b40 - 512*
                       m.b24*m.b32*m.b33 - 448*m.b24*m.b32*m.b34 - 384*m.b24*m.b32*m.b35 - 288*m.b24*m.b32*m.b36 - 192*
                       m.b24*m.b32*m.b37 - 96*m.b24*m.b32*m.b38 - 64*m.b24*m.b32*m.b39 - 448*m.b24*m.b33*m.b34 - 384*
                       m.b24*m.b33*m.b35 - 320*m.b24*m.b33*m.b36 - 224*m.b24*m.b33*m.b37 - 128*m.b24*m.b33*m.b38 - 64*
                       m.b24*m.b33*m.b39 - 32*m.b24*m.b33*m.b40 - 384*m.b24*m.b34*m.b35 - 320*m.b24*m.b34*m.b36 - 256*
                       m.b24*m.b34*m.b37 - 160*m.b24*m.b34*m.b38 - 64*m.b24*m.b34*m.b39 - 32*m.b24*m.b34*m.b40 - 320*
                       m.b24*m.b35*m.b36 - 256*m.b24*m.b35*m.b37 - 192*m.b24*m.b35*m.b38 - 96*m.b24*m.b35*m.b39 - 32*
                       m.b24*m.b35*m.b40 - 256*m.b24*m.b36*m.b37 - 192*m.b24*m.b36*m.b38 - 128*m.b24*m.b36*m.b39 - 32*
                       m.b24*m.b36*m.b40 - 192*m.b24*m.b37*m.b38 - 128*m.b24*m.b37*m.b39 - 64*m.b24*m.b37*m.b40 - 128*
                       m.b24*m.b38*m.b39 - 64*m.b24*m.b38*m.b40 - 64*m.b24*m.b39*m.b40 - 864*m.b25*m.b26*m.b27 - 1216*
                       m.b25*m.b26*m.b28 - 1120*m.b25*m.b26*m.b29 - 1024*m.b25*m.b26*m.b30 - 896*m.b25*m.b26*m.b31 - 768
                       *m.b25*m.b26*m.b32 - 640*m.b25*m.b26*m.b33 - 512*m.b25*m.b26*m.b34 - 384*m.b25*m.b26*m.b35 - 288*
                       m.b25*m.b26*m.b36 - 224*m.b25*m.b26*m.b37 - 160*m.b25*m.b26*m.b38 - 96*m.b25*m.b26*m.b39 - 32*
                       m.b25*m.b26*m.b40 - 1184*m.b25*m.b27*m.b28 - 704*m.b25*m.b27*m.b29 - 992*m.b25*m.b27*m.b30 - 896*
                       m.b25*m.b27*m.b31 - 768*m.b25*m.b27*m.b32 - 640*m.b25*m.b27*m.b33 - 512*m.b25*m.b27*m.b34 - 384*
                       m.b25*m.b27*m.b35 - 256*m.b25*m.b27*m.b36 - 192*m.b25*m.b27*m.b37 - 128*m.b25*m.b27*m.b38 - 64*
                       m.b25*m.b27*m.b39 - 32*m.b25*m.b27*m.b40 - 1056*m.b25*m.b28*m.b29 - 960*m.b25*m.b28*m.b30 - 544*
                       m.b25*m.b28*m.b31 - 768*m.b25*m.b28*m.b32 - 640*m.b25*m.b28*m.b33 - 512*m.b25*m.b28*m.b34 - 384*
                       m.b25*m.b28*m.b35 - 256*m.b25*m.b28*m.b36 - 160*m.b25*m.b28*m.b37 - 96*m.b25*m.b28*m.b38 - 64*
                       m.b25*m.b28*m.b39 - 32*m.b25*m.b28*m.b40 - 928*m.b25*m.b29*m.b30 - 832*m.b25*m.b29*m.b31 - 736*
                       m.b25*m.b29*m.b32 - 384*m.b25*m.b29*m.b33 - 512*m.b25*m.b29*m.b34 - 384*m.b25*m.b29*m.b35 - 256*
                       m.b25*m.b29*m.b36 - 128*m.b25*m.b29*m.b37 - 96*m.b25*m.b29*m.b38 - 64*m.b25*m.b29*m.b39 - 32*
                       m.b25*m.b29*m.b40 - 800*m.b25*m.b30*m.b31 - 704*m.b25*m.b30*m.b32 - 608*m.b25*m.b30*m.b33 - 512*
                       m.b25*m.b30*m.b34 - 192*m.b25*m.b30*m.b35 - 256*m.b25*m.b30*m.b36 - 160*m.b25*m.b30*m.b37 - 96*
                       m.b25*m.b30*m.b38 - 64*m.b25*m.b30*m.b39 - 32*m.b25*m.b30*m.b40 - 672*m.b25*m.b31*m.b32 - 576*
                       m.b25*m.b31*m.b33 - 480*m.b25*m.b31*m.b34 - 384*m.b25*m.b31*m.b35 - 288*m.b25*m.b31*m.b36 - 64*
                       m.b25*m.b31*m.b37 - 96*m.b25*m.b31*m.b38 - 64*m.b25*m.b31*m.b39 - 32*m.b25*m.b31*m.b40 - 544*
                       m.b25*m.b32*m.b33 - 448*m.b25*m.b32*m.b34 - 384*m.b25*m.b32*m.b35 - 320*m.b25*m.b32*m.b36 - 224*
                       m.b25*m.b32*m.b37 - 128*m.b25*m.b32*m.b38 - 32*m.b25*m.b32*m.b40 - 448*m.b25*m.b33*m.b34 - 384*
                       m.b25*m.b33*m.b35 - 320*m.b25*m.b33*m.b36 - 256*m.b25*m.b33*m.b37 - 160*m.b25*m.b33*m.b38 - 64*
                       m.b25*m.b33*m.b39 - 32*m.b25*m.b33*m.b40 - 384*m.b25*m.b34*m.b35 - 320*m.b25*m.b34*m.b36 - 256*
                       m.b25*m.b34*m.b37 - 192*m.b25*m.b34*m.b38 - 96*m.b25*m.b34*m.b39 - 32*m.b25*m.b34*m.b40 - 320*
                       m.b25*m.b35*m.b36 - 256*m.b25*m.b35*m.b37 - 192*m.b25*m.b35*m.b38 - 128*m.b25*m.b35*m.b39 - 32*
                       m.b25*m.b35*m.b40 - 256*m.b25*m.b36*m.b37 - 192*m.b25*m.b36*m.b38 - 128*m.b25*m.b36*m.b39 - 64*
                       m.b25*m.b36*m.b40 - 192*m.b25*m.b37*m.b38 - 128*m.b25*m.b37*m.b39 - 64*m.b25*m.b37*m.b40 - 128*
                       m.b25*m.b38*m.b39 - 64*m.b25*m.b38*m.b40 - 64*m.b25*m.b39*m.b40 - 800*m.b26*m.b27*m.b28 - 1120*
                       m.b26*m.b27*m.b29 - 1024*m.b26*m.b27*m.b30 - 928*m.b26*m.b27*m.b31 - 832*m.b26*m.b27*m.b32 - 704*
                       m.b26*m.b27*m.b33 - 576*m.b26*m.b27*m.b34 - 448*m.b26*m.b27*m.b35 - 320*m.b26*m.b27*m.b36 - 224*
                       m.b26*m.b27*m.b37 - 160*m.b26*m.b27*m.b38 - 96*m.b26*m.b27*m.b39 - 32*m.b26*m.b27*m.b40 - 1088*
                       m.b26*m.b28*m.b29 - 640*m.b26*m.b28*m.b30 - 896*m.b26*m.b28*m.b31 - 800*m.b26*m.b28*m.b32 - 704*
                       m.b26*m.b28*m.b33 - 576*m.b26*m.b28*m.b34 - 448*m.b26*m.b28*m.b35 - 320*m.b26*m.b28*m.b36 - 192*
                       m.b26*m.b28*m.b37 - 128*m.b26*m.b28*m.b38 - 64*m.b26*m.b28*m.b39 - 32*m.b26*m.b28*m.b40 - 960*
                       m.b26*m.b29*m.b30 - 864*m.b26*m.b29*m.b31 - 480*m.b26*m.b29*m.b32 - 672*m.b26*m.b29*m.b33 - 576*
                       m.b26*m.b29*m.b34 - 448*m.b26*m.b29*m.b35 - 320*m.b26*m.b29*m.b36 - 192*m.b26*m.b29*m.b37 - 96*
                       m.b26*m.b29*m.b38 - 64*m.b26*m.b29*m.b39 - 32*m.b26*m.b29*m.b40 - 832*m.b26*m.b30*m.b31 - 736*
                       m.b26*m.b30*m.b32 - 640*m.b26*m.b30*m.b33 - 320*m.b26*m.b30*m.b34 - 448*m.b26*m.b30*m.b35 - 320*
                       m.b26*m.b30*m.b36 - 192*m.b26*m.b30*m.b37 - 96*m.b26*m.b30*m.b38 - 64*m.b26*m.b30*m.b39 - 32*
                       m.b26*m.b30*m.b40 - 704*m.b26*m.b31*m.b32 - 608*m.b26*m.b31*m.b33 - 512*m.b26*m.b31*m.b34 - 416*
                       m.b26*m.b31*m.b35 - 160*m.b26*m.b31*m.b36 - 224*m.b26*m.b31*m.b37 - 128*m.b26*m.b31*m.b38 - 64*
                       m.b26*m.b31*m.b39 - 32*m.b26*m.b31*m.b40 - 576*m.b26*m.b32*m.b33 - 480*m.b26*m.b32*m.b34 - 384*
                       m.b26*m.b32*m.b35 - 320*m.b26*m.b32*m.b36 - 256*m.b26*m.b32*m.b37 - 64*m.b26*m.b32*m.b38 - 64*
                       m.b26*m.b32*m.b39 - 32*m.b26*m.b32*m.b40 - 448*m.b26*m.b33*m.b34 - 384*m.b26*m.b33*m.b35 - 320*
                       m.b26*m.b33*m.b36 - 256*m.b26*m.b33*m.b37 - 192*m.b26*m.b33*m.b38 - 96*m.b26*m.b33*m.b39 - 384*
                       m.b26*m.b34*m.b35 - 320*m.b26*m.b34*m.b36 - 256*m.b26*m.b34*m.b37 - 192*m.b26*m.b34*m.b38 - 128*
                       m.b26*m.b34*m.b39 - 32*m.b26*m.b34*m.b40 - 320*m.b26*m.b35*m.b36 - 256*m.b26*m.b35*m.b37 - 192*
                       m.b26*m.b35*m.b38 - 128*m.b26*m.b35*m.b39 - 64*m.b26*m.b35*m.b40 - 256*m.b26*m.b36*m.b37 - 192*
                       m.b26*m.b36*m.b38 - 128*m.b26*m.b36*m.b39 - 64*m.b26*m.b36*m.b40 - 192*m.b26*m.b37*m.b38 - 128*
                       m.b26*m.b37*m.b39 - 64*m.b26*m.b37*m.b40 - 128*m.b26*m.b38*m.b39 - 64*m.b26*m.b38*m.b40 - 64*
                       m.b26*m.b39*m.b40 - 736*m.b27*m.b28*m.b29 - 1024*m.b27*m.b28*m.b30 - 928*m.b27*m.b28*m.b31 - 832*
                       m.b27*m.b28*m.b32 - 736*m.b27*m.b28*m.b33 - 640*m.b27*m.b28*m.b34 - 512*m.b27*m.b28*m.b35 - 384*
                       m.b27*m.b28*m.b36 - 256*m.b27*m.b28*m.b37 - 160*m.b27*m.b28*m.b38 - 96*m.b27*m.b28*m.b39 - 32*
                       m.b27*m.b28*m.b40 - 992*m.b27*m.b29*m.b30 - 576*m.b27*m.b29*m.b31 - 800*m.b27*m.b29*m.b32 - 704*
                       m.b27*m.b29*m.b33 - 608*m.b27*m.b29*m.b34 - 512*m.b27*m.b29*m.b35 - 384*m.b27*m.b29*m.b36 - 256*
                       m.b27*m.b29*m.b37 - 128*m.b27*m.b29*m.b38 - 64*m.b27*m.b29*m.b39 - 32*m.b27*m.b29*m.b40 - 864*
                       m.b27*m.b30*m.b31 - 768*m.b27*m.b30*m.b32 - 416*m.b27*m.b30*m.b33 - 576*m.b27*m.b30*m.b34 - 480*
                       m.b27*m.b30*m.b35 - 384*m.b27*m.b30*m.b36 - 256*m.b27*m.b30*m.b37 - 128*m.b27*m.b30*m.b38 - 64*
                       m.b27*m.b30*m.b39 - 32*m.b27*m.b30*m.b40 - 736*m.b27*m.b31*m.b32 - 640*m.b27*m.b31*m.b33 - 544*
                       m.b27*m.b31*m.b34 - 256*m.b27*m.b31*m.b35 - 352*m.b27*m.b31*m.b36 - 256*m.b27*m.b31*m.b37 - 160*
                       m.b27*m.b31*m.b38 - 64*m.b27*m.b31*m.b39 - 32*m.b27*m.b31*m.b40 - 608*m.b27*m.b32*m.b33 - 512*
                       m.b27*m.b32*m.b34 - 416*m.b27*m.b32*m.b35 - 320*m.b27*m.b32*m.b36 - 128*m.b27*m.b32*m.b37 - 192*
                       m.b27*m.b32*m.b38 - 96*m.b27*m.b32*m.b39 - 32*m.b27*m.b32*m.b40 - 480*m.b27*m.b33*m.b34 - 384*
                       m.b27*m.b33*m.b35 - 320*m.b27*m.b33*m.b36 - 256*m.b27*m.b33*m.b37 - 192*m.b27*m.b33*m.b38 - 64*
                       m.b27*m.b33*m.b39 - 32*m.b27*m.b33*m.b40 - 384*m.b27*m.b34*m.b35 - 320*m.b27*m.b34*m.b36 - 256*
                       m.b27*m.b34*m.b37 - 192*m.b27*m.b34*m.b38 - 128*m.b27*m.b34*m.b39 - 64*m.b27*m.b34*m.b40 - 320*
                       m.b27*m.b35*m.b36 - 256*m.b27*m.b35*m.b37 - 192*m.b27*m.b35*m.b38 - 128*m.b27*m.b35*m.b39 - 64*
                       m.b27*m.b35*m.b40 - 256*m.b27*m.b36*m.b37 - 192*m.b27*m.b36*m.b38 - 128*m.b27*m.b36*m.b39 - 64*
                       m.b27*m.b36*m.b40 - 192*m.b27*m.b37*m.b38 - 128*m.b27*m.b37*m.b39 - 64*m.b27*m.b37*m.b40 - 128*
                       m.b27*m.b38*m.b39 - 64*m.b27*m.b38*m.b40 - 64*m.b27*m.b39*m.b40 - 672*m.b28*m.b29*m.b30 - 928*
                       m.b28*m.b29*m.b31 - 832*m.b28*m.b29*m.b32 - 736*m.b28*m.b29*m.b33 - 640*m.b28*m.b29*m.b34 - 544*
                       m.b28*m.b29*m.b35 - 448*m.b28*m.b29*m.b36 - 320*m.b28*m.b29*m.b37 - 192*m.b28*m.b29*m.b38 - 96*
                       m.b28*m.b29*m.b39 - 32*m.b28*m.b29*m.b40 - 896*m.b28*m.b30*m.b31 - 512*m.b28*m.b30*m.b32 - 704*
                       m.b28*m.b30*m.b33 - 608*m.b28*m.b30*m.b34 - 512*m.b28*m.b30*m.b35 - 416*m.b28*m.b30*m.b36 - 320*
                       m.b28*m.b30*m.b37 - 192*m.b28*m.b30*m.b38 - 64*m.b28*m.b30*m.b39 - 32*m.b28*m.b30*m.b40 - 768*
                       m.b28*m.b31*m.b32 - 672*m.b28*m.b31*m.b33 - 352*m.b28*m.b31*m.b34 - 480*m.b28*m.b31*m.b35 - 384*
                       m.b28*m.b31*m.b36 - 288*m.b28*m.b31*m.b37 - 192*m.b28*m.b31*m.b38 - 96*m.b28*m.b31*m.b39 - 32*
                       m.b28*m.b31*m.b40 - 640*m.b28*m.b32*m.b33 - 544*m.b28*m.b32*m.b34 - 448*m.b28*m.b32*m.b35 - 192*
                       m.b28*m.b32*m.b36 - 256*m.b28*m.b32*m.b37 - 192*m.b28*m.b32*m.b38 - 128*m.b28*m.b32*m.b39 - 32*
                       m.b28*m.b32*m.b40 - 512*m.b28*m.b33*m.b34 - 416*m.b28*m.b33*m.b35 - 320*m.b28*m.b33*m.b36 - 256*
                       m.b28*m.b33*m.b37 - 96*m.b28*m.b33*m.b38 - 128*m.b28*m.b33*m.b39 - 64*m.b28*m.b33*m.b40 - 384*
                       m.b28*m.b34*m.b35 - 320*m.b28*m.b34*m.b36 - 256*m.b28*m.b34*m.b37 - 192*m.b28*m.b34*m.b38 - 128*
                       m.b28*m.b34*m.b39 - 32*m.b28*m.b34*m.b40 - 320*m.b28*m.b35*m.b36 - 256*m.b28*m.b35*m.b37 - 192*
                       m.b28*m.b35*m.b38 - 128*m.b28*m.b35*m.b39 - 64*m.b28*m.b35*m.b40 - 256*m.b28*m.b36*m.b37 - 192*
                       m.b28*m.b36*m.b38 - 128*m.b28*m.b36*m.b39 - 64*m.b28*m.b36*m.b40 - 192*m.b28*m.b37*m.b38 - 128*
                       m.b28*m.b37*m.b39 - 64*m.b28*m.b37*m.b40 - 128*m.b28*m.b38*m.b39 - 64*m.b28*m.b38*m.b40 - 64*
                       m.b28*m.b39*m.b40 - 608*m.b29*m.b30*m.b31 - 832*m.b29*m.b30*m.b32 - 736*m.b29*m.b30*m.b33 - 640*
                       m.b29*m.b30*m.b34 - 544*m.b29*m.b30*m.b35 - 448*m.b29*m.b30*m.b36 - 352*m.b29*m.b30*m.b37 - 256*
                       m.b29*m.b30*m.b38 - 128*m.b29*m.b30*m.b39 - 32*m.b29*m.b30*m.b40 - 800*m.b29*m.b31*m.b32 - 448*
                       m.b29*m.b31*m.b33 - 608*m.b29*m.b31*m.b34 - 512*m.b29*m.b31*m.b35 - 416*m.b29*m.b31*m.b36 - 320*
                       m.b29*m.b31*m.b37 - 224*m.b29*m.b31*m.b38 - 128*m.b29*m.b31*m.b39 - 32*m.b29*m.b31*m.b40 - 672*
                       m.b29*m.b32*m.b33 - 576*m.b29*m.b32*m.b34 - 288*m.b29*m.b32*m.b35 - 384*m.b29*m.b32*m.b36 - 288*
                       m.b29*m.b32*m.b37 - 192*m.b29*m.b32*m.b38 - 128*m.b29*m.b32*m.b39 - 64*m.b29*m.b32*m.b40 - 544*
                       m.b29*m.b33*m.b34 - 448*m.b29*m.b33*m.b35 - 352*m.b29*m.b33*m.b36 - 128*m.b29*m.b33*m.b37 - 192*
                       m.b29*m.b33*m.b38 - 128*m.b29*m.b33*m.b39 - 64*m.b29*m.b33*m.b40 - 416*m.b29*m.b34*m.b35 - 320*
                       m.b29*m.b34*m.b36 - 256*m.b29*m.b34*m.b37 - 192*m.b29*m.b34*m.b38 - 64*m.b29*m.b34*m.b39 - 64*
                       m.b29*m.b34*m.b40 - 320*m.b29*m.b35*m.b36 - 256*m.b29*m.b35*m.b37 - 192*m.b29*m.b35*m.b38 - 128*
                       m.b29*m.b35*m.b39 - 64*m.b29*m.b35*m.b40 - 256*m.b29*m.b36*m.b37 - 192*m.b29*m.b36*m.b38 - 128*
                       m.b29*m.b36*m.b39 - 64*m.b29*m.b36*m.b40 - 192*m.b29*m.b37*m.b38 - 128*m.b29*m.b37*m.b39 - 64*
                       m.b29*m.b37*m.b40 - 128*m.b29*m.b38*m.b39 - 64*m.b29*m.b38*m.b40 - 64*m.b29*m.b39*m.b40 - 544*
                       m.b30*m.b31*m.b32 - 736*m.b30*m.b31*m.b33 - 640*m.b30*m.b31*m.b34 - 544*m.b30*m.b31*m.b35 - 448*
                       m.b30*m.b31*m.b36 - 352*m.b30*m.b31*m.b37 - 256*m.b30*m.b31*m.b38 - 160*m.b30*m.b31*m.b39 - 64*
                       m.b30*m.b31*m.b40 - 704*m.b30*m.b32*m.b33 - 384*m.b30*m.b32*m.b34 - 512*m.b30*m.b32*m.b35 - 416*
                       m.b30*m.b32*m.b36 - 320*m.b30*m.b32*m.b37 - 224*m.b30*m.b32*m.b38 - 128*m.b30*m.b32*m.b39 - 64*
                       m.b30*m.b32*m.b40 - 576*m.b30*m.b33*m.b34 - 480*m.b30*m.b33*m.b35 - 224*m.b30*m.b33*m.b36 - 288*
                       m.b30*m.b33*m.b37 - 192*m.b30*m.b33*m.b38 - 128*m.b30*m.b33*m.b39 - 64*m.b30*m.b33*m.b40 - 448*
                       m.b30*m.b34*m.b35 - 352*m.b30*m.b34*m.b36 - 256*m.b30*m.b34*m.b37 - 96*m.b30*m.b34*m.b38 - 128*
                       m.b30*m.b34*m.b39 - 64*m.b30*m.b34*m.b40 - 320*m.b30*m.b35*m.b36 - 256*m.b30*m.b35*m.b37 - 192*
                       m.b30*m.b35*m.b38 - 128*m.b30*m.b35*m.b39 - 32*m.b30*m.b35*m.b40 - 256*m.b30*m.b36*m.b37 - 192*
                       m.b30*m.b36*m.b38 - 128*m.b30*m.b36*m.b39 - 64*m.b30*m.b36*m.b40 - 192*m.b30*m.b37*m.b38 - 128*
                       m.b30*m.b37*m.b39 - 64*m.b30*m.b37*m.b40 - 128*m.b30*m.b38*m.b39 - 64*m.b30*m.b38*m.b40 - 64*
                       m.b30*m.b39*m.b40 - 480*m.b31*m.b32*m.b33 - 640*m.b31*m.b32*m.b34 - 544*m.b31*m.b32*m.b35 - 448*
                       m.b31*m.b32*m.b36 - 352*m.b31*m.b32*m.b37 - 256*m.b31*m.b32*m.b38 - 160*m.b31*m.b32*m.b39 - 64*
                       m.b31*m.b32*m.b40 - 608*m.b31*m.b33*m.b34 - 320*m.b31*m.b33*m.b35 - 416*m.b31*m.b33*m.b36 - 320*
                       m.b31*m.b33*m.b37 - 224*m.b31*m.b33*m.b38 - 128*m.b31*m.b33*m.b39 - 64*m.b31*m.b33*m.b40 - 480*
                       m.b31*m.b34*m.b35 - 384*m.b31*m.b34*m.b36 - 160*m.b31*m.b34*m.b37 - 192*m.b31*m.b34*m.b38 - 128*
                       m.b31*m.b34*m.b39 - 64*m.b31*m.b34*m.b40 - 352*m.b31*m.b35*m.b36 - 256*m.b31*m.b35*m.b37 - 192*
                       m.b31*m.b35*m.b38 - 64*m.b31*m.b35*m.b39 - 64*m.b31*m.b35*m.b40 - 256*m.b31*m.b36*m.b37 - 192*
                       m.b31*m.b36*m.b38 - 128*m.b31*m.b36*m.b39 - 64*m.b31*m.b36*m.b40 - 192*m.b31*m.b37*m.b38 - 128*
                       m.b31*m.b37*m.b39 - 64*m.b31*m.b37*m.b40 - 128*m.b31*m.b38*m.b39 - 64*m.b31*m.b38*m.b40 - 64*
                       m.b31*m.b39*m.b40 - 416*m.b32*m.b33*m.b34 - 544*m.b32*m.b33*m.b35 - 448*m.b32*m.b33*m.b36 - 352*
                       m.b32*m.b33*m.b37 - 256*m.b32*m.b33*m.b38 - 160*m.b32*m.b33*m.b39 - 64*m.b32*m.b33*m.b40 - 512*
                       m.b32*m.b34*m.b35 - 256*m.b32*m.b34*m.b36 - 320*m.b32*m.b34*m.b37 - 224*m.b32*m.b34*m.b38 - 128*
                       m.b32*m.b34*m.b39 - 64*m.b32*m.b34*m.b40 - 384*m.b32*m.b35*m.b36 - 288*m.b32*m.b35*m.b37 - 96*
                       m.b32*m.b35*m.b38 - 128*m.b32*m.b35*m.b39 - 64*m.b32*m.b35*m.b40 - 256*m.b32*m.b36*m.b37 - 192*
                       m.b32*m.b36*m.b38 - 128*m.b32*m.b36*m.b39 - 32*m.b32*m.b36*m.b40 - 192*m.b32*m.b37*m.b38 - 128*
                       m.b32*m.b37*m.b39 - 64*m.b32*m.b37*m.b40 - 128*m.b32*m.b38*m.b39 - 64*m.b32*m.b38*m.b40 - 64*
                       m.b32*m.b39*m.b40 - 352*m.b33*m.b34*m.b35 - 448*m.b33*m.b34*m.b36 - 352*m.b33*m.b34*m.b37 - 256*
                       m.b33*m.b34*m.b38 - 160*m.b33*m.b34*m.b39 - 64*m.b33*m.b34*m.b40 - 416*m.b33*m.b35*m.b36 - 192*
                       m.b33*m.b35*m.b37 - 224*m.b33*m.b35*m.b38 - 128*m.b33*m.b35*m.b39 - 64*m.b33*m.b35*m.b40 - 288*
                       m.b33*m.b36*m.b37 - 192*m.b33*m.b36*m.b38 - 64*m.b33*m.b36*m.b39 - 64*m.b33*m.b36*m.b40 - 192*
                       m.b33*m.b37*m.b38 - 128*m.b33*m.b37*m.b39 - 64*m.b33*m.b37*m.b40 - 128*m.b33*m.b38*m.b39 - 64*
                       m.b33*m.b38*m.b40 - 64*m.b33*m.b39*m.b40 - 288*m.b34*m.b35*m.b36 - 352*m.b34*m.b35*m.b37 - 256*
                       m.b34*m.b35*m.b38 - 160*m.b34*m.b35*m.b39 - 64*m.b34*m.b35*m.b40 - 320*m.b34*m.b36*m.b37 - 128*
                       m.b34*m.b36*m.b38 - 128*m.b34*m.b36*m.b39 - 64*m.b34*m.b36*m.b40 - 192*m.b34*m.b37*m.b38 - 128*
                       m.b34*m.b37*m.b39 - 32*m.b34*m.b37*m.b40 - 128*m.b34*m.b38*m.b39 - 64*m.b34*m.b38*m.b40 - 64*
                       m.b34*m.b39*m.b40 - 224*m.b35*m.b36*m.b37 - 256*m.b35*m.b36*m.b38 - 160*m.b35*m.b36*m.b39 - 64*
                       m.b35*m.b36*m.b40 - 224*m.b35*m.b37*m.b38 - 64*m.b35*m.b37*m.b39 - 64*m.b35*m.b37*m.b40 - 128*
                       m.b35*m.b38*m.b39 - 64*m.b35*m.b38*m.b40 - 64*m.b35*m.b39*m.b40 - 160*m.b36*m.b37*m.b38 - 160*
                       m.b36*m.b37*m.b39 - 64*m.b36*m.b37*m.b40 - 128*m.b36*m.b38*m.b39 - 32*m.b36*m.b38*m.b40 - 64*
                       m.b36*m.b39*m.b40 - 96*m.b37*m.b38*m.b39 - 64*m.b37*m.b38*m.b40 - 64*m.b37*m.b39*m.b40 - 32*m.b38
                       *m.b39*m.b40 + 272*m.b1*m.b2 + 264*m.b1*m.b3 + 256*m.b1*m.b4 + 248*m.b1*m.b5 + 240*m.b1*m.b6 + 
                       232*m.b1*m.b7 + 224*m.b1*m.b8 + 216*m.b1*m.b9 + 208*m.b1*m.b10 + 216*m.b1*m.b11 + 208*m.b1*m.b12
                        + 200*m.b1*m.b13 + 192*m.b1*m.b14 + 184*m.b1*m.b15 + 176*m.b1*m.b16 + 168*m.b1*m.b17 + 160*m.b1*
                       m.b18 + 152*m.b1*m.b19 + 144*m.b1*m.b20 + 544*m.b2*m.b3 + 544*m.b2*m.b4 + 528*m.b2*m.b5 + 512*
                       m.b2*m.b6 + 496*m.b2*m.b7 + 480*m.b2*m.b8 + 464*m.b2*m.b9 + 448*m.b2*m.b10 + 432*m.b2*m.b11 + 448
                       *m.b2*m.b12 + 432*m.b2*m.b13 + 416*m.b2*m.b14 + 400*m.b2*m.b15 + 384*m.b2*m.b16 + 368*m.b2*m.b17
                        + 352*m.b2*m.b18 + 336*m.b2*m.b19 + 304*m.b2*m.b20 + 144*m.b2*m.b21 + 832*m.b3*m.b4 + 824*m.b3*
                       m.b5 + 816*m.b3*m.b6 + 792*m.b3*m.b7 + 768*m.b3*m.b8 + 744*m.b3*m.b9 + 720*m.b3*m.b10 + 696*m.b3*
                       m.b11 + 688*m.b3*m.b12 + 696*m.b3*m.b13 + 672*m.b3*m.b14 + 648*m.b3*m.b15 + 624*m.b3*m.b16 + 600*
                       m.b3*m.b17 + 576*m.b3*m.b18 + 536*m.b3*m.b19 + 496*m.b3*m.b20 + 304*m.b3*m.b21 + 144*m.b3*m.b22
                        + 1136*m.b4*m.b5 + 1120*m.b4*m.b6 + 1104*m.b4*m.b7 + 1088*m.b4*m.b8 + 1056*m.b4*m.b9 + 1024*m.b4
                       *m.b10 + 992*m.b4*m.b11 + 960*m.b4*m.b12 + 960*m.b4*m.b13 + 960*m.b4*m.b14 + 928*m.b4*m.b15 + 896
                       *m.b4*m.b16 + 864*m.b4*m.b17 + 816*m.b4*m.b18 + 768*m.b4*m.b19 + 704*m.b4*m.b20 + 496*m.b4*m.b21
                        + 304*m.b4*m.b22 + 144*m.b4*m.b23 + 1456*m.b5*m.b6 + 1432*m.b5*m.b7 + 1408*m.b5*m.b8 + 1384*m.b5
                       *m.b9 + 1360*m.b5*m.b10 + 1320*m.b5*m.b11 + 1280*m.b5*m.b12 + 1256*m.b5*m.b13 + 1248*m.b5*m.b14
                        + 1240*m.b5*m.b15 + 1200*m.b5*m.b16 + 1144*m.b5*m.b17 + 1088*m.b5*m.b18 + 1016*m.b5*m.b19 + 944*
                       m.b5*m.b20 + 704*m.b5*m.b21 + 496*m.b5*m.b22 + 304*m.b5*m.b23 + 144*m.b5*m.b24 + 1792*m.b6*m.b7
                        + 1760*m.b6*m.b8 + 1728*m.b6*m.b9 + 1696*m.b6*m.b10 + 1664*m.b6*m.b11 + 1632*m.b6*m.b12 + 1584*
                       m.b6*m.b13 + 1568*m.b6*m.b14 + 1552*m.b6*m.b15 + 1520*m.b6*m.b16 + 1456*m.b6*m.b17 + 1376*m.b6*
                       m.b18 + 1296*m.b6*m.b19 + 1200*m.b6*m.b20 + 944*m.b6*m.b21 + 704*m.b6*m.b22 + 496*m.b6*m.b23 + 
                       304*m.b6*m.b24 + 144*m.b6*m.b25 + 2144*m.b7*m.b8 + 2104*m.b7*m.b9 + 2064*m.b7*m.b10 + 2024*m.b7*
                       m.b11 + 1984*m.b7*m.b12 + 1944*m.b7*m.b13 + 1920*m.b7*m.b14 + 1880*m.b7*m.b15 + 1840*m.b7*m.b16
                        + 1784*m.b7*m.b17 + 1696*m.b7*m.b18 + 1592*m.b7*m.b19 + 1488*m.b7*m.b20 + 1200*m.b7*m.b21 + 944*
                       m.b7*m.b22 + 704*m.b7*m.b23 + 496*m.b7*m.b24 + 304*m.b7*m.b25 + 144*m.b7*m.b26 + 2512*m.b8*m.b9
                        + 2464*m.b8*m.b10 + 2416*m.b8*m.b11 + 2368*m.b8*m.b12 + 2320*m.b8*m.b13 + 2256*m.b8*m.b14 + 2224
                       *m.b8*m.b15 + 2176*m.b8*m.b16 + 2112*m.b8*m.b17 + 2032*m.b8*m.b18 + 1920*m.b8*m.b19 + 1792*m.b8*
                       m.b20 + 1488*m.b8*m.b21 + 1200*m.b8*m.b22 + 944*m.b8*m.b23 + 704*m.b8*m.b24 + 496*m.b8*m.b25 + 
                       304*m.b8*m.b26 + 144*m.b8*m.b27 + 2896*m.b9*m.b10 + 2840*m.b9*m.b11 + 2784*m.b9*m.b12 + 2712*m.b9
                       *m.b13 + 2640*m.b9*m.b14 + 2568*m.b9*m.b15 + 2512*m.b9*m.b16 + 2440*m.b9*m.b17 + 2368*m.b9*m.b18
                        + 2264*m.b9*m.b19 + 2128*m.b9*m.b20 + 1792*m.b9*m.b21 + 1488*m.b9*m.b22 + 1200*m.b9*m.b23 + 944*
                       m.b9*m.b24 + 704*m.b9*m.b25 + 496*m.b9*m.b26 + 304*m.b9*m.b27 + 144*m.b9*m.b28 + 3296*m.b10*m.b11
                        + 3216*m.b10*m.b12 + 3136*m.b10*m.b13 + 3040*m.b10*m.b14 + 2944*m.b10*m.b15 + 2864*m.b10*m.b16
                        + 2784*m.b10*m.b17 + 2688*m.b10*m.b18 + 2592*m.b10*m.b19 + 2480*m.b10*m.b20 + 2128*m.b10*m.b21
                        + 1792*m.b10*m.b22 + 1488*m.b10*m.b23 + 1200*m.b10*m.b24 + 944*m.b10*m.b25 + 704*m.b10*m.b26 + 
                       496*m.b10*m.b27 + 304*m.b10*m.b28 + 144*m.b10*m.b29 + 3680*m.b11*m.b12 + 3576*m.b11*m.b13 + 3472*
                       m.b11*m.b14 + 3352*m.b11*m.b15 + 3248*m.b11*m.b16 + 3144*m.b11*m.b17 + 3040*m.b11*m.b18 + 2920*
                       m.b11*m.b19 + 2800*m.b11*m.b20 + 2480*m.b11*m.b21 + 2128*m.b11*m.b22 + 1792*m.b11*m.b23 + 1488*
                       m.b11*m.b24 + 1200*m.b11*m.b25 + 944*m.b11*m.b26 + 704*m.b11*m.b27 + 496*m.b11*m.b28 + 304*m.b11*
                       m.b29 + 144*m.b11*m.b30 + 4048*m.b12*m.b13 + 3920*m.b12*m.b14 + 3792*m.b12*m.b15 + 3648*m.b12*
                       m.b16 + 3536*m.b12*m.b17 + 3408*m.b12*m.b18 + 3280*m.b12*m.b19 + 3136*m.b12*m.b20 + 2800*m.b12*
                       m.b21 + 2480*m.b12*m.b22 + 2128*m.b12*m.b23 + 1792*m.b12*m.b24 + 1488*m.b12*m.b25 + 1200*m.b12*
                       m.b26 + 944*m.b12*m.b27 + 704*m.b12*m.b28 + 496*m.b12*m.b29 + 304*m.b12*m.b30 + 144*m.b12*m.b31
                        + 4400*m.b13*m.b14 + 4248*m.b13*m.b15 + 4096*m.b13*m.b16 + 3944*m.b13*m.b17 + 3808*m.b13*m.b18
                        + 3656*m.b13*m.b19 + 3504*m.b13*m.b20 + 3136*m.b13*m.b21 + 2800*m.b13*m.b22 + 2480*m.b13*m.b23
                        + 2128*m.b13*m.b24 + 1792*m.b13*m.b25 + 1488*m.b13*m.b26 + 1200*m.b13*m.b27 + 944*m.b13*m.b28 + 
                       704*m.b13*m.b29 + 496*m.b13*m.b30 + 304*m.b13*m.b31 + 144*m.b13*m.b32 + 4736*m.b14*m.b15 + 4560*
                       m.b14*m.b16 + 4384*m.b14*m.b17 + 4224*m.b14*m.b18 + 4064*m.b14*m.b19 + 3888*m.b14*m.b20 + 3504*
                       m.b14*m.b21 + 3136*m.b14*m.b22 + 2800*m.b14*m.b23 + 2480*m.b14*m.b24 + 2128*m.b14*m.b25 + 1792*
                       m.b14*m.b26 + 1488*m.b14*m.b27 + 1200*m.b14*m.b28 + 944*m.b14*m.b29 + 704*m.b14*m.b30 + 496*m.b14
                       *m.b31 + 304*m.b14*m.b32 + 144*m.b14*m.b33 + 5056*m.b15*m.b16 + 4856*m.b15*m.b17 + 4672*m.b15*
                       m.b18 + 4488*m.b15*m.b19 + 4304*m.b15*m.b20 + 3888*m.b15*m.b21 + 3504*m.b15*m.b22 + 3136*m.b15*
                       m.b23 + 2800*m.b15*m.b24 + 2480*m.b15*m.b25 + 2128*m.b15*m.b26 + 1792*m.b15*m.b27 + 1488*m.b15*
                       m.b28 + 1200*m.b15*m.b29 + 944*m.b15*m.b30 + 704*m.b15*m.b31 + 496*m.b15*m.b32 + 304*m.b15*m.b33
                        + 144*m.b15*m.b34 + 5360*m.b16*m.b17 + 5136*m.b16*m.b18 + 4944*m.b16*m.b19 + 4736*m.b16*m.b20 + 
                       4304*m.b16*m.b21 + 3888*m.b16*m.b22 + 3504*m.b16*m.b23 + 3136*m.b16*m.b24 + 2800*m.b16*m.b25 + 
                       2480*m.b16*m.b26 + 2128*m.b16*m.b27 + 1792*m.b16*m.b28 + 1488*m.b16*m.b29 + 1200*m.b16*m.b30 + 
                       944*m.b16*m.b31 + 704*m.b16*m.b32 + 496*m.b16*m.b33 + 304*m.b16*m.b34 + 144*m.b16*m.b35 + 5648*
                       m.b17*m.b18 + 5416*m.b17*m.b19 + 5200*m.b17*m.b20 + 4736*m.b17*m.b21 + 4304*m.b17*m.b22 + 3888*
                       m.b17*m.b23 + 3504*m.b17*m.b24 + 3136*m.b17*m.b25 + 2800*m.b17*m.b26 + 2480*m.b17*m.b27 + 2128*
                       m.b17*m.b28 + 1792*m.b17*m.b29 + 1488*m.b17*m.b30 + 1200*m.b17*m.b31 + 944*m.b17*m.b32 + 704*
                       m.b17*m.b33 + 496*m.b17*m.b34 + 304*m.b17*m.b35 + 144*m.b17*m.b36 + 5920*m.b18*m.b19 + 5680*m.b18
                       *m.b20 + 5200*m.b18*m.b21 + 4736*m.b18*m.b22 + 4304*m.b18*m.b23 + 3888*m.b18*m.b24 + 3504*m.b18*
                       m.b25 + 3136*m.b18*m.b26 + 2800*m.b18*m.b27 + 2480*m.b18*m.b28 + 2128*m.b18*m.b29 + 1792*m.b18*
                       m.b30 + 1488*m.b18*m.b31 + 1200*m.b18*m.b32 + 944*m.b18*m.b33 + 704*m.b18*m.b34 + 496*m.b18*m.b35
                        + 304*m.b18*m.b36 + 144*m.b18*m.b37 + 6192*m.b19*m.b20 + 5680*m.b19*m.b21 + 5200*m.b19*m.b22 + 
                       4736*m.b19*m.b23 + 4304*m.b19*m.b24 + 3888*m.b19*m.b25 + 3504*m.b19*m.b26 + 3136*m.b19*m.b27 + 
                       2800*m.b19*m.b28 + 2480*m.b19*m.b29 + 2128*m.b19*m.b30 + 1792*m.b19*m.b31 + 1488*m.b19*m.b32 + 
                       1200*m.b19*m.b33 + 944*m.b19*m.b34 + 704*m.b19*m.b35 + 496*m.b19*m.b36 + 304*m.b19*m.b37 + 144*
                       m.b19*m.b38 + 6192*m.b20*m.b21 + 5680*m.b20*m.b22 + 5200*m.b20*m.b23 + 4736*m.b20*m.b24 + 4304*
                       m.b20*m.b25 + 3888*m.b20*m.b26 + 3504*m.b20*m.b27 + 3136*m.b20*m.b28 + 2800*m.b20*m.b29 + 2480*
                       m.b20*m.b30 + 2128*m.b20*m.b31 + 1792*m.b20*m.b32 + 1488*m.b20*m.b33 + 1200*m.b20*m.b34 + 944*
                       m.b20*m.b35 + 704*m.b20*m.b36 + 496*m.b20*m.b37 + 304*m.b20*m.b38 + 144*m.b20*m.b39 + 6192*m.b21*
                       m.b22 + 5680*m.b21*m.b23 + 5200*m.b21*m.b24 + 4736*m.b21*m.b25 + 4304*m.b21*m.b26 + 3888*m.b21*
                       m.b27 + 3504*m.b21*m.b28 + 3136*m.b21*m.b29 + 2800*m.b21*m.b30 + 2480*m.b21*m.b31 + 2128*m.b21*
                       m.b32 + 1792*m.b21*m.b33 + 1488*m.b21*m.b34 + 1200*m.b21*m.b35 + 944*m.b21*m.b36 + 704*m.b21*
                       m.b37 + 496*m.b21*m.b38 + 304*m.b21*m.b39 + 144*m.b21*m.b40 + 5920*m.b22*m.b23 + 5416*m.b22*m.b24
                        + 4944*m.b22*m.b25 + 4488*m.b22*m.b26 + 4064*m.b22*m.b27 + 3656*m.b22*m.b28 + 3280*m.b22*m.b29
                        + 2920*m.b22*m.b30 + 2592*m.b22*m.b31 + 2264*m.b22*m.b32 + 1920*m.b22*m.b33 + 1592*m.b22*m.b34
                        + 1296*m.b22*m.b35 + 1016*m.b22*m.b36 + 768*m.b22*m.b37 + 536*m.b22*m.b38 + 336*m.b22*m.b39 + 
                       152*m.b22*m.b40 + 5648*m.b23*m.b24 + 5136*m.b23*m.b25 + 4672*m.b23*m.b26 + 4224*m.b23*m.b27 + 
                       3808*m.b23*m.b28 + 3408*m.b23*m.b29 + 3040*m.b23*m.b30 + 2688*m.b23*m.b31 + 2368*m.b23*m.b32 + 
                       2032*m.b23*m.b33 + 1696*m.b23*m.b34 + 1376*m.b23*m.b35 + 1088*m.b23*m.b36 + 816*m.b23*m.b37 + 576
                       *m.b23*m.b38 + 352*m.b23*m.b39 + 160*m.b23*m.b40 + 5360*m.b24*m.b25 + 4856*m.b24*m.b26 + 4384*
                       m.b24*m.b27 + 3944*m.b24*m.b28 + 3536*m.b24*m.b29 + 3144*m.b24*m.b30 + 2784*m.b24*m.b31 + 2440*
                       m.b24*m.b32 + 2112*m.b24*m.b33 + 1784*m.b24*m.b34 + 1456*m.b24*m.b35 + 1144*m.b24*m.b36 + 864*
                       m.b24*m.b37 + 600*m.b24*m.b38 + 368*m.b24*m.b39 + 168*m.b24*m.b40 + 5056*m.b25*m.b26 + 4560*m.b25
                       *m.b27 + 4096*m.b25*m.b28 + 3648*m.b25*m.b29 + 3248*m.b25*m.b30 + 2864*m.b25*m.b31 + 2512*m.b25*
                       m.b32 + 2176*m.b25*m.b33 + 1840*m.b25*m.b34 + 1520*m.b25*m.b35 + 1200*m.b25*m.b36 + 896*m.b25*
                       m.b37 + 624*m.b25*m.b38 + 384*m.b25*m.b39 + 176*m.b25*m.b40 + 4736*m.b26*m.b27 + 4248*m.b26*m.b28
                        + 3792*m.b26*m.b29 + 3352*m.b26*m.b30 + 2944*m.b26*m.b31 + 2568*m.b26*m.b32 + 2224*m.b26*m.b33
                        + 1880*m.b26*m.b34 + 1552*m.b26*m.b35 + 1240*m.b26*m.b36 + 928*m.b26*m.b37 + 648*m.b26*m.b38 + 
                       400*m.b26*m.b39 + 184*m.b26*m.b40 + 4400*m.b27*m.b28 + 3920*m.b27*m.b29 + 3472*m.b27*m.b30 + 3040
                       *m.b27*m.b31 + 2640*m.b27*m.b32 + 2256*m.b27*m.b33 + 1920*m.b27*m.b34 + 1568*m.b27*m.b35 + 1248*
                       m.b27*m.b36 + 960*m.b27*m.b37 + 672*m.b27*m.b38 + 416*m.b27*m.b39 + 192*m.b27*m.b40 + 4048*m.b28*
                       m.b29 + 3576*m.b28*m.b30 + 3136*m.b28*m.b31 + 2712*m.b28*m.b32 + 2320*m.b28*m.b33 + 1944*m.b28*
                       m.b34 + 1584*m.b28*m.b35 + 1256*m.b28*m.b36 + 960*m.b28*m.b37 + 696*m.b28*m.b38 + 432*m.b28*m.b39
                        + 200*m.b28*m.b40 + 3680*m.b29*m.b30 + 3216*m.b29*m.b31 + 2784*m.b29*m.b32 + 2368*m.b29*m.b33 + 
                       1984*m.b29*m.b34 + 1632*m.b29*m.b35 + 1280*m.b29*m.b36 + 960*m.b29*m.b37 + 688*m.b29*m.b38 + 448*
                       m.b29*m.b39 + 208*m.b29*m.b40 + 3296*m.b30*m.b31 + 2840*m.b30*m.b32 + 2416*m.b30*m.b33 + 2024*
                       m.b30*m.b34 + 1664*m.b30*m.b35 + 1320*m.b30*m.b36 + 992*m.b30*m.b37 + 696*m.b30*m.b38 + 432*m.b30
                       *m.b39 + 216*m.b30*m.b40 + 2896*m.b31*m.b32 + 2464*m.b31*m.b33 + 2064*m.b31*m.b34 + 1696*m.b31*
                       m.b35 + 1360*m.b31*m.b36 + 1024*m.b31*m.b37 + 720*m.b31*m.b38 + 448*m.b31*m.b39 + 208*m.b31*m.b40
                        + 2512*m.b32*m.b33 + 2104*m.b32*m.b34 + 1728*m.b32*m.b35 + 1384*m.b32*m.b36 + 1056*m.b32*m.b37
                        + 744*m.b32*m.b38 + 464*m.b32*m.b39 + 216*m.b32*m.b40 + 2144*m.b33*m.b34 + 1760*m.b33*m.b35 + 
                       1408*m.b33*m.b36 + 1088*m.b33*m.b37 + 768*m.b33*m.b38 + 480*m.b33*m.b39 + 224*m.b33*m.b40 + 1792*
                       m.b34*m.b35 + 1432*m.b34*m.b36 + 1104*m.b34*m.b37 + 792*m.b34*m.b38 + 496*m.b34*m.b39 + 232*m.b34
                       *m.b40 + 1456*m.b35*m.b36 + 1120*m.b35*m.b37 + 816*m.b35*m.b38 + 512*m.b35*m.b39 + 240*m.b35*
                       m.b40 + 1136*m.b36*m.b37 + 824*m.b36*m.b38 + 528*m.b36*m.b39 + 248*m.b36*m.b40 + 832*m.b37*m.b38
                        + 544*m.b37*m.b39 + 256*m.b37*m.b40 + 544*m.b38*m.b39 + 264*m.b38*m.b40 + 272*m.b39*m.b40 - 684*
                       m.b1 - 1432*m.b2 - 2236*m.b3 - 3088*m.b4 - 3980*m.b5 - 4904*m.b6 - 5852*m.b7 - 6816*m.b8 - 7788*
                       m.b9 - 8760*m.b10 - 9732*m.b11 - 10704*m.b12 - 11668*m.b13 - 12616*m.b14 - 13540*m.b15 - 14432*
                       m.b16 - 15284*m.b17 - 16088*m.b18 - 16836*m.b19 - 17520*m.b20 - 17520*m.b21 - 16836*m.b22 - 16088
                       *m.b23 - 15284*m.b24 - 14432*m.b25 - 13540*m.b26 - 12616*m.b27 - 11668*m.b28 - 10704*m.b29 - 9732
                       *m.b30 - 8760*m.b31 - 7788*m.b32 - 6816*m.b33 - 5852*m.b34 - 4904*m.b35 - 3980*m.b36 - 3088*m.b37
                        - 2236*m.b38 - 1432*m.b39 - 684*m.b40 - m.x41 <= 0)

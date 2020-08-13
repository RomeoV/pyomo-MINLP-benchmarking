#  MINLP written by GAMS Convert at 08/13/20 17:37:44
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

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b3*m.b4*m.b6
                        + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 64*m.b2*m.b3*m.b6*m.b7 + 64*m.b2*m.b4*m.b5
                       *m.b7 + 192*m.b3*m.b4*m.b5*m.b6 + 128*m.b3*m.b4*m.b6*m.b7 + 64*m.b3*m.b4*m.b7*m.b8 + 64*m.b3*m.b5
                       *m.b6*m.b8 + 192*m.b4*m.b5*m.b6*m.b7 + 128*m.b4*m.b5*m.b7*m.b8 + 64*m.b4*m.b5*m.b8*m.b9 + 64*m.b4
                       *m.b6*m.b7*m.b9 + 192*m.b5*m.b6*m.b7*m.b8 + 128*m.b5*m.b6*m.b8*m.b9 + 64*m.b5*m.b6*m.b9*m.b10 + 
                       64*m.b5*m.b7*m.b8*m.b10 + 192*m.b6*m.b7*m.b8*m.b9 + 128*m.b6*m.b7*m.b9*m.b10 + 64*m.b6*m.b7*m.b10
                       *m.b11 + 64*m.b6*m.b8*m.b9*m.b11 + 192*m.b7*m.b8*m.b9*m.b10 + 128*m.b7*m.b8*m.b10*m.b11 + 64*m.b7
                       *m.b8*m.b11*m.b12 + 64*m.b7*m.b9*m.b10*m.b12 + 192*m.b8*m.b9*m.b10*m.b11 + 128*m.b8*m.b9*m.b11*
                       m.b12 + 64*m.b8*m.b9*m.b12*m.b13 + 64*m.b8*m.b10*m.b11*m.b13 + 192*m.b9*m.b10*m.b11*m.b12 + 128*
                       m.b9*m.b10*m.b12*m.b13 + 64*m.b9*m.b10*m.b13*m.b14 + 64*m.b9*m.b11*m.b12*m.b14 + 192*m.b10*m.b11*
                       m.b12*m.b13 + 128*m.b10*m.b11*m.b13*m.b14 + 64*m.b10*m.b11*m.b14*m.b15 + 64*m.b10*m.b12*m.b13*
                       m.b15 + 192*m.b11*m.b12*m.b13*m.b14 + 128*m.b11*m.b12*m.b14*m.b15 + 64*m.b11*m.b12*m.b15*m.b16 + 
                       64*m.b11*m.b13*m.b14*m.b16 + 192*m.b12*m.b13*m.b14*m.b15 + 128*m.b12*m.b13*m.b15*m.b16 + 64*m.b12
                       *m.b13*m.b16*m.b17 + 64*m.b12*m.b14*m.b15*m.b17 + 192*m.b13*m.b14*m.b15*m.b16 + 128*m.b13*m.b14*
                       m.b16*m.b17 + 64*m.b13*m.b14*m.b17*m.b18 + 64*m.b13*m.b15*m.b16*m.b18 + 192*m.b14*m.b15*m.b16*
                       m.b17 + 128*m.b14*m.b15*m.b17*m.b18 + 64*m.b14*m.b15*m.b18*m.b19 + 64*m.b14*m.b16*m.b17*m.b19 + 
                       192*m.b15*m.b16*m.b17*m.b18 + 128*m.b15*m.b16*m.b18*m.b19 + 64*m.b15*m.b16*m.b19*m.b20 + 64*m.b15
                       *m.b17*m.b18*m.b20 + 192*m.b16*m.b17*m.b18*m.b19 + 128*m.b16*m.b17*m.b19*m.b20 + 64*m.b16*m.b17*
                       m.b20*m.b21 + 64*m.b16*m.b18*m.b19*m.b21 + 192*m.b17*m.b18*m.b19*m.b20 + 128*m.b17*m.b18*m.b20*
                       m.b21 + 64*m.b17*m.b18*m.b21*m.b22 + 64*m.b17*m.b19*m.b20*m.b22 + 192*m.b18*m.b19*m.b20*m.b21 + 
                       128*m.b18*m.b19*m.b21*m.b22 + 64*m.b18*m.b19*m.b22*m.b23 + 64*m.b18*m.b20*m.b21*m.b23 + 192*m.b19
                       *m.b20*m.b21*m.b22 + 128*m.b19*m.b20*m.b22*m.b23 + 64*m.b19*m.b20*m.b23*m.b24 + 64*m.b19*m.b21*
                       m.b22*m.b24 + 192*m.b20*m.b21*m.b22*m.b23 + 128*m.b20*m.b21*m.b23*m.b24 + 64*m.b20*m.b21*m.b24*
                       m.b25 + 64*m.b20*m.b22*m.b23*m.b25 + 128*m.b21*m.b22*m.b23*m.b24 + 64*m.b21*m.b22*m.b24*m.b25 + 
                       64*m.b22*m.b23*m.b24*m.b25 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 32*m.b1*
                       m.b2*m.b6 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b6 - 32*m.b1*m.b4*m.b5 - 32*m.b1*m.b4*m.b6 - 32*
                       m.b1*m.b5*m.b6 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 96*m.b2*m.b3*m.b6 - 32*m.b2*m.b3*m.b7
                        - 128*m.b2*m.b4*m.b5 - 32*m.b2*m.b4*m.b7 - 96*m.b2*m.b5*m.b6 - 32*m.b2*m.b5*m.b7 - 32*m.b2*m.b6*
                       m.b7 - 160*m.b3*m.b4*m.b5 - 192*m.b3*m.b4*m.b6 - 96*m.b3*m.b4*m.b7 - 32*m.b3*m.b4*m.b8 - 192*m.b3
                       *m.b5*m.b6 - 32*m.b3*m.b5*m.b8 - 96*m.b3*m.b6*m.b7 - 32*m.b3*m.b6*m.b8 - 32*m.b3*m.b7*m.b8 - 192*
                       m.b4*m.b5*m.b6 - 192*m.b4*m.b5*m.b7 - 96*m.b4*m.b5*m.b8 - 32*m.b4*m.b5*m.b9 - 192*m.b4*m.b6*m.b7
                        - 32*m.b4*m.b6*m.b9 - 96*m.b4*m.b7*m.b8 - 32*m.b4*m.b7*m.b9 - 32*m.b4*m.b8*m.b9 - 192*m.b5*m.b6*
                       m.b7 - 192*m.b5*m.b6*m.b8 - 96*m.b5*m.b6*m.b9 - 32*m.b5*m.b6*m.b10 - 192*m.b5*m.b7*m.b8 - 32*m.b5
                       *m.b7*m.b10 - 96*m.b5*m.b8*m.b9 - 32*m.b5*m.b8*m.b10 - 32*m.b5*m.b9*m.b10 - 192*m.b6*m.b7*m.b8 - 
                       192*m.b6*m.b7*m.b9 - 96*m.b6*m.b7*m.b10 - 32*m.b6*m.b7*m.b11 - 192*m.b6*m.b8*m.b9 - 32*m.b6*m.b8*
                       m.b11 - 96*m.b6*m.b9*m.b10 - 32*m.b6*m.b9*m.b11 - 32*m.b6*m.b10*m.b11 - 192*m.b7*m.b8*m.b9 - 192*
                       m.b7*m.b8*m.b10 - 96*m.b7*m.b8*m.b11 - 32*m.b7*m.b8*m.b12 - 192*m.b7*m.b9*m.b10 - 32*m.b7*m.b9*
                       m.b12 - 96*m.b7*m.b10*m.b11 - 32*m.b7*m.b10*m.b12 - 32*m.b7*m.b11*m.b12 - 192*m.b8*m.b9*m.b10 - 
                       192*m.b8*m.b9*m.b11 - 96*m.b8*m.b9*m.b12 - 32*m.b8*m.b9*m.b13 - 192*m.b8*m.b10*m.b11 - 32*m.b8*
                       m.b10*m.b13 - 96*m.b8*m.b11*m.b12 - 32*m.b8*m.b11*m.b13 - 32*m.b8*m.b12*m.b13 - 192*m.b9*m.b10*
                       m.b11 - 192*m.b9*m.b10*m.b12 - 96*m.b9*m.b10*m.b13 - 32*m.b9*m.b10*m.b14 - 192*m.b9*m.b11*m.b12
                        - 32*m.b9*m.b11*m.b14 - 96*m.b9*m.b12*m.b13 - 32*m.b9*m.b12*m.b14 - 32*m.b9*m.b13*m.b14 - 192*
                       m.b10*m.b11*m.b12 - 192*m.b10*m.b11*m.b13 - 96*m.b10*m.b11*m.b14 - 32*m.b10*m.b11*m.b15 - 192*
                       m.b10*m.b12*m.b13 - 32*m.b10*m.b12*m.b15 - 96*m.b10*m.b13*m.b14 - 32*m.b10*m.b13*m.b15 - 32*m.b10
                       *m.b14*m.b15 - 192*m.b11*m.b12*m.b13 - 192*m.b11*m.b12*m.b14 - 96*m.b11*m.b12*m.b15 - 32*m.b11*
                       m.b12*m.b16 - 192*m.b11*m.b13*m.b14 - 32*m.b11*m.b13*m.b16 - 96*m.b11*m.b14*m.b15 - 32*m.b11*
                       m.b14*m.b16 - 32*m.b11*m.b15*m.b16 - 192*m.b12*m.b13*m.b14 - 192*m.b12*m.b13*m.b15 - 96*m.b12*
                       m.b13*m.b16 - 32*m.b12*m.b13*m.b17 - 192*m.b12*m.b14*m.b15 - 32*m.b12*m.b14*m.b17 - 96*m.b12*
                       m.b15*m.b16 - 32*m.b12*m.b15*m.b17 - 32*m.b12*m.b16*m.b17 - 192*m.b13*m.b14*m.b15 - 192*m.b13*
                       m.b14*m.b16 - 96*m.b13*m.b14*m.b17 - 32*m.b13*m.b14*m.b18 - 192*m.b13*m.b15*m.b16 - 32*m.b13*
                       m.b15*m.b18 - 96*m.b13*m.b16*m.b17 - 32*m.b13*m.b16*m.b18 - 32*m.b13*m.b17*m.b18 - 192*m.b14*
                       m.b15*m.b16 - 192*m.b14*m.b15*m.b17 - 96*m.b14*m.b15*m.b18 - 32*m.b14*m.b15*m.b19 - 192*m.b14*
                       m.b16*m.b17 - 32*m.b14*m.b16*m.b19 - 96*m.b14*m.b17*m.b18 - 32*m.b14*m.b17*m.b19 - 32*m.b14*m.b18
                       *m.b19 - 192*m.b15*m.b16*m.b17 - 192*m.b15*m.b16*m.b18 - 96*m.b15*m.b16*m.b19 - 32*m.b15*m.b16*
                       m.b20 - 192*m.b15*m.b17*m.b18 - 32*m.b15*m.b17*m.b20 - 96*m.b15*m.b18*m.b19 - 32*m.b15*m.b18*
                       m.b20 - 32*m.b15*m.b19*m.b20 - 192*m.b16*m.b17*m.b18 - 192*m.b16*m.b17*m.b19 - 96*m.b16*m.b17*
                       m.b20 - 32*m.b16*m.b17*m.b21 - 192*m.b16*m.b18*m.b19 - 32*m.b16*m.b18*m.b21 - 96*m.b16*m.b19*
                       m.b20 - 32*m.b16*m.b19*m.b21 - 32*m.b16*m.b20*m.b21 - 192*m.b17*m.b18*m.b19 - 192*m.b17*m.b18*
                       m.b20 - 96*m.b17*m.b18*m.b21 - 32*m.b17*m.b18*m.b22 - 192*m.b17*m.b19*m.b20 - 32*m.b17*m.b19*
                       m.b22 - 96*m.b17*m.b20*m.b21 - 32*m.b17*m.b20*m.b22 - 32*m.b17*m.b21*m.b22 - 192*m.b18*m.b19*
                       m.b20 - 192*m.b18*m.b19*m.b21 - 96*m.b18*m.b19*m.b22 - 32*m.b18*m.b19*m.b23 - 192*m.b18*m.b20*
                       m.b21 - 32*m.b18*m.b20*m.b23 - 96*m.b18*m.b21*m.b22 - 32*m.b18*m.b21*m.b23 - 32*m.b18*m.b22*m.b23
                        - 192*m.b19*m.b20*m.b21 - 192*m.b19*m.b20*m.b22 - 96*m.b19*m.b20*m.b23 - 32*m.b19*m.b20*m.b24 - 
                       192*m.b19*m.b21*m.b22 - 32*m.b19*m.b21*m.b24 - 96*m.b19*m.b22*m.b23 - 32*m.b19*m.b22*m.b24 - 32*
                       m.b19*m.b23*m.b24 - 192*m.b20*m.b21*m.b22 - 192*m.b20*m.b21*m.b23 - 96*m.b20*m.b21*m.b24 - 32*
                       m.b20*m.b21*m.b25 - 192*m.b20*m.b22*m.b23 - 32*m.b20*m.b22*m.b25 - 96*m.b20*m.b23*m.b24 - 32*
                       m.b20*m.b23*m.b25 - 32*m.b20*m.b24*m.b25 - 160*m.b21*m.b22*m.b23 - 128*m.b21*m.b22*m.b24 - 32*
                       m.b21*m.b22*m.b25 - 128*m.b21*m.b23*m.b24 - 64*m.b21*m.b24*m.b25 - 96*m.b22*m.b23*m.b24 - 64*
                       m.b22*m.b23*m.b25 - 64*m.b22*m.b24*m.b25 - 32*m.b23*m.b24*m.b25 + 48*m.b1*m.b2 + 40*m.b1*m.b3 + 
                       48*m.b1*m.b4 + 40*m.b1*m.b5 + 32*m.b1*m.b6 + 96*m.b2*m.b3 + 96*m.b2*m.b4 + 112*m.b2*m.b5 + 80*
                       m.b2*m.b6 + 32*m.b2*m.b7 + 160*m.b3*m.b4 + 152*m.b3*m.b5 + 160*m.b3*m.b6 + 80*m.b3*m.b7 + 32*m.b3
                       *m.b8 + 208*m.b4*m.b5 + 192*m.b4*m.b6 + 160*m.b4*m.b7 + 80*m.b4*m.b8 + 32*m.b4*m.b9 + 256*m.b5*
                       m.b6 + 192*m.b5*m.b7 + 160*m.b5*m.b8 + 80*m.b5*m.b9 + 32*m.b5*m.b10 + 256*m.b6*m.b7 + 192*m.b6*
                       m.b8 + 160*m.b6*m.b9 + 80*m.b6*m.b10 + 32*m.b6*m.b11 + 256*m.b7*m.b8 + 192*m.b7*m.b9 + 160*m.b7*
                       m.b10 + 80*m.b7*m.b11 + 32*m.b7*m.b12 + 256*m.b8*m.b9 + 192*m.b8*m.b10 + 160*m.b8*m.b11 + 80*m.b8
                       *m.b12 + 32*m.b8*m.b13 + 256*m.b9*m.b10 + 192*m.b9*m.b11 + 160*m.b9*m.b12 + 80*m.b9*m.b13 + 32*
                       m.b9*m.b14 + 256*m.b10*m.b11 + 192*m.b10*m.b12 + 160*m.b10*m.b13 + 80*m.b10*m.b14 + 32*m.b10*
                       m.b15 + 256*m.b11*m.b12 + 192*m.b11*m.b13 + 160*m.b11*m.b14 + 80*m.b11*m.b15 + 32*m.b11*m.b16 + 
                       256*m.b12*m.b13 + 192*m.b12*m.b14 + 160*m.b12*m.b15 + 80*m.b12*m.b16 + 32*m.b12*m.b17 + 256*m.b13
                       *m.b14 + 192*m.b13*m.b15 + 160*m.b13*m.b16 + 80*m.b13*m.b17 + 32*m.b13*m.b18 + 256*m.b14*m.b15 + 
                       192*m.b14*m.b16 + 160*m.b14*m.b17 + 80*m.b14*m.b18 + 32*m.b14*m.b19 + 256*m.b15*m.b16 + 192*m.b15
                       *m.b17 + 160*m.b15*m.b18 + 80*m.b15*m.b19 + 32*m.b15*m.b20 + 256*m.b16*m.b17 + 192*m.b16*m.b18 + 
                       160*m.b16*m.b19 + 80*m.b16*m.b20 + 32*m.b16*m.b21 + 256*m.b17*m.b18 + 192*m.b17*m.b19 + 160*m.b17
                       *m.b20 + 80*m.b17*m.b21 + 32*m.b17*m.b22 + 256*m.b18*m.b19 + 192*m.b18*m.b20 + 160*m.b18*m.b21 + 
                       80*m.b18*m.b22 + 32*m.b18*m.b23 + 256*m.b19*m.b20 + 192*m.b19*m.b21 + 160*m.b19*m.b22 + 80*m.b19*
                       m.b23 + 32*m.b19*m.b24 + 256*m.b20*m.b21 + 192*m.b20*m.b22 + 160*m.b20*m.b23 + 80*m.b20*m.b24 + 
                       32*m.b20*m.b25 + 208*m.b21*m.b22 + 152*m.b21*m.b23 + 112*m.b21*m.b24 + 40*m.b21*m.b25 + 160*m.b22
                       *m.b23 + 96*m.b22*m.b24 + 48*m.b22*m.b25 + 96*m.b23*m.b24 + 40*m.b23*m.b25 + 48*m.b24*m.b25 - 40*
                       m.b1 - 88*m.b2 - 136*m.b3 - 184*m.b4 - 232*m.b5 - 272*m.b6 - 272*m.b7 - 272*m.b8 - 272*m.b9 - 272
                       *m.b10 - 272*m.b11 - 272*m.b12 - 272*m.b13 - 272*m.b14 - 272*m.b15 - 272*m.b16 - 272*m.b17 - 272*
                       m.b18 - 272*m.b19 - 272*m.b20 - 232*m.b21 - 184*m.b22 - 136*m.b23 - 88*m.b24 - 40*m.b25 - m.x26
                        <= 0)

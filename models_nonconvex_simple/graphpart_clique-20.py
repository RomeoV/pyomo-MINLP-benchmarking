#  MINLP written by GAMS Convert at 08/13/20 17:37:55
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21       21        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         61        1       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        121       61       60        0
# 
#  Reformulation has removed 1 variable and 1 equation


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

m.obj = Objective(expr=m.b1*m.b4 + 2*m.b1*m.b7 + 3*m.b1*m.b10 + 4*m.b1*m.b13 + 5*m.b1*m.b16 + 6*m.b1*m.b19 + 7*m.b1*
                       m.b22 + 8*m.b1*m.b25 + 9*m.b1*m.b28 + 10*m.b1*m.b31 + 11*m.b1*m.b34 + 12*m.b1*m.b37 + 13*m.b1*
                       m.b40 + 14*m.b1*m.b43 + 15*m.b1*m.b46 + 16*m.b1*m.b49 + 17*m.b1*m.b52 + 18*m.b1*m.b55 + 19*m.b1*
                       m.b58 + m.b2*m.b5 + 2*m.b2*m.b8 + 3*m.b2*m.b11 + 4*m.b2*m.b14 + 5*m.b2*m.b17 + 6*m.b2*m.b20 + 7*
                       m.b2*m.b23 + 8*m.b2*m.b26 + 9*m.b2*m.b29 + 10*m.b2*m.b32 + 11*m.b2*m.b35 + 12*m.b2*m.b38 + 13*
                       m.b2*m.b41 + 14*m.b2*m.b44 + 15*m.b2*m.b47 + 16*m.b2*m.b50 + 17*m.b2*m.b53 + 18*m.b2*m.b56 + 19*
                       m.b2*m.b59 + m.b3*m.b6 + 2*m.b3*m.b9 + 3*m.b3*m.b12 + 4*m.b3*m.b15 + 5*m.b3*m.b18 + 6*m.b3*m.b21
                        + 7*m.b3*m.b24 + 8*m.b3*m.b27 + 9*m.b3*m.b30 + 10*m.b3*m.b33 + 11*m.b3*m.b36 + 12*m.b3*m.b39 + 
                       13*m.b3*m.b42 + 14*m.b3*m.b45 + 15*m.b3*m.b48 + 16*m.b3*m.b51 + 17*m.b3*m.b54 + 18*m.b3*m.b57 + 
                       19*m.b3*m.b60 + m.b4*m.b7 + 2*m.b4*m.b10 + 3*m.b4*m.b13 + 4*m.b4*m.b16 + 5*m.b4*m.b19 + 6*m.b4*
                       m.b22 + 7*m.b4*m.b25 + 8*m.b4*m.b28 + 9*m.b4*m.b31 + 10*m.b4*m.b34 + 11*m.b4*m.b37 + 12*m.b4*
                       m.b40 + 13*m.b4*m.b43 + 14*m.b4*m.b46 + 15*m.b4*m.b49 + 16*m.b4*m.b52 + 17*m.b4*m.b55 + 18*m.b4*
                       m.b58 + m.b5*m.b8 + 2*m.b5*m.b11 + 3*m.b5*m.b14 + 4*m.b5*m.b17 + 5*m.b5*m.b20 + 6*m.b5*m.b23 + 7*
                       m.b5*m.b26 + 8*m.b5*m.b29 + 9*m.b5*m.b32 + 10*m.b5*m.b35 + 11*m.b5*m.b38 + 12*m.b5*m.b41 + 13*
                       m.b5*m.b44 + 14*m.b5*m.b47 + 15*m.b5*m.b50 + 16*m.b5*m.b53 + 17*m.b5*m.b56 + 18*m.b5*m.b59 + m.b6
                       *m.b9 + 2*m.b6*m.b12 + 3*m.b6*m.b15 + 4*m.b6*m.b18 + 5*m.b6*m.b21 + 6*m.b6*m.b24 + 7*m.b6*m.b27
                        + 8*m.b6*m.b30 + 9*m.b6*m.b33 + 10*m.b6*m.b36 + 11*m.b6*m.b39 + 12*m.b6*m.b42 + 13*m.b6*m.b45 + 
                       14*m.b6*m.b48 + 15*m.b6*m.b51 + 16*m.b6*m.b54 + 17*m.b6*m.b57 + 18*m.b6*m.b60 + m.b7*m.b10 + 2*
                       m.b7*m.b13 + 3*m.b7*m.b16 + 4*m.b7*m.b19 + 5*m.b7*m.b22 + 6*m.b7*m.b25 + 7*m.b7*m.b28 + 8*m.b7*
                       m.b31 + 9*m.b7*m.b34 + 10*m.b7*m.b37 + 11*m.b7*m.b40 + 12*m.b7*m.b43 + 13*m.b7*m.b46 + 14*m.b7*
                       m.b49 + 15*m.b7*m.b52 + 16*m.b7*m.b55 + 17*m.b7*m.b58 + m.b8*m.b11 + 2*m.b8*m.b14 + 3*m.b8*m.b17
                        + 4*m.b8*m.b20 + 5*m.b8*m.b23 + 6*m.b8*m.b26 + 7*m.b8*m.b29 + 8*m.b8*m.b32 + 9*m.b8*m.b35 + 10*
                       m.b8*m.b38 + 11*m.b8*m.b41 + 12*m.b8*m.b44 + 13*m.b8*m.b47 + 14*m.b8*m.b50 + 15*m.b8*m.b53 + 16*
                       m.b8*m.b56 + 17*m.b8*m.b59 + m.b9*m.b12 + 2*m.b9*m.b15 + 3*m.b9*m.b18 + 4*m.b9*m.b21 + 5*m.b9*
                       m.b24 + 6*m.b9*m.b27 + 7*m.b9*m.b30 + 8*m.b9*m.b33 + 9*m.b9*m.b36 + 10*m.b9*m.b39 + 11*m.b9*m.b42
                        + 12*m.b9*m.b45 + 13*m.b9*m.b48 + 14*m.b9*m.b51 + 15*m.b9*m.b54 + 16*m.b9*m.b57 + 17*m.b9*m.b60
                        + m.b10*m.b13 + 2*m.b10*m.b16 + 3*m.b10*m.b19 + 4*m.b10*m.b22 + 5*m.b10*m.b25 + 6*m.b10*m.b28 + 
                       7*m.b10*m.b31 + 8*m.b10*m.b34 + 9*m.b10*m.b37 + 10*m.b10*m.b40 + 11*m.b10*m.b43 + 12*m.b10*m.b46
                        + 13*m.b10*m.b49 + 14*m.b10*m.b52 + 15*m.b10*m.b55 + 16*m.b10*m.b58 + m.b11*m.b14 + 2*m.b11*
                       m.b17 + 3*m.b11*m.b20 + 4*m.b11*m.b23 + 5*m.b11*m.b26 + 6*m.b11*m.b29 + 7*m.b11*m.b32 + 8*m.b11*
                       m.b35 + 9*m.b11*m.b38 + 10*m.b11*m.b41 + 11*m.b11*m.b44 + 12*m.b11*m.b47 + 13*m.b11*m.b50 + 14*
                       m.b11*m.b53 + 15*m.b11*m.b56 + 16*m.b11*m.b59 + m.b12*m.b15 + 2*m.b12*m.b18 + 3*m.b12*m.b21 + 4*
                       m.b12*m.b24 + 5*m.b12*m.b27 + 6*m.b12*m.b30 + 7*m.b12*m.b33 + 8*m.b12*m.b36 + 9*m.b12*m.b39 + 10*
                       m.b12*m.b42 + 11*m.b12*m.b45 + 12*m.b12*m.b48 + 13*m.b12*m.b51 + 14*m.b12*m.b54 + 15*m.b12*m.b57
                        + 16*m.b12*m.b60 + m.b13*m.b16 + 2*m.b13*m.b19 + 3*m.b13*m.b22 + 4*m.b13*m.b25 + 5*m.b13*m.b28
                        + 6*m.b13*m.b31 + 7*m.b13*m.b34 + 8*m.b13*m.b37 + 9*m.b13*m.b40 + 10*m.b13*m.b43 + 11*m.b13*
                       m.b46 + 12*m.b13*m.b49 + 13*m.b13*m.b52 + 14*m.b13*m.b55 + 15*m.b13*m.b58 + m.b14*m.b17 + 2*m.b14
                       *m.b20 + 3*m.b14*m.b23 + 4*m.b14*m.b26 + 5*m.b14*m.b29 + 6*m.b14*m.b32 + 7*m.b14*m.b35 + 8*m.b14*
                       m.b38 + 9*m.b14*m.b41 + 10*m.b14*m.b44 + 11*m.b14*m.b47 + 12*m.b14*m.b50 + 13*m.b14*m.b53 + 14*
                       m.b14*m.b56 + 15*m.b14*m.b59 + m.b15*m.b18 + 2*m.b15*m.b21 + 3*m.b15*m.b24 + 4*m.b15*m.b27 + 5*
                       m.b15*m.b30 + 6*m.b15*m.b33 + 7*m.b15*m.b36 + 8*m.b15*m.b39 + 9*m.b15*m.b42 + 10*m.b15*m.b45 + 11
                       *m.b15*m.b48 + 12*m.b15*m.b51 + 13*m.b15*m.b54 + 14*m.b15*m.b57 + 15*m.b15*m.b60 + m.b16*m.b19 + 
                       2*m.b16*m.b22 + 3*m.b16*m.b25 + 4*m.b16*m.b28 + 5*m.b16*m.b31 + 6*m.b16*m.b34 + 7*m.b16*m.b37 + 8
                       *m.b16*m.b40 + 9*m.b16*m.b43 + 10*m.b16*m.b46 + 11*m.b16*m.b49 + 12*m.b16*m.b52 + 13*m.b16*m.b55
                        + 14*m.b16*m.b58 + m.b17*m.b20 + 2*m.b17*m.b23 + 3*m.b17*m.b26 + 4*m.b17*m.b29 + 5*m.b17*m.b32
                        + 6*m.b17*m.b35 + 7*m.b17*m.b38 + 8*m.b17*m.b41 + 9*m.b17*m.b44 + 10*m.b17*m.b47 + 11*m.b17*
                       m.b50 + 12*m.b17*m.b53 + 13*m.b17*m.b56 + 14*m.b17*m.b59 + m.b18*m.b21 + 2*m.b18*m.b24 + 3*m.b18*
                       m.b27 + 4*m.b18*m.b30 + 5*m.b18*m.b33 + 6*m.b18*m.b36 + 7*m.b18*m.b39 + 8*m.b18*m.b42 + 9*m.b18*
                       m.b45 + 10*m.b18*m.b48 + 11*m.b18*m.b51 + 12*m.b18*m.b54 + 13*m.b18*m.b57 + 14*m.b18*m.b60 + 
                       m.b19*m.b22 + 2*m.b19*m.b25 + 3*m.b19*m.b28 + 4*m.b19*m.b31 + 5*m.b19*m.b34 + 6*m.b19*m.b37 + 7*
                       m.b19*m.b40 + 8*m.b19*m.b43 + 9*m.b19*m.b46 + 10*m.b19*m.b49 + 11*m.b19*m.b52 + 12*m.b19*m.b55 + 
                       13*m.b19*m.b58 + m.b20*m.b23 + 2*m.b20*m.b26 + 3*m.b20*m.b29 + 4*m.b20*m.b32 + 5*m.b20*m.b35 + 6*
                       m.b20*m.b38 + 7*m.b20*m.b41 + 8*m.b20*m.b44 + 9*m.b20*m.b47 + 10*m.b20*m.b50 + 11*m.b20*m.b53 + 
                       12*m.b20*m.b56 + 13*m.b20*m.b59 + m.b21*m.b24 + 2*m.b21*m.b27 + 3*m.b21*m.b30 + 4*m.b21*m.b33 + 5
                       *m.b21*m.b36 + 6*m.b21*m.b39 + 7*m.b21*m.b42 + 8*m.b21*m.b45 + 9*m.b21*m.b48 + 10*m.b21*m.b51 + 
                       11*m.b21*m.b54 + 12*m.b21*m.b57 + 13*m.b21*m.b60 + m.b22*m.b25 + 2*m.b22*m.b28 + 3*m.b22*m.b31 + 
                       4*m.b22*m.b34 + 5*m.b22*m.b37 + 6*m.b22*m.b40 + 7*m.b22*m.b43 + 8*m.b22*m.b46 + 9*m.b22*m.b49 + 
                       10*m.b22*m.b52 + 11*m.b22*m.b55 + 12*m.b22*m.b58 + m.b23*m.b26 + 2*m.b23*m.b29 + 3*m.b23*m.b32 + 
                       4*m.b23*m.b35 + 5*m.b23*m.b38 + 6*m.b23*m.b41 + 7*m.b23*m.b44 + 8*m.b23*m.b47 + 9*m.b23*m.b50 + 
                       10*m.b23*m.b53 + 11*m.b23*m.b56 + 12*m.b23*m.b59 + m.b24*m.b27 + 2*m.b24*m.b30 + 3*m.b24*m.b33 + 
                       4*m.b24*m.b36 + 5*m.b24*m.b39 + 6*m.b24*m.b42 + 7*m.b24*m.b45 + 8*m.b24*m.b48 + 9*m.b24*m.b51 + 
                       10*m.b24*m.b54 + 11*m.b24*m.b57 + 12*m.b24*m.b60 + m.b25*m.b28 + 2*m.b25*m.b31 + 3*m.b25*m.b34 + 
                       4*m.b25*m.b37 + 5*m.b25*m.b40 + 6*m.b25*m.b43 + 7*m.b25*m.b46 + 8*m.b25*m.b49 + 9*m.b25*m.b52 + 
                       10*m.b25*m.b55 + 11*m.b25*m.b58 + m.b26*m.b29 + 2*m.b26*m.b32 + 3*m.b26*m.b35 + 4*m.b26*m.b38 + 5
                       *m.b26*m.b41 + 6*m.b26*m.b44 + 7*m.b26*m.b47 + 8*m.b26*m.b50 + 9*m.b26*m.b53 + 10*m.b26*m.b56 + 
                       11*m.b26*m.b59 + m.b27*m.b30 + 2*m.b27*m.b33 + 3*m.b27*m.b36 + 4*m.b27*m.b39 + 5*m.b27*m.b42 + 6*
                       m.b27*m.b45 + 7*m.b27*m.b48 + 8*m.b27*m.b51 + 9*m.b27*m.b54 + 10*m.b27*m.b57 + 11*m.b27*m.b60 + 
                       m.b28*m.b31 + 2*m.b28*m.b34 + 3*m.b28*m.b37 + 4*m.b28*m.b40 + 5*m.b28*m.b43 + 6*m.b28*m.b46 + 7*
                       m.b28*m.b49 + 8*m.b28*m.b52 + 9*m.b28*m.b55 + 10*m.b28*m.b58 + m.b29*m.b32 + 2*m.b29*m.b35 + 3*
                       m.b29*m.b38 + 4*m.b29*m.b41 + 5*m.b29*m.b44 + 6*m.b29*m.b47 + 7*m.b29*m.b50 + 8*m.b29*m.b53 + 9*
                       m.b29*m.b56 + 10*m.b29*m.b59 + m.b30*m.b33 + 2*m.b30*m.b36 + 3*m.b30*m.b39 + 4*m.b30*m.b42 + 5*
                       m.b30*m.b45 + 6*m.b30*m.b48 + 7*m.b30*m.b51 + 8*m.b30*m.b54 + 9*m.b30*m.b57 + 10*m.b30*m.b60 + 
                       m.b31*m.b34 + 2*m.b31*m.b37 + 3*m.b31*m.b40 + 4*m.b31*m.b43 + 5*m.b31*m.b46 + 6*m.b31*m.b49 + 7*
                       m.b31*m.b52 + 8*m.b31*m.b55 + 9*m.b31*m.b58 + m.b32*m.b35 + 2*m.b32*m.b38 + 3*m.b32*m.b41 + 4*
                       m.b32*m.b44 + 5*m.b32*m.b47 + 6*m.b32*m.b50 + 7*m.b32*m.b53 + 8*m.b32*m.b56 + 9*m.b32*m.b59 + 
                       m.b33*m.b36 + 2*m.b33*m.b39 + 3*m.b33*m.b42 + 4*m.b33*m.b45 + 5*m.b33*m.b48 + 6*m.b33*m.b51 + 7*
                       m.b33*m.b54 + 8*m.b33*m.b57 + 9*m.b33*m.b60 + m.b34*m.b37 + 2*m.b34*m.b40 + 3*m.b34*m.b43 + 4*
                       m.b34*m.b46 + 5*m.b34*m.b49 + 6*m.b34*m.b52 + 7*m.b34*m.b55 + 8*m.b34*m.b58 + m.b35*m.b38 + 2*
                       m.b35*m.b41 + 3*m.b35*m.b44 + 4*m.b35*m.b47 + 5*m.b35*m.b50 + 6*m.b35*m.b53 + 7*m.b35*m.b56 + 8*
                       m.b35*m.b59 + m.b36*m.b39 + 2*m.b36*m.b42 + 3*m.b36*m.b45 + 4*m.b36*m.b48 + 5*m.b36*m.b51 + 6*
                       m.b36*m.b54 + 7*m.b36*m.b57 + 8*m.b36*m.b60 + m.b37*m.b40 + 2*m.b37*m.b43 + 3*m.b37*m.b46 + 4*
                       m.b37*m.b49 + 5*m.b37*m.b52 + 6*m.b37*m.b55 + 7*m.b37*m.b58 + m.b38*m.b41 + 2*m.b38*m.b44 + 3*
                       m.b38*m.b47 + 4*m.b38*m.b50 + 5*m.b38*m.b53 + 6*m.b38*m.b56 + 7*m.b38*m.b59 + m.b39*m.b42 + 2*
                       m.b39*m.b45 + 3*m.b39*m.b48 + 4*m.b39*m.b51 + 5*m.b39*m.b54 + 6*m.b39*m.b57 + 7*m.b39*m.b60 + 
                       m.b40*m.b43 + 2*m.b40*m.b46 + 3*m.b40*m.b49 + 4*m.b40*m.b52 + 5*m.b40*m.b55 + 6*m.b40*m.b58 + 
                       m.b41*m.b44 + 2*m.b41*m.b47 + 3*m.b41*m.b50 + 4*m.b41*m.b53 + 5*m.b41*m.b56 + 6*m.b41*m.b59 + 
                       m.b42*m.b45 + 2*m.b42*m.b48 + 3*m.b42*m.b51 + 4*m.b42*m.b54 + 5*m.b42*m.b57 + 6*m.b42*m.b60 + 
                       m.b43*m.b46 + 2*m.b43*m.b49 + 3*m.b43*m.b52 + 4*m.b43*m.b55 + 5*m.b43*m.b58 + m.b44*m.b47 + 2*
                       m.b44*m.b50 + 3*m.b44*m.b53 + 4*m.b44*m.b56 + 5*m.b44*m.b59 + m.b45*m.b48 + 2*m.b45*m.b51 + 3*
                       m.b45*m.b54 + 4*m.b45*m.b57 + 5*m.b45*m.b60 + m.b46*m.b49 + 2*m.b46*m.b52 + 3*m.b46*m.b55 + 4*
                       m.b46*m.b58 + m.b47*m.b50 + 2*m.b47*m.b53 + 3*m.b47*m.b56 + 4*m.b47*m.b59 + m.b48*m.b51 + 2*m.b48
                       *m.b54 + 3*m.b48*m.b57 + 4*m.b48*m.b60 + m.b49*m.b52 + 2*m.b49*m.b55 + 3*m.b49*m.b58 + m.b50*
                       m.b53 + 2*m.b50*m.b56 + 3*m.b50*m.b59 + m.b51*m.b54 + 2*m.b51*m.b57 + 3*m.b51*m.b60 + m.b52*m.b55
                        + 2*m.b52*m.b58 + m.b53*m.b56 + 2*m.b53*m.b59 + m.b54*m.b57 + 2*m.b54*m.b60 + m.b55*m.b58 + 
                       m.b56*m.b59 + m.b57*m.b60, sense=minimize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 == 1)

m.c2 = Constraint(expr=   m.b4 + m.b5 + m.b6 == 1)

m.c3 = Constraint(expr=   m.b7 + m.b8 + m.b9 == 1)

m.c4 = Constraint(expr=   m.b10 + m.b11 + m.b12 == 1)

m.c5 = Constraint(expr=   m.b13 + m.b14 + m.b15 == 1)

m.c6 = Constraint(expr=   m.b16 + m.b17 + m.b18 == 1)

m.c7 = Constraint(expr=   m.b19 + m.b20 + m.b21 == 1)

m.c8 = Constraint(expr=   m.b22 + m.b23 + m.b24 == 1)

m.c9 = Constraint(expr=   m.b25 + m.b26 + m.b27 == 1)

m.c10 = Constraint(expr=   m.b28 + m.b29 + m.b30 == 1)

m.c11 = Constraint(expr=   m.b31 + m.b32 + m.b33 == 1)

m.c12 = Constraint(expr=   m.b34 + m.b35 + m.b36 == 1)

m.c13 = Constraint(expr=   m.b37 + m.b38 + m.b39 == 1)

m.c14 = Constraint(expr=   m.b40 + m.b41 + m.b42 == 1)

m.c15 = Constraint(expr=   m.b43 + m.b44 + m.b45 == 1)

m.c16 = Constraint(expr=   m.b46 + m.b47 + m.b48 == 1)

m.c17 = Constraint(expr=   m.b49 + m.b50 + m.b51 == 1)

m.c18 = Constraint(expr=   m.b52 + m.b53 + m.b54 == 1)

m.c19 = Constraint(expr=   m.b55 + m.b56 + m.b57 == 1)

m.c20 = Constraint(expr=   m.b58 + m.b59 + m.b60 == 1)

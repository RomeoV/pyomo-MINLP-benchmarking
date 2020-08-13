#  MINLP written by GAMS Convert at 08/13/20 17:38:07
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         31       31        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         91        1       90        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        181       91       90        0
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
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=m.b1*m.b4 + 2*m.b1*m.b7 + 3*m.b1*m.b10 + 4*m.b1*m.b13 + 5*m.b1*m.b16 + 6*m.b1*m.b19 + 7*m.b1*
                       m.b22 + 8*m.b1*m.b25 + 9*m.b1*m.b28 + 10*m.b1*m.b31 + 11*m.b1*m.b34 + 12*m.b1*m.b37 + 13*m.b1*
                       m.b40 + 14*m.b1*m.b43 + 15*m.b1*m.b46 + 16*m.b1*m.b49 + 17*m.b1*m.b52 + 18*m.b1*m.b55 + 19*m.b1*
                       m.b58 + 20*m.b1*m.b61 + 21*m.b1*m.b64 + 22*m.b1*m.b67 + 23*m.b1*m.b70 + 24*m.b1*m.b73 + 25*m.b1*
                       m.b76 + 26*m.b1*m.b79 + 27*m.b1*m.b82 + 28*m.b1*m.b85 + 29*m.b1*m.b88 + m.b2*m.b5 + 2*m.b2*m.b8
                        + 3*m.b2*m.b11 + 4*m.b2*m.b14 + 5*m.b2*m.b17 + 6*m.b2*m.b20 + 7*m.b2*m.b23 + 8*m.b2*m.b26 + 9*
                       m.b2*m.b29 + 10*m.b2*m.b32 + 11*m.b2*m.b35 + 12*m.b2*m.b38 + 13*m.b2*m.b41 + 14*m.b2*m.b44 + 15*
                       m.b2*m.b47 + 16*m.b2*m.b50 + 17*m.b2*m.b53 + 18*m.b2*m.b56 + 19*m.b2*m.b59 + 20*m.b2*m.b62 + 21*
                       m.b2*m.b65 + 22*m.b2*m.b68 + 23*m.b2*m.b71 + 24*m.b2*m.b74 + 25*m.b2*m.b77 + 26*m.b2*m.b80 + 27*
                       m.b2*m.b83 + 28*m.b2*m.b86 + 29*m.b2*m.b89 + m.b3*m.b6 + 2*m.b3*m.b9 + 3*m.b3*m.b12 + 4*m.b3*
                       m.b15 + 5*m.b3*m.b18 + 6*m.b3*m.b21 + 7*m.b3*m.b24 + 8*m.b3*m.b27 + 9*m.b3*m.b30 + 10*m.b3*m.b33
                        + 11*m.b3*m.b36 + 12*m.b3*m.b39 + 13*m.b3*m.b42 + 14*m.b3*m.b45 + 15*m.b3*m.b48 + 16*m.b3*m.b51
                        + 17*m.b3*m.b54 + 18*m.b3*m.b57 + 19*m.b3*m.b60 + 20*m.b3*m.b63 + 21*m.b3*m.b66 + 22*m.b3*m.b69
                        + 23*m.b3*m.b72 + 24*m.b3*m.b75 + 25*m.b3*m.b78 + 26*m.b3*m.b81 + 27*m.b3*m.b84 + 28*m.b3*m.b87
                        + 29*m.b3*m.b90 + m.b4*m.b7 + 2*m.b4*m.b10 + 3*m.b4*m.b13 + 4*m.b4*m.b16 + 5*m.b4*m.b19 + 6*m.b4
                       *m.b22 + 7*m.b4*m.b25 + 8*m.b4*m.b28 + 9*m.b4*m.b31 + 10*m.b4*m.b34 + 11*m.b4*m.b37 + 12*m.b4*
                       m.b40 + 13*m.b4*m.b43 + 14*m.b4*m.b46 + 15*m.b4*m.b49 + 16*m.b4*m.b52 + 17*m.b4*m.b55 + 18*m.b4*
                       m.b58 + 19*m.b4*m.b61 + 20*m.b4*m.b64 + 21*m.b4*m.b67 + 22*m.b4*m.b70 + 23*m.b4*m.b73 + 24*m.b4*
                       m.b76 + 25*m.b4*m.b79 + 26*m.b4*m.b82 + 27*m.b4*m.b85 + 28*m.b4*m.b88 + m.b5*m.b8 + 2*m.b5*m.b11
                        + 3*m.b5*m.b14 + 4*m.b5*m.b17 + 5*m.b5*m.b20 + 6*m.b5*m.b23 + 7*m.b5*m.b26 + 8*m.b5*m.b29 + 9*
                       m.b5*m.b32 + 10*m.b5*m.b35 + 11*m.b5*m.b38 + 12*m.b5*m.b41 + 13*m.b5*m.b44 + 14*m.b5*m.b47 + 15*
                       m.b5*m.b50 + 16*m.b5*m.b53 + 17*m.b5*m.b56 + 18*m.b5*m.b59 + 19*m.b5*m.b62 + 20*m.b5*m.b65 + 21*
                       m.b5*m.b68 + 22*m.b5*m.b71 + 23*m.b5*m.b74 + 24*m.b5*m.b77 + 25*m.b5*m.b80 + 26*m.b5*m.b83 + 27*
                       m.b5*m.b86 + 28*m.b5*m.b89 + m.b6*m.b9 + 2*m.b6*m.b12 + 3*m.b6*m.b15 + 4*m.b6*m.b18 + 5*m.b6*
                       m.b21 + 6*m.b6*m.b24 + 7*m.b6*m.b27 + 8*m.b6*m.b30 + 9*m.b6*m.b33 + 10*m.b6*m.b36 + 11*m.b6*m.b39
                        + 12*m.b6*m.b42 + 13*m.b6*m.b45 + 14*m.b6*m.b48 + 15*m.b6*m.b51 + 16*m.b6*m.b54 + 17*m.b6*m.b57
                        + 18*m.b6*m.b60 + 19*m.b6*m.b63 + 20*m.b6*m.b66 + 21*m.b6*m.b69 + 22*m.b6*m.b72 + 23*m.b6*m.b75
                        + 24*m.b6*m.b78 + 25*m.b6*m.b81 + 26*m.b6*m.b84 + 27*m.b6*m.b87 + 28*m.b6*m.b90 + m.b7*m.b10 + 2
                       *m.b7*m.b13 + 3*m.b7*m.b16 + 4*m.b7*m.b19 + 5*m.b7*m.b22 + 6*m.b7*m.b25 + 7*m.b7*m.b28 + 8*m.b7*
                       m.b31 + 9*m.b7*m.b34 + 10*m.b7*m.b37 + 11*m.b7*m.b40 + 12*m.b7*m.b43 + 13*m.b7*m.b46 + 14*m.b7*
                       m.b49 + 15*m.b7*m.b52 + 16*m.b7*m.b55 + 17*m.b7*m.b58 + 18*m.b7*m.b61 + 19*m.b7*m.b64 + 20*m.b7*
                       m.b67 + 21*m.b7*m.b70 + 22*m.b7*m.b73 + 23*m.b7*m.b76 + 24*m.b7*m.b79 + 25*m.b7*m.b82 + 26*m.b7*
                       m.b85 + 27*m.b7*m.b88 + m.b8*m.b11 + 2*m.b8*m.b14 + 3*m.b8*m.b17 + 4*m.b8*m.b20 + 5*m.b8*m.b23 + 
                       6*m.b8*m.b26 + 7*m.b8*m.b29 + 8*m.b8*m.b32 + 9*m.b8*m.b35 + 10*m.b8*m.b38 + 11*m.b8*m.b41 + 12*
                       m.b8*m.b44 + 13*m.b8*m.b47 + 14*m.b8*m.b50 + 15*m.b8*m.b53 + 16*m.b8*m.b56 + 17*m.b8*m.b59 + 18*
                       m.b8*m.b62 + 19*m.b8*m.b65 + 20*m.b8*m.b68 + 21*m.b8*m.b71 + 22*m.b8*m.b74 + 23*m.b8*m.b77 + 24*
                       m.b8*m.b80 + 25*m.b8*m.b83 + 26*m.b8*m.b86 + 27*m.b8*m.b89 + m.b9*m.b12 + 2*m.b9*m.b15 + 3*m.b9*
                       m.b18 + 4*m.b9*m.b21 + 5*m.b9*m.b24 + 6*m.b9*m.b27 + 7*m.b9*m.b30 + 8*m.b9*m.b33 + 9*m.b9*m.b36
                        + 10*m.b9*m.b39 + 11*m.b9*m.b42 + 12*m.b9*m.b45 + 13*m.b9*m.b48 + 14*m.b9*m.b51 + 15*m.b9*m.b54
                        + 16*m.b9*m.b57 + 17*m.b9*m.b60 + 18*m.b9*m.b63 + 19*m.b9*m.b66 + 20*m.b9*m.b69 + 21*m.b9*m.b72
                        + 22*m.b9*m.b75 + 23*m.b9*m.b78 + 24*m.b9*m.b81 + 25*m.b9*m.b84 + 26*m.b9*m.b87 + 27*m.b9*m.b90
                        + m.b10*m.b13 + 2*m.b10*m.b16 + 3*m.b10*m.b19 + 4*m.b10*m.b22 + 5*m.b10*m.b25 + 6*m.b10*m.b28 + 
                       7*m.b10*m.b31 + 8*m.b10*m.b34 + 9*m.b10*m.b37 + 10*m.b10*m.b40 + 11*m.b10*m.b43 + 12*m.b10*m.b46
                        + 13*m.b10*m.b49 + 14*m.b10*m.b52 + 15*m.b10*m.b55 + 16*m.b10*m.b58 + 17*m.b10*m.b61 + 18*m.b10*
                       m.b64 + 19*m.b10*m.b67 + 20*m.b10*m.b70 + 21*m.b10*m.b73 + 22*m.b10*m.b76 + 23*m.b10*m.b79 + 24*
                       m.b10*m.b82 + 25*m.b10*m.b85 + 26*m.b10*m.b88 + m.b11*m.b14 + 2*m.b11*m.b17 + 3*m.b11*m.b20 + 4*
                       m.b11*m.b23 + 5*m.b11*m.b26 + 6*m.b11*m.b29 + 7*m.b11*m.b32 + 8*m.b11*m.b35 + 9*m.b11*m.b38 + 10*
                       m.b11*m.b41 + 11*m.b11*m.b44 + 12*m.b11*m.b47 + 13*m.b11*m.b50 + 14*m.b11*m.b53 + 15*m.b11*m.b56
                        + 16*m.b11*m.b59 + 17*m.b11*m.b62 + 18*m.b11*m.b65 + 19*m.b11*m.b68 + 20*m.b11*m.b71 + 21*m.b11*
                       m.b74 + 22*m.b11*m.b77 + 23*m.b11*m.b80 + 24*m.b11*m.b83 + 25*m.b11*m.b86 + 26*m.b11*m.b89 + 
                       m.b12*m.b15 + 2*m.b12*m.b18 + 3*m.b12*m.b21 + 4*m.b12*m.b24 + 5*m.b12*m.b27 + 6*m.b12*m.b30 + 7*
                       m.b12*m.b33 + 8*m.b12*m.b36 + 9*m.b12*m.b39 + 10*m.b12*m.b42 + 11*m.b12*m.b45 + 12*m.b12*m.b48 + 
                       13*m.b12*m.b51 + 14*m.b12*m.b54 + 15*m.b12*m.b57 + 16*m.b12*m.b60 + 17*m.b12*m.b63 + 18*m.b12*
                       m.b66 + 19*m.b12*m.b69 + 20*m.b12*m.b72 + 21*m.b12*m.b75 + 22*m.b12*m.b78 + 23*m.b12*m.b81 + 24*
                       m.b12*m.b84 + 25*m.b12*m.b87 + 26*m.b12*m.b90 + m.b13*m.b16 + 2*m.b13*m.b19 + 3*m.b13*m.b22 + 4*
                       m.b13*m.b25 + 5*m.b13*m.b28 + 6*m.b13*m.b31 + 7*m.b13*m.b34 + 8*m.b13*m.b37 + 9*m.b13*m.b40 + 10*
                       m.b13*m.b43 + 11*m.b13*m.b46 + 12*m.b13*m.b49 + 13*m.b13*m.b52 + 14*m.b13*m.b55 + 15*m.b13*m.b58
                        + 16*m.b13*m.b61 + 17*m.b13*m.b64 + 18*m.b13*m.b67 + 19*m.b13*m.b70 + 20*m.b13*m.b73 + 21*m.b13*
                       m.b76 + 22*m.b13*m.b79 + 23*m.b13*m.b82 + 24*m.b13*m.b85 + 25*m.b13*m.b88 + m.b14*m.b17 + 2*m.b14
                       *m.b20 + 3*m.b14*m.b23 + 4*m.b14*m.b26 + 5*m.b14*m.b29 + 6*m.b14*m.b32 + 7*m.b14*m.b35 + 8*m.b14*
                       m.b38 + 9*m.b14*m.b41 + 10*m.b14*m.b44 + 11*m.b14*m.b47 + 12*m.b14*m.b50 + 13*m.b14*m.b53 + 14*
                       m.b14*m.b56 + 15*m.b14*m.b59 + 16*m.b14*m.b62 + 17*m.b14*m.b65 + 18*m.b14*m.b68 + 19*m.b14*m.b71
                        + 20*m.b14*m.b74 + 21*m.b14*m.b77 + 22*m.b14*m.b80 + 23*m.b14*m.b83 + 24*m.b14*m.b86 + 25*m.b14*
                       m.b89 + m.b15*m.b18 + 2*m.b15*m.b21 + 3*m.b15*m.b24 + 4*m.b15*m.b27 + 5*m.b15*m.b30 + 6*m.b15*
                       m.b33 + 7*m.b15*m.b36 + 8*m.b15*m.b39 + 9*m.b15*m.b42 + 10*m.b15*m.b45 + 11*m.b15*m.b48 + 12*
                       m.b15*m.b51 + 13*m.b15*m.b54 + 14*m.b15*m.b57 + 15*m.b15*m.b60 + 16*m.b15*m.b63 + 17*m.b15*m.b66
                        + 18*m.b15*m.b69 + 19*m.b15*m.b72 + 20*m.b15*m.b75 + 21*m.b15*m.b78 + 22*m.b15*m.b81 + 23*m.b15*
                       m.b84 + 24*m.b15*m.b87 + 25*m.b15*m.b90 + m.b16*m.b19 + 2*m.b16*m.b22 + 3*m.b16*m.b25 + 4*m.b16*
                       m.b28 + 5*m.b16*m.b31 + 6*m.b16*m.b34 + 7*m.b16*m.b37 + 8*m.b16*m.b40 + 9*m.b16*m.b43 + 10*m.b16*
                       m.b46 + 11*m.b16*m.b49 + 12*m.b16*m.b52 + 13*m.b16*m.b55 + 14*m.b16*m.b58 + 15*m.b16*m.b61 + 16*
                       m.b16*m.b64 + 17*m.b16*m.b67 + 18*m.b16*m.b70 + 19*m.b16*m.b73 + 20*m.b16*m.b76 + 21*m.b16*m.b79
                        + 22*m.b16*m.b82 + 23*m.b16*m.b85 + 24*m.b16*m.b88 + m.b17*m.b20 + 2*m.b17*m.b23 + 3*m.b17*m.b26
                        + 4*m.b17*m.b29 + 5*m.b17*m.b32 + 6*m.b17*m.b35 + 7*m.b17*m.b38 + 8*m.b17*m.b41 + 9*m.b17*m.b44
                        + 10*m.b17*m.b47 + 11*m.b17*m.b50 + 12*m.b17*m.b53 + 13*m.b17*m.b56 + 14*m.b17*m.b59 + 15*m.b17*
                       m.b62 + 16*m.b17*m.b65 + 17*m.b17*m.b68 + 18*m.b17*m.b71 + 19*m.b17*m.b74 + 20*m.b17*m.b77 + 21*
                       m.b17*m.b80 + 22*m.b17*m.b83 + 23*m.b17*m.b86 + 24*m.b17*m.b89 + m.b18*m.b21 + 2*m.b18*m.b24 + 3*
                       m.b18*m.b27 + 4*m.b18*m.b30 + 5*m.b18*m.b33 + 6*m.b18*m.b36 + 7*m.b18*m.b39 + 8*m.b18*m.b42 + 9*
                       m.b18*m.b45 + 10*m.b18*m.b48 + 11*m.b18*m.b51 + 12*m.b18*m.b54 + 13*m.b18*m.b57 + 14*m.b18*m.b60
                        + 15*m.b18*m.b63 + 16*m.b18*m.b66 + 17*m.b18*m.b69 + 18*m.b18*m.b72 + 19*m.b18*m.b75 + 20*m.b18*
                       m.b78 + 21*m.b18*m.b81 + 22*m.b18*m.b84 + 23*m.b18*m.b87 + 24*m.b18*m.b90 + m.b19*m.b22 + 2*m.b19
                       *m.b25 + 3*m.b19*m.b28 + 4*m.b19*m.b31 + 5*m.b19*m.b34 + 6*m.b19*m.b37 + 7*m.b19*m.b40 + 8*m.b19*
                       m.b43 + 9*m.b19*m.b46 + 10*m.b19*m.b49 + 11*m.b19*m.b52 + 12*m.b19*m.b55 + 13*m.b19*m.b58 + 14*
                       m.b19*m.b61 + 15*m.b19*m.b64 + 16*m.b19*m.b67 + 17*m.b19*m.b70 + 18*m.b19*m.b73 + 19*m.b19*m.b76
                        + 20*m.b19*m.b79 + 21*m.b19*m.b82 + 22*m.b19*m.b85 + 23*m.b19*m.b88 + m.b20*m.b23 + 2*m.b20*
                       m.b26 + 3*m.b20*m.b29 + 4*m.b20*m.b32 + 5*m.b20*m.b35 + 6*m.b20*m.b38 + 7*m.b20*m.b41 + 8*m.b20*
                       m.b44 + 9*m.b20*m.b47 + 10*m.b20*m.b50 + 11*m.b20*m.b53 + 12*m.b20*m.b56 + 13*m.b20*m.b59 + 14*
                       m.b20*m.b62 + 15*m.b20*m.b65 + 16*m.b20*m.b68 + 17*m.b20*m.b71 + 18*m.b20*m.b74 + 19*m.b20*m.b77
                        + 20*m.b20*m.b80 + 21*m.b20*m.b83 + 22*m.b20*m.b86 + 23*m.b20*m.b89 + m.b21*m.b24 + 2*m.b21*
                       m.b27 + 3*m.b21*m.b30 + 4*m.b21*m.b33 + 5*m.b21*m.b36 + 6*m.b21*m.b39 + 7*m.b21*m.b42 + 8*m.b21*
                       m.b45 + 9*m.b21*m.b48 + 10*m.b21*m.b51 + 11*m.b21*m.b54 + 12*m.b21*m.b57 + 13*m.b21*m.b60 + 14*
                       m.b21*m.b63 + 15*m.b21*m.b66 + 16*m.b21*m.b69 + 17*m.b21*m.b72 + 18*m.b21*m.b75 + 19*m.b21*m.b78
                        + 20*m.b21*m.b81 + 21*m.b21*m.b84 + 22*m.b21*m.b87 + 23*m.b21*m.b90 + m.b22*m.b25 + 2*m.b22*
                       m.b28 + 3*m.b22*m.b31 + 4*m.b22*m.b34 + 5*m.b22*m.b37 + 6*m.b22*m.b40 + 7*m.b22*m.b43 + 8*m.b22*
                       m.b46 + 9*m.b22*m.b49 + 10*m.b22*m.b52 + 11*m.b22*m.b55 + 12*m.b22*m.b58 + 13*m.b22*m.b61 + 14*
                       m.b22*m.b64 + 15*m.b22*m.b67 + 16*m.b22*m.b70 + 17*m.b22*m.b73 + 18*m.b22*m.b76 + 19*m.b22*m.b79
                        + 20*m.b22*m.b82 + 21*m.b22*m.b85 + 22*m.b22*m.b88 + m.b23*m.b26 + 2*m.b23*m.b29 + 3*m.b23*m.b32
                        + 4*m.b23*m.b35 + 5*m.b23*m.b38 + 6*m.b23*m.b41 + 7*m.b23*m.b44 + 8*m.b23*m.b47 + 9*m.b23*m.b50
                        + 10*m.b23*m.b53 + 11*m.b23*m.b56 + 12*m.b23*m.b59 + 13*m.b23*m.b62 + 14*m.b23*m.b65 + 15*m.b23*
                       m.b68 + 16*m.b23*m.b71 + 17*m.b23*m.b74 + 18*m.b23*m.b77 + 19*m.b23*m.b80 + 20*m.b23*m.b83 + 21*
                       m.b23*m.b86 + 22*m.b23*m.b89 + m.b24*m.b27 + 2*m.b24*m.b30 + 3*m.b24*m.b33 + 4*m.b24*m.b36 + 5*
                       m.b24*m.b39 + 6*m.b24*m.b42 + 7*m.b24*m.b45 + 8*m.b24*m.b48 + 9*m.b24*m.b51 + 10*m.b24*m.b54 + 11
                       *m.b24*m.b57 + 12*m.b24*m.b60 + 13*m.b24*m.b63 + 14*m.b24*m.b66 + 15*m.b24*m.b69 + 16*m.b24*m.b72
                        + 17*m.b24*m.b75 + 18*m.b24*m.b78 + 19*m.b24*m.b81 + 20*m.b24*m.b84 + 21*m.b24*m.b87 + 22*m.b24*
                       m.b90 + m.b25*m.b28 + 2*m.b25*m.b31 + 3*m.b25*m.b34 + 4*m.b25*m.b37 + 5*m.b25*m.b40 + 6*m.b25*
                       m.b43 + 7*m.b25*m.b46 + 8*m.b25*m.b49 + 9*m.b25*m.b52 + 10*m.b25*m.b55 + 11*m.b25*m.b58 + 12*
                       m.b25*m.b61 + 13*m.b25*m.b64 + 14*m.b25*m.b67 + 15*m.b25*m.b70 + 16*m.b25*m.b73 + 17*m.b25*m.b76
                        + 18*m.b25*m.b79 + 19*m.b25*m.b82 + 20*m.b25*m.b85 + 21*m.b25*m.b88 + m.b26*m.b29 + 2*m.b26*
                       m.b32 + 3*m.b26*m.b35 + 4*m.b26*m.b38 + 5*m.b26*m.b41 + 6*m.b26*m.b44 + 7*m.b26*m.b47 + 8*m.b26*
                       m.b50 + 9*m.b26*m.b53 + 10*m.b26*m.b56 + 11*m.b26*m.b59 + 12*m.b26*m.b62 + 13*m.b26*m.b65 + 14*
                       m.b26*m.b68 + 15*m.b26*m.b71 + 16*m.b26*m.b74 + 17*m.b26*m.b77 + 18*m.b26*m.b80 + 19*m.b26*m.b83
                        + 20*m.b26*m.b86 + 21*m.b26*m.b89 + m.b27*m.b30 + 2*m.b27*m.b33 + 3*m.b27*m.b36 + 4*m.b27*m.b39
                        + 5*m.b27*m.b42 + 6*m.b27*m.b45 + 7*m.b27*m.b48 + 8*m.b27*m.b51 + 9*m.b27*m.b54 + 10*m.b27*m.b57
                        + 11*m.b27*m.b60 + 12*m.b27*m.b63 + 13*m.b27*m.b66 + 14*m.b27*m.b69 + 15*m.b27*m.b72 + 16*m.b27*
                       m.b75 + 17*m.b27*m.b78 + 18*m.b27*m.b81 + 19*m.b27*m.b84 + 20*m.b27*m.b87 + 21*m.b27*m.b90 + 
                       m.b28*m.b31 + 2*m.b28*m.b34 + 3*m.b28*m.b37 + 4*m.b28*m.b40 + 5*m.b28*m.b43 + 6*m.b28*m.b46 + 7*
                       m.b28*m.b49 + 8*m.b28*m.b52 + 9*m.b28*m.b55 + 10*m.b28*m.b58 + 11*m.b28*m.b61 + 12*m.b28*m.b64 + 
                       13*m.b28*m.b67 + 14*m.b28*m.b70 + 15*m.b28*m.b73 + 16*m.b28*m.b76 + 17*m.b28*m.b79 + 18*m.b28*
                       m.b82 + 19*m.b28*m.b85 + 20*m.b28*m.b88 + m.b29*m.b32 + 2*m.b29*m.b35 + 3*m.b29*m.b38 + 4*m.b29*
                       m.b41 + 5*m.b29*m.b44 + 6*m.b29*m.b47 + 7*m.b29*m.b50 + 8*m.b29*m.b53 + 9*m.b29*m.b56 + 10*m.b29*
                       m.b59 + 11*m.b29*m.b62 + 12*m.b29*m.b65 + 13*m.b29*m.b68 + 14*m.b29*m.b71 + 15*m.b29*m.b74 + 16*
                       m.b29*m.b77 + 17*m.b29*m.b80 + 18*m.b29*m.b83 + 19*m.b29*m.b86 + 20*m.b29*m.b89 + m.b30*m.b33 + 2
                       *m.b30*m.b36 + 3*m.b30*m.b39 + 4*m.b30*m.b42 + 5*m.b30*m.b45 + 6*m.b30*m.b48 + 7*m.b30*m.b51 + 8*
                       m.b30*m.b54 + 9*m.b30*m.b57 + 10*m.b30*m.b60 + 11*m.b30*m.b63 + 12*m.b30*m.b66 + 13*m.b30*m.b69
                        + 14*m.b30*m.b72 + 15*m.b30*m.b75 + 16*m.b30*m.b78 + 17*m.b30*m.b81 + 18*m.b30*m.b84 + 19*m.b30*
                       m.b87 + 20*m.b30*m.b90 + m.b31*m.b34 + 2*m.b31*m.b37 + 3*m.b31*m.b40 + 4*m.b31*m.b43 + 5*m.b31*
                       m.b46 + 6*m.b31*m.b49 + 7*m.b31*m.b52 + 8*m.b31*m.b55 + 9*m.b31*m.b58 + 10*m.b31*m.b61 + 11*m.b31
                       *m.b64 + 12*m.b31*m.b67 + 13*m.b31*m.b70 + 14*m.b31*m.b73 + 15*m.b31*m.b76 + 16*m.b31*m.b79 + 17*
                       m.b31*m.b82 + 18*m.b31*m.b85 + 19*m.b31*m.b88 + m.b32*m.b35 + 2*m.b32*m.b38 + 3*m.b32*m.b41 + 4*
                       m.b32*m.b44 + 5*m.b32*m.b47 + 6*m.b32*m.b50 + 7*m.b32*m.b53 + 8*m.b32*m.b56 + 9*m.b32*m.b59 + 10*
                       m.b32*m.b62 + 11*m.b32*m.b65 + 12*m.b32*m.b68 + 13*m.b32*m.b71 + 14*m.b32*m.b74 + 15*m.b32*m.b77
                        + 16*m.b32*m.b80 + 17*m.b32*m.b83 + 18*m.b32*m.b86 + 19*m.b32*m.b89 + m.b33*m.b36 + 2*m.b33*
                       m.b39 + 3*m.b33*m.b42 + 4*m.b33*m.b45 + 5*m.b33*m.b48 + 6*m.b33*m.b51 + 7*m.b33*m.b54 + 8*m.b33*
                       m.b57 + 9*m.b33*m.b60 + 10*m.b33*m.b63 + 11*m.b33*m.b66 + 12*m.b33*m.b69 + 13*m.b33*m.b72 + 14*
                       m.b33*m.b75 + 15*m.b33*m.b78 + 16*m.b33*m.b81 + 17*m.b33*m.b84 + 18*m.b33*m.b87 + 19*m.b33*m.b90
                        + m.b34*m.b37 + 2*m.b34*m.b40 + 3*m.b34*m.b43 + 4*m.b34*m.b46 + 5*m.b34*m.b49 + 6*m.b34*m.b52 + 
                       7*m.b34*m.b55 + 8*m.b34*m.b58 + 9*m.b34*m.b61 + 10*m.b34*m.b64 + 11*m.b34*m.b67 + 12*m.b34*m.b70
                        + 13*m.b34*m.b73 + 14*m.b34*m.b76 + 15*m.b34*m.b79 + 16*m.b34*m.b82 + 17*m.b34*m.b85 + 18*m.b34*
                       m.b88 + m.b35*m.b38 + 2*m.b35*m.b41 + 3*m.b35*m.b44 + 4*m.b35*m.b47 + 5*m.b35*m.b50 + 6*m.b35*
                       m.b53 + 7*m.b35*m.b56 + 8*m.b35*m.b59 + 9*m.b35*m.b62 + 10*m.b35*m.b65 + 11*m.b35*m.b68 + 12*
                       m.b35*m.b71 + 13*m.b35*m.b74 + 14*m.b35*m.b77 + 15*m.b35*m.b80 + 16*m.b35*m.b83 + 17*m.b35*m.b86
                        + 18*m.b35*m.b89 + m.b36*m.b39 + 2*m.b36*m.b42 + 3*m.b36*m.b45 + 4*m.b36*m.b48 + 5*m.b36*m.b51
                        + 6*m.b36*m.b54 + 7*m.b36*m.b57 + 8*m.b36*m.b60 + 9*m.b36*m.b63 + 10*m.b36*m.b66 + 11*m.b36*
                       m.b69 + 12*m.b36*m.b72 + 13*m.b36*m.b75 + 14*m.b36*m.b78 + 15*m.b36*m.b81 + 16*m.b36*m.b84 + 17*
                       m.b36*m.b87 + 18*m.b36*m.b90 + m.b37*m.b40 + 2*m.b37*m.b43 + 3*m.b37*m.b46 + 4*m.b37*m.b49 + 5*
                       m.b37*m.b52 + 6*m.b37*m.b55 + 7*m.b37*m.b58 + 8*m.b37*m.b61 + 9*m.b37*m.b64 + 10*m.b37*m.b67 + 11
                       *m.b37*m.b70 + 12*m.b37*m.b73 + 13*m.b37*m.b76 + 14*m.b37*m.b79 + 15*m.b37*m.b82 + 16*m.b37*m.b85
                        + 17*m.b37*m.b88 + m.b38*m.b41 + 2*m.b38*m.b44 + 3*m.b38*m.b47 + 4*m.b38*m.b50 + 5*m.b38*m.b53
                        + 6*m.b38*m.b56 + 7*m.b38*m.b59 + 8*m.b38*m.b62 + 9*m.b38*m.b65 + 10*m.b38*m.b68 + 11*m.b38*
                       m.b71 + 12*m.b38*m.b74 + 13*m.b38*m.b77 + 14*m.b38*m.b80 + 15*m.b38*m.b83 + 16*m.b38*m.b86 + 17*
                       m.b38*m.b89 + m.b39*m.b42 + 2*m.b39*m.b45 + 3*m.b39*m.b48 + 4*m.b39*m.b51 + 5*m.b39*m.b54 + 6*
                       m.b39*m.b57 + 7*m.b39*m.b60 + 8*m.b39*m.b63 + 9*m.b39*m.b66 + 10*m.b39*m.b69 + 11*m.b39*m.b72 + 
                       12*m.b39*m.b75 + 13*m.b39*m.b78 + 14*m.b39*m.b81 + 15*m.b39*m.b84 + 16*m.b39*m.b87 + 17*m.b39*
                       m.b90 + m.b40*m.b43 + 2*m.b40*m.b46 + 3*m.b40*m.b49 + 4*m.b40*m.b52 + 5*m.b40*m.b55 + 6*m.b40*
                       m.b58 + 7*m.b40*m.b61 + 8*m.b40*m.b64 + 9*m.b40*m.b67 + 10*m.b40*m.b70 + 11*m.b40*m.b73 + 12*
                       m.b40*m.b76 + 13*m.b40*m.b79 + 14*m.b40*m.b82 + 15*m.b40*m.b85 + 16*m.b40*m.b88 + m.b41*m.b44 + 2
                       *m.b41*m.b47 + 3*m.b41*m.b50 + 4*m.b41*m.b53 + 5*m.b41*m.b56 + 6*m.b41*m.b59 + 7*m.b41*m.b62 + 8*
                       m.b41*m.b65 + 9*m.b41*m.b68 + 10*m.b41*m.b71 + 11*m.b41*m.b74 + 12*m.b41*m.b77 + 13*m.b41*m.b80
                        + 14*m.b41*m.b83 + 15*m.b41*m.b86 + 16*m.b41*m.b89 + m.b42*m.b45 + 2*m.b42*m.b48 + 3*m.b42*m.b51
                        + 4*m.b42*m.b54 + 5*m.b42*m.b57 + 6*m.b42*m.b60 + 7*m.b42*m.b63 + 8*m.b42*m.b66 + 9*m.b42*m.b69
                        + 10*m.b42*m.b72 + 11*m.b42*m.b75 + 12*m.b42*m.b78 + 13*m.b42*m.b81 + 14*m.b42*m.b84 + 15*m.b42*
                       m.b87 + 16*m.b42*m.b90 + m.b43*m.b46 + 2*m.b43*m.b49 + 3*m.b43*m.b52 + 4*m.b43*m.b55 + 5*m.b43*
                       m.b58 + 6*m.b43*m.b61 + 7*m.b43*m.b64 + 8*m.b43*m.b67 + 9*m.b43*m.b70 + 10*m.b43*m.b73 + 11*m.b43
                       *m.b76 + 12*m.b43*m.b79 + 13*m.b43*m.b82 + 14*m.b43*m.b85 + 15*m.b43*m.b88 + m.b44*m.b47 + 2*
                       m.b44*m.b50 + 3*m.b44*m.b53 + 4*m.b44*m.b56 + 5*m.b44*m.b59 + 6*m.b44*m.b62 + 7*m.b44*m.b65 + 8*
                       m.b44*m.b68 + 9*m.b44*m.b71 + 10*m.b44*m.b74 + 11*m.b44*m.b77 + 12*m.b44*m.b80 + 13*m.b44*m.b83
                        + 14*m.b44*m.b86 + 15*m.b44*m.b89 + m.b45*m.b48 + 2*m.b45*m.b51 + 3*m.b45*m.b54 + 4*m.b45*m.b57
                        + 5*m.b45*m.b60 + 6*m.b45*m.b63 + 7*m.b45*m.b66 + 8*m.b45*m.b69 + 9*m.b45*m.b72 + 10*m.b45*m.b75
                        + 11*m.b45*m.b78 + 12*m.b45*m.b81 + 13*m.b45*m.b84 + 14*m.b45*m.b87 + 15*m.b45*m.b90 + m.b46*
                       m.b49 + 2*m.b46*m.b52 + 3*m.b46*m.b55 + 4*m.b46*m.b58 + 5*m.b46*m.b61 + 6*m.b46*m.b64 + 7*m.b46*
                       m.b67 + 8*m.b46*m.b70 + 9*m.b46*m.b73 + 10*m.b46*m.b76 + 11*m.b46*m.b79 + 12*m.b46*m.b82 + 13*
                       m.b46*m.b85 + 14*m.b46*m.b88 + m.b47*m.b50 + 2*m.b47*m.b53 + 3*m.b47*m.b56 + 4*m.b47*m.b59 + 5*
                       m.b47*m.b62 + 6*m.b47*m.b65 + 7*m.b47*m.b68 + 8*m.b47*m.b71 + 9*m.b47*m.b74 + 10*m.b47*m.b77 + 11
                       *m.b47*m.b80 + 12*m.b47*m.b83 + 13*m.b47*m.b86 + 14*m.b47*m.b89 + m.b48*m.b51 + 2*m.b48*m.b54 + 3
                       *m.b48*m.b57 + 4*m.b48*m.b60 + 5*m.b48*m.b63 + 6*m.b48*m.b66 + 7*m.b48*m.b69 + 8*m.b48*m.b72 + 9*
                       m.b48*m.b75 + 10*m.b48*m.b78 + 11*m.b48*m.b81 + 12*m.b48*m.b84 + 13*m.b48*m.b87 + 14*m.b48*m.b90
                        + m.b49*m.b52 + 2*m.b49*m.b55 + 3*m.b49*m.b58 + 4*m.b49*m.b61 + 5*m.b49*m.b64 + 6*m.b49*m.b67 + 
                       7*m.b49*m.b70 + 8*m.b49*m.b73 + 9*m.b49*m.b76 + 10*m.b49*m.b79 + 11*m.b49*m.b82 + 12*m.b49*m.b85
                        + 13*m.b49*m.b88 + m.b50*m.b53 + 2*m.b50*m.b56 + 3*m.b50*m.b59 + 4*m.b50*m.b62 + 5*m.b50*m.b65
                        + 6*m.b50*m.b68 + 7*m.b50*m.b71 + 8*m.b50*m.b74 + 9*m.b50*m.b77 + 10*m.b50*m.b80 + 11*m.b50*
                       m.b83 + 12*m.b50*m.b86 + 13*m.b50*m.b89 + m.b51*m.b54 + 2*m.b51*m.b57 + 3*m.b51*m.b60 + 4*m.b51*
                       m.b63 + 5*m.b51*m.b66 + 6*m.b51*m.b69 + 7*m.b51*m.b72 + 8*m.b51*m.b75 + 9*m.b51*m.b78 + 10*m.b51*
                       m.b81 + 11*m.b51*m.b84 + 12*m.b51*m.b87 + 13*m.b51*m.b90 + m.b52*m.b55 + 2*m.b52*m.b58 + 3*m.b52*
                       m.b61 + 4*m.b52*m.b64 + 5*m.b52*m.b67 + 6*m.b52*m.b70 + 7*m.b52*m.b73 + 8*m.b52*m.b76 + 9*m.b52*
                       m.b79 + 10*m.b52*m.b82 + 11*m.b52*m.b85 + 12*m.b52*m.b88 + m.b53*m.b56 + 2*m.b53*m.b59 + 3*m.b53*
                       m.b62 + 4*m.b53*m.b65 + 5*m.b53*m.b68 + 6*m.b53*m.b71 + 7*m.b53*m.b74 + 8*m.b53*m.b77 + 9*m.b53*
                       m.b80 + 10*m.b53*m.b83 + 11*m.b53*m.b86 + 12*m.b53*m.b89 + m.b54*m.b57 + 2*m.b54*m.b60 + 3*m.b54*
                       m.b63 + 4*m.b54*m.b66 + 5*m.b54*m.b69 + 6*m.b54*m.b72 + 7*m.b54*m.b75 + 8*m.b54*m.b78 + 9*m.b54*
                       m.b81 + 10*m.b54*m.b84 + 11*m.b54*m.b87 + 12*m.b54*m.b90 + m.b55*m.b58 + 2*m.b55*m.b61 + 3*m.b55*
                       m.b64 + 4*m.b55*m.b67 + 5*m.b55*m.b70 + 6*m.b55*m.b73 + 7*m.b55*m.b76 + 8*m.b55*m.b79 + 9*m.b55*
                       m.b82 + 10*m.b55*m.b85 + 11*m.b55*m.b88 + m.b56*m.b59 + 2*m.b56*m.b62 + 3*m.b56*m.b65 + 4*m.b56*
                       m.b68 + 5*m.b56*m.b71 + 6*m.b56*m.b74 + 7*m.b56*m.b77 + 8*m.b56*m.b80 + 9*m.b56*m.b83 + 10*m.b56*
                       m.b86 + 11*m.b56*m.b89 + m.b57*m.b60 + 2*m.b57*m.b63 + 3*m.b57*m.b66 + 4*m.b57*m.b69 + 5*m.b57*
                       m.b72 + 6*m.b57*m.b75 + 7*m.b57*m.b78 + 8*m.b57*m.b81 + 9*m.b57*m.b84 + 10*m.b57*m.b87 + 11*m.b57
                       *m.b90 + m.b58*m.b61 + 2*m.b58*m.b64 + 3*m.b58*m.b67 + 4*m.b58*m.b70 + 5*m.b58*m.b73 + 6*m.b58*
                       m.b76 + 7*m.b58*m.b79 + 8*m.b58*m.b82 + 9*m.b58*m.b85 + 10*m.b58*m.b88 + m.b59*m.b62 + 2*m.b59*
                       m.b65 + 3*m.b59*m.b68 + 4*m.b59*m.b71 + 5*m.b59*m.b74 + 6*m.b59*m.b77 + 7*m.b59*m.b80 + 8*m.b59*
                       m.b83 + 9*m.b59*m.b86 + 10*m.b59*m.b89 + m.b60*m.b63 + 2*m.b60*m.b66 + 3*m.b60*m.b69 + 4*m.b60*
                       m.b72 + 5*m.b60*m.b75 + 6*m.b60*m.b78 + 7*m.b60*m.b81 + 8*m.b60*m.b84 + 9*m.b60*m.b87 + 10*m.b60*
                       m.b90 + m.b61*m.b64 + 2*m.b61*m.b67 + 3*m.b61*m.b70 + 4*m.b61*m.b73 + 5*m.b61*m.b76 + 6*m.b61*
                       m.b79 + 7*m.b61*m.b82 + 8*m.b61*m.b85 + 9*m.b61*m.b88 + m.b62*m.b65 + 2*m.b62*m.b68 + 3*m.b62*
                       m.b71 + 4*m.b62*m.b74 + 5*m.b62*m.b77 + 6*m.b62*m.b80 + 7*m.b62*m.b83 + 8*m.b62*m.b86 + 9*m.b62*
                       m.b89 + m.b63*m.b66 + 2*m.b63*m.b69 + 3*m.b63*m.b72 + 4*m.b63*m.b75 + 5*m.b63*m.b78 + 6*m.b63*
                       m.b81 + 7*m.b63*m.b84 + 8*m.b63*m.b87 + 9*m.b63*m.b90 + m.b64*m.b67 + 2*m.b64*m.b70 + 3*m.b64*
                       m.b73 + 4*m.b64*m.b76 + 5*m.b64*m.b79 + 6*m.b64*m.b82 + 7*m.b64*m.b85 + 8*m.b64*m.b88 + m.b65*
                       m.b68 + 2*m.b65*m.b71 + 3*m.b65*m.b74 + 4*m.b65*m.b77 + 5*m.b65*m.b80 + 6*m.b65*m.b83 + 7*m.b65*
                       m.b86 + 8*m.b65*m.b89 + m.b66*m.b69 + 2*m.b66*m.b72 + 3*m.b66*m.b75 + 4*m.b66*m.b78 + 5*m.b66*
                       m.b81 + 6*m.b66*m.b84 + 7*m.b66*m.b87 + 8*m.b66*m.b90 + m.b67*m.b70 + 2*m.b67*m.b73 + 3*m.b67*
                       m.b76 + 4*m.b67*m.b79 + 5*m.b67*m.b82 + 6*m.b67*m.b85 + 7*m.b67*m.b88 + m.b68*m.b71 + 2*m.b68*
                       m.b74 + 3*m.b68*m.b77 + 4*m.b68*m.b80 + 5*m.b68*m.b83 + 6*m.b68*m.b86 + 7*m.b68*m.b89 + m.b69*
                       m.b72 + 2*m.b69*m.b75 + 3*m.b69*m.b78 + 4*m.b69*m.b81 + 5*m.b69*m.b84 + 6*m.b69*m.b87 + 7*m.b69*
                       m.b90 + m.b70*m.b73 + 2*m.b70*m.b76 + 3*m.b70*m.b79 + 4*m.b70*m.b82 + 5*m.b70*m.b85 + 6*m.b70*
                       m.b88 + m.b71*m.b74 + 2*m.b71*m.b77 + 3*m.b71*m.b80 + 4*m.b71*m.b83 + 5*m.b71*m.b86 + 6*m.b71*
                       m.b89 + m.b72*m.b75 + 2*m.b72*m.b78 + 3*m.b72*m.b81 + 4*m.b72*m.b84 + 5*m.b72*m.b87 + 6*m.b72*
                       m.b90 + m.b73*m.b76 + 2*m.b73*m.b79 + 3*m.b73*m.b82 + 4*m.b73*m.b85 + 5*m.b73*m.b88 + m.b74*m.b77
                        + 2*m.b74*m.b80 + 3*m.b74*m.b83 + 4*m.b74*m.b86 + 5*m.b74*m.b89 + m.b75*m.b78 + 2*m.b75*m.b81 + 
                       3*m.b75*m.b84 + 4*m.b75*m.b87 + 5*m.b75*m.b90 + m.b76*m.b79 + 2*m.b76*m.b82 + 3*m.b76*m.b85 + 4*
                       m.b76*m.b88 + m.b77*m.b80 + 2*m.b77*m.b83 + 3*m.b77*m.b86 + 4*m.b77*m.b89 + m.b78*m.b81 + 2*m.b78
                       *m.b84 + 3*m.b78*m.b87 + 4*m.b78*m.b90 + m.b79*m.b82 + 2*m.b79*m.b85 + 3*m.b79*m.b88 + m.b80*
                       m.b83 + 2*m.b80*m.b86 + 3*m.b80*m.b89 + m.b81*m.b84 + 2*m.b81*m.b87 + 3*m.b81*m.b90 + m.b82*m.b85
                        + 2*m.b82*m.b88 + m.b83*m.b86 + 2*m.b83*m.b89 + m.b84*m.b87 + 2*m.b84*m.b90 + m.b85*m.b88 + 
                       m.b86*m.b89 + m.b87*m.b90, sense=minimize)

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

m.c21 = Constraint(expr=   m.b61 + m.b62 + m.b63 == 1)

m.c22 = Constraint(expr=   m.b64 + m.b65 + m.b66 == 1)

m.c23 = Constraint(expr=   m.b67 + m.b68 + m.b69 == 1)

m.c24 = Constraint(expr=   m.b70 + m.b71 + m.b72 == 1)

m.c25 = Constraint(expr=   m.b73 + m.b74 + m.b75 == 1)

m.c26 = Constraint(expr=   m.b76 + m.b77 + m.b78 == 1)

m.c27 = Constraint(expr=   m.b79 + m.b80 + m.b81 == 1)

m.c28 = Constraint(expr=   m.b82 + m.b83 + m.b84 == 1)

m.c29 = Constraint(expr=   m.b85 + m.b86 + m.b87 == 1)

m.c30 = Constraint(expr=   m.b88 + m.b89 + m.b90 == 1)

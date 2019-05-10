#  MINLP written by GAMS Convert at 05/10/19 14:22:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1020       21      689      310        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        279      150      129        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2866     2817       49        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x2 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x3 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x4 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x5 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x6 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x7 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x8 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x9 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x10 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x11 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x12 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x13 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x14 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x15 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x16 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x17 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x18 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x19 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x20 = Var(within=Reals,bounds=(3.79423996977176,6.35222947629824),initialize=3.79423996977176)
m.x21 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x22 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x23 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x24 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x25 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x26 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x27 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x28 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x29 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x30 = Var(within=Reals,bounds=(3.29891853254174,6.93674281585539),initialize=3.29891853254174)
m.x31 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x32 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x33 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x34 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x35 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x36 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x37 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x38 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x39 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x40 = Var(within=Reals,bounds=(3.44998754583159,6.70190322477799),initialize=3.44998754583159)
m.x41 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x42 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x43 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x44 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x45 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x46 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x47 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x48 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x49 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x50 = Var(within=Reals,bounds=(3.31620416882876,6.40266032992513),initialize=3.31620416882876)
m.x51 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x52 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x53 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x54 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x55 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x56 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x57 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x58 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x59 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x60 = Var(within=Reals,bounds=(2.83321334405622,6.65644085070123),initialize=2.83321334405622)
m.x61 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x62 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x63 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x64 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x65 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x66 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x67 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x68 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x69 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x70 = Var(within=Reals,bounds=(2.69500248570973,6.65644085070123),initialize=2.69500248570973)
m.x71 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x72 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x73 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x74 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x75 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x76 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x77 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x78 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x79 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x80 = Var(within=Reals,bounds=(3.5656126601013,6.51185962189012),initialize=3.5656126601013)
m.x81 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x82 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x83 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x84 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x85 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x86 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x87 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x88 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x89 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x90 = Var(within=Reals,bounds=(3.16641225533246,6.49281142691943),initialize=3.16641225533246)
m.x91 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x92 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x93 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x94 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x95 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x96 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x97 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x98 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x99 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x100 = Var(within=Reals,bounds=(3.54136181951467,6.51185962189012),initialize=3.54136181951467)
m.x101 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x102 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x103 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x104 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x105 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x106 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x107 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x108 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x109 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x110 = Var(within=Reals,bounds=(3.3489289531164,6.33596895542646),initialize=3.3489289531164)
m.x111 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,1.79175946922805),initialize=0)
m.x132 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x133 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x134 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x135 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x136 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x137 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x138 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x139 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x140 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=4.60517018598809)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=250*(exp(0.6*m.x1 + m.x111 + m.x121) + exp(0.6*m.x2 + m.x112 + m.x122) + exp(0.6*m.x3 + m.x113 + 
                       m.x123) + exp(0.6*m.x4 + m.x114 + m.x124) + exp(0.6*m.x5 + m.x115 + m.x125) + exp(0.6*m.x6 + 
                       m.x116 + m.x126) + exp(0.6*m.x7 + m.x117 + m.x127) + exp(0.6*m.x8 + m.x118 + m.x128) + exp(0.6*
                       m.x9 + m.x119 + m.x129) + exp(0.6*m.x10 + m.x120 + m.x130)) + 150*(exp(0.5*m.x132) + exp(0.5*
                       m.x133) + exp(0.5*m.x134) + exp(0.5*m.x135) + exp(0.5*m.x136) + exp(0.5*m.x137) + exp(0.5*m.x138)
                        + exp(0.5*m.x139) + exp(0.5*m.x140)), sense=minimize)

m.c1 = Constraint(expr=   m.x1 - m.x11 + m.x111 >= 1.06471073699243)

m.c2 = Constraint(expr=   m.x2 - m.x12 + m.x112 >= 0.693147180559945)

m.c3 = Constraint(expr=   m.x3 - m.x13 + m.x113 >= 1.64865862558738)

m.c4 = Constraint(expr=   m.x4 - m.x14 + m.x114 >= 1.58923520511658)

m.c5 = Constraint(expr=   m.x5 - m.x15 + m.x115 >= 1.80828877117927)

m.c6 = Constraint(expr=   m.x6 - m.x16 + m.x116 >= 1.43508452528932)

m.c7 = Constraint(expr=   m.x7 - m.x17 + m.x117 >= 1.6094379124341)

m.c8 = Constraint(expr=   m.x8 - m.x18 + m.x118 >= 0.0953101798043249)

m.c9 = Constraint(expr=   m.x9 - m.x19 + m.x119 >= 1.16315080980568)

m.c10 = Constraint(expr=   m.x10 - m.x20 + m.x120 >= 1.50407739677627)

m.c11 = Constraint(expr=   m.x1 - m.x21 + m.x111 >= -0.22314355131421)

m.c12 = Constraint(expr=   m.x2 - m.x22 + m.x112 >= -0.22314355131421)

m.c13 = Constraint(expr=   m.x3 - m.x23 + m.x113 >= -0.105360515657826)

m.c14 = Constraint(expr=   m.x4 - m.x24 + m.x114 >= 1.22377543162212)

m.c15 = Constraint(expr=   m.x5 - m.x25 + m.x115 >= 0.741937344729377)

m.c16 = Constraint(expr=   m.x6 - m.x26 + m.x116 >= 0.916290731874155)

m.c17 = Constraint(expr=   m.x7 - m.x27 + m.x117 >= -0.105360515657826)

m.c18 = Constraint(expr=   m.x8 - m.x28 + m.x118 >= 0.78845736036427)

m.c19 = Constraint(expr=   m.x9 - m.x29 + m.x119 >= 0.336472236621213)

m.c20 = Constraint(expr=   m.x10 - m.x30 + m.x120 >= 0.78845736036427)

m.c21 = Constraint(expr=   m.x1 - m.x31 + m.x111 >= -0.356674943938732)

m.c22 = Constraint(expr=   m.x2 - m.x32 + m.x112 >= 0.955511445027436)

m.c23 = Constraint(expr=   m.x3 - m.x33 + m.x113 >= 0.470003629245736)

m.c24 = Constraint(expr=   m.x4 - m.x34 + m.x114 >= 1.28093384546206)

m.c25 = Constraint(expr=   m.x5 - m.x35 + m.x115 >= 1.16315080980568)

m.c26 = Constraint(expr=   m.x6 - m.x36 + m.x116 >= 1.06471073699243)

m.c27 = Constraint(expr=   m.x7 - m.x37 + m.x117 >= 1.28093384546206)

m.c28 = Constraint(expr=   m.x8 - m.x38 + m.x118 >= 1.38629436111989)

m.c29 = Constraint(expr=   m.x9 - m.x39 + m.x119 >= 1.45861502269952)

m.c30 = Constraint(expr=   m.x10 - m.x40 + m.x120 >= -0.510825623765991)

m.c31 = Constraint(expr=   m.x1 - m.x41 + m.x111 >= 1.54756250871601)

m.c32 = Constraint(expr=   m.x2 - m.x42 + m.x112 >= 0.832909122935104)

m.c33 = Constraint(expr=   m.x3 - m.x43 + m.x113 >= 0.470003629245736)

m.c34 = Constraint(expr=   m.x4 - m.x44 + m.x114 >= 0.993251773010283)

m.c35 = Constraint(expr=   m.x5 - m.x45 + m.x115 >= 0.182321556793955)

m.c36 = Constraint(expr=   m.x6 - m.x46 + m.x116 >= 0.916290731874155)

m.c37 = Constraint(expr=   m.x7 - m.x47 + m.x117 >= 1.3609765531356)

m.c38 = Constraint(expr=   m.x8 - m.x48 + m.x118 >= -0.510825623765991)

m.c39 = Constraint(expr=   m.x9 - m.x49 + m.x119 >= 1.1314021114911)

m.c40 = Constraint(expr=   m.x10 - m.x50 + m.x120 >= 1.75785791755237)

m.c41 = Constraint(expr=   m.x1 - m.x51 + m.x111 >= 0.182321556793955)

m.c42 = Constraint(expr=   m.x2 - m.x52 + m.x112 >= 1.28093384546206)

m.c43 = Constraint(expr=   m.x3 - m.x53 + m.x113 >= 0.8754687373539)

m.c44 = Constraint(expr=   m.x4 - m.x54 + m.x114 >= 1.50407739677627)

m.c45 = Constraint(expr=   m.x5 - m.x55 + m.x115 >= 0.470003629245736)

m.c46 = Constraint(expr=   m.x6 - m.x56 + m.x116 >= 0.741937344729377)

m.c47 = Constraint(expr=   m.x7 - m.x57 + m.x117 >= -0.105360515657826)

m.c48 = Constraint(expr=   m.x8 - m.x58 + m.x118 >= 1.43508452528932)

m.c49 = Constraint(expr=   m.x9 - m.x59 + m.x119 >= 0.741937344729377)

m.c50 = Constraint(expr=   m.x10 - m.x60 + m.x120 >= 1.41098697371026)

m.c51 = Constraint(expr=   m.x1 - m.x61 + m.x111 >= 1.1314021114911)

m.c52 = Constraint(expr=   m.x2 - m.x62 + m.x112 >= 0.916290731874155)

m.c53 = Constraint(expr=   m.x3 - m.x63 + m.x113 >= 1.50407739677627)

m.c54 = Constraint(expr=   m.x4 - m.x64 + m.x114 >= 0.262364264467491)

m.c55 = Constraint(expr=   m.x5 - m.x65 + m.x115 >= 1.19392246847243)

m.c56 = Constraint(expr=   m.x6 - m.x66 + m.x116 >= 1.41098697371026)

m.c57 = Constraint(expr=   m.x7 - m.x67 + m.x117 >= 0.336472236621213)

m.c58 = Constraint(expr=   m.x8 - m.x68 + m.x118 >= 0)

m.c59 = Constraint(expr=   m.x9 - m.x69 + m.x119 >= 1.25276296849537)

m.c60 = Constraint(expr=   m.x10 - m.x70 + m.x120 >= -0.356674943938732)

m.c61 = Constraint(expr=   m.x1 - m.x71 + m.x111 >= 0)

m.c62 = Constraint(expr=   m.x2 - m.x72 + m.x112 >= 0.78845736036427)

m.c63 = Constraint(expr=   m.x3 - m.x73 + m.x113 >= -0.356674943938732)

m.c64 = Constraint(expr=   m.x4 - m.x74 + m.x114 >= 1.43508452528932)

m.c65 = Constraint(expr=   m.x5 - m.x75 + m.x115 >= 1.02961941718116)

m.c66 = Constraint(expr=   m.x6 - m.x76 + m.x116 >= 0.832909122935104)

m.c67 = Constraint(expr=   m.x7 - m.x77 + m.x117 >= 1.64865862558738)

m.c68 = Constraint(expr=   m.x8 - m.x78 + m.x118 >= 0.641853886172395)

m.c69 = Constraint(expr=   m.x9 - m.x79 + m.x119 >= 0.955511445027436)

m.c70 = Constraint(expr=   m.x10 - m.x80 + m.x120 >= 0.0953101798043249)

m.c71 = Constraint(expr=   m.x1 - m.x81 + m.x111 >= 0.916290731874155)

m.c72 = Constraint(expr=   m.x2 - m.x82 + m.x112 >= 0.0953101798043249)

m.c73 = Constraint(expr=   m.x3 - m.x83 + m.x113 >= 1.66770682055808)

m.c74 = Constraint(expr=   m.x4 - m.x84 + m.x114 >= 0.955511445027436)

m.c75 = Constraint(expr=   m.x5 - m.x85 + m.x115 >= 1.30833281965018)

m.c76 = Constraint(expr=   m.x6 - m.x86 + m.x116 >= 1.38629436111989)

m.c77 = Constraint(expr=   m.x7 - m.x87 + m.x117 >= 0.78845736036427)

m.c78 = Constraint(expr=   m.x8 - m.x88 + m.x118 >= 1.19392246847243)

m.c79 = Constraint(expr=   m.x9 - m.x89 + m.x119 >= 0.993251773010283)

m.c80 = Constraint(expr=   m.x10 - m.x90 + m.x120 >= 1.22377543162212)

m.c81 = Constraint(expr=   m.x1 - m.x91 + m.x111 >= 0.8754687373539)

m.c82 = Constraint(expr=   m.x2 - m.x92 + m.x112 >= 0.916290731874155)

m.c83 = Constraint(expr=   m.x3 - m.x93 + m.x113 >= 0.993251773010283)

m.c84 = Constraint(expr=   m.x4 - m.x94 + m.x114 >= 1.16315080980568)

m.c85 = Constraint(expr=   m.x5 - m.x95 + m.x115 >= 0.832909122935104)

m.c86 = Constraint(expr=   m.x6 - m.x96 + m.x116 >= 0.53062825106217)

m.c87 = Constraint(expr=   m.x7 - m.x97 + m.x117 >= 1.64865862558738)

m.c88 = Constraint(expr=   m.x8 - m.x98 + m.x118 >= 1.54756250871601)

m.c89 = Constraint(expr=   m.x9 - m.x99 + m.x119 >= 0.955511445027436)

m.c90 = Constraint(expr=   m.x10 - m.x100 + m.x120 >= 0.336472236621213)

m.c91 = Constraint(expr=   m.x1 - m.x101 + m.x111 >= 0.993251773010283)

m.c92 = Constraint(expr=   m.x2 - m.x102 + m.x112 >= 1.19392246847243)

m.c93 = Constraint(expr=   m.x3 - m.x103 + m.x113 >= 1.48160454092422)

m.c94 = Constraint(expr=   m.x4 - m.x104 + m.x114 >= 0.955511445027436)

m.c95 = Constraint(expr=   m.x5 - m.x105 + m.x115 >= 1.30833281965018)

m.c96 = Constraint(expr=   m.x6 - m.x106 + m.x116 >= -0.693147180559945)

m.c97 = Constraint(expr=   m.x7 - m.x107 + m.x117 >= 0.993251773010283)

m.c98 = Constraint(expr=   m.x8 - m.x108 + m.x118 >= 1.82454929205105)

m.c99 = Constraint(expr=   m.x9 - m.x109 + m.x119 >= 1.16315080980568)

m.c100 = Constraint(expr=   m.x10 - m.x110 + m.x120 >= 1.22377543162212)

m.c101 = Constraint(expr=   m.x11 + m.x121 + m.x141 >= 1.85629799036563)

m.c102 = Constraint(expr=   m.x12 + m.x122 + m.x141 >= 1.54756250871601)

m.c103 = Constraint(expr=   m.x13 + m.x123 + m.x141 >= 0.262364264467491)

m.c104 = Constraint(expr=   m.x14 + m.x124 + m.x141 >= 1.3609765531356)

m.c105 = Constraint(expr=   m.x15 + m.x125 + m.x141 >= 0.741937344729377)

m.c106 = Constraint(expr=   m.x16 + m.x126 + m.x141 >= 0.470003629245736)

m.c107 = Constraint(expr=   m.x17 + m.x127 + m.x141 >= 1.16315080980568)

m.c108 = Constraint(expr=   m.x18 + m.x128 + m.x141 >= 1.1314021114911)

m.c109 = Constraint(expr=   m.x19 + m.x129 + m.x141 >= 1.43508452528932)

m.c110 = Constraint(expr=   m.x20 + m.x130 + m.x141 >= 1.64865862558738)

m.c111 = Constraint(expr=   m.x21 + m.x121 + m.x142 >= 1.33500106673234)

m.c112 = Constraint(expr=   m.x22 + m.x122 + m.x142 >= 1.85629799036563)

m.c113 = Constraint(expr=   m.x23 + m.x123 + m.x142 >= 1.87180217690159)

m.c114 = Constraint(expr=   m.x24 + m.x124 + m.x142 >= 1.48160454092422)

m.c115 = Constraint(expr=   m.x25 + m.x125 + m.x142 >= 0.832909122935104)

m.c116 = Constraint(expr=   m.x26 + m.x126 + m.x142 >= 1.16315080980568)

m.c117 = Constraint(expr=   m.x27 + m.x127 + m.x142 >= 1.64865862558738)

m.c118 = Constraint(expr=   m.x28 + m.x128 + m.x142 >= 0.916290731874155)

m.c119 = Constraint(expr=   m.x29 + m.x129 + m.x142 >= 1.48160454092422)

m.c120 = Constraint(expr=   m.x30 + m.x130 + m.x142 >= 0.0953101798043249)

m.c121 = Constraint(expr=   m.x31 + m.x121 + m.x143 >= 0)

m.c122 = Constraint(expr=   m.x32 + m.x122 + m.x143 >= 1.84054963339749)

m.c123 = Constraint(expr=   m.x33 + m.x123 + m.x143 >= 1.22377543162212)

m.c124 = Constraint(expr=   m.x34 + m.x124 + m.x143 >= 1.58923520511658)

m.c125 = Constraint(expr=   m.x35 + m.x125 + m.x143 >= 0.993251773010283)

m.c126 = Constraint(expr=   m.x36 + m.x126 + m.x143 >= 1.82454929205105)

m.c127 = Constraint(expr=   m.x37 + m.x127 + m.x143 >= 1.1314021114911)

m.c128 = Constraint(expr=   m.x38 + m.x128 + m.x143 >= 0.182321556793955)

m.c129 = Constraint(expr=   m.x39 + m.x129 + m.x143 >= 0.832909122935104)

m.c130 = Constraint(expr=   m.x40 + m.x130 + m.x143 >= 1.62924053973028)

m.c131 = Constraint(expr=   m.x41 + m.x121 + m.x144 >= 1.16315080980568)

m.c132 = Constraint(expr=   m.x42 + m.x122 + m.x144 >= 1.09861228866811)

m.c133 = Constraint(expr=   m.x43 + m.x123 + m.x144 >= 1.25276296849537)

m.c134 = Constraint(expr=   m.x44 + m.x124 + m.x144 >= 1.19392246847243)

m.c135 = Constraint(expr=   m.x45 + m.x125 + m.x144 >= 1.02961941718116)

m.c136 = Constraint(expr=   m.x46 + m.x126 + m.x144 >= 1.22377543162212)

m.c137 = Constraint(expr=   m.x47 + m.x127 + m.x144 >= 1.43508452528932)

m.c138 = Constraint(expr=   m.x48 + m.x128 + m.x144 >= 1.06471073699243)

m.c139 = Constraint(expr=   m.x49 + m.x129 + m.x144 >= 1.82454929205105)

m.c140 = Constraint(expr=   m.x50 + m.x130 + m.x144 >= 0.78845736036427)

m.c141 = Constraint(expr=   m.x51 + m.x121 + m.x145 >= 0.741937344729377)

m.c142 = Constraint(expr=   m.x52 + m.x122 + m.x145 >= 0.916290731874155)

m.c143 = Constraint(expr=   m.x53 + m.x123 + m.x145 >= 1.43508452528932)

m.c144 = Constraint(expr=   m.x54 + m.x124 + m.x145 >= 1.28093384546206)

m.c145 = Constraint(expr=   m.x55 + m.x125 + m.x145 >= 1.30833281965018)

m.c146 = Constraint(expr=   m.x56 + m.x126 + m.x145 >= 0.78845736036427)

m.c147 = Constraint(expr=   m.x57 + m.x127 + m.x145 >= 1.62924053973028)

m.c148 = Constraint(expr=   m.x58 + m.x128 + m.x145 >= -0.916290731874155)

m.c149 = Constraint(expr=   m.x59 + m.x129 + m.x145 >= 1.41098697371026)

m.c150 = Constraint(expr=   m.x60 + m.x130 + m.x145 >= 0.262364264467491)

m.c151 = Constraint(expr=   m.x61 + m.x121 + m.x146 >= 1.25276296849537)

m.c152 = Constraint(expr=   m.x62 + m.x122 + m.x146 >= 1.41098697371026)

m.c153 = Constraint(expr=   m.x63 + m.x123 + m.x146 >= -0.105360515657826)

m.c154 = Constraint(expr=   m.x64 + m.x124 + m.x146 >= 0.336472236621213)

m.c155 = Constraint(expr=   m.x65 + m.x125 + m.x146 >= 1.28093384546206)

m.c156 = Constraint(expr=   m.x66 + m.x126 + m.x146 >= 0.993251773010283)

m.c157 = Constraint(expr=   m.x67 + m.x127 + m.x146 >= 1.06471073699243)

m.c158 = Constraint(expr=   m.x68 + m.x128 + m.x146 >= 1.30833281965018)

m.c159 = Constraint(expr=   m.x69 + m.x129 + m.x146 >= -0.22314355131421)

m.c160 = Constraint(expr=   m.x70 + m.x130 + m.x146 >= 0.405465108108164)

m.c161 = Constraint(expr=   m.x71 + m.x121 + m.x147 >= 1.41098697371026)

m.c162 = Constraint(expr=   m.x72 + m.x122 + m.x147 >= 1.90210752639692)

m.c163 = Constraint(expr=   m.x73 + m.x123 + m.x147 >= 0.78845736036427)

m.c164 = Constraint(expr=   m.x74 + m.x124 + m.x147 >= 0.336472236621213)

m.c165 = Constraint(expr=   m.x75 + m.x125 + m.x147 >= -0.356674943938732)

m.c166 = Constraint(expr=   m.x76 + m.x126 + m.x147 >= 1.54756250871601)

m.c167 = Constraint(expr=   m.x77 + m.x127 + m.x147 >= 0.262364264467491)

m.c168 = Constraint(expr=   m.x78 + m.x128 + m.x147 >= -0.510825623765991)

m.c169 = Constraint(expr=   m.x79 + m.x129 + m.x147 >= 1.16315080980568)

m.c170 = Constraint(expr=   m.x80 + m.x130 + m.x147 >= 0.741937344729377)

m.c171 = Constraint(expr=   m.x81 + m.x121 + m.x148 >= 1.66770682055808)

m.c172 = Constraint(expr=   m.x82 + m.x122 + m.x148 >= 1.1314021114911)

m.c173 = Constraint(expr=   m.x83 + m.x123 + m.x148 >= 1.02961941718116)

m.c174 = Constraint(expr=   m.x84 + m.x124 + m.x148 >= 0.405465108108164)

m.c175 = Constraint(expr=   m.x85 + m.x125 + m.x148 >= 1.16315080980568)

m.c176 = Constraint(expr=   m.x86 + m.x126 + m.x148 >= 1.80828877117927)

m.c177 = Constraint(expr=   m.x87 + m.x127 + m.x148 >= -0.693147180559945)

m.c178 = Constraint(expr=   m.x88 + m.x128 + m.x148 >= 1.3609765531356)

m.c179 = Constraint(expr=   m.x89 + m.x129 + m.x148 >= 0.993251773010283)

m.c180 = Constraint(expr=   m.x90 + m.x130 + m.x148 >= 1.41098697371026)

m.c181 = Constraint(expr=   m.x91 + m.x121 + m.x149 >= 0.955511445027436)

m.c182 = Constraint(expr=   m.x92 + m.x122 + m.x149 >= 1.64865862558738)

m.c183 = Constraint(expr=   m.x93 + m.x123 + m.x149 >= 1.16315080980568)

m.c184 = Constraint(expr=   m.x94 + m.x124 + m.x149 >= 1.22377543162212)

m.c185 = Constraint(expr=   m.x95 + m.x125 + m.x149 >= 1.48160454092422)

m.c186 = Constraint(expr=   m.x96 + m.x126 + m.x149 >= 0.0953101798043249)

m.c187 = Constraint(expr=   m.x97 + m.x127 + m.x149 >= 1.96009478404727)

m.c188 = Constraint(expr=   m.x98 + m.x128 + m.x149 >= 0.916290731874155)

m.c189 = Constraint(expr=   m.x99 + m.x129 + m.x149 >= 1.1314021114911)

m.c190 = Constraint(expr=   m.x100 + m.x130 + m.x149 >= -0.105360515657826)

m.c191 = Constraint(expr=   m.x101 + m.x121 + m.x150 >= 0.53062825106217)

m.c192 = Constraint(expr=   m.x102 + m.x122 + m.x150 >= 1.64865862558738)

m.c193 = Constraint(expr=   m.x103 + m.x123 + m.x150 >= 1.30833281965018)

m.c194 = Constraint(expr=   m.x104 + m.x124 + m.x150 >= 0.955511445027436)

m.c195 = Constraint(expr=   m.x105 + m.x125 + m.x150 >= 1.64865862558738)

m.c196 = Constraint(expr=   m.x106 + m.x126 + m.x150 >= 0.955511445027436)

m.c197 = Constraint(expr=   m.x107 + m.x127 + m.x150 >= 1.62924053973028)

m.c198 = Constraint(expr=   m.x108 + m.x128 + m.x150 >= 2.10413415427021)

m.c199 = Constraint(expr=   m.x109 + m.x129 + m.x150 >= 0.0953101798043249)

m.c200 = Constraint(expr=   m.x110 + m.x130 + m.x150 >= 1.06471073699243)

m.c201 = Constraint(expr=250000*exp(m.x141) + 150000*exp(m.x142) + 180000*exp(m.x143) + 160000*exp(m.x144) + 120000*exp(
                         m.x145) + 130000*exp(m.x146) + 190000*exp(m.x147) + 140000*exp(m.x148) + 175000*exp(m.x149) + 
                         125000*exp(m.x150) <= 6000)

m.c202 = Constraint(expr= - m.x12 + m.x132 - 4.04964438330419*m.b271 >= -1.74705929031015)

m.c203 = Constraint(expr= - m.x13 + m.x133 - 4.04964438330419*m.b272 >= -1.74705929031015)

m.c204 = Constraint(expr= - m.x14 + m.x134 - 4.04964438330419*m.b273 >= -1.74705929031015)

m.c205 = Constraint(expr= - m.x15 + m.x135 - 4.04964438330419*m.b274 >= -1.74705929031015)

m.c206 = Constraint(expr= - m.x16 + m.x136 - 4.04964438330419*m.b275 >= -1.74705929031015)

m.c207 = Constraint(expr= - m.x17 + m.x137 - 4.04964438330419*m.b276 >= -1.74705929031015)

m.c208 = Constraint(expr= - m.x18 + m.x138 - 4.04964438330419*m.b277 >= -1.74705929031015)

m.c209 = Constraint(expr= - m.x19 + m.x139 - 4.04964438330419*m.b278 >= -1.74705929031015)

m.c210 = Constraint(expr= - m.x20 + m.x140 - 4.04964438330419*m.b279 >= -1.74705929031015)

m.c211 = Constraint(expr= - m.x22 + m.x132 - 4.63415772286134*m.b271 >= -2.3315726298673)

m.c212 = Constraint(expr= - m.x23 + m.x133 - 4.63415772286134*m.b272 >= -2.3315726298673)

m.c213 = Constraint(expr= - m.x24 + m.x134 - 4.63415772286134*m.b273 >= -2.3315726298673)

m.c214 = Constraint(expr= - m.x25 + m.x135 - 4.63415772286134*m.b274 >= -2.3315726298673)

m.c215 = Constraint(expr= - m.x26 + m.x136 - 4.63415772286134*m.b275 >= -2.3315726298673)

m.c216 = Constraint(expr= - m.x27 + m.x137 - 4.63415772286134*m.b276 >= -2.3315726298673)

m.c217 = Constraint(expr= - m.x28 + m.x138 - 4.63415772286134*m.b277 >= -2.3315726298673)

m.c218 = Constraint(expr= - m.x29 + m.x139 - 4.63415772286134*m.b278 >= -2.3315726298673)

m.c219 = Constraint(expr= - m.x30 + m.x140 - 4.63415772286134*m.b279 >= -2.3315726298673)

m.c220 = Constraint(expr= - m.x32 + m.x132 - 4.39931813178394*m.b271 >= -2.0967330387899)

m.c221 = Constraint(expr= - m.x33 + m.x133 - 4.39931813178394*m.b272 >= -2.0967330387899)

m.c222 = Constraint(expr= - m.x34 + m.x134 - 4.39931813178394*m.b273 >= -2.0967330387899)

m.c223 = Constraint(expr= - m.x35 + m.x135 - 4.39931813178394*m.b274 >= -2.0967330387899)

m.c224 = Constraint(expr= - m.x36 + m.x136 - 4.39931813178394*m.b275 >= -2.0967330387899)

m.c225 = Constraint(expr= - m.x37 + m.x137 - 4.39931813178394*m.b276 >= -2.0967330387899)

m.c226 = Constraint(expr= - m.x38 + m.x138 - 4.39931813178394*m.b277 >= -2.0967330387899)

m.c227 = Constraint(expr= - m.x39 + m.x139 - 4.39931813178394*m.b278 >= -2.0967330387899)

m.c228 = Constraint(expr= - m.x40 + m.x140 - 4.39931813178394*m.b279 >= -2.0967330387899)

m.c229 = Constraint(expr= - m.x42 + m.x132 - 4.10007523693109*m.b271 >= -1.79749014393704)

m.c230 = Constraint(expr= - m.x43 + m.x133 - 4.10007523693109*m.b272 >= -1.79749014393704)

m.c231 = Constraint(expr= - m.x44 + m.x134 - 4.10007523693109*m.b273 >= -1.79749014393704)

m.c232 = Constraint(expr= - m.x45 + m.x135 - 4.10007523693109*m.b274 >= -1.79749014393704)

m.c233 = Constraint(expr= - m.x46 + m.x136 - 4.10007523693109*m.b275 >= -1.79749014393704)

m.c234 = Constraint(expr= - m.x47 + m.x137 - 4.10007523693109*m.b276 >= -1.79749014393704)

m.c235 = Constraint(expr= - m.x48 + m.x138 - 4.10007523693109*m.b277 >= -1.79749014393704)

m.c236 = Constraint(expr= - m.x49 + m.x139 - 4.10007523693109*m.b278 >= -1.79749014393704)

m.c237 = Constraint(expr= - m.x50 + m.x140 - 4.10007523693109*m.b279 >= -1.79749014393704)

m.c238 = Constraint(expr= - m.x52 + m.x132 - 4.35385575770719*m.b271 >= -2.05127066471314)

m.c239 = Constraint(expr= - m.x53 + m.x133 - 4.35385575770719*m.b272 >= -2.05127066471314)

m.c240 = Constraint(expr= - m.x54 + m.x134 - 4.35385575770719*m.b273 >= -2.05127066471314)

m.c241 = Constraint(expr= - m.x55 + m.x135 - 4.35385575770719*m.b274 >= -2.05127066471314)

m.c242 = Constraint(expr= - m.x56 + m.x136 - 4.35385575770719*m.b275 >= -2.05127066471314)

m.c243 = Constraint(expr= - m.x57 + m.x137 - 4.35385575770719*m.b276 >= -2.05127066471314)

m.c244 = Constraint(expr= - m.x58 + m.x138 - 4.35385575770719*m.b277 >= -2.05127066471314)

m.c245 = Constraint(expr= - m.x59 + m.x139 - 4.35385575770719*m.b278 >= -2.05127066471314)

m.c246 = Constraint(expr= - m.x60 + m.x140 - 4.35385575770719*m.b279 >= -2.05127066471314)

m.c247 = Constraint(expr= - m.x62 + m.x132 - 4.35385575770719*m.b271 >= -2.05127066471314)

m.c248 = Constraint(expr= - m.x63 + m.x133 - 4.35385575770719*m.b272 >= -2.05127066471314)

m.c249 = Constraint(expr= - m.x64 + m.x134 - 4.35385575770719*m.b273 >= -2.05127066471314)

m.c250 = Constraint(expr= - m.x65 + m.x135 - 4.35385575770719*m.b274 >= -2.05127066471314)

m.c251 = Constraint(expr= - m.x66 + m.x136 - 4.35385575770719*m.b275 >= -2.05127066471314)

m.c252 = Constraint(expr= - m.x67 + m.x137 - 4.35385575770719*m.b276 >= -2.05127066471314)

m.c253 = Constraint(expr= - m.x68 + m.x138 - 4.35385575770719*m.b277 >= -2.05127066471314)

m.c254 = Constraint(expr= - m.x69 + m.x139 - 4.35385575770719*m.b278 >= -2.05127066471314)

m.c255 = Constraint(expr= - m.x70 + m.x140 - 4.35385575770719*m.b279 >= -2.05127066471314)

m.c256 = Constraint(expr= - m.x72 + m.x132 - 4.20927452889608*m.b271 >= -1.90668943590203)

m.c257 = Constraint(expr= - m.x73 + m.x133 - 4.20927452889608*m.b272 >= -1.90668943590203)

m.c258 = Constraint(expr= - m.x74 + m.x134 - 4.20927452889608*m.b273 >= -1.90668943590203)

m.c259 = Constraint(expr= - m.x75 + m.x135 - 4.20927452889608*m.b274 >= -1.90668943590203)

m.c260 = Constraint(expr= - m.x76 + m.x136 - 4.20927452889608*m.b275 >= -1.90668943590203)

m.c261 = Constraint(expr= - m.x77 + m.x137 - 4.20927452889608*m.b276 >= -1.90668943590203)

m.c262 = Constraint(expr= - m.x78 + m.x138 - 4.20927452889608*m.b277 >= -1.90668943590203)

m.c263 = Constraint(expr= - m.x79 + m.x139 - 4.20927452889608*m.b278 >= -1.90668943590203)

m.c264 = Constraint(expr= - m.x80 + m.x140 - 4.20927452889608*m.b279 >= -1.90668943590203)

m.c265 = Constraint(expr= - m.x82 + m.x132 - 4.19022633392538*m.b271 >= -1.88764124093134)

m.c266 = Constraint(expr= - m.x83 + m.x133 - 4.19022633392538*m.b272 >= -1.88764124093134)

m.c267 = Constraint(expr= - m.x84 + m.x134 - 4.19022633392538*m.b273 >= -1.88764124093134)

m.c268 = Constraint(expr= - m.x85 + m.x135 - 4.19022633392538*m.b274 >= -1.88764124093134)

m.c269 = Constraint(expr= - m.x86 + m.x136 - 4.19022633392538*m.b275 >= -1.88764124093134)

m.c270 = Constraint(expr= - m.x87 + m.x137 - 4.19022633392538*m.b276 >= -1.88764124093134)

m.c271 = Constraint(expr= - m.x88 + m.x138 - 4.19022633392538*m.b277 >= -1.88764124093134)

m.c272 = Constraint(expr= - m.x89 + m.x139 - 4.19022633392538*m.b278 >= -1.88764124093134)

m.c273 = Constraint(expr= - m.x90 + m.x140 - 4.19022633392538*m.b279 >= -1.88764124093134)

m.c274 = Constraint(expr= - m.x92 + m.x132 - 4.20927452889608*m.b271 >= -1.90668943590203)

m.c275 = Constraint(expr= - m.x93 + m.x133 - 4.20927452889608*m.b272 >= -1.90668943590203)

m.c276 = Constraint(expr= - m.x94 + m.x134 - 4.20927452889608*m.b273 >= -1.90668943590203)

m.c277 = Constraint(expr= - m.x95 + m.x135 - 4.20927452889608*m.b274 >= -1.90668943590203)

m.c278 = Constraint(expr= - m.x96 + m.x136 - 4.20927452889608*m.b275 >= -1.90668943590203)

m.c279 = Constraint(expr= - m.x97 + m.x137 - 4.20927452889608*m.b276 >= -1.90668943590203)

m.c280 = Constraint(expr= - m.x98 + m.x138 - 4.20927452889608*m.b277 >= -1.90668943590203)

m.c281 = Constraint(expr= - m.x99 + m.x139 - 4.20927452889608*m.b278 >= -1.90668943590203)

m.c282 = Constraint(expr= - m.x100 + m.x140 - 4.20927452889608*m.b279 >= -1.90668943590203)

m.c283 = Constraint(expr= - m.x102 + m.x132 - 4.03338386243241*m.b271 >= -1.73079876943837)

m.c284 = Constraint(expr= - m.x103 + m.x133 - 4.03338386243241*m.b272 >= -1.73079876943837)

m.c285 = Constraint(expr= - m.x104 + m.x134 - 4.03338386243241*m.b273 >= -1.73079876943837)

m.c286 = Constraint(expr= - m.x105 + m.x135 - 4.03338386243241*m.b274 >= -1.73079876943837)

m.c287 = Constraint(expr= - m.x106 + m.x136 - 4.03338386243241*m.b275 >= -1.73079876943837)

m.c288 = Constraint(expr= - m.x107 + m.x137 - 4.03338386243241*m.b276 >= -1.73079876943837)

m.c289 = Constraint(expr= - m.x108 + m.x138 - 4.03338386243241*m.b277 >= -1.73079876943837)

m.c290 = Constraint(expr= - m.x109 + m.x139 - 4.03338386243241*m.b278 >= -1.73079876943837)

m.c291 = Constraint(expr= - m.x110 + m.x140 - 4.03338386243241*m.b279 >= -1.73079876943837)

m.c292 = Constraint(expr= - m.x11 + m.x132 - 4.04964438330419*m.b271 >= -1.74705929031015)

m.c293 = Constraint(expr= - m.x12 + m.x133 - 4.04964438330419*m.b272 >= -1.74705929031015)

m.c294 = Constraint(expr= - m.x13 + m.x134 - 4.04964438330419*m.b273 >= -1.74705929031015)

m.c295 = Constraint(expr= - m.x14 + m.x135 - 4.04964438330419*m.b274 >= -1.74705929031015)

m.c296 = Constraint(expr= - m.x15 + m.x136 - 4.04964438330419*m.b275 >= -1.74705929031015)

m.c297 = Constraint(expr= - m.x16 + m.x137 - 4.04964438330419*m.b276 >= -1.74705929031015)

m.c298 = Constraint(expr= - m.x17 + m.x138 - 4.04964438330419*m.b277 >= -1.74705929031015)

m.c299 = Constraint(expr= - m.x18 + m.x139 - 4.04964438330419*m.b278 >= -1.74705929031015)

m.c300 = Constraint(expr= - m.x19 + m.x140 - 4.04964438330419*m.b279 >= -1.74705929031015)

m.c301 = Constraint(expr= - m.x21 + m.x132 - 4.63415772286134*m.b271 >= -2.3315726298673)

m.c302 = Constraint(expr= - m.x22 + m.x133 - 4.63415772286134*m.b272 >= -2.3315726298673)

m.c303 = Constraint(expr= - m.x23 + m.x134 - 4.63415772286134*m.b273 >= -2.3315726298673)

m.c304 = Constraint(expr= - m.x24 + m.x135 - 4.63415772286134*m.b274 >= -2.3315726298673)

m.c305 = Constraint(expr= - m.x25 + m.x136 - 4.63415772286134*m.b275 >= -2.3315726298673)

m.c306 = Constraint(expr= - m.x26 + m.x137 - 4.63415772286134*m.b276 >= -2.3315726298673)

m.c307 = Constraint(expr= - m.x27 + m.x138 - 4.63415772286134*m.b277 >= -2.3315726298673)

m.c308 = Constraint(expr= - m.x28 + m.x139 - 4.63415772286134*m.b278 >= -2.3315726298673)

m.c309 = Constraint(expr= - m.x29 + m.x140 - 4.63415772286134*m.b279 >= -2.3315726298673)

m.c310 = Constraint(expr= - m.x31 + m.x132 - 4.39931813178394*m.b271 >= -2.0967330387899)

m.c311 = Constraint(expr= - m.x32 + m.x133 - 4.39931813178394*m.b272 >= -2.0967330387899)

m.c312 = Constraint(expr= - m.x33 + m.x134 - 4.39931813178394*m.b273 >= -2.0967330387899)

m.c313 = Constraint(expr= - m.x34 + m.x135 - 4.39931813178394*m.b274 >= -2.0967330387899)

m.c314 = Constraint(expr= - m.x35 + m.x136 - 4.39931813178394*m.b275 >= -2.0967330387899)

m.c315 = Constraint(expr= - m.x36 + m.x137 - 4.39931813178394*m.b276 >= -2.0967330387899)

m.c316 = Constraint(expr= - m.x37 + m.x138 - 4.39931813178394*m.b277 >= -2.0967330387899)

m.c317 = Constraint(expr= - m.x38 + m.x139 - 4.39931813178394*m.b278 >= -2.0967330387899)

m.c318 = Constraint(expr= - m.x39 + m.x140 - 4.39931813178394*m.b279 >= -2.0967330387899)

m.c319 = Constraint(expr= - m.x41 + m.x132 - 4.10007523693109*m.b271 >= -1.79749014393704)

m.c320 = Constraint(expr= - m.x42 + m.x133 - 4.10007523693109*m.b272 >= -1.79749014393704)

m.c321 = Constraint(expr= - m.x43 + m.x134 - 4.10007523693109*m.b273 >= -1.79749014393704)

m.c322 = Constraint(expr= - m.x44 + m.x135 - 4.10007523693109*m.b274 >= -1.79749014393704)

m.c323 = Constraint(expr= - m.x45 + m.x136 - 4.10007523693109*m.b275 >= -1.79749014393704)

m.c324 = Constraint(expr= - m.x46 + m.x137 - 4.10007523693109*m.b276 >= -1.79749014393704)

m.c325 = Constraint(expr= - m.x47 + m.x138 - 4.10007523693109*m.b277 >= -1.79749014393704)

m.c326 = Constraint(expr= - m.x48 + m.x139 - 4.10007523693109*m.b278 >= -1.79749014393704)

m.c327 = Constraint(expr= - m.x49 + m.x140 - 4.10007523693109*m.b279 >= -1.79749014393704)

m.c328 = Constraint(expr= - m.x51 + m.x132 - 4.35385575770719*m.b271 >= -2.05127066471314)

m.c329 = Constraint(expr= - m.x52 + m.x133 - 4.35385575770719*m.b272 >= -2.05127066471314)

m.c330 = Constraint(expr= - m.x53 + m.x134 - 4.35385575770719*m.b273 >= -2.05127066471314)

m.c331 = Constraint(expr= - m.x54 + m.x135 - 4.35385575770719*m.b274 >= -2.05127066471314)

m.c332 = Constraint(expr= - m.x55 + m.x136 - 4.35385575770719*m.b275 >= -2.05127066471314)

m.c333 = Constraint(expr= - m.x56 + m.x137 - 4.35385575770719*m.b276 >= -2.05127066471314)

m.c334 = Constraint(expr= - m.x57 + m.x138 - 4.35385575770719*m.b277 >= -2.05127066471314)

m.c335 = Constraint(expr= - m.x58 + m.x139 - 4.35385575770719*m.b278 >= -2.05127066471314)

m.c336 = Constraint(expr= - m.x59 + m.x140 - 4.35385575770719*m.b279 >= -2.05127066471314)

m.c337 = Constraint(expr= - m.x61 + m.x132 - 4.35385575770719*m.b271 >= -2.05127066471314)

m.c338 = Constraint(expr= - m.x62 + m.x133 - 4.35385575770719*m.b272 >= -2.05127066471314)

m.c339 = Constraint(expr= - m.x63 + m.x134 - 4.35385575770719*m.b273 >= -2.05127066471314)

m.c340 = Constraint(expr= - m.x64 + m.x135 - 4.35385575770719*m.b274 >= -2.05127066471314)

m.c341 = Constraint(expr= - m.x65 + m.x136 - 4.35385575770719*m.b275 >= -2.05127066471314)

m.c342 = Constraint(expr= - m.x66 + m.x137 - 4.35385575770719*m.b276 >= -2.05127066471314)

m.c343 = Constraint(expr= - m.x67 + m.x138 - 4.35385575770719*m.b277 >= -2.05127066471314)

m.c344 = Constraint(expr= - m.x68 + m.x139 - 4.35385575770719*m.b278 >= -2.05127066471314)

m.c345 = Constraint(expr= - m.x69 + m.x140 - 4.35385575770719*m.b279 >= -2.05127066471314)

m.c346 = Constraint(expr= - m.x71 + m.x132 - 4.20927452889608*m.b271 >= -1.90668943590203)

m.c347 = Constraint(expr= - m.x72 + m.x133 - 4.20927452889608*m.b272 >= -1.90668943590203)

m.c348 = Constraint(expr= - m.x73 + m.x134 - 4.20927452889608*m.b273 >= -1.90668943590203)

m.c349 = Constraint(expr= - m.x74 + m.x135 - 4.20927452889608*m.b274 >= -1.90668943590203)

m.c350 = Constraint(expr= - m.x75 + m.x136 - 4.20927452889608*m.b275 >= -1.90668943590203)

m.c351 = Constraint(expr= - m.x76 + m.x137 - 4.20927452889608*m.b276 >= -1.90668943590203)

m.c352 = Constraint(expr= - m.x77 + m.x138 - 4.20927452889608*m.b277 >= -1.90668943590203)

m.c353 = Constraint(expr= - m.x78 + m.x139 - 4.20927452889608*m.b278 >= -1.90668943590203)

m.c354 = Constraint(expr= - m.x79 + m.x140 - 4.20927452889608*m.b279 >= -1.90668943590203)

m.c355 = Constraint(expr= - m.x81 + m.x132 - 4.19022633392538*m.b271 >= -1.88764124093134)

m.c356 = Constraint(expr= - m.x82 + m.x133 - 4.19022633392538*m.b272 >= -1.88764124093134)

m.c357 = Constraint(expr= - m.x83 + m.x134 - 4.19022633392538*m.b273 >= -1.88764124093134)

m.c358 = Constraint(expr= - m.x84 + m.x135 - 4.19022633392538*m.b274 >= -1.88764124093134)

m.c359 = Constraint(expr= - m.x85 + m.x136 - 4.19022633392538*m.b275 >= -1.88764124093134)

m.c360 = Constraint(expr= - m.x86 + m.x137 - 4.19022633392538*m.b276 >= -1.88764124093134)

m.c361 = Constraint(expr= - m.x87 + m.x138 - 4.19022633392538*m.b277 >= -1.88764124093134)

m.c362 = Constraint(expr= - m.x88 + m.x139 - 4.19022633392538*m.b278 >= -1.88764124093134)

m.c363 = Constraint(expr= - m.x89 + m.x140 - 4.19022633392538*m.b279 >= -1.88764124093134)

m.c364 = Constraint(expr= - m.x91 + m.x132 - 4.20927452889608*m.b271 >= -1.90668943590203)

m.c365 = Constraint(expr= - m.x92 + m.x133 - 4.20927452889608*m.b272 >= -1.90668943590203)

m.c366 = Constraint(expr= - m.x93 + m.x134 - 4.20927452889608*m.b273 >= -1.90668943590203)

m.c367 = Constraint(expr= - m.x94 + m.x135 - 4.20927452889608*m.b274 >= -1.90668943590203)

m.c368 = Constraint(expr= - m.x95 + m.x136 - 4.20927452889608*m.b275 >= -1.90668943590203)

m.c369 = Constraint(expr= - m.x96 + m.x137 - 4.20927452889608*m.b276 >= -1.90668943590203)

m.c370 = Constraint(expr= - m.x97 + m.x138 - 4.20927452889608*m.b277 >= -1.90668943590203)

m.c371 = Constraint(expr= - m.x98 + m.x139 - 4.20927452889608*m.b278 >= -1.90668943590203)

m.c372 = Constraint(expr= - m.x99 + m.x140 - 4.20927452889608*m.b279 >= -1.90668943590203)

m.c373 = Constraint(expr= - m.x101 + m.x132 - 4.03338386243241*m.b271 >= -1.73079876943837)

m.c374 = Constraint(expr= - m.x102 + m.x133 - 4.03338386243241*m.b272 >= -1.73079876943837)

m.c375 = Constraint(expr= - m.x103 + m.x134 - 4.03338386243241*m.b273 >= -1.73079876943837)

m.c376 = Constraint(expr= - m.x104 + m.x135 - 4.03338386243241*m.b274 >= -1.73079876943837)

m.c377 = Constraint(expr= - m.x105 + m.x136 - 4.03338386243241*m.b275 >= -1.73079876943837)

m.c378 = Constraint(expr= - m.x106 + m.x137 - 4.03338386243241*m.b276 >= -1.73079876943837)

m.c379 = Constraint(expr= - m.x107 + m.x138 - 4.03338386243241*m.b277 >= -1.73079876943837)

m.c380 = Constraint(expr= - m.x108 + m.x139 - 4.03338386243241*m.b278 >= -1.73079876943837)

m.c381 = Constraint(expr= - m.x109 + m.x140 - 4.03338386243241*m.b279 >= -1.73079876943837)

m.c382 = Constraint(expr=   m.x111 + 1.79175946922805*m.b151 <= 1.79175946922805)

m.c383 = Constraint(expr=   m.x111 + 1.09861228866811*m.b161 <= 1.79175946922805)

m.c384 = Constraint(expr=   m.x111 + 0.693147180559945*m.b171 <= 1.79175946922805)

m.c385 = Constraint(expr=   m.x111 + 0.405465108108164*m.b181 <= 1.79175946922805)

m.c386 = Constraint(expr=   m.x111 + 0.182321556793955*m.b191 <= 1.79175946922805)

m.c387 = Constraint(expr=   m.x111 <= 1.79175946922805)

m.c388 = Constraint(expr=   m.x112 + 1.79175946922805*m.b152 <= 1.79175946922805)

m.c389 = Constraint(expr=   m.x112 + 1.09861228866811*m.b162 <= 1.79175946922805)

m.c390 = Constraint(expr=   m.x112 + 0.693147180559945*m.b172 <= 1.79175946922805)

m.c391 = Constraint(expr=   m.x112 + 0.405465108108164*m.b182 <= 1.79175946922805)

m.c392 = Constraint(expr=   m.x112 + 0.182321556793955*m.b192 <= 1.79175946922805)

m.c393 = Constraint(expr=   m.x112 <= 1.79175946922805)

m.c394 = Constraint(expr=   m.x113 + 1.79175946922805*m.b153 <= 1.79175946922805)

m.c395 = Constraint(expr=   m.x113 + 1.09861228866811*m.b163 <= 1.79175946922805)

m.c396 = Constraint(expr=   m.x113 + 0.693147180559945*m.b173 <= 1.79175946922805)

m.c397 = Constraint(expr=   m.x113 + 0.405465108108164*m.b183 <= 1.79175946922805)

m.c398 = Constraint(expr=   m.x113 + 0.182321556793955*m.b193 <= 1.79175946922805)

m.c399 = Constraint(expr=   m.x113 <= 1.79175946922805)

m.c400 = Constraint(expr=   m.x114 + 1.79175946922805*m.b154 <= 1.79175946922805)

m.c401 = Constraint(expr=   m.x114 + 1.09861228866811*m.b164 <= 1.79175946922805)

m.c402 = Constraint(expr=   m.x114 + 0.693147180559945*m.b174 <= 1.79175946922805)

m.c403 = Constraint(expr=   m.x114 + 0.405465108108164*m.b184 <= 1.79175946922805)

m.c404 = Constraint(expr=   m.x114 + 0.182321556793955*m.b194 <= 1.79175946922805)

m.c405 = Constraint(expr=   m.x114 <= 1.79175946922805)

m.c406 = Constraint(expr=   m.x115 + 1.79175946922805*m.b155 <= 1.79175946922805)

m.c407 = Constraint(expr=   m.x115 + 1.09861228866811*m.b165 <= 1.79175946922805)

m.c408 = Constraint(expr=   m.x115 + 0.693147180559945*m.b175 <= 1.79175946922805)

m.c409 = Constraint(expr=   m.x115 + 0.405465108108164*m.b185 <= 1.79175946922805)

m.c410 = Constraint(expr=   m.x115 + 0.182321556793955*m.b195 <= 1.79175946922805)

m.c411 = Constraint(expr=   m.x115 <= 1.79175946922805)

m.c412 = Constraint(expr=   m.x116 + 1.79175946922805*m.b156 <= 1.79175946922805)

m.c413 = Constraint(expr=   m.x116 + 1.09861228866811*m.b166 <= 1.79175946922805)

m.c414 = Constraint(expr=   m.x116 + 0.693147180559945*m.b176 <= 1.79175946922805)

m.c415 = Constraint(expr=   m.x116 + 0.405465108108164*m.b186 <= 1.79175946922805)

m.c416 = Constraint(expr=   m.x116 + 0.182321556793955*m.b196 <= 1.79175946922805)

m.c417 = Constraint(expr=   m.x116 <= 1.79175946922805)

m.c418 = Constraint(expr=   m.x117 + 1.79175946922805*m.b157 <= 1.79175946922805)

m.c419 = Constraint(expr=   m.x117 + 1.09861228866811*m.b167 <= 1.79175946922805)

m.c420 = Constraint(expr=   m.x117 + 0.693147180559945*m.b177 <= 1.79175946922805)

m.c421 = Constraint(expr=   m.x117 + 0.405465108108164*m.b187 <= 1.79175946922805)

m.c422 = Constraint(expr=   m.x117 + 0.182321556793955*m.b197 <= 1.79175946922805)

m.c423 = Constraint(expr=   m.x117 <= 1.79175946922805)

m.c424 = Constraint(expr=   m.x118 + 1.79175946922805*m.b158 <= 1.79175946922805)

m.c425 = Constraint(expr=   m.x118 + 1.09861228866811*m.b168 <= 1.79175946922805)

m.c426 = Constraint(expr=   m.x118 + 0.693147180559945*m.b178 <= 1.79175946922805)

m.c427 = Constraint(expr=   m.x118 + 0.405465108108164*m.b188 <= 1.79175946922805)

m.c428 = Constraint(expr=   m.x118 + 0.182321556793955*m.b198 <= 1.79175946922805)

m.c429 = Constraint(expr=   m.x118 <= 1.79175946922805)

m.c430 = Constraint(expr=   m.x119 + 1.79175946922805*m.b159 <= 1.79175946922805)

m.c431 = Constraint(expr=   m.x119 + 1.09861228866811*m.b169 <= 1.79175946922805)

m.c432 = Constraint(expr=   m.x119 + 0.693147180559945*m.b179 <= 1.79175946922805)

m.c433 = Constraint(expr=   m.x119 + 0.405465108108164*m.b189 <= 1.79175946922805)

m.c434 = Constraint(expr=   m.x119 + 0.182321556793955*m.b199 <= 1.79175946922805)

m.c435 = Constraint(expr=   m.x119 <= 1.79175946922805)

m.c436 = Constraint(expr=   m.x120 + 1.79175946922805*m.b160 <= 1.79175946922805)

m.c437 = Constraint(expr=   m.x120 + 1.09861228866811*m.b170 <= 1.79175946922805)

m.c438 = Constraint(expr=   m.x120 + 0.693147180559945*m.b180 <= 1.79175946922805)

m.c439 = Constraint(expr=   m.x120 + 0.405465108108164*m.b190 <= 1.79175946922805)

m.c440 = Constraint(expr=   m.x120 + 0.182321556793955*m.b200 <= 1.79175946922805)

m.c441 = Constraint(expr=   m.x120 <= 1.79175946922805)

m.c442 = Constraint(expr=   m.x111 >= 0)

m.c443 = Constraint(expr=   m.x111 - 0.693147180559945*m.b161 >= 0)

m.c444 = Constraint(expr=   m.x111 - 1.09861228866811*m.b171 >= 0)

m.c445 = Constraint(expr=   m.x111 - 1.38629436111989*m.b181 >= 0)

m.c446 = Constraint(expr=   m.x111 - 1.6094379124341*m.b191 >= 0)

m.c447 = Constraint(expr=   m.x111 - 1.79175946922805*m.b201 >= 0)

m.c448 = Constraint(expr=   m.x112 >= 0)

m.c449 = Constraint(expr=   m.x112 - 0.693147180559945*m.b162 >= 0)

m.c450 = Constraint(expr=   m.x112 - 1.09861228866811*m.b172 >= 0)

m.c451 = Constraint(expr=   m.x112 - 1.38629436111989*m.b182 >= 0)

m.c452 = Constraint(expr=   m.x112 - 1.6094379124341*m.b192 >= 0)

m.c453 = Constraint(expr=   m.x112 - 1.79175946922805*m.b202 >= 0)

m.c454 = Constraint(expr=   m.x113 >= 0)

m.c455 = Constraint(expr=   m.x113 - 0.693147180559945*m.b163 >= 0)

m.c456 = Constraint(expr=   m.x113 - 1.09861228866811*m.b173 >= 0)

m.c457 = Constraint(expr=   m.x113 - 1.38629436111989*m.b183 >= 0)

m.c458 = Constraint(expr=   m.x113 - 1.6094379124341*m.b193 >= 0)

m.c459 = Constraint(expr=   m.x113 - 1.79175946922805*m.b203 >= 0)

m.c460 = Constraint(expr=   m.x114 >= 0)

m.c461 = Constraint(expr=   m.x114 - 0.693147180559945*m.b164 >= 0)

m.c462 = Constraint(expr=   m.x114 - 1.09861228866811*m.b174 >= 0)

m.c463 = Constraint(expr=   m.x114 - 1.38629436111989*m.b184 >= 0)

m.c464 = Constraint(expr=   m.x114 - 1.6094379124341*m.b194 >= 0)

m.c465 = Constraint(expr=   m.x114 - 1.79175946922805*m.b204 >= 0)

m.c466 = Constraint(expr=   m.x115 >= 0)

m.c467 = Constraint(expr=   m.x115 - 0.693147180559945*m.b165 >= 0)

m.c468 = Constraint(expr=   m.x115 - 1.09861228866811*m.b175 >= 0)

m.c469 = Constraint(expr=   m.x115 - 1.38629436111989*m.b185 >= 0)

m.c470 = Constraint(expr=   m.x115 - 1.6094379124341*m.b195 >= 0)

m.c471 = Constraint(expr=   m.x115 - 1.79175946922805*m.b205 >= 0)

m.c472 = Constraint(expr=   m.x116 >= 0)

m.c473 = Constraint(expr=   m.x116 - 0.693147180559945*m.b166 >= 0)

m.c474 = Constraint(expr=   m.x116 - 1.09861228866811*m.b176 >= 0)

m.c475 = Constraint(expr=   m.x116 - 1.38629436111989*m.b186 >= 0)

m.c476 = Constraint(expr=   m.x116 - 1.6094379124341*m.b196 >= 0)

m.c477 = Constraint(expr=   m.x116 - 1.79175946922805*m.b206 >= 0)

m.c478 = Constraint(expr=   m.x117 >= 0)

m.c479 = Constraint(expr=   m.x117 - 0.693147180559945*m.b167 >= 0)

m.c480 = Constraint(expr=   m.x117 - 1.09861228866811*m.b177 >= 0)

m.c481 = Constraint(expr=   m.x117 - 1.38629436111989*m.b187 >= 0)

m.c482 = Constraint(expr=   m.x117 - 1.6094379124341*m.b197 >= 0)

m.c483 = Constraint(expr=   m.x117 - 1.79175946922805*m.b207 >= 0)

m.c484 = Constraint(expr=   m.x118 >= 0)

m.c485 = Constraint(expr=   m.x118 - 0.693147180559945*m.b168 >= 0)

m.c486 = Constraint(expr=   m.x118 - 1.09861228866811*m.b178 >= 0)

m.c487 = Constraint(expr=   m.x118 - 1.38629436111989*m.b188 >= 0)

m.c488 = Constraint(expr=   m.x118 - 1.6094379124341*m.b198 >= 0)

m.c489 = Constraint(expr=   m.x118 - 1.79175946922805*m.b208 >= 0)

m.c490 = Constraint(expr=   m.x119 >= 0)

m.c491 = Constraint(expr=   m.x119 - 0.693147180559945*m.b169 >= 0)

m.c492 = Constraint(expr=   m.x119 - 1.09861228866811*m.b179 >= 0)

m.c493 = Constraint(expr=   m.x119 - 1.38629436111989*m.b189 >= 0)

m.c494 = Constraint(expr=   m.x119 - 1.6094379124341*m.b199 >= 0)

m.c495 = Constraint(expr=   m.x119 - 1.79175946922805*m.b209 >= 0)

m.c496 = Constraint(expr=   m.x120 >= 0)

m.c497 = Constraint(expr=   m.x120 - 0.693147180559945*m.b170 >= 0)

m.c498 = Constraint(expr=   m.x120 - 1.09861228866811*m.b180 >= 0)

m.c499 = Constraint(expr=   m.x120 - 1.38629436111989*m.b190 >= 0)

m.c500 = Constraint(expr=   m.x120 - 1.6094379124341*m.b200 >= 0)

m.c501 = Constraint(expr=   m.x120 - 1.79175946922805*m.b210 >= 0)

m.c502 = Constraint(expr=   m.x121 + 1.79175946922805*m.b211 <= 1.79175946922805)

m.c503 = Constraint(expr=   m.x121 + 1.09861228866811*m.b221 <= 1.79175946922805)

m.c504 = Constraint(expr=   m.x121 + 0.693147180559945*m.b231 <= 1.79175946922805)

m.c505 = Constraint(expr=   m.x121 + 0.405465108108164*m.b241 <= 1.79175946922805)

m.c506 = Constraint(expr=   m.x121 + 0.182321556793955*m.b251 <= 1.79175946922805)

m.c507 = Constraint(expr=   m.x121 <= 1.79175946922805)

m.c508 = Constraint(expr=   m.x122 + 1.79175946922805*m.b212 <= 1.79175946922805)

m.c509 = Constraint(expr=   m.x122 + 1.09861228866811*m.b222 <= 1.79175946922805)

m.c510 = Constraint(expr=   m.x122 + 0.693147180559945*m.b232 <= 1.79175946922805)

m.c511 = Constraint(expr=   m.x122 + 0.405465108108164*m.b242 <= 1.79175946922805)

m.c512 = Constraint(expr=   m.x122 + 0.182321556793955*m.b252 <= 1.79175946922805)

m.c513 = Constraint(expr=   m.x122 <= 1.79175946922805)

m.c514 = Constraint(expr=   m.x123 + 1.79175946922805*m.b213 <= 1.79175946922805)

m.c515 = Constraint(expr=   m.x123 + 1.09861228866811*m.b223 <= 1.79175946922805)

m.c516 = Constraint(expr=   m.x123 + 0.693147180559945*m.b233 <= 1.79175946922805)

m.c517 = Constraint(expr=   m.x123 + 0.405465108108164*m.b243 <= 1.79175946922805)

m.c518 = Constraint(expr=   m.x123 + 0.182321556793955*m.b253 <= 1.79175946922805)

m.c519 = Constraint(expr=   m.x123 <= 1.79175946922805)

m.c520 = Constraint(expr=   m.x124 + 1.79175946922805*m.b214 <= 1.79175946922805)

m.c521 = Constraint(expr=   m.x124 + 1.09861228866811*m.b224 <= 1.79175946922805)

m.c522 = Constraint(expr=   m.x124 + 0.693147180559945*m.b234 <= 1.79175946922805)

m.c523 = Constraint(expr=   m.x124 + 0.405465108108164*m.b244 <= 1.79175946922805)

m.c524 = Constraint(expr=   m.x124 + 0.182321556793955*m.b254 <= 1.79175946922805)

m.c525 = Constraint(expr=   m.x124 <= 1.79175946922805)

m.c526 = Constraint(expr=   m.x125 + 1.79175946922805*m.b215 <= 1.79175946922805)

m.c527 = Constraint(expr=   m.x125 + 1.09861228866811*m.b225 <= 1.79175946922805)

m.c528 = Constraint(expr=   m.x125 + 0.693147180559945*m.b235 <= 1.79175946922805)

m.c529 = Constraint(expr=   m.x125 + 0.405465108108164*m.b245 <= 1.79175946922805)

m.c530 = Constraint(expr=   m.x125 + 0.182321556793955*m.b255 <= 1.79175946922805)

m.c531 = Constraint(expr=   m.x125 <= 1.79175946922805)

m.c532 = Constraint(expr=   m.x126 + 1.79175946922805*m.b216 <= 1.79175946922805)

m.c533 = Constraint(expr=   m.x126 + 1.09861228866811*m.b226 <= 1.79175946922805)

m.c534 = Constraint(expr=   m.x126 + 0.693147180559945*m.b236 <= 1.79175946922805)

m.c535 = Constraint(expr=   m.x126 + 0.405465108108164*m.b246 <= 1.79175946922805)

m.c536 = Constraint(expr=   m.x126 + 0.182321556793955*m.b256 <= 1.79175946922805)

m.c537 = Constraint(expr=   m.x126 <= 1.79175946922805)

m.c538 = Constraint(expr=   m.x127 + 1.79175946922805*m.b217 <= 1.79175946922805)

m.c539 = Constraint(expr=   m.x127 + 1.09861228866811*m.b227 <= 1.79175946922805)

m.c540 = Constraint(expr=   m.x127 + 0.693147180559945*m.b237 <= 1.79175946922805)

m.c541 = Constraint(expr=   m.x127 + 0.405465108108164*m.b247 <= 1.79175946922805)

m.c542 = Constraint(expr=   m.x127 + 0.182321556793955*m.b257 <= 1.79175946922805)

m.c543 = Constraint(expr=   m.x127 <= 1.79175946922805)

m.c544 = Constraint(expr=   m.x128 + 1.79175946922805*m.b218 <= 1.79175946922805)

m.c545 = Constraint(expr=   m.x128 + 1.09861228866811*m.b228 <= 1.79175946922805)

m.c546 = Constraint(expr=   m.x128 + 0.693147180559945*m.b238 <= 1.79175946922805)

m.c547 = Constraint(expr=   m.x128 + 0.405465108108164*m.b248 <= 1.79175946922805)

m.c548 = Constraint(expr=   m.x128 + 0.182321556793955*m.b258 <= 1.79175946922805)

m.c549 = Constraint(expr=   m.x128 <= 1.79175946922805)

m.c550 = Constraint(expr=   m.x129 + 1.79175946922805*m.b219 <= 1.79175946922805)

m.c551 = Constraint(expr=   m.x129 + 1.09861228866811*m.b229 <= 1.79175946922805)

m.c552 = Constraint(expr=   m.x129 + 0.693147180559945*m.b239 <= 1.79175946922805)

m.c553 = Constraint(expr=   m.x129 + 0.405465108108164*m.b249 <= 1.79175946922805)

m.c554 = Constraint(expr=   m.x129 + 0.182321556793955*m.b259 <= 1.79175946922805)

m.c555 = Constraint(expr=   m.x129 <= 1.79175946922805)

m.c556 = Constraint(expr=   m.x130 + 1.79175946922805*m.b220 <= 1.79175946922805)

m.c557 = Constraint(expr=   m.x130 + 1.09861228866811*m.b230 <= 1.79175946922805)

m.c558 = Constraint(expr=   m.x130 + 0.693147180559945*m.b240 <= 1.79175946922805)

m.c559 = Constraint(expr=   m.x130 + 0.405465108108164*m.b250 <= 1.79175946922805)

m.c560 = Constraint(expr=   m.x130 + 0.182321556793955*m.b260 <= 1.79175946922805)

m.c561 = Constraint(expr=   m.x130 <= 1.79175946922805)

m.c562 = Constraint(expr=   m.x121 >= 0)

m.c563 = Constraint(expr=   m.x121 - 0.693147180559945*m.b221 >= 0)

m.c564 = Constraint(expr=   m.x121 - 1.09861228866811*m.b231 >= 0)

m.c565 = Constraint(expr=   m.x121 - 1.38629436111989*m.b241 >= 0)

m.c566 = Constraint(expr=   m.x121 - 1.6094379124341*m.b251 >= 0)

m.c567 = Constraint(expr=   m.x121 - 1.79175946922805*m.b261 >= 0)

m.c568 = Constraint(expr=   m.x122 >= 0)

m.c569 = Constraint(expr=   m.x122 - 0.693147180559945*m.b222 >= 0)

m.c570 = Constraint(expr=   m.x122 - 1.09861228866811*m.b232 >= 0)

m.c571 = Constraint(expr=   m.x122 - 1.38629436111989*m.b242 >= 0)

m.c572 = Constraint(expr=   m.x122 - 1.6094379124341*m.b252 >= 0)

m.c573 = Constraint(expr=   m.x122 - 1.79175946922805*m.b262 >= 0)

m.c574 = Constraint(expr=   m.x123 >= 0)

m.c575 = Constraint(expr=   m.x123 - 0.693147180559945*m.b223 >= 0)

m.c576 = Constraint(expr=   m.x123 - 1.09861228866811*m.b233 >= 0)

m.c577 = Constraint(expr=   m.x123 - 1.38629436111989*m.b243 >= 0)

m.c578 = Constraint(expr=   m.x123 - 1.6094379124341*m.b253 >= 0)

m.c579 = Constraint(expr=   m.x123 - 1.79175946922805*m.b263 >= 0)

m.c580 = Constraint(expr=   m.x124 >= 0)

m.c581 = Constraint(expr=   m.x124 - 0.693147180559945*m.b224 >= 0)

m.c582 = Constraint(expr=   m.x124 - 1.09861228866811*m.b234 >= 0)

m.c583 = Constraint(expr=   m.x124 - 1.38629436111989*m.b244 >= 0)

m.c584 = Constraint(expr=   m.x124 - 1.6094379124341*m.b254 >= 0)

m.c585 = Constraint(expr=   m.x124 - 1.79175946922805*m.b264 >= 0)

m.c586 = Constraint(expr=   m.x125 >= 0)

m.c587 = Constraint(expr=   m.x125 - 0.693147180559945*m.b225 >= 0)

m.c588 = Constraint(expr=   m.x125 - 1.09861228866811*m.b235 >= 0)

m.c589 = Constraint(expr=   m.x125 - 1.38629436111989*m.b245 >= 0)

m.c590 = Constraint(expr=   m.x125 - 1.6094379124341*m.b255 >= 0)

m.c591 = Constraint(expr=   m.x125 - 1.79175946922805*m.b265 >= 0)

m.c592 = Constraint(expr=   m.x126 >= 0)

m.c593 = Constraint(expr=   m.x126 - 0.693147180559945*m.b226 >= 0)

m.c594 = Constraint(expr=   m.x126 - 1.09861228866811*m.b236 >= 0)

m.c595 = Constraint(expr=   m.x126 - 1.38629436111989*m.b246 >= 0)

m.c596 = Constraint(expr=   m.x126 - 1.6094379124341*m.b256 >= 0)

m.c597 = Constraint(expr=   m.x126 - 1.79175946922805*m.b266 >= 0)

m.c598 = Constraint(expr=   m.x127 >= 0)

m.c599 = Constraint(expr=   m.x127 - 0.693147180559945*m.b227 >= 0)

m.c600 = Constraint(expr=   m.x127 - 1.09861228866811*m.b237 >= 0)

m.c601 = Constraint(expr=   m.x127 - 1.38629436111989*m.b247 >= 0)

m.c602 = Constraint(expr=   m.x127 - 1.6094379124341*m.b257 >= 0)

m.c603 = Constraint(expr=   m.x127 - 1.79175946922805*m.b267 >= 0)

m.c604 = Constraint(expr=   m.x128 >= 0)

m.c605 = Constraint(expr=   m.x128 - 0.693147180559945*m.b228 >= 0)

m.c606 = Constraint(expr=   m.x128 - 1.09861228866811*m.b238 >= 0)

m.c607 = Constraint(expr=   m.x128 - 1.38629436111989*m.b248 >= 0)

m.c608 = Constraint(expr=   m.x128 - 1.6094379124341*m.b258 >= 0)

m.c609 = Constraint(expr=   m.x128 - 1.79175946922805*m.b268 >= 0)

m.c610 = Constraint(expr=   m.x129 >= 0)

m.c611 = Constraint(expr=   m.x129 - 0.693147180559945*m.b229 >= 0)

m.c612 = Constraint(expr=   m.x129 - 1.09861228866811*m.b239 >= 0)

m.c613 = Constraint(expr=   m.x129 - 1.38629436111989*m.b249 >= 0)

m.c614 = Constraint(expr=   m.x129 - 1.6094379124341*m.b259 >= 0)

m.c615 = Constraint(expr=   m.x129 - 1.79175946922805*m.b269 >= 0)

m.c616 = Constraint(expr=   m.x130 >= 0)

m.c617 = Constraint(expr=   m.x130 - 0.693147180559945*m.b230 >= 0)

m.c618 = Constraint(expr=   m.x130 - 1.09861228866811*m.b240 >= 0)

m.c619 = Constraint(expr=   m.x130 - 1.38629436111989*m.b250 >= 0)

m.c620 = Constraint(expr=   m.x130 - 1.6094379124341*m.b260 >= 0)

m.c621 = Constraint(expr=   m.x130 - 1.79175946922805*m.b270 >= 0)

m.c622 = Constraint(expr=   m.b151 + m.b161 + m.b171 + m.b181 + m.b191 + m.b201 == 1)

m.c623 = Constraint(expr=   m.b152 + m.b162 + m.b172 + m.b182 + m.b192 + m.b202 == 1)

m.c624 = Constraint(expr=   m.b153 + m.b163 + m.b173 + m.b183 + m.b193 + m.b203 == 1)

m.c625 = Constraint(expr=   m.b154 + m.b164 + m.b174 + m.b184 + m.b194 + m.b204 == 1)

m.c626 = Constraint(expr=   m.b155 + m.b165 + m.b175 + m.b185 + m.b195 + m.b205 == 1)

m.c627 = Constraint(expr=   m.b156 + m.b166 + m.b176 + m.b186 + m.b196 + m.b206 == 1)

m.c628 = Constraint(expr=   m.b157 + m.b167 + m.b177 + m.b187 + m.b197 + m.b207 == 1)

m.c629 = Constraint(expr=   m.b158 + m.b168 + m.b178 + m.b188 + m.b198 + m.b208 == 1)

m.c630 = Constraint(expr=   m.b159 + m.b169 + m.b179 + m.b189 + m.b199 + m.b209 == 1)

m.c631 = Constraint(expr=   m.b160 + m.b170 + m.b180 + m.b190 + m.b200 + m.b210 == 1)

m.c632 = Constraint(expr=   m.b211 + m.b221 + m.b231 + m.b241 + m.b251 + m.b261 == 1)

m.c633 = Constraint(expr=   m.b212 + m.b222 + m.b232 + m.b242 + m.b252 + m.b262 == 1)

m.c634 = Constraint(expr=   m.b213 + m.b223 + m.b233 + m.b243 + m.b253 + m.b263 == 1)

m.c635 = Constraint(expr=   m.b214 + m.b224 + m.b234 + m.b244 + m.b254 + m.b264 == 1)

m.c636 = Constraint(expr=   m.b215 + m.b225 + m.b235 + m.b245 + m.b255 + m.b265 == 1)

m.c637 = Constraint(expr=   m.b216 + m.b226 + m.b236 + m.b246 + m.b256 + m.b266 == 1)

m.c638 = Constraint(expr=   m.b217 + m.b227 + m.b237 + m.b247 + m.b257 + m.b267 == 1)

m.c639 = Constraint(expr=   m.b218 + m.b228 + m.b238 + m.b248 + m.b258 + m.b268 == 1)

m.c640 = Constraint(expr=   m.b219 + m.b229 + m.b239 + m.b249 + m.b259 + m.b269 == 1)

m.c641 = Constraint(expr=   m.b220 + m.b230 + m.b240 + m.b250 + m.b260 + m.b270 == 1)

m.c642 = Constraint(expr=   m.x11 - m.x12 + 1.45937721785837*m.b271 <= 2.55798950652648)

m.c643 = Constraint(expr=   m.x12 - m.x13 + 1.45937721785837*m.b272 <= 2.55798950652648)

m.c644 = Constraint(expr=   m.x13 - m.x14 + 1.45937721785837*m.b273 <= 2.55798950652648)

m.c645 = Constraint(expr=   m.x14 - m.x15 + 1.45937721785837*m.b274 <= 2.55798950652648)

m.c646 = Constraint(expr=   m.x15 - m.x16 + 1.45937721785837*m.b275 <= 2.55798950652648)

m.c647 = Constraint(expr=   m.x16 - m.x17 + 1.45937721785837*m.b276 <= 2.55798950652648)

m.c648 = Constraint(expr=   m.x17 - m.x18 + 1.45937721785837*m.b277 <= 2.55798950652648)

m.c649 = Constraint(expr=   m.x18 - m.x19 + 1.45937721785837*m.b278 <= 2.55798950652648)

m.c650 = Constraint(expr=   m.x19 - m.x20 + 1.45937721785837*m.b279 <= 2.55798950652648)

m.c651 = Constraint(expr=   m.x21 - m.x22 + 2.53921199464554*m.b271 <= 3.63782428331365)

m.c652 = Constraint(expr=   m.x22 - m.x23 + 2.53921199464554*m.b272 <= 3.63782428331365)

m.c653 = Constraint(expr=   m.x23 - m.x24 + 2.53921199464554*m.b273 <= 3.63782428331365)

m.c654 = Constraint(expr=   m.x24 - m.x25 + 2.53921199464554*m.b274 <= 3.63782428331365)

m.c655 = Constraint(expr=   m.x25 - m.x26 + 2.53921199464554*m.b275 <= 3.63782428331365)

m.c656 = Constraint(expr=   m.x26 - m.x27 + 2.53921199464554*m.b276 <= 3.63782428331365)

m.c657 = Constraint(expr=   m.x27 - m.x28 + 2.53921199464554*m.b277 <= 3.63782428331365)

m.c658 = Constraint(expr=   m.x28 - m.x29 + 2.53921199464554*m.b278 <= 3.63782428331365)

m.c659 = Constraint(expr=   m.x29 - m.x30 + 2.53921199464554*m.b279 <= 3.63782428331365)

m.c660 = Constraint(expr=   m.x31 - m.x32 + 2.15330339027829*m.b271 <= 3.2519156789464)

m.c661 = Constraint(expr=   m.x32 - m.x33 + 2.15330339027829*m.b272 <= 3.2519156789464)

m.c662 = Constraint(expr=   m.x33 - m.x34 + 2.15330339027829*m.b273 <= 3.2519156789464)

m.c663 = Constraint(expr=   m.x34 - m.x35 + 2.15330339027829*m.b274 <= 3.2519156789464)

m.c664 = Constraint(expr=   m.x35 - m.x36 + 2.15330339027829*m.b275 <= 3.2519156789464)

m.c665 = Constraint(expr=   m.x36 - m.x37 + 2.15330339027829*m.b276 <= 3.2519156789464)

m.c666 = Constraint(expr=   m.x37 - m.x38 + 2.15330339027829*m.b277 <= 3.2519156789464)

m.c667 = Constraint(expr=   m.x38 - m.x39 + 2.15330339027829*m.b278 <= 3.2519156789464)

m.c668 = Constraint(expr=   m.x39 - m.x40 + 2.15330339027829*m.b279 <= 3.2519156789464)

m.c669 = Constraint(expr=   m.x41 - m.x42 + 1.98784387242826*m.b271 <= 3.08645616109637)

m.c670 = Constraint(expr=   m.x42 - m.x43 + 1.98784387242826*m.b272 <= 3.08645616109637)

m.c671 = Constraint(expr=   m.x43 - m.x44 + 1.98784387242826*m.b273 <= 3.08645616109637)

m.c672 = Constraint(expr=   m.x44 - m.x45 + 1.98784387242826*m.b274 <= 3.08645616109637)

m.c673 = Constraint(expr=   m.x45 - m.x46 + 1.98784387242826*m.b275 <= 3.08645616109637)

m.c674 = Constraint(expr=   m.x46 - m.x47 + 1.98784387242826*m.b276 <= 3.08645616109637)

m.c675 = Constraint(expr=   m.x47 - m.x48 + 1.98784387242826*m.b277 <= 3.08645616109637)

m.c676 = Constraint(expr=   m.x48 - m.x49 + 1.98784387242826*m.b278 <= 3.08645616109637)

m.c677 = Constraint(expr=   m.x49 - m.x50 + 1.98784387242826*m.b279 <= 3.08645616109637)

m.c678 = Constraint(expr=   m.x51 - m.x52 + 2.7246152179769*m.b271 <= 3.82322750664501)

m.c679 = Constraint(expr=   m.x52 - m.x53 + 2.7246152179769*m.b272 <= 3.82322750664501)

m.c680 = Constraint(expr=   m.x53 - m.x54 + 2.7246152179769*m.b273 <= 3.82322750664501)

m.c681 = Constraint(expr=   m.x54 - m.x55 + 2.7246152179769*m.b274 <= 3.82322750664501)

m.c682 = Constraint(expr=   m.x55 - m.x56 + 2.7246152179769*m.b275 <= 3.82322750664501)

m.c683 = Constraint(expr=   m.x56 - m.x57 + 2.7246152179769*m.b276 <= 3.82322750664501)

m.c684 = Constraint(expr=   m.x57 - m.x58 + 2.7246152179769*m.b277 <= 3.82322750664501)

m.c685 = Constraint(expr=   m.x58 - m.x59 + 2.7246152179769*m.b278 <= 3.82322750664501)

m.c686 = Constraint(expr=   m.x59 - m.x60 + 2.7246152179769*m.b279 <= 3.82322750664501)

m.c687 = Constraint(expr=   m.x61 - m.x62 + 2.86282607632339*m.b271 <= 3.9614383649915)

m.c688 = Constraint(expr=   m.x62 - m.x63 + 2.86282607632339*m.b272 <= 3.9614383649915)

m.c689 = Constraint(expr=   m.x63 - m.x64 + 2.86282607632339*m.b273 <= 3.9614383649915)

m.c690 = Constraint(expr=   m.x64 - m.x65 + 2.86282607632339*m.b274 <= 3.9614383649915)

m.c691 = Constraint(expr=   m.x65 - m.x66 + 2.86282607632339*m.b275 <= 3.9614383649915)

m.c692 = Constraint(expr=   m.x66 - m.x67 + 2.86282607632339*m.b276 <= 3.9614383649915)

m.c693 = Constraint(expr=   m.x67 - m.x68 + 2.86282607632339*m.b277 <= 3.9614383649915)

m.c694 = Constraint(expr=   m.x68 - m.x69 + 2.86282607632339*m.b278 <= 3.9614383649915)

m.c695 = Constraint(expr=   m.x69 - m.x70 + 2.86282607632339*m.b279 <= 3.9614383649915)

m.c696 = Constraint(expr=   m.x71 - m.x72 + 1.84763467312072*m.b271 <= 2.94624696178883)

m.c697 = Constraint(expr=   m.x72 - m.x73 + 1.84763467312072*m.b272 <= 2.94624696178883)

m.c698 = Constraint(expr=   m.x73 - m.x74 + 1.84763467312072*m.b273 <= 2.94624696178883)

m.c699 = Constraint(expr=   m.x74 - m.x75 + 1.84763467312072*m.b274 <= 2.94624696178883)

m.c700 = Constraint(expr=   m.x75 - m.x76 + 1.84763467312072*m.b275 <= 2.94624696178883)

m.c701 = Constraint(expr=   m.x76 - m.x77 + 1.84763467312072*m.b276 <= 2.94624696178883)

m.c702 = Constraint(expr=   m.x77 - m.x78 + 1.84763467312072*m.b277 <= 2.94624696178883)

m.c703 = Constraint(expr=   m.x78 - m.x79 + 1.84763467312072*m.b278 <= 2.94624696178883)

m.c704 = Constraint(expr=   m.x79 - m.x80 + 1.84763467312072*m.b279 <= 2.94624696178883)

m.c705 = Constraint(expr=   m.x81 - m.x82 + 2.22778688291886*m.b271 <= 3.32639917158697)

m.c706 = Constraint(expr=   m.x82 - m.x83 + 2.22778688291886*m.b272 <= 3.32639917158697)

m.c707 = Constraint(expr=   m.x83 - m.x84 + 2.22778688291886*m.b273 <= 3.32639917158697)

m.c708 = Constraint(expr=   m.x84 - m.x85 + 2.22778688291886*m.b274 <= 3.32639917158697)

m.c709 = Constraint(expr=   m.x85 - m.x86 + 2.22778688291886*m.b275 <= 3.32639917158697)

m.c710 = Constraint(expr=   m.x86 - m.x87 + 2.22778688291886*m.b276 <= 3.32639917158697)

m.c711 = Constraint(expr=   m.x87 - m.x88 + 2.22778688291886*m.b277 <= 3.32639917158697)

m.c712 = Constraint(expr=   m.x88 - m.x89 + 2.22778688291886*m.b278 <= 3.32639917158697)

m.c713 = Constraint(expr=   m.x89 - m.x90 + 2.22778688291886*m.b279 <= 3.32639917158697)

m.c714 = Constraint(expr=   m.x91 - m.x92 + 1.87188551370734*m.b271 <= 2.97049780237545)

m.c715 = Constraint(expr=   m.x92 - m.x93 + 1.87188551370734*m.b272 <= 2.97049780237545)

m.c716 = Constraint(expr=   m.x93 - m.x94 + 1.87188551370734*m.b273 <= 2.97049780237545)

m.c717 = Constraint(expr=   m.x94 - m.x95 + 1.87188551370734*m.b274 <= 2.97049780237545)

m.c718 = Constraint(expr=   m.x95 - m.x96 + 1.87188551370734*m.b275 <= 2.97049780237545)

m.c719 = Constraint(expr=   m.x96 - m.x97 + 1.87188551370734*m.b276 <= 2.97049780237545)

m.c720 = Constraint(expr=   m.x97 - m.x98 + 1.87188551370734*m.b277 <= 2.97049780237545)

m.c721 = Constraint(expr=   m.x98 - m.x99 + 1.87188551370734*m.b278 <= 2.97049780237545)

m.c722 = Constraint(expr=   m.x99 - m.x100 + 1.87188551370734*m.b279 <= 2.97049780237545)

m.c723 = Constraint(expr=   m.x101 - m.x102 + 1.88842771364195*m.b271 <= 2.98704000231006)

m.c724 = Constraint(expr=   m.x102 - m.x103 + 1.88842771364195*m.b272 <= 2.98704000231006)

m.c725 = Constraint(expr=   m.x103 - m.x104 + 1.88842771364195*m.b273 <= 2.98704000231006)

m.c726 = Constraint(expr=   m.x104 - m.x105 + 1.88842771364195*m.b274 <= 2.98704000231006)

m.c727 = Constraint(expr=   m.x105 - m.x106 + 1.88842771364195*m.b275 <= 2.98704000231006)

m.c728 = Constraint(expr=   m.x106 - m.x107 + 1.88842771364195*m.b276 <= 2.98704000231006)

m.c729 = Constraint(expr=   m.x107 - m.x108 + 1.88842771364195*m.b277 <= 2.98704000231006)

m.c730 = Constraint(expr=   m.x108 - m.x109 + 1.88842771364195*m.b278 <= 2.98704000231006)

m.c731 = Constraint(expr=   m.x109 - m.x110 + 1.88842771364195*m.b279 <= 2.98704000231006)

m.c732 = Constraint(expr=   m.x11 - m.x12 - 1.45937721785837*m.b271 >= -2.55798950652648)

m.c733 = Constraint(expr=   m.x12 - m.x13 - 1.45937721785837*m.b272 >= -2.55798950652648)

m.c734 = Constraint(expr=   m.x13 - m.x14 - 1.45937721785837*m.b273 >= -2.55798950652648)

m.c735 = Constraint(expr=   m.x14 - m.x15 - 1.45937721785837*m.b274 >= -2.55798950652648)

m.c736 = Constraint(expr=   m.x15 - m.x16 - 1.45937721785837*m.b275 >= -2.55798950652648)

m.c737 = Constraint(expr=   m.x16 - m.x17 - 1.45937721785837*m.b276 >= -2.55798950652648)

m.c738 = Constraint(expr=   m.x17 - m.x18 - 1.45937721785837*m.b277 >= -2.55798950652648)

m.c739 = Constraint(expr=   m.x18 - m.x19 - 1.45937721785837*m.b278 >= -2.55798950652648)

m.c740 = Constraint(expr=   m.x19 - m.x20 - 1.45937721785837*m.b279 >= -2.55798950652648)

m.c741 = Constraint(expr=   m.x21 - m.x22 - 2.53921199464554*m.b271 >= -3.63782428331365)

m.c742 = Constraint(expr=   m.x22 - m.x23 - 2.53921199464554*m.b272 >= -3.63782428331365)

m.c743 = Constraint(expr=   m.x23 - m.x24 - 2.53921199464554*m.b273 >= -3.63782428331365)

m.c744 = Constraint(expr=   m.x24 - m.x25 - 2.53921199464554*m.b274 >= -3.63782428331365)

m.c745 = Constraint(expr=   m.x25 - m.x26 - 2.53921199464554*m.b275 >= -3.63782428331365)

m.c746 = Constraint(expr=   m.x26 - m.x27 - 2.53921199464554*m.b276 >= -3.63782428331365)

m.c747 = Constraint(expr=   m.x27 - m.x28 - 2.53921199464554*m.b277 >= -3.63782428331365)

m.c748 = Constraint(expr=   m.x28 - m.x29 - 2.53921199464554*m.b278 >= -3.63782428331365)

m.c749 = Constraint(expr=   m.x29 - m.x30 - 2.53921199464554*m.b279 >= -3.63782428331365)

m.c750 = Constraint(expr=   m.x31 - m.x32 - 2.15330339027829*m.b271 >= -3.2519156789464)

m.c751 = Constraint(expr=   m.x32 - m.x33 - 2.15330339027829*m.b272 >= -3.2519156789464)

m.c752 = Constraint(expr=   m.x33 - m.x34 - 2.15330339027829*m.b273 >= -3.2519156789464)

m.c753 = Constraint(expr=   m.x34 - m.x35 - 2.15330339027829*m.b274 >= -3.2519156789464)

m.c754 = Constraint(expr=   m.x35 - m.x36 - 2.15330339027829*m.b275 >= -3.2519156789464)

m.c755 = Constraint(expr=   m.x36 - m.x37 - 2.15330339027829*m.b276 >= -3.2519156789464)

m.c756 = Constraint(expr=   m.x37 - m.x38 - 2.15330339027829*m.b277 >= -3.2519156789464)

m.c757 = Constraint(expr=   m.x38 - m.x39 - 2.15330339027829*m.b278 >= -3.2519156789464)

m.c758 = Constraint(expr=   m.x39 - m.x40 - 2.15330339027829*m.b279 >= -3.2519156789464)

m.c759 = Constraint(expr=   m.x41 - m.x42 - 1.98784387242826*m.b271 >= -3.08645616109637)

m.c760 = Constraint(expr=   m.x42 - m.x43 - 1.98784387242826*m.b272 >= -3.08645616109637)

m.c761 = Constraint(expr=   m.x43 - m.x44 - 1.98784387242826*m.b273 >= -3.08645616109637)

m.c762 = Constraint(expr=   m.x44 - m.x45 - 1.98784387242826*m.b274 >= -3.08645616109637)

m.c763 = Constraint(expr=   m.x45 - m.x46 - 1.98784387242826*m.b275 >= -3.08645616109637)

m.c764 = Constraint(expr=   m.x46 - m.x47 - 1.98784387242826*m.b276 >= -3.08645616109637)

m.c765 = Constraint(expr=   m.x47 - m.x48 - 1.98784387242826*m.b277 >= -3.08645616109637)

m.c766 = Constraint(expr=   m.x48 - m.x49 - 1.98784387242826*m.b278 >= -3.08645616109637)

m.c767 = Constraint(expr=   m.x49 - m.x50 - 1.98784387242826*m.b279 >= -3.08645616109637)

m.c768 = Constraint(expr=   m.x51 - m.x52 - 2.7246152179769*m.b271 >= -3.82322750664501)

m.c769 = Constraint(expr=   m.x52 - m.x53 - 2.7246152179769*m.b272 >= -3.82322750664501)

m.c770 = Constraint(expr=   m.x53 - m.x54 - 2.7246152179769*m.b273 >= -3.82322750664501)

m.c771 = Constraint(expr=   m.x54 - m.x55 - 2.7246152179769*m.b274 >= -3.82322750664501)

m.c772 = Constraint(expr=   m.x55 - m.x56 - 2.7246152179769*m.b275 >= -3.82322750664501)

m.c773 = Constraint(expr=   m.x56 - m.x57 - 2.7246152179769*m.b276 >= -3.82322750664501)

m.c774 = Constraint(expr=   m.x57 - m.x58 - 2.7246152179769*m.b277 >= -3.82322750664501)

m.c775 = Constraint(expr=   m.x58 - m.x59 - 2.7246152179769*m.b278 >= -3.82322750664501)

m.c776 = Constraint(expr=   m.x59 - m.x60 - 2.7246152179769*m.b279 >= -3.82322750664501)

m.c777 = Constraint(expr=   m.x61 - m.x62 - 2.86282607632339*m.b271 >= -3.9614383649915)

m.c778 = Constraint(expr=   m.x62 - m.x63 - 2.86282607632339*m.b272 >= -3.9614383649915)

m.c779 = Constraint(expr=   m.x63 - m.x64 - 2.86282607632339*m.b273 >= -3.9614383649915)

m.c780 = Constraint(expr=   m.x64 - m.x65 - 2.86282607632339*m.b274 >= -3.9614383649915)

m.c781 = Constraint(expr=   m.x65 - m.x66 - 2.86282607632339*m.b275 >= -3.9614383649915)

m.c782 = Constraint(expr=   m.x66 - m.x67 - 2.86282607632339*m.b276 >= -3.9614383649915)

m.c783 = Constraint(expr=   m.x67 - m.x68 - 2.86282607632339*m.b277 >= -3.9614383649915)

m.c784 = Constraint(expr=   m.x68 - m.x69 - 2.86282607632339*m.b278 >= -3.9614383649915)

m.c785 = Constraint(expr=   m.x69 - m.x70 - 2.86282607632339*m.b279 >= -3.9614383649915)

m.c786 = Constraint(expr=   m.x71 - m.x72 - 1.84763467312072*m.b271 >= -2.94624696178883)

m.c787 = Constraint(expr=   m.x72 - m.x73 - 1.84763467312072*m.b272 >= -2.94624696178883)

m.c788 = Constraint(expr=   m.x73 - m.x74 - 1.84763467312072*m.b273 >= -2.94624696178883)

m.c789 = Constraint(expr=   m.x74 - m.x75 - 1.84763467312072*m.b274 >= -2.94624696178883)

m.c790 = Constraint(expr=   m.x75 - m.x76 - 1.84763467312072*m.b275 >= -2.94624696178883)

m.c791 = Constraint(expr=   m.x76 - m.x77 - 1.84763467312072*m.b276 >= -2.94624696178883)

m.c792 = Constraint(expr=   m.x77 - m.x78 - 1.84763467312072*m.b277 >= -2.94624696178883)

m.c793 = Constraint(expr=   m.x78 - m.x79 - 1.84763467312072*m.b278 >= -2.94624696178883)

m.c794 = Constraint(expr=   m.x79 - m.x80 - 1.84763467312072*m.b279 >= -2.94624696178883)

m.c795 = Constraint(expr=   m.x81 - m.x82 - 2.22778688291886*m.b271 >= -3.32639917158697)

m.c796 = Constraint(expr=   m.x82 - m.x83 - 2.22778688291886*m.b272 >= -3.32639917158697)

m.c797 = Constraint(expr=   m.x83 - m.x84 - 2.22778688291886*m.b273 >= -3.32639917158697)

m.c798 = Constraint(expr=   m.x84 - m.x85 - 2.22778688291886*m.b274 >= -3.32639917158697)

m.c799 = Constraint(expr=   m.x85 - m.x86 - 2.22778688291886*m.b275 >= -3.32639917158697)

m.c800 = Constraint(expr=   m.x86 - m.x87 - 2.22778688291886*m.b276 >= -3.32639917158697)

m.c801 = Constraint(expr=   m.x87 - m.x88 - 2.22778688291886*m.b277 >= -3.32639917158697)

m.c802 = Constraint(expr=   m.x88 - m.x89 - 2.22778688291886*m.b278 >= -3.32639917158697)

m.c803 = Constraint(expr=   m.x89 - m.x90 - 2.22778688291886*m.b279 >= -3.32639917158697)

m.c804 = Constraint(expr=   m.x91 - m.x92 - 1.87188551370734*m.b271 >= -2.97049780237545)

m.c805 = Constraint(expr=   m.x92 - m.x93 - 1.87188551370734*m.b272 >= -2.97049780237545)

m.c806 = Constraint(expr=   m.x93 - m.x94 - 1.87188551370734*m.b273 >= -2.97049780237545)

m.c807 = Constraint(expr=   m.x94 - m.x95 - 1.87188551370734*m.b274 >= -2.97049780237545)

m.c808 = Constraint(expr=   m.x95 - m.x96 - 1.87188551370734*m.b275 >= -2.97049780237545)

m.c809 = Constraint(expr=   m.x96 - m.x97 - 1.87188551370734*m.b276 >= -2.97049780237545)

m.c810 = Constraint(expr=   m.x97 - m.x98 - 1.87188551370734*m.b277 >= -2.97049780237545)

m.c811 = Constraint(expr=   m.x98 - m.x99 - 1.87188551370734*m.b278 >= -2.97049780237545)

m.c812 = Constraint(expr=   m.x99 - m.x100 - 1.87188551370734*m.b279 >= -2.97049780237545)

m.c813 = Constraint(expr=   m.x101 - m.x102 - 1.88842771364195*m.b271 >= -2.98704000231006)

m.c814 = Constraint(expr=   m.x102 - m.x103 - 1.88842771364195*m.b272 >= -2.98704000231006)

m.c815 = Constraint(expr=   m.x103 - m.x104 - 1.88842771364195*m.b273 >= -2.98704000231006)

m.c816 = Constraint(expr=   m.x104 - m.x105 - 1.88842771364195*m.b274 >= -2.98704000231006)

m.c817 = Constraint(expr=   m.x105 - m.x106 - 1.88842771364195*m.b275 >= -2.98704000231006)

m.c818 = Constraint(expr=   m.x106 - m.x107 - 1.88842771364195*m.b276 >= -2.98704000231006)

m.c819 = Constraint(expr=   m.x107 - m.x108 - 1.88842771364195*m.b277 >= -2.98704000231006)

m.c820 = Constraint(expr=   m.x108 - m.x109 - 1.88842771364195*m.b278 >= -2.98704000231006)

m.c821 = Constraint(expr=   m.x109 - m.x110 - 1.88842771364195*m.b279 >= -2.98704000231006)

m.c823 = Constraint(expr=   m.x132 - 18.8261458520605*m.b271 <= -9.21034037197618)

m.c824 = Constraint(expr=   m.x133 - 18.8261458520605*m.b272 <= -9.21034037197618)

m.c825 = Constraint(expr=   m.x134 - 18.8261458520605*m.b273 <= -9.21034037197618)

m.c826 = Constraint(expr=   m.x135 - 18.8261458520605*m.b274 <= -9.21034037197618)

m.c827 = Constraint(expr=   m.x136 - 18.8261458520605*m.b275 <= -9.21034037197618)

m.c828 = Constraint(expr=   m.x137 - 18.8261458520605*m.b276 <= -9.21034037197618)

m.c829 = Constraint(expr=   m.x138 - 18.8261458520605*m.b277 <= -9.21034037197618)

m.c830 = Constraint(expr=   m.x139 - 18.8261458520605*m.b278 <= -9.21034037197618)

m.c831 = Constraint(expr=   m.x140 - 18.8261458520605*m.b279 <= -9.21034037197618)

m.c832 = Constraint(expr=   m.x132 + 13.8155105579643*m.b271 >= -9.21034037197618)

m.c833 = Constraint(expr=   m.x133 + 13.8155105579643*m.b272 >= -9.21034037197618)

m.c834 = Constraint(expr=   m.x134 + 13.8155105579643*m.b273 >= -9.21034037197618)

m.c835 = Constraint(expr=   m.x135 + 13.8155105579643*m.b274 >= -9.21034037197618)

m.c836 = Constraint(expr=   m.x136 + 13.8155105579643*m.b275 >= -9.21034037197618)

m.c837 = Constraint(expr=   m.x137 + 13.8155105579643*m.b276 >= -9.21034037197618)

m.c838 = Constraint(expr=   m.x138 + 13.8155105579643*m.b277 >= -9.21034037197618)

m.c839 = Constraint(expr=   m.x139 + 13.8155105579643*m.b278 >= -9.21034037197618)

m.c840 = Constraint(expr=   m.x140 + 13.8155105579643*m.b279 >= -9.21034037197618)

m.c841 = Constraint(expr=   m.x11 - m.x12 - 2.55798950652648*m.b271 <= 0)

m.c842 = Constraint(expr=   m.x12 - m.x13 - 2.55798950652648*m.b272 <= 0)

m.c843 = Constraint(expr=   m.x13 - m.x14 - 2.55798950652648*m.b273 <= 0)

m.c844 = Constraint(expr=   m.x14 - m.x15 - 2.55798950652648*m.b274 <= 0)

m.c845 = Constraint(expr=   m.x15 - m.x16 - 2.55798950652648*m.b275 <= 0)

m.c846 = Constraint(expr=   m.x16 - m.x17 - 2.55798950652648*m.b276 <= 0)

m.c847 = Constraint(expr=   m.x17 - m.x18 - 2.55798950652648*m.b277 <= 0)

m.c848 = Constraint(expr=   m.x18 - m.x19 - 2.55798950652648*m.b278 <= 0)

m.c849 = Constraint(expr=   m.x19 - m.x20 - 2.55798950652648*m.b279 <= 0)

m.c850 = Constraint(expr=   m.x21 - m.x22 - 3.63782428331365*m.b271 <= 0)

m.c851 = Constraint(expr=   m.x22 - m.x23 - 3.63782428331365*m.b272 <= 0)

m.c852 = Constraint(expr=   m.x23 - m.x24 - 3.63782428331365*m.b273 <= 0)

m.c853 = Constraint(expr=   m.x24 - m.x25 - 3.63782428331365*m.b274 <= 0)

m.c854 = Constraint(expr=   m.x25 - m.x26 - 3.63782428331365*m.b275 <= 0)

m.c855 = Constraint(expr=   m.x26 - m.x27 - 3.63782428331365*m.b276 <= 0)

m.c856 = Constraint(expr=   m.x27 - m.x28 - 3.63782428331365*m.b277 <= 0)

m.c857 = Constraint(expr=   m.x28 - m.x29 - 3.63782428331365*m.b278 <= 0)

m.c858 = Constraint(expr=   m.x29 - m.x30 - 3.63782428331365*m.b279 <= 0)

m.c859 = Constraint(expr=   m.x31 - m.x32 - 3.2519156789464*m.b271 <= 0)

m.c860 = Constraint(expr=   m.x32 - m.x33 - 3.2519156789464*m.b272 <= 0)

m.c861 = Constraint(expr=   m.x33 - m.x34 - 3.2519156789464*m.b273 <= 0)

m.c862 = Constraint(expr=   m.x34 - m.x35 - 3.2519156789464*m.b274 <= 0)

m.c863 = Constraint(expr=   m.x35 - m.x36 - 3.2519156789464*m.b275 <= 0)

m.c864 = Constraint(expr=   m.x36 - m.x37 - 3.2519156789464*m.b276 <= 0)

m.c865 = Constraint(expr=   m.x37 - m.x38 - 3.2519156789464*m.b277 <= 0)

m.c866 = Constraint(expr=   m.x38 - m.x39 - 3.2519156789464*m.b278 <= 0)

m.c867 = Constraint(expr=   m.x39 - m.x40 - 3.2519156789464*m.b279 <= 0)

m.c868 = Constraint(expr=   m.x41 - m.x42 - 3.08645616109637*m.b271 <= 0)

m.c869 = Constraint(expr=   m.x42 - m.x43 - 3.08645616109637*m.b272 <= 0)

m.c870 = Constraint(expr=   m.x43 - m.x44 - 3.08645616109637*m.b273 <= 0)

m.c871 = Constraint(expr=   m.x44 - m.x45 - 3.08645616109637*m.b274 <= 0)

m.c872 = Constraint(expr=   m.x45 - m.x46 - 3.08645616109637*m.b275 <= 0)

m.c873 = Constraint(expr=   m.x46 - m.x47 - 3.08645616109637*m.b276 <= 0)

m.c874 = Constraint(expr=   m.x47 - m.x48 - 3.08645616109637*m.b277 <= 0)

m.c875 = Constraint(expr=   m.x48 - m.x49 - 3.08645616109637*m.b278 <= 0)

m.c876 = Constraint(expr=   m.x49 - m.x50 - 3.08645616109637*m.b279 <= 0)

m.c877 = Constraint(expr=   m.x51 - m.x52 - 3.82322750664501*m.b271 <= 0)

m.c878 = Constraint(expr=   m.x52 - m.x53 - 3.82322750664501*m.b272 <= 0)

m.c879 = Constraint(expr=   m.x53 - m.x54 - 3.82322750664501*m.b273 <= 0)

m.c880 = Constraint(expr=   m.x54 - m.x55 - 3.82322750664501*m.b274 <= 0)

m.c881 = Constraint(expr=   m.x55 - m.x56 - 3.82322750664501*m.b275 <= 0)

m.c882 = Constraint(expr=   m.x56 - m.x57 - 3.82322750664501*m.b276 <= 0)

m.c883 = Constraint(expr=   m.x57 - m.x58 - 3.82322750664501*m.b277 <= 0)

m.c884 = Constraint(expr=   m.x58 - m.x59 - 3.82322750664501*m.b278 <= 0)

m.c885 = Constraint(expr=   m.x59 - m.x60 - 3.82322750664501*m.b279 <= 0)

m.c886 = Constraint(expr=   m.x61 - m.x62 - 3.9614383649915*m.b271 <= 0)

m.c887 = Constraint(expr=   m.x62 - m.x63 - 3.9614383649915*m.b272 <= 0)

m.c888 = Constraint(expr=   m.x63 - m.x64 - 3.9614383649915*m.b273 <= 0)

m.c889 = Constraint(expr=   m.x64 - m.x65 - 3.9614383649915*m.b274 <= 0)

m.c890 = Constraint(expr=   m.x65 - m.x66 - 3.9614383649915*m.b275 <= 0)

m.c891 = Constraint(expr=   m.x66 - m.x67 - 3.9614383649915*m.b276 <= 0)

m.c892 = Constraint(expr=   m.x67 - m.x68 - 3.9614383649915*m.b277 <= 0)

m.c893 = Constraint(expr=   m.x68 - m.x69 - 3.9614383649915*m.b278 <= 0)

m.c894 = Constraint(expr=   m.x69 - m.x70 - 3.9614383649915*m.b279 <= 0)

m.c895 = Constraint(expr=   m.x71 - m.x72 - 2.94624696178883*m.b271 <= 0)

m.c896 = Constraint(expr=   m.x72 - m.x73 - 2.94624696178883*m.b272 <= 0)

m.c897 = Constraint(expr=   m.x73 - m.x74 - 2.94624696178883*m.b273 <= 0)

m.c898 = Constraint(expr=   m.x74 - m.x75 - 2.94624696178883*m.b274 <= 0)

m.c899 = Constraint(expr=   m.x75 - m.x76 - 2.94624696178883*m.b275 <= 0)

m.c900 = Constraint(expr=   m.x76 - m.x77 - 2.94624696178883*m.b276 <= 0)

m.c901 = Constraint(expr=   m.x77 - m.x78 - 2.94624696178883*m.b277 <= 0)

m.c902 = Constraint(expr=   m.x78 - m.x79 - 2.94624696178883*m.b278 <= 0)

m.c903 = Constraint(expr=   m.x79 - m.x80 - 2.94624696178883*m.b279 <= 0)

m.c904 = Constraint(expr=   m.x81 - m.x82 - 3.32639917158697*m.b271 <= 0)

m.c905 = Constraint(expr=   m.x82 - m.x83 - 3.32639917158697*m.b272 <= 0)

m.c906 = Constraint(expr=   m.x83 - m.x84 - 3.32639917158697*m.b273 <= 0)

m.c907 = Constraint(expr=   m.x84 - m.x85 - 3.32639917158697*m.b274 <= 0)

m.c908 = Constraint(expr=   m.x85 - m.x86 - 3.32639917158697*m.b275 <= 0)

m.c909 = Constraint(expr=   m.x86 - m.x87 - 3.32639917158697*m.b276 <= 0)

m.c910 = Constraint(expr=   m.x87 - m.x88 - 3.32639917158697*m.b277 <= 0)

m.c911 = Constraint(expr=   m.x88 - m.x89 - 3.32639917158697*m.b278 <= 0)

m.c912 = Constraint(expr=   m.x89 - m.x90 - 3.32639917158697*m.b279 <= 0)

m.c913 = Constraint(expr=   m.x91 - m.x92 - 2.97049780237545*m.b271 <= 0)

m.c914 = Constraint(expr=   m.x92 - m.x93 - 2.97049780237545*m.b272 <= 0)

m.c915 = Constraint(expr=   m.x93 - m.x94 - 2.97049780237545*m.b273 <= 0)

m.c916 = Constraint(expr=   m.x94 - m.x95 - 2.97049780237545*m.b274 <= 0)

m.c917 = Constraint(expr=   m.x95 - m.x96 - 2.97049780237545*m.b275 <= 0)

m.c918 = Constraint(expr=   m.x96 - m.x97 - 2.97049780237545*m.b276 <= 0)

m.c919 = Constraint(expr=   m.x97 - m.x98 - 2.97049780237545*m.b277 <= 0)

m.c920 = Constraint(expr=   m.x98 - m.x99 - 2.97049780237545*m.b278 <= 0)

m.c921 = Constraint(expr=   m.x99 - m.x100 - 2.97049780237545*m.b279 <= 0)

m.c922 = Constraint(expr=   m.x101 - m.x102 - 2.98704000231006*m.b271 <= 0)

m.c923 = Constraint(expr=   m.x102 - m.x103 - 2.98704000231006*m.b272 <= 0)

m.c924 = Constraint(expr=   m.x103 - m.x104 - 2.98704000231006*m.b273 <= 0)

m.c925 = Constraint(expr=   m.x104 - m.x105 - 2.98704000231006*m.b274 <= 0)

m.c926 = Constraint(expr=   m.x105 - m.x106 - 2.98704000231006*m.b275 <= 0)

m.c927 = Constraint(expr=   m.x106 - m.x107 - 2.98704000231006*m.b276 <= 0)

m.c928 = Constraint(expr=   m.x107 - m.x108 - 2.98704000231006*m.b277 <= 0)

m.c929 = Constraint(expr=   m.x108 - m.x109 - 2.98704000231006*m.b278 <= 0)

m.c930 = Constraint(expr=   m.x109 - m.x110 - 2.98704000231006*m.b279 <= 0)

m.c931 = Constraint(expr=   m.x11 - m.x12 + 2.55798950652648*m.b271 >= 0)

m.c932 = Constraint(expr=   m.x12 - m.x13 + 2.55798950652648*m.b272 >= 0)

m.c933 = Constraint(expr=   m.x13 - m.x14 + 2.55798950652648*m.b273 >= 0)

m.c934 = Constraint(expr=   m.x14 - m.x15 + 2.55798950652648*m.b274 >= 0)

m.c935 = Constraint(expr=   m.x15 - m.x16 + 2.55798950652648*m.b275 >= 0)

m.c936 = Constraint(expr=   m.x16 - m.x17 + 2.55798950652648*m.b276 >= 0)

m.c937 = Constraint(expr=   m.x17 - m.x18 + 2.55798950652648*m.b277 >= 0)

m.c938 = Constraint(expr=   m.x18 - m.x19 + 2.55798950652648*m.b278 >= 0)

m.c939 = Constraint(expr=   m.x19 - m.x20 + 2.55798950652648*m.b279 >= 0)

m.c940 = Constraint(expr=   m.x21 - m.x22 + 3.63782428331365*m.b271 >= 0)

m.c941 = Constraint(expr=   m.x22 - m.x23 + 3.63782428331365*m.b272 >= 0)

m.c942 = Constraint(expr=   m.x23 - m.x24 + 3.63782428331365*m.b273 >= 0)

m.c943 = Constraint(expr=   m.x24 - m.x25 + 3.63782428331365*m.b274 >= 0)

m.c944 = Constraint(expr=   m.x25 - m.x26 + 3.63782428331365*m.b275 >= 0)

m.c945 = Constraint(expr=   m.x26 - m.x27 + 3.63782428331365*m.b276 >= 0)

m.c946 = Constraint(expr=   m.x27 - m.x28 + 3.63782428331365*m.b277 >= 0)

m.c947 = Constraint(expr=   m.x28 - m.x29 + 3.63782428331365*m.b278 >= 0)

m.c948 = Constraint(expr=   m.x29 - m.x30 + 3.63782428331365*m.b279 >= 0)

m.c949 = Constraint(expr=   m.x31 - m.x32 + 3.2519156789464*m.b271 >= 0)

m.c950 = Constraint(expr=   m.x32 - m.x33 + 3.2519156789464*m.b272 >= 0)

m.c951 = Constraint(expr=   m.x33 - m.x34 + 3.2519156789464*m.b273 >= 0)

m.c952 = Constraint(expr=   m.x34 - m.x35 + 3.2519156789464*m.b274 >= 0)

m.c953 = Constraint(expr=   m.x35 - m.x36 + 3.2519156789464*m.b275 >= 0)

m.c954 = Constraint(expr=   m.x36 - m.x37 + 3.2519156789464*m.b276 >= 0)

m.c955 = Constraint(expr=   m.x37 - m.x38 + 3.2519156789464*m.b277 >= 0)

m.c956 = Constraint(expr=   m.x38 - m.x39 + 3.2519156789464*m.b278 >= 0)

m.c957 = Constraint(expr=   m.x39 - m.x40 + 3.2519156789464*m.b279 >= 0)

m.c958 = Constraint(expr=   m.x41 - m.x42 + 3.08645616109637*m.b271 >= 0)

m.c959 = Constraint(expr=   m.x42 - m.x43 + 3.08645616109637*m.b272 >= 0)

m.c960 = Constraint(expr=   m.x43 - m.x44 + 3.08645616109637*m.b273 >= 0)

m.c961 = Constraint(expr=   m.x44 - m.x45 + 3.08645616109637*m.b274 >= 0)

m.c962 = Constraint(expr=   m.x45 - m.x46 + 3.08645616109637*m.b275 >= 0)

m.c963 = Constraint(expr=   m.x46 - m.x47 + 3.08645616109637*m.b276 >= 0)

m.c964 = Constraint(expr=   m.x47 - m.x48 + 3.08645616109637*m.b277 >= 0)

m.c965 = Constraint(expr=   m.x48 - m.x49 + 3.08645616109637*m.b278 >= 0)

m.c966 = Constraint(expr=   m.x49 - m.x50 + 3.08645616109637*m.b279 >= 0)

m.c967 = Constraint(expr=   m.x51 - m.x52 + 3.82322750664501*m.b271 >= 0)

m.c968 = Constraint(expr=   m.x52 - m.x53 + 3.82322750664501*m.b272 >= 0)

m.c969 = Constraint(expr=   m.x53 - m.x54 + 3.82322750664501*m.b273 >= 0)

m.c970 = Constraint(expr=   m.x54 - m.x55 + 3.82322750664501*m.b274 >= 0)

m.c971 = Constraint(expr=   m.x55 - m.x56 + 3.82322750664501*m.b275 >= 0)

m.c972 = Constraint(expr=   m.x56 - m.x57 + 3.82322750664501*m.b276 >= 0)

m.c973 = Constraint(expr=   m.x57 - m.x58 + 3.82322750664501*m.b277 >= 0)

m.c974 = Constraint(expr=   m.x58 - m.x59 + 3.82322750664501*m.b278 >= 0)

m.c975 = Constraint(expr=   m.x59 - m.x60 + 3.82322750664501*m.b279 >= 0)

m.c976 = Constraint(expr=   m.x61 - m.x62 + 3.9614383649915*m.b271 >= 0)

m.c977 = Constraint(expr=   m.x62 - m.x63 + 3.9614383649915*m.b272 >= 0)

m.c978 = Constraint(expr=   m.x63 - m.x64 + 3.9614383649915*m.b273 >= 0)

m.c979 = Constraint(expr=   m.x64 - m.x65 + 3.9614383649915*m.b274 >= 0)

m.c980 = Constraint(expr=   m.x65 - m.x66 + 3.9614383649915*m.b275 >= 0)

m.c981 = Constraint(expr=   m.x66 - m.x67 + 3.9614383649915*m.b276 >= 0)

m.c982 = Constraint(expr=   m.x67 - m.x68 + 3.9614383649915*m.b277 >= 0)

m.c983 = Constraint(expr=   m.x68 - m.x69 + 3.9614383649915*m.b278 >= 0)

m.c984 = Constraint(expr=   m.x69 - m.x70 + 3.9614383649915*m.b279 >= 0)

m.c985 = Constraint(expr=   m.x71 - m.x72 + 2.94624696178883*m.b271 >= 0)

m.c986 = Constraint(expr=   m.x72 - m.x73 + 2.94624696178883*m.b272 >= 0)

m.c987 = Constraint(expr=   m.x73 - m.x74 + 2.94624696178883*m.b273 >= 0)

m.c988 = Constraint(expr=   m.x74 - m.x75 + 2.94624696178883*m.b274 >= 0)

m.c989 = Constraint(expr=   m.x75 - m.x76 + 2.94624696178883*m.b275 >= 0)

m.c990 = Constraint(expr=   m.x76 - m.x77 + 2.94624696178883*m.b276 >= 0)

m.c991 = Constraint(expr=   m.x77 - m.x78 + 2.94624696178883*m.b277 >= 0)

m.c992 = Constraint(expr=   m.x78 - m.x79 + 2.94624696178883*m.b278 >= 0)

m.c993 = Constraint(expr=   m.x79 - m.x80 + 2.94624696178883*m.b279 >= 0)

m.c994 = Constraint(expr=   m.x81 - m.x82 + 3.32639917158697*m.b271 >= 0)

m.c995 = Constraint(expr=   m.x82 - m.x83 + 3.32639917158697*m.b272 >= 0)

m.c996 = Constraint(expr=   m.x83 - m.x84 + 3.32639917158697*m.b273 >= 0)

m.c997 = Constraint(expr=   m.x84 - m.x85 + 3.32639917158697*m.b274 >= 0)

m.c998 = Constraint(expr=   m.x85 - m.x86 + 3.32639917158697*m.b275 >= 0)

m.c999 = Constraint(expr=   m.x86 - m.x87 + 3.32639917158697*m.b276 >= 0)

m.c1000 = Constraint(expr=   m.x87 - m.x88 + 3.32639917158697*m.b277 >= 0)

m.c1001 = Constraint(expr=   m.x88 - m.x89 + 3.32639917158697*m.b278 >= 0)

m.c1002 = Constraint(expr=   m.x89 - m.x90 + 3.32639917158697*m.b279 >= 0)

m.c1003 = Constraint(expr=   m.x91 - m.x92 + 2.97049780237545*m.b271 >= 0)

m.c1004 = Constraint(expr=   m.x92 - m.x93 + 2.97049780237545*m.b272 >= 0)

m.c1005 = Constraint(expr=   m.x93 - m.x94 + 2.97049780237545*m.b273 >= 0)

m.c1006 = Constraint(expr=   m.x94 - m.x95 + 2.97049780237545*m.b274 >= 0)

m.c1007 = Constraint(expr=   m.x95 - m.x96 + 2.97049780237545*m.b275 >= 0)

m.c1008 = Constraint(expr=   m.x96 - m.x97 + 2.97049780237545*m.b276 >= 0)

m.c1009 = Constraint(expr=   m.x97 - m.x98 + 2.97049780237545*m.b277 >= 0)

m.c1010 = Constraint(expr=   m.x98 - m.x99 + 2.97049780237545*m.b278 >= 0)

m.c1011 = Constraint(expr=   m.x99 - m.x100 + 2.97049780237545*m.b279 >= 0)

m.c1012 = Constraint(expr=   m.x101 - m.x102 + 2.98704000231006*m.b271 >= 0)

m.c1013 = Constraint(expr=   m.x102 - m.x103 + 2.98704000231006*m.b272 >= 0)

m.c1014 = Constraint(expr=   m.x103 - m.x104 + 2.98704000231006*m.b273 >= 0)

m.c1015 = Constraint(expr=   m.x104 - m.x105 + 2.98704000231006*m.b274 >= 0)

m.c1016 = Constraint(expr=   m.x105 - m.x106 + 2.98704000231006*m.b275 >= 0)

m.c1017 = Constraint(expr=   m.x106 - m.x107 + 2.98704000231006*m.b276 >= 0)

m.c1018 = Constraint(expr=   m.x107 - m.x108 + 2.98704000231006*m.b277 >= 0)

m.c1019 = Constraint(expr=   m.x108 - m.x109 + 2.98704000231006*m.b278 >= 0)

m.c1020 = Constraint(expr=   m.x109 - m.x110 + 2.98704000231006*m.b279 >= 0)

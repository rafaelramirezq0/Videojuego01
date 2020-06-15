import pygame
from pygame import *
from pygame.locals import *
from pygame_functions import *
import sys
import time
from random import randint


'''     TODAS LAS ANIMACIONES       '''
# Animación intro - parte1
freim1 = pygame.image.load("Animación1/intro00001.png")
freim2 = pygame.image.load("Animación1/intro00002.png")  
freim3 = pygame.image.load("Animación1/intro00003.png")  
freim4 = pygame.image.load("Animación1/intro00004.png")  
freim5 = pygame.image.load("Animación1/intro00005.png")  
freim6 = pygame.image.load("Animación1/intro00006.png")  
freim7 = pygame.image.load("Animación1/intro00007.png")  
freim8 = pygame.image.load("Animación1/intro00008.png")  
freim9 = pygame.image.load("Animación1/intro00009.png")  
freim10 = pygame.image.load("Animación1/intro00010.png")
freim11 = pygame.image.load("Animación1/intro00011.png") 
freim12 = pygame.image.load("Animación1/intro00012.png") 
freim13 = pygame.image.load("Animación1/intro00013.png") 
freim14 = pygame.image.load("Animación1/intro00014.png")
freim15 = pygame.image.load("Animación1/intro00015.png")
freim16 = pygame.image.load("Animación1/intro00016.png")
freim17 = pygame.image.load("Animación1/intro00017.png")
freim18 = pygame.image.load("Animación1/intro00018.png")
freim19 = pygame.image.load("Animación1/intro00019.png")
freim20 = pygame.image.load("Animación1/intro00020.png")
freim21 = pygame.image.load("Animación1/intro00021.png")
freim22 = pygame.image.load("Animación1/intro00022.png")
freim23 = pygame.image.load("Animación1/intro00023.png")
freim24 = pygame.image.load("Animación1/intro00024.png")
freim25 = pygame.image.load("Animación1/intro00025.png")
freim26 = pygame.image.load("Animación1/intro00026.png")
freim27 = pygame.image.load("Animación1/intro00027.png")
freim28 = pygame.image.load("Animación1/intro00028.png")
freim29 = pygame.image.load("Animación1/intro00029.png")
freim30 = pygame.image.load("Animación1/intro00030.png")
freim31 = pygame.image.load("Animación1/intro00031.png")
freim32 = pygame.image.load("Animación1/intro00032.png")
freim33 = pygame.image.load("Animación1/intro00033.png")
freim34 = pygame.image.load("Animación1/intro00034.png")
freim35 = pygame.image.load("Animación1/intro00035.png")
freim36 = pygame.image.load("Animación1/intro00036.png")
freim37 = pygame.image.load("Animación1/intro00037.png")
freim38 = pygame.image.load("Animación1/intro00038.png")
freim39 = pygame.image.load("Animación1/intro00039.png")
freim40 = pygame.image.load("Animación1/intro00040.png")
freim41 = pygame.image.load("Animación1/intro00041.png")
freim42 = pygame.image.load("Animación1/intro00042.png")
freim43 = pygame.image.load("Animación1/intro00043.png")
freim44 = pygame.image.load("Animación1/intro00044.png")
freim45 = pygame.image.load("Animación1/intro00045.png")
freim46 = pygame.image.load("Animación1/intro00046.png")
freim47 = pygame.image.load("Animación1/intro00047.png")
freim48 = pygame.image.load("Animación1/intro00048.png")
freim49 = pygame.image.load("Animación1/intro00049.png")
freim50 = pygame.image.load("Animación1/intro00050.png")
freim51 = pygame.image.load("Animación1/intro00051.png")
freim52 = pygame.image.load("Animación1/intro00052.png")
freim53 = pygame.image.load("Animación1/intro00053.png")
freim54 = pygame.image.load("Animación1/intro00054.png")
freim55 = pygame.image.load("Animación1/intro00055.png")
freim56 = pygame.image.load("Animación1/intro00056.png")
freim57 = pygame.image.load("Animación1/intro00057.png")
freim58 = pygame.image.load("Animación1/intro00058.png")
freim59 = pygame.image.load("Animación1/intro00059.png")
freim60 = pygame.image.load("Animación1/intro00060.png")
freim61 = pygame.image.load("Animación1/intro00061.png")
freim62 = pygame.image.load("Animación1/intro00062.png")
freim63 = pygame.image.load("Animación1/intro00063.png")
freim64 = pygame.image.load("Animación1/intro00064.png")
freim65 = pygame.image.load("Animación1/intro00065.png")
freim66 = pygame.image.load("Animación1/intro00066.png")
freim67 = pygame.image.load("Animación1/intro00067.png")
freim68 = pygame.image.load("Animación1/intro00068.png")
freim69 = pygame.image.load("Animación1/intro00069.png")
freim70 = pygame.image.load("Animación1/intro00070.png")
freim71 = pygame.image.load("Animación1/intro00071.png")
freim72 = pygame.image.load("Animación1/intro00072.png")
freim73 = pygame.image.load("Animación1/intro00073.png")
freim74 = pygame.image.load("Animación1/intro00074.png")
freim75 = pygame.image.load("Animación1/intro00075.png")
freim76 = pygame.image.load("Animación1/intro00076.png")
freim77 = pygame.image.load("Animación1/intro00077.png")
freim78 = pygame.image.load("Animación1/intro00078.png")
freim79 = pygame.image.load("Animación1/intro00079.png")
freim80 = pygame.image.load("Animación1/intro00080.png")
freim81 = pygame.image.load("Animación1/intro00081.png")
freim82 = pygame.image.load("Animación1/intro00082.png")
freim83 = pygame.image.load("Animación1/intro00083.png")
freim84 = pygame.image.load("Animación1/intro00084.png")
freim85 = pygame.image.load("Animación1/intro00085.png")
freim86 = pygame.image.load("Animación1/intro00086.png")
freim87 = pygame.image.load("Animación1/intro00087.png")
freim88 = pygame.image.load("Animación1/intro00088.png")
freim89 = pygame.image.load("Animación1/intro00089.png")
freim90 = pygame.image.load("Animación1/intro00090.png")
freim91 = pygame.image.load("Animación1/intro00091.png")
freim92 = pygame.image.load("Animación1/intro00092.png")
freim93 = pygame.image.load("Animación1/intro00093.png")
freim94 = pygame.image.load("Animación1/intro00094.png")
freim95 = pygame.image.load("Animación1/intro00095.png")
freim96 = pygame.image.load("Animación1/intro00096.png")
freim97 = pygame.image.load("Animación1/intro00097.png")
freim98 = pygame.image.load("Animación1/intro00098.png")
freim99 = pygame.image.load("Animación1/intro00099.png")
freim100 = pygame.image.load("Animación1/intro00100.png")
freim101 = pygame.image.load("Animación1/intro00101.png")
freim102 = pygame.image.load("Animación1/intro00102.png")
freim103 = pygame.image.load("Animación1/intro00103.png")
freim104 = pygame.image.load("Animación1/intro00104.png")
freim105 = pygame.image.load("Animación1/intro00105.png")
freim106 = pygame.image.load("Animación1/intro00106.png")
freim107 = pygame.image.load("Animación1/intro00107.png")
freim108 = pygame.image.load("Animación1/intro00108.png")
freim109 = pygame.image.load("Animación1/intro00109.png")
freim110 = pygame.image.load("Animación1/intro00110.png")
freim111 = pygame.image.load("Animación1/intro00111.png")
freim112 = pygame.image.load("Animación1/intro00112.png")
freim113 = pygame.image.load("Animación1/intro00113.png")
freim114 = pygame.image.load("Animación1/intro00114.png")
freim115 = pygame.image.load("Animación1/intro00115.png")
freim116 = pygame.image.load("Animación1/intro00116.png")
freim117 = pygame.image.load("Animación1/intro00117.png")
freim118 = pygame.image.load("Animación1/intro00118.png")
freim119 = pygame.image.load("Animación1/intro00119.png")
freim120 = pygame.image.load("Animación1/intro00120.png")
freim121 = pygame.image.load("Animación1/intro00121.png")
freim122 = pygame.image.load("Animación1/intro00122.png")
freim123 = pygame.image.load("Animación1/intro00123.png")
freim124 = pygame.image.load("Animación1/intro00124.png")
freim125 = pygame.image.load("Animación1/intro00125.png")
freim126 = pygame.image.load("Animación1/intro00126.png")
freim127 = pygame.image.load("Animación1/intro00127.png")
freim128 = pygame.image.load("Animación1/intro00128.png")
freim129 = pygame.image.load("Animación1/intro00129.png")
freim130 = pygame.image.load("Animación1/intro00130.png")
freim131 = pygame.image.load("Animación1/intro00131.png")
freim132 = pygame.image.load("Animación1/intro00132.png")
freim133 = pygame.image.load("Animación1/intro00133.png")
freim134 = pygame.image.load("Animación1/intro00134.png")
freim135 = pygame.image.load("Animación1/intro00135.png")
freim136 = pygame.image.load("Animación1/intro00136.png")
freim137 = pygame.image.load("Animación1/intro00137.png")
freim138 = pygame.image.load("Animación1/intro00138.png")
freim139 = pygame.image.load("Animación1/intro00139.png")
freim140 = pygame.image.load("Animación1/intro00140.png")
freim141 = pygame.image.load("Animación1/intro00141.png")
freim142 = pygame.image.load("Animación1/intro00142.png")
freim143 = pygame.image.load("Animación1/intro00143.png")
freim144 = pygame.image.load("Animación1/intro00144.png")
freim145 = pygame.image.load("Animación1/intro00145.png")
freim146 = pygame.image.load("Animación1/intro00146.png")
freim147 = pygame.image.load("Animación1/intro00147.png")
freim148 = pygame.image.load("Animación1/intro00148.png")
freim149 = pygame.image.load("Animación1/intro00149.png")
freim150 = pygame.image.load("Animación1/intro00150.png")
freim151 = pygame.image.load("Animación1/intro00151.png")
freim152 = pygame.image.load("Animación1/intro00152.png")
freim153 = pygame.image.load("Animación1/intro00153.png")
freim154 = pygame.image.load("Animación1/intro00154.png")
freim155 = pygame.image.load("Animación1/intro00155.png")
freim156 = pygame.image.load("Animación1/intro00156.png")
freim157 = pygame.image.load("Animación1/intro00157.png")
freim158 = pygame.image.load("Animación1/intro00158.png")
freim159 = pygame.image.load("Animación1/intro00159.png")
freim160 = pygame.image.load("Animación1/intro00160.png")
freim161 = pygame.image.load("Animación1/intro00161.png")
freim162 = pygame.image.load("Animación1/intro00162.png")
freim163 = pygame.image.load("Animación1/intro00163.png")
freim164 = pygame.image.load("Animación1/intro00164.png")
freim165 = pygame.image.load("Animación1/intro00165.png")
freim166 = pygame.image.load("Animación1/intro00166.png")
freim167 = pygame.image.load("Animación1/intro00167.png")
freim168 = pygame.image.load("Animación1/intro00168.png")
freim169 = pygame.image.load("Animación1/intro00169.png")
freim170 = pygame.image.load("Animación1/intro00170.png")
freim171 = pygame.image.load("Animación1/intro00171.png")
freim172 = pygame.image.load("Animación1/intro00172.png")
freim173 = pygame.image.load("Animación1/intro00173.png")
freim174 = pygame.image.load("Animación1/intro00174.png")
freim175 = pygame.image.load("Animación1/intro00175.png")
freim176 = pygame.image.load("Animación1/intro00176.png")
freim177 = pygame.image.load("Animación1/intro00177.png")
freim178 = pygame.image.load("Animación1/intro00178.png")
freim179 = pygame.image.load("Animación1/intro00179.png")
freim180 = pygame.image.load("Animación1/intro00180.png")
freim181 = pygame.image.load("Animación1/intro00181.png")
freim182 = pygame.image.load("Animación1/intro00182.png")
freim183 = pygame.image.load("Animación1/intro00183.png")
freim184 = pygame.image.load("Animación1/intro00184.png")
freim185 = pygame.image.load("Animación1/intro00185.png")
freim186 = pygame.image.load("Animación1/intro00186.png")
freim187 = pygame.image.load("Animación1/intro00187.png")
freim188 = pygame.image.load("Animación1/intro00188.png")
freim189 = pygame.image.load("Animación1/intro00189.png")
freim190 = pygame.image.load("Animación1/intro00190.png")
freim191 = pygame.image.load("Animación1/intro00191.png")
freim192 = pygame.image.load("Animación1/intro00192.png")
freim193 = pygame.image.load("Animación1/intro00193.png")
freim194 = pygame.image.load("Animación1/intro00194.png")
freim195 = pygame.image.load("Animación1/intro00195.png")
freim196 = pygame.image.load("Animación1/intro00196.png")
freim197 = pygame.image.load("Animación1/intro00197.png")
freim198 = pygame.image.load("Animación1/intro00198.png")
freim199 = pygame.image.load("Animación1/intro00199.png")
freim200 = pygame.image.load("Animación1/intro00200.png")
freim201 = pygame.image.load("Animación1/intro00201.png")
freim202 = pygame.image.load("Animación1/intro00202.png")
freim203 = pygame.image.load("Animación1/intro00203.png")
freim204 = pygame.image.load("Animación1/intro00204.png")
freim205 = pygame.image.load("Animación1/intro00205.png")
freim206 = pygame.image.load("Animación1/intro00206.png")
freim207 = pygame.image.load("Animación1/intro00207.png")
freim208 = pygame.image.load("Animación1/intro00208.png")
freim209 = pygame.image.load("Animación1/intro00209.png")
freim210 = pygame.image.load("Animación1/intro00210.png")
freim211 = pygame.image.load("Animación1/intro00211.png")
freim212 = pygame.image.load("Animación1/intro00212.png")
freim213 = pygame.image.load("Animación1/intro00213.png")
freim214 = pygame.image.load("Animación1/intro00214.png")
freim215 = pygame.image.load("Animación1/intro00215.png")
freim216 = pygame.image.load("Animación1/intro00216.png")
freim217 = pygame.image.load("Animación1/intro00217.png")
freim218 = pygame.image.load("Animación1/intro00218.png")
freim219 = pygame.image.load("Animación1/intro00219.png")
freim220 = pygame.image.load("Animación1/intro00220.png")
freim221 = pygame.image.load("Animación1/intro00221.png")
freim222 = pygame.image.load("Animación1/intro00222.png")
freim223 = pygame.image.load("Animación1/intro00223.png")
freim224 = pygame.image.load("Animación1/intro00224.png")
freim225 = pygame.image.load("Animación1/intro00225.png")
freim226 = pygame.image.load("Animación1/intro00226.png")
freim227 = pygame.image.load("Animación1/intro00227.png")
freim228 = pygame.image.load("Animación1/intro00228.png")
freim229 = pygame.image.load("Animación1/intro00229.png")
freim230 = pygame.image.load("Animación1/intro00230.png")
freim231 = pygame.image.load("Animación1/intro00231.png")
freim232 = pygame.image.load("Animación1/intro00232.png")
freim233 = pygame.image.load("Animación1/intro00233.png")
freim234 = pygame.image.load("Animación1/intro00234.png")
freim235 = pygame.image.load("Animación1/intro00235.png")
freim236 = pygame.image.load("Animación1/intro00236.png")
freim237 = pygame.image.load("Animación1/intro00237.png")
freim238 = pygame.image.load("Animación1/intro00238.png")
freim239 = pygame.image.load("Animación1/intro00239.png")
freim240 = pygame.image.load("Animación1/intro00240.png")
freim241 = pygame.image.load("Animación1/intro00241.png")
freim242 = pygame.image.load("Animación1/intro00242.png")
freim243 = pygame.image.load("Animación1/intro00243.png")
freim244 = pygame.image.load("Animación1/intro00244.png")
freim245 = pygame.image.load("Animación1/intro00245.png")
freim246 = pygame.image.load("Animación1/intro00246.png")
freim247 = pygame.image.load("Animación1/intro00247.png")
freim248 = pygame.image.load("Animación1/intro00248.png")
freim249 = pygame.image.load("Animación1/intro00249.png")
freim250 = pygame.image.load("Animación1/intro00250.png")
freim251 = pygame.image.load("Animación1/intro00251.png")
freim252 = pygame.image.load("Animación1/intro00252.png")
freim253 = pygame.image.load("Animación1/intro00253.png")
freim254 = pygame.image.load("Animación1/intro00254.png")
freim255 = pygame.image.load("Animación1/intro00255.png")
freim256 = pygame.image.load("Animación1/intro00256.png")
freim257 = pygame.image.load("Animación1/intro00257.png")
freim258 = pygame.image.load("Animación1/intro00258.png")
freim259 = pygame.image.load("Animación1/intro00259.png")
freim260 = pygame.image.load("Animación1/intro00260.png")
freim261 = pygame.image.load("Animación1/intro00261.png")
freim262 = pygame.image.load("Animación1/intro00262.png")
freim263 = pygame.image.load("Animación1/intro00263.png")
freim264 = pygame.image.load("Animación1/intro00264.png")
freim265 = pygame.image.load("Animación1/intro00265.png")
freim266 = pygame.image.load("Animación1/intro00266.png")
freim267 = pygame.image.load("Animación1/intro00267.png")
freim268 = pygame.image.load("Animación1/intro00268.png")
freim269 = pygame.image.load("Animación1/intro00269.png")
freim270 = pygame.image.load("Animación1/intro00270.png")
freim271 = pygame.image.load("Animación1/intro00271.png")
freim272 = pygame.image.load("Animación1/intro00272.png")
freim273 = pygame.image.load("Animación1/intro00273.png")
freim274 = pygame.image.load("Animación1/intro00274.png")
freim275 = pygame.image.load("Animación1/intro00275.png")
freim276 = pygame.image.load("Animación1/intro00276.png")
freim277 = pygame.image.load("Animación1/intro00277.png")
freim278 = pygame.image.load("Animación1/intro00278.png")
freim279 = pygame.image.load("Animación1/intro00279.png")
freim280 = pygame.image.load("Animación1/intro00280.png")
freim281 = pygame.image.load("Animación1/intro00281.png")
freim282 = pygame.image.load("Animación1/intro00282.png")
freim283 = pygame.image.load("Animación1/intro00283.png")
freim284 = pygame.image.load("Animación1/intro00284.png")
freim285 = pygame.image.load("Animación1/intro00285.png")
freim286 = pygame.image.load("Animación1/intro00286.png")
freim287 = pygame.image.load("Animación1/intro00287.png")
freim288 = pygame.image.load("Animación1/intro00288.png")
freim289 = pygame.image.load("Animación1/intro00289.png")
freim290 = pygame.image.load("Animación1/intro00290.png")
freim291 = pygame.image.load("Animación1/intro00291.png")
freim292 = pygame.image.load("Animación1/intro00292.png")
freim293 = pygame.image.load("Animación1/intro00293.png")
freim294 = pygame.image.load("Animación1/intro00294.png")
freim295 = pygame.image.load("Animación1/intro00295.png")
freim296 = pygame.image.load("Animación1/intro00296.png")
freim297 = pygame.image.load("Animación1/intro00297.png")
freim298 = pygame.image.load("Animación1/intro00298.png")
freim299 = pygame.image.load("Animación1/intro00299.png")
freim300 = pygame.image.load("Animación1/intro00300.png")
freim301 = pygame.image.load("Animación1/intro00301.png")
freim302 = pygame.image.load("Animación1/intro00302.png")
freim303 = pygame.image.load("Animación1/intro00303.png")
freim304 = pygame.image.load("Animación1/intro00304.png")
freim305 = pygame.image.load("Animación1/intro00305.png")
freim306 = pygame.image.load("Animación1/intro00306.png")
freim307 = pygame.image.load("Animación1/intro00307.png")
freim308 = pygame.image.load("Animación1/intro00308.png")
freim309 = pygame.image.load("Animación1/intro00309.png")
freim310 = pygame.image.load("Animación1/intro00310.png")
freim311 = pygame.image.load("Animación1/intro00311.png")
freim312 = pygame.image.load("Animación1/intro00312.png")
freim313 = pygame.image.load("Animación1/intro00313.png")
freim314 = pygame.image.load("Animación1/intro00314.png")
freim315 = pygame.image.load("Animación1/intro00315.png")
freim316 = pygame.image.load("Animación1/intro00316.png")
freim317 = pygame.image.load("Animación1/intro00317.png")
freim318 = pygame.image.load("Animación1/intro00318.png")
freim319 = pygame.image.load("Animación1/intro00319.png")
freim320 = pygame.image.load("Animación1/intro00320.png")
freim321 = pygame.image.load("Animación1/intro00321.png")
freim322 = pygame.image.load("Animación1/intro00322.png")
freim323 = pygame.image.load("Animación1/intro00323.png")
freim324 = pygame.image.load("Animación1/intro00324.png")
freim325 = pygame.image.load("Animación1/intro00325.png")
freim326 = pygame.image.load("Animación1/intro00326.png")
freim327 = pygame.image.load("Animación1/intro00327.png")
freim328 = pygame.image.load("Animación1/intro00328.png")
freim329 = pygame.image.load("Animación1/intro00329.png")
freim330 = pygame.image.load("Animación1/intro00330.png")
freim331 = pygame.image.load("Animación1/intro00331.png")
freim332 = pygame.image.load("Animación1/intro00332.png")
freim333 = pygame.image.load("Animación1/intro00333.png")
freim334 = pygame.image.load("Animación1/intro00334.png")
freim335 = pygame.image.load("Animación1/intro00335.png")
freim336 = pygame.image.load("Animación1/intro00336.png")
freim337 = pygame.image.load("Animación1/intro00337.png")
freim338 = pygame.image.load("Animación1/intro00338.png")
freim339 = pygame.image.load("Animación1/intro00339.png")
freim340 = pygame.image.load("Animación1/intro00340.png")
freim341 = pygame.image.load("Animación1/intro00341.png")
freim342 = pygame.image.load("Animación1/intro00342.png")
freim343 = pygame.image.load("Animación1/intro00343.png")
freim344 = pygame.image.load("Animación1/intro00344.png")
freim345 = pygame.image.load("Animación1/intro00345.png")
freim346 = pygame.image.load("Animación1/intro00346.png")
freim347 = pygame.image.load("Animación1/intro00347.png")
freim348 = pygame.image.load("Animación1/intro00348.png")
freim349 = pygame.image.load("Animación1/intro00349.png")
freim350 = pygame.image.load("Animación1/intro00350.png")
freim351 = pygame.image.load("Animación1/intro00351.png")
freim352 = pygame.image.load("Animación1/intro00352.png")
freim353 = pygame.image.load("Animación1/intro00353.png")
freim354 = pygame.image.load("Animación1/intro00354.png")
freim355 = pygame.image.load("Animación1/intro00355.png")
freim356 = pygame.image.load("Animación1/intro00356.png")
freim357 = pygame.image.load("Animación1/intro00357.png")
freim358 = pygame.image.load("Animación1/intro00358.png")
freim359 = pygame.image.load("Animación1/intro00359.png")
freim360 = pygame.image.load("Animación1/intro00360.png")
freim361 = pygame.image.load("Animación1/intro00361.png")
freim362 = pygame.image.load("Animación1/intro00362.png")
freim363 = pygame.image.load("Animación1/intro00363.png")
freim364 = pygame.image.load("Animación1/intro00364.png")
freim365 = pygame.image.load("Animación1/intro00365.png")
freim366 = pygame.image.load("Animación1/intro00366.png")
freim367 = pygame.image.load("Animación1/intro00367.png")
freim368 = pygame.image.load("Animación1/intro00368.png")
freim369 = pygame.image.load("Animación1/intro00369.png")
freim370 = pygame.image.load("Animación1/intro00370.png")
freim371 = pygame.image.load("Animación1/intro00371.png")
freim372 = pygame.image.load("Animación1/intro00372.png")
freim373 = pygame.image.load("Animación1/intro00373.png")
freim374 = pygame.image.load("Animación1/intro00374.png")
freim375 = pygame.image.load("Animación1/intro00375.png")
freim376 = pygame.image.load("Animación1/intro00376.png")
freim377 = pygame.image.load("Animación1/intro00377.png")
freim378 = pygame.image.load("Animación1/intro00378.png")
freim379 = pygame.image.load("Animación1/intro00379.png")
freim380 = pygame.image.load("Animación1/intro00380.png")
freim381 = pygame.image.load("Animación1/intro00381.png")
freim382 = pygame.image.load("Animación1/intro00382.png")
freim383 = pygame.image.load("Animación1/intro00383.png")
freim384 = pygame.image.load("Animación1/intro00384.png")
freim385 = pygame.image.load("Animación1/intro00385.png")
freim386 = pygame.image.load("Animación1/intro00386.png")
freim387 = pygame.image.load("Animación1/intro00387.png")
freim388 = pygame.image.load("Animación1/intro00388.png")
freim389 = pygame.image.load("Animación1/intro00389.png")
freim390 = pygame.image.load("Animación1/intro00390.png")
freim391 = pygame.image.load("Animación1/intro00391.png")
freim392 = pygame.image.load("Animación1/intro00392.png")
freim393 = pygame.image.load("Animación1/intro00393.png")
freim394 = pygame.image.load("Animación1/intro00394.png")
freim395 = pygame.image.load("Animación1/intro00395.png")
freim396 = pygame.image.load("Animación1/intro00396.png")
freim397 = pygame.image.load("Animación1/intro00397.png")
freim398 = pygame.image.load("Animación1/intro00398.png")
freim399 = pygame.image.load("Animación1/intro00399.png")
freim400 = pygame.image.load("Animación1/intro00400.png")
freim401 = pygame.image.load("Animación1/intro00401.png")
freim402 = pygame.image.load("Animación1/intro00402.png")
freim403 = pygame.image.load("Animación1/intro00403.png")
freim404 = pygame.image.load("Animación1/intro00404.png")
freim405 = pygame.image.load("Animación1/intro00405.png")
freim406 = pygame.image.load("Animación1/intro00406.png")
freim407 = pygame.image.load("Animación1/intro00407.png")
freim408 = pygame.image.load("Animación1/intro00408.png")
freim409 = pygame.image.load("Animación1/intro00409.png")
freim410 = pygame.image.load("Animación1/intro00410.png")
freim411 = pygame.image.load("Animación1/intro00411.png")
freim412 = pygame.image.load("Animación1/intro00412.png")
freim413 = pygame.image.load("Animación1/intro00413.png")
freim414 = pygame.image.load("Animación1/intro00414.png")
freim415 = pygame.image.load("Animación1/intro00415.png")
freim416 = pygame.image.load("Animación1/intro00416.png")
freim417 = pygame.image.load("Animación1/intro00417.png")
freim418 = pygame.image.load("Animación1/intro00418.png")
freim418 = pygame.image.load("Animación1/intro00418.png")
freim419 = pygame.image.load("Animación1/intro00419.png")
freim420 = pygame.image.load("Animación1/intro00420.png")
freim421 = pygame.image.load("Animación1/intro00421.png")
freim422 = pygame.image.load("Animación1/intro00422.png")
freim423 = pygame.image.load("Animación1/intro00423.png")
freim424 = pygame.image.load("Animación1/intro00424.png")
freim425 = pygame.image.load("Animación1/intro00425.png")
freim426 = pygame.image.load("Animación1/intro00426.png")
freim427 = pygame.image.load("Animación1/intro00427.png")
freim428 = pygame.image.load("Animación1/intro00428.png")
freim429 = pygame.image.load("Animación1/intro00429.png")
freim430 = pygame.image.load("Animación1/intro00430.png")
freim431 = pygame.image.load("Animación1/intro00431.png")
freim432 = pygame.image.load("Animación1/intro00432.png")
freim433 = pygame.image.load("Animación1/intro00433.png")
freim434 = pygame.image.load("Animación1/intro00434.png")
freim435 = pygame.image.load("Animación1/intro00435.png")
freim436 = pygame.image.load("Animación1/intro00436.png")
freim437 = pygame.image.load("Animación1/intro00437.png")
freim438 = pygame.image.load("Animación1/intro00438.png")
freim439 = pygame.image.load("Animación1/intro00439.png")
freim440 = pygame.image.load("Animación1/intro00440.png")
freim441 = pygame.image.load("Animación1/intro00441.png")
freim442 = pygame.image.load("Animación1/intro00442.png")
freim443 = pygame.image.load("Animación1/intro00443.png")
freim444 = pygame.image.load("Animación1/intro00444.png")
freim445 = pygame.image.load("Animación1/intro00445.png")
freim446 = pygame.image.load("Animación1/intro00446.png")
freim447 = pygame.image.load("Animación1/intro00447.png")
freim448 = pygame.image.load("Animación1/intro00448.png")
freim449 = pygame.image.load("Animación1/intro00449.png")
freim450 = pygame.image.load("Animación1/intro00450.png")
freim451 = pygame.image.load("Animación1/intro00451.png")
freim452 = pygame.image.load("Animación1/intro00452.png")
freim453 = pygame.image.load("Animación1/intro00453.png")
freim454 = pygame.image.load("Animación1/intro00454.png")
freim455 = pygame.image.load("Animación1/intro00455.png")
freim456 = pygame.image.load("Animación1/intro00456.png")
freim457 = pygame.image.load("Animación1/intro00457.png")
freim458 = pygame.image.load("Animación1/intro00458.png")
freim459 = pygame.image.load("Animación1/intro00459.png")
freim460 = pygame.image.load("Animación1/intro00460.png")
freim461 = pygame.image.load("Animación1/intro00461.png")
freim462 = pygame.image.load("Animación1/intro00462.png")
freim463 = pygame.image.load("Animación1/intro00463.png")
freim464 = pygame.image.load("Animación1/intro00464.png")
freim465 = pygame.image.load("Animación1/intro00465.png")
freim466 = pygame.image.load("Animación1/intro00466.png")
freim467 = pygame.image.load("Animación1/intro00467.png")

freim1 = pygame.transform.scale(freim1, (800, 600))
freim2 = pygame.transform.scale(freim2, (800, 600))  
freim3 = pygame.transform.scale(freim3, (800, 600))  
freim4 = pygame.transform.scale(freim4, (800, 600))  
freim5 = pygame.transform.scale(freim5, (800, 600))  
freim6 = pygame.transform.scale(freim6, (800, 600))  
freim7 = pygame.transform.scale(freim7, (800, 600))  
freim8 = pygame.transform.scale(freim8, (800, 600))  
freim9 = pygame.transform.scale(freim9, (800, 600))  
freim10 = pygame.transform.scale(freim10, (800, 600))
freim11 = pygame.transform.scale(freim11, (800, 600))
freim12 = pygame.transform.scale(freim12, (800, 600))
freim13 = pygame.transform.scale(freim13, (800, 600))
freim14 = pygame.transform.scale(freim14, (800, 600))
freim15 = pygame.transform.scale(freim15, (800, 600))
freim16 = pygame.transform.scale(freim16, (800, 600))
freim17 = pygame.transform.scale(freim17, (800, 600))
freim18 = pygame.transform.scale(freim18, (800, 600))
freim19 = pygame.transform.scale(freim19, (800, 600))
freim20 = pygame.transform.scale(freim20, (800, 600))
freim21 = pygame.transform.scale(freim21, (800, 600))
freim22 = pygame.transform.scale(freim22, (800, 600))
freim23 = pygame.transform.scale(freim23, (800, 600))
freim24 = pygame.transform.scale(freim24, (800, 600))
freim25 = pygame.transform.scale(freim25, (800, 600))
freim26 = pygame.transform.scale(freim26, (800, 600))
freim27 = pygame.transform.scale(freim27, (800, 600))
freim28 = pygame.transform.scale(freim28, (800, 600))
freim29 = pygame.transform.scale(freim29, (800, 600))
freim30 = pygame.transform.scale(freim30, (800, 600))
freim31 = pygame.transform.scale(freim31, (800, 600))
freim32 = pygame.transform.scale(freim32, (800, 600))
freim33 = pygame.transform.scale(freim33, (800, 600))
freim34 = pygame.transform.scale(freim34, (800, 600))
freim35 = pygame.transform.scale(freim35, (800, 600))
freim36 = pygame.transform.scale(freim36, (800, 600))
freim37 = pygame.transform.scale(freim37, (800, 600))
freim38 = pygame.transform.scale(freim38, (800, 600))
freim39 = pygame.transform.scale(freim39, (800, 600))
freim40 = pygame.transform.scale(freim40, (800, 600))
freim41 = pygame.transform.scale(freim41, (800, 600))
freim42 = pygame.transform.scale(freim42, (800, 600))
freim43 = pygame.transform.scale(freim43, (800, 600))
freim44 = pygame.transform.scale(freim44, (800, 600))
freim45 = pygame.transform.scale(freim45, (800, 600))
freim46 = pygame.transform.scale(freim46, (800, 600))
freim47 = pygame.transform.scale(freim47, (800, 600))
freim48 = pygame.transform.scale(freim48, (800, 600))
freim49 = pygame.transform.scale(freim49, (800, 600))
freim50 = pygame.transform.scale(freim50, (800, 600))
freim51 = pygame.transform.scale(freim51, (800, 600))
freim52 = pygame.transform.scale(freim52, (800, 600))
freim53 = pygame.transform.scale(freim53, (800, 600))
freim54 = pygame.transform.scale(freim54, (800, 600))
freim55 = pygame.transform.scale(freim55, (800, 600))
freim56 = pygame.transform.scale(freim56, (800, 600))
freim57 = pygame.transform.scale(freim57, (800, 600))
freim58 = pygame.transform.scale(freim58, (800, 600))
freim59 = pygame.transform.scale(freim59, (800, 600))
freim60 = pygame.transform.scale(freim60, (800, 600))
freim61 = pygame.transform.scale(freim61, (800, 600))
freim62 = pygame.transform.scale(freim62, (800, 600))
freim63 = pygame.transform.scale(freim63, (800, 600))
freim64 = pygame.transform.scale(freim64, (800, 600))
freim65 = pygame.transform.scale(freim65, (800, 600))
freim66 = pygame.transform.scale(freim66, (800, 600))
freim67 = pygame.transform.scale(freim67, (800, 600))
freim68 = pygame.transform.scale(freim68, (800, 600))
freim69 = pygame.transform.scale(freim69, (800, 600))
freim70 = pygame.transform.scale(freim70, (800, 600))
freim71 = pygame.transform.scale(freim71, (800, 600))
freim72 = pygame.transform.scale(freim72, (800, 600))
freim73 = pygame.transform.scale(freim73, (800, 600))
freim74 = pygame.transform.scale(freim74, (800, 600))
freim75 = pygame.transform.scale(freim75, (800, 600))
freim76 = pygame.transform.scale(freim76, (800, 600))
freim77 = pygame.transform.scale(freim77, (800, 600))
freim78 = pygame.transform.scale(freim78, (800, 600))
freim79 = pygame.transform.scale(freim79, (800, 600))
freim80 = pygame.transform.scale(freim80, (800, 600))
freim81 = pygame.transform.scale(freim81, (800, 600))
freim82 = pygame.transform.scale(freim82, (800, 600))
freim83 = pygame.transform.scale(freim83, (800, 600))
freim84 = pygame.transform.scale(freim84, (800, 600))
freim85 = pygame.transform.scale(freim85, (800, 600))
freim86 = pygame.transform.scale(freim86, (800, 600))
freim87 = pygame.transform.scale(freim87, (800, 600))
freim88 = pygame.transform.scale(freim88, (800, 600))
freim89 = pygame.transform.scale(freim89, (800, 600))
freim90 = pygame.transform.scale(freim90, (800, 600))
freim91 = pygame.transform.scale(freim91, (800, 600))
freim92 = pygame.transform.scale(freim92, (800, 600))
freim93 = pygame.transform.scale(freim93, (800, 600))
freim94 = pygame.transform.scale(freim94, (800, 600))
freim95 = pygame.transform.scale(freim95, (800, 600))
freim96 = pygame.transform.scale(freim96, (800, 600))
freim97 = pygame.transform.scale(freim97, (800, 600))
freim98 = pygame.transform.scale(freim98, (800, 600))
freim99 = pygame.transform.scale(freim99, (800, 600))
freim100 = pygame.transform.scale(freim100, (800, 600))
freim101 = pygame.transform.scale(freim101, (800, 600))
freim102 = pygame.transform.scale(freim102, (800, 600))
freim103 = pygame.transform.scale(freim103, (800, 600))
freim104 = pygame.transform.scale(freim104, (800, 600))
freim105 = pygame.transform.scale(freim105, (800, 600))
freim106 = pygame.transform.scale(freim106, (800, 600))
freim107 = pygame.transform.scale(freim107, (800, 600))
freim108 = pygame.transform.scale(freim108, (800, 600))
freim109 = pygame.transform.scale(freim109, (800, 600))
freim110 = pygame.transform.scale(freim110, (800, 600))
freim111 = pygame.transform.scale(freim111, (800, 600))
freim112 = pygame.transform.scale(freim112, (800, 600))
freim113 = pygame.transform.scale(freim113, (800, 600))
freim114 = pygame.transform.scale(freim114, (800, 600))
freim115 = pygame.transform.scale(freim115, (800, 600))
freim116 = pygame.transform.scale(freim116, (800, 600))
freim117 = pygame.transform.scale(freim117, (800, 600))
freim118 = pygame.transform.scale(freim118, (800, 600))
freim119 = pygame.transform.scale(freim119, (800, 600))
freim120 = pygame.transform.scale(freim120, (800, 600))
freim121 = pygame.transform.scale(freim121, (800, 600))
freim122 = pygame.transform.scale(freim122, (800, 600))
freim123 = pygame.transform.scale(freim123, (800, 600))
freim124 = pygame.transform.scale(freim124, (800, 600))
freim125 = pygame.transform.scale(freim125, (800, 600))
freim126 = pygame.transform.scale(freim126, (800, 600))
freim127 = pygame.transform.scale(freim127, (800, 600))
freim128 = pygame.transform.scale(freim128, (800, 600))
freim129 = pygame.transform.scale(freim129, (800, 600))
freim130 = pygame.transform.scale(freim130, (800, 600))
freim131 = pygame.transform.scale(freim131, (800, 600))
freim132 = pygame.transform.scale(freim132, (800, 600))
freim133 = pygame.transform.scale(freim133, (800, 600))
freim134 = pygame.transform.scale(freim134, (800, 600))
freim135 = pygame.transform.scale(freim135, (800, 600))
freim136 = pygame.transform.scale(freim136, (800, 600))
freim137 = pygame.transform.scale(freim137, (800, 600))
freim138 = pygame.transform.scale(freim138, (800, 600))
freim139 = pygame.transform.scale(freim139, (800, 600))
freim140 = pygame.transform.scale(freim140, (800, 600))
freim141 = pygame.transform.scale(freim141, (800, 600))
freim142 = pygame.transform.scale(freim142, (800, 600))
freim143 = pygame.transform.scale(freim143, (800, 600))
freim144 = pygame.transform.scale(freim144, (800, 600))
freim145 = pygame.transform.scale(freim145, (800, 600))
freim146 = pygame.transform.scale(freim146, (800, 600))
freim147 = pygame.transform.scale(freim147, (800, 600))
freim148 = pygame.transform.scale(freim148, (800, 600))
freim149 = pygame.transform.scale(freim149, (800, 600))
freim150 = pygame.transform.scale(freim150, (800, 600))
freim151 = pygame.transform.scale(freim151, (800, 600))
freim152 = pygame.transform.scale(freim152, (800, 600))
freim153 = pygame.transform.scale(freim153, (800, 600))
freim154 = pygame.transform.scale(freim154, (800, 600))
freim155 = pygame.transform.scale(freim155, (800, 600))
freim156 = pygame.transform.scale(freim156, (800, 600))
freim157 = pygame.transform.scale(freim157, (800, 600))
freim158 = pygame.transform.scale(freim158, (800, 600))
freim159 = pygame.transform.scale(freim159, (800, 600))
freim160 = pygame.transform.scale(freim160, (800, 600))
freim161 = pygame.transform.scale(freim161, (800, 600))
freim162 = pygame.transform.scale(freim162, (800, 600))
freim163 = pygame.transform.scale(freim163, (800, 600))
freim164 = pygame.transform.scale(freim164, (800, 600))
freim165 = pygame.transform.scale(freim165, (800, 600))
freim166 = pygame.transform.scale(freim166, (800, 600))
freim167 = pygame.transform.scale(freim167, (800, 600))
freim168 = pygame.transform.scale(freim168, (800, 600))
freim169 = pygame.transform.scale(freim169, (800, 600))
freim170 = pygame.transform.scale(freim170, (800, 600))
freim171 = pygame.transform.scale(freim171, (800, 600))
freim172 = pygame.transform.scale(freim172, (800, 600))
freim173 = pygame.transform.scale(freim173, (800, 600))
freim174 = pygame.transform.scale(freim174, (800, 600))
freim175 = pygame.transform.scale(freim175, (800, 600))
freim176 = pygame.transform.scale(freim176, (800, 600))
freim177 = pygame.transform.scale(freim177, (800, 600))
freim178 = pygame.transform.scale(freim178, (800, 600))
freim179 = pygame.transform.scale(freim179, (800, 600))
freim180 = pygame.transform.scale(freim180, (800, 600))
freim181 = pygame.transform.scale(freim181, (800, 600))
freim182 = pygame.transform.scale(freim182, (800, 600))
freim183 = pygame.transform.scale(freim183, (800, 600))
freim184 = pygame.transform.scale(freim184, (800, 600))
freim185 = pygame.transform.scale(freim185, (800, 600))
freim186 = pygame.transform.scale(freim186, (800, 600))
freim187 = pygame.transform.scale(freim187, (800, 600))
freim188 = pygame.transform.scale(freim188, (800, 600))
freim189 = pygame.transform.scale(freim189, (800, 600))
freim190 = pygame.transform.scale(freim190, (800, 600))
freim191 = pygame.transform.scale(freim191, (800, 600))
freim192 = pygame.transform.scale(freim192, (800, 600))
freim193 = pygame.transform.scale(freim193, (800, 600))
freim194 = pygame.transform.scale(freim194, (800, 600))
freim195 = pygame.transform.scale(freim195, (800, 600))
freim196 = pygame.transform.scale(freim196, (800, 600))
freim197 = pygame.transform.scale(freim197, (800, 600))
freim198 = pygame.transform.scale(freim198, (800, 600))
freim199 = pygame.transform.scale(freim199, (800, 600))
freim200 = pygame.transform.scale(freim200, (800, 600))
freim201 = pygame.transform.scale(freim201, (800, 600))
freim202 = pygame.transform.scale(freim202, (800, 600))
freim203 = pygame.transform.scale(freim203, (800, 600))
freim204 = pygame.transform.scale(freim204, (800, 600))
freim205 = pygame.transform.scale(freim205, (800, 600))
freim206 = pygame.transform.scale(freim206, (800, 600))
freim207 = pygame.transform.scale(freim207, (800, 600))
freim208 = pygame.transform.scale(freim208, (800, 600))
freim209 = pygame.transform.scale(freim209, (800, 600))
freim210 = pygame.transform.scale(freim210, (800, 600))
freim211 = pygame.transform.scale(freim211, (800, 600))
freim212 = pygame.transform.scale(freim212, (800, 600))
freim213 = pygame.transform.scale(freim213, (800, 600))
freim214 = pygame.transform.scale(freim214, (800, 600))
freim215 = pygame.transform.scale(freim215, (800, 600))
freim216 = pygame.transform.scale(freim216, (800, 600))
freim217 = pygame.transform.scale(freim217, (800, 600))
freim218 = pygame.transform.scale(freim218, (800, 600))
freim219 = pygame.transform.scale(freim219, (800, 600))
freim220 = pygame.transform.scale(freim220, (800, 600))
freim221 = pygame.transform.scale(freim221, (800, 600))
freim222 = pygame.transform.scale(freim222, (800, 600))
freim223 = pygame.transform.scale(freim223, (800, 600))
freim224 = pygame.transform.scale(freim224, (800, 600))
freim225 = pygame.transform.scale(freim225, (800, 600))
freim226 = pygame.transform.scale(freim226, (800, 600))
freim227 = pygame.transform.scale(freim227, (800, 600))
freim228 = pygame.transform.scale(freim228, (800, 600))
freim229 = pygame.transform.scale(freim229, (800, 600))
freim230 = pygame.transform.scale(freim230, (800, 600))
freim231 = pygame.transform.scale(freim231, (800, 600))
freim232 = pygame.transform.scale(freim232, (800, 600))
freim233 = pygame.transform.scale(freim233, (800, 600))
freim234 = pygame.transform.scale(freim234, (800, 600))
freim235 = pygame.transform.scale(freim235, (800, 600))
freim236 = pygame.transform.scale(freim236, (800, 600))
freim237 = pygame.transform.scale(freim237, (800, 600))
freim238 = pygame.transform.scale(freim238, (800, 600))
freim239 = pygame.transform.scale(freim239, (800, 600))
freim240 = pygame.transform.scale(freim240, (800, 600))
freim241 = pygame.transform.scale(freim241, (800, 600))
freim242 = pygame.transform.scale(freim242, (800, 600))
freim243 = pygame.transform.scale(freim243, (800, 600))
freim244 = pygame.transform.scale(freim244, (800, 600))
freim245 = pygame.transform.scale(freim245, (800, 600))
freim246 = pygame.transform.scale(freim246, (800, 600))
freim247 = pygame.transform.scale(freim247, (800, 600))
freim248 = pygame.transform.scale(freim248, (800, 600))
freim249 = pygame.transform.scale(freim249, (800, 600))
freim250 = pygame.transform.scale(freim250, (800, 600))
freim251 = pygame.transform.scale(freim251, (800, 600))
freim252 = pygame.transform.scale(freim252, (800, 600))
freim253 = pygame.transform.scale(freim253, (800, 600))
freim254 = pygame.transform.scale(freim254, (800, 600))
freim255 = pygame.transform.scale(freim255, (800, 600))
freim256 = pygame.transform.scale(freim256, (800, 600))
freim257 = pygame.transform.scale(freim257, (800, 600))
freim258 = pygame.transform.scale(freim258, (800, 600))
freim259 = pygame.transform.scale(freim259, (800, 600))
freim260 = pygame.transform.scale(freim260, (800, 600))
freim261 = pygame.transform.scale(freim261, (800, 600))
freim262 = pygame.transform.scale(freim262, (800, 600))
freim263 = pygame.transform.scale(freim263, (800, 600))
freim264 = pygame.transform.scale(freim264, (800, 600))
freim265 = pygame.transform.scale(freim265, (800, 600))
freim266 = pygame.transform.scale(freim266, (800, 600))
freim267 = pygame.transform.scale(freim267, (800, 600))
freim268 = pygame.transform.scale(freim268, (800, 600))
freim269 = pygame.transform.scale(freim269, (800, 600))
freim270 = pygame.transform.scale(freim270, (800, 600))
freim271 = pygame.transform.scale(freim271, (800, 600))
freim272 = pygame.transform.scale(freim272, (800, 600))
freim273 = pygame.transform.scale(freim273, (800, 600))
freim274 = pygame.transform.scale(freim274, (800, 600))
freim275 = pygame.transform.scale(freim275, (800, 600))
freim276 = pygame.transform.scale(freim276, (800, 600))
freim277 = pygame.transform.scale(freim277, (800, 600))
freim278 = pygame.transform.scale(freim278, (800, 600))
freim279 = pygame.transform.scale(freim279, (800, 600))
freim280 = pygame.transform.scale(freim280, (800, 600))
freim281 = pygame.transform.scale(freim281, (800, 600))
freim282 = pygame.transform.scale(freim282, (800, 600))
freim283 = pygame.transform.scale(freim283, (800, 600))
freim284 = pygame.transform.scale(freim284, (800, 600))
freim285 = pygame.transform.scale(freim285, (800, 600))
freim286 = pygame.transform.scale(freim286, (800, 600))
freim287 = pygame.transform.scale(freim287, (800, 600))
freim288 = pygame.transform.scale(freim288, (800, 600))
freim289 = pygame.transform.scale(freim289, (800, 600))
freim290 = pygame.transform.scale(freim290, (800, 600))
freim291 = pygame.transform.scale(freim291, (800, 600))
freim292 = pygame.transform.scale(freim292, (800, 600))
freim293 = pygame.transform.scale(freim293, (800, 600))
freim294 = pygame.transform.scale(freim294, (800, 600))
freim295 = pygame.transform.scale(freim295, (800, 600))
freim296 = pygame.transform.scale(freim296, (800, 600))
freim297 = pygame.transform.scale(freim297, (800, 600))
freim298 = pygame.transform.scale(freim298, (800, 600))
freim299 = pygame.transform.scale(freim299, (800, 600))
freim300 = pygame.transform.scale(freim300, (800, 600))
freim301 = pygame.transform.scale(freim301, (800, 600))
freim302 = pygame.transform.scale(freim302, (800, 600))
freim303 = pygame.transform.scale(freim303, (800, 600))
freim304 = pygame.transform.scale(freim304, (800, 600))
freim305 = pygame.transform.scale(freim305, (800, 600))
freim306 = pygame.transform.scale(freim306, (800, 600))
freim307 = pygame.transform.scale(freim307, (800, 600))
freim308 = pygame.transform.scale(freim308, (800, 600))
freim309 = pygame.transform.scale(freim309, (800, 600))
freim310 = pygame.transform.scale(freim310, (800, 600))
freim311 = pygame.transform.scale(freim311, (800, 600))
freim312 = pygame.transform.scale(freim312, (800, 600))
freim313 = pygame.transform.scale(freim313, (800, 600))
freim314 = pygame.transform.scale(freim314, (800, 600))
freim315 = pygame.transform.scale(freim315, (800, 600))
freim316 = pygame.transform.scale(freim316, (800, 600))
freim317 = pygame.transform.scale(freim317, (800, 600))
freim318 = pygame.transform.scale(freim318, (800, 600))
freim319 = pygame.transform.scale(freim319, (800, 600))
freim320 = pygame.transform.scale(freim320, (800, 600))
freim321 = pygame.transform.scale(freim321, (800, 600))
freim322 = pygame.transform.scale(freim322, (800, 600))
freim323 = pygame.transform.scale(freim323, (800, 600))
freim324 = pygame.transform.scale(freim324, (800, 600))
freim325 = pygame.transform.scale(freim325, (800, 600))
freim326 = pygame.transform.scale(freim326, (800, 600))
freim327 = pygame.transform.scale(freim327, (800, 600))
freim328 = pygame.transform.scale(freim328, (800, 600))
freim329 = pygame.transform.scale(freim329, (800, 600))
freim330 = pygame.transform.scale(freim330, (800, 600))
freim331 = pygame.transform.scale(freim331, (800, 600))
freim332 = pygame.transform.scale(freim332, (800, 600))
freim333 = pygame.transform.scale(freim333, (800, 600))
freim334 = pygame.transform.scale(freim334, (800, 600))
freim335 = pygame.transform.scale(freim335, (800, 600))
freim336 = pygame.transform.scale(freim336, (800, 600))
freim337 = pygame.transform.scale(freim337, (800, 600))
freim338 = pygame.transform.scale(freim338, (800, 600))
freim339 = pygame.transform.scale(freim339, (800, 600))
freim340 = pygame.transform.scale(freim340, (800, 600))
freim341 = pygame.transform.scale(freim341, (800, 600))
freim342 = pygame.transform.scale(freim342, (800, 600))
freim343 = pygame.transform.scale(freim343, (800, 600))
freim344 = pygame.transform.scale(freim344, (800, 600))
freim345 = pygame.transform.scale(freim345, (800, 600))
freim346 = pygame.transform.scale(freim346, (800, 600))
freim347 = pygame.transform.scale(freim347, (800, 600))
freim348 = pygame.transform.scale(freim348, (800, 600))
freim349 = pygame.transform.scale(freim349, (800, 600))
freim350 = pygame.transform.scale(freim350, (800, 600))
freim351 = pygame.transform.scale(freim351, (800, 600))
freim352 = pygame.transform.scale(freim352, (800, 600))
freim353 = pygame.transform.scale(freim353, (800, 600))
freim354 = pygame.transform.scale(freim354, (800, 600))
freim355 = pygame.transform.scale(freim355, (800, 600))
freim356 = pygame.transform.scale(freim356, (800, 600))
freim357 = pygame.transform.scale(freim357, (800, 600))
freim358 = pygame.transform.scale(freim358, (800, 600))
freim359 = pygame.transform.scale(freim359, (800, 600))
freim360 = pygame.transform.scale(freim360, (800, 600))
freim361 = pygame.transform.scale(freim361, (800, 600))
freim362 = pygame.transform.scale(freim362, (800, 600))
freim363 = pygame.transform.scale(freim363, (800, 600))
freim364 = pygame.transform.scale(freim364, (800, 600))
freim365 = pygame.transform.scale(freim365, (800, 600))
freim366 = pygame.transform.scale(freim366, (800, 600))
freim367 = pygame.transform.scale(freim367, (800, 600))
freim368 = pygame.transform.scale(freim368, (800, 600))
freim369 = pygame.transform.scale(freim369, (800, 600))
freim370 = pygame.transform.scale(freim370, (800, 600))
freim371 = pygame.transform.scale(freim371, (800, 600))
freim372 = pygame.transform.scale(freim372, (800, 600))
freim373 = pygame.transform.scale(freim373, (800, 600))
freim374 = pygame.transform.scale(freim374, (800, 600))
freim375 = pygame.transform.scale(freim375, (800, 600))
freim376 = pygame.transform.scale(freim376, (800, 600))
freim377 = pygame.transform.scale(freim377, (800, 600))
freim378 = pygame.transform.scale(freim378, (800, 600))
freim379 = pygame.transform.scale(freim379, (800, 600))
freim380 = pygame.transform.scale(freim380, (800, 600))
freim381 = pygame.transform.scale(freim381, (800, 600))
freim382 = pygame.transform.scale(freim382, (800, 600))
freim383 = pygame.transform.scale(freim383, (800, 600))
freim384 = pygame.transform.scale(freim384, (800, 600))
freim385 = pygame.transform.scale(freim385, (800, 600))
freim386 = pygame.transform.scale(freim386, (800, 600))
freim387 = pygame.transform.scale(freim387, (800, 600))
freim388 = pygame.transform.scale(freim388, (800, 600))
freim389 = pygame.transform.scale(freim389, (800, 600))
freim390 = pygame.transform.scale(freim390, (800, 600))
freim391 = pygame.transform.scale(freim391, (800, 600))
freim392 = pygame.transform.scale(freim392, (800, 600))
freim393 = pygame.transform.scale(freim393, (800, 600))
freim394 = pygame.transform.scale(freim394, (800, 600))
freim395 = pygame.transform.scale(freim395, (800, 600))
freim396 = pygame.transform.scale(freim396, (800, 600))
freim397 = pygame.transform.scale(freim397, (800, 600))
freim398 = pygame.transform.scale(freim398, (800, 600))
freim399 = pygame.transform.scale(freim399, (800, 600))
freim400 = pygame.transform.scale(freim400, (800, 600))
freim401 = pygame.transform.scale(freim401, (800, 600))
freim402 = pygame.transform.scale(freim402, (800, 600))
freim403 = pygame.transform.scale(freim403, (800, 600))
freim404 = pygame.transform.scale(freim404, (800, 600))
freim405 = pygame.transform.scale(freim405, (800, 600))
freim406 = pygame.transform.scale(freim406, (800, 600))
freim407 = pygame.transform.scale(freim407, (800, 600))
freim408 = pygame.transform.scale(freim408, (800, 600))
freim409 = pygame.transform.scale(freim409, (800, 600))
freim410 = pygame.transform.scale(freim410, (800, 600))
freim411 = pygame.transform.scale(freim411, (800, 600))
freim412 = pygame.transform.scale(freim412, (800, 600))
freim413 = pygame.transform.scale(freim413, (800, 600))
freim414 = pygame.transform.scale(freim414, (800, 600))
freim415 = pygame.transform.scale(freim415, (800, 600))
freim416 = pygame.transform.scale(freim416, (800, 600))
freim417 = pygame.transform.scale(freim417, (800, 600))
freim418 = pygame.transform.scale(freim418, (800, 600))
freim418 = pygame.transform.scale(freim418, (800, 600))
freim419 = pygame.transform.scale(freim419, (800, 600))
freim420 = pygame.transform.scale(freim420, (800, 600))
freim421 = pygame.transform.scale(freim421, (800, 600))
freim422 = pygame.transform.scale(freim422, (800, 600))
freim423 = pygame.transform.scale(freim423, (800, 600))
freim424 = pygame.transform.scale(freim424, (800, 600))
freim425 = pygame.transform.scale(freim425, (800, 600))
freim426 = pygame.transform.scale(freim426, (800, 600))
freim427 = pygame.transform.scale(freim427, (800, 600))
freim428 = pygame.transform.scale(freim428, (800, 600))
freim429 = pygame.transform.scale(freim429, (800, 600))
freim430 = pygame.transform.scale(freim430, (800, 600))
freim431 = pygame.transform.scale(freim431, (800, 600))
freim432 = pygame.transform.scale(freim432, (800, 600))
freim433 = pygame.transform.scale(freim433, (800, 600))
freim434 = pygame.transform.scale(freim434, (800, 600))
freim435 = pygame.transform.scale(freim435, (800, 600))
freim436 = pygame.transform.scale(freim436, (800, 600))
freim437 = pygame.transform.scale(freim437, (800, 600))
freim438 = pygame.transform.scale(freim438, (800, 600))
freim439 = pygame.transform.scale(freim439, (800, 600))
freim440 = pygame.transform.scale(freim440, (800, 600))
freim441 = pygame.transform.scale(freim441, (800, 600))
freim442 = pygame.transform.scale(freim442, (800, 600))
freim443 = pygame.transform.scale(freim443, (800, 600))
freim444 = pygame.transform.scale(freim444, (800, 600))
freim445 = pygame.transform.scale(freim445, (800, 600))
freim446 = pygame.transform.scale(freim446, (800, 600))
freim447 = pygame.transform.scale(freim447, (800, 600))
freim448 = pygame.transform.scale(freim448, (800, 600))
freim449 = pygame.transform.scale(freim449, (800, 600))
freim450 = pygame.transform.scale(freim450, (800, 600))
freim451 = pygame.transform.scale(freim451, (800, 600))
freim452 = pygame.transform.scale(freim452, (800, 600))
freim453 = pygame.transform.scale(freim453, (800, 600))
freim454 = pygame.transform.scale(freim454, (800, 600))
freim455 = pygame.transform.scale(freim455, (800, 600))
freim456 = pygame.transform.scale(freim456, (800, 600))
freim457 = pygame.transform.scale(freim457, (800, 600))
freim458 = pygame.transform.scale(freim458, (800, 600))
freim459 = pygame.transform.scale(freim459, (800, 600))
freim460 = pygame.transform.scale(freim460, (800, 600))
freim461 = pygame.transform.scale(freim461, (800, 600))
freim462 = pygame.transform.scale(freim462, (800, 600))
freim463 = pygame.transform.scale(freim463, (800, 600))
freim464 = pygame.transform.scale(freim464, (800, 600))
freim465 = pygame.transform.scale(freim465, (800, 600))
freim466 = pygame.transform.scale(freim466, (800, 600))
freim467 = pygame.transform.scale(freim467, (800, 600))
def delete_intro_img():
    del freim1
    del freim2
    del freim3
    del freim4
    del freim5
    del freim6
    del freim7
    del freim8
    del freim9
    del freim10
    del freim11
    del freim12
    del freim13
    del freim14
    del freim15
    del freim16
    del freim17
    del freim18
    del freim19
    del freim20
    del freim21
    del freim22
    del freim23
    del freim24
    del freim25
    del freim26
    del freim27
    del freim28
    del freim29
    del freim30
    del freim31
    del freim32
    del freim33
    del freim34
    del freim35
    del freim36
    del freim37
    del freim38
    del freim39
    del freim40
    del freim41
    del freim42
    del freim43
    del freim44
    del freim45
    del freim46
    del freim47
    del freim48
    del freim49
    del freim50
    del freim51
    del freim52
    del freim53
    del freim54
    del freim55
    del freim56
    del freim57
    del freim58
    del freim59
    del freim60
    del freim61
    del freim62
    del freim63
    del freim64
    del freim65
    del freim66
    del freim67
    del freim68
    del freim69
    del freim70
    del freim71
    del freim72
    del freim73
    del freim74
    del freim75
    del freim76
    del freim77
    del freim78
    del freim79
    del freim80
    del freim81
    del freim82
    del freim83
    del freim84
    del freim85
    del freim86
    del freim87
    del freim88
    del freim89
    del freim90
    del freim91
    del freim92
    del freim93
    del freim94
    del freim95
    del freim96
    del freim97
    del freim98
    del freim99
    del freim100
    del freim101
    del freim102
    del freim103
    del freim104
    del freim105
    del freim106
    del freim107
    del freim108
    del freim109
    del freim110
    del freim111
    del freim112
    del freim113
    del freim114
    del freim115
    del freim116
    del freim117
    del freim118
    del freim119
    del freim120
    del freim121
    del freim122
    del freim123
    del freim124
    del freim125
    del freim126
    del freim127
    del freim128
    del freim129
    del freim130
    del freim131
    del freim132
    del freim133
    del freim134
    del freim135
    del freim136
    del freim137
    del freim138
    del freim139
    del freim140
    del freim141
    del freim142
    del freim143
    del freim144
    del freim145
    del freim146
    del freim147
    del freim148
    del freim149
    del freim150
    del freim151
    del freim152
    del freim153
    del freim154
    del freim155
    del freim156
    del freim157
    del freim158
    del freim159
    del freim160
    del freim161
    del freim162
    del freim163
    del freim164
    del freim165
    del freim166
    del freim167
    del freim168
    del freim169
    del freim170
    del freim171
    del freim172
    del freim173
    del freim174
    del freim175
    del freim176
    del freim177
    del freim178
    del freim179
    del freim180
    del freim181
    del freim182
    del freim183
    del freim184
    del freim185
    del freim186
    del freim187
    del freim188
    del freim189
    del freim190
    del freim191
    del freim192
    del freim193
    del freim194
    del freim195
    del freim196
    del freim197
    del freim198
    del freim199
    del freim200
    del freim201
    del freim202
    del freim203
    del freim204
    del freim205
    del freim206
    del freim207
    del freim208
    del freim209
    del freim210
    del freim211
    del freim212
    del freim213
    del freim214
    del freim215
    del freim216
    del freim217
    del freim218
    del freim219
    del freim220
    del freim221
    del freim222
    del freim223
    del freim224
    del freim225
    del freim226
    del freim227
    del freim228
    del freim229
    del freim230
    del freim231
    del freim232
    del freim233
    del freim234
    del freim235
    del freim236
    del freim237
    del freim238
    del freim239
    del freim240
    del freim241
    del freim242
    del freim243
    del freim244
    del freim245
    del freim246
    del freim247
    del freim248
    del freim249
    del freim250
    del freim251
    del freim252
    del freim253
    del freim254
    del freim255
    del freim256
    del freim257
    del freim258
    del freim259
    del freim260
    del freim261
    del freim262
    del freim263
    del freim264
    del freim265
    del freim266
    del freim267
    del freim268
    del freim269
    del freim270
    del freim271
    del freim272
    del freim273
    del freim274
    del freim275
    del freim276
    del freim277
    del freim278
    del freim279
    del freim280
    del freim281
    del freim282
    del freim283
    del freim284
    del freim285
    del freim286
    del freim287
    del freim288
    del freim289
    del freim290
    del freim291
    del freim292
    del freim293
    del freim294
    del freim295
    del freim296
    del freim297
    del freim298
    del freim299
    del freim300
    del freim301
    del freim302
    del freim303
    del freim304
    del freim305
    del freim306
    del freim307
    del freim308
    del freim309
    del freim310
    del freim311
    del freim312
    del freim313
    del freim314
    del freim315
    del freim316
    del freim317
    del freim318
    del freim319
    del freim320
    del freim321
    del freim322
    del freim323
    del freim324
    del freim325
    del freim326
    del freim327
    del freim328
    del freim329
    del freim330
    del freim331
    del freim332
    del freim333
    del freim334
    del freim335
    del freim336
    del freim337
    del freim338
    del freim339
    del freim340
    del freim341
    del freim342
    del freim343
    del freim344
    del freim345
    del freim346
    del freim347
    del freim348
    del freim349
    del freim350
    del freim351
    del freim352
    del freim353
    del freim354
    del freim355
    del freim356
    del freim357
    del freim358
    del freim359
    del freim360
    del freim361
    del freim362
    del freim363
    del freim364
    del freim365
    del freim366
    del freim367
    del freim368
    del freim369
    del freim370
    del freim371
    del freim372
    del freim373
    del freim374
    del freim375
    del freim376
    del freim377
    del freim378
    del freim379
    del freim380
    del freim381
    del freim382
    del freim383
    del freim384
    del freim385
    del freim386
    del freim387
    del freim388
    del freim389
    del freim390
    del freim391
    del freim392
    del freim393
    del freim394
    del freim395
    del freim396
    del freim397
    del freim398
    del freim399
    del freim400
    del freim401
    del freim402
    del freim403
    del freim404
    del freim405
    del freim406
    del freim407
    del freim408
    del freim409
    del freim410
    del freim411
    del freim412
    del freim413
    del freim414
    del freim415
    del freim416
    del freim417
    del freim418
    del freim419
    del freim420
    del freim421
    del freim422
    del freim423
    del freim424
    del freim425
    del freim426
    del freim427
    del freim428
    del freim429
    del freim430
    del freim431
    del freim432
    del freim433
    del freim434
    del freim435
    del freim436
    del freim437
    del freim438
    del freim439
    del freim440
    del freim441
    del freim442
    del freim443
    del freim444
    del freim445
    del freim446
    del freim447
    del freim448
    del freim449
    del freim450
    del freim451
    del freim452
    del freim453
    del freim454
    del freim455
    del freim456
    del freim457
    del freim458
    del freim459
    del freim460
    del freim461
    del freim462
    del freim463
    del freim464
    del freim465
    del freim466
    del freim467

# Animación intro - parte2
background_image = pygame.image.load("Animación2/title1.png")
background_image2 = pygame.image.load("Animación2/title2.png")
background_image3 = pygame.image.load("Animación2/title3.png")
background_image4 = pygame.image.load("Animación2/title4.png")
background_image5 = pygame.image.load("Animación2/title5.png")

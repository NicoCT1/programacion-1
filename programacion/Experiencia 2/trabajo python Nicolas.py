# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 07:52:05 2025

@author: AULA
"""

ref = {
    'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
    'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 10},
    'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
    'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 20}
}



cubiculos = [
  [
    {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 3},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 3}
    },
    {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 5},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 2},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 1}
    },
   {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 10},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 16}
    },
  ],
  [
   {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 8},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 7},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 7}
    },
    {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 5},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 6},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 10}
    },
   {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 10},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 6}
    },
  ]
]
#%%

cubiculos[0]
cubiculos[1]

cubiculos[1][0]
cubiculos[1][0]["Camilla"]
cubiculos[1][0]["Camilla"]["Cantidad"]

cont_cubiculos = 0

for cubiculo in cubiculos:
    
    cont_cubiculos +=1
    cont_pacientes = 0
    print("cubiculo ", cont_cubiculos)
    print("------------------------")

    for paciente in cubiculo:
        
        cont_pacientes += 1
        print (paciente)
        print("paciente ", cont_pacientes)
        print("------------------------")
        
        for insumos in paciente:
            print(insumos)
            
            for cant in insumos["cantidad"]:
                
                print(cant)
                
                
    print("------------------------")
# %%
    
ref = {
    'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
    'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 10},
    'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
    'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 20}
}


for cubiculo in range(len(cubiculos)):
    print ("cubiculos", cubiculos+1)
    print("----------")
    for paciente in range(len(cubiculos[cubiculo])):
        print ("paciente", paciente+1)
        for insumos in cubiculos[cubiculo][paciente]:
            print("Insumo -", cubiculos[cubiculo][paciente][insumo]["Cantidad"])        























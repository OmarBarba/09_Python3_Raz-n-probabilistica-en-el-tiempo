from pgmpy.models import DynamicBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference
import numpy as np

# Crear un modelo de Red Bayesiana Dinámica
model = DynamicBayesianNetwork()

# Definir las variables y las tablas de probabilidad condicional (CPD)
estado_traffic = 'Traffic'
cpd_traffic_t0 = TabularCPD(variable=estado_traffic, variable_card=3, 
                            values=[[0.4], [0.4], [0.2]], state_names={estado_traffic: ['Light', 'Moderate', 'Heavy']})
cpd_traffic_t1 = TabularCPD(variable=estado_traffic, variable_card=3, 
                            values=[[0.3, 0.7, 0.1, 0.5, 0.2, 0.1, 0.1, 0.1, 0.7],
                                    [0.6, 0.2, 0.6, 0.4, 0.6, 0.6, 0.3, 0.5, 0.2],
                                    [0.1, 0.1, 0.3, 0.1, 0.2, 0.3, 0.6, 0.4, 0.1]],
                            evidence=[estado_traffic],
                            evidence_card=[3], state_names={estado_traffic: ['Light', 'Moderate', 'Heavy']})

# Agregar variables y CPD al modelo
model.add_edge(estado_traffic, estado_traffic, time_slice=0)
model.add_edge(estado_traffic, estado_traffic, time_slice=1)
model.add_cpds(cpd_traffic_t0, cpd_traffic_t1)

# Inferencia en la Red Bayesiana Dinámica
inference = DBNInference(model)
inference.get_independencies()

# Calcular la probabilidad de la condición futura
result = inference.query(variables=[estado_traffic], evidence={estado_traffic: 'Light'}, time_slice=1)
print(result)

# Calcular la probabilidad de la condición presente
result = inference.query(variables=[estado_traffic], evidence={estado_traffic: 'Light'}, time_slice=0)
print(result)

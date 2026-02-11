# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.4.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 9
VARIABLE_COUNT = 134


class VariableType(Enum):
    VARIABLE_OF_INTEGRATION = 0
    STATE = 1
    CONSTANT = 2
    COMPUTED_CONSTANT = 3
    ALGEBRAIC = 4


VOI_INFO = {"name": "time", "units": "second", "component": "environment", "type": VariableType.VARIABLE_OF_INTEGRATION}

STATE_INFO = [
    {"name": "q_C", "units": "m3", "component": "L2_E0_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "L2_E1_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "L2_E2_module", "type": VariableType.STATE},
    {"name": "q_C_d", "units": "m3", "component": "L2_E3_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "L2_E3_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "L2_E4_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "L2_E5_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "L2_E6_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "L2_E7_module", "type": VariableType.STATE}
]

VARIABLE_INFO = [
    {"name": "E_L2_E0", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "l_L2_E0", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "r_0_L2_E0", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_L2_E0", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_L2_E0", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "theta_L2_E0", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "E_L2_E1", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "l_L2_E1", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "r_0_L2_E1", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_L2_E1", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_L2_E1", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "theta_L2_E1", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "E_L2_E2", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "l_L2_E2", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "r_0_L2_E2", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_L2_E2", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_L2_E2", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "theta_L2_E2", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "E_L2_E3", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "l_L2_E3", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "r_0_L2_E3", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_L2_E3", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "theta_L2_E3", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_L2_E3", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "E_L2_E4", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "l_L2_E4", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "r_0_L2_E4", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_L2_E4", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_L2_E4", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "theta_L2_E4", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "E_L2_E5", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "l_L2_E5", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "r_0_L2_E5", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_L2_E5", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_L2_E5", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "theta_L2_E5", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "E_L2_E6", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "l_L2_E6", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "r_0_L2_E6", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_L2_E6", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_L2_E6", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "theta_L2_E6", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "E_L2_E7", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "l_L2_E7", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "r_0_L2_E7", "units": "metre", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_L2_E7", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_L2_E7", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "theta_L2_E7", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "P_L2_E2_PI", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "P_L2_E6_PO", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "beta_g", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "rho", "units": "kg_per_m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "mu", "units": "Js_per_m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "g", "units": "m_per_s2", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "a_vessel", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "b_vessel", "units": "per_m", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "c_vessel", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "d_vessel", "units": "per_m", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_0", "units": "m3", "component": "L2_E0_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q", "units": "m3", "component": "L2_E0_module", "type": VariableType.ALGEBRAIC},
    {"name": "h", "units": "metre", "component": "L2_E0_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "C", "units": "m6_per_J", "component": "L2_E0_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R", "units": "Js_per_m6", "component": "L2_E0_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "L2_E0_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u", "units": "J_per_m3", "component": "L2_E3_module", "type": VariableType.ALGEBRAIC},
    {"name": "u", "units": "J_per_m3", "component": "L2_E0_module", "type": VariableType.ALGEBRAIC},
    {"name": "v", "units": "m3_per_s", "component": "L2_E0_module", "type": VariableType.ALGEBRAIC},
    {"name": "v", "units": "m3_per_s", "component": "L2_E4_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "L2_E0_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_0", "units": "m3", "component": "L2_E1_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q", "units": "m3", "component": "L2_E1_module", "type": VariableType.ALGEBRAIC},
    {"name": "h", "units": "metre", "component": "L2_E1_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "C", "units": "m6_per_J", "component": "L2_E1_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R", "units": "Js_per_m6", "component": "L2_E1_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "L2_E1_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u", "units": "J_per_m3", "component": "L2_E1_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_d", "units": "J_per_m3", "component": "L2_E3_module", "type": VariableType.ALGEBRAIC},
    {"name": "v", "units": "m3_per_s", "component": "L2_E1_module", "type": VariableType.ALGEBRAIC},
    {"name": "v", "units": "m3_per_s", "component": "L2_E5_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "L2_E1_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_0", "units": "m3", "component": "L2_E2_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q", "units": "m3", "component": "L2_E2_module", "type": VariableType.ALGEBRAIC},
    {"name": "h", "units": "metre", "component": "L2_E2_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "C", "units": "m6_per_J", "component": "L2_E2_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R", "units": "Js_per_m6", "component": "L2_E2_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "L2_E2_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u", "units": "J_per_m3", "component": "L2_E2_module", "type": VariableType.ALGEBRAIC},
    {"name": "v", "units": "m3_per_s", "component": "L2_E2_module", "type": VariableType.ALGEBRAIC},
    {"name": "v_d", "units": "m3_per_s", "component": "L2_E2_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "L2_E2_module", "type": VariableType.ALGEBRAIC},
    {"name": "u", "units": "J_per_m3", "component": "L2_E7_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_0", "units": "m3", "component": "L2_E3_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q", "units": "m3", "component": "L2_E3_module", "type": VariableType.ALGEBRAIC},
    {"name": "h", "units": "metre", "component": "L2_E3_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "C", "units": "m6_per_J", "component": "L2_E3_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R", "units": "Js_per_m6", "component": "L2_E3_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "L2_E3_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "v", "units": "m3_per_s", "component": "L2_E3_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "L2_E3_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C_d", "units": "J_per_m3", "component": "L2_E3_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_0", "units": "m3", "component": "L2_E4_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q", "units": "m3", "component": "L2_E4_module", "type": VariableType.ALGEBRAIC},
    {"name": "h", "units": "metre", "component": "L2_E4_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "C", "units": "m6_per_J", "component": "L2_E4_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R", "units": "Js_per_m6", "component": "L2_E4_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "L2_E4_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u", "units": "J_per_m3", "component": "L2_E4_module", "type": VariableType.ALGEBRAIC},
    {"name": "v", "units": "m3_per_s", "component": "L2_E7_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "L2_E4_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_0", "units": "m3", "component": "L2_E5_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q", "units": "m3", "component": "L2_E5_module", "type": VariableType.ALGEBRAIC},
    {"name": "h", "units": "metre", "component": "L2_E5_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "C", "units": "m6_per_J", "component": "L2_E5_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R", "units": "Js_per_m6", "component": "L2_E5_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "L2_E5_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u", "units": "J_per_m3", "component": "L2_E5_module", "type": VariableType.ALGEBRAIC},
    {"name": "v_d", "units": "m3_per_s", "component": "L2_E5_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "L2_E5_module", "type": VariableType.ALGEBRAIC},
    {"name": "u", "units": "J_per_m3", "component": "L2_E6_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_0", "units": "m3", "component": "L2_E6_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q", "units": "m3", "component": "L2_E6_module", "type": VariableType.ALGEBRAIC},
    {"name": "h", "units": "metre", "component": "L2_E6_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "C", "units": "m6_per_J", "component": "L2_E6_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R", "units": "Js_per_m6", "component": "L2_E6_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "L2_E6_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "v", "units": "m3_per_s", "component": "L2_E6_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "L2_E6_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_0", "units": "m3", "component": "L2_E7_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q", "units": "m3", "component": "L2_E7_module", "type": VariableType.ALGEBRAIC},
    {"name": "h", "units": "metre", "component": "L2_E7_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "C", "units": "m6_per_J", "component": "L2_E7_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R", "units": "Js_per_m6", "component": "L2_E7_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "L2_E7_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_C", "units": "J_per_m3", "component": "L2_E7_module", "type": VariableType.ALGEBRAIC}
]


def create_states_array():
    return [nan]*STATE_COUNT


def create_variables_array():
    return [nan]*VARIABLE_COUNT


def initialise_variables(states, rates, variables):
    variables[0] = 195287.76505579543
    variables[1] = 7.7483e-06
    variables[2] = 2.7600000000000004e-07
    variables[3] = 7.716737277954605e-16
    variables[4] = 0.0
    variables[5] = 0.0
    variables[6] = 153712.68016968886
    variables[7] = 4.6814e-06
    variables[8] = 7.748e-07
    variables[9] = 7.970727979625374e-11
    variables[10] = 0.0
    variables[11] = 0.0
    variables[12] = 130372.26187279567
    variables[13] = 4.892e-07
    variables[14] = 1.3978999999999998e-06
    variables[15] = 5.832883627872877
    variables[16] = 0.0
    variables[17] = 0.0
    variables[18] = 129784.48751686089
    variables[19] = 7.7483e-06
    variables[20] = 2.7600000000000004e-07
    variables[21] = -9.42156972346806e-17
    variables[22] = 0.0
    variables[23] = 0.0
    variables[24] = 153443.41468611706
    variables[25] = 4.6814e-06
    variables[26] = 8.79e-07
    variables[27] = 4.607614660459828e-09
    variables[28] = 0.0
    variables[29] = 0.0
    variables[30] = 155729.31437934865
    variables[31] = 2.9824e-06
    variables[32] = 1.0062e-06
    variables[33] = 5.647791398748333e-06
    variables[34] = 0.0
    variables[35] = 0.0
    variables[36] = 182916.76933891617
    variables[37] = 4.892e-07
    variables[38] = 8.840999999999999e-07
    variables[39] = 0.09338926809753256
    variables[40] = 0.0
    variables[41] = 0.0
    variables[42] = 144301.91207081807
    variables[43] = 2.9824e-06
    variables[44] = 8.840999999999999e-07
    variables[45] = 0.00026125661199288244
    variables[46] = 0.0
    variables[47] = 0.0
    variables[48] = 6666.12
    variables[49] = 666.612
    variables[50] = 0.0
    variables[51] = 1040.0
    variables[52] = 0.004
    variables[53] = 9.81
    variables[54] = 0.2802
    variables[55] = -505.3
    variables[56] = 0.1324
    variables[57] = -11.14
    variables[63] = 0.0
    variables[74] = 0.0
    variables[85] = 0.0
    variables[96] = 0.0
    variables[105] = 0.0
    variables[114] = 0.0
    variables[124] = 0.0
    variables[132] = 0.0
    states[0] = 0.0
    states[1] = 0.0
    states[2] = 0.0
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 0.0
    states[6] = 0.0
    states[7] = 0.0
    states[8] = 0.0


def compute_computed_constants(variables):
    variables[58] = 3.14159265358979*pow(variables[2], 2.0)*variables[1]
    variables[60] = variables[2]*(variables[54]*exp(variables[55]*variables[2])+variables[56]*exp(variables[57]*variables[2]))
    variables[61] = 2.0*3.14159265358979*pow(variables[2], 3.0)*variables[1]/(variables[0]*variables[60])
    variables[62] = 8.0*variables[52]*variables[1]/(3.14159265358979*pow(variables[2], 4.0))
    variables[69] = 3.14159265358979*pow(variables[8], 2.0)*variables[7]
    variables[71] = variables[8]*(variables[54]*exp(variables[55]*variables[8])+variables[56]*exp(variables[57]*variables[8]))
    variables[72] = 2.0*3.14159265358979*pow(variables[8], 3.0)*variables[7]/(variables[6]*variables[71])
    variables[73] = 8.0*variables[52]*variables[7]/(3.14159265358979*pow(variables[8], 4.0))
    variables[80] = 3.14159265358979*pow(variables[14], 2.0)*variables[13]
    variables[82] = variables[14]*(variables[54]*exp(variables[55]*variables[14])+variables[56]*exp(variables[57]*variables[14]))
    variables[83] = 2.0*3.14159265358979*pow(variables[14], 3.0)*variables[13]/(variables[12]*variables[82])
    variables[84] = 8.0*variables[52]*variables[13]/(3.14159265358979*pow(variables[14], 4.0))
    variables[91] = 3.14159265358979*pow(variables[20], 2.0)*variables[19]
    variables[93] = variables[20]*(variables[54]*exp(variables[55]*variables[20])+variables[56]*exp(variables[57]*variables[20]))
    variables[94] = 2.0*3.14159265358979*pow(variables[20], 3.0)*variables[19]/(variables[18]*variables[93])
    variables[95] = 8.0*variables[52]*variables[19]/(3.14159265358979*pow(variables[20], 4.0))
    variables[100] = 3.14159265358979*pow(variables[26], 2.0)*variables[25]
    variables[102] = variables[26]*(variables[54]*exp(variables[55]*variables[26])+variables[56]*exp(variables[57]*variables[26]))
    variables[103] = 2.0*3.14159265358979*pow(variables[26], 3.0)*variables[25]/(variables[24]*variables[102])
    variables[104] = 8.0*variables[52]*variables[25]/(3.14159265358979*pow(variables[26], 4.0))
    variables[109] = 3.14159265358979*pow(variables[32], 2.0)*variables[31]
    variables[111] = variables[32]*(variables[54]*exp(variables[55]*variables[32])+variables[56]*exp(variables[57]*variables[32]))
    variables[112] = 2.0*3.14159265358979*pow(variables[32], 3.0)*variables[31]/(variables[30]*variables[111])
    variables[113] = 8.0*variables[52]*variables[31]/(3.14159265358979*pow(variables[32], 4.0))
    variables[119] = 3.14159265358979*pow(variables[38], 2.0)*variables[37]
    variables[121] = variables[38]*(variables[54]*exp(variables[55]*variables[38])+variables[56]*exp(variables[57]*variables[38]))
    variables[122] = 2.0*3.14159265358979*pow(variables[38], 3.0)*variables[37]/(variables[36]*variables[121])
    variables[123] = 8.0*variables[52]*variables[37]/(3.14159265358979*pow(variables[38], 4.0))
    variables[127] = 3.14159265358979*pow(variables[44], 2.0)*variables[43]
    variables[129] = variables[44]*(variables[54]*exp(variables[55]*variables[44])+variables[56]*exp(variables[57]*variables[44]))
    variables[130] = 2.0*3.14159265358979*pow(variables[44], 3.0)*variables[43]/(variables[42]*variables[129])
    variables[131] = 8.0*variables[52]*variables[43]/(3.14159265358979*pow(variables[44], 4.0))


def compute_rates(voi, states, rates, variables):
    variables[68] = states[0]/variables[61]
    variables[65] = variables[3]+variables[68]+variables[4]
    variables[98] = states[4]/(variables[94]/2.0)
    variables[64] = variables[21]+variables[98]+variables[23]+2.0
    variables[66] = (variables[65]-variables[64])/variables[62]
    variables[108] = states[5]/variables[103]
    variables[106] = variables[27]+variables[108]+variables[28]
    variables[67] = (variables[106]-variables[65])/variables[104]
    rates[0] = variables[67]-variables[66]
    variables[79] = states[1]/variables[72]
    variables[75] = variables[9]+variables[79]+variables[10]
    variables[117] = states[6]/variables[112]
    variables[115] = variables[33]+variables[117]+variables[34]
    variables[78] = (variables[75]-variables[115])/(variables[113]/2.0)
    variables[99] = states[3]/(variables[94]/2.0)
    variables[76] = variables[21]+variables[99]+variables[23]+2.0
    variables[77] = (variables[76]-variables[75])/variables[73]
    rates[1] = variables[77]-variables[78]
    variables[89] = states[2]/variables[83]
    variables[86] = variables[15]+variables[89]+variables[16]
    variables[87] = (variables[48]-variables[86])/(variables[84]/2.0)
    variables[133] = states[8]/variables[130]
    variables[90] = variables[45]+variables[133]+variables[46]
    variables[88] = (variables[86]-variables[90])/(variables[84]/2.0)
    rates[2] = variables[87]-variables[88]
    variables[97] = (variables[64]-variables[76])/variables[95]
    rates[4] = variables[66]-variables[97]
    rates[3] = variables[97]-variables[77]
    variables[107] = (variables[90]-variables[106])/variables[131]
    rates[5] = variables[107]-variables[67]
    variables[126] = states[7]/variables[122]
    variables[118] = variables[39]+variables[126]+variables[40]
    variables[116] = (variables[115]-variables[118])/(variables[113]/2.0)
    rates[6] = variables[78]-variables[116]
    variables[125] = (variables[118]-variables[49])/variables[123]
    rates[7] = variables[116]-variables[125]
    rates[8] = variables[88]-variables[107]


def compute_variables(voi, states, rates, variables):
    variables[59] = states[0]+variables[58]
    variables[68] = states[0]/variables[61]
    variables[65] = variables[3]+variables[68]+variables[4]
    variables[98] = states[4]/(variables[94]/2.0)
    variables[64] = variables[21]+variables[98]+variables[23]+2.0
    variables[66] = (variables[65]-variables[64])/variables[62]
    variables[70] = states[1]+variables[69]
    variables[79] = states[1]/variables[72]
    variables[75] = variables[9]+variables[79]+variables[10]
    variables[99] = states[3]/(variables[94]/2.0)
    variables[76] = variables[21]+variables[99]+variables[23]+2.0
    variables[77] = (variables[76]-variables[75])/variables[73]
    variables[81] = states[2]+variables[80]
    variables[89] = states[2]/variables[83]
    variables[86] = variables[15]+variables[89]+variables[16]
    variables[87] = (variables[48]-variables[86])/(variables[84]/2.0)
    variables[133] = states[8]/variables[130]
    variables[90] = variables[45]+variables[133]+variables[46]
    variables[88] = (variables[86]-variables[90])/(variables[84]/2.0)
    variables[92] = states[4]+states[3]+variables[91]
    variables[97] = (variables[64]-variables[76])/variables[95]
    variables[101] = states[5]+variables[100]
    variables[108] = states[5]/variables[103]
    variables[106] = variables[27]+variables[108]+variables[28]
    variables[67] = (variables[106]-variables[65])/variables[104]
    variables[110] = states[6]+variables[109]
    variables[117] = states[6]/variables[112]
    variables[115] = variables[33]+variables[117]+variables[34]
    variables[78] = (variables[75]-variables[115])/(variables[113]/2.0)
    variables[126] = states[7]/variables[122]
    variables[118] = variables[39]+variables[126]+variables[40]
    variables[116] = (variables[115]-variables[118])/(variables[113]/2.0)
    variables[120] = states[7]+variables[119]
    variables[125] = (variables[118]-variables[49])/variables[123]
    variables[128] = states[8]+variables[127]
    variables[107] = (variables[90]-variables[106])/variables[131]

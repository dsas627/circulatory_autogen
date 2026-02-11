# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.4.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 27
VARIABLE_COUNT = 143


class VariableType(Enum):
    VARIABLE_OF_INTEGRATION = 0
    STATE = 1
    CONSTANT = 2
    COMPUTED_CONSTANT = 3
    ALGEBRAIC = 4


VOI_INFO = {"name": "time", "units": "second", "component": "environment", "type": VariableType.VARIABLE_OF_INTEGRATION}

STATE_INFO = [
    {"name": "v", "units": "m3_per_s", "component": "pvn_module", "type": VariableType.STATE},
    {"name": "v", "units": "m3_per_s", "component": "par_module", "type": VariableType.STATE},
    {"name": "q_C_change", "units": "m3", "component": "pvn_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "par_module", "type": VariableType.STATE},
    {"name": "v_puv", "units": "m3_per_s", "component": "heart_module", "type": VariableType.STATE},
    {"name": "chi_a", "units": "dimensionless", "component": "heart_module", "type": VariableType.STATE},
    {"name": "chi_v", "units": "dimensionless", "component": "heart_module", "type": VariableType.STATE},
    {"name": "s", "units": "dimensionless", "component": "heart_module", "type": VariableType.STATE},
    {"name": "zeta_trv_pre", "units": "dimensionless", "component": "heart_module", "type": VariableType.STATE},
    {"name": "zeta_puv_pre", "units": "dimensionless", "component": "heart_module", "type": VariableType.STATE},
    {"name": "zeta_miv_pre", "units": "dimensionless", "component": "heart_module", "type": VariableType.STATE},
    {"name": "zeta_aov_pre", "units": "dimensionless", "component": "heart_module", "type": VariableType.STATE},
    {"name": "v_trv", "units": "m3_per_s", "component": "heart_module", "type": VariableType.STATE},
    {"name": "v_miv", "units": "m3_per_s", "component": "heart_module", "type": VariableType.STATE},
    {"name": "v_aov", "units": "m3_per_s", "component": "heart_module", "type": VariableType.STATE},
    {"name": "q_ra", "units": "m3", "component": "heart_module", "type": VariableType.STATE},
    {"name": "q_rv", "units": "m3", "component": "heart_module", "type": VariableType.STATE},
    {"name": "q_la", "units": "m3", "component": "heart_module", "type": VariableType.STATE},
    {"name": "q_lv", "units": "m3", "component": "heart_module", "type": VariableType.STATE},
    {"name": "v", "units": "m3_per_s", "component": "venous_svc_module", "type": VariableType.STATE},
    {"name": "q_C_d", "units": "m3", "component": "aortic_root_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "aortic_root_module", "type": VariableType.STATE},
    {"name": "v", "units": "m3_per_s", "component": "aortic_root_module", "type": VariableType.STATE},
    {"name": "v", "units": "m3_per_s", "component": "systemic_T_module", "type": VariableType.STATE},
    {"name": "v_T", "units": "m3_per_s", "component": "systemic_T_module", "type": VariableType.STATE},
    {"name": "q", "units": "m3", "component": "systemic_T_module", "type": VariableType.STATE},
    {"name": "q_C_change", "units": "m3", "component": "venous_svc_module", "type": VariableType.STATE}
]

VARIABLE_INFO = [
    {"name": "R_pvn", "units": "Js_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "C_pvn", "units": "m6_per_J", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_pvn", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "I_pvn", "units": "Js2_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "q_C_init_pvn", "units": "m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "q_us_0_pvn", "units": "m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "Delta_q_us_pvn", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "Delta_C_pvn", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "q_0_par", "units": "m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "R_par", "units": "Js_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "C_par", "units": "m6_per_J", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "I_par", "units": "Js2_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_par", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_par", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "q_0_aortic_root", "units": "m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "R_aortic_root", "units": "Js_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "C_aortic_root", "units": "m6_per_J", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_aortic_root", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "I_aortic_root", "units": "Js2_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_0_aortic_root", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "R_T_systemic_T", "units": "Js_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "C_T_systemic_T", "units": "m6_per_J", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_systemic_T", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "q_us_systemic_T", "units": "m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "q_init_systemic_T", "units": "m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "R_venous_svc", "units": "Js_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "C_venous_svc", "units": "m6_per_J", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_venous_svc", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "I_venous_svc", "units": "Js2_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "q_C_init_venous_svc", "units": "m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "q_us_0_venous_svc", "units": "m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "Delta_q_us_venous_svc", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "Delta_C_venous_svc", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "rho", "units": "kg_per_m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "T", "units": "second", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_ra_us", "units": "m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_rv_us", "units": "m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_la_us", "units": "m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_lv_us", "units": "m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_ra_init", "units": "m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_rv_init", "units": "m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_la_init", "units": "m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "q_lv_init", "units": "m3", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "T_ac", "units": "second", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "T_ar", "units": "second", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "t_astart", "units": "second", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "T_vc", "units": "second", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "T_vr", "units": "second", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "t_vstart", "units": "second", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "E_ra_A", "units": "J_per_m6", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "E_ra_B", "units": "J_per_m6", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "E_rv_A", "units": "J_per_m6", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "E_rv_B", "units": "J_per_m6", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "E_la_A", "units": "J_per_m6", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "E_la_B", "units": "J_per_m6", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "E_lv_A", "units": "J_per_m6", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "E_lv_B", "units": "J_per_m6", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "K_vo_trv", "units": "m3_per_Js", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "K_vo_puv", "units": "m3_per_Js", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "K_vo_miv", "units": "m3_per_Js", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "K_vo_aov", "units": "m3_per_Js", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "K_vc_trv", "units": "m3_per_Js", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "K_vc_puv", "units": "m3_per_Js", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "K_vc_miv", "units": "m3_per_Js", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "K_vc_aov", "units": "m3_per_Js", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "M_rg_trv", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "M_rg_puv", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "M_rg_miv", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "M_rg_aov", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "M_st_trv", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "M_st_puv", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "M_st_miv", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "M_st_aov", "units": "dimensionless", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "l_eff", "units": "metre", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "A_nn_trv", "units": "m2", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "A_nn_puv", "units": "m2", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "A_nn_miv", "units": "m2", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "A_nn_aov", "units": "m2", "component": "parameters_global", "type": VariableType.CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "pvn_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_la", "units": "J_per_m3", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "u", "units": "J_per_m3", "component": "pvn_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_us_wCont", "units": "m3", "component": "pvn_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q_C", "units": "m3", "component": "pvn_module", "type": VariableType.ALGEBRAIC},
    {"name": "q", "units": "m3", "component": "pvn_module", "type": VariableType.ALGEBRAIC},
    {"name": "C_wCont", "units": "m6_per_J", "component": "pvn_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_C", "units": "J_per_m3", "component": "pvn_module", "type": VariableType.ALGEBRAIC},
    {"name": "q", "units": "m3", "component": "par_module", "type": VariableType.ALGEBRAIC},
    {"name": "R_v", "units": "Js_per_m6", "component": "par_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u", "units": "J_per_m3", "component": "par_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "par_module", "type": VariableType.ALGEBRAIC},
    {"name": "chi_afloor", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "eps_1", "units": "dimensionless", "component": "heart_module", "type": VariableType.CONSTANT},
    {"name": "t_astart_norm", "units": "dimensionless", "component": "heart_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "mt", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "eps_2", "units": "dimensionless", "component": "heart_module", "type": VariableType.CONSTANT},
    {"name": "chi_afloor_final", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "chi_vfloor", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "t_vstart_norm", "units": "dimensionless", "component": "heart_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "chi_vfloor_final", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "e_a", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "e_v", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "eps_m4", "units": "m4", "component": "heart_module", "type": VariableType.CONSTANT},
    {"name": "A_eff_trv", "units": "m2", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "B_trv", "units": "Js2_per_m9", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "A_eff_puv", "units": "m2", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "B_puv", "units": "Js2_per_m9", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "A_eff_miv", "units": "m2", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "B_miv", "units": "Js2_per_m9", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "A_eff_aov", "units": "m2", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "B_aov", "units": "Js2_per_m9", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "eps_m2", "units": "m2", "component": "heart_module", "type": VariableType.CONSTANT},
    {"name": "L_trv", "units": "Js2_per_m6", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "L_puv", "units": "Js2_per_m6", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "L_miv", "units": "Js2_per_m6", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "L_aov", "units": "Js2_per_m6", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "zeta_trv", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "zeta_puv", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "zeta_miv", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "zeta_aov", "units": "dimensionless", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_rv", "units": "J_per_m3", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_ra", "units": "J_per_m3", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_lv", "units": "J_per_m3", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "u", "units": "J_per_m3", "component": "aortic_root_module", "type": VariableType.ALGEBRAIC},
    {"name": "v_zero", "units": "m3_per_s", "component": "zero_flow_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q_heart", "units": "m3", "component": "heart_module", "type": VariableType.ALGEBRAIC},
    {"name": "q", "units": "m3", "component": "aortic_root_module", "type": VariableType.ALGEBRAIC},
    {"name": "R_v", "units": "Js_per_m6", "component": "aortic_root_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_d", "units": "J_per_m3", "component": "aortic_root_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "aortic_root_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C_d", "units": "J_per_m3", "component": "aortic_root_module", "type": VariableType.ALGEBRAIC},
    {"name": "R_v", "units": "Js_per_m6", "component": "systemic_T_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "I_T", "units": "Js2_per_m6", "component": "systemic_T_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_C", "units": "J_per_m3", "component": "systemic_T_module", "type": VariableType.ALGEBRAIC},
    {"name": "u", "units": "J_per_m3", "component": "systemic_T_module", "type": VariableType.ALGEBRAIC},
    {"name": "u", "units": "J_per_m3", "component": "venous_svc_module", "type": VariableType.ALGEBRAIC},
    {"name": "R_v", "units": "Js_per_m6", "component": "venous_svc_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "v_venous_svc", "units": "m3_per_s", "component": "terminal_venous_connection", "type": VariableType.ALGEBRAIC},
    {"name": "q_us_wCont", "units": "m3", "component": "venous_svc_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "q_C", "units": "m3", "component": "venous_svc_module", "type": VariableType.ALGEBRAIC},
    {"name": "q", "units": "m3", "component": "venous_svc_module", "type": VariableType.ALGEBRAIC},
    {"name": "C_wCont", "units": "m6_per_J", "component": "venous_svc_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_C", "units": "J_per_m3", "component": "venous_svc_module", "type": VariableType.ALGEBRAIC},
    {"name": "q_volume_sum_sum", "units": "m3", "component": "sum_blood_volume", "type": VariableType.ALGEBRAIC}
]


def lt_func(x, y):
    return 1.0 if x < y else 0.0


def leq_func(x, y):
    return 1.0 if x <= y else 0.0


def gt_func(x, y):
    return 1.0 if x > y else 0.0


def geq_func(x, y):
    return 1.0 if x >= y else 0.0


def and_func(x, y):
    return 1.0 if bool(x) & bool(y) else 0.0


def max(x, y):
    return x if x > y else y


def create_states_array():
    return [nan]*STATE_COUNT


def create_variables_array():
    return [nan]*VARIABLE_COUNT


def initialise_variables(states, rates, variables):
    variables[0] = 1333000.0
    variables[1] = 0.0000000060015
    variables[2] = 0.0
    variables[3] = 0.000001
    variables[4] = 0.0001
    variables[5] = 0.0
    variables[6] = 0.0
    variables[7] = 0.0
    variables[8] = 0.0
    variables[9] = 10664000.0
    variables[10] = 3.09077e-10
    variables[11] = 0.000001
    variables[12] = 0.0
    variables[13] = 1463.0
    variables[14] = 6.94e-06
    variables[15] = 1000000.0
    variables[16] = 0.000000012028
    variables[17] = 0.0
    variables[18] = 10000.0
    variables[19] = 13300.0
    variables[20] = 110000000.0
    variables[21] = 0.0000001
    variables[22] = 0.0
    variables[23] = 0.00245
    variables[24] = 0.00245
    variables[25] = 1114600.0
    variables[26] = 0.000001
    variables[27] = 0.0
    variables[28] = 0.01
    variables[29] = 0.0013
    variables[30] = 0.0
    variables[31] = 0.0
    variables[32] = 0.0
    variables[33] = 1050.0
    variables[34] = 1.0
    variables[35] = 0.000004
    variables[36] = 0.00001
    variables[37] = 0.000004
    variables[38] = 0.000005
    variables[39] = 0.000004
    variables[40] = 0.00001
    variables[41] = 0.000004
    variables[42] = 0.002
    variables[43] = 0.17
    variables[44] = 0.17
    variables[45] = 0.8
    variables[46] = 0.30
    variables[47] = 0.15
    variables[48] = 0.0
    variables[49] = 7998000.0
    variables[50] = 9331000.0
    variables[51] = 73315000.0
    variables[52] = 6665000.0
    variables[53] = 9331000.0
    variables[54] = 11997000.0
    variables[55] = 366575000.0
    variables[56] = 10664000.0
    variables[57] = 0.3
    variables[58] = 0.2
    variables[59] = 0.3
    variables[60] = 0.04
    variables[61] = 0.4
    variables[62] = 0.2
    variables[63] = 0.4
    variables[64] = 0.04
    variables[65] = 0.0
    variables[66] = 0.0
    variables[67] = 0.0
    variables[68] = 0.0
    variables[69] = 1.0
    variables[70] = 1.0
    variables[71] = 1.0
    variables[72] = 1.0
    variables[73] = 0.01
    variables[74] = 0.0009
    variables[75] = 0.0004
    variables[76] = 0.0006
    variables[77] = 0.000314
    variables[91] = 0.07
    variables[94] = 0.02
    variables[101] = 1.0e-14
    variables[110] = 1.0e-14
    variables[131] = 1.0e-6
    variables[123] = 0.0
    states[0] = 0.0
    states[1] = 0.0
    states[2] = variables[4]
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 0.0
    states[6] = 0.0
    states[7] = 0.0
    states[8] = 0.0
    states[9] = 0.0
    states[10] = 0.0
    states[11] = 0.0
    states[12] = 0.0
    states[13] = 0.0
    states[14] = 0.0
    states[15] = variables[39]
    states[16] = variables[40]
    states[17] = variables[41]
    states[18] = variables[42]
    states[19] = 0.0
    states[20] = 0.0
    states[21] = 0.0
    states[22] = 0.0
    states[23] = 0.0
    states[24] = 0.0
    states[25] = variables[24]
    states[26] = variables[29]


def compute_computed_constants(variables):
    variables[78] = 0.01/variables[1]
    variables[81] = variables[5]*(1.0-variables[6])
    variables[84] = variables[1]*(1.0-variables[7])
    variables[87] = 0.01/variables[10]
    variables[92] = variables[45]/variables[34]
    variables[97] = variables[48]/variables[34]
    variables[126] = 0.01/variables[16]
    variables[130] = 0.01/variables[21]
    variables[135] = 0.01/variables[26]
    variables[137] = variables[30]*(1.0-variables[31])
    variables[140] = variables[26]*(1.0-variables[32])


def compute_rates(voi, states, rates, variables):
    variables[82] = states[2]+variables[5]-variables[81]
    variables[85] = variables[82]/variables[84]
    variables[80] = variables[85]+variables[2]+variables[78]*(states[1]-states[0])
    variables[90] = states[5]-floor(states[5])
    variables[95] = variables[90]*2.0 if leq_func(variables[90], 0.5) else 0.0
    variables[99] = 0.5*(1.0-cos(2.0*3.14159265358979*variables[95]))
    variables[79] = (variables[99]*variables[53]+variables[54])*(states[17]-variables[37])
    rates[0] = (variables[80]-variables[79]-variables[0]*states[0])/variables[3]
    rates[2] = states[1]-states[0]
    variables[89] = states[3]/variables[10]
    variables[88] = variables[13]+variables[89]+variables[12]+variables[87]*(states[4]-states[1])
    rates[1] = (variables[88]-variables[80]-variables[9]*states[1])/variables[11]
    rates[3] = states[4]-states[1]
    variables[93] = states[7]-floor(states[7])
    rates[5] = 0.25/variables[43] if and_func(geq_func(variables[93], variables[92]), and_func(leq_func(variables[93], variables[92]+variables[91]), leq_func(variables[90], 0.25))) else 0.25/variables[43] if and_func(gt_func(variables[92]+variables[91], 1.0), and_func(leq_func(variables[93], variables[92]+variables[91]-1.0), leq_func(variables[90], 0.25))) else 0.25/variables[43] if and_func(gt_func(variables[90], variables[94]), leq_func(variables[90], 0.25)) else 0.25/variables[44] if and_func(geq_func(variables[90], 0.25), lt_func(variables[90], 0.5)) else 0.5/(variables[34]-variables[43]-variables[44]) if geq_func(variables[90], 0.5) else 0.0
    variables[96] = states[6]-floor(states[6])
    rates[6] = 0.25/variables[46] if and_func(geq_func(variables[93], variables[97]), and_func(leq_func(variables[93], variables[97]+variables[91]), leq_func(variables[96], 0.25))) else 0.25/variables[46] if and_func(gt_func(variables[97]+variables[91], 1.0), and_func(leq_func(variables[93], variables[97]+variables[91]-1.0), leq_func(variables[96], 0.25))) else 0.25/variables[46] if and_func(gt_func(variables[96], variables[94]), leq_func(variables[96], 0.25)) else 0.25/variables[47] if and_func(gt_func(variables[96], 0.25), lt_func(variables[96], 0.5)) else 0.5/(variables[34]-variables[46]-variables[47]) if gt_func(variables[96], 0.5) else 0.0
    rates[7] = 1.0/variables[34]
    variables[98] = variables[96]*2.0 if leq_func(variables[96], 0.5) else 0.0
    variables[100] = 0.5*(1.0-cos(2.0*3.14159265358979*variables[98]))
    variables[119] = (variables[100]*variables[51]+variables[52])*(states[16]-variables[36])
    variables[120] = (variables[99]*variables[49]+variables[50])*(states[15]-variables[35])
    rates[8] = (1.0-states[8])*variables[57]*(variables[120]-variables[119]) if geq_func(variables[120], variables[119]) else states[8]*variables[61]*(variables[120]-variables[119])
    rates[9] = (1.0-states[9])*variables[58]*(variables[119]-variables[88]) if geq_func(variables[119], variables[88]) else states[9]*variables[62]*(variables[119]-variables[88])
    variables[121] = (variables[100]*variables[55]+variables[56])*(states[18]-variables[38])
    rates[10] = (1.0-states[10])*variables[59]*(variables[79]-variables[121]) if geq_func(variables[79], variables[121]) else states[10]*variables[63]*(variables[79]-variables[121])
    variables[128] = states[21]/(variables[16]/2.0)
    variables[122] = variables[19]+variables[128]+variables[17]+2.0*variables[126]*(states[14]-states[22])
    rates[11] = (1.0-states[11])*variables[60]*(variables[121]-variables[122]) if geq_func(variables[121], variables[122]) else states[11]*variables[64]*(variables[121]-variables[122])
    variables[115] = max(states[8], 0.0)
    variables[102] = (variables[69]*variables[74]-variables[65]*variables[74])*variables[115]+variables[65]*variables[74]
    variables[111] = variables[33]*variables[73]/(variables[102]+variables[110])
    variables[103] = variables[33]/(2.0*pow(variables[102], 2.0)+variables[101])
    rates[12] = (-variables[103]*states[12]*fabs(states[12])+variables[120]-variables[119])/variables[111]
    variables[116] = max(states[9], 0.0)
    variables[104] = (variables[70]*variables[75]-variables[66]*variables[75])*variables[116]+variables[66]*variables[75]
    variables[112] = variables[33]*variables[73]/(variables[104]+variables[110])
    variables[105] = variables[33]/(2.0*pow(variables[104], 2.0)+variables[101])
    rates[4] = (-variables[105]*states[4]*fabs(states[4])+variables[119]-variables[88])/variables[112]
    variables[117] = max(states[10], 0.0)
    variables[106] = (variables[71]*variables[76]-variables[67]*variables[76])*variables[117]+variables[67]*variables[76]
    variables[113] = variables[33]*variables[73]/(variables[106]+variables[110])
    variables[107] = variables[33]/(2.0*pow(variables[106], 2.0)+variables[101])
    rates[13] = (-variables[107]*states[13]*fabs(states[13])+variables[79]-variables[121])/variables[113]
    variables[118] = max(states[11], 0.0)
    variables[108] = (variables[72]*variables[77]-variables[68]*variables[77])*variables[118]+variables[68]*variables[77]
    variables[114] = variables[33]*variables[73]/(variables[108]+variables[110])
    variables[109] = variables[33]/(2.0*pow(variables[108], 2.0)+variables[101])
    rates[14] = (-variables[109]*states[14]*fabs(states[14])+variables[121]-variables[122])/variables[114]
    rates[15] = states[19]+variables[123]-states[12]
    rates[16] = states[12]-states[4]
    rates[17] = states[0]-states[13]
    rates[18] = states[13]-states[14]
    variables[129] = states[20]/(variables[16]/2.0)
    variables[127] = variables[19]+variables[129]+variables[17]+2.0*variables[126]*(states[22]-states[23])
    rates[22] = (variables[122]-variables[127]-variables[15]*states[22])/variables[18]
    rates[21] = states[14]-states[22]
    rates[20] = states[22]-states[23]
    rates[25] = states[23]-states[24]
    variables[132] = (states[25]-variables[23])/variables[21]
    variables[133] = variables[132]+variables[22]+variables[130]*(states[23]-states[24])
    rates[23] = (variables[127]-variables[133]-states[23]*variables[20]/2.0)/variables[131]
    variables[138] = states[26]+variables[30]-variables[137]
    variables[141] = variables[138]/variables[140]
    variables[136] = states[24]
    variables[134] = variables[141]+variables[27]+variables[135]*(variables[136]-states[19])
    rates[24] = (variables[133]-variables[134]-states[24]*variables[20]/2.0)/variables[131]
    rates[19] = (variables[134]-variables[120]-variables[25]*states[19])/variables[28]
    rates[26] = variables[136]-states[19]


def compute_variables(voi, states, rates, variables):
    variables[82] = states[2]+variables[5]-variables[81]
    variables[83] = variables[82]+variables[81]
    variables[85] = variables[82]/variables[84]
    variables[80] = variables[85]+variables[2]+variables[78]*(states[1]-states[0])
    variables[86] = states[3]+variables[8]
    variables[89] = states[3]/variables[10]
    variables[88] = variables[13]+variables[89]+variables[12]+variables[87]*(states[4]-states[1])
    variables[90] = states[5]-floor(states[5])
    variables[95] = variables[90]*2.0 if leq_func(variables[90], 0.5) else 0.0
    variables[96] = states[6]-floor(states[6])
    variables[98] = variables[96]*2.0 if leq_func(variables[96], 0.5) else 0.0
    variables[93] = states[7]-floor(states[7])
    variables[99] = 0.5*(1.0-cos(2.0*3.14159265358979*variables[95]))
    variables[100] = 0.5*(1.0-cos(2.0*3.14159265358979*variables[98]))
    variables[115] = max(states[8], 0.0)
    variables[102] = (variables[69]*variables[74]-variables[65]*variables[74])*variables[115]+variables[65]*variables[74]
    variables[103] = variables[33]/(2.0*pow(variables[102], 2.0)+variables[101])
    variables[116] = max(states[9], 0.0)
    variables[104] = (variables[70]*variables[75]-variables[66]*variables[75])*variables[116]+variables[66]*variables[75]
    variables[105] = variables[33]/(2.0*pow(variables[104], 2.0)+variables[101])
    variables[117] = max(states[10], 0.0)
    variables[106] = (variables[71]*variables[76]-variables[67]*variables[76])*variables[117]+variables[67]*variables[76]
    variables[107] = variables[33]/(2.0*pow(variables[106], 2.0)+variables[101])
    variables[118] = max(states[11], 0.0)
    variables[108] = (variables[72]*variables[77]-variables[68]*variables[77])*variables[118]+variables[68]*variables[77]
    variables[109] = variables[33]/(2.0*pow(variables[108], 2.0)+variables[101])
    variables[111] = variables[33]*variables[73]/(variables[102]+variables[110])
    variables[112] = variables[33]*variables[73]/(variables[104]+variables[110])
    variables[113] = variables[33]*variables[73]/(variables[106]+variables[110])
    variables[114] = variables[33]*variables[73]/(variables[108]+variables[110])
    variables[120] = (variables[99]*variables[49]+variables[50])*(states[15]-variables[35])
    variables[119] = (variables[100]*variables[51]+variables[52])*(states[16]-variables[36])
    variables[79] = (variables[99]*variables[53]+variables[54])*(states[17]-variables[37])
    variables[121] = (variables[100]*variables[55]+variables[56])*(states[18]-variables[38])
    variables[124] = states[15]+states[16]+states[17]+states[18]
    variables[125] = states[21]+states[20]+variables[14]
    variables[128] = states[21]/(variables[16]/2.0)
    variables[129] = states[20]/(variables[16]/2.0)
    variables[122] = variables[19]+variables[128]+variables[17]+2.0*variables[126]*(states[14]-states[22])
    variables[127] = variables[19]+variables[129]+variables[17]+2.0*variables[126]*(states[22]-states[23])
    variables[132] = (states[25]-variables[23])/variables[21]
    variables[133] = variables[132]+variables[22]+variables[130]*(states[23]-states[24])
    variables[138] = states[26]+variables[30]-variables[137]
    variables[139] = variables[138]+variables[137]
    variables[141] = variables[138]/variables[140]
    variables[136] = states[24]
    variables[134] = variables[141]+variables[27]+variables[135]*(variables[136]-states[19])
    variables[142] = variables[83]+variables[86]+variables[124]+variables[125]+states[25]+variables[139]

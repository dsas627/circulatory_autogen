# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.4.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 1
VARIABLE_COUNT = 15


class VariableType(Enum):
    VARIABLE_OF_INTEGRATION = 0
    STATE = 1
    CONSTANT = 2
    COMPUTED_CONSTANT = 3
    ALGEBRAIC = 4


VOI_INFO = {"name": "time", "units": "second", "component": "environment", "type": VariableType.VARIABLE_OF_INTEGRATION}

STATE_INFO = [
    {"name": "e_int", "units": "second", "component": "pid_control_module", "type": VariableType.STATE}
]

VARIABLE_INFO = [
    {"name": "P_target_pid_control", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "P_scale_pid_control", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "K_p_pid_control", "units": "Hz", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "K_i_pid_control", "units": "per_s2", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "K_d_pid_control", "units": "dimensionless", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "f_stim_min_pid_control", "units": "Hz", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "f_stim_max_pid_control", "units": "Hz", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "f_stim_HF_pid_control", "units": "Hz", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "e_int_init_pid_control", "units": "second", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "P_a_pid_control", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "dP_a_dt_pid_control", "units": "J_per_m3s", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "e_norm", "units": "dimensionless", "component": "pid_control_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "d_e_dt", "units": "Hz", "component": "pid_control_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "f_stim_raw", "units": "Hz", "component": "pid_control_module", "type": VariableType.ALGEBRAIC},
    {"name": "f_stim", "units": "Hz", "component": "pid_control_module", "type": VariableType.ALGEBRAIC}
]


def lt_func(x, y):
    return 1.0 if x < y else 0.0


def gt_func(x, y):
    return 1.0 if x > y else 0.0


def create_states_array():
    return [nan]*STATE_COUNT


def create_variables_array():
    return [nan]*VARIABLE_COUNT


def initialise_variables(states, rates, variables):
    variables[0] = 12000.0
    variables[1] = 4000.0
    variables[2] = 0.1
    variables[3] = 0.01
    variables[4] = 0.02
    variables[5] = 0.0
    variables[6] = 30.0
    variables[7] = 20000.0
    variables[8] = 0.0
    variables[9] = 12000.0
    variables[10] = 0.0
    states[0] = variables[8]


def compute_computed_constants(variables):
    variables[11] = (variables[0]-variables[9])/variables[1]
    variables[12] = (0.0-variables[10])/variables[1]


def compute_rates(voi, states, rates, variables):
    rates[0] = variables[11]


def compute_variables(voi, states, rates, variables):
    variables[13] = variables[2]*variables[11]+variables[3]*states[0]+variables[4]*variables[12]
    variables[14] = variables[7] if lt_func(variables[13], variables[5]) else variables[6] if gt_func(variables[13], variables[6]) else variables[13]

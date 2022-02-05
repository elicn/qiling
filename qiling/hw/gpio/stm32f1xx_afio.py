#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import ctypes

from qiling.hw.peripheral import QlPeripheral


class STM32F1xxAfio(QlPeripheral):
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("EVCR"     , ctypes.c_uint32),    
            ("MAPR"     , ctypes.c_uint32),    
            ("EXTICR"   , ctypes.c_uint32 * 4),
            ("RESERVED0", ctypes.c_uint32),    
            ("MAPR2"    , ctypes.c_uint32),    
        ]

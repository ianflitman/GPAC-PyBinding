from ctypes import *


class GF_SystemRTInfo(Structure):
	_fields_=[
		("sampling_instant", c_int),
		("sampling_period_duration", c_int),
		("total_cpu_time", c_int),
		("process_cpu_time", c_int),
		("total_cpu_time_diff", c_int),
		("process_cpu_time_diff", c_int),
		("cpu_idle_time", c_int),
		("total_cpu_usage", c_int),
		("process_cpu_usage", c_int),
		("pid", c_int),
		("thread_count", c_int),
		("process_memory", c_uint64),
		("physical_memory", c_uint64),
		("physical_memory_avail", c_uint64),
		("gpac_memory", c_uint64)
	]
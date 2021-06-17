from distutils.core import Extension, setup

extension_mod = Extension("mod_yj49750w464a_yj49750w464a",
		[ r'mod_yj49750w464a_yj49750w464a_wrapper.c' ],
		extra_objects = [r'/home/um6p/HPC/TPs/Distributed-Computing-HPC-Assignments/notebooks/Numba_Pyccel/__epyccel__/__pyccel__/bind_c_mod_yj49750w464a_yj49750w464a.o',
				r'/home/um6p/HPC/TPs/Distributed-Computing-HPC-Assignments/notebooks/Numba_Pyccel/__epyccel__/__pyccel__/mod_yj49750w464a_yj49750w464a.o'],
		include_dirs = [r'/home/um6p/HPC/TPs/Distributed-Computing-HPC-Assignments/notebooks/Numba_Pyccel/__epyccel__/__pyccel__',
				r'/home/um6p/anaconda3/lib/python3.7/site-packages/numpy/core/include'],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_compile_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/um6p/HPC/TPs/Distributed-Computing-HPC-Assignments/notebooks/Numba_Pyccel/__epyccel__/__pyccel__"'],
		extra_link_args = [])

setup(name = "mod_yj49750w464a_yj49750w464a", ext_modules=[extension_mod])
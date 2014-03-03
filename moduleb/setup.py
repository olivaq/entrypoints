from distutils.core import setup
setup(name='test_module_b',
      version="1",
      packages = ['moduleb'],
      entry_points = {'probe_device':['myprobe = moduleb:probe_b']}
      )

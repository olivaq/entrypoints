from distutils.core import setup
setup(name='test_module_a',
      version="1",
      packages = ['modulea'],
      entry_points = {'probe_device':['my_probe = modulea:probe_a']}
      )

import pkg_resources

res = []
for k in pkg_resources.iter_entry_points(group='probe_device'):
    res.append(k.load())

print res
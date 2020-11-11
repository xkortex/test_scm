__version__ = "unset"
# try:
#     from importlib.metadata import version, PackageNotFoundError
#     __version__ = version('test_scm')
#     print('importlib')
# except NameError as exc:
#     print('{}: {}'.format(exc.__class__.__name__, exc))
# except (PackageNotFoundError, NameError) as exc:
#     # package is not installed
#     print('{}: {}'.format(exc.__class__.__name__, exc))
#     pass

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
    print('pkg_resources')
except (DistributionNotFound, NameError) as exc:
    # package is not installed
    print('{}: {}'.format(exc.__class__.__name__, exc))
    pass




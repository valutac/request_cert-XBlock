import pkg_resources

from xblock.core import XBlock


def resource_string(self, path):
    """
    Gets the content of a resource
    """
    data = pkg_resources.resource_string(__name__, path)
    return data.decode('utf8')

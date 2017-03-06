import re

########################################
# GlslType #############################
########################################

class GlslType:
  """GLSL type identifier."""

  def __init__(self, source):
    """Constructor."""
    self.__type = source.lower()

  def format(self):
    """Return formatted output."""
    return self.__type

  def __str__(self):
    """String representation."""
    return "GlslType('%s')" % (self.__type)

########################################
# Functions ############################
########################################

def interpret_type(source):
  """Try to interpret type identifier."""
  if re.match(r'^(float|int|ivec\d|vec\d|void)$', source, re.I):
    return GlslType(source)
  return None

def is_glsl_type(op):
  """Tell if token is type identifier."""
  return isinstance(op, GlslType)
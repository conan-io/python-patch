from __future__ import print_function

import re
import tempfile
import codecs

# cStringIO doesn't support unicode in 2.5
try:
  from StringIO import StringIO
except ImportError:
  from io import BytesIO as StringIO # python 3
try:
  import urllib2 as urllib_request
except ImportError:
  import urllib.request as urllib_request

from os.path import exists, isfile, abspath
import sys


PY3K = sys.version_info >= (3, 0)

# PEP 3114
if not PY3K:
  compat_next = lambda gen: gen.next()
else:
  compat_next = lambda gen: gen.__next__()

def tostr(b):
  """ Python 3 bytes encoder. Used to print filename in
      diffstat output. Assumes that filenames are in utf-8.
  """
  if not PY3K:
    return b

  # [ ] figure out how to print non-utf-8 filenames without
  #     information loss
  return b.decode('utf-8')

class NullHandler(logging.Handler):
  """ Copied from Python 2.7 to avoid getting
      `No handlers could be found for logger "patch"`
      http://bugs.python.org/issue16539
  """
  def handle(self, record):
    pass
  def emit(self, record):
    pass
  def createLock(self):
    self.lock = None

logger.addHandler(NullHandler())
  fp = open(filename, "rb")
  res = patchset.parse(fp)
  fp.close()
  if res == True:
  ps = PatchSet( StringIO(s) )
  ps = PatchSet( urllib_request.urlopen(url) )
def to_file_bytes(content):
  if PY3K:
    if not isinstance(content, bytes):
      content = bytes(content, "utf-8")
  elif isinstance(content, unicode):
    content = content.encode("utf-8")
  return content


  new_content = to_file_bytes(content)
    for h in self.hunks:
      yield h
    for i in self.items:
      yield i
          self._lineno, self._line = compat_next(super(wrapumerate, self))
        # git-format-patch with --full-index generates full blob index, which is 40 symbols length
        # shortcut index length may vary, seems to depend on the project size
            and re.match(b'(?:index \\w{7,40}..\\w{7,40} \\d{6}|new file mode \\d*)', p.header[idx+1])):
      output += (format % (tostr(names[i]), str(insert[i] + delete[i]), hist))
    src = open(srcname, "rb")
    tgt = open(tgtname, "wb")

    debug("processing target file %s" % tgtname)

    tgt.writelines(self.patch_stream(src, hunks))
    tgt.close()
    src.close()
import re
import hashlib
import os
import subprocess

import settings
from django.core.cache import cache

class Compiler(object):
	""" Compile Stylus CSS files """

    def __init__(self, files):
        self.files = files

    def path(self, *paths):
        return os.path.join(settings.STYLUS_ROOT, *paths)

    @property
    def hash(self):
        if not hasattr(self, '_hash'):
            self._hash = hashlib.sha1(''.join(self.files)).hexdigest()
        return self._hash

    def mtime(self, f):
        return os.path.getmtime(self.path(f))

    @property
    def mtimes(self):
        return map(self.mtime, self.files)
    
    def build(self, output):
        files = map(self.path, self.files)
        with open(os.path.join(settings.STYLUS_OUTPUT_DIR, output), 'w') as out:
            proc = subprocess.Popen([settings.STYLUS_BIN, settings.STYLUS_PARAMS] + files,
                                    stdout=subprocess.PIPE)
            stdout, stderr = proc.communicate()
            out.write(stdout)

    def compile(self):
        mtimes = self.mtimes

        base_name = hashlib.sha1(''.join(map(str, mtimes))).hexdigest()[:16]
        name = '.'.join([base_name, 'js'])        

        key = '-'.join(['STYLUS', self.hash])

        previous = cache.get(key)
        if previous is None or previous != name:
            self.build(name)
            cache.set(key, name, settings.STYLUS_CACHE_TIME)

        return os.path.join(settings.STYLUS_OUTPUT_DIR, name)


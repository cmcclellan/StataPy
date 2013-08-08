import subprocess
from tempfile import NamedTemporaryFile
import os
import json

class Model(object):

    def __init__(self, data, cmdline, scalars=['N', 'r2'],
                 macros=['cmdline'], matrices=['b', 'V'], format='%12.6f',
                 path_to_stata_binary='stata'):
        self.data = data
        self.cmdline = cmdline

        assert len(scalars) > 0, "The code in template.do assumes at least one scalar."
        self.save = {
            'scalars': scalars,
            'macros': macros,
            'matrices': matrices
            }
        self.format = format

        self.paths = {
            'csv': self._temporary_file_path(suffix='.csv'),
            'do': self._temporary_file_path(suffix='.do'),
            'json': self._temporary_file_path(suffix='.json'),
            }
        self.path_to_stata_binary = path_to_stata_binary

    def _temporary_file_path(self, **kwargs):
        f = NamedTemporaryFile(delete=False, **kwargs)
        f.close()
        return f.name

    def to_dict(self):
        result = dict([(k, ' '.join(v)) for k, v in self.save.items()])
        result.update({
            'cmdline': self.cmdline,
            'format': self.format,
        })
        result.update(self.paths)
        return result

    # TODO: This path may need to be made relative to this file.
    with open('template.do') as f:
        template = f.read()

    def estimate(self):
        self.data.to_csv(self.paths['csv'])
        with open(self.paths['do'], 'w') as f:
            text = self.template % self.to_dict()
            f.write(text)
        subprocess.call([self.path_to_stata_binary, '-b', self.paths['do']])
        with open(self.paths['json']) as f:
            result = json.load(f)
        self.cleanup()
        return result

    def cleanup(self):
        for path in self.paths.values():
            os.remove(path)
        do_file_name = os.path.basename(self.paths['do'])
        root, extension = os.path.splitext(do_file_name)
        log_file_name = root + '.log'
        os.remove(log_file_name)

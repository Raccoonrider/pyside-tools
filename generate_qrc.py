### Automatic Qt resource file generator

from pathlib import Path
import os

__location__ = Path(os.path.dirname(os.path.realpath(__file__)))

target_path = __location__ / 'src' / 'resource.qrc'
resources = [
    {'prefix':'icons',       'dir':__location__ / 'src' / 'static' / 'icons'},
    {'prefix':'stylesheets', 'dir':__location__ / 'src' / 'ui' / 'stylesheets'},
]
formats = [
    '.qss',
    '.svg'
]


with target_path.open(mode='wt', encoding='utf-8') as target:
    target.write('<!DOCTYPE RCC>\n<RCC version="1.0">\n')

    for resource in resources:
        prefix = resource['prefix']
        dir = resource['dir']

        target.write(f'\t<qresource prefix="{prefix}">\n')

        dirpath, dirnames, filenames = next(os.walk(str(dir)))
        for filename in filenames:
            for fmt in formats:
                if filename.endswith(fmt):
                    target.write(f'\t\t<file alias="{filename}">')
                    target.write(str(dir / filename))
                    target.write(f'</file>\n')
        target.write(f'\t</qresource>\n')
    target.write('</RCC>\n')
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=invalid-name, too-few-public-methods

"""Documentation TBD"""

from __future__ import unicode_literals
from __future__ import print_function

import logging # pylint: disable=unused-import

from .common import container_type

class blob(object):
    """Documentation TBD"""

    def __init__(self, **kwargs):
        """Documentation TBD"""

        #super(blob, self).__init__()

        self.docker = kwargs.get('docker', {}) # Docker specific
        self.singularity = kwargs.get('singularity', {}) # Singularity specific

    def __read_blob(self, path):
        """Documentation TBD"""

        blob = ''
        try:
            if path:
                with open(path, 'r') as f:
                    blob = f.read()
            else:
                logging.warning('Blob file not specified')
        except:
            logging.error('Error opening blob {}'.format(path))

        return blob

    def toString(self, ctype):
        """Documentation TBD"""

        if ctype == container_type.DOCKER:
            return self.__read_blob(self.docker)
        if ctype == container_type.SINGULARITY:
            return self.__read_blob(self.singularity)
        else:
            logging.error('Unknown container type')
            return ''

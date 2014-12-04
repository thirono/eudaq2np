eudaq2np
=======================

A simple script to convertert DUT data from EUDAQ to python.
 
# Installation

setup env:
```bash
export CFLAGS="-I${EUDAQ_DIR}/main/include" 
export LDFLAGS="-L${EUDAQ_DIR}/build/main/lib"
```

install:
```bash
python setup.py install
```

or develop:
```bash
python setup.py develop
```

# Installation (Windows)
* change #setup.cfg# to setup.cfg
* edit (path to python)\Lib\distutils\msvc9compiler.py (not recommended but how?)
```python
383  plat_spec="x86_amd64"
```
* with command prompt,
```bash
set SET VS90COMNTOOLS=%VS120COMNTOOLS%
python setup.py develop
```
* add EUDAQ_DIR/bin to PATH

# Example usage 

Setup path to libEUDAQ.so:
```bash
export LD_LIBRARY_PATH=${EUDAQ_DIR}/build/main/lib/:${LD_LIBRARY_PATH}
```

```python
import numpy as np
from eudaq2np import data_np

if __name__ == "__main__":

    data = data_np("run000022.raw", "GENERIC")
    print data, data['x'].astype(int)

    H, xedges, yedges = np.histogram2d(data['y'].astype(int), data['x'].astype(int))
    print H
```



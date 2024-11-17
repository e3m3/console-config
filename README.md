#  Copyright

Copyright 2024, Giordano Salvador
SPDX-License-Identifier: BSD-3-Clause

Author/Maintainer:  Giordano Salvador <73959795+e3m3@users.noreply.github.com>


#  Description (Console Configurations)

A repository of console configuration files to easily bootstrap new development environments.

##  Prerequisites

*   python3

*   python3-lit (for testing)

*   FileCheck/llvm (for testing)

*   [podman][1][[1]]|[docker][2][[2]] (for testing)

##  Setup

*   To install the the configuration files to their default local user paths, run:
    
    ```shell
    python3 ./setup.py
    ```

*   To test the setup script on a fresh [Fedora][3][[3]] container, run:

    ```shell
    podman build -t console-config-fedora41 -f container/Containerfile .
    #   OR
    docker build -t console-config-fedora41 -f container/Dockerfile .
    ```


#  References

[1]:    https://podman.io/

[2]:    https://www.docker.com/

[3]:    https://fedoraproject.org/

1.  `https://podman.io/`

1.  `https://www.docker.com/`

1.  `https://fedoraproject.org/`

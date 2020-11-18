Open-CE
=======
:slug: opence
:author: Ken Lett
:menu: POWERLinux/OpenPOWER Development Hosting, Open-CE, 3

The Open Source Lab (OSUOSL) and Center for Genome Research and Biocomputing (CGRB) partner with IBM and OpenPOWER in order to provide a download resources around Open-CE. Open-CE is a community driven software distribution for machine learning that runs on standard Linux platforms with NVIDIA GPU technologies.
- `Current release`_

- `Previous releases`_

.. _Current release:
.. _Release 1.0.0:

Open-CE Release 1.0.0
---------------------

*Release date: 11/10/2020*

**What's new**

Open-CE 1.0 is the `current release`_ of Open-CE and includes the following features:

- conda packages are now available on ppc64le.
- conda packages are now available on x86.
- TensorFlow 2.3.1
- PyTorch 1.6.0
- Open-CE is distributed as prebuilt containers, or on demand through the Conda provisioning process.

  - All of the Conda packages are available in a `Open-CE Conda channel`_
  - Current Conda packages are available in a `Current Open-CE Conda channel`_
  - There is no install package to download, instead connect to the Conda channel and install your packages from there
  - Package dependencies are automatically resolved
  - Delivery of packages is open and continuous
  - Enable Python versions 3.6, 3.7, 3.8
  - You can run more than one framework at the same time in the same environment. For example, you can run TensorFlow and PyTorch at the same time.

.. _Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/
.. _Current Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/current

**Learn more**

Get information about planning, configuring, and managing Open-CE 1.0 Below:

- `Planning`_
- `System setup`_
- `Setting up the software repository`_
- `Creating conda environments`_ (recommended)
- `Installing the MLDL frameworks`_
- `Uninstalling the MLDL frameworks`_

.. _planning:

Planning
--------

We recommend users use one of the listed operating systems listed below. This is a standard conda repository and can be added to any conda install. Conda must be configured to give priority to installing packages from this channel.

.. _system setup:

System setup
------------

Open-CE can be installed and run directly on a bare-metal RHEL and Ubuntu based systems.

Supported hardware:
^^^^^^^^^^^^^^^^^^^

- IBM Power System IC922 with NVIDIA Tesla T4 GPUs
- IBM Power System AC922 with NVIDIA Tesla V100 GPUs
- IBM Power System S822LC with NVIDIA Tesla P100 GPUs
- x86_64 systems with NVIDIA Tesla V100 or P100 GPUs

- Supported operating systems:

  - Red Hat Enterprise Linux for POWER LE 7.8
  - Community Enterprise Operating System (CentOS) 7.8
  - Ubuntu 20.04.1

- Required 3rd party software:

  - NVIDIA GPU driver 440.33.01
  - CUDA driver 10.2

Installing the Open-CE Repository and Frameworks
------------------------------------------------

.. _Setting up the software repository:

Setting up the software repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Open-CE MLDL packages are distributed as conda packages in an online conda repository. conda must be configured to give priority to installing packages from this channel.

Add the Open-CE channel to the conda configuration by running the following command:

.. code-block:: bash

  conda config --prepend channels https://ftp.osuosl.org/pub/open-ce/current/

.. _Creating conda environments:

Creating conda environments (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With conda, you can create environments that have different versions of Python or packages installed in them. Conda environments are optional but recommended. If not used, packages are installed in the default environment called base, which often has a higher risk of containing conflicting packages or dependencies. Switching between environments is called activating the environment.

The syntax to create and activate a conda environment is:

.. code-block:: bash

  conda create --name <environment name> python=<python version> conda activate <environment name>

Note: It is recommended that you specify the Python version when creating a new environment. If you do not specify the version, Python 3.7 is installed when any package that requires Python are installed.

The only valid Python versions with Open-CE are Python 3.6, 3.7 and 3.8.

For example, to create an environment named opence_env with Python 3.6:

.. code-block:: bash

  conda create --name opence_env python=3.6 conda activate opence_env

For more information on what you can do with conda environment see https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html.

Note: Open-CE should be run as a non-privileged user and not root. The Open-CE components are designed to be usable by normal users, and the pre-installed docker images provide a non-root user by default. Some of the Open-CE components will give warnings or will fail when run as root.


.. _Installing the MLDL frameworks:

Installing frameworks individually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can install the MLDL frameworks individually. The framework packages include the following versions.

**Table 1. Framework packages**

======================  ===========================  =======   ====================  ===================
Package                 Description                  Version   Available on ppc64le  Available on x86_64
======================  ===========================  =======   ====================  ===================
``pytorch``             PyTorch                      1.6.0     X                     X
``tensorflow``          TensorFlow with GPU support  2.3.1     X                     X
``tensorflow-serving``  TensorFlow Serving           2.3.0     X                     X
``py-xgboost``          xgboost with GPU support     1.2.0     X                     X
======================  ===========================  =======   ====================  ===================


With the conda environment activated, run the following command:

.. code-block:: bash

  conda install <package name>

.. _Uninstalling the MLDL frameworks:

Uninstalling the Open-CE MLDL frameworks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Find information about uninstalling machine learning and deep learning MLDL frameworks.

The MLDL framework packages can be uninstalled individually, or you can uninstall all of the MLDL packages at the same time.

If the frameworks are installed into a separate conda environment, all of the frameworks can be removed by simply deleting the environment:

.. code-block:: bash

  conda env remove -n <environment name>

Individual frameworks (and any packages that depend on them) can be removed by removing the individual package:

.. code-block:: bash

  conda remove <package name>

Important: This command removes the specified packages and any packages that depend on any of the specified packages. If you want to skip this dependency checking and remove just the requested packages, add the --force option. However, this may break your environment, so use this option with caution.

Previous releases

We recommend that you install the most current release of Open-CE, however, if you have an earlier version installed, you can find information below:

.. _Previous releases:

Previous releases
-----------------

- `Release 1.0.0`_

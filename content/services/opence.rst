Open-CE
=======
:slug: services/powerdev/opence
:author: Maximillian Schmidt, Ken Lett
:menu: POWERLinux/OpenPOWER Development Hosting, Open-CE, 5

The Open Source Lab (OSUOSL) and Center for Quantitative Life Sciences (CQLS, previously CGRB) partner with IBM and OpenPOWER in order to provide a download resources around Open-CE. Open-CE is a community driven software distribution for machine learning that runs on standard Linux platforms with NVIDIA GPU technologies.

- `Current release`_
- `Previous releases`_

.. _Current release:

.. _Release 1.9.1:

Open-CE Release 1.9.1
---------------------

*Release date: 08/07/2023*

This is bug fix release 1 of release 1.9. Version 1.8.0 was also released (01/12/2023), but no description/update was given.

**What's new**

- Various bugs fixed
- Updated packages

  - xgboost 1.7.6
  - DALI 1.26
  - mamba 1.4.2
  - Onnxruntime 1.15.1
  - Pytorch 2.0.1
  - Ray 2.5.0
  - Tensorboard 2.12.2
  - Tensorflow-addons 0.19.0
  - Tensorflow Serving 2.12.1
  - Apache-beam 2.48.0

- This release of Open-CE supports:

  - NVIDIA's CUDA version 11.8
  - Python 3.9 and 3.10

- All the packages are built with openssl 1.*.


**Learn more**

Get information about planning, configuring, and managing Open-CE 1.9 Below:

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
- x86_64 systems with NVIDIA Tesla V100 or P100 GPUs

Supported operating systems:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ppc64le

  - Community Enterprise Operating System (CentOS) 8.1-6
  - Red Hat Enterprise Linux for POWER LE 8.1-6
  - Rocky / Alma Linux 8.1-6
  - Ubuntu 20.04.1


- x86

  - Community Enterprise Operating System (CentOS) 7.8, 8.x
  - Red Hat Enterprise Linux for POWER LE 7.8, 8.1-6, 9.0
  - Rocky / Alma Linux 8.1-6, 9.0
  - Ubuntu 20.04.1-4, 22.04.x


Required 3rd party software:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- NVIDIA GPU driver 520.61.05
- CUDA version 11.8

Installing the Open-CE Repository and Frameworks
------------------------------------------------

.. _Setting up the software repository:

Setting up the software repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Open-CE MLDL packages are distributed as conda packages in an online conda repository. Conda must be configured to give priority to installing packages from this channel.

Add the Open-CE channel to the conda configuration by running the following command:

.. code-block:: bash

  conda config --prepend channels https://ftp.osuosl.org/pub/open-ce/current/

.. _Creating conda environments:

Creating conda environments (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With conda, you can create environments that have different versions of Python or packages installed in them. Conda environments are optional but recommended. If not used, packages are installed in the default environment called base, which often has a higher risk of containing conflicting packages or dependencies. Switching between environments is called activating the environment.

The syntax to create and activate a conda environment is:

.. code-block:: bash

  conda create --name <environment name> python=<python version>
  conda activate <environment name>

**Note**: It is recommended that you specify the Python version when creating a new environment. If you do not specify the version, Python 3.7 is installed when any package that requires Python are installed.

The only valid Python versions with Open-CE 1.9 are Python 3.9 and 3.10.

For example, to create an environment named opence_env with Python 3.9:

.. code-block:: bash

  conda create --name opence_env python=3.9
  0conda activate opence_env

For more information on what you can do with conda environment see https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html.

Note: Open-CE should be run as a non-privileged user and not root. The Open-CE components are designed to be usable by normal users, and the pre-installed docker images provide a non-root user by default. Some of the Open-CE components will give warnings or will fail when run as root.

.. _Installing the MLDL frameworks:

Installing frameworks individually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can install the MLDL frameworks individually. The framework packages include the following versions.

**Table 1. Framework packages (Open-CE 1.9.1)**

======================================  ==========  ================================================================================  ====================  ================  ======
Package                                 Version     Description                                                                       Available on ppc64le  Available on x86  noarch
======================================  ==========  ================================================================================  ====================  ================  ======
_pytorch_select                         2           Package used to select the specific PyTorch build variant                         X                     tbd
_tensorflow_select                      2           Package used to select the specific Tensorflow build variant                      X                     tbd
absl-py                                 1.0.0       This repository is a collection of Python library code for building...            X                     tbd
aioredis                                2.0.1       asyncio (PEP 3156) Redis support                                                  X                     tbd               X
aiorwlock                               1.3.0       Read write lock for asyncio.                                                      X                     tbd               X
apache-beam                             2.48.0      Apache Beam: An advanced unified programming model                                X                     tbd
array-record                            0.2.0       A new file format derived from Riegeli                                            X                     tbd
arrow-cpp                               11.0.0      C++ libraries for Apache Arrow                                                    X                     tbd
arrow-cpp-proc                          11.0.0      A meta-package to select Arrow build variant                                      X                     tbd
arviz                                   0.14.0      Exploratory analysis of Bayesian models with Python                               X                     tbd               X
av                                      10.0.0      Pythonic bindings for FFmpeg.                                                     X                     tbd
bazel                                   5.3.0       build system originally authored by Google                                        X                     tbd
bazel-toolchain                         0.1.5       Helper script to generate a crosscompile toolchain for Bazel with the...          X                     tbd
black                                   22.12.0     The uncompromising code formatter.                                                X                     tbd
blas                                    1                                                                                             X                     tbd
blessed                                 1.19.1      Easy, practical library for making terminal apps, by providing an...              X                     tbd               X
boost_mp11                              1.76.0      C++11 metaprogramming library                                                     X                     tbd
bsddb3                                  6.2.9       Python bindings for Oracle Berkeley DB                                            X                     tbd
cargo-bundle-licenses                   0.4.0       Bundle thirdparty licenses for Cargo projects into a single file.                 X                     tbd
cfitsio                                 3.47        A library for reading and writing FITS files                                      X                     tbd
cli11                                   2.2.0       CLI11 is a command line parser for C++11 and beyond that provides a...            X                     tbd
cloudpickle                             2.2.1       Extended pickling support for Python objects                                      X                     tbd               X
cmake                                   3.26.4      CMake is an extensible, open-source system that manages the build process         X                     tbd
cmdstan                                 2.31.0      CmdStan, the command line interface to Stan                                       X                     tbd
cmdstanpy                               1.1.0       CmdStanPy is a lightweight interface to Stan for Python users which...            X                     tbd               X
coin-or-cbc                             2.10.7      COIN-OR branch and cut (Cbc)                                                      X                     tbd
coin-or-cgl                             0.60.6      COIN-OR Cut Generation Library (Cgl)                                              X                     tbd
coin-or-clp                             1.17.7      COIN-OR linear programming (Clp)                                                  X                     tbd
coin-or-osi                             0.108.7     Coin OR Open Solver Interface (OSI)                                               X                     tbd
coin-or-utils                           2.11.6      COIN-OR Utilities (CoinUtils)                                                     X                     tbd
coincbc                                 2.10.7      COIN-OR branch and cut (Cbc)                                                      X                     tbd               X
crcmod                                  1.7         CRC Generator                                                                     X                     tbd
cudatoolkit                             11.8.0      CUDA Toolkit - Including CUDA runtime                                             X                     tbd
cudatoolkit-dev                         11.8.0      Develop, Optimize and Deploy GPU-accelerated Apps                                 X                     tbd
cudnn                                   8.8.1_11.8  The NVIDIA CUDA Deep Neural Network library. A GPU-accelerated library...         X                     tbd
dali                                    1.26.0      A library containing both highly optimized building blocks and an...              X                     tbd
dali-ffmpeg                             5.1.1       Cross-platform solution to record, convert and stream audio and video.            X                     tbd
dali-tf-plugin                          1.26.0      A library containing both highly optimized building blocks and an...              X                     tbd
datasets                                2.10.1      HuggingFace/Datasets is an open library of NLP datasets.                          X                     tbd               X
dateutils                               0.6.12      Various utilities for working with date and datetime objects                      X                     tbd               X
deepdiff                                5.8.1       Deep Difference and Search of any Python object/data.                             X                     tbd               X
deepspeed                               0.8.3       DeepSpeed Library: An easy-to-use deep learning optimization software suite.      X                     tbd
dill                                    0.3.1.1     Serialize all of python (almost)                                                  X                     tbd               X
dm-tree                                 0.1.7       A library for working with nested data structures.                                X                     tbd
eigen                                   3.4.0       C++ template library for linear algebra                                           X                     tbd
etils                                   1.0.0       Collection of eclectic utils for python.                                          X                     tbd               X
fastapi                                 0.85.1      FastAPI framework, high performance, easy to learn, fast to code, ready...        X                     tbd               X
fire                                    0.4.0       Python Fire is a library for creating command line interfaces (CLIs)...           X                     tbd               X
gmock                                   1.13.0      Google's C++ test framework                                                       X                     tbd
googledrivedownloader                   0.4         Minimal class to download shared files from Google Drive.                         X                     tbd               X
grpc-cpp                                1.41.0      gRPC - A high-performance, open-source universal RPC framework                    X                     tbd
grpcio                                  1.51.3      HTTP/2-based RPC framework                                                        X                     tbd
gtest                                   1.13.0      Google's C++ test framework                                                       X                     tbd
hatch-fancy-pypi-readme                 22.8.0      Fancy PyPI READMEs with Hatch                                                     X                     tbd               X
hjson-py                                3.1.0       Hjson, a user interface for JSON.                                                 X                     tbd               X
horovod                                 0.28.0      Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet.  X                     tbd
httplib2                                0.19.1      A comprehensive HTTP client library                                               X                     tbd               X
inquirer                                2.10.1      Collection of common interactive command line user interfaces, based on...        X                     tbd               X
java-11-openjdk-cos7-ppc64le            11.0.6.10   (CDT) OpenJDK Runtime Environment                                                 X                     tbd               X
java-11-openjdk-devel-cos7-ppc64le      11.0.6.10   (CDT) OpenJDK Development Toolkit                                                 X                     tbd               X
java-11-openjdk-headless-cos7-ppc64le   11.0.6.10   (CDT) The OpenJDK runtime environment without audio and video support             X                     tbd               X
jax                                     0.4.7       Differentiate, compile, and transform Numpy code                                  X                     tbd
jaxlib                                  0.4.7       Composable transformations of Python+NumPy programs: differentiate,...            X                     tbd
jpeg-turbo                              2.1.4       IJG JPEG compliant runtime library with SIMD and other optimizations              X                     tbd
keras                                   2.12.0      Deep Learning for Python                                                          X                     tbd
libabseil                               20230125    Abseil Common Libraries (C++)                                                     X                     tbd
libdate                                 3.0.1       A date and time library based on the C++11/14/17 <chrono> header                  X                     tbd
libevent                                2.1.11      An event notification library.                                                    X                     tbd
libflac                                 1.3.3       Flac audio format                                                                 X                     tbd
liblightgbm                             3.3.5       Light Gradient Boosting Machine that uses tree based learning algorithms          X                     tbd
libmamba                                1.4.2       A fast drop-in alternative to conda, using libsolv for dependency resolution      X                     tbd
libmambapy                              1.4.2       A fast drop-in alternative to conda, using libsolv for dependency resolution      X                     tbd
libnetcdf                               4.8.1       Libraries and data formats that support array-oriented scientific data.           X                     tbd
libopenblas                             0.3.23      An Optimized BLAS library                                                         X                     tbd
libopenblas-static                      0.3.23      OpenBLAS static libraries.                                                        X                     tbd
libopencv                               4.7.0       Computer vision and machine learning software library.                            X                     tbd
libortools                              9.6         Google Operations Research Tools (or-tools) python package                        X                     tbd
libprotobuf                             3.21.12     Protocol Buffers - Google's data interchange format. C++ Libraries...             X                     tbd
libprotobuf-static                      3.21.12     Protocol Buffers - Google's data interchange format. C++ Libraries...             X                     tbd
libsndfile                              1.0.31      libsndfile - a C library for reading and writing files containing...              X                     tbd
libtar                                  1.2.20      C library for manipulating tar files                                              X                     tbd
libtensorflow                           2.12.0      TensorFlow is a machine learning library, base GPU package, tensorflow only.      X                     tbd
libxgboost                              1.7.6       Scalable, Portable and Distributed Gradient Boosting Library                      X                     tbd
lightgbm                                3.3.5       Light Gradient Boosting Machine that uses tree based learning algorithms          X                     tbd
lightgbm-proc                           3.3.5       Light Gradient Boosting Machine that uses tree based learning algorithms          X                     tbd
lightning-app                           2.0.1       Use Lightning Apps to build everything from production-ready,...                  X                     tbd               X
lightning-cloud                         0.5.32      Lightning Cloud.                                                                  X                     tbd               X
lightning-fabric                        2.0.1       Use Lightning Apps to build everything from production-ready,...                  X                     tbd               X
lightning-utilities                     0.8.0       Lightning Utilities.                                                              X                     tbd               X
llvm-openmp                             14.0.6      The OpenMP API supports multi-platform shared-memory parallel...                  X                     tbd
magma                                   2.6.1       Dense linear algebra library similar to LAPACK but for...                         X                     tbd
mamba                                   1.4.2       A fast drop-in alternative to conda, using libsolv for dependency resolution      X                     tbd
maturin                                 0.13.2      Build and publish crates with pyo3, rust-cpython and cffi bindings as...          X                     tbd
ml_dtypes                               0.1.0       A stand-alone implementation of several NumPy dtype extensions used in...         X                     tbd
mypy-protobuf                           3.1.0       Generate mypy stub files from protobuf specs                                      X                     tbd               X
nasm                                    2.15.05     Netwide Assembler: an assembler targetting the Intel x86 series of processors.    X                     tbd
nccl                                    2.17.1      NVIDIA Collective Communications Library. Implements multi-GPU and...             X                     tbd
nomkl                                   3           None                                                                              X                     tbd
numactl                                 2.0.16      Control NUMA policy for processes or shared memory                                X                     tbd
nvcc_linux-ppc64le                      11.8        A meta-package to enable the right nvcc.                                          X                     tbd
objsize                                 0.6.1       Traversal over Python's objects subtree and calculate the total...                X                     tbd               X
onnx                                    1.13.1      Open Neural Network Exchange library                                              X                     tbd
onnxconverter-common                    1.13.0      Common utilities for ONNX converters                                              X                     tbd               X
onnxmltools                             1.11.2      ONNXMLTools enables conversion of models to ONNX                                  X                     tbd               X
onnxruntime                             1.15.1      cross-platform, high performance ML inferencing and training accelerator          X                     tbd
openblas                                0.3.23      An optimized BLAS library                                                         X                     tbd
openblas-devel                          0.3.23      OpenBLAS headers and libraries for developing software that used OpenBLAS.        X                     tbd
opencensus                              0.7.13      OpenCensus - A stats collection and distributed tracing framework                 X                     tbd               X
opencv                                  4.7.0       Computer vision and machine learning software library.                            X                     tbd
openmpi                                 4.1.4       An open source Message Passing Interface implementation.                          X                     tbd
optional-lite                           3.4.0       A C++17-like optional, a nullable object for C++98, C++11 and later in...         X                     tbd
orbit-ml                                1.1.4.2     Orbit is a package for bayesian time series modeling and inference.               X                     tbd
orc                                     1.8.2       C++ libraries for Apache ORC                                                      X                     tbd
ordered-set                             4.1.0       A MutableSet that remembers its order, so that every entry has an index.          X                     tbd               X
orjson                                  3.8.0       orjson is a fast, correct JSON library for Python.                                X                     tbd
ortools-cpp                             9.6         Google Operations Research Tools (or-tools) python package                        X                     tbd
ortools-python                          9.6         Google Operations Research Tools (or-tools) python package                        X                     tbd
prophet                                 1.1.2       Automatic Forecasting Procedure                                                   X                     tbd
protobuf                                4.21.12     Protocol Buffers - Google's data interchange format.                              X                     tbd
py-opencv                               4.7.0       Computer vision and machine learning software library.                            X                     tbd
pyarrow                                 11.0.0      Python libraries for Apache Arrow                                                 X                     tbd
pybind11                                2.9.2       Seamless operability between C++11 and Python                                     X                     tbd
pybind11-abi                            4           Seamless operability between C++11 and Python                                     X                     tbd               X
pybind11-global                         2.9.2       Seamless operability between C++11 and Python                                     X                     tbd
pydot                                   1.4.1       Python interface to Graphviz's Dot                                                X                     tbd
pyink                                   23.1.1      Pyink is a python formatter, forked from Black with slightly different behavior.  X                     tbd               X
pyro-api                                0.1.2       Generic API for dispatch to Pyro backends.                                        X                     tbd               X
pyro-ppl                                1.8.4       A Python library for probabilistic modeling and inference                         X                     tbd               X
python-multipart                        0.0.5       A streaming multipart parser for Python.                                          X                     tbd               X
pytorch                                 2.0.1       Meta-package to install GPU-enabled PyTorch variant                               X                     tbd
pytorch-base                            2.0.1       PyTorch is an optimized tensor library for deep learning using GPUs and CPUs.     X                     tbd
pytorch-cpu                             2.0.1       Meta-package to install CPU-only PyTorch variant                                  X                     tbd
pytorch-lightning                       2.0.1       PyTorch Lightning is the lightweight PyTorch wrapper for ML...                    X                     tbd               X
pytorch-lightning-bolts                 0.6.0       Pretrained SOTA Deep Learning models, callbacks and more for research...          X                     tbd               X
pytorch_geometric                       2.3.0       Geometric Deep Learning Extension Library for PyTorch                             X                     tbd               X
pytorch_scatter                         2.1.1       PyTorch Extension Library of Optimized Scatter Operations                         X                     tbd
pytorch_sparse                          0.6.17      PyTorch Extension Library of Optimized Autograd Sparse Matrix Operations          X                     tbd
ray-air                                 2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-all                                 2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-core                                2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-dashboard                           2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-data                                2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-default                             2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-k8s                                 2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-rllib                               2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-serve                               2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-train                               2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
ray-tune                                2.5.0       Ray is a fast and simple framework for building and running distributed...        X                     tbd
rdflib                                  6.1.1       RDFLib is a Python library for working with RDF, a simple yet powerful...         X                     tbd               X
readchar                                4.0.3       Library to easily read single chars and key strokes.                              X                     tbd               X
rust                                    1.65.0      Rust is a systems programming language that runs blazingly fast,...               X                     tbd
rust-std-powerpc64le-unknown-linux-gnu  1.65.0      Rust is a systems programming language that runs blazingly fast,...               X                     tbd               X
rust_linux-ppc64le                      1.65.0      A safe systems programming language (conda activation scripts)                    X                     tbd
safeint                                 3.0.26      SafeInt is a class library for C++ that manages integer overflows.                X                     tbd
sentencepiece                           0.1.97      An unsupervised text tokenizer and detokenizer mainly for Neural...               X                     tbd
setuptools-rust                         1.5.1       Setuptools rust extension plugin                                                  X                     tbd               X
skl2onnx                                1.14        Convert scikit-learn models and pipelines to ONNX                                 X                     tbd               X
sklearn-pandas                          2.1.0       Pandas integration with sklearn                                                   X                     tbd               X
starlette                               0.20.4      The little ASGI framework that shines. ✨                                         X                     tbd               X
starlette-full                          0.20.4      The little ASGI framework that shines. ✨                                         X                     tbd               X
starsessions                            1.3.0       Pluggable session support for Starlette.                                          X                     tbd               X
tensorboard                             2.12.2      TensorFlow's Visualization Toolkit.                                               X                     tbd               X
tensorboard-data-server                 0.7.0       Data server for TensorBoard                                                       X                     tbd               X
tensorflow                              2.12.0      Meta-package to install GPU-enabled TensorFlow variant                            X                     tbd
tensorflow-addons                       0.19.0      A library that implements new functionality not available in core TensorFlow.     X                     tbd
tensorflow-addons-proc                  0.19.0      A meta-package to select TensorFlow addons build variant                          X                     tbd
tensorflow-base                         2.12.0      TensorFlow is a machine learning library, base GPU package, tensorflow only.      X                     tbd
tensorflow-cpu                          2.12.0      Meta-package to install CPU-only TensorFlow variant                               X                     tbd
tensorflow-datasets                     4.9.2       A collection of datasets ready to use with TensorFlow                             X                     tbd               X
tensorflow-estimator                    2.12.0      TensorFlow Estimator                                                              X                     tbd               X
tensorflow-hub                          0.13.0      A library for transfer learning by reusing parts of TensorFlow models.            X                     tbd               X
tensorflow-io                           0.32.0      Dataset, streaming, and file system extensions                                    X                     tbd
tensorflow-io-gcs-filesystem            0.32.0      Dataset, streaming, and file system extensions                                    X                     tbd
tensorflow-metadata                     1.13.1      Utilities for passing TensorFlow-related metadata between tools                   X                     tbd               X
tensorflow-model-optimization           0.7.4       A library that to optimize TensorFlow models for deployment and execution.        X                     tbd
tensorflow-probability                  0.19.0      TensorFlow Probability is a library for probabilistic reasoning and...            X                     tbd
tensorflow-serving                      2.12.1      TensorFlow Serving is an open-source library for serving machine learning models  X                     tbd
tensorflow-serving-api                  2.12.1      TensorFlow Serving is an open-source library for serving machine learning models  X                     tbd               X
tensorflow-text                         2.12.0      TF.Text is a TensorFlow library of text related ops, modules, and subgraphs.      X                     tbd
tf2onnx                                 1.13.0      Tensorflow to ONNX converter                                                      X                     tbd
tokenize-rt                             4.2.1       A wrapper around the stdlib `tokenize` which roundtrips.                          X                     tbd               X
torchdata                               0.6.0       Common modular data loading primitives for easily constructing flexible...        X                     tbd
torchmetrics                            0.11.4      Machine learning metrics for distributed, scalable PyTorch applications.          X                     tbd               X
torchtext                               0.15.2      Meta-package to install torchtext variant for GPU-enabled pytorch                 X                     tbd
torchtext-base                          0.15.2      Text utilities and datasets for PyTorch                                           X                     tbd
torchtext-cpu                           0.15.2      Meta-package to install torchtext variant for CPU-only pytorch                    X                     tbd
torchvision                             0.15.2      Meta-package to install GPU-enabled torchvision variant                           X                     tbd
torchvision-base                        0.15.2      Image and video datasets and models for torch deep learning                       X                     tbd
torchvision-cpu                         0.15.2      Meta-package to install CPU-only torchvision variant                              X                     tbd
types-futures                           3.3.8       Typing stubs for futures                                                          X                     tbd               X
types-protobuf                          4.21.0.2    Typing stubs for protobuf                                                         X                     tbd               X
tzdata-java-cos7-ppc64le                2019c       (CDT) OpenJDK Runtime Environment                                                 X                     tbd               X
uvicorn                                 0.16.0      The lightning-fast ASGI server.                                                   X                     tbd
xarray-einstats                         0.4.0       Stats, linear algebra and einops for xarray.                                      X                     tbd               X
xgboost                                 1.7.6       Scalable, Portable and Distributed Gradient Boosting Library                      X                     tbd
xgboost-proc                            1.7.6       Scalable, Portable and Distributed Gradient Boosting Library                      X                     tbd
xsimd                                   9.0.1       C++ Wrappers for SIMD Intrinsices                                                 X                     tbd
======================================  ==========  ================================================================================  ====================  ================  ======

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
^^^^^^^^^^^^^^^^^

We recommend that you install the most current release of Open-CE, however, if you have an earlier version installed, you can find information below:

.. _Previous releases:

Previous releases
-----------------

.. _Release 1.7.2:

Open-CE Release 1.7.2
---------------------

*Release date: 09/29/2022*

This is bug fix release 2 of release 1.7

**What's new**

- Various build fixed
- Upadated packages

  - TensorFlow  2.9.2
  - xgboost 1.6.2
  - DALI  1.16.1
  - Ray 1.13.1
  - PyTorch Geometric 2.1.0
  - numba 0.56.1
  - snapml  1.8.10
  - TF Serving  2.9.2

.. _Release 1.6.1:

Open-CE Release 1.6.1
---------------------

*Release date: 05/19/2022*

This is bug fix release 1 of release 1.6

**What's new**

- Various build fixed
- Upadated packages

  - pytorch-lightning 1.6.3
  - pyDeprecate 0.3.2
  - torchmetrics  0.8.2
  - tensorflow-io-gcs-filesystem  0.25.0
  - ray 1.11.1


.. _Release 1.5.1:

Open-CE Release 1.5.1
---------------------

*Release date: 01/11/2021*

This is bug fix release 1 of release 1.5

**What's new**

Key changes include:

Refresh PyTorch to v1.10.1
remove py36 blocks and dataclasses from all recipes
Update DALI to 1.9 (from 1.9-dev)
Update tensorflow metadata to 1.5.0
Enable uwsgi for python version 3.9

.. _Release 1.5.0:


Open-CE Release 1.5.0
---------------------

*Release date: 12/08/2021*

**What's new**

This is release 1.5.0 of the Open Cognitive Environment (Open-CE), codenamed Otter

This release of Open-CE supports NVIDIA's CUDA versions 10.2,11.2 as well as Python 3.7,3.8,3.9.


.. _Release 1.4.1:


Open-CE Release 1.4.1
---------------------

*Release date: 10/10/2021*

**What's new**

This is bug fix 1 of release 1.4 of Open Cognitive Environment (Open-CE). Main updates are:

- TensorFlow is now at 2.6.2
- PyTorch is now at 1.9.1
- The DALI recipe now builds on both x86 and ppc.
- Bug Fix Changes
- Changes For open-ce
- Release updates for 1.4.1 (#545)
- Use updated uwsgi 2.0.20 from conda-forge (#544)
- Pin updates for 1.4.1 (#540)
- Update OpenCV to v3.4.16 (#open-ce/opencv-feedstock#27)
- Update Tensorflow Probability to v0.14.1 (#open-ce/tensorflow-probability-feedstock#19)
- Update pytorch-lightning to 1.4.9 and torchmetrics to v0.5.1 (#open-ce/pytorch-lightning-feedstock#24)

For a complete list of changes also see the `1.4.0 release`_.

.. _1.4.0 release: https://github.com/open-ce/open-ce/releases/tag/open-ce-v1.4.0

.. _Release 1.3.1:


Open-CE Release 1.3.1
---------------------

*Release date: 08/26/2021*

**What's new**

This is bug fix 1 of release 1.3 of Open Cognitive Environment (Open-CE), code named Chipmunk.
Bug Fix Changes

- Fix uwsgi build #470 #474
- Adjust h5py pins for py39 #473 #482
- enable open-cv build directly in opence-env.yaml #477
- Move feedstock patches directory into /envs #484
- Update OpenBLAS to 0.3.13 #479
- Add pin for ICU #493
- adjust build resources for TensorFlow builds open-ce/tensorflow-feedstock#58 open-ce/tensorflow-feedstock#59
- TensorFlow: update to 2.5.1 open-ce/tensorflow-feedstock#61
- Pytorch: use TBB for CPU and OpenMP for GPU open-ce/pytorch-feedstock#68
- Horovod: use system compilers when using system MPI open-ce/horovod-feedstock#28
- LightGBM: use system compilers when using system MPI open-ce/LightGBM-feedstock#21
- OpenCV: disable LAPACK temporarily open-ce/opencv-feedstock#19

For a complete list of changes also see the `1.3.0 release`_.

.. _1.3.0 release: https://github.com/open-ce/open-ce/releases/tag/open-ce-v1.3.0


.. _Release 1.2.2:


Open-CE Release 1.2.2
---------------------

*Release date: 06/16/2021*

**What's new**

This is release 1.2.2 of Open Cognitive Environment (Open-CE).

This is bug fix 2 of release 1.2 of Open Cognitive Environment (Open-CE), code named Prairiedog.

Bug Fix Changes

- libgcc and libstdc++ were pinned to cos6 versions to allow for compilation with GCC 7.2/7.3 #433
- TensorFlow was updated to version 2.4.2
- Dependency pins were loosened for networkx, requests, scipy and werkzeug #439
- Changed PyArrow to build with -O2 optimizations to avoid a compiler error in GCC 7.x
- Add patch to PyArrow to fix handling of decimal types with negative scale in C data import


Previously, the Open-CE build tools were part of the `Open-CE repository`_. `They can now be found in their own repo`_.

A release of Open-CE now only includes:
- The Open-CE env files used to generate a conda channel containing all of the packages that are part of an Open-CE release.
- A collection of feedstocks containing conda recipes for building the packages that are part of an Open-CE release.

**New Features**
- PyArrow is now included as part of Open-CE.
- The protobuf version that all Open-CE packages use is now set to 3.11.2.
- TensorFlow serving was removed, due to its incompatibility with protobuf 3.11.2

**Bug Fix Changes**
- The conda hash string has been removed from the name of all noarch packages.
- The version of sqlite that TensorFlow uses is now explicitly set 38 39.

- Open-CE is distributed as prebuilt containers, or on demand through the Conda provisioning process.

  - All of the Conda packages are available in a `Open-CE Conda channel`_
  - Conda packages are available in the `Open-CE 1.2.0 Conda channel`_
  - There is no install package to download, instead connect to the Conda channel and install your packages from there
  - Package dependencies are automatically resolved
  - Delivery of packages is open and continuous
  - Enable Python versions 3.6, 3.7, 3.8
  - You can run more than one framework at the same time in the same environment. For example, you can run TensorFlow and PyTorch at the same time.

.. _They can now be found in their own repo: https://github.com/open-ce/open-ce-builder
.. _Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/
.. _Current Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/current
.. _Open-CE repository: https://github.com/open-ce
.. _Open-CE 1.2.0 Conda channel: https://ftp.osuosl.org/pub/open-ce/1.2.0



.. _Release 1.2.0:

Open-CE Release 1.2.0
---------------------

*Release date: 04/16/2021*

**What's new**

This is release 1.2 of Open Cognitive Environment (Open-CE), code named Prairiedog.

Previously, the Open-CE build tools were part of the `Open-CE repository`_. `They can now be found in their own repo`_.

A release of Open-CE now only includes:
- The Open-CE env files used to generate a conda channel containing all of the packages that are part of an Open-CE release.
- A collection of feedstocks containing conda recipes for building the packages that are part of an Open-CE release.

**New Features**
- PyArrow is now included as part of Open-CE.
- The protobuf version that all Open-CE packages use is now set to 3.11.2.
- TensorFlow serving was removed, due to its incompatibility with protobuf 3.11.2

**Bug Fix Changes**
- The conda hash string has been removed from the name of all noarch packages.
- The version of sqlite that TensorFlow uses is now explicitly set 38 39.

- Open-CE is distributed as prebuilt containers, or on demand through the Conda provisioning process.

  - All of the Conda packages are available in a `Open-CE Conda channel`_
  - Conda packages are available in the `Open-CE 1.2.0 Conda channel`_
  - There is no install package to download, instead connect to the Conda channel and install your packages from there
  - Package dependencies are automatically resolved
  - Delivery of packages is open and continuous
  - Enable Python versions 3.6, 3.7, 3.8
  - You can run more than one framework at the same time in the same environment. For example, you can run TensorFlow and PyTorch at the same time.

.. _They can now be found in their own repo: https://github.com/open-ce/open-ce-builder
.. _Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/
.. _Current Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/current
.. _Open-CE repository: https://github.com/open-ce
.. _Open-CE 1.2.0 Conda channel: https://ftp.osuosl.org/pub/open-ce/1.2.0


.. _Release 1.1.1:

Open-CE Release 1.1.1
---------------------

*Release date: 01/12/2021*

**What's new**

This is release 1.1 of Open Cognitive Environment (Open-CE), code named Meerkat.

- Added support for CUDA 11.0, which is currently supported on RHEL8.
- Added recipes for the following new packages: LightGBM, TensorFlow Model Optimization, TensorFlow Addons, PyTorch Lightning Bolts, Python Flatbuffers.
- Added the open-ce tool for running build and validate commands. This replaces the previously existing build_env.py and build_feedstock.py entry points to Open-CE.
- Added the open-ce test commands to test packages that are built by Open-CE.
    open-ce build env will now output conda environment files that can be used to create conda environments containing the packages that were just built.
- The open-ce build image command has been added to create Docker images from the output of open-ce build env.
- Open-CE build tools can now accept --cuda_versions as an argument to choose a version of CUDA to build with.
- open-ce build env will now check for circular dependencies between packages.
- open-ce build env will verify that all packages that are being built can be installed within the same conda environment before starting a build.
- Added the --skip_build_packages argument to open-ce build env.
- Jinja can now be used within any Open-CE configuration file.
- Improved performance when attempting to build packages that already exist.
- Added the patches key to the Open-CE environment files to allow for patching feedstocks.

.. _Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/
.. _Current Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/current


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
  - Conda packages are available in the `Open-CE 1.0.0 Conda channel`_
  - There is no install package to download, instead connect to the Conda channel and install your packages from there
  - Package dependencies are automatically resolved
  - Delivery of packages is open and continuous
  - Enable Python versions 3.6, 3.7, 3.8
  - You can run more than one framework at the same time in the same environment. For example, you can run TensorFlow and PyTorch at the same time.

.. _Open-CE Conda channel: https://ftp.osuosl.org/pub/open-ce/
.. _Open-CE 1.0.0 Conda channel: https://ftp.osuosl.org/pub/open-ce/1.0.0

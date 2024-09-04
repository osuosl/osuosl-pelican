Open-CE
=======
:slug: services/powerdev/opence
:author: Maximillian Schmidt (>1.8.0), Ken Lett (<=1.8.0)
:menu: POWERLinux/OpenPOWER Development Hosting, Open-CE, 5

The Open Source Lab (OSUOSL) and Center for Quantitative Life Sciences (CQLS, previously CGRB) partner with IBM and OpenPOWER in order to provide download resources around Open-CE. Open-CE is a community driven software distribution for machine learning that runs on standard Linux platforms alongside NVIDIA GPU technologies. Questions and general discussions involving OSU's builds can be directed to the Open-CE Slack channel: https://open-ce.slack.com/archives/C06DGE5GHND .

- `Current release`_
- `Previous releases`_

.. _Current release:

.. _Release 1.11.2:

Open-CE Release 1.11.2
----------------------

This is release 1.11.2 of Open Cognitive Environment (Open-CE)

Build Status:

============ ========== ====== ====== ======== ========= ========= =============
CPU Arch     Build Base Py3.10 Py3.11 CPU-only CUDA 11.8 CUDA 12.2 Date
============ ========== ====== ====== ======== ========= ========= =============
ppc64le(P9)  UBI 8      DONE   DONE   DONE     DONE      DONE      08/15/2024
ppc64le(P10) UBI 9      DONE   DONE   DONE     N/A       N/A       08/20/2024
x86_64       UBI 9      DONE   DONE   DONE     Err       Err
============ ========== ====== ====== ======== ========= ========= =============

**What's new**

- Updated packages

  - langchain 0.1.13
  - langchain-community 0.0.29
  - langchain-core 0.1.35
  - langchain-text-splitters 0.0.2
  - langsmith 0.1.19
  - libmamba 1.5.7
  - libmambapy 1.5.7
  - libopenblas 0.3.26
  - libopenblas-static 0.3.26
  - mamba 1.5.7
  - onnx 1.16.0
  - openblas[-devel] 0.3.27
  - orjson 3.9.15
  - safetensors 0.4.1
  - transformers 4.38.0
  - werkzeug 3.0.3

- This release of Open-CE supports:

  - NVIDIA's CUDA version 11.8, 12.2
  - Python 3.10, 3.11

- Important Notes:

  - ppc64le builds with CUDA are UBI 8 container image based, not UBI 9 (amd64,arm64 only)
    - Nvidia will not provide ppc64le-based UBI 8(+) images with CUDA > 12.4.1
    - See: https://hub.docker.com/r/nvidia/cuda/tags?page=1&page_size=&ordering=&name=-devel-ubi
  - CV-CUDA is disabled in DALI for ppc64le
  - Jax and Jaxlib packages not available for ppc64le CUDA

**Learn more**

Get information about planning, configuring, and managing Open-CE below:

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

Open-CE can be installed and run directly on a bare-metal RHEL and Ubuntu based system.

Supported hardware:
^^^^^^^^^^^^^^^^^^^

- IBM Power System IC922 with NVIDIA Tesla T4 GPUs
- IBM Power System AC922 with NVIDIA Tesla V100 GPUs
- X86_64 systems with NVIDIA Tesla V100 or P100 GPUs

Supported operating systems:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ppc64le

  - Community Enterprise Operating System (CentOS) 8.1-6
  - Red Hat Enterprise Linux for POWER LE 8.1-10
  - Rocky / Alma Linux 8.1-10
  - Ubuntu 20.04.1


- X86

  - Community Enterprise Operating System (CentOS) 8.1-6
  - Red Hat Enterprise Linux for POWER LE 8.X, 9.X
  - Rocky / Alma Linux 8.X, 9.X
  - Ubuntu 20.04.1-4, 22.04.x

\* Note: We (CQLS & OSL) have dropped support of RHEL/CentOS 7, as we have transitioned most systems away before the EOS date.


Required 3rd party software:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- NVIDIA GPU driver >= 520.61.05
- CUDA version 11.8, 12.2

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

**Note**: It is recommended that you specify the Python version when creating a new environment. If you do not specify the version, the minimum python version for all dependent packages that require Python is installed.

For example, to create an environment named opence_env with Python 3.11:

.. code-block:: bash

  conda create --name opence_env python=3.11
  conda activate opence_env

For more information on what you can do with conda environment see https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html.

Note: Open-CE should be run as a non-privileged user and not root. The Open-CE components are designed to be usable by normal users, and the pre-installed docker images provide a non-root user by default. Some of the Open-CE components will give warnings or will fail when run as root.

.. _Installing the MLDL frameworks:

Installing frameworks individually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can install the MLDL frameworks individually. The framework packages include the following versions.

**Table 1. Framework packages (Open-CE 1.11.0)**

======================================== =========== ================================================================================== ========
Package                                  Version     Summary                                                                            noarch
======================================== =========== ================================================================================== ========
_pytorch_select                          2.0         Package used to select the specific PyTorch build variant
_tensorflow_select                       2.0         Package used to select the specific Tensorflow build variant
absl-py                                  2.0.0       This repository is a collection of Python library code for building...
aioredis                                 2.0.1       asyncio (PEP 3156) Redis support                                                   X
aiorwlock                                1.3.0       Read write lock for asyncio.                                                       X
apache-beam                              2.53.0      Apache Beam: An advanced unified programming model
array-record                             0.2.0       A new file format derived from Riegeli
arrow-cpp                                15.0.1      C++ libraries for Apache Arrow
arrow-cpp-proc                           15.0.1      A meta-package to select Arrow build variant
arviz                                    0.14.0      Exploratory analysis of Bayesian models with Python                                X
av                                       10.0.0      Pythonic bindings for FFmpeg.
backoff                                  2.2.1       Function decoration for backoff and retry                                          X
bazel                                    6.1.0       build system originally authored by Google
bazel-toolchain                          0.1.5       Helper script to generate a crosscompile toolchain for Bazel with the...
black                                    23.10.0     The uncompromising code formatter.
blas                                     1.0         None
blessed                                  1.19.1      Easy, practical library for making terminal apps, by providing an...               X
boost_mp11                               1.76.0      C++11 metaprogramming library
bsddb3                                   6.2.9       Python bindings for Oracle Berkeley DB
cfitsio                                  3.470       A library for reading and writing FITS files
cli11                                    2.2.0       CLI11 is a command line parser for C++11 and beyond that provides a...
cmake                                    3.26.4      CMake is an extensible, open-source system that manages the build process
cmdstan                                  2.33.1      CmdStan, the command line interface to Stan
cmdstanpy                                1.2.0       CmdStanPy is a lightweight interface to Stan for Python users which...             X
coin-or-cbc                              2.10.7      COIN-OR branch and cut (Cbc)
coin-or-cgl                              0.60.6      COIN-OR Cut Generation Library (Cgl)
coin-or-clp                              1.17.7      COIN-OR linear programming (Clp)
coin-or-osi                              0.108.7     Coin OR Open Solver Interface (OSI)
coin-or-utils                            2.11.6      COIN-OR Utilities (CoinUtils)
coincbc                                  2.10.7      COIN-OR branch and cut (Cbc)                                                       X
crcmod                                   1.7         CRC Generator
cudatoolkit                              12.2.0      CUDA Toolkit - Including CUDA runtime
cudatoolkit-dev                          12.2.0      Develop, Optimize and Deploy GPU-accelerated Apps
cudnn                                    8.9.6_12.2  The NVIDIA CUDA Deep Neural Network library. A GPU-accelerated library...
dali                                     1.32.0      A library containing both highly optimized building blocks and an...
dali-ffmpeg                              5.1.1       Cross-platform solution to record, convert and stream audio and video.
dali-tf-plugin                           1.32.0      A library containing both highly optimized building blocks and an...
datasets                                 2.16.1      HuggingFace/Datasets is an open library of NLP datasets.                           X
dateutils                                0.6.12      Various utilities for working with date and datetime objects                       X
deepdiff                                 5.8.1       Deep Difference and Search of any Python object/data.                              X
deepspeed                                0.11.1      DeepSpeed Library: An easy-to-use deep learning optimization software suite.
dm-tree                                  0.1.8       A library for working with nested data structures.
eigen                                    3.4.0       C++ template library for linear algebra
etils                                    1.0.0       Collection of eclectic utils for python.                                           X
fastapi                                  0.92.0      FastAPI framework, high performance, easy to learn, fast to code, ready...         X
ffmpeg                                   4.2.2       Cross-platform solution to record, convert and stream audio and video.
fire                                     0.4.0       Python Fire is a library for creating command line interfaces (CLIs)...            X
flatbuffers                              23.1.21     Memory Efficient Serialization Library
fsspec                                   2023.10.0   A specification for pythonic filesystems                                           X
gmock                                    1.13.0      Google's C++ test framework
googledrivedownloader                    0.4         Minimal class to download shared files from Google Drive.                          X
grpc-cpp                                 1.54.3      gRPC - A high-performance, open-source universal RPC framework
grpcio                                   1.54.3      HTTP/2-based RPC framework
gtest                                    1.13.0      Google's C++ test framework
hatch-fancy-pypi-readme                  23.1.0      Fancy PyPI READMEs with Hatch                                                      X
hjson-py                                 3.1.0       Hjson, a user interface for JSON.                                                  X
holidays                                 0.27        Generate and work with holidays in Python                                          X
horovod                                  0.28.1      Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet.
httplib2                                 0.19.1      A comprehensive HTTP client library                                                X
huggingface_hub                          0.20.0      Client library to download and publish models on the huggingface.co hub            X
inquirer                                 2.10.1      Collection of common interactive command line user interfaces, based on...         X
java-11-openjdk-cos7-ppc64le             11.0.6.10   (CDT) OpenJDK Runtime Environment                                                  X
java-11-openjdk-devel-cos7-ppc64le       11.0.6.10   (CDT) OpenJDK Development Toolkit                                                  X
java-11-openjdk-headless-cos7-ppc64le    11.0.6.10   (CDT) The OpenJDK runtime environment without audio and video support              X
jax                                      0.4.23      Differentiate, compile, and transform Numpy code
jaxlib                                   0.4.23      Composable transformations of Python+NumPy programs: differentiate,...
joblib                                   1.3.2       Lightweight pipelining: using Python functions as pipeline jobs.                   X
jpeg-turbo                               2.1.4       IJG JPEG compliant runtime library with SIMD and other optimizations
jsonpatch                                1.33        Apply JSON-Patches (RFC 6902)                                                      X
keras                                    2.14.0      Deep Learning for Python
langchain                                0.1.13      Building applications with LLMs through composability                              X
langchain-community                      0.0.29      Community contributed LangChain integrations.                                      X
langchain-core                           0.1.35      Core APIs for LangChain, the LLM framework for buildilng applications...           X
langchain-text-splitters                 0.0.2       LangChain text splitting utilities                                                 X
langsmith                                0.1.19      Client library to connect to the LangSmith language model tracing and...           X
libabseil                                20230125.0  Abseil Common Libraries (C++)
libdate                                  3.0.1       A date and time library based on the C++11/14/17 &lt;chrono&gt; header
libflac                                  1.3.3       Flac audio format
liblightgbm                              4.2.0       Light Gradient Boosting Machine that uses tree based learning algorithms
libmamba                                 1.5.7       A fast drop-in alternative to conda, using libsolv for dependency resolution
libmambapy                               1.5.7       A fast drop-in alternative to conda, using libsolv for dependency resolution
libnvjitlink                             12.2.140    CUDA nvJitLink library
libopenblas                              0.3.27      An Optimized BLAS library
libopenblas-static                       0.3.27      OpenBLAS static libraries.
libopencv                                4.8.1       Computer vision and machine learning software library.
libortools                               9.6         Google Operations Research Tools (or-tools) python package
libprotobuf                              3.21.12     Protocol Buffers - Google&#39;s data interchange format. C++ Libraries...
libprotobuf-static                       3.21.12     Protocol Buffers - Google&#39;s data interchange format. C++ Libraries...
libsndfile                               1.0.31      libsndfile - a C library for reading and writing files containing...
libtar                                   1.2.20      C library for manipulating tar files
libtensorflow                            2.14.1      TensorFlow is a machine learning library, base GPU package, tensorflow only.
libxgboost                               2.0.3       Scalable, Portable and Distributed Gradient Boosting Library
lightgbm                                 4.2.0       Light Gradient Boosting Machine that uses tree based learning algorithms
lightgbm-proc                            4.2.0       Light Gradient Boosting Machine that uses tree based learning algorithms
lightning-app                            2.1.3       Use Lightning Apps to build everything from production-ready,...                   X
lightning-cloud                          0.5.57      Lightning Cloud.                                                                   X
lightning-fabric                         2.1.3       Use Lightning Apps to build everything from production-ready,...                   X
lightning-utilities                      0.10.0      Lightning Utilities.                                                               X
llvm-openmp                              14.0.6      The OpenMP API supports multi-platform shared-memory parallel...
magma                                    2.6.1       Dense linear algebra library similar to LAPACK but for...
mamba                                    1.5.7       A fast drop-in alternative to conda, using libsolv for dependency resolution
nasm                                     2.15.05     Netwide Assembler: an assembler targetting the Intel x86 series of processors.
nccl                                     2.19.3      NVIDIA Collective Communications Library. Implements multi-GPU and...
nomkl                                    3.0         None
numactl                                  2.0.16      Control NUMA policy for processes or shared memory
objsize                                  0.6.1       Traversal over Python&#39;s objects subtree and calculate the total...             X
onnx                                     1.16.0      Open Neural Network Exchange library
onnxconverter-common                     1.14.0      Common utilities for ONNX converters                                               X
onnxmltools                              1.12.0      ONNXMLTools enables conversion of models to ONNX                                   X
onnxruntime                              1.16.3      cross-platform, high performance ML inferencing and training accelerator
openblas                                 0.3.27      An optimized BLAS library
openblas-devel                           0.3.27      OpenBLAS headers and libraries for developing software that used OpenBLAS.
opencensus                               0.7.13      OpenCensus - A stats collection and distributed tracing framework                  X
opencv                                   4.8.1       Computer vision and machine learning software library.
opencv-proc                              4.8.1       Computer vision and machine learning software library.
openmpi                                  4.1.5       An open source Message Passing Interface implementation.
optional-lite                            3.4.0       A C++17-like optional, a nullable object for C++98, C++11 and later in...
orbit-ml                                 1.1.4.2     Orbit is a package for bayesian time series modeling and inference.
orc                                      1.9.0       C++ libraries for Apache ORC
ordered-set                              4.1.0       A MutableSet that remembers its order, so that every entry has an index.           X
orjson                                   3.9.15      orjson is a fast, correct JSON library for Python.
ortools-cpp                              9.6         Google Operations Research Tools (or-tools) python package
ortools-python                           9.6         Google Operations Research Tools (or-tools) python package
packaging                                23.2        Core utilities for Python packages                                                 X
prophet                                  1.1.5       Automatic Forecasting Procedure
protobuf                                 4.21.12     Protocol Buffers - Google&#39;s data interchange format.
py-opencv                                4.8.1       Computer vision and machine learning software library.
pyarrow                                  15.0.1      Python libraries for Apache Arrow
pyink                                    23.10.0     Pyink is a python formatter, forked from Black with slightly different behavior.   X
pyro-api                                 0.1.2       Generic API for dispatch to Pyro backends.                                         X
pyro-ppl                                 1.8.4       A Python library for probabilistic modeling and inference                          X
python-flatbuffers                       23.1.21     Python runtime library for use with the Flatbuffers serialization format.          X
python-multipart                         0.0.5       A streaming multipart parser for Python.                                           X
pytorch                                  2.1.2       Meta-package to install GPU-enabled PyTorch variant
pytorch-base                             2.1.2       PyTorch is an optimized tensor library for deep learning using GPUs and CPUs.
pytorch-cpu                              2.1.2       Meta-package to install CPU-only PyTorch variant
pytorch-lightning                        2.1.3       PyTorch Lightning is the lightweight PyTorch wrapper for ML...                     X
pytorch-lightning-bolts                  0.7.0       Pretrained SOTA Deep Learning models, callbacks and more for research...           X
pytorch_geometric                        2.4.0       Geometric Deep Learning Extension Library for PyTorch                              X
pytorch_scatter                          2.1.2       PyTorch Extension Library of Optimized Scatter Operations
pytorch_sparse                           0.6.18      PyTorch Extension Library of Optimized Autograd Sparse Matrix Operations
ray-air                                  2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-all                                  2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-client                               2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-core                                 2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-data                                 2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-default                              2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-rllib                                2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-serve                                2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-train                                2.9.2       Ray is a fast and simple framework for building and running distributed...
ray-tune                                 2.9.2       Ray is a fast and simple framework for building and running distributed...
rdflib                                   6.1.1       RDFLib is a Python library for working with RDF, a simple yet powerful...          X
rust                                     1.77.0      Rust is a systems programming language that runs blazingly fast,...
rust-std-powerpc64le-unknown-linux-gnu   1.77.0      Rust is a systems programming language that runs blazingly fast,...                X
rust_linux-ppc64le                       1.77.0      A safe systems programming language (conda activation scripts)
safeint                                  3.0.26      SafeInt is a class library for C++ that manages integer overflows.
safetensors                              0.4.1       Fast and Safe Tensor serialization
scikit-learn                             1.3.0       A set of python modules for machine learning and data mining
sentencepiece                            0.1.99      An unsupervised text tokenizer and detokenizer mainly for Neural...
setuptools-rust                          1.5.1       Setuptools rust extension plugin                                                   X
skl2onnx                                 1.16.0      Convert scikit-learn models and pipelines to ONNX                                  X
sklearn-pandas                           2.2.0       Pandas integration with sklearn                                                    X
stanio                                   0.3.0       Preparing inputs to and reading outputs from Stan.                                 X
starlette                                0.25.0      The little ASGI framework that shines.                                             X
starlette-full                           0.25.0      The little ASGI framework that shines.                                             X
starsessions                             1.3.0       Pluggable session support for Starlette.                                           X
tensorboard                              2.14.0      TensorFlow&#39;s Visualization Toolkit.                                            X
tensorboard-data-server                  0.7.0       Data server for TensorBoard                                                        X
tensorflow                               2.14.1      Meta-package to install GPU-enabled TensorFlow variant
tensorflow-base                          2.14.1      TensorFlow is a machine learning library, base GPU package, tensorflow only.
tensorflow-cpu                           2.14.1      Meta-package to install CPU-only TensorFlow variant
tensorflow-datasets                      4.9.4       A collection of datasets ready to use with TensorFlow                              X
tensorflow-estimator                     2.14.0      TensorFlow Estimator                                                               X
tensorflow-hub                           0.15.0      A library for transfer learning by reusing parts of TensorFlow models.             X
tensorflow-io                            0.35.0      Dataset, streaming, and file system extensions
tensorflow-io-gcs-filesystem             0.35.0      Dataset, streaming, and file system extensions
tensorflow-metadata                      1.14.0      Utilities for passing TensorFlow-related metadata between tools                    X
tensorflow-model-optimization            0.7.5       A library that to optimize TensorFlow models for deployment and execution.
tensorflow-probability                   0.22.1      TensorFlow Probability is a library for probabilistic reasoning and...
tensorflow-serving                       2.14.1      TensorFlow Serving is an open-source library for serving machine learning models
tensorflow-serving-api                   2.14.1      TensorFlow Serving is an open-source library for serving machine learning models   X
tensorflow-text                          2.14.0      TF.Text is a TensorFlow library of text related ops, modules, and subgraphs.
tf2onnx                                  1.15.1      Tensorflow to ONNX converter
tiktoken                                 0.6.0       tiktoken is a fast BPE tokeniser for use with OpenAI&#39;s models
tokenize-rt                              4.2.1       A wrapper around the stdlib `tokenize` which roundtrips.                           X
tokenizers                               0.15.2      Fast State-of-the-Art Tokenizers optimized for Research and Production
torchdata                                0.7.1       Common modular data loading primitives for easily constructing flexible...
torchmetrics                             1.2.1       Machine learning metrics for distributed, scalable PyTorch applications.           X
torchtext                                0.16.2      Meta-package to install torchtext variant for GPU-enabled pytorch
torchtext-base                           0.16.2      Text utilities and datasets for PyTorch
torchtext-cpu                            0.16.2      Meta-package to install torchtext variant for CPU-only pytorch
torchvision                              0.16.2      Meta-package to install GPU-enabled torchvision variant
torchvision-base                         0.16.2      Image and video datasets and models for torch deep learning
torchvision-cpu                          0.16.2      Meta-package to install CPU-only torchvision variant
transformers                             4.38.0      State-of-the-art Natural Language Processing for TensorFlow 2.0 and PyTorch        X
tzdata-java-cos7-ppc64le                 2019c       (CDT) OpenJDK Runtime Environment                                                  X
uvicorn                                  0.16.0      The lightning-fast ASGI server.
uwsgi                                    2.0.25.1    The uWSGI project aims at developing a full stack for building hosting...
werkzeug                                 3.0.3       The comprehensive WSGI web application library.
xgboost                                  2.0.3       Scalable, Portable and Distributed Gradient Boosting Library
xgboost-proc                             2.0.3       Scalable, Portable and Distributed Gradient Boosting Library
======================================== =========== ================================================================================== ========

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

We recommend that you install the latest release of Open-CE. However, if you have an earlier version installed, you can find information below:

.. _Previous releases:

Previous releases
-----------------

.. _Release 1.11.0:

Open-CE Release 1.11.0
----------------------

This is release 1.11.0 of Open Cognitive Environment (Open-CE)

============ ========== ====== ====== ======== ========= ========= =============
CPU Arch     Build Base Py3.10 Py3.11 CPU-only CUDA 11.8 CUDA 12.2 Date
============ ========== ====== ====== ======== ========= ========= =============
ppc64le(P9)  UBI 8      DONE   DONE   DONE     Err       DONE      06/07/2024
ppc64le(P10) UBI 9      DONE   DONE   DONE     N/A       N/A       06/11/2024
x86_64       UBI 9      DONE   DONE   DONE     Err       DONE
============ ========== ====== ====== ======== ========= ========= =============

**What's new**

- Updated packages

  - absl-py 2.0.0
  - apache-beam 2.53.0
  - arrow-cpp[-proc] 15.0.1
  - bazel 6.1.0
  - black 23.10.0
  - cmdstan 2.33.1
  - cmdstanpy 1.2.0
  - cudatoolkit[-dev] 12.2.0
  - cudnn 8.9.6_12.2
  - dali[-tf-plugin] 1.32.0
  - datasets 2.16.1
  - deepspeed 0.11.1
  - fsspec 2023.10.0
  - hatch-fancy-pypi-readme 23.1.0
  - horovod 0.28.1
  - huggingface_hub 0.20.0
  - java-11-openjdk 11.0.6.10
  - jax 0.4.23
  - joblib 1.3.2
  - jsonpatch 1.33
  - keras 2.14.0
  - langchain 0.1.6
  - langchain-community 0.0.19
  - langchain-core 0.1.22
  - langsmith 0.0.87
  - libnvjitlink 12.2.140
  - lightgbm[-proc] 4.2.0
  - lightning-app 2.1.3
  - lightning-cloud 0.5.57
  - lightning-fabric 2.1.3
  - lightning-utilities 0.10.0
  - mamba 1.5.6
  - nasm 2.15.05
  - nccl 2.19.3
  - onnx 1.15.0
  - onnxmltools 1.12.0
  - onnxruntime 1.16.3
  - openblas[-devel] 0.3.26
  - [py-]opencv[-proc] 4.8.1
  - packaging 23.2
  - prophet 1.1.5
  - pyarrow 15.0.1
  - pyink 23.10.0
  - pytorch[-base|-cpu] 2.1.2
  - pytorch-lighting 2.1.3
  - pytorch_geometric 2.4.0
  - pytorch_scatter 2.1.2
  - pytorch_sparse 0.6.18
  - ray 2.9.2
  - rust 1.77.0
  - rust-std-\* 1.71.1
  - scikit-learn 1.3.0
  - sentencepiece 0.1.99
  - skl2onnx 1.16.0
  - sklearn-pandas 2.2.0
  - stanio 0.3.0
  - tensorboard 2.14.0
  - tensorflow 2.14.1
  - tensorflow-datasets 4.9.4
  - tensorflow-estimator 2.14.0
  - tensorflow-hub 0.15.0
  - tensorflow-io[-gcs-filesystem] 0.35.0
  - tensorflow-metadata 1.14.0
  - tensorflow-probability 0.22.1
  - tensorflow-text 2.14.0
  - tf2onnx 1.15.1
  - tiktoken 0.6.0
  - tokenizers 0.15.2
  - torchdata 0.7.1
  - torchmetrics 1.2.1
  - torchtext 0.16.2
  - torchvision 0.16.2
  - transformers 4.36.2
  - uwsgi 2.0.25.1
  - xgboost 2.0.3

- This release of Open-CE supports:

  - NVIDIA's CUDA version 11.8, 12.2
  - Python 3.10, 3.11

- Important Notes:

  - ppc64le builds with CUDA are UBI 8 container image based, not UBI 9 (amd64,arm64 only)
    - Nvidia will not provide ppc64le-based UBI 8(+) images with CUDA > 12.4.1
    - See: https://hub.docker.com/r/nvidia/cuda/tags?page=1&page_size=&ordering=&name=-devel-ubi
  - CV-CUDA is disabled in DALI for ppc64le
  - Jax and Jaxlib packages not available for ppc64le CUDA
  - Python 3.9 is no longer supported
  - OSU drops support of EL7


.. _Release 1.10.0:

Open-CE Release 1.10.0
----------------------

*Release date: 01/29/2024 (x86), 02/14/2024 (ppc64le)*

This is release 1.10.0 of Open Cognitive Environment (Open-CE)

**What's new**

- Updated packages

  - aiorwlock 1.3.0
  - arrow-cpp[-proc] 12.0.1
  - backoff 2.2.1
  - cfitsio 3.470
  - cudnn 8.9.2_11.8
  - dali[-tf-plugin] 1.28.0
  - datasets 2.14.4
  - deepspeed 0.10.0
  - dm-tree 0.1.8
  - flatbuffers 23.1.21
  - grpc-cpp & grpcio 1.54.3
  - holidays 0.27
  - jaxlib 0.4.23
  - keras 2.13.1
  - libsolv[-static] 0.7.24
  - lightgbm[-proc] 4.0.0
  - lightning-app 2.0.6
  - lightning-cloud 0.5.37
  - lightning-fabric 2.0.6
  - mamba 1.4.9
  - nccl 2.18.3
  - onnx[converter-common] 1.14.0
  - opencensus 0.7.13
  - [py-]opencv[-proc] 4.8.0
  - openmpi 4.1.4
  - orc 1.9.0
  - prophet 1.1.4
  - pyarrow 12.0.1
  - pytorch-lighting 2.0.6
  - pytorch-lightning-bolts 0.7.0
  - pytorch_geometric 2.3.1
  - ray 2.6.3
  - scipy 1.11.1
  - skl2onnx 1.15.0
  - starlette[-full] 0.25.0
  - tensorboard 2.13.0
  - tensorflow 2.13.0
  - tensorflow-addons 0.21.0
  - tensorflow-hub 0.14.0
  - tensorflow-io[-gcs-filesystem] 0.33.0
  - tensorflow-model-optimization 0.7.5
  - tensorflow-probability 0.20.0
  - tf2onnx 1.15.0

- This release of Open-CE supports:

  - NVIDIA's CUDA version 11.8, 12.2
  - Python 3.9, 3.10, 3.11

- Important Notes:

  - Built with OpenSSL v3
  - CUDA 11.2 is no longer supported
  - Python 3.8 is no longer supported

.. _Release 1.9.3:

Open-CE Release 1.9.3
---------------------

*Release date: 12/20/2023*

This is bug fix release 3 of release 1.9. No other additions have been made since 1.9.1.

**What's new**

- Various bugs fixed
- Updated packages

  - Xgboost 1.7.6
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

.. _Release 1.9.1:

Open-CE Release 1.9.1
---------------------

*Release date: 08/07/2023*

This is bug fix release 1 of release 1.9. Version 1.8.0 was also released (01/12/2023), but no description/update was given.


.. _Release 1.7.2:

Open-CE Release 1.7.2
---------------------

*Release date: 09/29/2022*

This is bug fix release 2 of release 1.7

**What's new**

- Various build fixed
- Upadated packages

  - TensorFlow  2.9.2
  - Xgboost 1.6.2
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
- The DALI recipe now builds on both X86 and ppc.
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
- conda packages are now available on X86.
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

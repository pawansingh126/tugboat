..
      Copyright 2018 AT&T Intellectual Property.
      All Rights Reserved.

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

===============
Getting Started
===============

What is Tugboat?
----------------

Tugboat is a tool to generate Airship site manifest files from an excel
based engineering spec. The tool accepts Excel sheet and corresponding
excel specification as inputs and generates the site level manifests. As
an optional step it can generate an intermediary yaml which contain all
the information that will be rendered to generate Airship site manifests.
This optional step will help the deployment engineer to modify any data
if required.

Basic Usage
-----------

Before using Tugboat, you must:

1. Clone the Tugboat repository:

.. code-block:: console

    git clone https://github.com/att-comdev/tugboat

2. Install the required packages in tugboat/:

.. code-block:: console

     pip3 install -r tugboat/requirements.txt

3. To run the tool:

.. code-block:: console

    export WORKSPACE=<dir where excelspecs are placed>
    export IMAGE=<docker_image>
    tugboat/tools/tugboat.sh <command> <options>

CLI Options
-----------


**-g / --generate_intermediary**

Generate intermediary file from passed excel and excel spec.

**-m / --generate_manifests**

Generate manifests from the generated intermediary file

**-x / --excel PATH**

Path to engineering excel file, to be passed with generate_intermediary.

**-s / --spec PATH**

Path to excel spec, to be passed with generate_intermediary.

**-i / --intermediary**

Path to intermediary file, to be passed with generate_manifests.

**-d / --site_config**

Path to site specific config file, to be passed with generate_manifests.

**-l / --loglevel**

Log level for tugboat. It is INFO:20 by defualt

**-h / --help**

Show the options and exit.

Usage:

::

    # Generate intermediary yaml and site manifests as separate steps
    # Generate Manifest & Intermediary: tugboat -mg -x <DesignSpec> -s <excel spec>
    # Generate Manifest with Intermediary: tugboat -m -i <intermediary>



.. _site definition libraries: https://airship-pegleg.readthedocs.io/en/latest/artifacts.html#definition-library-layout


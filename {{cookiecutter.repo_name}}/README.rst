=============================
{{ cookiecutter.project_name }}
=============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.png
    :target: http://badge.fury.io/py/{{ cookiecutter.repo_name }}
    
.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.png?branch=master
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://coveralls.io/repos/lpomfrey/{{ cookiecutter.repo_name }}/badge.png?branch=master
    :target: https://coveralls.io/r/lpomfrey/{{ cookiecutter.repo_name }}?branch=master

.. image:: https://pypip.in/d/{{ cookiecutter.repo_name }}/badge.png
        :target: https://crate.io/packages/{{ cookiecutter.repo_name }}?version=latest


{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at http://{{ cookiecutter.repo_name }}.rtfd.org.

Quickstart
----------

Install {{ cookiecutter.project_name }}::

    pip install {{ cookiecutter.repo_name }}


Add to your `INSTALLED_APPS`::


    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.app_name }}',
        ...
    )

Then use it in a project::

	import {{ cookiecutter.repo_name }}

Features
--------

* TODO

Debianize, a buildout recipe to create debian packages
======================================================

Debianize uses fpm (https://github.com/jordansissel/fpm) to create debian
packages from python source directories. The only thing it really adds, is
that debianize will also create packages for all depencencies that your
source package has (``install_requires``). Debianize will only create a debian
package from a python
**package**. So you *need* a setup.py.


Usage::

    [buildout]
    parts =
        debianize

    [debianize]
    maintainer = somebody@example.com
    follow_dependencies =
        someobscurepackage
        morestuff
        ivegotnodebianpackageyet

If you define ``follow_dependencies`` debianize will only create packages for
things that match any of the regex patterns in that option. If omit
``follow_dependencies``, it will build debian packages for anything defined as
a dependency with ``install_requires``. You can not use spaces in any of the
patterns! This is useful if some of the dependencies are allready available as
debian packages and others are not.

The above defined ``follow_dependencies`` will be matched like this::

    $NAME =~ someobscurepackage|morestuff|ivegotnodebianpackageyet

So it will simply put a ``|`` symbol in between the patterns.

Last but not least
------------------

This recipe does not install fpm for you.
instead use http://pypi.python.org/pypi/rubygemsrecipe/0.1.5::

    [rubygems]
    recipe = rubygemsrecipe
    gems = fpm

Don't use spaces in the ``maintainer`` if you are using this recipe because it
passes arguments with $* which causes errors.
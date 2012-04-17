Debianize, a buildout recipe to create debian packages
======================================================

Debianize uses fpm (https://github.com/jordansissel/fpm) to create debian
packages from python source directories. The only thing it really adds, is
that debianize will also create packages for all depencencies that your
source package has. Debianize will only create a debian package from a python
package. So you need a setup.py.


Usage::
    
    [buildout]
    parts =
        debianize
    
    [debianize]
    maintainer = Somebody <somebody@example.com>
    follow_dependencies =
        someobscurepackage
        morestuff
        ivegotnodebianpackageyet

If you define ``follow_dependencies`` debianize will only create packages for
things that match any of the regex patterns in that option. If omit
``follow_dependencies``, it will build debian packages for anything defined as
a dependency with ``install_requires``.


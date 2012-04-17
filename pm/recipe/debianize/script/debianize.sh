#! /bin/bash

MAINTAINER="{{ maintainer or 'Somebody <somebody@example.com>' }}"

if [[ $EUID -ne 0 ]]; then
   echo "You must be root to build a debian package." 1>&2
   exit 100
fi

# remove existing packages
echo "Cleaning old .deb files."
rm -f *.deb

# build package
echo "building package."
fpm --maintainer="$MAINTAINER" --exclude=*.pyc,*.pyo --depends=python --category=python -s python -t deb setup.py > /dev/null

echo "-----------------------------------------------------------"
echo "Downloading dependencies."

# download dependencies
HASH=`openssl dgst -sha1 setup.py | cut -c 17-`
PACKAGE_VAULT=/tmp/.$HASH
mkdir -p $PACKAGE_VAULT
pip -q install --upgrade --no-install --build=$PACKAGE_VAULT -e .

echo "processing dependencies."
for NAME in `ls $PACKAGE_VAULT`
do
    echo -n "package $NAME found in dependency chain, "
    if [[ $NAME =~ {{ follow_dependencies|join('|') }} ]]; then
        echo "BUILDING ...."
        fpm --maintainer="$MAINTAINER" --exclude=*.pyc,,*.pyo --depends=python --category=python -s python -t deb $PACKAGE_VAULT/$NAME/setup.py > /dev/null
    else
        echo "skipping ...."
    fi
done
echo "-----------------------------------------------------------"

#clean up
rm -fr $PACKAGE_VAULT
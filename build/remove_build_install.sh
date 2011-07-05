#!/bin/sh

SRCDIR=../src/

# Check for version number
if [ "$1" = "" ]; then
	echo "Usage: build.sh version_number";
	exit 1
else
	VERSION="$1"
fi

BUILDDIR=scavenger-$VERSION

# sed hack...
if [ `uname -s` = "Darwin" ]; then 
	SED="sed -i \"\""
else
	SED="sed -i\"\""
fi

# Remove the non-functioning version
rm -r $BUILDDIR
rm -r $BUILDDIR.tar.gz

# Create the $BUILDDIR dir
if [ -d $BUILDDIR ]; then 
	rm -rf $BUILDDIR;
fi
mkdir -p $BUILDDIR/scavenger/schedule

# Copy python files into the $BUILDDIR dir.
cp $SRCDIR/CHANGELOG $BUILDDIR
cp $SRCDIR/scavenger/*.py $BUILDDIR/scavenger
cp $SRCDIR/scavenger/schedule/*.py $BUILDDIR/scavenger/schedule/
cp setup.py $BUILDDIR/
$SED s/VERSION/$VERSION/ $BUILDDIR/setup.py

tar cfz $BUILDDIR.tar.gz $BUILDDIR

cd $BUILDDIR
python setup.py build
sudo python setup.py install
cd ..

exit 0

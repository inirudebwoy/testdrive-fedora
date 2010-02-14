#!/bin/sh -e

PKG="testdrive"
MAJOR=1

error() {
	echo "ERROR: $@"
	exit 1
}

head -n1 debian/changelog | grep "lucid" || error "This version must be ready for 'lucid'"

# Tag the release in bzr
minor=`head -n1 debian/changelog | sed "s/^.*($MAJOR.//" | sed "s/-.*$//"`
dch --release
debcommit --release --message="releasing $MAJOR.$minor"

# Sign the tarball
gpg --armor --sign --detach-sig ../"$PKG"_*.orig.tar.gz

# Open the next release for development
nextminor=`expr $minor + 1`
dch -v "$MAJOR.$nextminor" "UNRELEASED"
sed -i "s/$MAJOR.$nextminor) .*;/$MAJOR.$nextminor) unreleased;/" debian/changelog
bzr commit -m "opening $MAJOR.$nextminor"

echo
echo "# To push:"
echo "  bzr push lp:$PKG"
echo
echo "# To upload:"
echo "  dput $PKG-ppa ../*ppa*changes"
echo "  dput ../${PKG}_${MAJOR}.${minor}-0ubuntu1_source.changes"
echo
echo "# Publish tarball at:"
echo "  https://launchpad.net/$PKG/trunk/+addrelease"
echo
echo

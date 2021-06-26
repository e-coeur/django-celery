#!/bin/sh
#
# Downloads maxmind database from http://dev.maxmind.com/geoip/legacy/geolite/
#

mkdir geolite

cd geolite

curl "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country&license_key=SET_YOUR_LICENSE_KEY&suffix=tar.gz" -o GeoLite2-Country.tar.gz

tar xvzf GeoLite2-Country.tar.gz --strip-components 1

rm GeoLite2-Country.tar.gz
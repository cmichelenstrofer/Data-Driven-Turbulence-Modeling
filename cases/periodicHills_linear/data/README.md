
* Get the DNS data from the GitHub repository: https://github.com/xiaoh/para-database-for-PIML

```sh
cd dns
cp -r $para-database-for-PIML/pehill-cases-OpenFOAM/case_1p0/ .fine

cd mapped
blockMesh
# manually change the file /constant/polyMesh/boundaries to match the boundary order in ../fine/constant/polyMesh/boundaries
mapFields ../fine -consistent
cd 0
rm Tau TauDNS U V epsilon k nut p
mv UDNS U
# manually change the object name from UDNS to U in the file.

cd ../../
get_fullfield.py # (dns/mapped, 0, .)

./scale_data.py

get_point.py # (dns/mapped, UxFullField, 7.0, 0.5, 0.005, Ux_point_1)
get_point.py # (dns/mapped, UyFullField, 7.0, 0.5, 0.005, Uy_point_1)
get_point.py # (dns/mapped, UxFullField, 7.0, 2.5, 0.005, Ux_point_2)
get_point.py # (dns/mapped, UyFullField, 7.0, 2.5, 0.005, Uy_point_2)
get_point.py # (dns/mapped, UxFullField, 2.0, 0.5, 0.005, Ux_point_3)
get_point.py # (dns/mapped, UyFullField, 2.0, 0.5, 0.005, Uy_point_3)
get_point.py # (dns/mapped, UxFullField, 2.0, 2.5, 0.005, Ux_point_4)
get_point.py # (dns/mapped, UyFullField, 2.0, 2.5, 0.005, Uy_point_4)

postProcess -func writeCellCentres -case dns/mapped -time 0
cp dns/mapped/0/Cx ./x # (manually delete header/end, leave only the 3000 values)
cp dns/mapped/0/Cy ./y # (manually delete header/end, leave only the 3000 values)
```



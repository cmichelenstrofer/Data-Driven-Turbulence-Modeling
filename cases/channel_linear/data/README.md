

* __foam_synthetic_truth__: foam case to generate "true" (k-omega) data
* __neumann_boundaries__: list of symmetry boundary points for creating symmetric samples (used for ensemble gradient, not adjoint)

Steps to run:
* 1. Run foam_synthetic truth case (cd foam_synthetic_truth; run)
* 2. get_fullfield.py
* 3. get point, (0.05 0.25, 0.005) Ux
* 4. get coordinates (for plotting)

```sh
cd foam_synthetic_truth
./run

cd ..
get_fullfield.py # (foam_synthetic_truth, 5000, .)
rm UyFullField UzFullField
get_point.py # (foam_synthetic_truth, UxFullField, 0.05, 0.25, 0.005, UxPoint_0)

postProcess -func writeCellCentres -case foam_synthetic_truth -time '5000'
cp foam_synthetic_truth/5000/Cy ./y # (manually delete header/end, leave only the 50 values)

get_inputs.py # (foam_synthetic_truth, 5000, .)
```

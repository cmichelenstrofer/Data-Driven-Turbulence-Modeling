

* __foam_synthetic_truth__: foam case to generate "true" (k-omega) data
* __neumann_boundaries__: list of symmetry boundary points for creating symmetric samples (used for ensemble gradient, not adjoint)

Steps to run:
* 1. Run foam_synthetic truth case
* 2. get_fullfield.py
* 3. get point, (0.05 0.25, 0.005) Ux
* 4. get coordinates (for plotting)

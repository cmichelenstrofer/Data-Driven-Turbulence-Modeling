

Create the following from pre-training: 
* __w.0__: weights from pre-training

Create the following from foam_laminar results (TODO: write script to do this):
* __gradU.flow_0.0__
* __timeScale.flow_0.0__
* __tke.flow_0.0__
Note: run foam laminar using

Then create a new 'results' directory and copy these files there. 

Copy the laminar results __{U, p, k, omega, nut, g1}__ to __../foam_primal/0.orig/{}.orig__

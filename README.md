# Data Driven Turbulence Modeling
* Trained with measureable quantities (derived from velocity and pressure fields, e.g. sparse velocity, drag coefficient).
* Deep neural network representing a non-linear eddy viscosity model (NLEVM) using the integrity basis representation (preserve Galilean invariance)
* Fully differentiable (end-to-end) using continuous adjoint equations of the Reynolds-averaged Navier-Stokes (RANS) equations or ensemble gradient. 


Requires [DAFI](https://github.com/xiaoh/DAFI)

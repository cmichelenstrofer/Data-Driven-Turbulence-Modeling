

Create the following from pre-training: 
* __w.0__: weights from pre-training

Create the following from foam_laminar results (TODO: write script to do this):
* __gradU.flow_0.0__
* __timeScale.flow_0.0__
* __tke.flow_0.0__
Note: run foam laminar using

Then create a new 'results' directory and copy these files there. 

Copy the laminar results __{U, p, k, omega, nut, g1}__ to __../foam_primal/0.orig/{}.orig__


```sh
cd pretrain
pretrain.py input.yaml # (plot with plot.ipynb to check it looks ok)
mkdir ../results
cp results/w.1000 ../results/w.0
cd ../foam_laminar
run

cp 5000/grad\(U\) ../results/gradU.flow_0.0 # (manually remove header/end, parenthesis)
cp 5000/timeScale ../results/timeScale.flow_0.0 # (manually remove header/end)
cp 5000/k ../results/tke.flow_0.0 # (manually remove header/end)
echo "0.0" > ../results/V.0
echo "0.0" > ../results/S.0
cp -r ../results ../../

mkdir ../../foam_primal/0.orig
cp 5000/U ../../foam_primal/0.orig/U.orig
cp 5000/p ../../foam_primal/0.orig/p.orig
cp 5000/k ../../foam_primal/0.orig/k.orig
cp 5000/omega ../../foam_primal/0.orig/omega.orig
cp 5000/nut ../../foam_primal/0.orig/nut.orig
cp 5000/g1 ../../foam_primal/0.orig/g1.orig # (manually write internal field 0.0)
```
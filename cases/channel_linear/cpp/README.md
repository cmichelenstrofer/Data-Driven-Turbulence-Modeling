The OpenFOAM case is similar to the baseline k-omega case. 
* change the turbulence model (constant/turbulenceProperties) to kOmegaNNLinear
* include initial 'g1' and 'theta1' files (0.orig) 
* create the model by doing >> tf_save_model.py input_savemodel.yaml

```sh
cd foam_cpp
./run
cd ..

mkdir results
get_inputs.py # (foam_cpp, 5000, results)
cp foam_cpp/5000/g1 results/ # manually delete header/end
cp foam_cpp/5000/U results/ # manually delete header/end and parenthesis
```

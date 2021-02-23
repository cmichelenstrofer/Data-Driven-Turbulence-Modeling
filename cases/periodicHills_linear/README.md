
Training
* case_1p0 is the training case
* DNS data has to be scaled by nu_ratio = 0.00017857142857142857 / 5e-6

DNS
* the dns/fine cases are from the GitHub repository
* the dns/mapped is mapped to the coarser mesh
* before mapping, after creating the coarse mesh: reorder the boundaries in /dns/mapped/constant/polyMesh/boundary to match those in the dns/fine/constant/polymesh/boundary


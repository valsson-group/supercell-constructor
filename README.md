# SuperCellGenerator
Tool for setting up molecular crystal supercell from CIF files

## Authors:
- [Pradip Si](https://www.valsson.info/members/pradip-si), University of North Texas

## Requirments
- ASE
- Mercury visualization
- Pymatgen
- Rdkit
- Open babel
- NumPy

## Instructions 

### How to generate a PBC supercell from a CIF file collected from the CCDC database
1. Save the CIF files for all polymorphs as PDB files in Mercury. 
2. If you select the molecule as the template ( preferably choose the PDB with a unique atom sequence) that will be used to match the atom sequence for other polymorphs.
3. Use `ASE_cif_to_pymatgen_supercell_cif.py` to generate the supercell cif file (choose your cell matrix).
4. Save the supercell cif file as a PDB file in Mercury.
5. Use `mapping_sequence.py` to match the atom sequence to the original PDB. (Ensure that the supercell PDB file saved from Mercury has a similar atom order (it may show different names) as the single molecule PBD file, if not manually create the list for `key_mapping` that matches the atom order).

### If the molecule is not selected as the template file, before proceeding to the step2

- First, reorder the PDB file to match the atom sequence with the template PDB file using `reorder-atoms.py`.
- It should pass the validation and also visualize in Molden or Gaussview to ensure that the connectivity is similar to the template. Otherwise, manually change the coordinates in the reordered PDB file to match the connectivity (!this issue needs to be fixed in the code later).
- Use Open Babel to convert the reordered PDB to cif ( `obabel input.pdb -O output.cif`).
- To avoid any inconvenience change the space group to "P1" in the cif file (`sed -i "s/_space_group_name_H-M_alt '.*'/_space_group_name_H-M_alt 'P1'/" your_file.cif`).
- Return to the step2.


**Check the new file after each step to ensure that the code is doing the correct task**

## Acknowledgements
The development of this tool was supported by an DOE Early Career Award (BES Condensed Phase and Interfacial Molecular Science (CPIMS) / DE-SC0024283)


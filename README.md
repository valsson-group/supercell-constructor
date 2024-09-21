# Super Cell Constructor
Tool for setting up molecular crystal super cells from CIF files

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

### Generate a PBC supercell from a CIF file collected from the CCDC database
1. Save the CIF files for all polymorphs as PDB files using Mercury.
2. Add missing Hs if required ( `obabel file.pdb -O file.pdb -p 7`) and change the space group to original space group or "P1".
3. Select one as a template (preferably choose the PDB with a unique atom sequence) that will be used to match the atom sequence for other PDBs.
4. Use `ASE_cif_to_pymatgen_supercell_cif.py` to generate the supercell cif file for the template. (Change the space group to "P1" in the cif file if it shows error due to space group) 
5. Save the supercell cif file as a PDB file in Mercury.
6. Use `mapping_sequence.py` to match the atom sequence to the original PDB. (Ensure that the supercell PDB file saved from Mercury has a similar atom order as the single molecule PBD file, if not specially for highly symmetric molecule, manually create the list for `key_mapping` that matches the atom order).

### If the molecule is not selected as the template file, before proceeding to the step4

- First, reorder the PDB file to match the atom sequence with the template PDB file using `reorder-atoms.py`.
- It should pass the validation and also visualize in Molden or Gaussview to ensure that the connectivity is similar to the template.
- Use Mercury to convert the reordered PDB to cif.
- Return to the step4.


**Check the new file after each step to ensure that the code is doing the correct task**

## Acknowledgements
The development of this tool was supported by an DOE Early Career Award (BES Condensed Phase and Interfacial Molecular Science (CPIMS) / DE-SC0024283)


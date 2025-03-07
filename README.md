# Super Cell Constructor
Tool for setting up molecular crystal super cells from CIF files

## Authors:
- [Pradip Si](https://www.valsson.info/members/pradip-si), University of North Texas

## Requirments
- ASE
- Pymatgen
- Rdkit
- Open babel 
- NumPy

## Instructions 

### Generate a PBC supercell from a CIF file collected from the CCDC database
1. Save the CIF files for all polymorphs as PDB and add missing Hs if required ( `obabel file.pdb -O file.pdb -h`) using openbabel and delete CONECT lines (sed -i '/^CONECT/d' input.pdb)
3. Select one as a template (preferably choose unit cell has one molecule and the PDB with a unique atom sequence) that will be used to match the atom sequence for other PDBs.
4. Use `ASE_cif_to_pymatgen_supercell_cif.py` to generate the supercell cif file for the template. (Change the space group to "P1" in the cif file if it shows error due to space group) 
5. Use atom_ordering.py to convert supercell.cif to supercell.pdb and regroup the atoms for each molecule 
6. Use `mapping_sequence.py` to match the atom sequence to the template PDB. 

### If the molecule is not selected as the template file, before proceeding to the step4

- First, reorder the PDB file to match the atom sequence with the template PDB file using `reorder-atoms.py`. (use `split_files.py` and `merged_reorder_pdbs.py` for unit cell having more that one molecule)
- It should pass the validation and also visualize to ensure that the connectivity is similar to the template.
- Convert reordered PDB to CIF using obabel and Change the space group to "P1" (sed -i "s/_space_group_name_H-M_alt 'P 1 21\/n 1'/_space_group_name_H-M_alt 'P 1'/" 1241886_reordered.cif)
- Return to the step4.


**Check the new file after each step to ensure that the code is doing the correct task**

## Acknowledgements
The development of this tool was supported by an DOE Early Career Award (BES Condensed Phase and Interfacial Molecular Science (CPIMS) / DE-SC0024283)


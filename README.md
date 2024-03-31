# SuperCellGenerator
Tool for setting up molecular crystal super cell from cif files

## Authors:
- [Pradip Si](https://www.valsson.info/members/pradip-si), University of North Texas

## Requirments
- ASE
- Mercury
- ....

## Instructions 

### How to generate a PBC supercell from a cif file collected from CCDC database
1. Save the cif file as pdb in Mercury
If you select the molecule as template ( preferrebly choose the pdb which has unique atom sequence) that is going to be used to match the atom sequence for other polymorphs
2. Use `ASE_cif_to_pymatgen_supercell_cif.py` to generate the supercell cif file (choose your cell matrix)
3. Save the supercell cif file as pdb in Mercury
4. Use mapping_sequence.py to match the atom squence to the original pdb.(Make sure the supercell pdb file save from Mercury has the similar atom order (can be different name) with the single molecule PBD file, if not manually create the list for key_mapping that matches the atom order)

if the molecule is not selected as the template file, before doing to the step2
a. First reorder the pdb to match atom sequence with the template pdb using reorder-atoms.py
b. It should pass the validation and also visualize in Molden to make sure, connectivity is same as template. Otherwise manually change the coordinates in the reordered file to match the connectivity (!we need to fix the code later)
c. Use openbabel to convert the reordered pdb to cif ( obabel input.pdb -O output.cif )
d. To avoid any inconvenience change the space group to "P1" in the cif file (sed -i "s/_space_group_name_H-M_alt '.*'/_space_group_name_H-M_alt 'P1'/" your_file.cif)
e. Go back to the step2


**Check the new file after each step to make sure the code is doing correct job**

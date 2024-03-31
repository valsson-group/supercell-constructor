obabel input.pdb -O output.cif
sed -i "s/_space_group_name_H-M_alt '.*'/_space_group_name_H-M_alt 'P1'/" output.cif

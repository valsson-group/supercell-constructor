#!/usr/bin/env python

def reorder_atoms(mol_pdb_fname, mol_repeat_pdb, mol_match_pdb):

    elements = []
    
    with open(mol_pdb_fname, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith('HETATM'):
                columns = line.split()
                element = columns[2]
                elements.append(element)
   
    data = {}
    current_key = 0
    
    with open(mol_repeat_pdb, 'r') as f:
        for line in f:
            if line.startswith('HETATM'):
                line_data = line.strip().split()
                if len(line_data[0]) > 6:
                    atom_name = line_data[1]
                    
                    if current_key not in data:
                        data[current_key] = {}
    
                    # Appending a unique index for duplicate entries
                    if atom_name in data[current_key]:
                        atom_name += str(len(data[current_key]))
    
                    values = {
                            'x_cord': float(line_data[4]),
                            'y_cord': float(line_data[5]),
                            'z_cord': float(line_data[6])
                        }
    
                    data[current_key][atom_name] = values
                    
                    
    
                else:
                    atom_name = line_data[2]
                
                    if current_key not in data:
                        data[current_key] = {}
    
                # Appending a unique index for duplicate entries
                    if atom_name in data[current_key]:
                        atom_name += str(len(data[current_key]))
    
                    values = {
                    'x_cord': float(line_data[5]),
                    'y_cord': float(line_data[6]),
                    'z_cord': float(line_data[7])
                    }
    
                    data[current_key][atom_name] = values
    
                if len(data[current_key]) == len(elements):
                    current_key += 1   


    ### Make sure the supercell pdb file save from Mercury has the similar atom order (can be different name) with the single compund PBD file, if not manually create the list the matches the atom order.
    ###keys_mapping = manually generated list
    keys_mapping = elements
    #keys_mapping = ['C1', 'C1D', 'C2', 'C2D', 'C3', 'C3D', 'H1', 'H1D', 'H2', 'H2D', 'H3', 'H3D' ]

    # Replace the keys in each dictionary
    for key, val in data.items():
        temp = {}
        for old_key, new_key in zip(list(val), keys_mapping):
            temp[new_key] = val[old_key]
        val.clear()
        val.update(temp)  
    # if your key_mapping is similar to the elements, you mightn't have to run next three lines, but anyway it does not make any difference
    new_data = {}
    for key, entry in data.items():
        new_data[key] = {atom: entry.get(atom, {}) for atom in elements}

    with open(mol_match_pdb, 'w') as outfile, open(mol_repeat_pdb, 'r') as infile:
        for line in infile:
                if line.startswith('HETATM'):
                    break
                outfile.write(line)
    
        # Initialize the global atom_counter
        atom_counter = 1
    
        # Iterate over each dictionary in the data
        for idx, atom_data in enumerate(new_data.values(), start=1):
            for atom_name, coordinates in atom_data.items():
                outfile.write('{ATOM:<6}{serial_number:>5} {atom_name:<4}{alt_loc_indicator:<1}{res_name:<3} {chain_id:<1}{res_seq_number:>4}{insert_code:<1}   {x:8.3f}{y:8.3f}{z:8.3f}{occupancy:6.2f}{temp_factor:6.2f}\n'.format(
                        ATOM='HETATM',
                        serial_number=atom_counter,
                        atom_name=atom_name,
                        alt_loc_indicator=' ',
                        res_name="UNK",
                        chain_id='',
                        res_seq_number=1,
                        insert_code=' ',
                        x= coordinates['x_cord'],
                        y= coordinates['y_cord'],
                        z= coordinates['z_cord'],
                        occupancy=1.0,
                        temp_factor=0.0
                    ))
    
                # Increment the global atom_counter
                atom_counter += 1
    
        print("END", file=outfile)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='match the connectivity of two PDBs for same molecule',
                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--template', metavar='pdb file', default='in.pdb',
                    help='(in) file name of the original PDB file save from cif file')
    parser.add_argument('--input', metavar='pdb file', default='template.pdb',
                    help='(in) file name of the supercell pdb file save from pymatgen cif file')
    parser.add_argument('--output', metavar='pdb file', default='out.pdb',
                    help='(out) file name for the reordered supercell molecule ')

    args = parser.parse_args()
    reorder_atoms(args.template, args.input, args.output)

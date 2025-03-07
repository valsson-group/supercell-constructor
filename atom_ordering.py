#!/usr/bin/env python

import numpy as np
from ase.io import read, write
from ase import Atoms, neighborlist
from ase.build import sort
from scipy import sparse
import argparse

def reorder_supercell(cif_input, template_pdb, pdb_output):
    """
    Function reorders the atoms for each molecule one after the other.

    Parameters:
    ----------
    cif_input : str
        CIF file of the supercell.
    template_pdb : str
        original PDB to find the unique atom lise
    pdb_output : str
        PDB file of the reordered supercell.
    """
    
    elements = []

    with open(template_pdb, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith('HETATM'):
                element = line.split()[2]  # Extract the element symbol (e.g., CL1)
                element = ''.join([char for char in element if not char.isdigit()])  # Remove digits
                if element not in elements:  # Only add if not already in the list
                    elements.append(element)
    
    print(elements)


    
    # Read the structure
    supercell = read(cif_input)

    # Determine the indices of each molecule using neighborlists
    cutoff = neighborlist.natural_cutoffs(supercell)
    nl = neighborlist.build_neighbor_list(supercell, cutoffs=cutoff)
    connmat = nl.get_connectivity_matrix(False)  # Connectivity matrix
    
    # n_components contains the number of molecules
    # component_list contains molecule number of each atom in the system
    n_components, component_list = sparse.csgraph.connected_components(connmat)

    # Sorting based on the molecule index first (`component_list`)
    # and then by chemical symbol of the atom
    # adjust the number 20 according to the size of the system if needed
    supercell_sorted = sort(
        supercell,
        tags=[(component_list[i]*20) + elements.index(s)
              for i, s in enumerate(supercell.get_chemical_symbols())]
    )

    # Write to file
    write(pdb_output, supercell_sorted)

if __name__ == '__main__':
    # Command line argument parsing
    parser = argparse.ArgumentParser(description='Reorder a supercell from a CIF file.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input', metavar='cif file', default='in.cif',
                        help='(in) file name of the original CIF file')
    parser.add_argument('--template', metavar='pdb file', default='template.pdb',
                    help='(in) pdb file name of the template molecule with the desired order')
    parser.add_argument('--output', metavar='pdb file', default='out.pdb',
                        help='(out) file name for the reordered supercell')

    # Parse arguments
    args = parser.parse_args()

    # Call the function to reorder the supercell
    reorder_supercell(args.input, args.template, args.output)


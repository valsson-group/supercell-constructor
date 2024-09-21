def split_pdb_file(file_path, lines_per_file=15):
    with open(file_path, 'r') as infile:
        lines = infile.readlines()
    
    header = lines[:5]  # First 5 lines of the original PDB file
    footer = lines[-1]  # Last line of the original PDB file
    hetatm_lines = [line for line in lines if line.startswith("HETATM")]
    
    total_hetatm_lines = len(hetatm_lines)
    num_files = (total_hetatm_lines + lines_per_file - 1) // lines_per_file  # Ceiling division
    
    for i in range(num_files):
        start_idx = i * lines_per_file
        end_idx = start_idx + lines_per_file
        subset_lines = hetatm_lines[start_idx:end_idx]
        
        output_file_path = f"{file_path.rsplit('.', 1)[0]}_part{i+1}.pdb"
        with open(output_file_path, 'w') as outfile:
            outfile.writelines(header + subset_lines + [footer])
        
        print(f"Created {output_file_path} with {len(subset_lines)} HETATM lines.")

# Usage
file_path = "1866092.pdb"
split_pdb_file(file_path, lines_per_file=15)


def read_pdb(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[:5]  # First 5 lines of the original PDB file
        footer = lines[-1]  # Last line of the original PDB file
        hetatm_lines = [line for line in lines if line.startswith("HETATM")]
    return header, hetatm_lines, footer

pdb_files = [f"file_part{i}_reorder.pdb" for i in range(1, 21)]

all_hetatm_lines = []

header, hetatm_lines, footer = read_pdb(pdb_files[0])
all_hetatm_lines.extend(hetatm_lines)

for pdb_file in pdb_files[1:]:
    _, hetatm_lines, _ = read_pdb(pdb_file)
    all_hetatm_lines.extend(hetatm_lines)

# Write the concatenated output to a new PDB file
with open('merged.pdb', 'w') as outfile:
    outfile.writelines(header)
    outfile.writelines(all_hetatm_lines)
    outfile.writelines(footer)

print("PDB files merged successfully into merged.pdb")


def get_residues_from_pdb(residues, padding, use_ca=False):
    
    x_positions = []
    y_positions = []
    z_positions = []

    for residue in residues:
        for atom in residue:
            if (use_ca and residue.get_name() == 'CA') or (use_ca == False):
                x_positions.append(atom.get_coord()[0])
                y_positions.append(atom.get_coord()[1])
                z_positions.append(atom.get_coord()[2])
    
    box_config = {
        'center_x': round(sum(x_positions) / len(x_positions), 2),
        'center_y': round(sum(y_positions) / len(y_positions), 2),
        'center_z': round(sum(z_positions) / len(z_positions), 2),
        'size_x': round(max(x_positions) - min(x_positions) + padding, 2),
        'size_y': round(max(y_positions) - min(y_positions) + padding, 2),
        'size_z': round(max(z_positions) - min(z_positions) + padding, 2)
    }

    return box_config
        

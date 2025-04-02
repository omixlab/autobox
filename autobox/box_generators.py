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
        'x_center': round(sum(x_positions) / len(x_positions), 2),
        'y_center': round(sum(y_positions) / len(y_positions), 2),
        'z_center': round(sum(z_positions) / len(z_positions), 2),
        'x_size': round(max(x_positions) - min(x_positions) + padding, 2),
        'y_size': round(max(y_positions) - min(y_positions) + padding, 2),
        'z_size': round(max(z_positions) - min(z_positions) + padding, 2)
    }

    return box_config
        
from Bio.PDB import PDBParser

def get_ligands_from_pdb(pdb_file, target_ligands, ignore_missing=False):

    residues = []
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_file)
    found_ligands = set([])
    for model in structure:
        for chain in model:
            for residue in chain:
                residue_str = '{}{}{}'.format(residue.resname, residue.get_id()[1], chain.id).upper()
                if residue_str in target_ligands:
                    found_ligands.add(residue.resname)
                    residues.append(residue)
    if ignore_missing is False:
        if len(found_ligands) < len(target_ligands):
            print('error: the following ligands were not found:', ' '.join([ligand for ligand in target_ligands if ligand not in found_ligands]))
            exit(1)
    return residues


def get_residues_from_pdb(pdb_file, target_residues, ignore_missing=True):

    residues = []
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_file)
    found_residues = set()
    for model in structure:
        for chain in model:
            for residue in chain:
                residue_str = '{}{}{}'.format(residue.resname, residue.get_id()[1], chain.id).upper()
                if residue_str in target_residues:
                    residues.append(residue)
                    found_residues.add(residue_str)
    
    if ignore_missing:
        if len(found_residues) < len(target_residues):
            print('error: the following residues were not found:', ' '.join([residue for residue in target_residues if residue not in found_residues]))
            exit(1)

    return residues

def get_all_residues_from_pdb(pdb_file):

    residues = []
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_file)

    for model in structure:
        for chain in model:
            for residue in chain:
                residues.append(residue)
    
    return residues

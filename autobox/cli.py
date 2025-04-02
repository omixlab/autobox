from argparse import ArgumentParser
from autobox import box_generators 
from autobox import pdb_reader
from autobox import output_writer

def main():

    argument_parser = ArgumentParser()
    argument_parser.add_argument("--ligands", metavar='LIGANDS', nargs="*", help="generates a box covering one or more ligands (must not be used in combination with --residues or --blind)")
    argument_parser.add_argument("--residues", metavar='RESIDUES', nargs="*", help="generates a box covering one or more residues (must not be used in combination with --ligands or --blind)")
    argument_parser.add_argument("--blind", help="generates a box covering the entire protein (must not be used in combination with --residues or --ligands)", action='store_true', default=False)
    argument_parser.add_argument("--padding", default=10, type=int, help="adds a space around the selection in the three axis (default: 10 Angstrons)")
    argument_parser.add_argument("--format", default='vina', choices=['vina'], help='output format (currently, only "vina" is available)')
    argument_parser.add_argument("--input", help='input file in PDB format', required=True)
    argument_parser.add_argument("--alpha", help='get position of the residue based on the alpha carbon (full-atom is default)', default=False, action='store_true')
    argument_parser.add_argument("--output", help='output file')


    arguments = argument_parser.parse_args()

    modes = []

    if arguments.ligands:
        modes.append("--ligands")
    
    if arguments.residues:
        modes.append("--residues")
    
    if arguments.blind:
        modes.append("--blind")
    
    if len(modes) == 0:
        print("No mode was specified")
        exit(1)
    
    if len(modes) > 1:
        print("More than one mode was specified: ", ' '.join(modes))
        exit(1)

    if modes[0] == '--ligands':
        residues = pdb_reader.get_ligands_from_pdb(arguments.input, target_ligands=[ligand.upper() for ligand in arguments.ligands])
    elif modes[0] == '--residues':
        residues = pdb_reader.get_residues_from_pdb(arguments.input, target_residues=[residue.upper() for residue in arguments.residues])

    else:
        residues = pdb_reader.get_all_residues_from_pdb(arguments.input)

    if len(residues) == 0:
        print('error: no residue or ligand was found')
        exit(1)

    box = box_generators.get_residues_from_pdb(
        residues,
        padding=arguments.padding,
        use_ca=arguments.alpha
    )
    
    if arguments.format == 'vina':
        content = output_writer.vina_output_writer(box)
        if arguments.output:
            with open(arguments.output, 'w') as writer:
                writer.write(content)
        else:
            print(content)
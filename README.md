# Autobox

A simple command line tool to generate box coodinates for Autodock Vina.

## Installing

```bash
$ pip install git+https://github.com/omixlab/autobox
```

## Usage

### Creating a box around a ligand

```bash
$ autobox --ligands VO31001A --input test/1e59.pdb --padding 5
```

### Creating a box around specific residues


```bash
$ autobox --residues VAL2A LYS4A --input test/1e59.pdb
```

### Creating a box around specific residues using only the alpha carbon


```bash
$ autobox --residues VAL2A LYS4A --input test/1e59.pdb --alpha
```

### Creating a box for the entire protein (blind docking)


```bash
$ autobox --blind --input test/1e59.pdb
```

## Note

Ligands and residues are specified using the concatenation of the `name` + `id` + `chain`. For residues, the `id` 
is the residue position inside the protein sequence. For ligands, the `id` is an arbitrary number to distinct multiple
instances of the same molecule.
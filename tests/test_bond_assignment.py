from autode import bond_lengths
from autode.molecule import Molecule


def test_bond_assignment():

    xyz_list = [['C', -2.10761, 0.73803, -0.25499],
                ['C', -2.40465, -0.75863, 0.05393],
                ['N', -1.51400, 1.39351, 0.91244],
                ['H', -0.61071, 0.92675, 1.15912],
                ['H', -1.28615, 2.38644, 0.67628],
                ['O', -1.22098, -1.42565, 0.41329],
                ['H', -0.63427, -1.45373, -0.38717],
                ['P', -3.66223, 1.66560, -0.76636],
                ['H', -3.04374, 2.97983, -0.81430],
                ['H', -4.23561, 1.74879, 0.56627],
                ['S', -3.56395, -0.94129, 1.45914],
                ['H', -4.73315, -0.78660, 0.68963],
                ['Cl', -3.10582, -1.59943, -1.37034],
                ['F', -1.21464, 0.80946, -1.31273]]

    xyz_bond_list = bond_lengths.get_xyz_bond_list(xyz_list)
    assert len(xyz_bond_list) == 13


def test_rdkit_bond_list():

    methane = Molecule(name='methane', smiles='C')
    bond_list = bond_lengths.get_bond_list_from_rdkit_bonds(methane.mol_obj.GetBonds())
    # Methane has 4 bonds
    assert len(bond_list) == 4


def test_get_ideal_bond_length_matrix():

    xyz_list = [['H', 0.0, 0.0, 0.0], ['H', 1.0, 0.0, 0.0]]
    bond_list = [(0, 1)]

    ideal_bond_length_matrix = bond_lengths.get_ideal_bond_length_matrix(xyzs=xyz_list, bonds=bond_list)
    assert ideal_bond_length_matrix.shape == (2, 2)
    assert 0.5 < ideal_bond_length_matrix[0, 1] < 1.0   # Å


def test_avg_bond_lengths():

    methane = Molecule(name='methane', smiles='C')

    # Methane has 4 bonds
    assert 1.0 < bond_lengths.get_avg_bond_length(mol=methane, bond=(0, 1)) < 1.5
    assert 1.0 < bond_lengths.get_avg_bond_length(atom_i_label='C', atom_j_label='H') < 1.5

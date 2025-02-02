import mbuild as mb
import pytest

from flowermd.library import (
    PEEK,
    PPS,
    LJChain,
    PEKK_meta,
    PEKK_para,
    PolyEthylene,
)


class TestPolymers:
    def test_pps_n_particles(self):
        chain = PPS(lengths=5, num_mols=1)
        monomer = mb.load(chain.smiles, smiles=True)
        assert chain.n_particles == (monomer.n_particles * 5) - 8

    def test_polyethylene(self):
        chain = PolyEthylene(lengths=5, num_mols=1)
        monomer = mb.load(chain.smiles, smiles=True)
        assert chain.n_particles == (monomer.n_particles * 5) - 8

    def test_pekk_meta(self):
        chain = PEKK_meta(lengths=5, num_mols=1)
        monomer = mb.load(chain.smiles, smiles=True)
        assert chain.n_particles == (monomer.n_particles * 5) - 8

    def test_pekk_para(self):
        chain = PEKK_para(lengths=5, num_mols=1)
        monomer = mb.load(chain.smiles, smiles=True)
        assert chain.n_particles == (monomer.n_particles * 5) - 8

    @pytest.mark.skip()
    def test_peek(self):
        chain = PEEK(lengths=5, num_mols=1)
        monomer = mb.load(chain.smiles, smiles=True)
        assert chain.n_particles == (monomer.n_particles * 5) - 8

    def test_lj_chain(self):
        cg_chain = LJChain(
            lengths=3,
            num_mols=1,
            bead_sequence=["A"],
            bead_mass={"A": 100},
            bond_lengths={"A-A": 1.5},
        )
        assert cg_chain.n_particles == 3
        assert cg_chain.molecules[0].mass == 300

    def test_lj_chain_sequence(self):
        cg_chain = LJChain(
            lengths=3,
            num_mols=1,
            bead_sequence=["A", "B"],
            bead_mass={"A": 100, "B": 150},
            bond_lengths={"A-A": 1.5, "A-B": 1.0},
        )
        assert cg_chain.n_particles == 6
        assert cg_chain.molecules[0].mass == 300 + 450

    def test_lj_chain_sequence_bonds(self):
        LJChain(
            lengths=3,
            num_mols=1,
            bead_sequence=["A", "B"],
            bead_mass={"A": 100, "B": 150},
            bond_lengths={"A-A": 1.5, "A-B": 1.0},
        )

        LJChain(
            lengths=3,
            num_mols=1,
            bead_sequence=["A", "B"],
            bead_mass={"A": 100, "B": 150},
            bond_lengths={"A-A": 1.5, "B-A": 1.0},
        )

    def test_lj_chain_sequence_bad_bonds(self):
        with pytest.raises(ValueError):
            LJChain(
                lengths=3,
                num_mols=1,
                bead_sequence=["A", "B"],
                bead_mass={"A": 100, "B": 150},
                bond_lengths={"A-A": 1.5},
            )

    def test_lj_chain_sequence_bad_mass(self):
        with pytest.raises(ValueError):
            LJChain(
                lengths=3,
                num_mols=1,
                bead_sequence=["A", "B"],
                bead_mass={"A": 100},
                bond_lengths={"A-A": 1.5},
            )

    def test_copolymer(self):
        pass

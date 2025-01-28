"""Main entry point for the application."""

import numpy as np

MAX_QUALITY_RARE = 3
MAX_QUALITY_EPIC = 4
MAX_QUALITY_LEGENDARY = 5


def make_green_circuit():
    """Make a green circuit."""
    print("Made a green circuit.")


def get_quality_matrix(base_quality: float, size: int) -> np.ndarray:
    """Generate a quality matrix based on the base quality."""
    if not (MAX_QUALITY_RARE <= size <= MAX_QUALITY_LEGENDARY):
        raise ValueError(f"Size must be between {MAX_QUALITY_RARE} and {MAX_QUALITY_LEGENDARY}.")

    quality_matrix = np.zeros((size, size))
    for col in range(size):
        for row in range(col + 1, size):
            quality_matrix[row, col] = base_quality * 10 ** (col - row + 1)
        quality_matrix[col, col] = 1 - np.sum(quality_matrix[:, col])

    return quality_matrix


def main():
    """Main entry point for the application."""
    size = MAX_QUALITY_EPIC
    material_fractions = np.zeros((size, 1))
    material_fractions[1] = 1000.
    final_output = np.zeros_like(material_fractions)
    q_recycler = get_quality_matrix(0.047 * 4, size)
    q_em_plant = get_quality_matrix(0.047 * 5, size)
    prod_recycler = 0.25
    prod_em_plant = 1.50

    n_iters = 10
    for i in range(n_iters):
        material_fractions = np.dot(q_recycler, material_fractions) * prod_recycler
        material_fractions = np.dot(q_em_plant, material_fractions) * prod_em_plant
        final_output[-1] += material_fractions[-1]
        material_fractions[-1] = 0
    print(final_output)


if __name__ == "__main__":
    main()

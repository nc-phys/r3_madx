# R3 MAD-X Simulation

Simulation framework utilising [cpymad](https://github.com/hibtc/cpymad) for modelling the Rare Radioisotope Ring (R3) at RIKEN.
Code adapted from work by Y. Yamaguchi & [G. Hudson-Chang](https://github.com/gwgwhc/r3_madx).

#### Installation

Setup venv & install requirements in `requirements.txt` through the `makefile` or through whatever method you'd prefer:

`$ make init`

#### Usage

Activate venv by sourcing activation script:

`$ source .env/bin/activate`

Typical usage flow would be:

- Modify R3 & Beam configuration in `src/config/config.py`.
- Modify `R3MADX()` child class within `src/R3MADX` by modifying the `R3Mutate()`, `R3Review()` and `R3Run()` parent classes.
`R3MADX()` will inherit changes through [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance) so keep that in mind when naming methods to avoid naming conflicts due to [Method Resolution Order](https://docs.python.org/3/howto/mro.html).
- Modify and run `main.py` to execute `R3MADX()` methods or directly call `cpymad`.

Data & plots are recommended to be output to the `data/` folder.

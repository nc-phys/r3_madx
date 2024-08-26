# RIKEN's R3 MAD-X Simulation

Program utilising [cpymad](https://github.com/hibtc/cpymad) to simulate the Rare Radioisotope Ring (R3) at RIKEN.
Code adapted from work by Y. Yamaguchi & [G. Hudson-Chang](https://github.com/gwgwhc/r3_madx).

### Usage

Setup venv & install requirements in requirements.txt with makefile or whatever method you'd like:

`$ make init`

Activate venv by sourcing activation script:

`$ source .env/bin/activate`

Modify R3 & Beam configuration in `config.py` and then run `main.py`.
Data & plots are outputted into the `data/` folder.

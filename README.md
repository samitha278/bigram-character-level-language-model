# Bigram Character-Level Language Model

A simple character-level bigram language model built with PyTorch.  
It can train on a dataset of names/words and then generate new samples character by character.

---

## Features
- Text generation in **two ways**:
  1. From **statistics & counts** (bigram frequency table)  
  2. From a **neural network** trained with PyTorch  
- Train on any text dataset (e.g. names.txt)  
- Generate new words/names character by character  
- Includes scripts for training, generation, and basic analysis  

---

## Project Structure
- `data/` – dataset (e.g. names.txt)  
- `notebooks/` – Jupyter notebook with experiments  
- `src/` – source code  
  - `bigram_stats.py` – text generation using bigram statistics  
  - `bigram_nn.py` – neural network bigram model  
  - `train_nn.py` – training script for NN  
  - `generate.py` – text generation with NN  
  - `test.py` – quick tests  

---


cd bigram-character-level-language-model
pip install -r requirements.txt

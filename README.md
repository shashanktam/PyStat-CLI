# PyStat-CLI: Statistical Analysis Toolkit

**A lightweight, modular command-line tool for statistical analysis and probability calculations, built entirely in Python.**

## Project Overview:
PyStat-CLI is a custom-built library designed to perform statistical operations without relying on external dependencies like NumPy or SciPy. The goal of this project is to demonstrate a low-level understanding of statistical algorithms by implementing them from scratch.

It currently supports descriptive statistics (Mean, Variance) with plans to expand into probability distributions and hypothesis testing.

## Features:
- **Zero Dependencies:** Built using only Python's standard library.
- **Descriptive Statistics:** - Arithmetic Mean
  - Sample Variance (using Bessel's Correction $n-1$)
- **Interactive CLI:** Simple text-based interface for easy usage.
- **Modular Architecture:** Logic is separated from the interface (`statistics_utils.py`), making the code testable and reusable.

## Prerequisites
- Python 3.x installed on your system.

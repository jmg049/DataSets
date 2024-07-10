# MM Data Set Downloader

A collection of scripts for downloading various multimodal datasets used as part of my PhD research.

## Installation

You can install this package using pip:
```
pip install git+https://github.com/jmg049/DataSets.git
```

## Usage

After installation, you can use the `mm_dataset` command-line tool:

Options:
- `--dataset`: Dataset to download (choices are: ["mmimdb", "avmnist", "kinetics-sounds"])
- `--download_dir`: Directory to save the dataset (default: "data")
- `--unzip`: Unzip the resulting download file. Default: False
- `--del_zip`: Flag indicating the zip file should be deleted after unzipping. Default: False

## Available Datasets

Currently, the following datasets are supported:

- MMIMDb: Multimodal IMDb dataset
- Kinetics-Sounds
- AVMNIST

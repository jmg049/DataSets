# MM Data Set Downloader

A Python library for downloading various multimodal datasets used in machine learning research. This tool simplifies the process of obtaining datasets for multimodal analysis and experimentation.

## Installation

You can install this package using pip:

```bash
pip install git+https://github.com/jmg049/DataSets.git
```

## Usage
After installation, you can use the mm_dataset command-line tool:
```bash
mm_dataset --dataset DATASET_NAME [--download_dir DOWNLOAD_DIR] [--unzip] [--del_zip]
```

## Options


``--dataset``: Required. Dataset to download. Choices are: ``["mmimdb"
"avmnist"
"kinetics-sounds"
"mosi"
"mosei"
"msp-improv"
"iemocap"
"genspeech"
"tcd_voip"
"audioset_urban_rural"]``


``--download_dir``: Directory to save the dataset (default: "data")

``--unzip``: Flag to unzip the downloaded file (default: False)

``--del_zip``: Flag to delete the zip file after unzipping (default: False)

## Available Datasets
The following datasets are supported:

- MMIMDb: Multimodal IMDb dataset
- AVMNIST: Audio-Visual MNIST dataset
- Kinetics-Sounds: Audio-visual dataset for action recognition
- MOSI: Multimodal Opinion Sentiment Intensity dataset
- MOSEI: Multimodal Opinion Sentiment and Emotion Intensity dataset
- MSP-IMPROV: Multimodal database of improvisational emotional dyadic interactions
- IEMOCAP: Interactive Emotional Dyadic Motion Capture database
- GenSpeech: Generated Speech dataset 
- TCD-VOIP: Voice Over IP Quality dataset
- AudioSet Urban-Rural: Urban and rural sounds from AudioSet (wav only)

## Example
To download the MMIMDb dataset and save it in the "data" directory:
```bash
mm_dataset --dataset mmimdb --download_dir data --unzip --del_zip
```
This command will download the MMIMDb dataset, unzip it in the "data" directory, and delete the original zip file.


## License
This project is licensed under the MIT License.
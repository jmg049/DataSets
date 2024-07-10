from enum import Enum
from argparse import ArgumentParser, Namespace
import os
from pathlib import Path
from typing import Union

import gdown

MM_IMDB_URL = (
    "https://drive.google.com/uc?export=download&id=1rdB2HpsGn0dI_9fD1MQt82Qa8D8RVLFM"
)


def parse_args() -> Namespace:
    parser = ArgumentParser("Tool for downloading multimodal datasets")
    parser.add_argument(
        "--download_dir", type=str, default="data", help="Directory to save the dataset"
    )
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Dataset to download",
        choices=["mmimdb"],
    )
    parser.add_argument("--unzip", action="store_true", help="Flag indicating whether the downloaded zip should be unzipped.")
    return parser.parse_args()


class DataSet(Enum):
    MMIMDb = "mmimdb"
    INVALID = None

    def __str__(self):
        return self.value

    @staticmethod
    def from_string(label: str):
        label = label.lower()
        for ds in DataSet:
            if str(ds) == label:
                return ds
        return DataSet.INVALID


def download_dataset(dataset: DataSet, download_dir: Union[str, Path, os.PathLike]):

    if not isinstance(download_dir, Path):
        download_dir = Path(download_dir)

    os.makedirs(download_dir, exist_ok=True)

    match dataset:
        case DataSet.MMIMDb:
            gdown.download(MM_IMDB_URL, str(download_dir / "mmimdb.zip"))
        case DataSet.INVALID:
            raise ValueError("Invalid dataset")


def main():
    args = parse_args()
    download_dataset(DataSet.from_string(args.dataset), args.download_dir)
    
    if args.unzip:
        import zipfile
        data_name = os.path.join(args.download_dir, f"{args.dataset}.zip")
        print(f"Unzipping: {data_name}")
        with zipfile.ZipFile(data_name, "r") as zip_ref:
            zip_ref.extractall(args.download_dir)

if __name__ == "__main__":
    main()
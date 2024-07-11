from enum import Enum
from argparse import ArgumentParser, Namespace
import os
from pathlib import Path
from typing import Union

import gdown

MM_IMDB_URL = (
    "https://drive.google.com/uc?export=download&id=1rdB2HpsGn0dI_9fD1MQt82Qa8D8RVLFM"
)

AVMNIST_URL = (
    "https://drive.google.com/uc?export=download&id=1DMPiR6SckrgpycsiaeyIzDENTRGej3o3"
)
KINETICS_SOUNDS_URL = (
    "https://drive.google.com/uc?export=download&id=1KNORgh7AIpPHUYd9M_CTyABDtt74UUyd"
)

MOSI_URL = ""
MOSEI_URL = (
    "https://drive.google.com/uc?export=download&id=1KZTYSoPjk1k9SEQ4YfbeURPPMXtcdjog"
)
MSP_IMPROV_URL = "https://drive.google.com/file/d/1TayFFgVFTl8HlYjOak8zRXr4-t1yu2Xh/view?usp=drive_link"
IEMOCAP_URL = "https://drive.google.com/file/d/1W1k-_-VmE1CmHrzcAmEkAQvxKTJcOoh8/view?usp=drive_link"


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
        choices=[
            "mmimdb",
            "avmnist",
            "kinetics-sounds",
            "mosi",
            "mosei",
            "msp-improv",
            "iemocap",
        ],
    )
    parser.add_argument(
        "--unzip",
        action="store_true",
        help="Flag indicating whether the downloaded zip should be unzipped.",
    )
    parser.add_argument(
        "--del_zip",
        action="store_true",
        help="Can be used alongside the unzip flag to also delete the orignal downloaded zip.",
    )
    return parser.parse_args()


class DataSet(Enum):
    MMIMDb = "mmimdb"
    AVMNIST = "avmnist"
    KINETICS_SOUNDS = "kinetics-sounds"
    MOSI = "cmu-mosi"
    MOSEI = "cmu-mosei"
    MSP_IMPROV = "msp-improv"
    IEMOCAP = "iemocap"
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
            gdown.download(
                MM_IMDB_URL, str(download_dir / f"{str(DataSet.MMIMDb)}.zip")
            )
        case DataSet.AVMNIST:
            gdown.download(
                AVMNIST_URL, str(download_dir / f"{str(DataSet.AVMNIST)}.zip")
            )
        case DataSet.KINETICS_SOUNDS:
            gdown.download(
                KINETICS_SOUNDS_URL,
                str(download_dir / f"{str(DataSet.KINETICS_SOUNDS)}.zip"),
            )
        case DataSet.MOSI:
            gdown.download(MOSI_URL, str(download_dir / f"{str(DataSet.MOSI)}.zip"))
        case DataSet.MOSEI:
            gdown.download(MOSEI_URL, str(download_dir / f"{str(DataSet.MOSEI)}.zip"))
        case DataSet.MSP_IMPROV:
            gdown.download(
                MSP_IMPROV_URL, str(download_dir / f"{str(DataSet.MSP_IMPROV)}.zip")
            )
        case DataSet.IEMOCAP:
            gdown.download(
                IEMOCAP_URL, str(download_dir / f"{str(DataSet.IEMOCAP)}.zip")
            )

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

        if args.del_zip:
            os.remove(f"{args.download_dir}/{args.dataset}.zip")

    ## cleap up any ".part" files
    for f in [
        os.path.join(args.download_dir, f) for f in os.listdir(args.download_dir)
    ]:
        if Path(f).stem == "part":
            print(f"Removing: {f}")
            os.remove(f)


if __name__ == "__main__":
    main()

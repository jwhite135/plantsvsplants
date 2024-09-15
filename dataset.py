import fiftyone as fo

session = fo.launch_app()

name = "plants7"
dataset_dir = "/home/josiahaw/python/data/plants/train"

dataset = fo.Dataset.from_dir( 
    dataset_dir=dataset_dir,
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    name=name,
)
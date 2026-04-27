from pathlib import Path
import json, os, yaml


# function to convert COCO annotations to YOLO format
def coco_to_yolo(coco_json, labels_dir):
    labels_dir = Path(labels_dir); labels_dir.mkdir(parents=True, exist_ok=True)
    data = json.load(open(coco_json))
    cats = {c["id"]: i for i, c in enumerate(sorted(data["categories"], key=lambda x: x["id"]))}
    imgs = {img["id"]: img for img in data["images"]}
    anns_by_img = {}
    for ann in data["annotations"]:
        if "bbox" not in ann or ann.get("iscrowd", 0) == 1:
            continue
        anns_by_img.setdefault(ann["image_id"], []).append(ann)

    for img_id, img in imgs.items():
        w, h = img["width"], img["height"]
        out = []
        for ann in anns_by_img.get(img_id, []):
            x, y, bw, bh = ann["bbox"]
            xc, yc = (x + bw / 2) / w, (y + bh / 2) / h
            out.append(f'{cats[ann["category_id"]]} {xc:.6f} {yc:.6f} {bw/w:.6f} {bh/h:.6f}')
        (labels_dir / (Path(img["file_name"]).stem + ".txt")).write_text("\n".join(out))


# use current script directory as base dir
base_dir = os.path.join(os.path.dirname(__file__), "data")

# Create YOLO labels for train, val, and test sets
coco_to_yolo(os.path.join(base_dir, "train.json"), os.path.join(base_dir, "train"))
coco_to_yolo(os.path.join(base_dir, "val.json"), os.path.join(base_dir, "val"))
coco_to_yolo(os.path.join(base_dir, "test.json"), os.path.join(base_dir, "test")) 

print("generated YOLO text files in the folders train, val, and test.")


# Load class names from train.json
with open(os.path.join(base_dir, "train.json"), 'r') as f:
    train_data = json.load(f)

class_names = {i: cat["name"] for i, cat in enumerate(sorted(train_data["categories"], key=lambda x: x["id"]))}


# Create data.yaml for YOLO training (yaml might be not needed depending on the framework)
data_yaml = {
    "path": base_dir,
    "train": "train",
    "val": "val",
    "names": class_names
}

with open(os.path.join(base_dir, "yolo.yaml"), "w") as f:
    yaml.dump(data_yaml, f, allow_unicode=True)

print("generated yaml file at:", os.path.join(base_dir, "yolo.yaml"))

# Data

```
cd data
```

load `dataset.json` into `workspace`:

```
python -m management.unpacker
```

save `workspace` to `dataset.json`

```
python -m management.packer
```

# Get Structure (Version 1.0)

One shot, without revise iteration:

```
python get_structure_v1.py
```

With revise iteration:

```
python get_structure_with_revise_iteration.py
```
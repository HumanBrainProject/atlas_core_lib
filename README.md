# Ebrains Atlascore python library 

This library is a wrapper for the [ebrains atlascore](https://ebrains-atlascore.apps.hbp.eu/) REST API

Author: Vadim Marcenko

## Installation

`pip install ebrains-atlascore`

## Basic setup

The library is using the latest production version of the Atlascore API.
If you want to use a development version you have to set it as an environment variable:

`export ATLASCORE_ENV=DEV`

## Basic Usage with examples

Get all referencespaces known by the atlas-core:

```python
from ebrains_atlascore import referencespaces
ref_spaces = referencespaces.get_all_referencespaces()
print(ref_spaces)
```

Get a single referencespace by a given name:

```python
from ebrains_atlascore import referencespaces
mni152_ref_space = referencespaces.get_referencespace_by_name('MNI152')
print(mni152_ref_space.parcellations)
```

Get all parcellations for a referencespace name:

```python
from ebrains_atlascore import parcellations
parcellations_in_mni152 = parcellations.get_all_parcellations('MNI152')
print(parcellations_in_mni152)
```

Get a single parcellation for a reference name:

```python
from ebrains_atlascore import parcellations
jubrain_in_mni152 = parcellations.get_parcellation_by_name('MNI152', 'JuBrain Cytoarchitectonic Atlas')
print(jubrain_in_mni152)
```

Get all regions for a parcellation in a referencespace:

```python
from ebrains_atlascore import regions
colin_jubrain_re = regions.get_all_regions('colin', 'JuBrain Cytoarchitectonic Atlas')
print(colin_jubrain_re)
```

Get a single region for a parcellation in a referencespace:

```python
from ebrains_atlascore import regions
fp1_left_colin = regions.get_region_by_name('colin', 'JuBrain Cytoarchitectonic Atlas', 'Area Fp1 (FPole) - left hemisphere')
print(fp1_left_colin)
```

Retrieve a probability map for a region as a ROI:
```python
from ebrains_atlascore import regions
from ebrains_atlascore.util.hemisphere import Hemisphere
from ebrains_atlascore.region import Region
pmap = regions.get_probability_map_for_region(Region('Area-Fp1', 'colin', 'JuBrain Cytoarchitectonic Atlas'), Hemisphere.LEFT.value, 0.2)
print(pmap)
```

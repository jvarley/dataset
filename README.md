# dset
Code related to creating and using datasets for machine learning.  My datasets tend to be on the order of 10s to 100s of GB, to big to fit in memory, but still able to fit on a single HD. 

I store my data as flat files in /srv/data
ex: /srv/data/shape_completion_data

I put my dataset in /srv/datasets
The datasets have the following structure:
```
DATSET_NAME:
  - split0.txt
     x0.pcd, y0.pcd
     x1.pcd, y1.pcd
     ...
     
  - split1.txt
     x0.pcd, y0.pcd
     x1.pcd, y1.pcd
     ...
     
   - split2.txt
     x0.pcd, y0.pcd
     x1.pcd, y1.pcd
     ...
     
  - info.yaml
    {
    patch_size: 40,
     ...
     }
```


